"""Render the worksheet.pdf (pre-drill practice problems) with answer key for one module."""
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

# Oral board questions as scenario-based worksheet problems
for i, q in enumerate(src["oral_board_questions"], 1):
    story.append(Paragraph(f"Problem {i}", q_style))
    story.append(Paragraph(q, styles['Normal']))
    story.append(Paragraph("___________________________________________<br/>___________________________________________<br/>___________________________________________", space_style))

# Additional procedure fill-in problems from tasks
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
