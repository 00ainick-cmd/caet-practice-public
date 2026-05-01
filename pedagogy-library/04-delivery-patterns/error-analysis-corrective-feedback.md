---
id: error-analysis-corrective-feedback
title: Error Analysis & Corrective Feedback
category: 04-delivery-patterns
aliases: [corrective-feedback, error-correction, elaborated-feedback]
evidence_strength: strong
effect_size: "Cohen's d ≈ 0.66 across 435 studies and ~61,000 learners (Wisniewski, Zierer & Hattie 2020 meta-analysis); d ≈ 0.7 from the Hattie & Timperley 2007 synthesis. Elaborated feedback that names the underlying error mechanism outperforms verification-only feedback by roughly d = 0.4 (Bangert-Drowns et al. 1991 meta-analysis)."
key_sources:
  - "Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research*, 77(1), 81-112. doi:10.3102/003465430298487"
  - "Wisniewski, B., Zierer, K., & Hattie, J. (2020). The power of feedback revisited: A meta-analysis of educational feedback research. *Frontiers in Psychology*, 10, Article 3087. doi:10.3389/fpsyg.2019.03087"
  - "Kluger, A. N., & DeNisi, A. (1996). The effects of feedback interventions on performance: A historical review, a meta-analysis, and a preliminary feedback intervention theory. *Psychological Bulletin*, 119(2), 254-284. doi:10.1037/0033-2909.119.2.254"
  - "Shute, V. J. (2008). Focus on formative feedback. *Review of Educational Research*, 78(1), 153-189. doi:10.3102/0034654307313795"
  - "Bangert-Drowns, R. L., Kulik, C.-L. C., Kulik, J. A., & Morgan, M. (1991). The instructional effect of feedback in test-like events. *Review of Educational Research*, 61(2), 213-238. doi:10.3102/00346543061002213"
  - "Pashler, H., Cepeda, N. J., Wixted, J. T., & Rohrer, D. (2005). When does feedback facilitate learning of words? *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 31(1), 3-8. doi:10.1037/0278-7393.31.1.3"
  - "Metcalfe, J. (2017). Learning from errors. *Annual Review of Psychology*, 68, 465-489. doi:10.1146/annurev-psych-010416-044022"
last_reviewed: 2026-04-30
applies_to: [acquisition, retention, transfer]
contraindicated_when:
  - learner_state.overwhelmed
  - learner_state.first_exposure
  - material.high_element_interactivity_no_scaffolding
  - task_type.exploratory_inquiry_emergent_outcomes
runtime_triggers:
  - learner_error_committed
  - formative_assessment_completed
  - retrieval_attempt_incorrect
  - misconception_pattern_detected
  - second_attempt_scheduled
related: [testing-effect, spaced-retrieval, mastery-learning, predict-before-reveal, self-explanation-prompts, productive-failure, coach-encourager, pre-post-assessment-effect-size, distractor-analysis]
---

# Error Analysis & Corrective Feedback

## One-line claim

When a learner errs, diagnose the underlying error type, then deliver elaborated feedback that names the correct answer and the mechanism that generated the error before the learner re-attempts the task — verification-only feedback ("right/wrong") is roughly half as effective.

## Evidence base

Hattie and Timperley (2007) synthesized roughly 12 meta-analyses on feedback in *Review of Educational Research* and reported an average effect of d ≈ 0.79 on achievement, ranking feedback among the highest-leverage instructional moves available — but with the warning that the variance across studies is enormous, and over a third of feedback interventions in the underlying base produce zero or negative effects. Their three-question model — *Where am I going? How am I going? Where to next?* — operationalizes feedback at four levels (task, process, self-regulation, self) and predicts that task- and process-level feedback (the corrective levels) drive learning while self-level feedback ("good job") does not (Hattie & Timperley, 2007, pp. 90-99). The Kluger and DeNisi (1996) meta-analysis in *Psychological Bulletin* established the boundary: across 607 effect sizes and 23,663 observations, mean feedback effect was d = 0.41, but feedback that pulled attention to the *self* rather than the task degraded performance — feedback intervention effectiveness "decreases as attention moves up the hierarchy closer to the self and away from the task" (Kluger & DeNisi, 1996, pp. 254-258).

