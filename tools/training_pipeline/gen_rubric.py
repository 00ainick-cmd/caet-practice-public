"""Render the practical-rubric.pdf evaluator scoring sheet (Accept/Reject per task) for one module."""
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

story.append(Paragraph("Evaluator: _________________ Student: _________________ Date: _____________", styles['Normal']))
story.append(Spacer(1, 0.2*inch))

# One Accept/Reject table per task
for t in src["tasks"]:
    story.append(Paragraph(t["heading"], task_style))
    # Derive accept criteria: first 3 sentences from body. Reject: standard boilerplate.
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
