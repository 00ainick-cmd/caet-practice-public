---
id: pre-post-assessment-effect-size
title: Pre/Post Assessment & Effect Size
category: 03-assessment-science
aliases: [effect-size-measurement, pretest-posttest-effect-size]
evidence_strength: strong
effect_size: "Cohen's d benchmarks: 0.2 small, 0.5 medium, 0.8 large (Cohen 1988); educational interventions average d ≈ 0.40 across 800+ meta-analyses (Hattie 2009); empirical benchmarks for education (Kraft 2020) recommend smaller cuts (<0.05 small, 0.05–0.20 medium, >0.20 large) for causal studies on standardized achievement"
key_sources:
  - "Cohen, J. (1988). Statistical power analysis for the behavioral sciences (2nd ed.). Hillsdale, NJ: Lawrence Erlbaum. doi:10.4324/9780203771587"
  - "Hattie, J. (2009). Visible learning: A synthesis of over 800 meta-analyses relating to achievement. London: Routledge. doi:10.4324/9780203887332"
  - "Morris, S. B., & DeShon, R. P. (2002). Combining effect size estimates in meta-analysis with repeated measures and independent-groups designs. Psychological Methods, 7(1), 105-125. doi:10.1037/1082-989X.7.1.105"
  - "Lakens, D. (2013). Calculating and reporting effect sizes to facilitate cumulative science: A practical primer for t-tests and ANOVAs. Frontiers in Psychology, 4, 863. doi:10.3389/fpsyg.2013.00863"
  - "Kraft, M. A. (2020). Interpreting effect sizes of education interventions. Educational Researcher, 49(4), 241-253. doi:10.3102/0013189X20912798"
  - "Bloom, H. S., Hill, C. J., Black, A. R., & Lipsey, M. W. (2008). Performance trajectories and performance gaps as achievement effect-size benchmarks for educational interventions. Journal of Research on Educational Effectiveness, 1(4), 289-328. doi:10.1080/19345740802400072"
  - "Cumming, G. (2014). The new statistics: Why and how. Psychological Science, 25(1), 7-29. doi:10.1177/0956797613504966"
last_reviewed: 2026-04-29
applies_to: [measurement]
contraindicated_when:
  - learner_state.first_exposure
  - material.high_element_interactivity_no_scaffolding
  - task_type.motor_acquisition
runtime_triggers:
  - segment_started
  - segment_completed
  - module_completed
  - delayed_review_window_open
  - tutor_strategy_changed
related: [testing-effect, pretesting-effect, validity-reliability, item-difficulty-discrimination, mastery-thresholds, mastery-threshold-transfer-test-design, transfer-of-learning]
---

# Pre/Post Assessment & Effect Size

## One-line claim

Measure learning by giving the same parallel assessment before and after instruction, then express the change as a standardized effect size so the magnitude of learning is comparable across learners, segments, and tutor strategies.

## Evidence base

The pre/post design is the simplest credible measurement of whether instruction produced learning, and the standardized mean difference — Cohen's *d*, or its bias-corrected sibling Hedges' *g* — is the metric that lets results be compared across instruments, scales, and populations. Cohen (1988) defined the small/medium/large benchmarks (*d* = 0.2, 0.5, 0.8) as a default vocabulary for interpreting effects in the absence of domain-specific data, while explicitly cautioning that the labels were relative and that field-specific benchmarks should take precedence when available. Morris and DeShon (2002) is the load-bearing methodological paper for pre/post designs specifically: they showed that the appropriate effect size for a single-group pretest–posttest comparison is the mean change divided by the *pretest* standard deviation, that variance estimation differs from the independent-groups case (correlated pre–post scores reduce the sampling variance), and that combining repeated-measures and independent-groups designs in the same meta-analysis requires design-specific variance formulas. Lakens (2013) operationalizes both formulations with worked examples and is the practical reference an AI tutor's analytics layer should consult when computing *d* from raw scores.

