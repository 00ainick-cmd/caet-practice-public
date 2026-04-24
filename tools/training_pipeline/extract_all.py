"""Run extract_source.py against every module in the manifest with a source docx."""
import json, subprocess, sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
MANIFEST = json.load((SCRIPT_DIR / "module_manifest.json").open("r", encoding="utf-8"))

SOURCE_DIR = Path("C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/training_source")
STAGING_DIR = Path("C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/staging")
STAGING_DIR.mkdir(parents=True, exist_ok=True)

fail = []
for m in MANIFEST["modules"]:
    if not m.get("source_docx"):
        print(f"skip {m['slug']}: no source docx ({m.get('note','')})")
        continue
    src = SOURCE_DIR / m["source_docx"]
    out = STAGING_DIR / f"{m['slug']}_source.json"
    if not src.exists():
        print(f"FAIL {m['slug']}: source missing {src}")
        fail.append(m['slug'])
        continue
    r = subprocess.run(
        [sys.executable, str(SCRIPT_DIR / "extract_source.py"), str(src), str(out)],
        capture_output=True, text=True,
    )
    if r.returncode == 0:
        print(f"{m['slug']}: {r.stdout.strip()}")
    else:
        print(f"FAIL {m['slug']}: {r.stderr.strip()}")
        fail.append(m['slug'])

if fail:
    print(f"\nFailures: {fail}")
    sys.exit(1)
print(f"\n{len(MANIFEST['modules'])-1} modules extracted (adv15 skipped)")
