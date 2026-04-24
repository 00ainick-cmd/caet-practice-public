"""Render the lesson-plan.pdf (instructor guide) for one module using reportlab."""
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

story.append(Paragraph("Duration &amp; Format", h2_style))
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

story.append(Paragraph("Oral Board Q&amp;A Prep (ask students these)", h2_style))
for q in src["oral_board_questions"]:
    story.append(Paragraph(q, styles['Normal']))
    story.append(Spacer(1, 0.05*inch))

doc.build(story)
print(f"Wrote {out_path}")
