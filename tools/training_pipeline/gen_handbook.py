"""Render the handbook.html + handbook.pdf artifacts for one module from extracted source JSON.

HTML is rendered via Jinja2. PDF is printed from the HTML using Microsoft Edge
headless mode (Windows-native substitute for weasyprint, which requires GTK3).
"""
import json, sys, subprocess, tempfile, time
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

# PDF generation via Edge headless (Windows-native alternative to weasyprint).
# Edge requires absolute paths for both --print-to-pdf target and the input URL.
html_abs = out_path.resolve()
pdf_abs = html_abs.with_suffix(".pdf")
edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
try:
    # Isolate in a temp user-data-dir so we don't collide with the user's browser session.
    with tempfile.TemporaryDirectory(prefix="edge-pdf-") as tmp_profile:
        subprocess.run([
            edge_exe,
            "--headless=new",
            "--disable-gpu",
            f"--user-data-dir={tmp_profile}",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_abs}",
            html_abs.as_uri(),
        ], check=True, timeout=60, capture_output=True)
        # Windows file writes are async; give Edge a moment to flush.
        for _ in range(10):
            if pdf_abs.exists():
                break
            time.sleep(0.2)
    if not pdf_abs.exists():
        raise RuntimeError("Edge returned 0 but PDF was not created")
    print(f"Wrote {pdf_abs}")
except Exception as e:
    print(f"PDF generation failed: {e}")
