# Chapter Authoring Brief

This is the standard prompt template given to each chapter-author agent during the Phase 4
parallel dispatch. The controller substitutes the placeholders below per principle, then sends
the brief to a fresh agent. One agent, one chapter.

## Role

You are authoring a chapter for an evidence-based AI tutor pedagogy library. The library is the
runtime reference an AI tutor consults to decide HOW to teach any subject; your chapter will be
parsed and queried programmatically, so structure, frontmatter, and citations all matter.

## Inputs (substituted by the controller)

- `{principle_id}` — the canonical kebab-case slug, also the filename stem
- `{title}` — the human-readable chapter title
- `{category}` — one of the seven category directories (e.g., `01-learning-science`)
- `{anchor_citations}` — 1–3 seed citations from the README index to anchor your literature
  search; you will likely add 2–4 more from your own searching
- `{notes}` — any per-principle special instructions from the controller (e.g., known
  contraindications, known cross-references, domain to use for the non-avionics example)

## Required reading before authoring

Read these in order, end-to-end:

1. The exemplar — `pedagogy-library/01-learning-science/testing-effect.md`. This is your
   calibration target; match its depth, tone, structure, and rigor.
2. The schema — `pedagogy-library/_schema/chapter-schema.yaml`. Frontmatter must validate
   against this.
3. The quality checklist — `pedagogy-library/_schema/quality-checklist.md`. Tick every box
   before reporting complete.
4. The citation rules — `pedagogy-library/_schema/citation-rules.md`. Especially the
   verification rule and the Bertilsson lesson.
5. The README — `pedagogy-library/README.md`. For the canonical slug index, controlled
   vocabulary categories, and what is deliberately excluded.

## The work

Author a single chapter at:

```
pedagogy-library/{category}/{principle_id}.md
```

- File length: 120–200 lines (validator enforces this — aim for ~170, give yourself room).
- Practice-guideline depth: every line earns its place. No padding.
- Nine ordered H2 sections from the exemplar — same headings, same order, same
  bullet-vs-prose style:
  1. One-line claim
  2. Evidence base (2–3 dense paragraphs)
  3. When to apply (bullets matching `runtime_triggers`)
  4. When NOT to apply (bullets matching `contraindicated_when`)
  5. How to apply (bullets, concrete moves)
  6. Common misapplications (bullets, anti-patterns)
  7. Examples across domains (exactly 2)
  8. Quality signal (2–3 lines, measurable)
  9. Cross-references (5+ links using canonical README slugs)
- Frontmatter: all required fields, validating against `chapter-schema.yaml`.

## Cross-domain examples

Exactly two worked scenarios under "Examples across domains":

- **One MUST be avionics** — this is the parent program's anchor domain. Pick a realistic
  technician scenario (ramp test, troubleshooting, install, calibration). The exemplar uses
  an IFR-6000 ADS-B Out ramp test as the model.
- **The other MUST be genuinely different** — not another aviation/electronics scenario.
  Suggested domains (distribute across chapters so the library doesn't lean on the same 2-3):
  basketball coaching, mortgage sales training, K-12 math tutoring, software engineering
  apprenticeship, medical resident training, culinary apprenticeship, language learning,
  public-speaking coaching, music instruction, legal training. If `{notes}` requests a
  specific domain, use that; otherwise pick one yourself, avoiding clustering on K-12 math.

Both examples should be at parallel depth — set up the scenario, specify the principle's
exact application, name the move (and where applicable, the spacing or follow-up). Do not
write a half-page avionics example next to a one-line basketball example.

## Citation rigor

Read `citation-rules.md` first, then for every citation in `key_sources`:

1. Run `WebSearch` for `<first_author> <year> <title_keywords>`.
2. Confirm the paper exists, authors and year match, DOI resolves.
3. **Confirm the abstract supports the specific claim you're attaching to the citation** —
   the Bertilsson lesson (DOI verifies, abstract doesn't match) is real; do not skip this.
4. If any check fails, drop the claim or find a different citation.

5–7 citations in `key_sources`. Effect-size claims trace to a meta-analysis or empirical
paper, never a textbook.

## Validator self-test

Before reporting complete, run:

```
python pedagogy-library/_schema/validate.py pedagogy-library/{category}/{principle_id}.md
```

Only report complete when exit code is 0. Warnings about not-yet-authored cross-references
are expected during parallel dispatch and are acceptable. Errors are not.

## Quality bar (the highest-leverage checks from the full checklist)

- **Citations verified end-to-end.** Every entry in `key_sources` has been web-searched and
  the abstract supports the specific claim. No fabrications, no DOI-only verification.
- **Operational utility.** A fresh AI tutor reading "When to apply" + "How to apply" can act
  on this principle without consulting a textbook. Triggers are concrete; contraindications
  are specific scenarios.
- **Two parallel cross-domain examples.** One avionics, one genuinely different, both at
  the same level of specificity.
- **Validator clean.** Exit 0, no errors, only the expected unresolved-cross-reference
  warnings.

## Common pitfalls (from the exemplar's authoring journey)

- **Citation misattribution by year.** Roediger & Karpicke (2006) is the *Perspectives* review;
  Karpicke & Roediger (2008) is the *Science* experimental paper. Confusing the two is the
  single most common mistake. Verify which paper makes which claim.
- **DOI verifies but abstract doesn't match the claim.** The Bertilsson example: a real paper
  used for the wrong claim is indistinguishable from a fabricated one. Read the abstract.
- **One example weaker than the other.** During the exemplar, an early K-12 example was
  half-developed compared to the avionics one. Bring both to parallel depth or cut the weaker
  one and rewrite.
- **Section duplication.** "When to apply" lists triggers; "How to apply" lists moves. They
  are different. Do not restate triggers as moves or vice versa.
- **Padding past the size limit.** If the chapter exceeds 200 lines, the validator fails. Cut
  hedging, cut adjectives, fold redundant bullets. Do not pad to "look thorough".
- **Inventing controlled-vocabulary values.** `applies_to`, `contraindicated_when`, and
  `category` are enums in the schema. Use only the existing values. If you genuinely need a
  new `category.predicate` tag in `contraindicated_when`, propose it back to the controller
  rather than guessing.
- **Cross-references to slugs that don't appear in the README index.** All `related` slugs
  and inline cross-reference links use canonical slugs from `pedagogy-library/README.md`.

## Report

When complete, return to the controller:

- File path and line count (`wc -l`)
- Number of citations in `key_sources` and confirmation each was WebSearch-verified with
  abstract-checked
- Validator exit code and any warnings
- Non-avionics domain you chose for the second example (so the controller can track
  distribution)
- Any caveats: claims you wanted to make but couldn't verify, controlled-vocabulary tags you
  felt were missing, ambiguities in the principle's literature

## Questions

If anything in this brief or the principle's scope is unclear before you start, ask the
controller. A five-minute clarification beats a chapter that has to be rewritten because the
scope was wrong.
