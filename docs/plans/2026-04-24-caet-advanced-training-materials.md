# CAET Advanced Training Materials Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a complete training materials package (6 artifacts per module) for all 15 CAET Advanced practice modules, deployed to `/advanced/training/advN-*/training/` and linked from each module's hub.

**Architecture:** Pilot one module (adv10 Wire Harness Fabrication) end-to-end, get user approval, then replicate the template to the other 14 modules via parallel agents. Source material is 18 existing AEA docx files plus the PQS Standards v5 PDF. Artifacts are rendered via HTML-first templates (handbook/lesson) and Python-generated PDFs for print artifacts (lesson-plan, job-aid, worksheet, practical-rubric).

**Tech Stack:**
- Python 3 with `python-docx` (source extraction), `reportlab` (PDF generation for print artifacts), `jinja2` (HTML templating)
- HTML-to-PDF via `weasyprint` for handbook.pdf (matches web styling)
- Jinja2 templates for handbook.html and lesson.html (reuse site `ace-theme.css`)
- Existing practice bank JSON (`/advanced/master-bank.json`) for lesson.html quiz data

**Design doc:** `docs/plans/2026-04-24-caet-advanced-training-materials-design.md`

**Source material:**
- 18 docx files in OneDrive: `Desktop/CAET/CAET Advanced/CAET-Advanced-Training-Program Curricullum/CAET-Advanced-Training-Program/`
- Working copy location: `C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/training_source/` (to be created in Task 0)

---

## Phase 0: Environment Setup

### Task 0: Verify Python toolchain + copy source docs locally

**Files:**
- Create: `C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/training_source/` (staging dir)
- Copy: 18 docx files from OneDrive → this staging dir

**Step 1: Check Python packages available**

Run:
```bash
python -c "import docx, reportlab, jinja2, weasyprint; print('all ok')"
```
Expected: `all ok`

If any missing:
```bash
pip install python-docx reportlab jinja2 weasyprint
```

**Step 2: Create local staging directory for source docx**

Run:
```bash
mkdir -p "C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/training_source"
```

**Step 3: Copy all 18 source docx files**

Run:
```bash
cp "C:/Users/nickb/OneDrive - Aircraft Electronics Association/Desktop/CAET/CAET Advanced/CAET-Advanced-Training-Program Curricullum/CAET-Advanced-Training-Program/PQS-Training-Modules/"*.docx "C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/training_source/"
cp "C:/Users/nickb/OneDrive - Aircraft Electronics Association/Desktop/CAET/CAET Advanced/CAET-Advanced-Training-Program Curricullum/CAET-Advanced-Training-Program/Exam-Study-Modules/"*.docx "C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/training_source/"
cp "C:/Users/nickb/OneDrive - Aircraft Electronics Association/Desktop/CAET/CAET Advanced/CAET_Advanced_PQS_Standards_v5.pdf" "C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/training_source/"
```

**Step 4: Verify file count**

Run:
```bash
ls "C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/training_source/" | wc -l
```
Expected: `19` (18 docx + 1 pdf)

**Step 5: Commit pipeline infrastructure placeholder**

```bash
cd "C:/Users/nickb/Downloads/caet-practice-public"
mkdir -p tools/training_pipeline
echo "# Training material generation pipeline" > tools/training_pipeline/README.md
git add tools/training_pipeline/README.md
git commit -m "chore: create training pipeline tools directory"
```

---

## Phase 1: Pilot — adv10 Wire Harness Fabrication (Tasks 1-11)

The pilot builds all 6 artifacts for one module. User approves before Phase 2.

### Task 1: Source extraction — parse adv10 docx into structured JSON

**Files:**
- Create: `tools/training_pipeline/extract_source.py`
- Input: `C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/training_source/04-Wire-Harness-Fabrication-Testing.docx`
- Output: `C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/staging/adv10_source.json`

**Step 1: Write extractor script**

```python
# tools/training_pipeline/extract_source.py
"""Parse a CAET Advanced training docx into structured JSON for artifact generation."""
import json, sys, re
from pathlib import Path
from docx import Document

sys.stdout.reconfigure(encoding="utf-8")

def extract(docx_path):
    doc = Document(docx_path)
    result = {
        "title": None,
        "intro": [],
        "knowledge_requirements": [],   # [{heading, body}]
        "tasks": [],                    # [{heading, body}]
        "oral_board_questions": [],
        "written_exam_crosswalk": "",
    }
    section = None
    current_sub = None
    for p in doc.paragraphs:
        text = p.text.strip()
        if not text: continue
        style = p.style.name if p.style else ""

        # Identify major sections
        if "Heading 1" in style:
            if text.startswith("Section"):
                result["title"] = text
                section = "intro"
            elif "Knowledge Requirements" in text:
                section = "knowledge"
            elif "Task Preparation" in text:
                section = "tasks"
            elif "Oral Board" in text:
                section = "oral"
            elif "Written Exam Crosswalk" in text:
                section = "crosswalk"
            continue

        if "Heading 2" in style:
            current_sub = {"heading": text, "body": ""}
            if section == "knowledge":
                result["knowledge_requirements"].append(current_sub)
            elif section == "tasks":
                result["tasks"].append(current_sub)
            continue

        # Body text
        if section == "intro":
            result["intro"].append(text)
        elif section in ("knowledge", "tasks") and current_sub:
            current_sub["body"] += (("\n" if current_sub["body"] else "") + text)
        elif section == "oral" and text.startswith("Q"):
            result["oral_board_questions"].append(text)
        elif section == "crosswalk":
            result["written_exam_crosswalk"] += (" " + text).strip() + " "

    result["written_exam_crosswalk"] = result["written_exam_crosswalk"].strip()
    return result

if __name__ == "__main__":
    src = Path(sys.argv[1])
    out = Path(sys.argv[2])
    out.parent.mkdir(parents=True, exist_ok=True)
    data = extract(src)
    out.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Extracted: title={data['title']}, {len(data['knowledge_requirements'])} knowledge, {len(data['tasks'])} tasks, {len(data['oral_board_questions'])} oral")
```

**Step 2: Run extractor on adv10 source**

