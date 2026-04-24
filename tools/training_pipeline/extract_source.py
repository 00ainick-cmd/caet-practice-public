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
