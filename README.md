# CAET Practice (Public)

Open-access CAET exam practice for Aircraft Electronics Association candidates. Students come here from their Thinkific course Rise modules to drill test questions before sitting the real CAET exam.

## What this is

A **static, login-free** fork of the internal CAET Prep Course app. Students land on a hub with three practice modes:

- **Battle ACE** — Jeopardy-style trivia across all 8 modules
- **Flash Cards** — rapid recall with a Pomodoro timer
- **Drill Mode** — multiple-choice exam practice with instant feedback (closest to the real CAET format)

All three draw from the same question bank. Progress (right/wrong per question, session scores) is stored only in the student's browser via `localStorage` — nothing is sent to a server.

## What this is NOT

- Not a replacement for the full Thinkific-hosted Rise modules — students are expected to have already worked through those.
- Not a grading or certification platform — there is no account, no transcript, no proctor.

## Deployment

Pure static. Deployed to GitHub Pages from the `main` branch root.

## Question bank

The 8 module categories and their question files:

| # | Module | Drill bank (questions) | Jeopardy bank |
|---|---|---|---|
| 1 | Maintenance Regulations | `training/caet/mod1-maintenance-regs/data/questions.json` | `jeopardy.json` |
| 2 | Basic Electrical | `training/caet/mod2-basic-electrical/data/...` | " |
| 3 | CNS Systems | `training/caet/mod3-cns-systems/data/...` | " |
| 4 | Flight Instruments | `training/caet/mod4-flight-instruments/data/...` | " |
| 5 | Digital Databus | `training/caet/mod5-digital-databus/data/...` | " |
| 6 | Aircraft Wiring | `training/caet/mod6-aircraft-wiring/data/...` | " |
| 7 | Tools & Test Equipment | `training/caet/mod7-tools-test-equipment/data/...` | " |
| 8 | Shop Safety | `training/caet/mod8-shop-safety/data/...` | " |

The Drill mode also reads the consolidated `master-bank.json` at the repo root.

## Relationship to the private repo

This is stripped down from the internal app at `00ainick-cmd/aea-caet` / `00ainick-cmd/caet-prep-app`:

- Removed: Node/Express server, SQLite DB, admin/employer dashboards, enrollment/checkout, journey nodes, classroom, onboarding, exam-results, final exam, Rise modules, all server-side auth.
- Stubbed: `shared/js/ace-auth.js`, `shared/js/supabase-client.js`, `shared/js/progress-tracker.js`, `shared/js/lo-mastery-tracker.js` — all converted to safe localStorage-only no-ops so the activity pages work without a backend.
- Kept: `index.html` (hub), `shared/drill.html`, `shared/flashcards.html`, `shared/jeopardy.html`, theme CSS, sprites, and the 8 module question banks.

## Local preview

Any static HTTP server works — you cannot open this via `file://` because the pages fetch JSON at runtime:

```
python -m http.server 8765
# then open http://localhost:8765/
```