Run:
```bash
cd "C:/Users/nickb/Downloads/caet-practice-public"
python tools/training_pipeline/extract_source.py \
  "C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/training_source/04-Wire-Harness-Fabrication-Testing.docx" \
  "C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/staging/adv10_source.json"
```
Expected: `Extracted: title=Section 4: Wire Harness Fabrication & Testing, 3 knowledge, 6 tasks, 5 oral`

**Step 3: Verify JSON structure**

Run:
```bash
python -c "import json; d=json.load(open('C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/staging/adv10_source.json',encoding='utf-8')); print(list(d.keys()))"
```
Expected: `['title', 'intro', 'knowledge_requirements', 'tasks', 'oral_board_questions', 'written_exam_crosswalk']`

**Step 4: Commit**

```bash
git add tools/training_pipeline/extract_source.py
git commit -m "feat: add docx source extractor for training pipeline"
```

---

### Task 2: Generate handbook.html (pilot)

**Files:**
- Create: `tools/training_pipeline/gen_handbook.py`
- Create: `tools/training_pipeline/templates/handbook.html.j2`
- Output: `advanced/training/adv10-wire-harness-fabrication/training/handbook.html`

**Step 1: Write Jinja2 template**

```html
<!-- tools/training_pipeline/templates/handbook.html.j2 -->
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{ title }} | CAET Advanced Handbook</title>
<link rel="stylesheet" href="../../../../shared/ace-theme.css">
<style>
body { font-family: 'Inter', sans-serif; max-width: 880px; margin: 0 auto;
       padding: 40px 24px; background: #080C1A; color: var(--text-primary); line-height: 1.6; }
h1 { color: var(--gold); border-bottom: 2px solid var(--gold); padding-bottom: 8px; }
h2 { color: #22d3ee; margin-top: 2em; }
.callout { background: rgba(212,168,83,0.1); border-left: 4px solid var(--gold);
           padding: 16px 20px; margin: 20px 0; border-radius: 6px; }
.mistakes { background: rgba(239,68,68,0.08); border-left: 4px solid #ef4444;
            padding: 16px 20px; margin: 20px 0; border-radius: 6px; }
.quiz { background: rgba(34,211,238,0.08); border-left: 4px solid #22d3ee;
        padding: 20px 24px; margin: 24px 0; border-radius: 6px; }
.toc { background: rgba(255,255,255,0.05); padding: 20px 24px; border-radius: 8px; }
.page-break { page-break-after: always; }
@media print { body { background: white; color: black; } }
</style>
</head>
<body>
<h1>{{ title }}</h1>
<p><em>CAET Advanced Certification — Student Handbook</em></p>

<div class="toc">
<h2>Table of Contents</h2>
<ol>
<li>Why This Matters</li>
{% for kr in knowledge %}<li>{{ kr.heading }}</li>{% endfor %}
{% for t in tasks %}<li>{{ t.heading }}</li>{% endfor %}
<li>Self-Check Quick Quiz</li>
</ol>
</div>

<div class="page-break"></div>

<h2>1. Why This Matters</h2>
{% for para in intro %}<p>{{ para }}</p>{% endfor %}

{% for kr in knowledge %}
<h2>{{ loop.index + 1 }}. {{ kr.heading }}</h2>
<p>{{ kr.body }}</p>
{% endfor %}

<h2>{{ knowledge|length + 2 }}. Procedures</h2>
{% for t in tasks %}
<h3>{{ t.heading }}</h3>
<p>{{ t.body }}</p>
<div class="callout"><strong>Evaluator is watching for:</strong> See practical rubric for accept/reject criteria.</div>
{% endfor %}

<h2>{{ knowledge|length + 3 }}. Self-Check Quick Quiz</h2>
<div class="quiz">
{% for q in oral %}<p>{{ loop.index }}. {{ q }}</p>{% endfor %}
<p><em>Answers in handbook appendix.</em></p>
</div>

<hr>
<p><small>© 2026 Aircraft Electronics Association. Derived from CAET Advanced PQS Training Module.</small></p>
</body>
</html>
```

**Step 2: Write handbook generator**

```python
# tools/training_pipeline/gen_handbook.py
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
```

**Step 3: Run generator**

Run:
```bash
python tools/training_pipeline/gen_handbook.py \
  "C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/staging/adv10_source.json" \
  "advanced/training/adv10-wire-harness-fabrication/training/handbook.html"
```
Expected: `Wrote advanced/training/adv10-wire-harness-fabrication/training/handbook.html`

**Step 4: Open in browser to spot-check**

Open: `advanced/training/adv10-wire-harness-fabrication/training/handbook.html` in browser.
Verify: Title correct, 6 task sections visible, quiz section shows 5 oral questions, theme CSS applied.

**Step 5: Commit**

```bash
git add tools/training_pipeline/templates/handbook.html.j2 tools/training_pipeline/gen_handbook.py advanced/training/adv10-wire-harness-fabrication/training/handbook.html
git commit -m "feat: add handbook generator + adv10 pilot handbook.html"
```

---

### Task 3: Generate handbook.pdf from HTML via weasyprint

**Files:**
- Modify: `tools/training_pipeline/gen_handbook.py` (add PDF output)
- Output: `advanced/training/adv10-wire-harness-fabrication/training/handbook.pdf`

**Step 1: Add PDF generation to generator**

Edit `tools/training_pipeline/gen_handbook.py` — append to end of file:

```python
# PDF generation (after HTML write)
try:
    from weasyprint import HTML
    pdf_path = out_path.with_suffix(".pdf")
    HTML(filename=str(out_path)).write_pdf(str(pdf_path))
    print(f"Wrote {pdf_path}")
except Exception as e:
    print(f"PDF generation failed: {e}")
```

**Step 2: Re-run generator**

Run:
```bash
python tools/training_pipeline/gen_handbook.py \
  "C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/staging/adv10_source.json" \
  "advanced/training/adv10-wire-harness-fabrication/training/handbook.html"
```
Expected output includes: `Wrote .../handbook.pdf`

**Step 3: Verify PDF exists + opens**

```bash
ls -la advanced/training/adv10-wire-harness-fabrication/training/handbook.pdf
```
Expected: file exists, size > 10KB.

Open PDF in viewer — verify content + formatting look reasonable.

**Step 4: Commit**

