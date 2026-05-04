---
id: validity-reliability
title: Validity & Reliability
category: 03-assessment-science
aliases: [psychometric-validity, test-reliability]
evidence_strength: strong
# effect_size is null because validity & reliability is the foundational psychometric
# framework against which assessments are evaluated, not a single intervention with a
# d/g estimate. Specific reliability coefficients (alpha, omega) and validity-evidence
# magnitudes are reported per-instrument in the literature; the framework itself sets
# the criteria the runtime must meet, not an effect to be produced.
effect_size: null
key_sources:
  - "Cronbach, L. J. (1951). Coefficient alpha and the internal structure of tests. Psychometrika, 16(3), 297-334. doi:10.1007/BF02310555"
  - "Messick, S. (1989). Validity. In R. L. Linn (Ed.), Educational measurement (3rd ed., pp. 13-103). New York: American Council on Education and Macmillan."
  - "Kane, M. T. (2013). Validating the interpretations and uses of test scores. Journal of Educational Measurement, 50(1), 1-73. doi:10.1111/jedm.12000"
  - "American Educational Research Association, American Psychological Association, & National Council on Measurement in Education. (2014). Standards for educational and psychological testing. Washington, DC: American Educational Research Association."
  - "Sijtsma, K. (2009). On the use, the misuse, and the very limited usefulness of Cronbach's alpha. Psychometrika, 74(1), 107-120. doi:10.1007/s11336-008-9101-0"
  - "Cizek, G. J. (2012). Defining and distinguishing validity: Interpretations of score meaning and justifications of test use. Psychological Methods, 17(1), 31-43. doi:10.1037/a0026975"
  - "McDonald, R. P. (1999). Test theory: A unified treatment. Mahwah, NJ: Lawrence Erlbaum Associates."
last_reviewed: 2026-04-29
applies_to: [measurement, decision]
contraindicated_when:
  - material.high_element_interactivity_no_scaffolding
  - learner_state.first_exposure
  - task_type.motor_acquisition
runtime_triggers:
  - assessment_authored
  - mastery_decision_pending
  - score_interpretation_made
  - item_retired_or_replaced
  - cohort_data_window_closed
related: [item-writing-rules, distractor-analysis, item-difficulty-discrimination, mastery-thresholds, mastery-threshold-transfer-test-design, pre-post-assessment-effect-size, bloom-levels-in-assessment]
---

# Validity & Reliability

## One-line claim

A score is usable for a decision only when the evidence supports the specific interpretation being made (validity) and the score is reproducible enough that the decision would not flip on a different sitting, form, or rater (reliability); validity is a property of the inference, not the test.

## Evidence base

Modern validity theory descends from Messick's (1989) chapter in *Educational Measurement*, which rejected the older tripartite "content-criterion-construct" division and recast validity as a unitary construct: an "integrated evaluative judgment of the degree to which empirical evidence and theoretical rationales support the adequacy and appropriateness of inferences and actions based on test scores" (Messick, 1989, p. 13). The shift moved validity from a property of the *test* to a property of the *interpretation and use* of the test's scores — a test cannot be "valid" in the abstract, only valid for a specified inference made for a specified purpose with a specified population. Kane (2013) operationalized this in the *Journal of Educational Measurement* with the argument-based approach: an interpretation/use argument lays out the chain of inferences (scoring → generalization → extrapolation → decision) the score has to support, and validation is the systematic evaluation of each link's plausibility, with more-ambitious claims (high-stakes decisions, far-transfer extrapolations) requiring proportionally stronger evidence (Kane, 2013, pp. 7-12, on the four-inference chain). Cizek (2012) refined the framework further in *Psychological Methods*, distinguishing validation of *score meaning* from justification of *score use* — a useful operational split when the same score is being used to support multiple downstream decisions.

The contemporary professional standard is the *Standards for Educational and Psychological Testing* (AERA, APA, & NCME, 2014), which enumerates five sources of validity evidence the runtime can audit against: evidence from test content (do the items represent the construct's domain?), response processes (are examinees engaging the construct, not a surrogate strategy?), internal structure (do the items group as the construct predicts?), relations to other variables (does the score correlate with theoretically related criteria and diverge from unrelated ones?), and consequences of testing (do the score-based decisions produce the intended effects without unjustified adverse impact?). Reliability sits beneath these as a precondition: a score that is unstable across repeated administrations, parallel forms, or independent raters cannot anchor any interpretation, however well-argued. Cronbach's (1951) coefficient alpha in *Psychometrika* established the dominant internal-consistency estimator and remains the most-reported reliability statistic in educational measurement; it is the average of all possible split-half correlations and, under tau-equivalence, a lower bound on the score's reliability (Cronbach, 1951, pp. 299-303).

The principal modern qualification is on alpha itself. Sijtsma (2009) showed in *Psychometrika* that alpha is *not* a measure of internal consistency in any structural sense — it is unrelated to whether the items measure one factor or several — and is a lower bound on reliability that can be substantially below the true value when items violate tau-equivalence. McDonald's (1999) *Test Theory: A Unified Treatment* developed coefficient omega from a factor-analytic model that does not require tau-equivalence and typically yields higher, more accurate reliability estimates for realistic item sets. Operationally: report alpha for tradition and continuity, but treat omega (or stratified alpha for multidimensional instruments) as the defensible estimate when items are heterogeneous. For decisions that hinge on rater judgment — performance assessments, hands-on tasks, written constructed-response items — inter-rater reliability (Cohen's kappa for categorical, ICC for continuous) is the operative coefficient, and rater training plus calibration to anchor exemplars is the operative remediation.

