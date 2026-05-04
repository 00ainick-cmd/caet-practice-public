# AI Tutor Pedagogy Library (Library A) Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a 50-chapter, evidence-based, domain-agnostic pedagogy reference library that any AI tutor can consult to decide *how to teach* a given concept across any subject (avionics, basketball, mortgages, etc.).

**Architecture:** Filesystem of YAML-frontmattered markdown chapters at `pedagogy-library/<category>/<principle>.md`. Each chapter is full-chapter depth (~12 pages, ≥5 peer-reviewed citations). Library is consumed at runtime by the (separate) tutor engine via frontmatter queries. Authored via a 5-phase process: gold-standard exemplar → schema spec → parallel agent dispatch → multi-pass verification.

**Tech Stack:** Markdown + YAML frontmatter, Python (validator + dispatch script), parallel sub-agent dispatch via the Agent tool with web-search access for citation verification.

**Design doc:** `docs/plans/2026-04-29-ai-tutor-pedagogy-library-design.md`

**STOP points (user review checkpoints):** Tasks 4, 13, 19. Do NOT proceed past these without explicit user approval.

---

## Phase 2 — Exemplar Authoring (Tasks 0–4)

The exemplar (`testing-effect.md`) sets the quality bar concretely. Every parallel agent in Phase 4 will see this file as their model.

### Task 0: Set up library directory structure

**Files:**
- Create: `pedagogy-library/README.md`
- Create: `pedagogy-library/01-learning-science/.gitkeep`
- Create: `pedagogy-library/02-instructional-design/.gitkeep`
- Create: `pedagogy-library/03-assessment-science/.gitkeep`
- Create: `pedagogy-library/04-delivery-patterns/.gitkeep`
- Create: `pedagogy-library/05-tutor-personas/.gitkeep`
- Create: `pedagogy-library/06-motivation-engagement/.gitkeep`
- Create: `pedagogy-library/07-runtime-decisions/.gitkeep`
- Create: `pedagogy-library/_schema/.gitkeep`

**Step 1: Create directory structure**

```bash
cd "C:/Users/nickb/Downloads/caet-practice-public/.claude/worktrees/laughing-shockley-17815f"
mkdir -p pedagogy-library/01-learning-science pedagogy-library/02-instructional-design \
         pedagogy-library/03-assessment-science pedagogy-library/04-delivery-patterns \
         pedagogy-library/05-tutor-personas pedagogy-library/06-motivation-engagement \
         pedagogy-library/07-runtime-decisions pedagogy-library/_schema
for d in pedagogy-library/01-* pedagogy-library/02-* pedagogy-library/03-* \
         pedagogy-library/04-* pedagogy-library/05-* pedagogy-library/06-* \
         pedagogy-library/07-* pedagogy-library/_schema; do
  touch "$d/.gitkeep"
done
```

**Step 2: Author README.md**

Create `pedagogy-library/README.md` with:
- One-paragraph mission statement (what this library is for)
- Schema overview (link to `_schema/chapter-schema.yaml` once it exists)
- The 50-principle index (copy from design doc section 4)
- "What's deliberately excluded" (copy from design doc section 4 final table)
- Authoring discipline note (citation rules, review process)

**Step 3: Commit**

```bash
git add pedagogy-library/
git commit -m "feat: scaffold pedagogy library directory structure"
```

---

### Task 1: Research citations for testing-effect.md

**Files:**
- Create: `pedagogy-library/01-learning-science/_research-notes-testing-effect.md` (working notes, not committed)

**Step 1: Web-search the foundational papers**

I'll use WebSearch to verify each of these citations actually exists and pull the current state of evidence:

- Roediger, H. L., & Karpicke, J. D. (2006). The power of testing memory: Basic research and implications for educational practice. *Perspectives on Psychological Science*, 1(3), 181–210.
- Adesope, O. O., Trevisan, D. A., & Sundararajan, N. (2017). Rethinking the use of tests: A meta-analysis of practice testing. *Review of Educational Research*, 87(3), 659–701.
- Karpicke, J. D., & Blunt, J. R. (2011). Retrieval practice produces more learning than elaborative studying with concept mapping. *Science*, 331(6018), 772–775.
- Roediger, H. L., & Butler, A. C. (2011). The critical role of retrieval practice in long-term retention. *Trends in Cognitive Sciences*, 15(1), 20–27.
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest*, 14(1), 4–58.