```bash
git add tools/training_pipeline/gen_handbook.py advanced/training/adv10-wire-harness-fabrication/training/handbook.pdf
git commit -m "feat: add PDF output to handbook generator"
```

---

### Task 4: Generate lesson.html (interactive 5E lesson)

**Files:**
- Create: `tools/training_pipeline/gen_lesson.py`
- Create: `tools/training_pipeline/templates/lesson.html.j2`
- Output: `advanced/training/adv10-wire-harness-fabrication/training/lesson.html`

**Step 1: Write 5E lesson template**

```html
<!-- tools/training_pipeline/templates/lesson.html.j2 -->
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<title>{{ title }} — Interactive Lesson</title>
<link rel="stylesheet" href="../../../../shared/ace-theme.css">
<style>
body { font-family: 'Inter', sans-serif; max-width: 900px; margin: 0 auto;
       padding: 40px 24px; background: #080C1A; color: var(--text-primary); }
.phase { background: rgba(255,255,255,0.04); border-radius: 12px;
         padding: 24px; margin: 20px 0; border: 1px solid rgba(255,255,255,0.1); }
.phase-label { color: var(--gold); font-size: 12px; text-transform: uppercase;
               letter-spacing: 2px; font-weight: 700; margin-bottom: 8px; }
.phase h2 { margin: 0 0 12px; font-size: 24px; }
.timing { float: right; color: var(--text-muted); font-size: 13px; }
.card { background: rgba(34,211,238,0.06); border-left: 3px solid #22d3ee;
        padding: 16px 20px; margin: 12px 0; border-radius: 6px; cursor: pointer; }
.card h3 { margin: 0 0 8px; color: #22d3ee; }
.quiz-start { background: var(--gold); color: #000; border: none; padding: 12px 24px;
              border-radius: 8px; font-weight: 700; cursor: pointer; font-size: 14px; }
</style>
</head>
<body>
<h1>📚 {{ title }}</h1>
<p><em>Interactive Lesson — ~25 minutes</em></p>

<div class="phase">
  <div class="phase-label">Engage</div>
  <span class="timing">~2 min</span>
  <h2>Get Your Attention</h2>
  <p>{{ engage_prompt }}</p>
</div>

<div class="phase">
  <div class="phase-label">Explore</div>
  <span class="timing">~5 min</span>
  <h2>Discover the Concept</h2>
  <p>{{ explore_prompt }}</p>
</div>

<div class="phase">
  <div class="phase-label">Explain</div>
  <span class="timing">~10 min</span>
  <h2>Core Concepts</h2>
  {% for kr in knowledge %}
  <div class="card">
    <h3>{{ kr.heading }}</h3>
    <p>{{ kr.body[:400] }}...</p>
  </div>
  {% endfor %}
</div>

<div class="phase">
  <div class="phase-label">Elaborate</div>
  <span class="timing">~8 min</span>
  <h2>Apply It</h2>
  <p>Walk through this scenario: {{ tasks[0].heading if tasks else '' }}</p>
  <p>{{ tasks[0].body[:300] if tasks else '' }}...</p>
</div>

<div class="phase">
  <div class="phase-label">Evaluate</div>
  <span class="timing">~5 min</span>
  <h2>Test Your Understanding</h2>
  <p>Answer 10 questions from this module's practice bank.</p>
  <button class="quiz-start" onclick="window.location.href='../drill.html'">Start 10-Question Quiz →</button>
</div>

<p style="margin-top: 40px; font-size: 12px; color: var(--text-muted);">
When done, return to the module hub to drill the full question bank.
</p>
</body>
</html>
```

**Step 2: Write lesson generator with engage/explore prompts derived from content**

```python
# tools/training_pipeline/gen_lesson.py
import json, sys
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

tpl_dir = Path(__file__).parent / "templates"
env = Environment(loader=FileSystemLoader(tpl_dir))
tpl = env.get_template("lesson.html.j2")

src_path, out_path = Path(sys.argv[1]), Path(sys.argv[2])
src = json.load(src_path.open("r", encoding="utf-8"))

# Derive engage prompt from first knowledge heading
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
```

**Step 3: Run + open to check**

Run:
```bash
python tools/training_pipeline/gen_lesson.py \
  "C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/staging/adv10_source.json" \
  "advanced/training/adv10-wire-harness-fabrication/training/lesson.html"
```

Open in browser, verify all 5 phase blocks render, "Start Quiz" button links to drill.html.

**Step 4: Commit**

```bash
git add tools/training_pipeline/templates/lesson.html.j2 tools/training_pipeline/gen_lesson.py advanced/training/adv10-wire-harness-fabrication/training/lesson.html
git commit -m "feat: add 5E lesson generator + adv10 pilot lesson.html"
```

---

### Task 5: Generate lesson-plan.pdf (instructor guide)

**Files:**
- Create: `tools/training_pipeline/gen_lesson_plan.py`
- Output: `advanced/training/adv10-wire-harness-fabrication/training/lesson-plan.pdf`

**Step 1: Write generator using reportlab**

