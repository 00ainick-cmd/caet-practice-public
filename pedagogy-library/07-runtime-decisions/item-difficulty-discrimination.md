---
id: item-difficulty-discrimination
title: Item Difficulty & Discrimination
category: 07-runtime-decisions
aliases: [irt-item-parameters, b-parameter-a-parameter, item-parameter-selection]
evidence_strength: strong
effect_size: null  # Psychometric framework — IRT defines item parameters and the information function the runtime uses to choose the next item; no single intervention effect size applies. Magnitudes appear instead in CAT efficiency findings (e.g., Weiss 2004: ~50% test-length reduction at fixed precision) which are reported in context.
key_sources:
  - "Lord, F. M. (1980). Applications of item response theory to practical testing problems. Hillsdale, NJ: Lawrence Erlbaum Associates."
  - "Embretson, S. E., & Reise, S. P. (2000). Item response theory for psychologists. Mahwah, NJ: Lawrence Erlbaum Associates."
  - "Birnbaum, A. (1968). Some latent trait models and their use in inferring an examinee's ability. In F. M. Lord & M. R. Novick (Eds.), Statistical theories of mental test scores (pp. 397-479). Reading, MA: Addison-Wesley."
  - "Hambleton, R. K., Swaminathan, H., & Rogers, H. J. (1991). Fundamentals of item response theory. Newbury Park, CA: Sage."
  - "Hambleton, R. K., & Jones, R. W. (1993). Comparison of classical test theory and item response theory and their applications to test development. Educational Measurement: Issues and Practice, 12(3), 38-47. doi:10.1111/j.1745-3992.1993.tb00543.x"
  - "Weiss, D. J. (2004). Computerized adaptive testing for effective and efficient measurement in counseling and education. Measurement and Evaluation in Counseling and Development, 37(2), 70-84. doi:10.1080/07481756.2004.11909751"
  - "van der Linden, W. J., & Glas, C. A. W. (Eds.). (2010). Elements of adaptive testing. New York, NY: Springer. doi:10.1007/978-0-387-85461-8"
last_reviewed: 2026-04-29
applies_to: [measurement, decision]
contraindicated_when:
  - material.uncalibrated_item_pool
  - learner_state.first_exposure
  - task_type.motor_acquisition
  - material.small_pool_no_targeting_room
runtime_triggers:
  - next_item_selection_due
  - ability_estimate_updated
  - item_pool_calibrated
  - mastery_decision_pending
  - exposure_limit_reached
related: [bayesian-knowledge-tracing, sm2-fsrs, mastery-thresholds, knowledge-graph-traversal, distractor-analysis, validity-reliability, item-writing-rules, performance-factor-analysis]
---

# Item Difficulty & Discrimination

## One-line claim

Pick the next item by matching its IRT difficulty parameter `b` to the learner's current ability estimate `θ̂` and preferring items with high discrimination `a`, so each response transmits the most information per minute about what the learner does and does not know.

## Evidence base

Item response theory (IRT) parameterizes each test item with a difficulty `b` (the ability level at which a learner has a 50% chance of correct response, on the same logit scale as ability `θ`) and a discrimination `a` (how steeply the probability of correct response rises with ability around `b`). The two-parameter logistic model — `P(correct | θ) = 1 / (1 + exp(-a(θ - b)))` — was developed in Birnbaum's (1968) chapters of *Statistical Theories of Mental Test Scores* and remains the workhorse parameterization. Lord (1980) consolidated the practical machinery in *Applications of Item Response Theory to Practical Testing Problems*, including the item information function `I(θ) = a²·P(θ)·(1-P(θ))`, which Hambleton, Swaminathan, and Rogers (1991) and Embretson and Reise (2000) re-derived with worked examples. The information function peaks at `θ = b` and scales with `a²`. The runtime consequence is direct: an item delivers maximum information about a learner whose ability matches the item's difficulty, and a high-`a` item delivers proportionally more information than a low-`a` item at the same match.