**Step 2: Capture verified citations + DOIs into research notes**

Write the working notes file with the verified citation list, abstracts, and effect sizes from each.

**Step 3: Identify boundary-condition / contested-claim papers**

Search for replication studies and meta-analyses identifying *when* the testing effect doesn't work (Karpicke & Aue 2015 on overlearning; recent contested-fluency literature).

**Step 4: No commit yet** — these are throwaway research notes.

---

### Task 2: Author the exemplar chapter

**Files:**
- Create: `pedagogy-library/01-learning-science/testing-effect.md`

**Step 1: Author the YAML frontmatter**

Per the design doc schema, populate every required field:
- id, title, category, aliases, evidence_strength: `strong`, effect_size with a defensible range, key_sources (≥5), last_reviewed, applies_to, contraindicated_when, runtime_triggers, related.

**Step 2: Author all 9 body sections**

In order:
1. **One-line claim** (1 sentence)
2. **Evidence base** (3–5 paragraphs; cite Roediger 2006, Adesope 2017 meta-analysis with d ≈ 0.5–0.8, Karpicke & Blunt 2011, replication notes)
3. **When to apply** (concrete decision rules tied to runtime_triggers)
4. **When NOT to apply** (initial encoding, overload, pure motor skills)
5. **How to apply** (link to delivery-pattern files: predict-before-reveal, faded worked examples for the studied-then-tested pattern, etc.)
6. **Common misapplications** (recognition vs recall, ceiling-effect items)
7. **Examples across domains** (3 concrete examples — avionics megger procedure recall, basketball play-recognition recall, mortgage APR computation recall)
8. **Quality signal** (compare retention on retrieval-applied items vs control at +24h; effect should appear with d > 0.3)
9. **Cross-references** (links to spaced-retrieval, desirable-difficulties, generation-effect, predict-before-reveal)

**Step 3: Verify file length**

Run:
```bash
wc -l pedagogy-library/01-learning-science/testing-effect.md
```
Expected: 120–200 lines (corresponds to ~3–5 pages of practice-guideline-dense content).

**Step 4: Commit**

```bash
git add pedagogy-library/01-learning-science/testing-effect.md
git commit -m "feat: author exemplar chapter (testing-effect.md)"
```

---

### Task 3: Self-review pass on exemplar

**Files:**
- Modify: `pedagogy-library/01-learning-science/testing-effect.md` (if revisions needed)

**Step 1: Read the exemplar end-to-end**

Open and read the entire file. Check against quality criteria from design doc section 6:
- ≥ 5 peer-reviewed citations with full reference
- No fabricated citations
- Effect size quantified
- Operational sections give executable decision rules
- Cross-domain examples present
- Boundary conditions stated
- Frontmatter complete

**Step 2: Cross-check every citation**

For each cited paper, run a WebSearch with `<authors> <year> <title>` to confirm it exists and the cited claim matches the abstract. Flag any citation where the search returns no result or where the cited claim doesn't match the paper's actual content.

**Step 3: Apply revisions if needed**

If any citation fails verification or any section is weak, edit the file. Re-commit:

```bash
git add pedagogy-library/01-learning-science/testing-effect.md
git commit -m "fix: tighten exemplar after self-review"
```

---

### Task 4: STOP — User review of exemplar

**Step 1: Open the exemplar in user's preview**

Tell user: "Exemplar ready at `pedagogy-library/01-learning-science/testing-effect.md`. This is the quality bar. Every other chapter in the library will match this depth, structure, and citation rigor. Please read it end-to-end and tell me:
- Is the depth right? Too academic? Too operational?
- Are there sections that feel weak or unnecessary?
- Are the cross-domain examples (avionics + basketball + mortgage) doing what we need?
- Any citation that needs to be added or removed?"

**Step 2: STOP — await explicit user approval**

Do NOT proceed to Task 5 until user says "approved" or equivalent. Iterate on the exemplar (return to Task 2/3) until they sign off.

---

