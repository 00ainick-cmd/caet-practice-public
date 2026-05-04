"""Copy the pedagogy-library/ contents to one or more browsable destinations.

Default destinations:
  1. OneDrive (cloud-synced):
     C:\\Users\\nickb\\OneDrive - Aircraft Electronics Association\\Desktop\\AI-Tutor-Pedagogy-Library\\
  2. Obsidian Genesis vault (note-taking):
     C:\\Users\\nickb\\Desktop\\Genesis\\65-Pedagogy-Library\\

Override either with --onedrive=<path> or --obsidian=<path>.
Pass --skip-onedrive or --skip-obsidian to disable a destination.

Layout produced at each destination:
  AI-Tutor-Pedagogy-Library/  (or 65-Pedagogy-Library/)
  ├── README.md
  ├── 01-learning-science/
  │   └── testing-effect.md  (and 12 more once Phase 4 completes)
  ├── 02-instructional-design/  ... (empty for now)
  └── ... (other category dirs)
"""
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SRC = REPO_ROOT / "pedagogy-library"

ONEDRIVE_DEFAULT = Path(r"C:\Users\nickb\OneDrive - Aircraft Electronics Association\Desktop\AI-Tutor-Pedagogy-Library")
OBSIDIAN_DEFAULT = Path(r"C:\Users\nickb\Desktop\Genesis\65-Pedagogy-Library")

def parse_args():
    onedrive = ONEDRIVE_DEFAULT
    obsidian = OBSIDIAN_DEFAULT
    skip_onedrive = False
    skip_obsidian = False
    for a in sys.argv[1:]:
        if a == "--skip-onedrive":
            skip_onedrive = True
        elif a == "--skip-obsidian":
            skip_obsidian = True
        elif a.startswith("--onedrive="):
            onedrive = Path(a.split("=", 1)[1])
        elif a.startswith("--obsidian="):
            obsidian = Path(a.split("=", 1)[1])
    return onedrive, obsidian, skip_onedrive, skip_obsidian

def copy_to(dst):
    """Mirror SRC into dst. Removes dst first if it exists to avoid stale files."""
    if not SRC.exists():
        print(f"FAIL: source missing {SRC}")
        return False
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(SRC, dst)
    n = sum(1 for _ in dst.rglob("*") if _.is_file())
    print(f"  -> {dst}  ({n} files)")
    return True

def main():
    onedrive, obsidian, skip_onedrive, skip_obsidian = parse_args()
    print(f"Source: {SRC}")
    if not skip_onedrive:
        print("Copying to OneDrive:")
        copy_to(onedrive)
    if not skip_obsidian:
        print("Copying to Obsidian Genesis vault:")
        copy_to(obsidian)
    print("Done.")
    print()
    print("Open in File Explorer:")
    if not skip_onedrive:
        print(f'  explorer.exe "{onedrive}"')
    if not skip_obsidian:
        print(f'  explorer.exe "{obsidian}"')

if __name__ == "__main__":
    main()