```python
# tools/training_pipeline/gen_lesson_plan.py
import json, sys
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.units import inch
from reportlab.lib import colors

src_path, out_path = Path(sys.argv[1]), Path(sys.argv[2])
src = json.load(src_path.open("r", encoding="utf-8"))

styles = getSampleStyleSheet()
title_style = ParagraphStyle('Title', parent=styles['Title'], textColor=colors.HexColor("#0a2540"))
h2_style = ParagraphStyle('H2', parent=styles['Heading2'], textColor=colors.HexColor("#0a2540"))

out_path.parent.mkdir(parents=True, exist_ok=True)
doc = SimpleDocTemplate(str(out_path), pagesize=letter, topMargin=0.75*inch, bottomMargin=0.75*inch)
story = []

story.append(Paragraph(f"Instructor Lesson Plan<br/>{src['title']}", title_style))
story.append(Paragraph("CAET Advanced Certification — Practical Qualification Standards", styles['Italic']))
story.append(Spacer(1, 0.3*inch))

story.append(Paragraph("Duration & Format", h2_style))
story.append(Paragraph("3 hours total (90 min direct instruction + demo · 90 min hands-on lab)", styles['Normal']))
story.append(Paragraph("Prerequisites: Student has read the handbook chapters 1-5 before class.", styles['Normal']))

story.append(Paragraph("Equipment (Per Student)", h2_style))
story.append(Paragraph("Specific to this module — instructor adapts based on facility inventory.", styles['Normal']))

story.append(Paragraph("Minute-by-Minute Agenda", h2_style))
data = [["Time", "Activity"]]
agenda = [
    ("0:00-0:15", "Hook: real-world failure photos (instructor notes)"),
    ("0:15-0:45", "Direct instruction: first two Knowledge Requirements"),
    ("0:45-1:00", "Demo: instructor walks through first task"),
    ("1:00-1:30", "Student hands-on: practice first task"),
    ("1:30-1:45", "BREAK"),
    ("1:45-2:15", "Demo: second task"),
    ("2:15-2:45", "Student hands-on: second task"),
    ("2:45-3:00", "Wrap + Q&A"),
]
for row in agenda:
    data.append(row)
t = Table(data, colWidths=[1.5*inch, 5*inch])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0a2540")),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
]))
story.append(t)
story.append(Spacer(1, 0.3*inch))

story.append(Paragraph("Key Teaching Points (from source material)", h2_style))
for kr in src["knowledge_requirements"]:
    story.append(Paragraph(f"<b>{kr['heading']}</b>", styles['Normal']))
    story.append(Paragraph(kr['body'][:400] + "...", styles['Normal']))
    story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("Oral Board Q&A Prep (ask students these)", h2_style))
for q in src["oral_board_questions"]:
    story.append(Paragraph(q, styles['Normal']))
    story.append(Spacer(1, 0.05*inch))

doc.build(story)
print(f"Wrote {out_path}")
```

**Step 2: Run generator**

```bash
python tools/training_pipeline/gen_lesson_plan.py \
  "C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/staging/adv10_source.json" \
  "advanced/training/adv10-wire-harness-fabrication/training/lesson-plan.pdf"
```
Expected: `Wrote .../lesson-plan.pdf`

**Step 3: Open PDF to verify**

Verify: table with 8-row agenda, Knowledge Requirements section, Oral Board questions listed at bottom. Formatting reasonable.

**Step 4: Commit**

```bash
git add tools/training_pipeline/gen_lesson_plan.py advanced/training/adv10-wire-harness-fabrication/training/lesson-plan.pdf
git commit -m "feat: add lesson-plan PDF generator + adv10 pilot"
```

---

### Task 6: Generate job-aid.pdf (1-page quick reference)

**Files:**
- Create: `tools/training_pipeline/gen_job_aid.py`
- Output: `advanced/training/adv10-wire-harness-fabrication/training/job-aid.pdf`

**Step 1: Write generator**

```python
# tools/training_pipeline/gen_job_aid.py
import json, sys
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch
from reportlab.lib import colors

src_path, out_path = Path(sys.argv[1]), Path(sys.argv[2])
src = json.load(src_path.open("r", encoding="utf-8"))

styles = getSampleStyleSheet()
title_style = ParagraphStyle('T', parent=styles['Title'], textColor=colors.HexColor("#0a2540"), fontSize=18)
section_style = ParagraphStyle('S', parent=styles['Heading2'], textColor=colors.HexColor("#D4A853"),
                                fontSize=12, spaceAfter=6)

out_path.parent.mkdir(parents=True, exist_ok=True)
doc = SimpleDocTemplate(str(out_path), pagesize=letter,
                        topMargin=0.4*inch, bottomMargin=0.4*inch,
                        leftMargin=0.5*inch, rightMargin=0.5*inch)
story = []

story.append(Paragraph(f"<b>{src['title']}</b> — Quick Reference", title_style))
story.append(Paragraph("CAET Advanced | Job Aid | AEA 2026", styles['Italic']))
story.append(Spacer(1, 0.15*inch))

# Distill top 4 knowledge requirements as job-aid sections
for idx, kr in enumerate(src["knowledge_requirements"][:4]):
    story.append(Paragraph(kr["heading"], section_style))
    # Compress body to key facts (first sentence + any bullet-like content)
    body = kr["body"]
    # Take first 200 chars as summary
    summary = body[:200] + "..." if len(body) > 200 else body
    story.append(Paragraph(summary, styles['Normal']))
    story.append(Spacer(1, 0.1*inch))

# Task list as "quick procedures"
story.append(Paragraph("Key Procedures", section_style))
task_data = [[f"#{i+1}", t["heading"]] for i, t in enumerate(src["tasks"])]
t = Table(task_data, colWidths=[0.5*inch, 6.5*inch])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f3f4f6")),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BOX', (0,0), (-1,-1), 0.5, colors.grey),
]))
story.append(t)

doc.build(story)
print(f"Wrote {out_path}")
```

**Step 2: Run + verify**

```bash
python tools/training_pipeline/gen_job_aid.py \
  "C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/staging/adv10_source.json" \
  "advanced/training/adv10-wire-harness-fabrication/training/job-aid.pdf"
```
Expected: PDF generated, fits on ~1 page.

Open PDF. Verify: title, 4 knowledge sections abbreviated, procedures table at bottom, fits on one page.

**Step 3: Commit**

```bash
git add tools/training_pipeline/gen_job_aid.py advanced/training/adv10-wire-harness-fabrication/training/job-aid.pdf
git commit -m "feat: add job-aid PDF generator + adv10 pilot"
```

---

### Task 7: Generate worksheet.pdf (pre-drill practice problems)

**Files:**
- Create: `tools/training_pipeline/gen_worksheet.py`
- Output: `advanced/training/adv10-wire-harness-fabrication/training/worksheet.pdf`

**Step 1: Write generator — derives problems from oral board Qs + knowledge requirements**

