"""Run all 6 artifact generators against every module in the manifest."""
import json, subprocess, sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
MANIFEST = json.load((SCRIPT_DIR / "module_manifest.json").open("r", encoding="utf-8"))
STAGING = Path("C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/staging")
REPO_ROOT = SCRIPT_DIR.parent.parent

GENERATORS = [
    ("gen_handbook.py",    "handbook.html"),
    ("gen_lesson.py",      "lesson.html"),
    ("gen_lesson_plan.py", "lesson-plan.pdf"),
    ("gen_job_aid.py",     "job-aid.pdf"),
    ("gen_worksheet.py",   "worksheet.pdf"),
    ("gen_rubric.py",      "practical-rubric.pdf"),
]

def run_module(slug, dir_name, skip_adv10=True):
    if skip_adv10 and slug == "adv10":
        return ("adv10", "skipped")
    src = STAGING / f"{slug}_source.json"
    if not src.exists():
        return (slug, f"FAIL: source missing {src}")
    out_dir = REPO_ROOT / "advanced" / "training" / f"{slug}-{dir_name}" / "training"
    out_dir.mkdir(parents=True, exist_ok=True)
    for gen, artifact in GENERATORS:
        out = out_dir / artifact
        r = subprocess.run(
            [sys.executable, str(SCRIPT_DIR / gen), str(src), str(out), f"--slug={slug}"],
            capture_output=True, text=True, timeout=180,
        )
        if r.returncode != 0:
            return (slug, f"FAIL {gen}: {r.stderr[-300:]}")
    return (slug, "ok")

if __name__ == "__main__":
    include_adv10 = "--include-adv10" in sys.argv
    results = []
    for m in MANIFEST["modules"]:
        r = run_module(m["slug"], m["dir"], skip_adv10=not include_adv10)
        print(f"{r[0]}: {r[1]}")
        results.append(r)
    failures = [r for r in results if r[1] != "ok" and r[1] != "skipped"]
    if failures:
        print(f"\n{len(failures)} failure(s):")
        for s, msg in failures:
            print(f"  {s}: {msg}")
        sys.exit(1)
    print(f"\nAll {len([r for r in results if r[1] == 'ok'])} modules generated successfully")
