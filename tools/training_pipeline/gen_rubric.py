"""Render the practical-rubric.pdf evaluator scoring sheet.

Uses enrichment's evaluator_watching_for as specific ACCEPT criteria and
common_mistakes as specific REJECT criteria (rather than generic boilerplate).
"""
import json, sys
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.units import inch
from reportlab.lib import colors

SCRIPT_DIR = Path(__file__).parent
import sys as _sys
_sys.path.insert(0, str(SCRIPT_DIR))
from merge import effective_tasks

NAVY = colors.HexColor("#0a2540")
GOLD = colors.HexColor("#8b6914")
GREEN_SOFT = colors.HexColor("#e7f0e5")
GREEN = colors.HexColor("#1b4332")
RED_SOFT = colors.HexColor("#fbe9e7")
RED = colors.HexColor("#8b1a1a")
PAPER_ACCENT = colors.HexColor("#f5f2e8")
RULE = colors.HexColor("#d8d3c3")

def load_enrichment(slug):
    f = SCRIPT_DIR / "enrichment" / f"{slug}.json"
    return json.load(f.open("r", encoding="utf-8")) if f.exists() else {
        "task_enrichment": {},
    }

def infer_slug(p):
    n = p.stem
    return n.split("_")[0] if "_" in n else n

def match_key(h):
    if not h: return ""
    return h.split("—")[0].split("–")[0].strip().split(" ")[-1]

