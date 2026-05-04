---
id: distractor-analysis
title: Distractor Analysis
category: 03-assessment-science
aliases: [option-analysis, foil-analysis, choice-frequency-analysis]
evidence_strength: strong
effect_size: null  # Distractor analysis is a measurement-quality diagnostic, not an instructional intervention. The relevant magnitudes are item-level statistics — proportion-endorsing each option, distractor point-biserial r_pb, IRT trace-line slope — reported per item, not as a single intervention effect size. Empirical magnitudes from the literature (e.g., ~50% of distractors non-functioning in Tarrant et al. 2009) are cited inline.
key_sources:
  - "Haladyna, T. M., & Rodriguez, M. C. (2013). Developing and validating test items. New York, NY: Routledge. doi:10.4324/9780203850381"
  - "Haladyna, T. M., Downing, S. M., & Rodriguez, M. C. (2002). A review of multiple-choice item-writing guidelines for classroom assessment. Applied Measurement in Education, 15(3), 309-333. doi:10.1207/S15324818AME1503_5"
  - "Gierl, M. J., Bulut, O., Guo, Q., & Zhang, X. (2017). Developing, analyzing, and using distractors for multiple-choice tests in education: A comprehensive review. Review of Educational Research, 87(6), 1082-1116. doi:10.3102/0034654317726529"
  - "Rodriguez, M. C. (2005). Three options are optimal for multiple-choice items: A meta-analysis of 80 years of research. Educational Measurement: Issues and Practice, 24(2), 3-13. doi:10.1111/j.1745-3992.2005.00006.x"
  - "Haladyna, T. M., & Downing, S. M. (1993). How many options is enough for a multiple-choice test item? Educational and Psychological Measurement, 53(4), 999-1010. doi:10.1177/0013164493053004013"
  - "Tarrant, M., Ware, J., & Mohammed, A. M. (2009). An assessment of functioning and non-functioning distractors in multiple-choice questions: A descriptive analysis. BMC Medical Education, 9, 40. doi:10.1186/1472-6920-9-40"
  - "Downing, S. M. (2005). The effects of violating standard item writing principles on tests and students: The consequences of using flawed test items on achievement examinations in medical education. Advances in Health Sciences Education, 10(2), 133-143. doi:10.1007/s10459-004-4019-5"
last_reviewed: 2026-04-29
applies_to: [measurement, decision]
contraindicated_when:
  - material.uncalibrated_item_pool
  - material.small_pool_no_targeting_room
  - task_type.motor_acquisition
runtime_triggers:
  - item_response_data_available
  - item_pool_review_due
  - item_flagged_low_discrimination
  - new_item_pilot_complete
  - cohort_results_aggregated
related: [item-writing-rules, item-difficulty-discrimination, validity-reliability, bloom-levels-in-assessment, error-analysis-corrective-feedback, pre-post-assessment-effect-size, mastery-threshold-transfer-test-design]
---

# Distractor Analysis

## One-line claim

For each multiple-choice item, examine how many examinees chose each incorrect option and how that choice correlates with total-test performance, then revise or replace any distractor that fails to attract a meaningful share of low-scorers more than high-scorers.

## Evidence base

Distractor analysis is the per-item, per-option diagnostic that distinguishes a multiple-choice item that measures the intended construct from one that merely fills space. Haladyna and Rodriguez (2013), in *Developing and Validating Test Items*, define a functioning distractor with two empirical criteria: (a) selected by ≥5% of examinees, and (b) point-biserial with total score is negative — lower-scoring examinees choose it more often than higher-scoring ones. Distractors failing either test contribute no information about ability and effectively shrink the item to fewer working options. Haladyna, Downing, and Rodriguez (2002) codified plausibility, parallelism, and avoidance of giveaway cues as the construction conditions that make functioning distractors achievable; distractor analysis is the post-hoc audit confirming whether construction succeeded.