The information-maximization rule for adaptive item selection follows from those equations, not from a separate empirical claim. Lord (1980) showed that selecting the next item to maximize `I(θ̂)` at the current ability estimate `θ̂` minimizes the asymptotic standard error of measurement. Weiss (2004), reviewing the cumulative computerized adaptive testing (CAT) literature in *Measurement and Evaluation in Counseling and Development*, reported that maximum-information CATs reach the same measurement precision as fixed-form tests with roughly half the items — an efficiency gain that compounds across sessions and is the operational reason adaptive runtimes use IRT-based selection over random or block-sequential delivery. van der Linden and Glas (2010) compiled the modern variants — Fisher information, Kullback-Leibler information, exposure-controlled selection, item-pool maintenance — in *Elements of Adaptive Testing*, all of which preserve the underlying difficulty-matching logic.

The framework has well-documented boundary conditions. Hambleton and Jones (1993) emphasized in their NCME instructional module that IRT parameter estimates require an item pool calibrated on a sample large enough to stabilize `a` and `b` (typical guidance: hundreds of responses per item for the 2PL model). With small samples, classical-test-theory item statistics — proportion correct (`p`) for difficulty, point-biserial correlation (`r_pb`) for discrimination — are the realistic substitutes, with the standard rules of thumb that `r_pb < 0.20` flags a poorly discriminating item. Embretson and Reise (2000) further note that the maximum-information selector concentrates exposure on a small subset of high-`a` items near the ability mode, which degrades content validity and pool security if used without exposure controls. The runtime applies item-information selection within an outer envelope of content-balancing and exposure constraints, not in isolation.

## When to apply

- **Next-item selection is due** — When the runtime must choose the next item from a calibrated
  pool, score each candidate's information at the current ability estimate `θ̂`, select the item
  that maximizes `I(θ̂)` subject to content-balance and exposure constraints. This is the
  baseline operation of any IRT-based adaptive assessment.
- **Ability estimate has just been updated** — After each scored response, re-estimate `θ̂`
  (maximum likelihood or expected a posteriori) and recompute the information ranking before
  picking the next item; do not cache "the next item" decided before the prior response landed.
- **Item pool is calibrated** — Apply the framework only when `a` and `b` exist with stable
  estimates from a calibration sample. For uncalibrated pools, fall back to CTT difficulty (`p`)
  and point-biserial discrimination as documented in Hambleton & Jones (1993).
- **Mastery decision pending** — When deciding whether to advance the learner past a knowledge
  component, route final-pass items toward `b` near the cut score and high `a`, so the pass/fail
  decision sits in the region of maximum measurement precision (see
  [mastery-thresholds](../07-runtime-decisions/mastery-thresholds.md)).
- **Exposure limit reached** — When a high-information item has hit its exposure cap for the
  current cohort, drop to the next-best item by information rather than re-using the capped one;
  pool maintenance is part of the selection rule (van der Linden & Glas, 2010).
- **Initial item placement at session start** — In the absence of a prior `θ̂`, seed with a
  moderate-`b`, high-`a` item near the population mean and converge from one or two responses
  (Weiss, 2004).

## When NOT to apply

- **Item pool has not been calibrated** — Without stable `a` and `b`, the information function
  is meaningless and the runtime is selecting on noise. Hambleton et al. (1991) recommend at
  least several hundred responses per item before trusting 2PL estimates; for small pools,
  switch to classical item statistics and accept the precision loss.
- **Learner is in the first-exposure encoding phase** — Difficulty-matched selection is a
  measurement and decision tool, not an instruction tool. While the learner is building a mental
  model, the right move is worked examples and guided practice
  ([cognitive-load-theory](../01-learning-science/cognitive-load-theory.md)), not
  maximum-information probing.
- **Pure motor skill acquisition** — IRT scores binary or polytomous responses against a latent
  trait. Procedural motor execution does not reduce to that signal during encoding;
  verbal-conceptual companion items can be IRT-selected, the motor execution itself cannot.
- **Item pool is too small to leave targeting room** — When the pool has only a handful of items
  at any given `θ`, the selector reduces to "pick whatever's left" and exposure controls
  collapse. With fewer than ~5–10 items inside a half-logit window of `θ̂`, switch to fixed-form
  or domain-balanced random selection (van der Linden & Glas, 2010).
- **Decisions need content coverage, not precision on a single trait** — A certification exam
  with content-blueprint requirements must cover specified subdomains in mandated proportions;
  pure information-maximization ignores those constraints. Use IRT inside a constrained-CAT
  framework, not as the sole selection rule.

## How to apply

