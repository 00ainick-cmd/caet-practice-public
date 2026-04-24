"""Render the 1-page job-aid.pdf (quick reference) for one module using reportlab."""
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
    body = kr["body"]
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
