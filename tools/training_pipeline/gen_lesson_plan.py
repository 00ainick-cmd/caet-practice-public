"""Render the lesson-plan.pdf (instructor guide) for one module using reportlab.

Merges source + enrichment content so instructors see:
- Why This Matters narrative to hook students
- Per-KR teaching points (theory overview + key bullets)
- Per-task step-by-step procedures with evaluator criteria
- Common mistakes to watch for and preemptively address
- Oral board answer key
"""
import json, sys
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, ListFlowable, ListItem, KeepTogether
from reportlab.lib.units import inch
from reportlab.lib import colors

SCRIPT_DIR = Path(__file__).parent
import sys as _sys
_sys.path.insert(0, str(SCRIPT_DIR))
from merge import effective_tasks, effective_oral

NAVY = colors.HexColor("#0a2540")
GOLD = colors.HexColor("#8b6914")
PAPER = colors.HexColor("#fbfaf5")
PAPER_ACCENT = colors.HexColor("#f5f2e8")
CYAN = colors.HexColor("#0e4a6e")
GREEN_SOFT = colors.HexColor("#e7f0e5")
RED_SOFT = colors.HexColor("#fbe9e7")
GOLD_SOFT = colors.HexColor("#f4ead0")
RULE = colors.HexColor("#d8d3c3")

def load_enrichment(slug):
    f = SCRIPT_DIR / "enrichment" / f"{slug}.json"
    return json.load(f.open("r", encoding="utf-8")) if f.exists() else {
        "why_this_matters": [], "key_terms": [], "knowledge_enrichment": {},
        "task_enrichment": {}, "oral_board_answers": {}, "background_theory": {},
    }

def infer_slug(p):
    n = p.stem
    return n.split("_")[0] if "_" in n else n

def match_key(heading):
    """Extract section key like '4.2.1' or '4.4.1' from a heading string."""
    if not heading: return ""
    return heading.split("—")[0].split("–")[0].strip().split(" ")[-1]