- **Compute item information at the current `θ̂` for every candidate** — `I(θ̂) = a²·P(θ̂)·(1-P(θ̂))`
  for the 2PL; for 3PL include the lower asymptote `c`. Rank candidates by `I(θ̂)`, intersect
  with content-balance and exposure constraints, pick the top-ranked admissible item.
- **Center `b` on the current ability estimate** — Items with `b` within ±0.5 logit of `θ̂`
  carry near-peak information; outside ±1.0 logit the information collapses. Do not serve
  far-easy or far-hard items except for ceiling/floor screening or initial seeding.
- **Prefer high `a` (discrimination ≥ 1.0) within the difficulty band** — Sort the band by `a`
  descending. High-`a` items deliver `a²×` more information at matched difficulty (Embretson &
  Reise, 2000); preferring them shortens tests at fixed precision (see
  [validity-reliability](../03-assessment-science/validity-reliability.md) for SEM consequences).
- **Cap exposure with Sympson-Hetter or randomesque selection** — Pure max-information
  over-exposes a small subset. Apply an exposure ceiling (commonly 30%) or randomize among the
  top-`k` admissible items per step (van der Linden & Glas, 2010).
- **Tighten difficulty around the mastery cut for pass/fail decisions** — Route the final 3–5
  items to `b` within ±0.3 logit of the cut; this is where item information about the decision
  is highest and classification error is lowest (see
  [mastery-thresholds](../07-runtime-decisions/mastery-thresholds.md)).
- **Fall back to CTT statistics on uncalibrated pools** — Without IRT calibration, target items
  with `p` near 0.5 (shifted toward the desired difficulty) and `r_pb ≥ 0.30`. Drop or flag
  items with `r_pb < 0.20`; low-discrimination items add noise without resolving ability
  (Hambleton & Jones, 1993). See
  [distractor-analysis](../03-assessment-science/distractor-analysis.md) for the diagnostics.
- **Re-estimate `θ̂` after each response, not on a schedule** — The information ranking can
  flip after a single unexpected response, especially early when `θ̂` is imprecise. Ranking
  once and serving down a queue is the most common implementation error.

## Common misapplications

- **Treating CTT proportion-correct as IRT difficulty** — `p = 0.5` is not `b = 0`. CTT
  difficulty is sample-dependent; IRT difficulty is on the ability scale. Hambleton and Jones
  (1993) detail where the two diverge — especially for low-`p` items where guessing inflates
  `p` without affecting `b`.
- **Selecting on `a` while ignoring `b`** — A high-discrimination item far from `θ̂`
  contributes little information; `I(θ̂)` collapses as `|θ̂ - b|` grows because `P·(1-P) → 0`.
  Discrimination amplifies the difficulty-match advantage, it does not substitute for it.
- **Running max-information selection without exposure control** — In closed pools this burns
  high-information items into wide exposure and degrades pool security and content validity.
  Combine with Sympson-Hetter, conditional-exposure, or top-`k` randomization from the start.
- **Updating `θ̂` only at session end** — Adaptive selection requires per-response
  re-estimation; otherwise the runtime is delivering a fixed-form sequence with extra
  bookkeeping. Weiss (2004) is explicit that the efficiency gain comes from per-response adaptation.
- **Ignoring local item dependence** — When items share a stimulus (passage, wiring diagram),
  the 2PL/3PL independence assumption breaks and information additivity overstates precision.
  Use a testlet model or treat the cluster as one polytomous unit.
- **Trusting parameter estimates from undersized calibration samples** — `a` is especially
  unstable below ~500 responses per item. A 2PL fit on a 50-response calibration produces
  rankings that are mostly noise; the runtime then "adapts" against that noise (Hambleton et
  al., 1991).

## Examples across domains

**Avionics — adaptive end-of-module assessment for a Garmin GTN 750 navigator installation course.**

*Setup.* The shop's training platform has a calibrated 240-item bank covering the GTN 750
installation module: pinout interpretation, configuration menus, antenna isolation checks,
RAIM rules, and post-install verification. Calibrated on ~1,800 prior technicians — `a` and
`b` stable. The runtime must decide pass/fail at mastery cut `θ_cut = 0.0` with SEM ≤ 0.30.

