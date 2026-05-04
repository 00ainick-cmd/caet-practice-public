---
id: performance-factor-analysis
title: Performance Factor Analysis
category: 07-runtime-decisions
aliases: [pfa, performance-factors-analysis]
evidence_strength: strong
effect_size: null  # Logistic-regression student model — PFA is a parameter-estimation framework, not a single intervention. Magnitudes appear instead in head-to-head predictive-accuracy comparisons against BKT (e.g., Pavlik et al. 2009: AIC/BIC favor PFA on the AlgebraI dataset; Gong, Beck & Heffernan 2011: PFA AUC ≈ 0.73 vs. KT+EM ≈ 0.71 on ASSISTments) which are reported in context.
key_sources:
  - "Pavlik, P. I., Cen, H., & Koedinger, K. R. (2009). Performance factors analysis - A new alternative to knowledge tracing. In V. Dimitrova, R. Mizoguchi, B. du Boulay, & A. Graesser (Eds.), Proceedings of the 14th International Conference on Artificial Intelligence in Education (pp. 531-538). Amsterdam: IOS Press."
  - "Corbett, A. T., & Anderson, J. R. (1995). Knowledge tracing: Modeling the acquisition of procedural knowledge. User Modeling and User-Adapted Interaction, 4(4), 253-278. doi:10.1007/BF01099821"
  - "Cen, H., Koedinger, K. R., & Junker, B. (2006). Learning factors analysis - A general method for cognitive model evaluation and improvement. In M. Ikeda, K. Ashley, & T.-W. Chan (Eds.), Intelligent Tutoring Systems (pp. 164-175). Berlin: Springer. doi:10.1007/11774303_17"
  - "Gong, Y., Beck, J. E., & Heffernan, N. T. (2011). How to construct more accurate student models: Comparing and optimizing knowledge tracing and performance factor analysis. International Journal of Artificial Intelligence in Education, 21(1-2), 27-46. doi:10.3233/JAI-2011-016"
  - "Pavlik, P. I., & Anderson, J. R. (2008). Using a model to compute the optimal schedule of practice. Journal of Experimental Psychology: Applied, 14(2), 101-117. doi:10.1037/1076-898X.14.2.101"
  - "Khajah, M., Lindsey, R. V., & Mozer, M. C. (2016). How deep is knowledge tracing? In T. Barnes, M. Chi, & M. Feng (Eds.), Proceedings of the 9th International Conference on Educational Data Mining (pp. 94-101). Raleigh, NC: International Educational Data Mining Society."
  - "Pelánek, R. (2017). Bayesian knowledge tracing, logistic models, and beyond: An overview of learner modeling techniques. User Modeling and User-Adapted Interaction, 27(3-5), 313-350. doi:10.1007/s11257-017-9193-2"
last_reviewed: 2026-04-30
applies_to: [measurement, sequencing, decision]
contraindicated_when:
  - material.uncalibrated_item_pool
  - learner_state.first_exposure
  - task_type.motor_acquisition
  - material.high_element_interactivity_no_scaffolding
runtime_triggers:
  - response_logged
  - mastery_estimate_due
  - next_item_selection_due
  - kc_difficulty_recalibration_due
  - mastery_decision_pending
related: [bayesian-knowledge-tracing, item-difficulty-discrimination, mastery-thresholds, schema-theory-knowledge-components, knowledge-graph-traversal, sm2-fsrs, spaced-retrieval]
---

# Performance Factor Analysis

## One-line claim

Estimate the learner's probability of correct response on the next item by counting prior successes and failures on the relevant knowledge components and feeding those counts — not a hidden mastery state — into a logistic regression with per-KC difficulty and per-success/per-failure learning-rate parameters.

## Evidence base

Performance Factor Analysis (PFA), introduced by Pavlik, Cen, and Koedinger (2009) in the *Proceedings of the 14th International Conference on Artificial Intelligence in Education*, models the probability that a learner will answer the next item correctly as a logistic function of three terms summed over the knowledge components (KCs) the item exercises: a per-KC difficulty intercept `β_j`, a learning-rate coefficient `γ_j` multiplied by prior successes `s_ij`, and a coefficient `ρ_j` multiplied by prior failures `f_ij`. The full equation is `m = Σ_j (β_j + γ_j · s_ij + ρ_j · f_ij)` and `P(correct) = 1 / (1 + exp(-m))`. Unlike Bayesian Knowledge Tracing (Corbett & Anderson, 1995), which models a hidden binary mastery state with learn/guess/slip parameters, PFA carries no hidden state — only observable success and failure counts and a learned KC difficulty. Pavlik, Cen, and Koedinger (2009) showed on the LearnLab AlgebraI dataset that PFA fit better than three competing models (LFA, LFA+student, BKT) by AIC/BIC, attributing the gap primarily to PFA's separable success/failure coefficients, which absorb the asymmetric information in correct versus incorrect responses that BKT's single learn-rate parameter cannot.