## Phase 3 — Schema & Spec (Tasks 5–10)

Once the exemplar is approved, distill it into machine-readable specs that govern all 49 remaining chapters.

### Task 5: Author the JSON-Schema for chapter frontmatter

**Files:**
- Create: `pedagogy-library/_schema/chapter-schema.yaml`

**Step 1: Write the schema**

Author a JSON Schema (in YAML) covering every required and optional frontmatter field. Define enums for `category`, `evidence_strength`, `applies_to`, `runtime_triggers`. Include format constraints (effect_size must match a regex pattern; key_sources must have ≥5 items).

**Step 2: Commit**

```bash
git add pedagogy-library/_schema/chapter-schema.yaml
git commit -m "feat: define JSON schema for chapter frontmatter"
```

---

### Task 6: Build the Python validator

**Files:**
- Create: `pedagogy-library/_schema/validate.py`
- Create: `pedagogy-library/_schema/test_validate.py`

**Step 1: Write the failing test**

Test that `validate.py` correctly identifies a fixture chapter with missing required frontmatter as invalid:

```python
def test_validator_rejects_missing_frontmatter():
    result = validate_chapter("fixtures/missing-fields.md")
    assert not result.ok
    assert "id" in result.errors[0]
```

**Step 2: Run test to verify it fails**

```bash
cd pedagogy-library/_schema
python -m pytest test_validate.py -v
```
Expected: FAIL (validate function not defined yet).

**Step 3: Implement minimal validator**

`validate.py` parses the YAML frontmatter via `python-frontmatter`, validates against `chapter-schema.yaml` via `jsonschema`, and additionally checks:
- 5–7 entries in `key_sources` (warn outside this range)
- Body has all 9 required sections (regex H2 headings)
- File length within 120–200 lines
- Cross-references in `related:` resolve to actual files
- Exactly 2 cross-domain examples in section 7 (avionics + one other)

**Step 4: Run tests to verify pass**

```bash
python -m pytest test_validate.py -v
```
Expected: PASS.

**Step 5: Commit**

```bash
git add pedagogy-library/_schema/validate.py pedagogy-library/_schema/test_validate.py
git commit -m "feat: add chapter validator with frontmatter and structure checks"
```

---

### Task 7: Run validator against exemplar

**Step 1: Validate the exemplar**

```bash
cd "C:/Users/nickb/Downloads/caet-practice-public/.claude/worktrees/laughing-shockley-17815f"
python pedagogy-library/_schema/validate.py pedagogy-library/01-learning-science/testing-effect.md
```
Expected: `OK: testing-effect.md passes all checks`.

**Step 2: If validation fails, fix EITHER the exemplar OR the validator**

The exemplar is the source of truth for "what good looks like." If the validator complains about a check the exemplar doesn't satisfy, the validator's check is wrong (or too strict). Adjust validator to align with exemplar. Re-run.

**Step 3: Commit any adjustments**

```bash
git add pedagogy-library/_schema/validate.py pedagogy-library/_schema/chapter-schema.yaml
git commit -m "fix: align validator with exemplar conventions"
```

---

### Task 8: Author quality-checklist.md

**Files:**
- Create: `pedagogy-library/_schema/quality-checklist.md`

**Step 1: Write the human-readable quality bar**

Restate the design doc's section 6 as a checklist:
- [ ] ≥5 peer-reviewed citations with full reference
- [ ] All citations verifiable via web search
- [ ] Effect size quantified (or explicitly noted as foundational/qualitative)
- [ ] All 9 body sections present
- [ ] Cross-domain examples in section 7
- [ ] Boundary conditions in section 4
- [ ] Frontmatter complete and validates against schema
- [ ] Cross-references resolve

This is what reviewers will check against by hand.

**Step 2: Commit**

```bash
git add pedagogy-library/_schema/quality-checklist.md
git commit -m "feat: add human quality checklist for chapter review"
```

---

### Task 9: Author citation-rules.md

**Files:**
- Create: `pedagogy-library/_schema/citation-rules.md`

**Step 1: Write the citation discipline rules**

