"""Shared helpers for merging source docx content with enrichment JSON.

Some modules (Exam Study Modules) have no tasks or oral-board in source;
for those the enrichment must provide synthesized_tasks and synthesized_oral_board,
which are structurally compatible with the source fields.
"""

def effective_tasks(src, enrichment):
    """Return tasks list, preferring source, falling back to enrichment.synthesized_tasks."""
    if src.get("tasks"):
        return src["tasks"]
    return enrichment.get("synthesized_tasks", [])

def effective_oral(src, enrichment):
    """Return oral-board questions list, preferring source, falling back to synthesized."""
    if src.get("oral_board_questions"):
        return src["oral_board_questions"]
    return enrichment.get("synthesized_oral_board", [])

def effective_intro(src, enrichment):
    """Return intro paragraphs — source first, enrichment.why_this_matters[0:1] as fallback."""
    if src.get("intro"):
        return src["intro"]
    why = enrichment.get("why_this_matters", [])
    return why[:1] if why else []
