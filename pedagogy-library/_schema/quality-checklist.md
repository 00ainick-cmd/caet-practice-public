# Chapter Quality Checklist

Tick every box before approving a chapter. Authors run this on themselves first; reviewers run it
again. The exemplar (`pedagogy-library/01-learning-science/testing-effect.md`) passes every line
of this checklist — it is the calibration target.

## Length

- [ ] File is between 120 and 200 lines (`wc -l <file>` confirms within bounds)
- [ ] Padding has been cut — every line is load-bearing, every bullet earns its place
- [ ] Prose is confined to "Evidence base"; operational sections are bulleted

## Frontmatter

- [ ] All 11 required frontmatter fields present (`aliases` is optional, +1 if used) and
      validate against `chapter-schema.yaml`
- [ ] `id` is lowercase-kebab, matches the filename stem, and matches the canonical slug in
      `pedagogy-library/README.md`
- [ ] `category` matches the parent directory name exactly (e.g., `01-learning-science`)
- [ ] `evidence_strength: strong` — moderate is allowed by schema but the library filters to
      strong in Phase 4 (deviation requires controller approval)
- [ ] `effect_size` is quantified with a citation in the same string (Cohen's d, Hedges' g, or
      odds ratio), OR explicitly `null` with a justification comment for foundational principles
      (cognitive load, schema theory, Bloom's taxonomy, etc.)
- [ ] `key_sources` has 5–7 entries, each a full APA-format citation including DOI when available
- [ ] `applies_to` uses only the controlled vocabulary
      (`acquisition`, `retention`, `transfer`, `measurement`, `sequencing`, `decision`)
- [ ] `contraindicated_when` uses `category.predicate` form
      (`learner_state.*`, `material.*`, `task_type.*`) — see README "Schema conventions"
- [ ] `runtime_triggers` are lowercase snake_case event names (no dots)
- [ ] `related` slugs all appear in the README index
- [ ] `last_reviewed` is today's ISO date (`YYYY-MM-DD`)

## Citations

- [ ] Every citation is verifiable via `WebSearch` for `<first_author> <year> <title_keywords>`
      — the author has actually run the search and confirmed the paper exists
- [ ] No fabricated citations — no invented authors, journals, page ranges, or DOIs
- [ ] Effect-size claims trace to a meta-analysis or empirical paper, not a textbook
- [ ] Replication notes cite the actual replication paper, not the original
- [ ] DOIs included where the publisher provides them
- [ ] Each citation's abstract supports the claim it's used for (DOI verification alone is not
      sufficient — see `citation-rules.md` "Bertilsson lesson")

## Body sections (all 9 in this exact order)

- [ ] `## One-line claim` — single operational sentence the runtime can act on
- [ ] `## Evidence base` — 2–3 dense paragraphs covering foundational study, modern
      meta-analysis, and known boundary condition
- [ ] `## When to apply` — bulleted trigger conditions that match the `runtime_triggers`
      frontmatter
- [ ] `## When NOT to apply` — bulleted contraindications matching the `contraindicated_when`
      frontmatter, each a specific scenario not a platitude
- [ ] `## How to apply` — bulleted concrete moves with cross-references to related chapters
- [ ] `## Common misapplications` — bulleted anti-patterns drawn from the literature
- [ ] `## Examples across domains` — exactly 2 worked scenarios, parallel depth (see
      "Cross-domain examples" below)
- [ ] `## Quality signal` — 2–3 line measurable success criterion the runtime can compute
- [ ] `## Cross-references` — 5+ links using canonical slugs from the README

## Operational utility (the AI tutor test)

- [ ] An AI tutor reading "When to apply" + "How to apply" could act on this principle without
      consulting a separate textbook
- [ ] Triggers are concrete and testable (e.g., "pre-assessment below 50% on current segment"
      not "learner is struggling")
- [ ] Contraindications are specific scenarios with observable signals, not generic warnings
- [ ] "How to apply" moves are executable behaviors (what the tutor says or does), not
      abstract principles

## Style

- [ ] Active voice; direct sentences; no hedging language ("it might be the case that…")
- [ ] Reads like a clinical practice guideline, not a textbook chapter
- [ ] No marketing-style adjectives ("powerful", "amazing", "groundbreaking")
- [ ] Inline cross-references use canonical slug paths
      (e.g., `[spaced-retrieval](../01-learning-science/spaced-retrieval.md)`)

## Cross-domain examples (the generalization test)

- [ ] Exactly 2 examples, no more, no less
- [ ] One IS avionics (mandatory — this is the parent program's anchor domain)
- [ ] The other is genuinely different — not another aviation/electronics scenario
      (basketball, mortgage sales, K-12 math, software engineering education, medical training,
      culinary apprenticeship, language learning, etc.)
- [ ] Both examples specify Setup, the principle's application, and where applicable Spacing or
      a follow-up move (parallel structure to the exemplar)
- [ ] Both examples at the same level of specificity — no half-page avionics example next to a
      one-line basketball example

## Validator

- [ ] `python pedagogy-library/_schema/validate.py pedagogy-library/<category>/<id>.md`
      exits 0 (no errors)
- [ ] Any warnings emitted are only about not-yet-authored cross-references — those are
      expected during Phase 4 and acceptable
- [ ] No frontmatter schema errors, no missing-section errors, no line-count errors

## Final read-through

- [ ] Read the chapter end-to-end once more before marking complete
- [ ] Skim "When to apply" and "How to apply" out of context — would a fresh tutor know what
      to do? If not, tighten
- [ ] Confirm the chapter doesn't contradict the exemplar's depth or tone