## When to apply

- **Assessment authored** — Whenever the runtime adds, edits, or composes an assessment that will inform a decision (mastery, advancement, certification readiness), validity and reliability evidence must be established before the score is acted on. Authoring without this audit is the largest single source of bad downstream decisions.
- **Mastery decision pending** — Before declaring a learner has met a threshold, confirm the score the threshold is being applied to has reliability sufficient for that decision (≥ 0.80 for low-stakes formative; ≥ 0.90 for high-stakes summative or certification) and that the construct the decision presumes is the construct the score actually supports inferences about (see [mastery-thresholds](../07-runtime-decisions/mastery-thresholds.md)).
- **Score interpretation made** — Any time a score is being interpreted ("knows the topic", "ready for the field", "needs remediation"), name the specific inference and audit which of the five evidence sources support it. Scores travel further than the inference they were validated for; the runtime must check the match.
- **Item retired or replaced** — When an item is dropped (poor discrimination, compromised content) or a new item is added, the change is a validity event for the test as a whole, not just the item. Re-establish that the construct coverage and reliability still hold (see [distractor-analysis](../03-assessment-science/distractor-analysis.md), [item-difficulty-discrimination](../07-runtime-decisions/item-difficulty-discrimination.md)).
- **Cohort data window closed** — When enough learners have completed an instrument to estimate item statistics and reliability empirically, run the audit: omega/alpha for internal consistency, item-total correlations for discrimination, and where applicable a factor model for internal-structure evidence (AERA, APA, & NCME, 2014).
- **Cross-population deployment proposed** — Before reusing an instrument with a population it was not validated on (different role, prior background, language), require fresh evidence; validity does not transfer with the test.
- **Stakes-of-decision change** — A score originally validated for a low-stakes formative use (next-segment recommendation) cannot be recycled into a high-stakes use (certification gate) without a fresh validation appropriate to the new stakes. Stakes proportionality is a Kane (2013) requirement, not a courtesy.

## When NOT to apply

- **Learner is at first exposure to the construct being measured** — Formative checks during initial encoding are not "tests" in the inferential sense; their job is to surface confusion, not to anchor a decision. Insisting on full validation of every check produces analysis paralysis without protecting any decision (see [pretesting-effect](../01-learning-science/pretesting-effect.md) for the encoding-time use case).
- **Material is high-element-interactivity and the learner has no scaffolding** — A score on a complex integrated task during the schema-construction phase reflects load as much as competence; treat it as diagnostic, not as a decision input, until scaffolds have been faded ([cognitive-load-theory](../01-learning-science/cognitive-load-theory.md)).
- **Pure motor acquisition phase** — Reliability of self-report or paper-test items about a motor skill does not validate inferences about motor execution. Use direct observational rubrics with calibrated raters (an inter-rater reliability problem), not a written instrument standing in as a proxy.
- **n is too small to estimate the coefficient** — Reporting alpha or omega with fewer than ~50–100 examinees on the form yields confidence intervals so wide the point estimate is uninformative. Either accumulate data before reporting, or report with explicit interval and treat the score's stability cautiously in the interim.
- **Decision stakes do not warrant the burden** — Low-stakes formative feedback that simply tells the learner "review this" does not need the same validation rigor as a certification cut-score; calibrate the validation effort to the decision's stakes per Kane (2013).

## How to apply

