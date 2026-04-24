"""Render the handbook.html + handbook.pdf artifacts for one module.

Usage: python gen_handbook.py <source.json> <output.html> [--slug=advN]

HTML is rendered via Jinja2 using the light-theme template.
Enrichment content is loaded from enrichment/<slug>.json if present.
PDF is printed from the HTML using Microsoft Edge headless mode (Windows-
native substitute for weasyprint, which requires GTK3 runtime).
"""
import json, sys, subprocess, tempfile, time
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))
from merge import effective_tasks, effective_oral, effective_intro

def load_enrichment(slug):
    f = SCRIPT_DIR / "enrichment" / f"{slug}.json"
    if f.exists():
        return json.load(f.open("r", encoding="utf-8"))
    # Empty skeleton so the template's {{ enrichment.foo }} lookups don't error.
    return {
        "why_this_matters": [],
        "key_terms": [],
        "knowledge_enrichment": {},
        "task_enrichment": {},
        "oral_board_answers": {},
        "background_theory": {},
    }

def infer_slug(src_path):
    """Extract 'advN' from staging filename like adv10_source.json."""
    name = src_path.stem
    if "_" in name:
        return name.split("_")[0]
    return name

def render_pdf(html_path):
    """Print HTML to PDF via Edge headless in an isolated profile."""
    html_abs = html_path.resolve()
    pdf_abs = html_abs.with_suffix(".pdf")
    edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    # TemporaryDirectory(ignore_cleanup_errors=...) added in 3.10; if absent, fall back.
    tmp_kwargs = {"prefix": "edge-pdf-"}
    try:
        tmp_kwargs["ignore_cleanup_errors"] = True
        tmp_profile = tempfile.TemporaryDirectory(**tmp_kwargs)
    except TypeError:
        tmp_kwargs.pop("ignore_cleanup_errors")
        tmp_profile = tempfile.TemporaryDirectory(**tmp_kwargs)
    try:
        subprocess.run([
            edge_exe,
            "--headless=new",
            "--disable-gpu",
            f"--user-data-dir={tmp_profile.name}",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_abs}",
            html_abs.as_uri(),
        ], check=True, timeout=90, capture_output=True)
        for _ in range(15):
            if pdf_abs.exists():
                break
            time.sleep(0.2)
        if not pdf_abs.exists():
            raise RuntimeError("Edge returned 0 but PDF was not created")
        print(f"Wrote {pdf_abs}")
    except Exception as e:
        print(f"PDF generation failed: {e}")
    finally:
        try:
            tmp_profile.cleanup()
        except Exception:
            pass  # Edge may still hold locks on Windows; OS will clean up temp later.

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
    tpl = env.get_template("handbook.html.j2")
    html = tpl.render(
        title=src["title"],
        intro=effective_intro(src, enrichment),
        knowledge=src["knowledge_requirements"],
        tasks=effective_tasks(src, enrichment),
        oral=effective_oral(src, enrichment),
        written_exam_crosswalk=src.get("written_exam_crosswalk", ""),
        enrichment=enrichment,
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")
    print(f"Wrote {out_path}")

    render_pdf(out_path)

if __name__ == "__main__":
    main()