Document for the parallel agents:
- Only peer-reviewed sources (or seminal book chapters from established academic publishers).
- Every citation must have authors, year, title, journal/publisher, DOI where available.
- Effect-size claims must cite a meta-analysis or specific empirical paper (not a textbook).
- If you can't find a real paper for a claim, **omit the claim** rather than fabricate.
- Use APA-style citations.
- "Replication" claims must cite the actual replication, not the original.

**Step 2: Commit**

```bash
git add pedagogy-library/_schema/citation-rules.md
git commit -m "docs: define citation discipline for chapter authors"
```

---

### Task 10: Author the authoring-brief template

**Files:**
- Create: `pedagogy-library/_schema/authoring-brief.md`

**Step 1: Write the brief**

This becomes the standard agent prompt template. Include placeholders for `{principle_id}`, `{title}`, `{category}`, `{anchor_citation}`. Tell the agent:
- Read `pedagogy-library/01-learning-science/testing-effect.md` as the model.
- Read `_schema/chapter-schema.yaml`, `quality-checklist.md`, `citation-rules.md`.
- Author `pedagogy-library/{category}/{principle_id}.md` matching the exemplar's structure, tone, and **size** (120–200 lines).
- This is a **practice guideline**, not a textbook chapter — every word earns its place. Bullets over paragraphs in operational sections.
- Verify every citation by web search; do not fabricate.
- Include exactly 2 cross-domain examples (avionics + one other domain of your choice).
- Run `_schema/validate.py` on your output before finishing.
- Return: file size, citation count, validation result, any caveats about contested claims.

**Step 2: Commit**

```bash
git add pedagogy-library/_schema/authoring-brief.md
git commit -m "feat: standardize authoring brief for parallel agents"
```

---

## Phase 4 — Parallel Authoring (Tasks 11–16)

### Task 11: Build the agent dispatch script

**Files:**
- Create: `pedagogy-library/_schema/dispatch.py`
- Create: `pedagogy-library/_schema/principles.json`

**Step 1: Write the principle index as JSON**

`principles.json` is a list of 49 entries (50 minus the exemplar already done). Each entry has `id`, `title`, `category`, `anchor_citation` (the seminal source — copy from the design doc index), and `notes` (any special instructions, e.g., "this principle is foundational, no specific d available").

**Step 2: Write the dispatch script**

`dispatch.py` reads `principles.json` and prints (does not execute) the agent-prompt for each principle, formed from the authoring-brief template. Two modes: `--principle <id>` (single) or `--all` (full list with separators). The script does NOT call the Agent tool itself — Claude in conversation does that, using this script's output to construct prompts.

**Step 3: Commit**

```bash
git add pedagogy-library/_schema/dispatch.py pedagogy-library/_schema/principles.json
git commit -m "feat: add dispatch helper for parallel chapter authoring"
```

---

### Task 12: Single-agent test dispatch

**Step 1: Generate prompt for one principle**

```bash
python pedagogy-library/_schema/dispatch.py --principle spaced-retrieval
```

Capture the output. Use it as the prompt for one Agent tool call (subagent_type: `general-purpose`). The agent has Read, Write, Glob, Grep, Bash, WebSearch tools.

**Step 2: Wait for agent completion, then validate output**

When the agent reports complete:

```bash
python pedagogy-library/_schema/validate.py pedagogy-library/01-learning-science/spaced-retrieval.md
```
Expected: PASS.

**Step 3: Read the output**

Manually read `spaced-retrieval.md`. Compare to exemplar:
- Depth comparable?
- Citations real? (verify 2-3 random ones via web search)
- Cross-domain examples present?
- Frontmatter populated correctly?

**Step 4: Commit if acceptable**

```bash
git add pedagogy-library/01-learning-science/spaced-retrieval.md
git commit -m "feat: author spaced-retrieval chapter (parallel-test)"
```

If the output is poor quality, return to Task 10 — refine the authoring brief and retry.

---

### Task 13: STOP — User review of agent output

**Step 1: Surface to user**

Tell user: "First parallel-author agent produced `pedagogy-library/01-learning-science/spaced-retrieval.md`. Please review and tell me:
- Is the quality comparable to the exemplar?
- Are there systematic differences (depth, tone, citation rigor) that suggest the brief needs revision?
- Citations look real or any suspicious ones?"