- **Specify the interpretation/use argument first** — Write down the specific claim the score is meant to support ("the learner can perform task X to standard Y in context Z") before authoring items. The argument identifies which evidence sources are load-bearing; without it, the runtime is collecting evidence for an unspecified claim (Kane, 2013).
- **Audit content evidence at authoring time** — Map every item to a target objective, knowledge component, or PQS task; flag objectives without items and items without objectives. The mapping is the content-evidence artifact and is cheap to maintain at authoring time, expensive to reconstruct after the fact (see [item-writing-rules](../03-assessment-science/item-writing-rules.md)).
- **Compute reliability appropriate to the decision** — For a multi-item internal-consistency report on a unidimensional scale, use coefficient omega when item factor loadings are available and stratified alpha for multidimensional instruments; report Cronbach's alpha as the legacy companion (Sijtsma, 2009; McDonald, 1999). For test-retest or alternate-form decisions, use the matching coefficient, not a substitute.
- **Inter-rater reliability for performance tasks** — When the score depends on rater judgment, train raters against anchor exemplars, score a calibration sample double-blind, and require Cohen's kappa ≥ 0.70 (or ICC(2,1) ≥ 0.75 for continuous ratings) before raters score independently. Re-calibrate at least quarterly and after any rubric change.
- **Set decision thresholds with reliability in mind** — A cut-score sitting inside one standard error of measurement has a substantial probability of misclassifying. Either widen the band (a "needs review" zone), increase test length to shrink the SEM, or require a confirmatory second sitting before the decision is acted on (see [mastery-threshold-transfer-test-design](../03-assessment-science/mastery-threshold-transfer-test-design.md)).
- **Watch for consequential evidence** — Track whether score-based decisions produce the intended downstream effects (certification holders perform on the job; remediation triggered by low scores actually improves outcomes) and whether they produce unjustified adverse impact across subgroups (AERA, APA, & NCME, 2014). A score that "works" psychometrically but fails consequentially is not validated.
- **Re-validate when the population, content, or stakes change** — Validity is an ongoing argument, not a one-time certification. Treat any material change as a trigger to re-audit rather than to assume the prior evidence transfers.

## Common misapplications

- **Treating "valid" as a property of the test** — Tests are not valid; *interpretations and uses* are. A score validated for "ready to attempt the practical" is not automatically validated for "ready to be employed unsupervised" (Messick, 1989; Kane, 2013).
- **Reporting alpha and stopping** — Alpha can be high on a multidimensional instrument that no single decision should be made from, and low on a fine instrument that simply has heterogeneous items. Pair alpha with omega, item-total correlations, and a factor check rather than treating alpha alone as proof of reliability (Sijtsma, 2009).
- **Confusing reliability with validity** — A perfectly reliable score on the wrong construct supports the wrong decision precisely. Reliability is necessary but never sufficient; an instrument that measures consistently the wrong thing is the textbook validity failure.
- **Importing a cut-score from one population to another** — Cut-scores are validated against the population they were standardized on; deploying them on a different cohort (different prior experience, different instructional pathway) without re-validation is a validity failure dressed as continuity.
- **Treating high content-expert face validity as sufficient** — SME consensus that "this looks like the right test" is content evidence at best, and only when SMEs were sampled to represent the construct's domain rather than to confirm a draft. It is one source of evidence, not the audit.
- **Conflating "the test is biased" with "any subgroup difference is bias"** — Differential item functioning is evaluated against expected differences given the construct, not against equality of outcomes. A statistically significant subgroup difference may be valid; the audit is whether the difference reflects the construct or an irrelevant nuisance dimension (AERA, APA, & NCME, 2014).
- **Letting reliability estimates drift unmonitored** — A test that was reliable in 2022 may not be in 2026 if the curriculum, learner mix, or item pool has changed. Re-estimate on the current cohort rather than citing a historical coefficient.
- **Padding a short test to "raise alpha"** — Alpha rises mechanically with item count via the Spearman-Brown formula; a longer test of redundant items has higher alpha and no more information about the construct. Add items that cover under-represented sub-domains, not items that ask the same thing in a new wording.

## Examples across domains

**Avionics — recurrency knowledge check before an ADS-B Out installation.**

*Setup.* A shop deploys a 30-item knowledge check covering Mode S transponder behavior, ADS-B Out message structure, IFR-6000 ramp-test interpretation, and STC compliance documentation. The cut-score (24/30, 80%) is the gate to scheduling the technician on a paying ADS-B install. The interpretation/use argument is: "a 24+ score on this form supports the inference that the technician will execute the install and post-install verification to the standard required for FAA Part 91.227 compliance, on a King Air with this STC, supervised at the standard apprentice level."

*Validity move.* Content evidence is built from the AC 20-165B task list and the shop's installation procedure: every item maps to a specific procedural step or compliance criterion, and every step has at least two items. Internal-structure evidence comes from a factor check on the first 100 sittings showing the items load on three sub-skills (regulatory, procedure, ramp-test interpretation), so reliability is reported as stratified alpha (0.86) plus omega (0.88) rather than a single alpha. Consequential evidence is tracked: of technicians who scored 24+ and then performed an install in the next 90 days, 96% passed the post-install ramp test on the first attempt; of those scoring 22-23, 71%; of those below 22, 48%. The cut-score is supported by this gradient.

