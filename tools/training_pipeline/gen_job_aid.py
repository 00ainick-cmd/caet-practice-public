"""Render the job-aid.pdf — a dense 1-2 page quick reference card for the evaluator day.

Pulls the most mission-critical bullets from the enrichment: key terms (top 6),
evaluator accept criteria per task (top 2 each), and the most common mistakes.
"""
import json, sys
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib.units import inch
from reportlab.lib import colors

SCRIPT_DIR = Path(__file__).parent
NAVY = colors.HexColor("#0a2540")
GOLD = colors.HexColor("#8b6914")
PAPER_ACCENT = colors.HexColor("#f5f2e8")
GREEN_SOFT = colors.HexColor("#e7f0e5")
RED_SOFT = colors.HexColor("#fbe9e7")
GOLD_SOFT = colors.HexColor("#f4ead0")
RULE = colors.HexColor("#d8d3c3")

def load_enrichment(slug):
    f = SCRIPT_DIR / "enrichment" / f"{slug}.json"
    return json.load(f.open("r", encoding="utf-8")) if f.exists() else {
        "key_terms": [], "knowledge_enrichment": {}, "task_enrichment": {},
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

    base = getSampleStyleSheet()
    h1 = ParagraphStyle('H1', parent=base['Title'], textColor=NAVY, fontName='Helvetica-Bold',
                        fontSize=16, leading=19, spaceAfter=2, alignment=0)
    h2 = ParagraphStyle('H2', parent=base['Heading2'], textColor=GOLD, fontName='Helvetica-Bold',
                        fontSize=10, leading=12, spaceBefore=6, spaceAfter=2,
                        letterSpacing=1.2, textTransform='uppercase')
    task_h = ParagraphStyle('TaskH', parent=base['Normal'], textColor=NAVY, fontName='Helvetica-Bold',
                            fontSize=9.5, leading=11, spaceBefore=4, spaceAfter=1)
    body = ParagraphStyle('Body', parent=base['Normal'], fontName='Helvetica', fontSize=8.5,
                          leading=11, textColor=colors.HexColor("#1a2332"))
    mini = ParagraphStyle('Mini', parent=body, fontSize=8, leading=10)
    tag = ParagraphStyle('Tag', parent=base['Normal'], textColor=NAVY, fontName='Helvetica-Bold',
                         fontSize=7.5, leading=9)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(out_path), pagesize=letter,
                            topMargin=0.35*inch, bottomMargin=0.35*inch,
                            leftMargin=0.4*inch, rightMargin=0.4*inch,
                            title=f"Job Aid — {src['title']}")
    story = []

    story.append(Paragraph(f"{src['title']} — Quick Reference", h1))
    story.append(Paragraph("CAET Advanced · Job Aid · Aircraft Electronics Association",
                           ParagraphStyle('sub', parent=body, fontSize=8.5, textColor=colors.HexColor("#4a5568"),
                                          fontName='Helvetica-Oblique', spaceAfter=6)))

    # Key terms (two-column table for density)
    terms = enr.get("key_terms", [])[:6]
    if terms:
        story.append(Paragraph("KEY TERMS", h2))
        rows = []
        for term in terms:
            rows.append([
                Paragraph(f"<b>{term['term']}</b>", mini),
                Paragraph(term['definition'], mini),
            ])
        t = Table(rows, colWidths=[1.1*inch, 6.3*inch])
        t.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('BACKGROUND', (0,0), (0,-1), PAPER_ACCENT),
            ('LEFTPADDING', (0,0), (-1,-1), 5),
            ('RIGHTPADDING', (0,0), (-1,-1), 5),
            ('TOPPADDING', (0,0), (-1,-1), 3),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
            ('LINEBELOW', (0,0), (-1,-1), 0.25, RULE),
        ]))
        story.append(t)

    # Per-task: pair evaluator-watching with common-mistakes in side-by-side tables
    story.append(Paragraph("TASK CHECKLIST — WHAT EVALUATOR WATCHES / WHAT TO AVOID", h2))
    for task in src["tasks"]:
        k = match_key(task["heading"])
        e = enr.get("task_enrichment", {}).get(k, {})
        watch = e.get("evaluator_watching_for", [])[:3]
        mistakes = e.get("common_mistakes", [])[:3]
        if not (watch or mistakes):
            continue

        # Task heading bar
        story.append(Paragraph(task["heading"], task_h))

        # Two-column accept/avoid
        watch_cell = [Paragraph(f"✓ {w}", mini) for w in watch] or [Paragraph("<i>—</i>", mini)]
        avoid_cell = [Paragraph(f"✗ {m}", mini) for m in mistakes] or [Paragraph("<i>—</i>", mini)]
        rows = [[
            Paragraph("<b>EVALUATOR ACCEPTS</b>", ParagraphStyle('accepth', parent=tag, textColor=colors.HexColor("#1b4332"))),
            Paragraph("<b>COMMON MISTAKES</b>", ParagraphStyle('avoidh', parent=tag, textColor=colors.HexColor("#8b1a1a"))),
        ]]
        # Stack cells into multi-line content
        watch_stack = []
        for w in watch:
            watch_stack.append(Paragraph(f"✓ {w}", mini))
        if not watch_stack:
            watch_stack.append(Paragraph("<i>See full rubric.</i>", mini))
        mistakes_stack = []
        for m in mistakes:
            mistakes_stack.append(Paragraph(f"✗ {m}", mini))
        if not mistakes_stack:
            mistakes_stack.append(Paragraph("<i>See handbook.</i>", mini))

        rows.append([watch_stack, mistakes_stack])
        t = Table(rows, colWidths=[3.75*inch, 3.75*inch])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (0,0), GREEN_SOFT),
            ('BACKGROUND', (1,0), (1,0), RED_SOFT),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('RIGHTPADDING', (0,0), (-1,-1), 6),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('BOX', (0,0), (-1,-1), 0.25, RULE),
            ('INNERGRID', (0,0), (-1,-1), 0.25, RULE),
        ]))
        story.append(KeepTogether(t))
        story.append(Spacer(1, 0.04*inch))

    doc.build(story)
    print(f"Wrote {out_path}")

if __name__ == "__main__":
    main()