**Step 2: STOP — await explicit user approval**

If user identifies a systematic issue, return to Task 10 (revise brief) and re-run Task 12 with another principle. Do NOT dispatch the remaining 48 until user signs off on the agent quality.

---

### Task 14: Refine authoring brief if needed

**Files:**
- Modify: `pedagogy-library/_schema/authoring-brief.md`

If user feedback in Task 13 identifies issues, edit the brief to:
- Add explicit instructions for whatever was missing (more depth in evidence base, more variety in examples, etc.)
- Add explicit anti-patterns ("do not use textbooks for effect-size claims")
- Tighten any constraint that the test agent violated.

Commit changes:

```bash
git add pedagogy-library/_schema/authoring-brief.md
git commit -m "fix: tighten authoring brief based on first-agent review"
```

---

### Task 15: Dispatch all remaining 48 principles in parallel

**Step 1: Generate prompts for all remaining principles**

```bash
python pedagogy-library/_schema/dispatch.py --all > /tmp/all-prompts.txt
```

The output file contains 48 separated prompts (one per principle, excluding `testing-effect` and `spaced-retrieval` which are already authored).

**Step 2: Dispatch all 48 agents concurrently**

In a single Claude Code message, issue 48 Agent tool calls (subagent_type `general-purpose`, with `run_in_background: true` if available). Each agent gets its own principle's prompt.

**Step 3: Wait for completion notifications**

Each agent runs ~5–10 minutes. Background completions arrive as notifications.

**Step 4: Run validator on every output**

```bash
for f in pedagogy-library/*/*.md; do
  python pedagogy-library/_schema/validate.py "$f" || echo "FAIL: $f"
done
```

Any file that fails: re-dispatch a fix-agent for that specific principle with the validation error in the prompt.

**Step 5: Commit all 48 chapters**

```bash
git add pedagogy-library/
git commit -m "feat: author 48 pedagogy chapters via parallel agent dispatch"
```

---

### Task 16: Sanity-check coverage

**Step 1: Verify all 50 chapters exist**

```bash
ls pedagogy-library/01-*/*.md pedagogy-library/02-*/*.md pedagogy-library/03-*/*.md \
   pedagogy-library/04-*/*.md pedagogy-library/05-*/*.md pedagogy-library/06-*/*.md \
   pedagogy-library/07-*/*.md | wc -l
```
Expected: 50.

**Step 2: Verify counts per category match the index**

```bash
ls pedagogy-library/01-*/*.md | wc -l   # expect 13
ls pedagogy-library/02-*/*.md | wc -l   # expect 7
ls pedagogy-library/03-*/*.md | wc -l   # expect 6
ls pedagogy-library/04-*/*.md | wc -l   # expect 8
ls pedagogy-library/05-*/*.md | wc -l   # expect 4
ls pedagogy-library/06-*/*.md | wc -l   # expect 5
ls pedagogy-library/07-*/*.md | wc -l   # expect 7
```

**Step 3: Run validator on entire library**

```bash
python pedagogy-library/_schema/validate.py pedagogy-library/
```
Expected: All 50 PASS.

---

## Phase 5 — Verification (Tasks 17–20)

### Task 17: Citation verification pass

**Step 1: Build the citation auditor agent prompt**

Author a prompt that takes one chapter file as input and:
- Extracts every citation from `key_sources` frontmatter and from inline citations in the body.
- Web-searches each citation with the format `<first_author> <year> <title_keywords>`.
- For each, reports: VERIFIED (paper exists, claim plausibly supported) / SUSPECT (paper exists but claim seems mismatched) / NOT FOUND (likely fabricated).

**Step 2: Dispatch verification agents in parallel**

50 sub-agents in parallel, one per chapter file. Each runs the citation audit.

**Step 3: Aggregate results**

Collect each agent's report. Build a single audit summary at `pedagogy-library/_AUDIT-citations.md`:
- Total citations checked
- VERIFIED count
- SUSPECT count + list (chapter + citation)
- NOT FOUND count + list

**Step 4: Fix every NOT FOUND and SUSPECT**

For each flagged citation, dispatch a fix-agent with the specific chapter and the specific issue. Replace the citation with a verified one or remove the unsupported claim.

