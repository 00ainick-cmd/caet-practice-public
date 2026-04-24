"""Render the 5E interactive lesson.html for one module."""
import json, sys
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

tpl_dir = Path(__file__).parent / "templates"
env = Environment(loader=FileSystemLoader(tpl_dir))
tpl = env.get_template("lesson.html.j2")

src_path, out_path = Path(sys.argv[1]), Path(sys.argv[2])
src = json.load(src_path.open("r", encoding="utf-8"))

engage = "Before we start, think about this: What's the single most common mistake a new technician makes in this module's tasks?"
explore = "Read through the first two task preparation guides below. Notice how the evaluator is watching for specific physical evidence of correct technique."

html = tpl.render(
    title=src["title"],
    engage_prompt=engage,
    explore_prompt=explore,
    knowledge=src["knowledge_requirements"],
    tasks=src["tasks"],
)
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(html, encoding="utf-8")
print(f"Wrote {out_path}")