*Selection.* The first item is `b ≈ 0.0, a ≈ 1.4`, a configuration-menu question seeded near
the population mean. Correct; `θ̂` updates to +0.4, SEM 0.85. The runtime ranks admissible
items (not yet served, not exposure-capped, inside the subdomain rotation) by `I(0.4)`, picks
`b ≈ 0.4, a ≈ 1.6` — an antenna-isolation calculation. Wrong; `θ̂` drops to +0.1, SEM 0.62.
Re-rank; next item `b ≈ 0.0, a ≈ 1.5`. After 12 items, `θ̂ = +0.18`, SEM = 0.28 — inside
target — runtime stops. A fixed-form 24-item test would hit the same SEM with twice the seat
time (Weiss, 2004, on roughly 50% length reduction at matched precision).

*Decision.* The final 4 items were routed to `b` within ±0.3 logit of the cut and the
resulting SEM is 0.28, so the pass decision sits in the region of maximum classification
precision. The technician advances to the practical install rubric.

**Music performance — adaptive harmonic-analysis assessment in a private piano studio's quarterly progress test.**

*Setup.* A piano teacher uses a calibrated 180-item digital bank covering interval
identification, key-signature recognition, chord-quality labeling (major/minor/diminished/
augmented + inversions), and short-passage harmonic analysis from late-intermediate to
early-advanced. Calibrated on ~600 studio-network students; `b` and `a` stable. The teacher
needs `θ` to decide whether to advance the student from "Level 5" to "Level 6" repertoire.

*Selection.* Seed with `b ≈ 0.0, a ≈ 1.3`, a chord-quality item near the Level-5/6 boundary.
Correct; `θ̂` moves to +0.3, SEM 0.80. The runtime picks the highest-`I(0.3)` admissible item
— `b ≈ 0.4, a ≈ 1.5`, a short-passage key-modulation question. Wrong; `θ̂` drops to +0.05,
SEM 0.60. Twelve items in, `θ̂ = +0.10`, SEM = 0.32. Exposure control caps the showpiece
V7-of-V modulation item below 30% of sessions, and the rotation across subdomains keeps the
test honoring the harmonic-analysis blueprint rather than degenerating into the two
highest-information items.

*Decision.* The Level-6 cut sits at `θ_cut = +0.20`, so the final three items route to `b`
within ±0.3 logit of +0.20 (high-`a` interval-recognition and chord-inversion items). The
resulting `θ̂ = +0.10` with SEM 0.32 places the student below the cut at the stopping
precision; the teacher holds them at Level 5 for one more cycle and schedules targeted
retrieval drills on the missed items
(see [testing-effect](../01-learning-science/testing-effect.md)).

## Quality signal

Adaptive selection is working when (a) the SEM of `θ̂` decreases monotonically across the session and reaches the stopping criterion (e.g., SEM ≤ 0.30) in roughly half the items required by a fixed-form test of comparable precision (Weiss, 2004), and (b) item-exposure rates across the cohort stay below the runtime's ceiling (commonly 30%). A faster within-session signal: at least 70% of served items fall within ±0.5 logit of the current `θ̂` after the third response. Drift to extremes or oscillation indicates an unstable `θ̂` (too few items so far) or an undersized pool in the active band.

## Cross-references

- See [bayesian-knowledge-tracing](../07-runtime-decisions/bayesian-knowledge-tracing.md) for the per-knowledge-component mastery probabilities that complement IRT-based item selection at the trait level.
- See [sm2-fsrs](../07-runtime-decisions/sm2-fsrs.md) for the spacing schedulers that pair with item-information selection on the timing axis.
- See [mastery-thresholds](../07-runtime-decisions/mastery-thresholds.md) for the cut-score logic that determines where to concentrate item difficulty during pass/fail decisions.
- See [distractor-analysis](../03-assessment-science/distractor-analysis.md) for the item-level diagnostics that feed the discrimination parameter `a` from response patterns.
- See [validity-reliability](../03-assessment-science/validity-reliability.md) for the standard-error-of-measurement framing the information function operationalizes.
- See [item-writing-rules](../03-assessment-science/item-writing-rules.md) for the construction quality that determines whether high-`a` items are achievable in the first place.
- See [knowledge-graph-traversal](../07-runtime-decisions/knowledge-graph-traversal.md) for content-balancing constraints layered on top of pure information-maximization.
- See [performance-factor-analysis](../07-runtime-decisions/performance-factor-analysis.md) for an alternative framework that estimates per-skill ability from response history without requiring item calibration.