**Step 5: Commit**

```bash
git add pedagogy-library/_AUDIT-citations.md pedagogy-library/
git commit -m "fix: citation verification pass — replace/remove unverifiable refs"
```

---

### Task 18: Cross-file consistency pass

**Step 1: Dispatch consistency checker**

One agent reads every chapter and checks:
- Effect-size claims for the same principle agree across files (e.g., testing-effect d in `testing-effect.md` should match what `desirable-difficulties.md` cites about retrieval practice).
- Cross-references in `related:` frontmatter are bidirectional where appropriate.
- No two chapters contradict on the same empirical claim.

**Step 2: Aggregate findings**

Output to `pedagogy-library/_AUDIT-consistency.md`. Each finding: chapter A claims X; chapter B claims Y; resolution recommended.

**Step 3: Fix contradictions**

For each finding, decide which chapter is correct (use the more recent meta-analysis as the tiebreaker) and update the other.

**Step 4: Commit**

```bash
git add pedagogy-library/_AUDIT-consistency.md pedagogy-library/
git commit -m "fix: cross-file consistency pass"
```

---

### Task 19: STOP — User gap analysis

**Step 1: Run the audit script**

Build a final summary script that produces a per-category table: chapter count, total citation count, average chapter length, total file size. Output to `pedagogy-library/_AUDIT-coverage.md`.

**Step 2: Surface to user**

Tell user: "All 50 chapters authored, validated, citation-checked, and consistency-checked. The library is at `pedagogy-library/`. Audit reports at:
- `_AUDIT-citations.md` — what we verified vs flagged
- `_AUDIT-consistency.md` — any cross-file contradictions found and fixed
- `_AUDIT-coverage.md` — per-category statistics

Please review and answer:
- Any principles missing that you wanted included?
- Any chapter that reads thinly compared to the exemplar?
- Are the categories balanced enough?
- Should we commission an external SME peer-review pass?"

**Step 3: STOP — await user approval**

If user identifies gaps, dispatch fix-agents for the specific chapters or add new chapters. Iterate until user approves.

---

### Task 20: Final commit + push

**Step 1: Verify clean state**

```bash
cd "C:/Users/nickb/Downloads/caet-practice-public/.claude/worktrees/laughing-shockley-17815f"
git status
```
Expected: clean working tree.

**Step 2: Push branch**

```bash
git push origin claude/laughing-shockley-17815f
```

**Step 3: Generate completion report**

Tell user: "Library A complete. 50 chapters authored across 7 categories, all schema-validated and citation-verified. Ready for handoff to Library B refactor and runtime engine design (separate work)."

---

## Open Questions to Revisit During Execution

- **Visualizations** — Some principles benefit from diagrams (forgetting curves, ZPD diagrams, Bloom's pyramid). Out of scope for v1; consider as a follow-on if user wants illustrated chapters.
- **Multi-language reference** — Library A is English-only. Translation is a follow-on if AEA serves international markets.
- **Versioning** — Once published, chapters need version history when meta-analyses update. Defer until first annual review.
- **Library C (domain adaptations)** — Will likely emerge organically once the avionics tutor runtime is built and we discover which principles need avionics-specific tuning.

---

## Summary

20 tasks across 4 phases (Phase 1 already complete in design doc):

- **Phase 2 (Tasks 0–4):** Author exemplar `testing-effect.md` to set the quality bar. STOP for user approval.
- **Phase 3 (Tasks 5–10):** Build schema, validator, quality checklist, citation rules, authoring brief.
- **Phase 4 (Tasks 11–16):** Test agent dispatch with one principle, STOP for user approval, then dispatch remaining 48 in parallel.
- **Phase 5 (Tasks 17–20):** Citation verification pass, consistency pass, gap analysis with user STOP, final commit.

Estimated wall time: 30 min for Phase 2 (smaller exemplar), 30 min for Phase 3, 45 min for Phase 4 (agents now ~5 min each instead of ~10), 1 hour for Phase 5. Estimated cost: $25–75 for Phase 4 + 5 agent dispatches (about half the original). Frequent commits at every task boundary. STOP gates at Tasks 4, 13, 19.
