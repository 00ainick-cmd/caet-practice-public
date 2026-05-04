# Training material generation pipeline

Generates 6 training artifacts (handbook.html, handbook.pdf, lesson.html, lesson-plan.pdf, job-aid.pdf, worksheet.pdf, practical-rubric.pdf) per CAET Advanced module from source docx.

## Pipeline stages

1. **Source extraction** (`extract_source.py`) — parse docx → structured JSON in staging dir (outside repo).
2. **Generators** (`gen_*.py`) — render JSON → individual artifacts via Jinja2 (HTML) or reportlab (print PDFs).
3. **HTML→PDF** — uses Microsoft Edge headless on Windows (replaces weasyprint, which requires GTK3 runtime not available on stock Windows).

## Source location

Source docx files staged in `C:/Users/nickb/Downloads/CAET_Blueprint_PRIVATE/training_source/` (read-only working copy from OneDrive).

## Output location

`advanced/training/advN-<slug>/training/` — committed to repo.