```python
# tools/training_pipeline/gen_worksheet.py
import json, sys
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.units import inch
from reportlab.lib import colors

src_path, out_path = Path(sys.argv[1]), Path(sys.argv[2])
src = json.load(src_path.open("r", encoding="utf-8"))

styles = getSampleStyleSheet()
title_style = ParagraphStyle('T', parent=styles['Title'], textColor=colors.HexColor("#0a2540"))
q_style = ParagraphStyle('Q', parent=styles['Normal'], spaceBefore=14, spaceAfter=4, fontName='Helvetica-Bold')
space_style = ParagraphStyle('Space', parent=styles['Normal'], fontName='Helvetica', leading=24,
                              textColor=colors.grey, fontSize=11)

out_path.parent.mkdir(parents=True, exist_ok=True)
doc = SimpleDocTemplate(str(out_path), pagesize=letter, topMargin=0.75*inch, bottomMargin=0.75*inch)
story = []

story.append(Paragraph(f"Worksheet: {src['title']}", title_style))
story.append(Paragraph("Complete these problems BEFORE taking the practice drill. Answers at back.", styles['Italic']))
story.append(Spacer(1, 0.2*inch))

# Use oral board questions as primary worksheet problems (they're scenario-based)
for i, q in enumerate(src["oral_board_questions"], 1):
    story.append(Paragraph(f"Problem {i}", q_style))
    story.append(Paragraph(q, styles['Normal']))
    # Add blank space for student to write answer
    story.append(Paragraph("___________________________________________<br/>___________________________________________<br/>___________________________________________", space_style))

# Add 5 more problems derived from tasks (fill-in-the-blank procedure style)
for i, t in enumerate(src["tasks"][:5], len(src["oral_board_questions"]) + 1):
    story.append(Paragraph(f"Problem {i} — Procedure Fill-In", q_style))
    prompt = f"Describe the procedure for: <b>{t['heading']}</b>. What are the main steps and what is the evaluator looking for?"
    story.append(Paragraph(prompt, styles['Normal']))
    story.append(Paragraph("___________________________________________<br/>___________________________________________<br/>___________________________________________", space_style))

# Answer key
story.append(PageBreak())
story.append(Paragraph("Answer Key", title_style))
for i, q in enumerate(src["oral_board_questions"], 1):
    story.append(Paragraph(f"Problem {i}:", q_style))
    story.append(Paragraph("See handbook section matching this topic for full answer. Practice answering aloud before oral board.", styles['Normal']))

for i, t in enumerate(src["tasks"][:5], len(src["oral_board_questions"]) + 1):
    story.append(Paragraph(f"Problem {i}: {t['heading']}", q_style))
    story.append(Paragraph(t['body'][:500], styles['Normal']))

doc.build(story)
print(f"Wrote {out_path}")
```

**Step 2: Run + verify**

```bash
python tools/training_pipeline/gen_worksheet.py \
  "C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/staging/adv10_source.json" \
  "advanced/training/adv10-wire-harness-fabrication/training/worksheet.pdf"
```

Verify: ~5-10 problems, blank space for answers, answer key after page break.

**Step 3: Commit**

```bash
git add tools/training_pipeline/gen_worksheet.py advanced/training/adv10-wire-harness-fabrication/training/worksheet.pdf
git commit -m "feat: add worksheet PDF generator + adv10 pilot"
```

---

### Task 8: Generate practical-rubric.pdf (evaluator scoring sheet)

**Files:**
- Create: `tools/training_pipeline/gen_rubric.py`
- Output: `advanced/training/adv10-wire-harness-fabrication/training/practical-rubric.pdf`

**Step 1: Write generator with Accept/Reject 2-column tables per task**

```python
# tools/training_pipeline/gen_rubric.py
import json, sys
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.units import inch
from reportlab.lib import colors

src_path, out_path = Path(sys.argv[1]), Path(sys.argv[2])
src = json.load(src_path.open("r", encoding="utf-8"))

styles = getSampleStyleSheet()
title_style = ParagraphStyle('T', parent=styles['Title'], textColor=colors.HexColor("#0a2540"))
task_style = ParagraphStyle('Task', parent=styles['Heading2'], textColor=colors.HexColor("#0a2540"))

out_path.parent.mkdir(parents=True, exist_ok=True)
doc = SimpleDocTemplate(str(out_path), pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)
story = []

story.append(Paragraph(f"Practical Rubric: {src['title']}", title_style))
story.append(Paragraph("CAET Advanced — Evaluator Scoring Sheet", styles['Italic']))
story.append(Spacer(1, 0.1*inch))

# Header fields
story.append(Paragraph("Evaluator: _________________ Student: _________________ Date: _____________", styles['Normal']))
story.append(Spacer(1, 0.2*inch))

# One Accept/Reject table per task
for t in src["tasks"]:
    story.append(Paragraph(t["heading"], task_style))
    # Split body into accept/reject heuristic: take first 3 sentences as accept criteria,
    # derive inversions as reject criteria
    sentences = [s.strip() for s in t["body"].split(".") if s.strip()][:4]
    accept_items = sentences[:3] if len(sentences) >= 3 else sentences
    reject_items = ["Criteria not met — see accept column", "Missed step or incorrect technique",
                    "Unsafe practice observed", "Did not complete in allotted time"][:len(accept_items)]

    accept_cell = "☐ " + "<br/>☐ ".join(accept_items)
    reject_cell = "☐ " + "<br/>☐ ".join(reject_items)

    data = [["ACCEPT", "REJECT"], [Paragraph(accept_cell, styles['Normal']), Paragraph(reject_cell, styles['Normal'])]]
    tbl = Table(data, colWidths=[3.25*inch, 3.25*inch])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), colors.HexColor("#d1fae5")),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor("#fee2e2")),
        ('TEXTCOLOR', (0,0), (0,0), colors.HexColor("#065f46")),
        ('TEXTCOLOR', (1,0), (1,0), colors.HexColor("#991b1b")),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOX', (0,0), (-1,-1), 0.5, colors.black),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 0.15*inch))

# Scoring summary
story.append(PageBreak())
story.append(Paragraph("Scoring", task_style))
story.append(Paragraph(f"{len(src['tasks'])}/{len(src['tasks'])} tasks passed: PASS", styles['Normal']))
story.append(Paragraph(f"{len(src['tasks'])-1}/{len(src['tasks'])} with remediation plan: CONDITIONAL PASS (30-day retest)", styles['Normal']))
story.append(Paragraph(f"Less than {len(src['tasks'])-1}: FAIL (module retake required)", styles['Normal']))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("Evaluator Signature: _______________________", styles['Normal']))

doc.build(story)
print(f"Wrote {out_path}")
```

