"""Render the worksheet.pdf — pre-drill practice problems with enriched answer key."""
import json, sys
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether, Table, TableStyle
from reportlab.lib.units import inch
from reportlab.lib import colors

SCRIPT_DIR = Path(__file__).parent
NAVY = colors.HexColor("#0a2540")
GOLD = colors.HexColor("#8b6914")
PAPER_ACCENT = colors.HexColor("#f5f2e8")
RULE = colors.HexColor("#d8d3c3")

def load_enrichment(slug):
    f = SCRIPT_DIR / "enrichment" / f"{slug}.json"
    return json.load(f.open("r", encoding="utf-8")) if f.exists() else {
        "key_terms": [], "knowledge_enrichment": {}, "task_enrichment": {},
        "oral_board_answers": {}, "background_theory": {},
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
                        fontSize=18, leading=22, alignment=0, spaceAfter=4)
    h2 = ParagraphStyle('H2', parent=base['Heading2'], textColor=GOLD, fontName='Helvetica-Bold',
                        fontSize=11, leading=14, spaceBefore=14, spaceAfter=4,
                        textTransform='uppercase', letterSpacing=1.2)
    q_label = ParagraphStyle('QL', parent=base['Normal'], textColor=NAVY, fontName='Helvetica-Bold',
                             fontSize=11, leading=14, spaceBefore=12, spaceAfter=3)
    body = ParagraphStyle('Body', parent=base['Normal'], fontName='Helvetica', fontSize=10,
                          leading=14, spaceAfter=4, textColor=colors.HexColor("#1a2332"))
    italic = ParagraphStyle('Italic', parent=body, fontName='Helvetica-Oblique')
    space = ParagraphStyle('Sp', parent=body, fontName='Helvetica', leading=26,
                           textColor=colors.HexColor("#a0a0a0"), fontSize=10)
    answer = ParagraphStyle('Ans', parent=body, fontSize=9.5, leading=13,
                            textColor=colors.HexColor("#4a5568"),
                            leftIndent=12, spaceAfter=6)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(out_path), pagesize=letter,
                            topMargin=0.7*inch, bottomMargin=0.7*inch,
                            leftMargin=0.85*inch, rightMargin=0.85*inch,
                            title=f"Worksheet — {src['title']}")
    story = []

    story.append(Paragraph(f"Worksheet: {src['title']}", h1))
    story.append(Paragraph("Complete these problems BEFORE the practice drill. Answer in the space provided, then self-grade against the key on page 2.", italic))
    story.append(Paragraph("Target: zero wrong answers. If you miss one, re-read the handbook section and try again.", italic))
    story.append(Spacer(1, 0.1*inch))

    # Section 1: Oral board (scenario) problems
    story.append(Paragraph("SECTION 1 · Oral Board Scenarios", h2))
    story.append(Paragraph("Answer each in 2–3 sentences. Imagine you are speaking to an evaluator.", italic))
    problems_idx = 1
    for q in src["oral_board_questions"]:
        story.append(Paragraph(f"Problem {problems_idx}", q_label))
        story.append(Paragraph(q, body))
        for _ in range(3):
            story.append(Paragraph("_________________________________________________________________________________", space))
        problems_idx += 1

    # Section 2: Procedure recall from task enrichment
    tasks_with_steps = [t for t in src["tasks"] if enr.get("task_enrichment", {}).get(match_key(t["heading"]), {}).get("step_by_step")]
    if tasks_with_steps:
        story.append(PageBreak())
        story.append(Paragraph("SECTION 2 · Procedure Recall", h2))
        story.append(Paragraph("List the steps for each procedure in the correct order. Do not look at the handbook.", italic))
        for task in tasks_with_steps[:3]:  # Top 3 to keep worksheet from being too long
            k = match_key(task["heading"])
            e = enr["task_enrichment"][k]
            story.append(Paragraph(f"Problem {problems_idx} — {task['heading']}", q_label))
            story.append(Paragraph(
                f"List the {len(e['step_by_step'])} steps in order. Don't worry about exact wording — capture the key action.",
                body
            ))
            for _ in range(6):
                story.append(Paragraph("_________________________________________________________________________________", space))
            problems_idx += 1

    # Section 3: Common-mistake identification
    story.append(Paragraph("SECTION 3 · What Went Wrong?", h2))
    story.append(Paragraph("For each scenario, name the specific mistake and explain the correct approach.", italic))
    scenario_probs = []
    # Build from common_mistakes across tasks
    for task in src["tasks"]:
        k = match_key(task["heading"])
        e = enr.get("task_enrichment", {}).get(k, {})
        for m in e.get("common_mistakes", [])[:1]:  # First mistake per task
            scenario_probs.append((task["heading"], m))
    for heading, mistake in scenario_probs[:4]:
        story.append(Paragraph(f"Problem {problems_idx}", q_label))
        story.append(Paragraph(
            f"<b>During {heading}:</b> A trainee does the following — <i>{mistake.split('.')[0]}</i>. "
            f"What is the specific error? What should they have done instead? Why does this matter in service?",
            body
        ))
        for _ in range(3):
            story.append(Paragraph("_________________________________________________________________________________", space))
        problems_idx += 1

    # ========== ANSWER KEY ==========
    story.append(PageBreak())
    story.append(Paragraph("Answer Key", h1))
    story.append(Paragraph("Self-grade honestly. The goal is learning, not scoring.", italic))
    story.append(Spacer(1, 0.12*inch))

    # Oral board answers from enrichment
    story.append(Paragraph("SECTION 1 · Oral Board", h2))
    idx = 1
    for q in src["oral_board_questions"]:
        qnum = q.split(":")[0].strip()
        ans = enr.get("oral_board_answers", {}).get(qnum)
        story.append(Paragraph(f"Problem {idx}: {qnum}", q_label))
        if ans:
            story.append(Paragraph(ans, answer))
        else:
            story.append(Paragraph("See handbook section matching this topic.", answer))
        idx += 1

    # Procedure answers
    if tasks_with_steps:
        story.append(Paragraph("SECTION 2 · Procedures", h2))
        for task in tasks_with_steps[:3]:
            k = match_key(task["heading"])
            e = enr["task_enrichment"][k]
            story.append(Paragraph(f"Problem {idx}: {task['heading']}", q_label))
            for step_idx, s in enumerate(e["step_by_step"], 1):
                story.append(Paragraph(f"<b>{step_idx}.</b> {s}", answer))
            idx += 1

    # Scenario answers
    story.append(Paragraph("SECTION 3 · What Went Wrong", h2))
    for heading, mistake in scenario_probs[:4]:
        story.append(Paragraph(f"Problem {idx}: {heading}", q_label))
        story.append(Paragraph(mistake, answer))
        idx += 1

    doc.build(story)
    print(f"Wrote {out_path}")

if __name__ == "__main__":
    main()