The empirical record on how often construction succeeds is sobering. Haladyna and Downing (1993) reported in *Educational and Psychological Measurement* that across the multiple-choice items they reviewed, only a minority of four- and five-option items had three or more functioning distractors; the modal item had one or two. Tarrant, Ware, and Mohammed (2009), examining 514 items (1,542 distractors) from a Hong Kong nursing program in *BMC Medical Education*, found that 47.8% of distractors were non-functioning by the standard criteria, and 10.2% were chosen by zero examinees. Rodriguez's (2005) meta-analysis of 80 years of research in *Educational Measurement: Issues and Practice* concluded that three-option items match four- or five-option items on reliability and validity per item and beat them on items-per-minute throughput, precisely because additional distractors typically do not function. Gierl, Bulut, Guo, and Zhang (2017), reviewing the modern literature in *Review of Educational Research*, synthesized the diagnostic methods (option choice frequency, distractor point-biserial, IRT trace lines, distractor-driven misconception inference) and emphasized that the analysis is the bridge between item-construction theory and item-pool maintenance.

Distractor analysis is also the principal mechanism by which item-writing flaws translate into measurement damage. Downing (2005), in *Advances in Health Sciences Education*, documented that 36–65% of items on four medical-school basic-science exams were flawed in ways that affected option performance, flawed items were 0–15 percentage points more difficult than parallel standard items, and the construct-irrelevant variance introduced could shift up to 10–15% of pass/fail decisions. The link is mechanical: a flaw such as an implausible distractor, a stem clue, or a "none of the above" lifeboat shows up first in the option-choice distribution, and distractor analysis surfaces it before the next administration.

## When to apply

- **Item response data are available** — Once a cohort (n ≥ 30 per item for stable
  percentages, n ≥ 200 for stable point-biserials) has responded, run distractor analysis
  before the item is reused. New items pilot first; diagnostics gate promotion to scored use.
- **Periodic item-pool review is due** — On a recurring cadence (per cohort, term, or
  certification cycle), audit every active item's option-frequency table and distractor
  point-biserials; flag drift to drive revision, retirement, or replacement decisions.
- **Item flagged for low overall discrimination** — When an item's r_pb drops below the
  program threshold (commonly 0.20), distractor analysis is the first diagnostic step: the
  cause is almost always non-functioning distractors, a miskeyed key, or a positive-r_pb
  distractor that high-scorers are choosing. The fix follows from which pattern appears.
- **New item has just completed pilot administration** — Before promotion to the scored
  pool, confirm every distractor was selected by ≥5% with negative point-biserial. Pilots
  that fail are revised or replaced rather than promoted (Haladyna & Rodriguez, 2013).
- **Cohort results aggregated for a high-stakes decision** — Before issuing pass/fail letters
  or certification, inspect items near the cut for distractor anomalies that could have
  shifted classification — the post-hoc validity check against Downing's (2005)
  construct-irrelevant variance.

## When NOT to apply

- **Sample size is too small for stable estimates** — Below ~30 examinees per item, option
  proportions swing on a single response and point-biserials are unstable; below ~200 the
  r_pb confidence interval routinely spans the 0.20 threshold. Tarrant et al. (2009) and
  Haladyna & Rodriguez (2013) flag underpowered samples as a primary cause of spurious
  "non-functioning" verdicts. Wait for adequate volume or pool across cohorts.
- **Item pool is too small to leave revision room** — When a 30-item bank is fully in use,
  retiring an item on distractor evidence creates a content gap the pool cannot fill. The
  diagnostic is still informative, but action requires concurrent item development.
- **Pure motor skill assessment** — Distractor analysis applies to selected-response items.
  Performance assessments and motor-procedure check-offs use rubric-criterion analysis
  instead (see [validity-reliability](../03-assessment-science/validity-reliability.md) for
  the generalizability-theory framing).