**Step 2: Run + verify**

```bash
python tools/training_pipeline/gen_rubric.py \
  "C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/staging/adv10_source.json" \
  "advanced/training/adv10-wire-harness-fabrication/training/practical-rubric.pdf"
```

Verify: one 2-column Accept/Reject table per task, header fields, scoring summary at end.

**Step 3: Commit**

```bash
git add tools/training_pipeline/gen_rubric.py advanced/training/adv10-wire-harness-fabrication/training/practical-rubric.pdf
git commit -m "feat: add practical rubric PDF generator + adv10 pilot"
```

---

### Task 9: Update adv10 module hub with "Study First" card row

**Files:**
- Modify: `advanced/training/adv10-wire-harness-fabrication/index.html`

**Step 1: Open file + identify insertion point**

Find the section in `index.html` that renders the activity cards (Drill, Flashcards, Final Test). The section has a heading or grid container. Insert a new "Study First" section directly above.

**Step 2: Add Study First HTML block**

Inject above the existing activity grid:

```html
<!-- STUDY FIRST CARD ROW -->
<h2 style="color:var(--gold); margin: 30px 0 16px; font-size: 18px; text-transform: uppercase; letter-spacing: 1.5px;">Study First</h2>
<div class="activity-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 40px;">
  <a href="training/handbook.html" target="_blank" class="activity-card">
    <div class="activity-icon">📖</div>
    <div class="activity-title">Handbook</div>
    <div class="activity-desc">Full study guide</div>
  </a>
  <a href="training/lesson.html" target="_blank" class="activity-card">
    <div class="activity-icon">💡</div>
    <div class="activity-title">Interactive Lesson</div>
    <div class="activity-desc">25 min · 5E format</div>
  </a>
  <a href="training/lesson-plan.pdf" target="_blank" class="activity-card">
    <div class="activity-icon">👨‍🏫</div>
    <div class="activity-title">Lesson Plan</div>
    <div class="activity-desc">Instructor guide</div>
  </a>
  <a href="training/job-aid.pdf" target="_blank" class="activity-card">
    <div class="activity-icon">📋</div>
    <div class="activity-title">Job Aid</div>
    <div class="activity-desc">1-page reference</div>
  </a>
  <a href="training/worksheet.pdf" target="_blank" class="activity-card">
    <div class="activity-icon">✏️</div>
    <div class="activity-title">Worksheet</div>
    <div class="activity-desc">Practice problems</div>
  </a>
  <a href="training/practical-rubric.pdf" target="_blank" class="activity-card">
    <div class="activity-icon">✅</div>
    <div class="activity-title">Practical Rubric</div>
    <div class="activity-desc">Evaluator sheet</div>
  </a>
</div>
<!-- /STUDY FIRST -->
```

**Step 3: Open in browser to verify**

Open: `advanced/training/adv10-wire-harness-fabrection/index.html`
Verify: Study First section appears above existing Drill/Flashcards/Final Test cards. All 6 cards clickable. Links open correct artifacts.

**Step 4: Commit**

```bash
git add advanced/training/adv10-wire-harness-fabrication/index.html
git commit -m "feat: add Study First section to adv10 module hub"
```

---

### Task 10: Deploy pilot + user approval checkpoint

**Step 1: Push to GitHub**

```bash
git push origin main
```

**Step 2: Wait for GitHub Pages deploy**

```bash
until curl -s -o /dev/null -w "%{http_code}" "https://00ainick-cmd.github.io/caet-practice-public/advanced/training/adv10-wire-harness-fabrication/training/handbook.html?v=$(date +%s)" | grep -q "200"; do sleep 5; done
echo "LIVE"
```

**Step 3: User validation**

Tell user: "Pilot module live at https://00ainick-cmd.github.io/caet-practice-public/advanced/training/adv10-wire-harness-fabrication/ — please open the Study First cards and review all 6 artifacts."

**Step 4: STOP — await user approval**

Do NOT proceed to Phase 2 until user says "approved" or equivalent. If user requests changes, return to the relevant Task 1-9 and iterate.

---

## Phase 2: Bulk Production — 14 Remaining Modules (Tasks 11-17)

### Task 11: Map all 14 remaining modules to source docx + build manifest

**Files:**
- Create: `tools/training_pipeline/module_manifest.json`

**Step 1: Write manifest**

```json
{
  "modules": [
    {"slug": "adv1", "dir": "cabin-management-systems", "source_docx": "14-Cabin-Management-Systems.docx"},
    {"slug": "adv2", "dir": "connectivity", "source_docx": "12-EFB-Connectivity.docx"},
    {"slug": "adv3", "dir": "datalink-fundamentals", "source_docx": "15-Datalink-Fundamentals.docx"},
    {"slug": "adv4", "dir": "flight-management-systems", "source_docx": "13-Flight-Management-Systems.docx"},
    {"slug": "adv5", "dir": "attitude-heading-reference", "source_docx": "16-AHRS-Attitude-Heading-Reference.docx"},
    {"slug": "adv6", "dir": "audio-panels", "source_docx": "05-Audio-Panel-Intercom.docx"},
    {"slug": "adv7", "dir": "nav-com-systems", "source_docx": "06-Navigation-Systems.docx"},
    {"slug": "adv8", "dir": "14-cfr-65-91", "source_docx": "01-Regulatory-Compliance-Approved-Data.docx"},
    {"slug": "adv9", "dir": "smart-probes-air-data", "source_docx": "17-Smart-Probes-Air-Data.docx"},
    {"slug": "adv11", "dir": "autopilot-systems", "source_docx": "10-Autopilot-Systems.docx"},
    {"slug": "adv12", "dir": "transponders-ads-b", "source_docx": "08-Transponder-ADSB.docx"},
    {"slug": "adv13", "dir": "documentation", "source_docx": "02-Maintenance-Documentation.docx"},
    {"slug": "adv14", "dir": "software-database-loading", "source_docx": "18-Software-Database-Loading.docx"},
    {"slug": "adv15", "dir": "emergency-autoland", "source_docx": null, "note": "No direct source - use PQS Standards v5 + supplementary refs"}
  ]
}
```

**Step 2: Save + commit**

