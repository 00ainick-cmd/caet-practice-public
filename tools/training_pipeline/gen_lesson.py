"""Render the 5E interactive lesson.html for one module, merging enrichment content."""
import json, sys
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))
from merge import effective_tasks, effective_oral, effective_intro

def load_enrichment(slug):
    f = SCRIPT_DIR / "enrichment" / f"{slug}.json"
    if f.exists():
        return json.load(f.open("r", encoding="utf-8"))
    return {
        "why_this_matters": [],
        "key_terms": [],
        "knowledge_enrichment": {},
        "task_enrichment": {},
        "background_theory": {},
    }

def infer_slug(src_path):
    name = src_path.stem
    if "_" in name:
        return name.split("_")[0]
    return name

def main():
    src_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])
    slug = None
    for arg in sys.argv[3:]:
        if arg.startswith("--slug="):
            slug = arg.split("=", 1)[1]
    if slug is None:
        slug = infer_slug(src_path)

    src = json.load(src_path.open("r", encoding="utf-8"))
    enrichment = load_enrichment(slug)

    env = Environment(loader=FileSystemLoader(SCRIPT_DIR / "templates"))
    tpl = env.get_template("lesson.html.j2")
    html = tpl.render(
        title=src["title"],
        intro=effective_intro(src, enrichment),
        knowledge=src["knowledge_requirements"],
        tasks=effective_tasks(src, enrichment),
        oral=effective_oral(src, enrichment),
        enrichment=enrichment,
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")
    print(f"Wrote {out_path}")

if __name__ == "__main__":
    main()