The interpretation problem is sharper than the computation problem. Hattie's (2009) synthesis of more than 800 meta-analyses placed the average effect of educational influences at *d* ≈ 0.40 — the "hinge point" — and argued that interventions below this benchmark are below the typical effect of being in school for a year. Bloom, Hill, Black, and Lipsey (2008) sharpened the picture by computing typical annual achievement gains from nationally standardized tests and showing they decline from roughly *d* = 1.0 in early elementary grades to *d* < 0.30 in high school. Kraft (2020) applied a similar empirical lens to causal evaluations of education interventions and proposed revised benchmarks for that class of study (*d* < 0.05 small, 0.05–0.20 medium, > 0.20 large), arguing Cohen's defaults systematically overstate what counts as a meaningful intervention effect once cost and scalability are considered. The operational implication for an AI tutor: do not interpret a within-segment *d* of 0.5 as automatically "medium" — it is large for a 20-minute lesson and modest for a year-long curriculum. Always compare against an in-domain benchmark.

The principal threats to a pre/post effect size are baseline-dependent: regression to the mean inflates apparent gains for low pretest scores, ceiling effects suppress them for high pretest scores, and pretest exposure can itself produce measurable learning (the pretesting effect — see [pretesting-effect](../01-learning-science/pretesting-effect.md)). Cumming (2014) argued in *Psychological Science* that point estimates without confidence intervals are misleading at small *n*, and that a 95% CI around an effect size captures the replication effect with roughly 83% probability — a useful uncertainty floor for any single-learner measurement, where *n* = 1 means the CI is wide. The standard mitigations are parallel forms (different items, same blueprint), counterbalanced anchor items between pre and post to monitor drift, and reporting the effect size *with* its confidence interval rather than as a single number.

## When to apply

- **Segment started / pre-assessment check-in** — Administer a short pretest at the start of
  any segment whose mastery the tutor will later claim. The pretest establishes the baseline
  for the effect-size calculation and surfaces prerequisite gaps before instruction begins.
- **Segment completed** — Within minutes of finishing instruction on a discrete segment,
  administer a parallel posttest covering the same blueprint. Compute the within-learner
  standardized change immediately so the segment's evidentiary record is closed.
- **Module completed** — At the close of a multi-segment module, run a longer parallel-form
  posttest aligned to module objectives and compute *d* against the corresponding pretest.
  Module-level effects are the level at which curriculum decisions get made.
- **Delayed review window opens** — Re-administer a parallel form at +7 to +30 days to
  measure *retained* learning, not initial acquisition. Retention *d* is the operational
  target; immediate *d* alone overstates durable learning.
- **Tutor strategy changed** — When the tutor switches a delivery strategy (e.g., worked
  examples → retrieval practice, or massed → spaced), the pre/post effect size on the next
  comparable segment is the primary signal of whether the change helped.

## When NOT to apply

- **First exposure to dense, high-element-interactivity material** — A pretest on content the
  learner has had no chance to encode produces floor scores that exaggerate post-pre gains
  and reflect ignorance, not learning. Build the schema first; measure on the second exposure.
- **High-element-interactivity material with no scaffolding** — When pretest items require
  integrating many novel elements simultaneously, scores cluster near zero with high variance
  and the effect-size estimate is unstable. Decompose to lower-element-interactivity items
  or wait for scaffolding to be in place.
- **Pure motor-skill acquisition phases** — Written pre/post designs do not capture the
  dimensions of motor performance that matter (smoothness, timing, force calibration). Use
  rubric-based observation of the task itself; pre/post is appropriate for the declarative
  knowledge embedded in the procedure, not the execution.
- **Identical instrument used at pre and post** — Repeating the same items conflates learning
  with memory of the test. Use parallel forms drawn from the same blueprint, or item-level
  randomization that prevents recall of specific items from inflating the gain.
- **Single-item or very-short assessments** — A 3-item pretest produces a pre–post change
  with a CI that spans most plausible effect sizes. *d* becomes uninterpretable below ~8–10
  items per construct (compounding with single-learner *n* = 1).

## How to apply

