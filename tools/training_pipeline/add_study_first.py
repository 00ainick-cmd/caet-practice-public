"""Inject the Study First card row into each module hub's index.html.

Insertion marker: the existing "Study Activities" section label. We insert the new
Study First section and its card grid BEFORE that label, matching the pattern
already applied to adv10.
"""
import json
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
MANIFEST = json.load((SCRIPT_DIR / "module_manifest.json").open("r", encoding="utf-8"))
REPO_ROOT = SCRIPT_DIR.parent.parent

STUDY_FIRST_HTML = '''    <!-- ═══════════════════════════════════════════════════════
         STUDY FIRST — Reading & Reference Materials
    ═══════════════════════════════════════════════════════ -->
    <div class="section-label">Study First</div>
    <div class="activity-grid">
      <a href="training/handbook.html" target="_blank" class="activity-card" style="text-decoration:none; color:inherit;">
        <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/></svg></div>
        <div class="card-title">Handbook</div>
        <div class="card-desc">Full study guide — web and printable.</div>
        <div class="card-footer"><span class="card-xp">Read</span><span class="card-status status-new">HTML + PDF</span></div>
      </a>
      <a href="training/lesson.html" target="_blank" class="activity-card" style="text-decoration:none; color:inherit;">
        <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6"/><path d="M10 22h4"/><path d="M15.09 14a5 5 0 1 0-6.18 0A3 3 0 0 1 10 18h4a3 3 0 0 1 1.09-4Z"/></svg></div>
        <div class="card-title">Interactive Lesson</div>
        <div class="card-desc">45-minute 5E-format walkthrough.</div>
        <div class="card-footer"><span class="card-xp">~45 min</span><span class="card-status status-new">5E</span></div>
      </a>
      <a href="training/lesson-plan.pdf" target="_blank" class="activity-card" style="text-decoration:none; color:inherit;">
        <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="9" y1="13" x2="15" y2="13"/><line x1="9" y1="17" x2="15" y2="17"/></svg></div>
        <div class="card-title">Lesson Plan</div>
        <div class="card-desc">Instructor guide with agenda &amp; Q&amp;A.</div>
        <div class="card-footer"><span class="card-xp">Instructor</span><span class="card-status status-new">PDF</span></div>
      </a>
      <a href="training/job-aid.pdf" target="_blank" class="activity-card" style="text-decoration:none; color:inherit;">
        <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4"/><path d="M8 2v4"/><path d="M3 10h18"/></svg></div>
        <div class="card-title">Job Aid</div>
        <div class="card-desc">1-page quick reference.</div>
        <div class="card-footer"><span class="card-xp">Quick ref</span><span class="card-status status-new">PDF</span></div>
      </a>
      <a href="training/worksheet.pdf" target="_blank" class="activity-card" style="text-decoration:none; color:inherit;">
        <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg></div>
        <div class="card-title">Worksheet</div>
        <div class="card-desc">Pre-drill practice problems.</div>
        <div class="card-footer"><span class="card-xp">Practice</span><span class="card-status status-new">PDF</span></div>
      </a>
      <a href="training/practical-rubric.pdf" target="_blank" class="activity-card" style="text-decoration:none; color:inherit;">
        <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg></div>
        <div class="card-title">Practical Rubric</div>
        <div class="card-desc">Evaluator scoring sheet.</div>
        <div class="card-footer"><span class="card-xp">Evaluator</span><span class="card-status status-new">PDF</span></div>
      </a>
    </div>

'''

OLD_SECTION = '''    <!-- ═══════════════════════════════════════════════════════
         STUDY ACTIVITIES — v4 Card Grid
    ═══════════════════════════════════════════════════════ -->
    <div class="section-label">Study Activities</div>'''

NEW_SECTION = STUDY_FIRST_HTML + '''    <!-- ═══════════════════════════════════════════════════════
         STUDY ACTIVITIES — v4 Card Grid
    ═══════════════════════════════════════════════════════ -->
    <div class="section-label">Study Activities</div>'''

def main():
    updated, skipped, failed = [], [], []
    for m in MANIFEST["modules"]:
        # Skip adv10 — already done manually in Task 9
        if m["slug"] == "adv10":
            continue
        idx = REPO_ROOT / "advanced" / "training" / f"{m['slug']}-{m['dir']}" / "index.html"
        if not idx.exists():
            failed.append(f"{m['slug']}: {idx} missing")
            continue
        content = idx.read_text(encoding="utf-8")
        if "STUDY FIRST" in content or "Study First" in content:
            skipped.append(m["slug"])
            continue
        if OLD_SECTION not in content:
            failed.append(f"{m['slug']}: insertion marker not found")
            continue
        new = content.replace(OLD_SECTION, NEW_SECTION, 1)
        idx.write_text(new, encoding="utf-8")
        updated.append(m["slug"])

    print(f"Updated: {len(updated)} — {updated}")
    print(f"Skipped (already had Study First): {len(skipped)} — {skipped}")
    if failed:
        print(f"\nFAILED ({len(failed)}):")
        for f in failed:
            print(f"  {f}")
        return 1
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
