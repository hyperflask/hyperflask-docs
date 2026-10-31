"""MkDocs hook publishing the hyperflask agent skill under /.well-known/agent-skills/
so that it can be installed using `npx skills add https://hyperflask.dev`.

The skill is made of agent-skill/SKILL.md, followed by a generated list of references.
References are the documentation pages listed in the llmstxt-md plugin sections, as well as
the DaisyUI component pages.
"""

import json
import posixpath
import re
import shutil
from pathlib import Path

import yaml


SKILL_NAME = "hyperflask"
SKILL_DIR = Path(__file__).parent / "agent-skill"
WELL_KNOWN_DIR = ".well-known/agent-skills"
EXTRA_REFERENCES_DIRS = ["components/daisyui"]

frontmatter_re = re.compile(r"\A---\n.*?\n---\n", re.S)
absolute_link_re = re.compile(r"\]\((/[^)\s]*)\)")
title_re = re.compile(r"^# (.+)$", re.M)


def on_post_build(config):
    docs_dir = Path(config.docs_dir)
    sections = config.plugins["llmstxt-md"].config["sections"]

    references = {}  # docs path -> markdown content
    for pages in sections.values():
        for src_path in pages:
            references[src_path] = read_page(docs_dir / src_path)
    for dirname in EXTRA_REFERENCES_DIRS:
        for filename in sorted((docs_dir / dirname).glob("*.md")):
            references.setdefault(f"{dirname}/{filename.name}", read_page(filename))

    out_dir = Path(config.site_dir) / WELL_KNOWN_DIR
    skill_dir = out_dir / SKILL_NAME
    if skill_dir.exists():
        shutil.rmtree(skill_dir)

    files = ["SKILL.md"]
    for src_path, content in references.items():
        ref_path = f"references/{src_path}"
        write_file(skill_dir / ref_path, rewrite_links(content, ref_path, references, config.site_url))
        files.append(ref_path)

    skill = (SKILL_DIR / "SKILL.md").read_text().rstrip() + "\n"
    for section, pages in sections.items():
        skill += f"\n### {section}\n\n"
        for src_path in pages:
            skill += f"- [{page_title(references[src_path])}](references/{src_path})\n"
    write_file(skill_dir / "SKILL.md", skill)

    frontmatter = yaml.safe_load(frontmatter_re.match(skill).group(0).strip("-\n"))
    index = {"skills": [{
        "name": SKILL_NAME,
        "description": frontmatter["description"],
        "files": files,
    }]}
    write_file(out_dir / "index.json", json.dumps(index, indent=2))


def read_page(filename):
    return frontmatter_re.sub("", filename.read_text(), count=1).lstrip()


def page_title(content):
    match = title_re.search(content)
    return match.group(1).strip() if match else None


def rewrite_links(content, ref_path, references, site_url):
    """Make links to other references relative so that they can be followed inside the skill,
    and links to other pages absolute.
    """
    def replace(match):
        path, _, anchor = match.group(1).partition("#")
        path = path.strip("/")
        for candidate in (f"{path}.md", f"{path}/index.md" if path else "index.md"):
            if candidate in references:
                url = posixpath.relpath(f"references/{candidate}", posixpath.dirname(ref_path))
                break
        else:
            url = site_url.rstrip("/") + match.group(1)
            anchor = None
        return f"]({url}#{anchor})" if anchor else f"]({url})"

    return absolute_link_re.sub(replace, content)


def write_file(filename, content):
    filename.parent.mkdir(parents=True, exist_ok=True)
    filename.write_text(content)