*Reliability and decision protection.* The standard error of measurement at the cut is ~1.4 items, so any score within 22-25 triggers a confirmatory second sitting on a parallel form rather than an immediate decision. When the FAA updates AC 20-165 (any revision), the content-evidence audit re-runs and the cohort data window opens fresh — historical reliability does not carry forward through a regulatory change. Inter-rater reliability is not the relevant coefficient here because the items are objectively scored; the rater issue arises in the post-install practical, where calibrated evaluators using a published rubric maintain ICC(2,1) ≥ 0.80 against an anchor sample, recertified quarterly.

**Mortgage / financial services sales — pre-licensing readiness assessment for residential loan officers.**

*Setup.* A national lender administers a 60-item internal readiness assessment to candidate loan officers two weeks before they sit the SAFE Act/NMLS national exam. The cut-score (45/60, 75%) determines whether the candidate is registered for the next NMLS testing window or routed back into a remediation block. The interpretation/use argument is: "a 45+ score on this form supports the inference that the candidate is likely (≥ 80%) to pass the NMLS national exam on the first attempt and is ready to begin supervised origination practice, in the lender's product mix, in the candidate's licensed states."

*Validity move.* Content evidence is built from the NMLS test specification (general mortgage knowledge, federal law, state-specific law, ethics, uniform state content) plus the lender's own product-mix coverage; every domain has at least eight items, and items are reviewed annually against the published NMLS content outline because the specification updates. Criterion evidence comes from the lender's longitudinal tracking: of candidates scoring 45+, the first-attempt NMLS pass rate is 84%; of candidates scoring 40-44, 58%; below 40, 31%. Internal-structure evidence (omega = 0.89 on the 2025 cohort, n = 612) supports the unidimensional readiness interpretation; the federal-law subscale is reported separately because its content domain is the most volatile under regulatory change.

*Reliability and decision protection.* The SEM at the cut is ~2 items; candidates scoring 43-47 receive a parallel-form retake within five days, and the decision is made on the higher of the two attempts only when the gap is ≤ 1 SEM (otherwise the candidate is routed to targeted remediation per [error-analysis-corrective-feedback](../04-delivery-patterns/error-analysis-corrective-feedback.md)). Consequential evidence is also audited at the supervisory level: candidates who passed the readiness assessment but later required compliance retraining within 12 months are a flag the score's "ready for supervised origination" inference is over-extending. State-specific content blocks are revalidated whenever a state's licensing curriculum changes, mirroring the AC-revision trigger in the avionics example.

## Quality signal

The runtime knows validity and reliability are being honored when (a) every score-based decision can be traced to an interpretation/use argument the audited evidence supports, (b) reliability for the operative decision sits at or above the conventional thresholds (≥ 0.80 formative, ≥ 0.90 summative; inter-rater κ ≥ 0.70 or ICC(2,1) ≥ 0.75 for performance tasks), and (c) consequential follow-up — downstream success on the criterion the score was supposed to predict — confirms the inference holds for the current cohort. Drift on any of the three is the operative alarm: a score with no corresponding argument, a coefficient sliding below threshold, or a flat or inverted relationship between scores and downstream outcomes.

## Cross-references

- See [item-writing-rules](../03-assessment-science/item-writing-rules.md) for the authoring-time discipline that protects content validity at the item level.
- See [distractor-analysis](../03-assessment-science/distractor-analysis.md) for the post-administration audit that surfaces malfunctioning items threatening reliability and content evidence.
- See [item-difficulty-discrimination](../07-runtime-decisions/item-difficulty-discrimination.md) for the item-level statistics that feed the reliability estimate and flag content gaps.
- See [mastery-thresholds](../07-runtime-decisions/mastery-thresholds.md) for the runtime rule that pairs cut-scores with reliability bands when classifying learners.
- See [mastery-threshold-transfer-test-design](../03-assessment-science/mastery-threshold-transfer-test-design.md) for the assessment design pattern that builds the criterion-related evidence supporting a "ready for the field" inference.
- See [pre-post-assessment-effect-size](../03-assessment-science/pre-post-assessment-effect-size.md) for the gain-score audit that depends on both forms being parallel and reliably scored.
- See [bloom-levels-in-assessment](../03-assessment-science/bloom-levels-in-assessment.md) for the alignment check that the items and the construct's intended cognitive level actually match.
- See [error-analysis-corrective-feedback](../04-delivery-patterns/error-analysis-corrective-feedback.md) for how a near-miss score (within one SEM of the cut) should drive remediation rather than an immediate gate decision.