- **Items scored for partial credit** — Polytomous or multi-key items ("select all that
  apply" with partial credit) require partial-credit IRT diagnostics; the binary
  functioning-distractor criterion does not transfer.

## How to apply

- **Build the option-frequency table for every item** — Tabulate the percentage selecting
  each option, segmented by upper and lower thirds (or quartiles) of total score. The key's
  rate should rise from lower to upper; each distractor's rate should fall. Reversed
  gradients are immediate flags.
- **Compute the point-biserial for each option, not just the key** — Each option's r_pb
  against total score should be negative for distractors and positive for the key. A
  distractor with positive r_pb means high-scorers are picking it — miskeyed, ambiguous, or
  a "distractor" that is actually the better answer. Haladyna & Rodriguez (2013) treat this
  as the most diagnostic single statistic.
- **Apply the 5% / negative-r_pb functioning rule** — Tag a distractor as functioning if
  selected by ≥5% AND r_pb < 0; otherwise non-functioning. Items with two or more
  non-functioning distractors are revision candidates (Tarrant et al., 2009).
- **Read distractor patterns as misconception evidence** — When a single distractor attracts
  20%+ across a cohort and skews toward mid-scorers, it is almost certainly capturing a real
  misconception, not random error. Preserve it (it is doing diagnostic work) and feed the
  misconception back into instruction (see
  [error-analysis-corrective-feedback](../04-delivery-patterns/error-analysis-corrective-feedback.md)).
- **Trim to the empirical option count, not the policy option count** — When two distractors
  are persistently non-functioning across cohorts, drop them. Rodriguez (2005) showed
  three-option items match four/five-option on reliability while freeing items-per-minute
  capacity; chasing four functioning distractors is rarely worth the construction cost.
- **Inspect items near the cut score with extra care** — For pass/fail decisions, items
  with `p` near the cut carry the most classification weight. Apply tighter thresholds
  (functioning rate ≥80%, no positive-r_pb distractors) on these items per Downing (2005)
  on construct-irrelevant variance at decision boundaries.
- **Re-pilot revised items before scoring** — A revised distractor is a new item
  psychometrically. Re-pilot; do not assume the previous calibration carries. Feed cleaned
  items back into the calibration step that
  [item-difficulty-discrimination](../07-runtime-decisions/item-difficulty-discrimination.md)
  consumes.

## Common misapplications

- **Treating non-functioning distractors as harmless** — A non-functioning distractor reduces
  the effective option count and inflates the guessing-corrected difficulty (Haladyna &
  Downing, 1993). The item is no longer measuring what its blueprint claimed.
- **Ignoring positive-r_pb distractors as a "minor anomaly"** — A distractor high-scorers
  choose is the single strongest signal the item is broken: miskeyed, two defensible
  answers, or the "distractor" is actually the better answer than the scored key. Stop
  scoring it until it is fixed (Haladyna & Rodriguez, 2013).
- **Running the analysis on too small a sample, then trusting the verdict** — A 12-examinee
  pilot will mark half of working distractors "non-functioning" by chance. Tarrant et al.
  (2009) insist on adequate sample size before action.
- **Confusing item difficulty with distractor quality** — A hard item (`p` = 0.30) is not
  the same as a flawed item. The diagnostic is the option-choice gradient across ability,
  not whether the item is hard. A well-functioning hard item shows lower-group examinees
  distributed across the distractors and upper-group examinees concentrated on the key.
- **Auto-revising every flagged distractor without reading the cohort response** — Some
  fail because the cohort no longer holds the misconception they were written to capture —
  good news about instruction, not bad news about the item. Distinguish "implausible from
  the start" (revise) from "misconception extinct" (retire and replace with a current one).
- **Stuffing a fourth or fifth distractor to look thorough** — Implausible filler distractors
  are the modal item-writing flaw in Haladyna et al. (2002). Three plausible options beat
  five with two non-functioning fillers on every empirical metric Rodriguez (2005) reviewed.

## Examples across domains

**Avionics — distractor audit on a Garmin GTN 750 installation knowledge test.**

*Setup.* A regional shop's 40-item end-of-module test on GTN 750 installation (configuration,
pinout, RAIM, antenna isolation) was completed by 142 spring-cohort technicians. The
assessment lead pulls the option-frequency report. Item 17 — "Which RAIM mode is required
for IFR enroute approach use of the GTN 750 GPS?" — has overall `p` = 0.62 and overall r_pb
0.18, just under the program's 0.20 cutoff.

