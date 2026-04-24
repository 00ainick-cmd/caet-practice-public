"""Render the handbook.html artifact for one module from extracted source JSON."""
import json, sys
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

tpl_dir = Path(__file__).parent / "templates"
env = Environment(loader=FileSystemLoader(tpl_dir))
tpl = env.get_template("handbook.html.j2")

src_path, out_path = Path(sys.argv[1]), Path(sys.argv[2])
src = json.load(src_path.open("r", encoding="utf-8"))
html = tpl.render(
    title=src["title"],
    intro=src["intro"],
    knowledge=src["knowledge_requirements"],
    tasks=src["tasks"],
    oral=src["oral_board_questions"],
)
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(html, encoding="utf-8")
print(f"Wrote {out_path}")