- **Build pre and post from one blueprint, two parallel forms** — Specify objectives and item
  difficulty targets (see
  [item-difficulty-discrimination](../07-runtime-decisions/item-difficulty-discrimination.md))
  once; randomly draw two non-overlapping forms of equal length, with 1–2 anchor items common
  to both to monitor instrument drift.
- **Compute the standardized change correctly** — For a single learner on the same form-
  equivalent test, use *d* = (M_post − M_pre) / SD_pretest (Morris & DeShon, 2002). With a
  comparison condition, use the difference-in-differences variant. Lakens (2013) gives the
  formulas; do not invent.
- **Report a confidence interval, not a point estimate** — Cumming (2014) is explicit that
  single-point effect sizes mislead at small samples. Bootstrap a learner-level CI from item
  scores or use the closed-form CI for *d*; treat the lower bound, not the mean, as the
  action-relevant number.
- **Compare against an in-domain benchmark, not Cohen's defaults** — A within-segment *d*
  must be compared to typical *d* for similarly-sized segments in the same domain (see
  [transfer-of-learning](../01-learning-science/transfer-of-learning.md) for far-vs-near
  distinctions). Bloom et al. (2008) and Kraft (2020) both argue Cohen's labels are inflated
  for education.
- **Mitigate regression-to-the-mean and ceiling effects explicitly** — Flag pretests below
  20% or above 80% as unreliable baselines; the SD compresses at the extremes and the gain
  is partly statistical artifact. Above 80% pretest the segment was likely already mastered
  (see [mastery-thresholds](../07-runtime-decisions/mastery-thresholds.md)) — switch to a
  transfer test rather than a recall post.
- **Plan a delayed retention probe at the same time as the post** — Schedule a parallel-form
  posttest at +7 days the moment the immediate post is recorded. Retention *d* is the
  operational mastery signal; immediate-post *d* is encoding. This is also where retrieval
  practice (see [testing-effect](../01-learning-science/testing-effect.md)) shows its largest
  measurable gains.

## Common misapplications

- **Treating Cohen's labels as universal** — *d* = 0.30 is "small" by Cohen and "above the
  education-research median" by Kraft (2020). The same number means different things in
  different contexts; reporting "small effect" without the comparison class is the most
  common misuse.
- **Reusing pretest items as posttest items** — Memory for the items inflates the apparent
  effect; the pretesting literature confirms even unanswered exposure produces measurable
  later gains. Always parallel-form, drawn from a calibrated bank.
- **Reporting *d* without sample size or CI** — *d* = 0.8 from *n* = 4 has a 95% CI of roughly
  (−0.3, 1.9). Without the CI the number cannot drive a decision (Cumming, 2014). For
  single-learner analytics the CI is always wide; report it anyway and act conservatively.
- **Confusing pretest-as-baseline with pretesting-effect** — A diagnostic pretest establishes
  a measurement baseline; a learning-oriented pretest is an instructional move (see
  [pretesting-effect](../01-learning-science/pretesting-effect.md)). Mixing the roles
  invalidates the measurement — learning from the pretest is mis-attributed to instruction.
- **Using single-group pre/post to claim instruction caused the gain** — Without a counter-
  factual, the gain may reflect maturation, repeated exposure, or the pretesting effect.
  For causal claims, use a comparison condition or stagger instruction across segments.

## Examples across domains

**Avionics — TDR-94D Mode S transponder fault-isolation segment (technician training).**

*Setup.* The technician completes a 25-minute lesson on diagnosing intermittent Mode S replies
on a TDR-94D transponder using a ramp tester. A 12-item parallel-form bank covers four
diagnostic concepts (interrogation–reply timing, antenna VSWR symptoms, encoder bus faults,
squitter-rate anomalies); each pre/post draws 6 non-overlapping items at matched difficulty
(target *p* = 0.55, point-biserial > 0.30 from prior calibration).

