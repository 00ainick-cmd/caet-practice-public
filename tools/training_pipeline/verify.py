"""QA: verify all 15 modules have all 7 expected artifacts + Study First in hub."""
import json, sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
MANIFEST = json.load((SCRIPT_DIR / "module_manifest.json").open("r", encoding="utf-8"))
REPO_ROOT = SCRIPT_DIR.parent.parent

EXPECTED_ARTIFACTS = [
    ("handbook.html", 8000),     # min size in bytes
    ("handbook.pdf", 50000),
    ("lesson.html", 5000),
    ("lesson-plan.pdf", 10000),
    ("job-aid.pdf", 3500),
    ("worksheet.pdf", 6000),
    ("practical-rubric.pdf", 6000),
]

# adv10 isn't in manifest (it's the pilot) — verify it too
ALL_MODULES = [{"slug": "adv10", "dir": "wire-harness-fabrication"}] + MANIFEST["modules"]

failures = []
artifact_count = 0
for m in ALL_MODULES:
    slug, dir_name = m["slug"], m["dir"]
    mod_path = REPO_ROOT / "advanced" / "training" / f"{slug}-{dir_name}"
    if not mod_path.exists():
        failures.append(f"{slug}: module dir missing — {mod_path}")
        continue

    # Hub Study First check
    hub = mod_path / "index.html"
    if hub.exists():
        content = hub.read_text(encoding="utf-8")
        if "Study First" not in content:
            failures.append(f"{slug}: hub missing 'Study First' section")
    else:
        failures.append(f"{slug}: index.html missing")

    # Artifact check
    training = mod_path / "training"
    if not training.exists():
        failures.append(f"{slug}: training/ subdir missing")
        continue
    for artifact, min_size in EXPECTED_ARTIFACTS:
        f = training / artifact
        if not f.exists():
            failures.append(f"{slug}: missing {artifact}")
            continue
        size = f.stat().st_size
        if size < min_size:
            failures.append(f"{slug}/{artifact}: too small ({size} bytes, min {min_size})")
        artifact_count += 1

if failures:
    print(f"FAILURES ({len(failures)}):")
    for f in failures:
        print(f"  {f}")
    sys.exit(1)
print(f"PASS: all {len(ALL_MODULES)} modules have all 7 expected artifacts and Study First section")
print(f"Total artifacts verified: {artifact_count}")
