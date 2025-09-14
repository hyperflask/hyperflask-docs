from uilibspec_binding_generator.transformers.jinja import JinjaMacroTagsMarkdownTransformer
import os


class HyperflaskDocTransformer(JinjaMacroTagsMarkdownTransformer):
    name = "hyperflask_doc"
    sections = {
        "actions": "Actions",
        "data-display": "Data display",
        "navigation": "Navigation",
        "feedback": "Feedback",
        "data-input": "Data input",
        "layout": "Layout",
    }

    def transform_intro(self, component):
        return "---\nhide: [navigation, footer]\n---\n" + super().transform_intro(component)
    
    def generate_component_link(self, name):
        return f"[{name}](/components/daisyui/{name})"
    
    def write_manifest(self, components, outdir):
        tables = {s: [] for s in self.sections.keys()}
        for com in sorted(components, key=lambda c: c.name):
            if com.doc and com.doc.hidden:
                continue
            desc = ((com.doc.description if com.doc else None) or "").split("\n")[0]
            tables[os.path.dirname(com.filename)].append(f"| [{com.name}](/components/daisyui/{com.name}) | {desc} |")

        doc = ["---\nhide: [footer]\n---",
               "# DaisyUI components\n",
               "List of available components from DaisyUI\n"]
        
        for section, title in self.sections.items():
            if not tables[section]:
                continue
            doc.append(f"## {title}\n")
            doc.append("| Component | Description |\n|-----------|-------------|")
            doc.extend(tables[section])
            doc.append("\n")

        with open(os.path.join(outdir, "index.md"), "w") as f:
            f.write("\n".join(doc))