*Distractor analysis.* Option-frequency by score third: A (key) 72%/64%/48% upper/middle/
lower (working as designed); B 4%/12%/16% (functioning, r_pb = -0.18); C 22%/22%/24% (flat
across thirds, near-zero r_pb, including a chunk of upper-third examinees); D 2%/2%/12%
(functioning at the lower end, r_pb = -0.21). The lead inspects C — "Fault Detection (FD)
only" — defensible for non-precision approach but ambiguous against the keyed "FDE"
depending on how "approach use" reads. High-scorers who read the stem as covering both
enroute and approach are picking C correctly within their reading.

*Decision.* The item is rewritten to "RAIM mode required for IFR enroute and terminal
operations under FAA TSO-C145/C146" and re-piloted; distractor C becomes "WAAS-only, RAIM
disabled." Items 22 and 31, each with one non-functioning distractor (<3%), are trimmed to
three options per Rodriguez (2005). At the program's 75% cut, the pre-revision Item 17 alone
would have unfairly held back ~6 of 142 technicians (Downing, 2005, on construct-irrelevant
variance at the cut).

**K-12 math — distractor diagnostics on a 5th-grade fractions unit assessment.**

*Setup.* A district math team has administered a 25-item fractions assessment to 612
fifth-graders. Item 8: "Add 1/3 + 1/4. Which is closest to the correct sum?" Options:
A) 7/12, B) 2/7, C) 1/7, D) 1/12. Item statistics: `p` = 0.41, r_pb = 0.34 — discriminating
reasonably, but unusually difficult for the unit.

*Distractor analysis.* B (2/7) is selected by 44% of the cohort — more than the keyed A
(41%) — with r_pb = -0.08 (mildly negative; lower third picks it slightly more than upper).
B is selected at 41% / 38% by middle / upper thirds. C (1/7) and D (1/12) draw 9% and 6%
with strongly negative r_pb (-0.28, -0.31). The team recognizes B as the canonical "add
numerators, add denominators" misconception (1+1 over 3+4).

*Decision.* B is preserved — its high cross-third selection rate is misconception evidence
to act on, not noise. The team flags the misconception for targeted re-teaching with
bar-model representations and schedules spaced retrieval on fraction-addition reasoning over
four weeks (see
[error-analysis-corrective-feedback](../04-delivery-patterns/error-analysis-corrective-feedback.md)
and [testing-effect](../01-learning-science/testing-effect.md)). C and D, functioning at
low rates, cleanly separate low-skill guessing from the misconception captured by B; the
item is not revised. Tarrant et al. (2009) frame this as the textbook case where distractor
analysis informs instruction rather than item revision.

## Quality signal

Distractor analysis is producing decisions when, after each cohort, every active item has at minimum two functioning distractors (≥5% selection rate, negative point-biserial) and zero distractors with positive point-biserial; items violating either rule are routed to revision before re-administration. A second signal: across the pool, the proportion of non-functioning distractors should trend downward across cohorts as the audit-and-revise loop runs — Tarrant et al. (2009) found 47.8% non-functioning at baseline; programs with active maintenance typically drop below 25% within two to three cycles.

## Cross-references

- See [item-writing-rules](../03-assessment-science/item-writing-rules.md) for the construction guidelines (plausibility, parallelism, avoiding clues) that determine whether distractors can function in the first place.
- See [item-difficulty-discrimination](../07-runtime-decisions/item-difficulty-discrimination.md) for how the distractor-cleaned item statistics feed downstream IRT calibration and adaptive selection.
- See [validity-reliability](../03-assessment-science/validity-reliability.md) for the broader framework distractor analysis serves — every non-functioning distractor is construct-irrelevant variance.
- See [bloom-levels-in-assessment](../03-assessment-science/bloom-levels-in-assessment.md) for matching item cognitive level to the distractor patterns appropriate at each level.
- See [error-analysis-corrective-feedback](../04-delivery-patterns/error-analysis-corrective-feedback.md) for how to use distractor patterns as misconception data that drives re-teaching, not just item revision.
- See [pre-post-assessment-effect-size](../03-assessment-science/pre-post-assessment-effect-size.md) for the program-level evaluation that depends on items being free of construct-irrelevant variance.
- See [mastery-threshold-transfer-test-design](../03-assessment-science/mastery-threshold-transfer-test-design.md) for the cut-score logic that requires extra distractor scrutiny on near-cut items.