Independent replication has confirmed the head-to-head predictive advantage. Gong, Beck, and Heffernan (2011), reporting in the *International Journal of Artificial Intelligence in Education* on the ASSISTments middle-school math dataset, found PFA produced higher predictive accuracy (AUC ≈ 0.73) than expectation-maximization-fit BKT (AUC ≈ 0.71), with PFA parameter estimates judged more interpretable by domain experts. Khajah, Lindsey, and Mozer (2016), responding at the 9th International Conference on Educational Data Mining to the deep-knowledge-tracing claim of large neural-network gains over BKT, demonstrated that the apparent gap closes once BKT is extended with the regularities PFA already captures (item-level difficulty, separate response-correctness signals, recency). Pelánek's (2017) review in *User Modeling and User-Adapted Interaction* placed PFA and its variants alongside BKT as the two canonical baselines; on most public datasets the two are within a few AUC points, with PFA winning on rich item-level data and BKT winning on sparse-per-KC data.

The framework rests on the same Q-matrix infrastructure as the Learning Factors Analysis precursor (Cen, Koedinger, & Junker, 2006), which maps each item to one or more KCs and must be calibrated before PFA's `β`, `γ`, `ρ` parameters can be estimated. PFA inherits LFA's boundary conditions: stable parameter estimates require hundreds of responses per KC, and a misspecified Q-matrix degrades both fit and the runtime decisions built on top of it. PFA also ignores inter-trial spacing — counts are unweighted by time — which means it underestimates forgetting on long delays. The Pavlik and Anderson (2008) activation-based model in *Journal of Experimental Psychology: Applied* captures spacing and is the lineage feeding the PFA-decay variant and downstream FSRS-style schedulers. The runtime treats PFA as the per-KC mastery estimator and pairs it with a separate spacing scheduler when long retention matters.

## When to apply

- **Response just logged on a KC-tagged item** — Update the relevant KCs' success or failure
  count, recompute `m` and `P(correct)` for the candidate next items. This is the per-response
  inner loop of any PFA-driven runtime.
- **Mastery estimate due before a sequencing decision** — When the runtime needs a per-KC
  mastery estimate to decide whether to advance, remediate, or interleave, compute `P(correct)`
  for a hypothetical canonical item on each KC and use that probability as the mastery proxy.