def main():
    src_path, out_path = Path(sys.argv[1]), Path(sys.argv[2])
    slug = infer_slug(src_path)
    for arg in sys.argv[3:]:
        if arg.startswith("--slug="):
            slug = arg.split("=", 1)[1]

    src = json.load(src_path.open("r", encoding="utf-8"))
    enr = load_enrichment(slug)
    tasks = effective_tasks(src, enr)

    base = getSampleStyleSheet()
    h1 = ParagraphStyle('H1', parent=base['Title'], textColor=NAVY, fontName='Helvetica-Bold',
                        fontSize=18, leading=22, alignment=0, spaceAfter=4)
    h2 = ParagraphStyle('H2', parent=base['Heading2'], textColor=GOLD, fontName='Helvetica-Bold',
                        fontSize=11, leading=14, spaceBefore=14, spaceAfter=4)
    task_h = ParagraphStyle('TaskH', parent=base['Normal'], textColor=NAVY, fontName='Helvetica-Bold',
                            fontSize=11, leading=14, spaceBefore=10, spaceAfter=4)
    body = ParagraphStyle('Body', parent=base['Normal'], fontName='Helvetica', fontSize=9.5,
                          leading=13, textColor=colors.HexColor("#1a2332"))
    cell_a = ParagraphStyle('CellA', parent=body, fontSize=9, leading=11, textColor=GREEN)
    cell_r = ParagraphStyle('CellR', parent=body, fontSize=9, leading=11, textColor=RED)
    header_cell = ParagraphStyle('Hc', parent=base['Normal'], fontName='Helvetica-Bold',
                                 fontSize=10, alignment=1)
    italic = ParagraphStyle('Italic', parent=body, fontName='Helvetica-Oblique',
                            textColor=colors.HexColor("#4a5568"))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(out_path), pagesize=letter,
                            topMargin=0.5*inch, bottomMargin=0.5*inch,
                            leftMargin=0.6*inch, rightMargin=0.6*inch,
                            title=f"Practical Rubric — {src['title']}")
    story = []

    story.append(Paragraph(f"Practical Rubric: {src['title']}", h1))
    story.append(Paragraph("CAET Advanced · Evaluator Scoring Sheet", italic))
    story.append(Spacer(1, 0.08*inch))

    # Header info fields
    hdr = [
        ["Evaluator:", "", "Student:", "", "Date:", ""],
    ]
    t = Table(hdr, colWidths=[0.9*inch, 1.55*inch, 0.8*inch, 1.55*inch, 0.6*inch, 1.3*inch])
    t.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,0), 'Helvetica-Bold'),
        ('FONTNAME', (2,0), (2,0), 'Helvetica-Bold'),
        ('FONTNAME', (4,0), (4,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9.5),
        ('LINEBELOW', (1,0), (1,0), 0.5, colors.black),
        ('LINEBELOW', (3,0), (3,0), 0.5, colors.black),
        ('LINEBELOW', (5,0), (5,0), 0.5, colors.black),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.12*inch))

    story.append(Paragraph("SCORING INSTRUCTIONS", h2))
    story.append(Paragraph(
        "Check each criterion observed. Accept a task when ALL critical accept-criteria are demonstrated and NO reject-criteria are triggered. "
        "Write specific observations in the margin — scoring decisions must be defensible if the student appeals.",
        body
    ))
    story.append(Spacer(1, 0.1*inch))

    # One table per task with real accept/reject criteria from enrichment
    for task in tasks:
        k = match_key(task["heading"])
        e = enr.get("task_enrichment", {}).get(k, {})
        accept = e.get("evaluator_watching_for", [])
        reject = e.get("common_mistakes", [])

        # Fall back to source-derived if enrichment missing
        if not accept and task.get("body"):
            sentences = [s.strip() for s in task["body"].split(".") if s.strip()][:3]
            accept = sentences
        if not reject:
            reject = ["Criterion not met — see accept column",
                      "Unsafe practice observed",
                      "Did not complete in allotted time"]

        # Pad both columns to equal length so cells align
        max_len = max(len(accept), len(reject))
        while len(accept) < max_len: accept.append("")
        while len(reject) < max_len: reject.append("")

        rows = [[
            Paragraph("<b>ACCEPT — observed</b>", header_cell),
            Paragraph("<b>REJECT — triggered</b>", header_cell),
        ]]
        for a, r in zip(accept, reject):
            rows.append([
                Paragraph(f"☐ {a}" if a else "", cell_a),
                Paragraph(f"☐ {r}" if r else "", cell_r),
            ])

        tbl = Table(rows, colWidths=[3.65*inch, 3.65*inch])
        tbl.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (0,0), GREEN_SOFT),
            ('BACKGROUND', (1,0), (1,0), RED_SOFT),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('FONTSIZE', (0,0), (-1,-1), 9),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('RIGHTPADDING', (0,0), (-1,-1), 6),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
            ('BOX', (0,0), (-1,-1), 0.5, colors.black),
            ('INNERGRID', (0,0), (-1,-1), 0.25, RULE),
        ]))

        # Add task-scoring row below table
        score_row = Table([[
            Paragraph(f"<b>Task result:</b>  ☐ PASS  ☐ CONDITIONAL  ☐ FAIL",
                      ParagraphStyle('scr', parent=body, fontSize=9.5)),
            Paragraph("Notes: ___________________________________________________",
                      ParagraphStyle('nt', parent=body, fontSize=9)),
        ]], colWidths=[2.2*inch, 5.1*inch])
        score_row.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), PAPER_ACCENT),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('RIGHTPADDING', (0,0), (-1,-1), 6),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
            ('BOX', (0,0), (-1,-1), 0.5, colors.black),
        ]))

        story.append(KeepTogether([
            Paragraph(task["heading"], task_h),
            tbl,
            score_row,
            Spacer(1, 0.1*inch),
        ]))

    # Final scoring summary
    story.append(PageBreak())
    story.append(Paragraph("Overall Scoring", h2))
    total = len(tasks)
    summary_rows = [
        ["Tasks PASSED", "Result", "Remediation"],
        [f"{total}/{total}", "PASS — candidate is qualified", "None"],
        [f"{total-1}/{total}", "CONDITIONAL PASS", "Retest failed task within 30 days"],
        [f"<{total-1}/{total}", "FAIL", "Re-attempt entire module after documented instruction"],
    ]
    t = Table(summary_rows, colWidths=[1.5*inch, 3.0*inch, 2.8*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('GRID', (0,0), (-1,-1), 0.5, RULE),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.3*inch))

    story.append(Paragraph("Evaluator Signature: _______________________________________________",
                           ParagraphStyle('sig', parent=body, fontSize=10.5, spaceBefore=20)))
    story.append(Spacer(1, 0.15*inch))
    story.append(Paragraph("Evaluator Certificate #: ________________________________________",
                           ParagraphStyle('sig2', parent=body, fontSize=10.5)))
    story.append(Spacer(1, 0.15*inch))
    story.append(Paragraph("Student Signature (acknowledges results): ______________________",
                           ParagraphStyle('sig3', parent=body, fontSize=10.5)))

    doc.build(story)
    print(f"Wrote {out_path}")

if __name__ == "__main__":
    main()