Modern meta-analytic evidence sharpens the picture. Wisniewski, Zierer, and Hattie (2020) synthesized 435 studies and ~61,000 learners in *Frontiers in Psychology* and reported a mean d = 0.48 with the strongest moderator being information content: high-information feedback (elaborated, with reasoning) substantially outperforms low-information feedback (correct/incorrect alone). Bangert-Drowns, Kulik, Kulik, and Morgan (1991) had earlier shown the same pattern in 58 effect sizes from 40 *Review of Educational Research* studies, finding that elaborated feedback (feedback that explains *why* the answer is right or wrong) produced approximately d = 0.55 while answer-only verification produced near-zero or negative effects — and that pre-search-available feedback (telling the learner the answer before they tried) actively *reduced* learning. Shute's (2008) review systematized the implementation guidance: feedback should be specific, focused on the task not the learner, timed to the learner's state, and short enough to be processed rather than skipped (Shute, 2008, pp. 158-178). Pashler, Cepeda, Wixted, and Rohrer (2005) demonstrated the asymmetry experimentally: supplying the correct answer after an *incorrect* response on a Luganda-English vocabulary task increased one-week retention by 494% over no feedback, while feedback after correct responses produced negligible benefit — feedback's payoff is concentrated at the moment of error.

The mechanism for why errors corrected with elaboration learn better than errors avoided is documented in Metcalfe's (2017) *Annual Review of Psychology* synthesis: errors made with high confidence are corrected more readily than low-confidence errors (the hypercorrection effect), and errorful generation followed by corrective feedback consistently outperforms error-free study under controlled conditions. Two boundary conditions are well-established. First, when cognitive load is already saturated — initial exposure to high-element-interactivity material — eliciting errors and processing corrective feedback both add load and produce no learning gain (Kluger & DeNisi, 1996, on attention budget). Second, when feedback redirects attention to self-evaluation rather than task evaluation ("you're not good at this"), the meta-analytic effect inverts and becomes negative; this is the dominant explanation for the third of feedback interventions that harm performance.

## When to apply

- **Learner just committed an error during practice or assessment** — Within seconds to minutes
  of the wrong response, deliver elaborated feedback: correct answer, error type, mechanism.
  Pashler et al. (2005) showed this is the high-leverage moment; feedback on correct responses
  adds little.
- **Formative assessment completed and errors cluster around identifiable sub-skills** — When
  errors are non-random (specific rule, step, or distractor), category-by-category analysis
  turns the score into a corrective plan. See
  [distractor-analysis](../03-assessment-science/distractor-analysis.md) for the diagnostic.
- **Retrieval attempt was incorrect** — Retrieval without feedback locks in errors (see
  [testing-effect](../01-learning-science/testing-effect.md)). Always close the loop on
  incorrect retrievals before the next attempt or concept.
- **Misconception pattern detected across learners or sessions** — When the same wrong answer
  recurs (distractor choice, language-production error, physical-procedure deviation), the
  corrective must address the mental model, not the surface answer.
- **Second attempt scheduled within same session or next day** — Feedback the learner cannot
  apply is decoration. Schedule a parallel attempt while the corrective is still active in
  working memory but past re-encoding; one to twenty-four hours is the empirical sweet spot.
- **Stakes are summative or downstream content depends on this skill** — When uncorrected-error
  cost is high (certification, downstream skill blocked, field error), invest in elaborated
  feedback. Hattie and Timperley (2007) showed effects are largest when learners do not yet
  know what they got wrong.

## When NOT to apply

- **Learner is in the initial encoding phase of a complex concept** — Forcing error elicitation
  and corrective processing before a stable mental model exists adds extraneous load and
  produces no gain (Kluger & DeNisi, 1996). Build the model with worked examples first;
  error-analyze once the schema is in place.
- **Cognitive load is already saturated** — Slow responses, errors on basics, expressed
  frustration, or a pre-assessment below ~50% on the current segment all signal that adding
  corrective processing will worsen the load. Reduce extraneous load first; correct errors
  second. See [cognitive-load-theory](../01-learning-science/cognitive-load-theory.md).
- **The "error" is exploratory inquiry or genuine creative divergence** — When the activity is
  open-ended exploration ([productive-failure](../04-delivery-patterns/productive-failure.md))
  and the desired outcome is novel synthesis, treating divergent attempts as errors collapses
  the inquiry. Reserve corrective feedback for tasks with a defensible criterion answer.