- **Next-item selection is due** — Rank candidate items by the expected information gain about
  the underrepresented or weakest KCs given the current `s` and `f` counts; prefer items whose
  predicted `P(correct)` is in the productive-difficulty band (roughly 0.5–0.85 depending on the
  domain's tolerance for failure; see [item-difficulty-discrimination](../07-runtime-decisions/item-difficulty-discrimination.md)).
- **KC difficulty recalibration window** — When enough new responses have accumulated (e.g.,
  weekly batch on the cohort), refit `β`, `γ`, `ρ` to absorb item-pool drift and curriculum
  edits. Carry the prior posterior as a regularization anchor so per-KC counts stay comparable
  across recalibrations.
- **Mastery decision pending and the prior model is BKT** — If the runtime's incumbent estimator
  is BKT and decisions disagree with observed performance (high posterior mastery but recent
  failures, or vice versa), PFA's separable success/failure coefficients usually resolve the
  discrepancy with fewer free parameters (Gong, Beck, & Heffernan, 2011).
- **Item-level difficulty is rich and per-KC sample is large** — PFA's relative advantage over
  BKT grows with per-item difficulty variance and per-KC sample size (Pelánek, 2017). When the
  Q-matrix has many items per KC and items vary substantially in difficulty, prefer PFA.

## When NOT to apply

- **Knowledge components are not yet specified or the Q-matrix is uncalibrated** — Without a
  KC tagging on every item and at least a tentative Q-matrix, the success/failure counts have
  nothing to attach to. Calibrate the cognitive model first (Cen, Koedinger, & Junker, 2006);
  do not run PFA on uncoded items.
- **Per-KC sample size is too small to fit `β`, `γ`, `ρ` stably** — With fewer than ~100
  responses per KC, the three parameters are mostly noise and the runtime will adapt against
  that noise. Hold the model at population priors or fall back to simpler proportion-correct
  heuristics (Pelánek, 2017).
- **Learner is in the first-exposure encoding phase of a high-element-interactivity concept** —
  Estimating mastery via response counts assumes the learner has at least begun to build the
  schema. While the schema is still forming, the runtime's job is worked-example scaffolding
  ([cognitive-load-theory](../01-learning-science/cognitive-load-theory.md)), not mastery
  probing.
- **Pure motor skill acquisition** — PFA scores binary or polytomous responses on
  conceptually-tagged items. Procedural motor execution does not reduce to that signal during
  encoding; verbal-conceptual companion items can be PFA-tracked, the motor execution itself
  cannot.
- **Long retention intervals dominate the use case and no spacing extension is layered on** —
  Vanilla PFA ignores time between trials and therefore underestimates forgetting on
  multi-week delays. For long-delay retention, extend with a spacing-aware variant
  (PFA-decay, FSRS) or pair PFA with a separate scheduler ([sm2-fsrs](../07-runtime-decisions/sm2-fsrs.md)).

## How to apply

- **Tag every item with one or more KCs in a calibrated Q-matrix** — Use the Q-matrix from the
  domain pack (see [schema-theory-knowledge-components](../01-learning-science/schema-theory-knowledge-components.md))
  and refine it against item-fit statistics (Cen, Koedinger, & Junker, 2006) before fitting PFA.
- **Fit `β`, `γ`, `ρ` with logistic regression on the calibration response log** — The canonical
  PFA in Pavlik, Cen, and Koedinger (2009) deliberately omits a per-student difficulty term to
  keep KC-level learning claims crisp. Expect `γ > ρ ≥ 0` for most KCs but allow the
  coefficients to take their fitted signs.
- **Update success and failure counts incrementally on each scored response** — On correct,
  increment `s_ij` for every KC `j` tagged on item `i`; on incorrect, increment `f_ij`. Cap
  counts only if the runtime explicitly models forgetting via a recency-weighted variant.
- **Use `P(correct)` as a mastery proxy, not a calibrated probability** — Predicted probability
  is well-ordered but its absolute calibration drifts as the item pool changes. Set thresholds
  against held-out validation accuracy, not a fixed cutoff (see [mastery-thresholds](../07-runtime-decisions/mastery-thresholds.md)).
- **Choose the next item to maximize expected information gain on weak KCs** — Rank candidates
  by low current `P(correct)` on KCs the learner needs and by item discrimination when
  available. Skip items already above `P ≈ 0.95` — they add no information.
- **Pair PFA with a spacing scheduler when long-delay retention matters** — Vanilla PFA does
  not model forgetting; pass mastery estimates to ([sm2-fsrs](../07-runtime-decisions/sm2-fsrs.md))
  for cross-session timing.
- **Recalibrate KC difficulty on a fixed cadence as the item pool grows** — Refit `β`, `γ`, `ρ`
  on the rolling response log (e.g., weekly), holding prior estimates as a regularization anchor.

## Common misapplications

- **Treating `P(correct)` as a calibrated probability across runtimes** — PFA's predicted
  probabilities are well-ordered within a fitted model but drift across recalibrations and
  curricula. Use them as a relative ranking, not as a population-stable percentage (Pelánek,
  2017).
- **Skipping the Q-matrix or using a too-coarse one** — A single "algebra" KC tag on every item
  collapses the model's resolution and makes `γ` and `ρ` meaningless. PFA's claims rest on the
  KC tagging being granular enough that within-KC items genuinely transfer (Cen, Koedinger, &
  Junker, 2006).
- **Including a per-student difficulty parameter without enough data** — Pavlik, Cen, and
  Koedinger (2009) deliberately omitted per-student terms; adding one without thousands of
  responses per learner consumes degrees of freedom that should go to KC parameters.
- **Ignoring spacing and using PFA as a long-delay retention model** — Vanilla PFA's
  unweighted counts mean a success three months ago counts the same as a success yesterday.
  For retention horizons beyond a few sessions, extend with PFA-decay or hand off to a
  spacing scheduler (Pavlik & Anderson, 2008; [sm2-fsrs](../07-runtime-decisions/sm2-fsrs.md)).
- **Comparing PFA to BKT on AUC alone** — Differences of 0.01–0.02 are common and
  dataset-dependent. Triangulate with calibration plots, residual analysis, and downstream
  decision quality (Gong, Beck, & Heffernan, 2011; Khajah, Lindsey, & Mozer, 2016).
- **Letting failure counts grow unboundedly on a learner who has clearly mastered the KC** —
  After saturation, successes barely move `P(correct)` but rare failures still register. Cap
  counts or switch to a recency-weighted variant once `P(correct) > 0.95`.

## Examples across domains

**Avionics — adaptive practice for a Garmin GTN 750 navigator installation course.**

*Setup.* The shop's platform tags its 320-item GTN 750 bank against a 36-KC Q-matrix
covering pinout interpretation, configuration menus, antenna isolation, RAIM rules, and
post-install verification. PFA fit on ~2,400 prior technicians: typical `β_j` ≈ −1.2,
`γ_j` ≈ 0.45, `ρ_j` ≈ 0.18. A new technician has 3 successes and 1 failure on "DME hold
input wiring".

*Estimation and selection.* `m = −1.2 + 0.45·3 + 0.18·1 = 0.33`, `P(correct) ≈ 0.58`.
The runtime ranks candidates: a "DME hold input" item predicts 0.58 (productive), an
"RS-232 baud-rate setting" item predicts 0.42 (weaker KC — higher information), a
"front-panel labeling" item predicts 0.93 (skip — saturated). The runtime serves RS-232.
Wrong; `f` increments, `P(correct)` for that KC drops to 0.36 and next-item ranking
re-prioritizes it.

*Decision and handoff.* The mastery cut to advance to the practical install rubric is
`P(correct) ≥ 0.85` per KC, calibrated against held-out accuracy. After 38 items, 32 of
36 KCs clear cut. The four below — RS-232, side-by-side antenna isolation, RAIM edge
cases, CAN-bus termination — get one more practice block, then mastery estimates hand
off to the cross-session scheduler
([sm2-fsrs](../07-runtime-decisions/sm2-fsrs.md)) for spaced review before the exam.

**Mortgage / financial services sales — adaptive product-knowledge and compliance practice for new loan officers.**

*Setup.* A regional lender's platform tags 280 items against a 22-KC Q-matrix:
conventional/FHA/VA eligibility, debt-to-income, ATR/QM triggers, RESPA disclosure
timing, TRID redisclosure windows, lock-extension policy. PFA fit on ~1,100 prior
cohorts: `β_j` from −2.0 (rare TRID edges) to −0.4 (common DTI math); `γ_j` averages
0.50, `ρ_j` averages 0.22. A new loan officer has 6 successes and 2 failures on "ATR/QM
ability-to-repay verification".

*Estimation and selection.* `m = −1.1 + 0.50·6 + 0.22·2 = 2.34`, `P(correct) ≈ 0.91` —
saturating; PFA stops prioritizing this KC. The runtime routes to "TRID redisclosure
window" (`P ≈ 0.45`) and "VA funding-fee exemption" (`P ≈ 0.38`), the two weakest. A
wrong TRID answer drops `P` to 0.31; the runtime treats `P < 0.35` as a signal to step
out of practice into scaffolded reteach before continuing.

*Decision and handoff.* The compliance team's licensure-readiness cut is `P(correct) ≥
0.88` on every KC, calibrated against NMLS state-exam pass rate. The runtime advances
the officer to live-pipeline shadowing only when all 22 KCs clear cut, then persists
estimates into a weekly spaced-review queue
([spaced-retrieval](../01-learning-science/spaced-retrieval.md)) so newly-mastered KCs
do not decay before the licensure exam.

## Quality signal

PFA is producing useful runtime decisions when (a) on held-out responses, the model's predicted `P(correct)` is well-calibrated within ±0.05 across the 0.3–0.9 band and AUC is at least 0.70 — Gong, Beck, & Heffernan (2011) report ~0.73 on ASSISTments as a typical operational benchmark; and (b) downstream mastery-decisions made against PFA cut scores produce ≤ 10% reversal rate when re-tested 1–2 weeks later (lower than the BKT incumbent on the same data). A faster within-session signal: per-response `P(correct)` updates should move monotonically in the right direction (up after success, down after failure on the same KC). Erratic flips after single responses indicate underfit `γ` or `ρ`, often from too small a per-KC calibration sample.

## Cross-references

- See [bayesian-knowledge-tracing](../07-runtime-decisions/bayesian-knowledge-tracing.md) for the hidden-state Bayesian alternative PFA is positioned against; runtimes often run both and reconcile disagreements.
- See [item-difficulty-discrimination](../07-runtime-decisions/item-difficulty-discrimination.md) for the IRT-based item-selection logic that complements PFA's per-KC mastery estimates at the item level.
- See [mastery-thresholds](../07-runtime-decisions/mastery-thresholds.md) for the cut-score logic that turns PFA's `P(correct)` into pass/fail decisions.
- See [schema-theory-knowledge-components](../01-learning-science/schema-theory-knowledge-components.md) for the KC tagging and Q-matrix infrastructure PFA depends on.
- See [knowledge-graph-traversal](../07-runtime-decisions/knowledge-graph-traversal.md) for the prerequisite-graph constraints that scope which KCs PFA should be probing at any given moment.
- See [sm2-fsrs](../07-runtime-decisions/sm2-fsrs.md) for the spacing schedulers PFA hands off to when long-delay retention matters; vanilla PFA does not model forgetting.
- See [spaced-retrieval](../01-learning-science/spaced-retrieval.md) for the underlying learning-science principle that motivates the spacing handoff.
