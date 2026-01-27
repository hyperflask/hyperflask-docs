import json
import os
import re
import shutil
from pathlib import Path

from mkdocs.plugins import BasePlugin


class HyperflaskPlugin(BasePlugin):
    def on_post_build(self, config):
        """Copy agent-skills folder and process @INCLUDE statements in SKILL.md files."""
        # Get paths
        repo_root = Path(config.config_file_path).parent
        agent_skills_src = repo_root / "agent-skills"
        docs_src = repo_root / "docs"
        build_dir = Path(config.site_dir)
        agent_skills_dest = build_dir / "agent-skills"
        
        # Copy agent-skills folder to build directory
        if agent_skills_src.exists():
            if agent_skills_dest.exists():
                shutil.rmtree(agent_skills_dest)
            shutil.copytree(agent_skills_src, agent_skills_dest)
            
            # Process all SKILL.md files and collect skill metadata
            skills = []
            for skill_file in sorted(agent_skills_dest.rglob("SKILL.md")):
                self._process_skill_file(skill_file, docs_src)
                skill_metadata = self._extract_skill_metadata(skill_file)
                if skill_metadata:
                    skills.append(skill_metadata)
            
            # Write skills.json file
            skills_json_path = agent_skills_dest / "skills.json"
            with open(skills_json_path, "w", encoding="utf-8") as f:
                json.dump(skills, f, indent=2, ensure_ascii=False)
    
    def _process_skill_file(self, skill_file: Path, docs_src: Path):
        """Process @INCLUDE statements in a SKILL.md file."""
        content = skill_file.read_text(encoding="utf-8")
        
        # Find and replace all @INCLUDE statements
        def replace_include(match):
            include_path = match.group(1).strip()
            include_file = docs_src / include_path
            
            if include_file.exists():
                file_content = include_file.read_text(encoding="utf-8")
                # Strip frontmatter (content between --- markers at the start)
                file_content = self._strip_frontmatter(file_content)
                return file_content
            else:
                # If file not found, return the original statement
                return match.group(0)
        
        # Replace @INCLUDE(...) statements
        processed_content = re.sub(
            r"@INCLUDE\s*\(\s*([^)]+)\s*\)",
            replace_include,
            content
        )
        
        skill_file.write_text(processed_content, encoding="utf-8")
    
    def _strip_frontmatter(self, content: str) -> str:
        """Remove YAML frontmatter from markdown content."""
        # Check if content starts with ---
        if content.startswith("---"):
            # Find the closing --- (second occurrence)
            lines = content.split("\n")
            if len(lines) > 1:
                # Look for the closing --- after the first one
                for i in range(1, len(lines)):
                    if lines[i].strip() == "---":
                        # Remove everything up to and including this line
                        return "\n".join(lines[i + 1:]).lstrip("\n")
        
        return content
    
    def _extract_skill_metadata(self, skill_file: Path) -> dict:
        """Extract name and description from SKILL.md frontmatter."""
        content = skill_file.read_text(encoding="utf-8")
        
        if not content.startswith("---"):
            return None
        
        lines = content.split("\n")
        frontmatter = {}
        
        # Extract frontmatter
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                # End of frontmatter
                break
            
            # Parse YAML-like key: value format
            if ":" in lines[i]:
                key, value = lines[i].split(":", 1)
                frontmatter[key.strip()] = value.strip().strip("'\"")
        
        if "name" not in frontmatter:
            return None
        
        # Construct URL based on folder structure
        relative_path = skill_file.parent.relative_to(skill_file.parent.parent)
        url = f"https://hyperflask.dev/agent-skills/{relative_path}/"
        
        return {
            "name": frontmatter.get("name"),
            "description": frontmatter.get("description", ""),
            "url": url
        }