- **Feedback would land at the self level rather than the task level** — Comments that
  evaluate the learner ("you don't have a knack for this") rather than the work invert the
  effect (Kluger & DeNisi, 1996, pp. 277-280). If the only available framing is self-level,
  delay the feedback until task-level framing is available.
- **No second attempt or application opportunity exists** — Feedback the learner cannot apply
  has near-zero effect. If the only assessment is a one-shot summative with no follow-up,
  invest the corrective elsewhere (instructional redesign, re-teach the cohort) rather than
  delivering feedback that has no surface to land on.

## How to apply

- **Diagnose the error type before responding** — Misconception (wrong mental model), slip
  (right model, execution failure), gap (model not yet built), or guess (no model engaged)
  each call for different correctives. A one-line internal classification — "slip on step 3,
  not a rule misconception" — disciplines the response. Hattie and Timperley (2007, pp. 90-94)
  frame this as the *How am I going?* / *Where to next?* split.
- **Deliver elaborated, task-focused feedback in one exchange** — Confirm the correct answer,
  name the error mechanism in one sentence, stop. Bangert-Drowns et al. (1991) showed
  elaborated feedback outperforms answer-only verification by ≈ d = 0.4; elaboration past one
  sentence shows diminishing returns and risks reverting to lecture.
- **Keep feedback at the task and process levels; avoid the self level** — "The trace shows X,
  so the encoder is mis-set" is task-level. "You're not good at troubleshooting" is self-level
  and meta-analytically *worse* than no feedback (Kluger & DeNisi, 1996). See
  [coach-encourager](../05-tutor-personas/coach-encourager.md) for the persona discipline.
- **Schedule a parallel second attempt within 1-24 hours** — Feedback the learner does not
  apply does not consolidate. A second item probing the same construct with different surface
  features within the day converts the corrective into learning; longer delays let it fade. See
  [mastery-learning](../02-instructional-design/mastery-learning.md) for the Formative A/B
  structure this drops into.
- **For high-confidence errors, surface the confidence-correction loop explicitly** — Metcalfe
  (2017) showed high-confidence errors are corrected more readily when the learner sees they
  were both confident and wrong. "You sounded sure of that, but the answer is X because Y"
  exploits the hypercorrection effect rather than hiding it.
- **Calibrate to the learner's error rate** — Above ~30% errors, the task is too hard for
  productive correction; below ~10%, retrieval is recognition and feedback has nothing to
  grip. The band is 70-85% accuracy on a stretch prompt; see
  [desirable-difficulties](../01-learning-science/desirable-difficulties.md).

## Common misapplications

- **"Right/wrong" verification with no mechanism** — Verdict-only feedback is near-zero effect
  (Bangert-Drowns et al., 1991) and the modal failure of automated graders.
- **Self-level praise or criticism** — "Great job!" and "you're disappointing" pull attention
  up the Kluger-DeNisi hierarchy and degrade performance. Keep feedback on the task.
- **Pre-search-available feedback** — Showing the answer *before* an attempt converts practice
  into re-reading; Bangert-Drowns et al. (1991) found this *negatively* affects learning.
- **Burying the corrective in praise** — A two-paragraph reassurance with one sentence of
  correction is processed as praise (Shute, 2008, pp. 167-170). Lead with the corrective.
- **Re-teaching the whole concept for one missed item** — Over-corrects, adds load, signals
  total failure. Match corrective scope to error scope.
- **Ignoring high-confidence errors as "honest mistakes"** — High-confidence errors are *most*
  learnable when corrected (Metcalfe, 2017); treating them as unimportant wastes the moment.
- **Skipping feedback to "let them learn from the mistake"** — Unfed errors consolidate as
  errors. [Productive-failure](../04-delivery-patterns/productive-failure.md) endorses unfed
  *exploration*, not unfed *practice on criterion*.

## Examples across domains

**Avionics — IFR-6000 ramp test, technician misreads a Mode S squitter trace.**

*Setup.* A junior technician performing an ADS-B Out verification with an IFR-6000 ramp
tester has declared the install compliant after seeing three Mode S replies, but missed that
the ES squitter position-source latency is 0.6 s — outside the 0.5 s window in 14 CFR
91.227(c)(3). The error is a high-confidence rule-application slip, not a gap.