```bash
git add tools/training_pipeline/module_manifest.json
git commit -m "chore: manifest of 14 remaining modules + source mapping"
```

---

### Task 12: Extract source for all 13 modules with docx (skip adv15)

**Step 1: Batch extract**

```bash
for slug in adv1 adv2 adv3 adv4 adv5 adv6 adv7 adv8 adv9 adv11 adv12 adv13 adv14; do
  python -c "
import json, sys
m = json.load(open('tools/training_pipeline/module_manifest.json'))['modules']
target = [x for x in m if x['slug'] == '$slug'][0]
print(target['source_docx'])
" | xargs -I {} python tools/training_pipeline/extract_source.py \
    "C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/training_source/{}" \
    "C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/staging/${slug}_source.json"
done
```

**Step 2: Verify all 13 JSON files exist**

```bash
ls "C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/staging/"adv*_source.json | wc -l
```
Expected: 14 (13 new + 1 adv10 pilot)

**Step 3: Commit**

```bash
# Staging files live outside repo; just commit a marker
echo "extraction-complete: 13 modules" > tools/training_pipeline/extraction.log
git add tools/training_pipeline/extraction.log
git commit -m "chore: extracted source JSON for 13 modules"
```

---

### Task 13: Run all 6 generators against each of the 13 modules

**Step 1: Build master generator loop**

Create `tools/training_pipeline/generate_all.sh`:

```bash
#!/bin/bash
MODULES=(adv1 adv2 adv3 adv4 adv5 adv6 adv7 adv8 adv9 adv11 adv12 adv13 adv14)
declare -A DIRS=(
  [adv1]="cabin-management-systems" [adv2]="connectivity" [adv3]="datalink-fundamentals"
  [adv4]="flight-management-systems" [adv5]="attitude-heading-reference" [adv6]="audio-panels"
  [adv7]="nav-com-systems" [adv8]="14-cfr-65-91" [adv9]="smart-probes-air-data"
  [adv11]="autopilot-systems" [adv12]="transponders-ads-b" [adv13]="documentation"
  [adv14]="software-database-loading"
)

for slug in "${MODULES[@]}"; do
  dir="${DIRS[$slug]}"
  src="C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/staging/${slug}_source.json"
  out_dir="advanced/training/${slug}-${dir}/training"
  mkdir -p "$out_dir"
  python tools/training_pipeline/gen_handbook.py "$src" "$out_dir/handbook.html"
  python tools/training_pipeline/gen_lesson.py "$src" "$out_dir/lesson.html"
  python tools/training_pipeline/gen_lesson_plan.py "$src" "$out_dir/lesson-plan.pdf"
  python tools/training_pipeline/gen_job_aid.py "$src" "$out_dir/job-aid.pdf"
  python tools/training_pipeline/gen_worksheet.py "$src" "$out_dir/worksheet.pdf"
  python tools/training_pipeline/gen_rubric.py "$src" "$out_dir/practical-rubric.pdf"
  echo "Done: $slug"
done
```

**Step 2: Run**

```bash
chmod +x tools/training_pipeline/generate_all.sh
bash tools/training_pipeline/generate_all.sh
```

Expected: 13 × 6 = 78 artifacts generated (plus handbook.pdf from weasyprint in handbook generator).

**Step 3: Verify file counts**

```bash
ls advanced/training/adv*-*/training/ | grep -v '^$' | sort -u | wc -l
```
Expected: ~84 files (14 modules × 6 artifacts, adv15 still empty at this point).

**Step 4: Commit**

```bash
git add advanced/training/adv*/training/
git commit -m "feat: generate training artifacts for 13 modules"
```

---

### Task 14: Handle adv15 (Emergency Autoland) — no source docx

**Step 1: Ask user for supplementary source**

Tell user: "adv15 Emergency Autoland has no source docx. Options:
(a) You provide a reference document
(b) I derive content from PQS Standards v5 + publicly available EAL documentation (Garmin Autoland, FAA Advisory docs)
(c) Skip adv15 for this pilot; add manually later"

**Step 2: Based on user answer, produce adv15 artifacts OR skip**

If (a): extract user's document and run through pipeline as normal.
If (b): dispatch an agent to author source-like JSON from EAL domain knowledge, then run pipeline.
If (c): flag adv15 in module hub with "Training coming soon" message; skip.

**Step 3: Commit**

```bash
git add advanced/training/adv15-emergency-autoland/
git commit -m "feat: training artifacts for adv15 Emergency Autoland"
```

---

### Task 15: Update all 14 remaining module hubs with Study First sections

**Step 1: Write batch updater**

Create `tools/training_pipeline/add_study_first.py`:

```python
import sys
from pathlib import Path

MODULES = [
    ("adv1", "cabin-management-systems"), ("adv2", "connectivity"),
    ("adv3", "datalink-fundamentals"), ("adv4", "flight-management-systems"),
    ("adv5", "attitude-heading-reference"), ("adv6", "audio-panels"),
    ("adv7", "nav-com-systems"), ("adv8", "14-cfr-65-91"),
    ("adv9", "smart-probes-air-data"), ("adv11", "autopilot-systems"),
    ("adv12", "transponders-ads-b"), ("adv13", "documentation"),
    ("adv14", "software-database-loading"), ("adv15", "emergency-autoland"),
]

STUDY_FIRST_BLOCK = """
<!-- STUDY FIRST CARD ROW -->
<h2 style="color:var(--gold); margin: 30px 0 16px; font-size: 18px; text-transform: uppercase; letter-spacing: 1.5px;">Study First</h2>
<div class="activity-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 40px;">
  <a href="training/handbook.html" target="_blank" class="activity-card"><div class="activity-icon">📖</div><div class="activity-title">Handbook</div><div class="activity-desc">Full study guide</div></a>
  <a href="training/lesson.html" target="_blank" class="activity-card"><div class="activity-icon">💡</div><div class="activity-title">Interactive Lesson</div><div class="activity-desc">25 min · 5E format</div></a>
  <a href="training/lesson-plan.pdf" target="_blank" class="activity-card"><div class="activity-icon">👨‍🏫</div><div class="activity-title">Lesson Plan</div><div class="activity-desc">Instructor guide</div></a>
  <a href="training/job-aid.pdf" target="_blank" class="activity-card"><div class="activity-icon">📋</div><div class="activity-title">Job Aid</div><div class="activity-desc">1-page reference</div></a>
  <a href="training/worksheet.pdf" target="_blank" class="activity-card"><div class="activity-icon">✏️</div><div class="activity-title">Worksheet</div><div class="activity-desc">Practice problems</div></a>
  <a href="training/practical-rubric.pdf" target="_blank" class="activity-card"><div class="activity-icon">✅</div><div class="activity-title">Practical Rubric</div><div class="activity-desc">Evaluator sheet</div></a>
</div>
<!-- /STUDY FIRST -->
"""

for slug, dir_name in MODULES:
    idx_path = Path(f"advanced/training/{slug}-{dir_name}/index.html")
    content = idx_path.read_text(encoding="utf-8")
    if "STUDY FIRST" in content:
        print(f"skip {slug} (already added)")
        continue
    # Insert before the existing activity-grid
    marker = '<div class="activity-grid"'
    if marker not in content:
        print(f"WARN: no insertion marker in {slug}")
        continue
    new_content = content.replace(marker, STUDY_FIRST_BLOCK + "\n" + marker, 1)
    idx_path.write_text(new_content, encoding="utf-8")
    print(f"updated {slug}")
```

