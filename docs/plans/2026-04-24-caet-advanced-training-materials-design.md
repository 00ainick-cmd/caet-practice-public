# CAET Advanced Training Materials — Design Document

**Date:** 2026-04-24
**Scope:** Produce a complete training materials package for all 15 CAET Advanced certification modules, co-located with the existing practice bank in the `caet-practice-public` repo.
**Strategy:** Pilot one module end-to-end, validate with sign-off, then scale the template to the remaining 14 modules via parallel agents.

## Motivation

The `/advanced/` practice bank (launched 2026-04-23) gives CAET Advanced candidates 193 drill items, flashcards, and Battle ACE — but nothing to study from. Students can test their knowledge but not learn new content. The existing base CAET site has the same gap (the `training-config.json` has slots for `cat-N-lesson.html` files that don't exist). This project fills that gap for the Advanced certification first.

## Source Material Available

We already have 18 training documents authored by AEA's Workforce Development team, stored in OneDrive at `Desktop/CAET/CAET Advanced/CAET-Advanced-Training-Program Curricullum/CAET-Advanced-Training-Program/`:

- **PQS-Training-Modules** (01–13) — practical/hands-on focus: regulatory compliance, maintenance documentation, wiring diagrams, wire harness fabrication, audio panel, navigation, communication, transponder/ADS-B, pitot-static, autopilot, compass, EFB connectivity, FMS
- **Exam-Study-Modules** (14–18) — knowledge focus: CMS, datalink, AHRS, smart probes, software/database loading

Each docx contains Knowledge Requirements, Task Preparation Guide sections (PQS modules), and Oral Board practice questions. These serve as authoritative source material — not skeletons.

Supporting source files available:
- `CAET_Advanced_PQS_Standards_v5.pdf` — authoritative practical evaluation standards (source for practical rubrics)
- `CAET_Advanced_Program_Framework.pdf` — program structure
- `00-Candidate-Preparation-Guide.docx` — candidate-facing intro material

## Architecture

### File Layout

Training artifacts live as a subfolder inside each existing module directory, parallel to the practice data:

```
caet-practice-public/
└── advanced/
    └── training/
        └── adv10-wire-harness-fabrication/       # 1 of 15 Advanced modules
            ├── index.html                         # existing module hub
            ├── drill.html, flashcards.html, ...   # existing practice modes
            ├── data/                              # existing practice bank
            │   ├── questions.json
            │   └── jeopardy.json
            └── training/                          # NEW subdirectory
                ├── handbook.pdf                   # student study guide
                ├── handbook.html                  # same content, web-readable
                ├── lesson.html                    # interactive 5E online lesson
                ├── lesson-plan.pdf                # instructor guide
                ├── job-aid.pdf                    # 1-page printable reference
                ├── worksheet.pdf                  # pre-drill practice problems
                └── practical-rubric.pdf           # evaluator scoring sheet
```

Module hub (`index.html`) gets a new "Study First" card row above the existing "Practice" cards, linking to the 6 artifacts.

### Module-to-Source Mapping

The 15 practice-bank modules map to source documents as follows:

| Practice slug | Module | Primary source docx |
|---|---|---|
| adv1 | Cabin Management Systems | Exam-Study 14 |
| adv2 | Connectivity | PQS 12 (EFB Connectivity) |
| adv3 | Datalink Fundamentals | Exam-Study 15 |
| adv4 | Flight Management Systems | PQS 13 |
| adv5 | Attitude & Heading Reference | Exam-Study 16 + PQS 11 (Compass) |
| adv6 | Audio Panels | PQS 05 |
| adv7 | NAV/COM Systems | PQS 06 + PQS 07 |
| adv8 | 14 CFR 65.91 Regulations | PQS 01 (Regulatory) |
| adv9 | Smart Probes & Air Data | Exam-Study 17 + PQS 09 (Pitot-Static) |
| adv10 | Wire Harness Fabrication | PQS 04 ← **PILOT MODULE** |
| adv11 | Autopilot Systems | PQS 10 |
| adv12 | Transponders & ADS-B | PQS 08 |
| adv13 | Documentation | PQS 02 + PQS 03 (Wiring Diagrams) |
| adv14 | Software & Database Loading | Exam-Study 18 |
| adv15 | Emergency Autoland | (no direct source — derive from PQS Standards v5) |

Three orphaned PQS source docs (03 Wiring Diagrams, 09 Pitot-Static, 11 Compass) fold into related modules above.

adv15 (EAL) has no direct source — we'll derive content from the PQS Standards v5 document and publicly available EAL technical references.

## Artifact Specification

Each of the 15 modules gets 6 artifacts. Definition below uses adv10 (Wire Harness Fabrication) as the reference example.

### 1. `handbook.pdf` + `handbook.html` — Student study guide

Target: ~18 pages (scales 10-25 by topic complexity).

Structure:
1. Why This Matters (expanded from source intro)
2. Topic sub-sections (1-2 per Knowledge Requirement in source)
3. Procedures (one sub-section per Task in source)
4. Self-Check Quick Quiz (10 questions with answers)
5. Glossary + regulatory references

Running features:
- "Evaluator is watching for..." callout boxes (from source Task Prep)
- Memory hook mnemonics per key concept
- "Common mistakes" warning boxes
- Chapter-end summary + 3-5 self-check questions
- Diagram placeholders (images commissioned separately)

Format: PDF (print) + HTML (web-readable, same content). HTML uses the existing `ace-theme.css` so it matches the practice site aesthetic.

### 2. `lesson.html` — Interactive online lesson (5E model)

Single-file HTML, 20-30 minutes of self-paced student work, embedded in the `/advanced/` site. Sections:

- **Engage** (2 min) — attention-grabbing opener (e.g., "Spot the defective crimp" with 4 photos)
- **Explore** (5 min) — interactive widget (decision tree, interactive diagram)
- **Explain** (10 min) — expandable concept cards with deep content
- **Elaborate** (8 min) — virtual lab walkthrough with checkpoint questions
- **Evaluate** (5 min) — 10-question quiz sourcing from the drill bank (`../data/questions.json`)

Technical: single HTML file. Same visual system as `drill.html`. No new dependencies. Data for the quiz loads from the existing practice bank — zero duplication of question content.

### 3. `lesson-plan.pdf` — Instructor guide

3-hour classroom block (90 min lecture/demo + 90 min hands-on lab). Includes:

- Prerequisites (student read handbook chapters X-Y)
- Equipment list per student
- Minute-by-minute agenda
- Direct instruction notes (what to say at each point)
- Demo scripts for instructor
- Assessment procedure (peer checks + instructor spot checks)
- Common student errors (observed during demos)
- Remediation plan for struggling students

Format: PDF, instructor-facing.

### 4. `job-aid.pdf` — 1-page printable quick reference

Single 8.5×11 page, designed to be printed and taped to a shop wall or kept in a tool kit. For adv10, sections would be:

- Terminal color code table
- Shield termination decision flowchart
- Megger safety mandatory sequence
- Crimp inspection checklist
- AC 43.13-1B / AEA CAET reference footer

Layout optimized for at-a-glance scanning. High visual density.

### 5. `worksheet.pdf` — Pre-drill practice problems

10 problems, ~6 pages with answer key. Mixed problem types:
- Terminal/component selection problems
- Troubleshooting scenarios (2-3 plausible causes + how to distinguish)
- Fill-in-the-blank procedure sequences
- Diagram-based identification (with blanks)

Each answer key entry references the handbook page for remediation.

### 6. `practical-rubric.pdf` — Evaluator scoring sheet

Evaluator-facing. For each PQS task in the module, provides an Accept/Reject checklist:

```
TASK 4.4.1 — HARNESS FABRICATION
  ACCEPT                          REJECT
  □ Correct wire type             □ Wrong insulation
  □ Clean strip, no nicks         □ Nicked conductors
  □ Shield terminated correctly   □ Shield grounded wrong end
  ...
```

Scoring rules:
- 6/6 tasks passed = Pass
- 5/6 with remediation plan = Conditional Pass (30-day retest)
- <5 = Fail (module retake required)

Each module's rubric pulls authoritative criteria from `CAET_Advanced_PQS_Standards_v5.pdf`.

## Module Hub Integration

Each `/advanced/training/advN-*/index.html` already renders a grid of activity cards (Drill, Flashcards, Final Test). Add a new "Study First" section above those cards with 6 tiles:

| Tile | Links to | Icon suggestion |
|---|---|---|
| Handbook | `training/handbook.html` | 📖 |
| Interactive Lesson | `training/lesson.html` | 💡 |
| Lesson Plan (Instructor) | `training/lesson-plan.pdf` | 👨‍🏫 |
| Job Aid | `training/job-aid.pdf` | 📋 |
| Worksheet | `training/worksheet.pdf` | ✏️ |
| Practical Rubric | `training/practical-rubric.pdf` | ✅ |

Cards that open PDFs use `target="_blank"`. Handbook and lesson open in-page.

## Production Approach

### Phase 1 — Pilot (adv10 Wire Harness Fabrication)

Single module, all 6 artifacts. Sequential production with user validation at the end.

Skill assignments per artifact:

| Artifact | Primary skill | Notes |
|---|---|---|
| handbook | `unified-training-generator` or `enhanced-installation-manual-builder` | Feed source docx + Program Framework |
| lesson.html | `caet-training-module-builder` | Merrill/5E single-file HTML output |
| lesson-plan | `lesson-plan-generator` | 5E format from source task-prep |
| job-aid | `canvas-design` skill + manual layout | Distill source docx key facts |
| worksheet | `5e-active-learning-asset-generator` | Produces ready-to-use practice problems |
| practical-rubric | `caet-rubric-builder` | Pulls from PQS Standards v5 |

User reviews the complete pilot. Approval required before Phase 2.

### Phase 2 — Replicate to 14 remaining modules

Dispatch parallel agents (one per module) — each produces all 6 artifacts for its module using the approved pilot as template. Estimate: 14 parallel agents × ~20 min per agent = one batch run.

Central QA after aggregation:
- All 6 artifacts present per module
- Source content faithfully represented (check against docx for each module)
- Styling consistent with pilot
- All links in module hub work
- PDFs render cleanly

### Phase 3 — Module hub integration + deploy

Update all 15 `/advanced/training/advN-*/index.html` files with the new "Study First" card row. Link to the 6 artifacts per module.

Deploy, verify live:
- `https://00ainick-cmd.github.io/caet-practice-public/advanced/training/adv10-wire-harness-fabrication/training/handbook.html` should load
- Each module's index.html should show all 6 Study First cards
- PDFs downloadable

## Data Flow

```
source docx (OneDrive)
       │
       ▼
[caet-training-module-builder / lesson-plan-generator / etc.]
       │
       ▼
artifact files (PDF + HTML) → /advanced/training/advN-*/training/
       │
       ▼
module hub index.html → new "Study First" card row
       │
       ▼
deployed site → students click → study → practice
```

## Testing & Validation

No automated tests for content (it's study material). Validation approach:

1. **Pilot review** — user opens every artifact, confirms content fidelity to source, confirms visual quality
2. **Per-module spot-check** in Phase 2 — random sampling of 3-4 modules after bulk generation
3. **Link integrity** — automated check that every module hub links to all 6 artifact files and they load (HTTP 200)
4. **PDF render check** — automated (pdftotext > 0 words)
5. **Cross-module consistency** — visual diff sampling to confirm pilot template followed

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Parallel agents produce inconsistent quality | Pilot template approved first; agents told to match it exactly |
| Source docx has gaps for some modules (esp. adv15 EAL) | Flag gap modules in Phase 1; user provides supplementary source or approves AI-derived content |
| PDF generation complexity (need reliable HTML→PDF pipeline) | Use headless Chrome or weasyprint (well-established tools); lock down once working on pilot |
| Content scope creep (handbook grows to 50 pages per module) | Target page counts defined above; ruthless YAGNI |
| PQS Standards v5 changes during production | Source is considered frozen for this work; any post-v5 updates handled in a revision pass |

## Scope Exclusions (YAGNI cuts)

Not building in this project:
- React app per module (the existing practice site provides interactivity)
- Remediation materials per module (practice tests already serve this purpose)
- Lab sheets separate from worksheets (combined into worksheet.pdf)
- Video content (out of scope — could be added later if needed)
- Instructor training certification program (separate initiative)
- Localization to other languages
- Updates to base CAET site (Advanced-only for now)

## Success Criteria

Phase 1 (Pilot):
- All 6 artifacts produced for adv10 Wire Harness Fabrication
- User approval given
- Pilot's module hub shows working Study First section with all 6 links

Phase 2 (Bulk):
- All 14 remaining modules have all 6 artifacts
- Content faithful to source docx (for modules with source)
- Styling consistent with pilot
- 0 broken links

Phase 3 (Deploy):
- Live at `/advanced/training/advN-*/training/` for all 15 modules
- Module hubs show Study First section
- User validates at least 5 modules end-to-end student-journey

## Open Questions (to resolve during writing-plans stage)

- adv15 (Emergency Autoland) — what source material beyond PQS Standards v5 is available? User may need to provide supplementary docs.
- PDF generation toolchain — use headless Chrome (better styling) or WeasyPrint (pure Python, simpler)?
- Handbook HTML vs PDF — do we generate HTML first then convert to PDF, or produce them independently from the same source?
- Job aid layout — use `canvas-design` skill output, custom print-CSS HTML → PDF, or direct PDF authoring?

These get resolved in the detailed implementation plan (next step via `writing-plans` skill).