*Application.* Pretest *M* = 2.1/6, posttest *M* = 4.7/6, pretest SD = 1.1.
*d* = (4.7 − 2.1) / 1.1 = 2.4 — a very large within-segment effect. The analytics layer flags
the pretest (35%) as inside the reliable-baseline window (20–80%), bootstraps a 95% CI of
[1.6, 3.1], and compares against the in-domain benchmark for similarly-sized avionics
segments (typically *d* ≈ 0.7–1.2). The effect is above the in-domain large band; the tutor
records the segment as evidentially mastered and schedules a +7-day retention probe.

*Follow-up.* At +7 days, the technician scores 3.9/6 on a third parallel form. Retention
*d* = (3.9 − 2.1) / 1.1 = 1.6 — still in the in-domain large band, confirming durable
learning. Had retention fallen below the instruction-level benchmark (~0.7), the tutor would
surface a remediation segment and repeat the cycle.

**Emergency medicine resident training — pediatric anaphylaxis recognition and IM epinephrine
dosing.**

*Setup.* A second-year emergency medicine resident completes a 30-minute simulator-based
module on pediatric anaphylaxis: recognition criteria, weight-based IM epinephrine dosing
(0.01 mg/kg, max 0.5 mg), airway adjuncts, and disposition. A 10-item parallel-form bank
built from the program's mastery blueprint draws two 5-item forms with matched difficulty;
pretest before the scenario, posttest immediately after the debrief.

*Application.* Pretest *M* = 1/5, posttest *M* = 4/5, pretest SD across the cohort = 0.9.
*d* = (4 − 1) / 0.9 = 3.3. The program's benchmark for high-acuity recognition modules is
*d* ≈ 1.0–2.0 immediate-post (residents bring substantial prior knowledge, so SDs are larger
and standardized gains smaller than in novice populations). The resident's effect is above
benchmark; the tutor logs the segment as evidentially mastered.

*Follow-up.* At +30 days the resident takes a third parallel form interleaved with two
distractor cases (acute asthma exacerbation, septic shock) to test whether anaphylaxis
recognition transfers under realistic case-mix pressure (see
[transfer-of-learning](../01-learning-science/transfer-of-learning.md) for why interleaved
post-tests are the higher-validity transfer probe). Retention *d* = 1.8. Because high-stakes
clinical recognition decays faster under interference than the simulator suggests, the tutor
schedules a second probe at +90 days before any program-level mastery claim.

## Quality signal

The pre/post measurement system is working when (a) within-learner immediate-post *d* exceeds the in-domain segment benchmark with a 95% CI whose lower bound is also above the next-lower benchmark band, and (b) the +7-day retention *d* retains at least 60% of the immediate-post *d* — a drop below this threshold indicates encoding-without-consolidation and the tutor should add spaced retrieval before declaring the segment mastered. Failure mode: pretest scores chronically below 20% or above 80%, which signals the assessment is mis-targeted (too hard, too easy, or wrong blueprint) before any effect-size interpretation is meaningful.

## Cross-references

- See [validity-reliability](../03-assessment-science/validity-reliability.md) for the
  prerequisite measurement properties — an effect size built on an unreliable instrument
  is uninterpretable regardless of *d*.
- See [item-difficulty-discrimination](../07-runtime-decisions/item-difficulty-discrimination.md)
  for how to calibrate the items that go into the pre/post parallel forms.
- See [mastery-thresholds](../07-runtime-decisions/mastery-thresholds.md) for converting
  posttest scores into advance/remediate decisions once *d* is computed.
- See [mastery-threshold-transfer-test-design](../03-assessment-science/mastery-threshold-transfer-test-design.md)
  for when to escalate from a recall posttest to a transfer posttest at the segment boundary.
- See [pretesting-effect](../01-learning-science/pretesting-effect.md) for the distinction
  between pretest-as-measurement and pretest-as-instruction, and how the latter contaminates
  the former.
- See [testing-effect](../01-learning-science/testing-effect.md) for why +7-day retention is
  the operational mastery signal rather than the immediate post.
- See [transfer-of-learning](../01-learning-science/transfer-of-learning.md) for why
  interleaved or context-shifted posttests are the higher-validity transfer probe.