**Step 2: Run + verify**

```bash
python tools/training_pipeline/add_study_first.py
```
Expected: 14 "updated advN" lines.

Spot-check 2-3 random index.html files — verify STUDY FIRST block present.

**Step 3: Commit**

```bash
git add advanced/training/*/index.html
git commit -m "feat: add Study First card row to 14 module hubs"
```

---

### Task 16: QA — link integrity + PDF render check across all 15 modules

**Step 1: Write verification script**

Create `tools/training_pipeline/verify.py`:

```python
import sys, subprocess
from pathlib import Path

MODULES_ROOT = Path("advanced/training")
EXPECTED_ARTIFACTS = ["handbook.html", "handbook.pdf", "lesson.html",
                      "lesson-plan.pdf", "job-aid.pdf", "worksheet.pdf", "practical-rubric.pdf"]

failures = []
for mod_dir in sorted(MODULES_ROOT.iterdir()):
    if not mod_dir.is_dir(): continue
    training_dir = mod_dir / "training"
    if not training_dir.exists():
        failures.append(f"{mod_dir.name}: no training/ subdir")
        continue
    for artifact in EXPECTED_ARTIFACTS:
        f = training_dir / artifact
        if not f.exists():
            failures.append(f"{mod_dir.name}: missing {artifact}")
            continue
        if f.suffix == ".pdf" and f.stat().st_size < 1000:
            failures.append(f"{mod_dir.name}/{artifact}: suspiciously small ({f.stat().st_size} bytes)")

if failures:
    print("FAILURES:")
    for f in failures: print(f"  {f}")
    sys.exit(1)
else:
    print(f"✓ All 15 modules have all 7 expected artifacts")
```

**Step 2: Run verification**

```bash
python tools/training_pipeline/verify.py
```
Expected: `✓ All 15 modules have all 7 expected artifacts` (or fix failures and re-run).

**Step 3: Commit**

```bash
git add tools/training_pipeline/verify.py
git commit -m "chore: add training artifacts verification script"
```

---

## Phase 3: Deploy + Final Validation (Tasks 17-19)

### Task 17: Push + wait for GitHub Pages deploy

**Step 1: Push**

```bash
git push origin main
```

**Step 2: Wait for live**

```bash
until curl -s -o /dev/null -w "%{http_code}" "https://00ainick-cmd.github.io/caet-practice-public/advanced/training/adv1-cabin-management-systems/training/handbook.html?v=$(date +%s)" | grep -q "200"; do sleep 5; done
echo "LIVE"
```

---

### Task 18: Cross-module live-site smoke test

**Step 1: Fetch random sample of artifacts from live**

```bash
for slug in adv3 adv7 adv11 adv14; do
  for art in handbook.html handbook.pdf lesson.html lesson-plan.pdf job-aid.pdf worksheet.pdf practical-rubric.pdf; do
    status=$(curl -s -o /dev/null -w "%{http_code}" "https://00ainick-cmd.github.io/caet-practice-public/advanced/training/${slug}-*/training/${art}?v=$(date +%s)")
    echo "$slug $art: $status"
  done
done
```
Expected: all 200.

---

### Task 19: Final user validation

Tell user: "Training materials deployed live. Please spot-check 3-5 modules:

1. Open `/advanced/training/adv1-cabin-management-systems/` → verify Study First cards load all 6 artifacts
2. Open `/advanced/training/adv11-autopilot-systems/` → same check
3. Open `/advanced/training/adv4-flight-management-systems/` → same check
4. Sample the handbook.html content — does it read right?
5. Try the lesson.html 5E flow — engage → explore → ... → quiz

Report any broken artifacts or content issues."

Task complete when user confirms all 15 modules check out.

---

## Open Questions to Revisit During Execution

- **PDF styling polish** — the reportlab-generated PDFs are functional but plain. After pilot, do we want a visual-design pass (consistent branding, better typography)? If yes, add a Task between Phase 1 approval and Phase 2 kickoff.
- **adv15 Emergency Autoland source** — resolution needed at Task 14.
- **Quiz data integration on lesson.html** — current template just links to drill.html. Future enhancement: embed 10 questions directly in lesson.html for in-context quiz. Out of scope for v1.

---

## Summary

19 tasks across 3 phases:
- **Phase 0 (Task 0):** Environment setup + source staging
- **Phase 1 (Tasks 1-10):** Pilot adv10 Wire Harness — 6 artifacts + module hub + deploy + user approval
- **Phase 2 (Tasks 11-16):** Bulk production for 14 remaining modules + QA
- **Phase 3 (Tasks 17-19):** Live deploy + cross-module validation

Estimated agent time: ~3-4 hours for Phase 1 pilot, ~30 min for Phase 2 bulk (batch-parallel), ~15 min for Phase 3.

Frequent commits at every task boundary. Each task takes 2-15 minutes. DRY (one pipeline serves all 15 modules). YAGNI (no React apps, no separate lab sheets).