*Diagnosis and feedback.* The tutor classifies it as a slip on the latency-tolerance check
(rule known, wrong trace field consulted). Task-level feedback in one exchange: "Three Mode S
replies are present, but check the ES position latency — 0.6 s on the trace, 91.227 limit is
0.5 s. That's a non-compliance." The mechanism (latency field), rule (91.227(c)(3)), and
verdict are named. No re-teach.

*Spacing and second attempt.* A parallel scenario with a different tail and a marginal
latency value (0.48 vs. 0.51 s) is queued for the next-day shop session. Wisniewski et al.
(2020) report d ≈ 0.48 for elaborated feedback at this scope; Pashler et al. (2005) showed the
+494% one-week retention gain from supplying the correct answer after an incorrect response —
the operative move here. If the latency-field error recurs at +14 days under
[spaced-retrieval](../01-learning-science/spaced-retrieval.md), escalate to a
misconception-level corrective re-covering the rule's measurement geometry.

**Basketball coaching — point guard repeatedly turns the ball over on the pick-and-roll.**

*Setup.* A varsity point guard has turned the ball over four times in two practices on the
same play: a high pick-and-roll where she picks up her dribble too early after the screen,
forcing a contested pass. Film shows the error is high-confidence (she believes she is
"reading help") and consistent across opponents — a misconception about read order, not a slip.

*Diagnosis and feedback.* The coach classifies it as a misconception (wrong read order: she
reads help-side before the screener's defender). Task-level feedback while watching the clip:
"Your eyes go to help first — see, you pick up the dribble. First read is the screener's
defender: drop or hedge. Help-side is read two. You're reading them backward, which is why the
pass is late." Mechanism named (read order), correct sequence given, recurring symptom tied to
cause. No self-evaluation.

*Spacing and second attempt.* The next practice opens with a 10-minute small-sided drill
isolating the pick-and-roll read, with the coach calling first read on each rep until the
guard makes the call before picking up her dribble. A scrimmage rep that practice is the
parallel second attempt; next week's game film is the +7-day spaced check
([spaced-retrieval](../01-learning-science/spaced-retrieval.md)). Hattie and Timperley (2007)
report d ≈ 0.79 average feedback effects; Metcalfe's (2017) hypercorrection finding predicts
this high-confidence error, once corrected, is more durable than a tentative one.

## Quality signal

The AI tutor knows error analysis and corrective feedback are working when (a) second-attempt accuracy on a parallel item within 24 hours exceeds first-attempt accuracy by Cohen's d > 0.5 — within the Wisniewski et al. (2020) meta-analytic range — and (b) the same error category does not recur on the +7-day spaced check for at least 70% of learners. A negative signal: if learners pass the immediate corrective re-test but the same error reappears at +7 days, the feedback was processed at the verification level not the mechanism level, and the next iteration must elaborate the underlying model rather than the surface fix.

## Cross-references

- See [testing-effect](../01-learning-science/testing-effect.md) for retrieval-with-feedback as the pairing this chapter completes.
- See [mastery-learning](../02-instructional-design/mastery-learning.md) for the Formative A → corrective → Formative B structure at unit scale.
- See [spaced-retrieval](../01-learning-science/spaced-retrieval.md) for the +7-to-+14-day check that distinguishes a corrective that consolidated from one that faded.
- See [predict-before-reveal](../04-delivery-patterns/predict-before-reveal.md) for the move that elicits the error in the first place.
- See [self-explanation-prompts](../04-delivery-patterns/self-explanation-prompts.md) for elaboration that turns a corrective into generative re-encoding.
- See [productive-failure](../04-delivery-patterns/productive-failure.md) for the contrasting case where exploration errors are not corrected on the spot.
- See [coach-encourager](../05-tutor-personas/coach-encourager.md) for the persona discipline that keeps feedback at task/process level (Kluger & DeNisi, 1996).
- See [distractor-analysis](../03-assessment-science/distractor-analysis.md) for the item-level diagnostic that surfaces the misconception pattern to correct.
- See [pre-post-assessment-effect-size](../03-assessment-science/pre-post-assessment-effect-size.md) for the calculation that detects when feedback is producing the meta-analytic effect.
