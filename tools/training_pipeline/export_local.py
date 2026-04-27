"""Copy all 15 module training/ folders to a flat browsable structure on the local disk.

Default destination: OneDrive CAET Advanced folder (cloud-synced, alongside source docs).
Override with: python export_local.py --to=<path>

Layout produced:
  <EXPORT_ROOT>/
    README.md
    adv1-cabin-management-systems/
      handbook.html
      handbook.pdf
      lesson.html
      lesson-plan.pdf
      job-aid.pdf
      worksheet.pdf
      practical-rubric.pdf
    adv2-connectivity/
    ...
    adv15-emergency-autoland/
    _enrichment-source/    (the JSON content files — edit then regen)
    _regenerate.txt        (instructions to rebuild after editing enrichment)
"""
import json, shutil
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent.parent
MANIFEST = json.load((SCRIPT_DIR / "module_manifest.json").open("r", encoding="utf-8"))

# adv10 isn't in manifest (pilot) — add it back for export
ALL_MODULES = [{"slug": "adv10", "dir": "wire-harness-fabrication", "topic": "Wire Harness Fabrication & Testing"}] + MANIFEST["modules"]
# Sort by adv number for human-friendly ordering
ALL_MODULES.sort(key=lambda m: int(m["slug"].replace("adv", "")))

# Export to OneDrive so the materials sync to cloud and live alongside other
# CAET program documents. Override with --to=<path> if you want elsewhere.
import sys as _sys
_default_export = r"C:\Users\nickb\OneDrive - Aircraft Electronics Association\Desktop\CAET\CAET Advanced\CAET-Advanced-Training-Materials"
_export_override = next((a.split("=", 1)[1] for a in _sys.argv[1:] if a.startswith("--to=")), None)
EXPORT_ROOT = Path(_export_override or _default_export)
EXPORT_ROOT.mkdir(parents=True, exist_ok=True)

# Copy each module's training/ contents
copied = 0
for m in ALL_MODULES:
    src = REPO_ROOT / "advanced" / "training" / f"{m['slug']}-{m['dir']}" / "training"
    if not src.exists():
        print(f"SKIP {m['slug']}: {src} missing")
        continue
    dest = EXPORT_ROOT / f"{m['slug']}-{m['dir']}"
    dest.mkdir(exist_ok=True)
    for f in src.iterdir():
        if f.is_file():
            shutil.copy2(f, dest / f.name)
            copied += 1
    print(f"{m['slug']:6s} -> {dest.name}/  ({len(list(dest.iterdir()))} files)")

# Copy enrichment JSONs (so user can edit content)
enr_dest = EXPORT_ROOT / "_enrichment-source"
enr_dest.mkdir(exist_ok=True)
enr_src = SCRIPT_DIR / "enrichment"
for f in enr_src.iterdir():
    if f.is_file() and f.suffix == ".json":
        shutil.copy2(f, enr_dest / f.name)

# Top-level README
readme = """# CAET Advanced Training Materials

This folder contains training artifacts for all 15 CAET Advanced modules. Each
module has its own subfolder with seven files.

## What's in each module subfolder

| File | Audience | Format | Purpose |
|------|----------|--------|---------|
| handbook.html | Student | Web (open in browser) | Full study document — read it first |
| handbook.pdf | Student | Print | Same content as handbook.html, formatted for print |
| lesson.html | Student | Web (open in browser) | 45-minute interactive 5E-format lesson |
| lesson-plan.pdf | Instructor | Print | Minute-by-minute teaching guide for a 3-hour class |
| job-aid.pdf | Student/Tech | Print | 1-page evaluator-day quick reference (laminate it) |
| worksheet.pdf | Student | Print | Pre-drill practice problems with answer key |
| practical-rubric.pdf | Evaluator | Print | Per-task accept/reject scoring sheet |

## Modules

| Folder | Topic |
|--------|-------|
"""
for m in ALL_MODULES:
    readme += f"| `{m['slug']}-{m['dir']}/` | {m.get('topic', m['dir'].replace('-', ' ').title())} |\n"

readme += """
## How to use

- **HTML files**: double-click — they open in your default browser. No internet
  required, fully self-contained.
- **PDF files**: double-click — they open in your default PDF viewer. Print
  worksheet/job-aid/rubric as needed for class or evaluator use.

## Editing the content

The `_enrichment-source/` folder contains the per-module content JSON files.
These are the editable source of all the teaching material (Why-This-Matters
narratives, glossary terms, step-by-step procedures, evaluator-watching-for
items, common mistakes, oral board answers, background theory).

To edit a module's content:
1. Open `_enrichment-source/advN.json` in any text editor (VS Code recommended).
2. Modify the JSON values you want to change. Keep the structure intact.
3. Regenerate the artifacts. See `_regenerate.txt` for the command.

The original git repo with the regen pipeline is at:
  C:/Users/nickb/Downloads/caet-practice-public/

## Important notes

- These materials are AI-authored. Standards citations (MIL-SPEC, ARINC, RTCA,
  14 CFR, FAA AC) and accident references are accurate to my training-data
  knowledge but should be reviewed by a qualified SME before being treated
  as official AEA curriculum.
- The PQS source documents (in your OneDrive CAET Advanced folder) were the
  starting point; the AI-authored enrichment supplements them with teaching-
  grade depth.

Generated by the CAET training pipeline (tools/training_pipeline/) on the
caet-practice-public repo.
"""
(EXPORT_ROOT / "README.md").write_text(readme, encoding="utf-8")

# Regen instructions
regen = """# How to regenerate these artifacts after editing _enrichment-source/

After editing any `_enrichment-source/advN.json` file, run this from the repo:

  cd "C:/Users/nickb/Downloads/caet-practice-public"
  python tools/training_pipeline/generate_all.py --include-adv10
  python tools/training_pipeline/export_local.py

The first command rebuilds the artifacts inside the repo. The second copies
them back to this folder.

If you only edited one module:

  python tools/training_pipeline/gen_handbook.py \\
    "C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/staging/advN_source.json" \\
    "advanced/training/advN-<dir>/training/handbook.html" --slug=advN

Replace N with the module number (e.g. adv4) and <dir> with the slug
(e.g. flight-management-systems). Repeat for each generator (gen_lesson,
gen_lesson_plan, gen_job_aid, gen_worksheet, gen_rubric).

Then re-export:

  python tools/training_pipeline/export_local.py
"""
(EXPORT_ROOT / "_regenerate.txt").write_text(regen, encoding="utf-8")

print(f"\nCopied {copied} artifacts + {len(list(enr_dest.iterdir()))} enrichment files")
print(f"Export ready at: {EXPORT_ROOT}")
print(f"Open this in File Explorer:")
print(f"  explorer.exe \"{EXPORT_ROOT}\"")