def main():
    src_path, out_path = Path(sys.argv[1]), Path(sys.argv[2])
    slug = infer_slug(src_path)
    for arg in sys.argv[3:]:
        if arg.startswith("--slug="):
            slug = arg.split("=", 1)[1]

    src = json.load(src_path.open("r", encoding="utf-8"))
    enr = load_enrichment(slug)
    tasks = effective_tasks(src, enr)
    oral_questions = effective_oral(src, enr)

    base = getSampleStyleSheet()
    h1 = ParagraphStyle('H1', parent=base['Title'], textColor=NAVY, fontName='Helvetica-Bold',
                        fontSize=20, leading=24, spaceAfter=4)
    h2 = ParagraphStyle('H2', parent=base['Heading2'], textColor=NAVY, fontName='Helvetica-Bold',
                        fontSize=14, leading=17, spaceBefore=16, spaceAfter=8)
    h3 = ParagraphStyle('H3', parent=base['Heading3'], textColor=NAVY, fontName='Helvetica-Bold',
                        fontSize=12, leading=15, spaceBefore=12, spaceAfter=6)
    h4 = ParagraphStyle('H4', parent=base['Normal'], textColor=GOLD, fontName='Helvetica-Bold',
                        fontSize=10, leading=12, spaceBefore=10, spaceAfter=4)
    body = ParagraphStyle('Body', parent=base['Normal'], fontName='Helvetica', fontSize=10,
                          leading=14, spaceAfter=6, textColor=colors.HexColor("#1a2332"))
    italic = ParagraphStyle('Italic', parent=body, fontName='Helvetica-Oblique')
    bullet = ParagraphStyle('Bullet', parent=body, leftIndent=16, bulletIndent=4, spaceAfter=3)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(out_path), pagesize=letter,
                            topMargin=0.6*inch, bottomMargin=0.6*inch,
                            leftMargin=0.75*inch, rightMargin=0.75*inch,
                            title=f"Lesson Plan — {src['title']}")
    story = []

    # Cover
    story.append(Paragraph("INSTRUCTOR LESSON PLAN", ParagraphStyle('eyebrow', parent=body,
                           textColor=GOLD, fontName='Helvetica-Bold', fontSize=10,
                           alignment=0, spaceAfter=2)))
    story.append(Paragraph(src["title"], h1))
    story.append(Paragraph("CAET Advanced Certification · Aircraft Electronics Association", italic))
    story.append(Spacer(1, 0.12*inch))

    # Summary table
    summary = [
        ["Duration", "3 hours (90 min direct + 90 min lab)"],
        ["Class size", "6–12 students, 1 instructor"],
        ["Prerequisites", "Handbook chapters 1–3 read; basic multimeter familiarity"],
        ["Materials", "Per-student harness kit; shared megger, crimp tools, pegboards"],
        ["Assessment", "In-class worksheet (formative) · drill ≥80% (gate) · practical rubric (summative)"],
    ]
    t = Table(summary, colWidths=[1.3*inch, 5.0*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), PAPER_ACCENT),
        ('TEXTCOLOR', (0,0), (0,-1), NAVY),
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LINEBELOW', (0,0), (-1,-1), 0.25, RULE),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.15*inch))

    # Why this matters (hook for instructor)
    if enr.get("why_this_matters"):
        story.append(Paragraph("Opening Hook — Why Students Should Care", h2))
        story.append(Paragraph("Read or paraphrase the following aloud before starting direct instruction. It sets the stakes.", italic))
        for para in enr["why_this_matters"]:
            story.append(Paragraph(para, body))

    # Minute-by-minute agenda
    story.append(PageBreak())
    story.append(Paragraph("Minute-by-Minute Agenda", h2))
    agenda = [
        ["Time", "Activity", "Notes / Materials"],
        ["0:00–0:10", "Opening hook + learning objectives", "Use the 'Why Students Should Care' script"],
        ["0:10–0:40", "Direct instruction: Knowledge Requirements 1 & 2", "Whiteboard + handbook §2–3; stop for questions every 10 min"],
        ["0:40–1:00", "Instructor demo: first task", "Stage at front bench; narrate each step with rationale"],
        ["1:00–1:30", "Student hands-on: practice first task", "Circulate; note common mistakes (see callouts below)"],
        ["1:30–1:45", "BREAK", ""],
        ["1:45–2:05", "Direct instruction: Knowledge Requirement 3 + theory", "Focus on oral-board depth; use background-theory callouts"],
        ["2:05–2:25", "Instructor demo: second task", "Especially safety steps — do not rush"],
        ["2:25–2:55", "Student hands-on: second task + self-check", "Worksheet problems 1–5 as exit ticket"],
        ["2:55–3:00", "Wrap-up, Q&A, preview next session", ""],
    ]
    t = Table(agenda, colWidths=[0.95*inch, 2.3*inch, 3.05*inch], repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('GRID', (0,0), (-1,-1), 0.25, RULE),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t)

    # Teaching points per KR
    story.append(PageBreak())
    story.append(Paragraph("Teaching Points — Knowledge Requirements", h2))
    for kr in src["knowledge_requirements"]:
        k = match_key(kr["heading"])
        e = enr.get("knowledge_enrichment", {}).get(k, {})
        story.append(Paragraph(kr["heading"], h3))
        if e.get("overview"):
            story.append(Paragraph(e["overview"], body))
        if kr.get("body"):
            story.append(Paragraph(kr["body"], body))
        if e.get("key_points"):
            story.append(Paragraph("Key points to cover:", h4))
            story.append(ListFlowable(
                [ListItem(Paragraph(p, bullet), leftIndent=14) for p in e["key_points"]],
                bulletType='bullet', start='•',
            ))

    # Task-by-task instructor notes
    story.append(PageBreak())
    story.append(Paragraph("Task-by-Task Instructor Notes", h2))
    for task in tasks:
        k = match_key(task["heading"])
        e = enr.get("task_enrichment", {}).get(k, {})
        story.append(Paragraph(task["heading"], h3))
        if task.get("body"):
            story.append(Paragraph(task["body"], body))
        if e.get("step_by_step"):
            story.append(Paragraph("Demonstrate these steps:", h4))
            story.append(ListFlowable(
                [ListItem(Paragraph(s, bullet), leftIndent=14) for s in e["step_by_step"]],
                bulletType='1', start='1',
            ))
        if e.get("evaluator_watching_for"):
            story.append(Paragraph("Evaluator will watch for (tell students this):", h4))
            story.append(ListFlowable(
                [ListItem(Paragraph(s, bullet), leftIndent=14) for s in e["evaluator_watching_for"]],
                bulletType='bullet', start='✓',
            ))
        if e.get("common_mistakes"):
            story.append(Paragraph("Common mistakes — intervene when you see:", h4))
            story.append(ListFlowable(
                [ListItem(Paragraph(s, bullet), leftIndent=14) for s in e["common_mistakes"]],
                bulletType='bullet', start='✗',
            ))

    # Oral board Q&A prep
    story.append(PageBreak())
    story.append(Paragraph("Oral Board Practice — Ask Students These", h2))
    for q in oral_questions:
        qnum = q.split(":")[0].strip()
        answer = enr.get("oral_board_answers", {}).get(qnum)
        story.append(Paragraph(q, h4))
        if answer:
            story.append(Paragraph(f"<b>Expected answer framework:</b> {answer}", body))
        story.append(Spacer(1, 0.08*inch))

    doc.build(story)
    print(f"Wrote {out_path}")

if __name__ == "__main__":
    main()
