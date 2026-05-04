---
id: bayesian-knowledge-tracing
title: Bayesian Knowledge Tracing
category: 07-runtime-decisions
aliases: [bkt, knowledge-tracing, corbett-anderson-knowledge-tracing]
evidence_strength: strong
effect_size: null  # BKT is an inference algorithm, not a single intervention; magnitudes appear instead in mastery-decision precision and learning-rate gains. The four parameters (P(L0), P(T), P(S), P(G)) are reported per skill. The original Corbett & Anderson (1995) study reported a 0.95 mastery threshold and roughly 30% reduction in problem-solving time at matched test performance under knowledge-tracing-driven mastery learning.
key_sources:
  - "Corbett, A. T., & Anderson, J. R. (1995). Knowledge tracing: Modeling the acquisition of procedural knowledge. User Modeling and User-Adapted Interaction, 4(4), 253-278. doi:10.1007/BF01099821"
  - "Baker, R. S. J. d., Corbett, A. T., & Aleven, V. (2008). More accurate student modeling through contextual estimation of slip and guess probabilities in Bayesian Knowledge Tracing. In Intelligent Tutoring Systems (Lecture Notes in Computer Science, Vol. 5091, pp. 406-415). Springer. doi:10.1007/978-3-540-69132-7_44"
  - "Pardos, Z. A., & Heffernan, N. T. (2010). Modeling individualization in a Bayesian networks implementation of knowledge tracing. In P. De Bra, A. Kobsa, & D. Chin (Eds.), User Modeling, Adaptation, and Personalization (UMAP 2010), Lecture Notes in Computer Science, Vol. 6075 (pp. 255-266). Springer. doi:10.1007/978-3-642-13470-8_24"
  - "Pardos, Z. A., & Heffernan, N. T. (2011). KT-IDEM: Introducing item difficulty to the knowledge tracing model. In J. A. Konstan, R. Conejo, J. L. Marzo, & N. Oliver (Eds.), User Modeling, Adaption and Personalization (UMAP 2011), Lecture Notes in Computer Science, Vol. 6787 (pp. 243-254). Springer. doi:10.1007/978-3-642-22362-4_21"
  - "Yudelson, M. V., Koedinger, K. R., & Gordon, G. J. (2013). Individualized Bayesian knowledge tracing models. In H. C. Lane, K. Yacef, J. Mostow, & P. Pavlik (Eds.), Artificial Intelligence in Education (AIED 2013), Lecture Notes in Computer Science, Vol. 7926 (pp. 171-180). Springer. doi:10.1007/978-3-642-39112-5_18"
  - "Beck, J. E., & Chang, K. (2007). Identifiability: A fundamental problem of student modeling. In C. Conati, K. McCoy, & G. Paliouras (Eds.), User Modeling 2007, Lecture Notes in Computer Science, Vol. 4511 (pp. 137-146). Springer. doi:10.1007/978-3-540-73078-1_17"
  - "van de Sande, B. (2013). Properties of the Bayesian knowledge tracing model. Journal of Educational Data Mining, 5(2), 1-10. doi:10.5281/zenodo.3554629"
last_reviewed: 2026-04-30
applies_to: [measurement, sequencing, decision]
contraindicated_when:
  - material.uncalibrated_item_pool
  - learner_state.first_exposure
  - task_type.motor_acquisition
  - material.high_element_interactivity_no_scaffolding
runtime_triggers:
  - response_scored
  - mastery_decision_pending
  - next_item_selection_due
  - skill_pool_calibrated
  - session_start_prior_lookup
related: [item-difficulty-discrimination, performance-factor-analysis, mastery-thresholds, sm2-fsrs, knowledge-graph-traversal, schema-theory-knowledge-components, mastery-learning, testing-effect]
---

# Bayesian Knowledge Tracing

## One-line claim

Treat each knowledge component as a two-state hidden Markov chain with four parameters — P(L₀), P(T), P(S), P(G) — and update P(Lₙ), the probability the learner has mastered it, after every scored response so the runtime can decide when to advance, drill, or stop.

## Evidence base

Corbett and Anderson (1995) introduced knowledge tracing in *User Modeling and User-Adapted Interaction* as the inference engine inside the LISP and ACT programming tutors at Carnegie Mellon. Each production rule in the cognitive model is given a hidden binary state — known or unknown by the student — and four parameters: P(L₀), the prior probability the rule is already known at first encounter; P(T), the transition probability the rule is learned at any given practice opportunity; P(S), the slip probability of an incorrect response when the rule is known; and P(G), the guess probability of a correct response when the rule is unknown. After each scored response, the runtime applies Bayes' rule to update P(Lₙ), and predicts P(correct) on the next attempt as P(Lₙ)·(1 − P(S)) + (1 − P(Lₙ))·P(G). Corbett and Anderson reported that a knowledge-tracing-driven mastery cut at P(Lₙ) ≥ 0.95 reduced problem-solving time by roughly 30% at matched test performance, establishing the algorithm as the per-skill mastery scheduler that anchored two decades of cognitive-tutor deployments.

Modern work has extended and stress-tested the four-parameter model. Baker, Corbett, and Aleven (2008) showed at *Intelligent Tutoring Systems* that contextual estimation of slip and guess probabilities — letting P(S) and P(G) vary with response time, error type, and prior context rather than fixing one value per skill — improved prediction accuracy on subsequent items in the Cognitive Tutor. Pardos and Heffernan (2010, 2011) extended BKT in two complementary directions: the Prior Per Student model (UMAP 2010) gave each learner a personalized P(L₀) and produced better fits than the global prior; KT-IDEM (UMAP 2011) added an item-difficulty node that lets P(S) and P(G) vary by item and substantially improved prediction over standard BKT on ASSISTments and Cognitive Tutor data. Yudelson, Koedinger, and Gordon (2013) at AIED concluded from a large multi-dataset study that individualizing P(T) — the learner's speed of learning — yields larger gains than individualizing P(L₀), with student-specific parameters improving held-out prediction across all datasets tested.

The framework has well-documented boundary conditions. Beck and Chang (2007) argued at *User Modeling 2007* that BKT is susceptible to an identifiability problem: distinct (P(L₀), P(T), P(S), P(G)) tuples can produce identical observable predictions, so EM-fit parameters can land in semantically degenerate regions (e.g., P(S) > 0.5 implies a "known" state predicts errors more than correct answers). van de Sande (2013) in the *Journal of Educational Data Mining* derived analytical solutions to the BKT Markov chain and identified the parameter region in which the model behaves as the theory intends — practical guidance for constraining EM with priors (e.g., P(G) ≤ 0.3, P(S) ≤ 0.1) so fitted parameters remain interpretable. The runtime consequence: BKT requires a calibrated parameter set and bounded EM, not raw maximum likelihood on small data.

## When to apply

- **Response scored on a knowledge component** — Immediately after a scored attempt at an item
  tagged to a skill, run the Bayesian update on P(Lₙ) for that skill before any next-action
  decision. Caching the prior P(Lₙ) and updating once per response is the baseline operation.
- **Mastery decision pending** — When the runtime must decide whether to advance the learner past
  a skill, read the current P(Lₙ); compare against the mastery threshold (Corbett & Anderson
  used 0.95; see [mastery-thresholds](../07-runtime-decisions/mastery-thresholds.md) for the
  threshold logic). Advance when above, schedule more practice when below.
- **Next-item selection within the active skill** — While P(Lₙ) is below threshold, route the
  learner to additional items tagged to that skill before introducing dependent skills; combine
  with [item-difficulty-discrimination](../07-runtime-decisions/item-difficulty-discrimination.md)
  to pick the highest-information item at the learner's current level.
- **Skill pool has been calibrated** — Apply BKT only when (P(L₀), P(T), P(S), P(G)) exist with
  stable per-skill estimates from a calibration sample (typically several hundred student-skill
  trajectories); otherwise the posterior is a weighted noise transform.
- **Session start, returning learner** — Initialize P(L₀) from the learner's prior trajectory
  rather than the population default when individualized priors are available (Pardos &
  Heffernan, 2010). For a brand-new learner, fall back to the population P(L₀).
- **Identifying long-term gaps for spaced review** — Skills with P(Lₙ) that drifted below 0.5
  since the last session are candidates for [sm2-fsrs](../07-runtime-decisions/sm2-fsrs.md)
  spacing prompts before introducing new dependent material.

## When NOT to apply

- **Skill parameters are uncalibrated** — Without stable (P(L₀), P(T), P(S), P(G)), the posterior
  drifts on whatever P(S)/P(G) defaults were guessed; Beck and Chang (2007) showed equally
  good-fitting tuples can produce opposite mastery decisions. Use a CTT-style proportion-correct
  threshold until the pool is calibrated, and accept the precision loss.
- **Learner is in the first-exposure encoding phase** — BKT estimates state transitions across
  practice opportunities; before the learner has built any mental model, attributing a
  "transition" between known/unknown states is meaningless. Use worked examples first
  ([worked-example-effect](../01-learning-science/worked-example-effect.md)) and start tracing
  once attempted practice begins.
- **Pure motor skill acquisition** — BKT scores binary or near-binary item correctness against a
  declarative skill state. Procedural motor execution does not reduce to that signal during
  encoding; the verbal-conceptual companion items can be traced, the motor execution itself
  cannot.
- **High element-interactivity material without scaffolding** — When items demand integrating
  many subskills simultaneously, the binary "known/unknown" assumption per skill collapses;
  attribute the response to the wrong knowledge component and the posterior moves the wrong
  variable. Decompose the skill first
  ([schema-theory-knowledge-components](../01-learning-science/schema-theory-knowledge-components.md)).
- **Fitted parameters fall in the degenerate region** — If EM lands at P(S) > 0.3 or P(G) > 0.5
  for a skill, the model is not BKT-as-intended (van de Sande, 2013); refit with bounded priors
  or drop that skill from automated mastery decisions until the calibration is fixed.

## How to apply

- **Apply the canonical update after every scored response** — given prior P(Lₙ₋₁), observation
  oₙ ∈ {correct, incorrect}, compute the posterior P(Lₙ₋₁ | oₙ) using P(S) and P(G), then add the
  learning step P(Lₙ) = P(Lₙ₋₁ | oₙ) + (1 − P(Lₙ₋₁ | oₙ))·P(T). Persist P(Lₙ) per
  (learner, skill).
- **Source the four parameters from the calibration store, not from defaults** — P(L₀), P(T),
  P(S), P(G) per skill come from offline EM fits over the prior cohort's response logs (or from
  the canonical-tutor lookup table when one exists). The runtime reads them; it does not re-fit
  per session. If individualized P(T) is available, use it (Yudelson et al., 2013).
- **Bound EM during calibration** — Constrain P(G) ≤ 0.3 and P(S) ≤ 0.1 during parameter fitting
  to keep estimates inside the interpretable region; flag any skill that hits the bound as a
  candidate for re-tagging or item review (van de Sande, 2013).
- **Use 0.95 as the default mastery threshold** — match Corbett and Anderson's (1995) cut
  unless local validation supports a different value; cross-check against the
  [mastery-thresholds](../07-runtime-decisions/mastery-thresholds.md) chapter for the
  threshold-selection logic.
- **Combine with item difficulty for selection inside a skill** — once a skill is below mastery,
  don't pick items uniformly — call
  [item-difficulty-discrimination](../07-runtime-decisions/item-difficulty-discrimination.md)
  to choose the next item with `b` near the learner's level. BKT decides which skill to drill;
  IRT decides which item inside the skill.
- **Monitor and individualize P(T) over time** — for learners with substantial trajectory
  history, refit P(T) per learner offline; this is the parameter Yudelson et al. (2013) found
  most beneficial to individualize.
- **Pair with retrieval and spacing on advance** — when P(Lₙ) crosses 0.95, schedule retrieval
  attempts ([testing-effect](../01-learning-science/testing-effect.md)) at expanding intervals
  via [sm2-fsrs](../07-runtime-decisions/sm2-fsrs.md); BKT-mastery without spaced retrieval is
  short-term mastery only.

## Common misapplications

- **Treating a single correct response as mastery** — one correct attempt with population P(G) =
  0.2 raises P(Lₙ) modestly, not to 0.95. BKT explicitly weights guess against state evidence;
  advancing on first-correct ignores the math.
- **Using global P(S)/P(G) when per-item difficulty varies** — fixed P(G) misattributes
  guessing-on-easy-items to learning. KT-IDEM (Pardos & Heffernan, 2011) addresses this; move
  to per-item P(S)/P(G) before trusting the posterior for advancement.
- **Refitting parameters from a single learner's session** — calibration needs cohort-scale data;
  per-learner EM on a few dozen responses produces unstable fits, especially for P(T). Read
  parameters from the calibration store, update only P(Lₙ) at runtime.
- **Conflating low P(Lₙ) with low ability** — P(Lₙ) is per-skill. A learner below threshold on
  one skill can be above on adjacent skills; the right move is drill on the deficit skill, not
  a global remediation track.
- **Advancing on P(Lₙ) ≥ 0.95 without checking degeneracy** — if fitted P(S) = 0.4, P(Lₙ) = 0.95
  predicts only 60% correct on the next item, which is not mastery in any intuitive sense.
  Validate parameters are in the interpretable region (Beck & Chang, 2007; van de Sande, 2013).
- **Ignoring forgetting between sessions** — standard BKT has no decay term; P(Lₙ) at +30 days
  is treated as if at +30 seconds. Pair with
  [forgetting-curve](../01-learning-science/forgetting-curve.md) or FSRS, or apply a session-gap
  discount before reading the prior at session start.

## Examples across domains

**Avionics — DME (Distance Measuring Equipment) installation curriculum, post-install bench checkout module.**

*Setup.* The shop's training platform tracks 18 knowledge components for the King KN-63 DME
install module (pinout interpretation, antenna co-location, suppressor pulse logic, self-test
interpretation, etc.). Calibration sample: ~1,200 prior technicians; per-skill parameters fit
with bounded EM all fall inside (P(G) ≤ 0.3, P(S) ≤ 0.1).

*Update.* On the suppressor-pulse-logic KC, P(Lₙ₋₁) = 0.62, parameters P(S) = 0.08, P(G) = 0.18,
P(T) = 0.12. Item served (a "what voltage indicates active suppression" question), correct.
Posterior P(Lₙ₋₁ | correct) = (0.62·0.92) / (0.62·0.92 + 0.38·0.18) = 0.893; learning step P(Lₙ)
= 0.906. Below 0.95 — runtime serves one more item near `b = 0.0` per
[item-difficulty-discrimination](../07-runtime-decisions/item-difficulty-discrimination.md);
correct again, P(Lₙ) climbs to 0.974, crosses threshold.

*Decision.* Mastery recorded; runtime advances to the dependent KC (self-test interpretation),
seeds P(L₀) from the population prior, and schedules a +24-hour retrieval prompt on the just-
mastered KC ([sm2-fsrs](../07-runtime-decisions/sm2-fsrs.md)) before the bench-checkout practical.

**Emergency medicine training — adult tachyarrhythmia ACLS algorithm module for second-year EM residents.**

*Setup.* The residency program tracks 14 knowledge components inside the adult tachycardia
algorithm (rhythm recognition, stable-vs-unstable triage, synchronized cardioversion energy,
adenosine dosing, expert-consult triggers). Calibration: ~900 prior residents through a shared
item bank; bounded-EM parameter fits with individualized P(L₀) per resident from PGY-1 trajectory.

*Update.* On the synchronized-cardioversion-energy KC, the resident's prior P(Lₙ₋₁) = 0.78,
parameters P(S) = 0.07, P(G) = 0.20, P(T) = 0.10. Simulator scenario served (an unstable atrial
flutter with QRS narrow, asking for first cardioversion energy in joules); resident answers
incorrectly (chose 200 J synchronized; correct first dose is 50–100 J). Posterior P(Lₙ₋₁ |
incorrect) = (0.78·0.07) / (0.78·0.07 + 0.22·0.80) = 0.236; learning step P(Lₙ) = 0.236 +
(1 − 0.236)·0.10 = 0.312. Far below threshold — runtime drops back to a worked-example briefing
on stable-vs-unstable energy selection, then serves two more items targeted to the same KC.

*Decision.* The runtime defers advancement to the next KC until P(Lₙ) ≥ 0.95 and routes the
resident to a brief
[error-analysis](../04-delivery-patterns/error-analysis-corrective-feedback.md) prompt on
the energy-selection mistake. The simulator session schedules the same scenario at +48 hours
and again at +7 days; if P(Lₙ) holds above threshold across both, the KC is recorded as durably
mastered before the resident next runs an unsupervised resus.

## Quality signal

BKT is calibrated and producing trustworthy decisions when (a) per-skill EM fits with bounded priors all fall inside the interpretable region (P(G) ≤ 0.3, P(S) ≤ 0.1), (b) held-out prediction accuracy on the next-attempt outcome reaches AUC ≥ 0.70 averaged across skills (the typical band reported in the BKT literature for well-calibrated cognitive-tutor pools), and (c) advance decisions at P(Lₙ) ≥ 0.95 are followed by ≥ 80% accuracy on a delayed transfer item from the same KC at +7 days. A faster within-session signal: the posterior P(Lₙ) trajectory should be monotonic-or-recovering across consecutive correct responses; oscillation suggests degenerate parameters or KC mis-tagging.

## Cross-references

- See [item-difficulty-discrimination](../07-runtime-decisions/item-difficulty-discrimination.md) for the IRT-based item-selection layer that picks the next item inside a BKT-driven skill.
- See [performance-factor-analysis](../07-runtime-decisions/performance-factor-analysis.md) for an alternative learner-modeling framework that estimates per-skill ability from response history without the BKT hidden-state assumption.
- See [mastery-thresholds](../07-runtime-decisions/mastery-thresholds.md) for the threshold-selection logic that decides where to set the BKT mastery cut.
- See [sm2-fsrs](../07-runtime-decisions/sm2-fsrs.md) for the spacing scheduler that handles between-session retention after BKT mastery is recorded.
- See [knowledge-graph-traversal](../07-runtime-decisions/knowledge-graph-traversal.md) for the prerequisite logic that decides which skill BKT updates next once a KC is mastered.
- See [schema-theory-knowledge-components](../01-learning-science/schema-theory-knowledge-components.md) for the knowledge-component decomposition that defines the unit BKT traces in the first place.
- See [mastery-learning](../02-instructional-design/mastery-learning.md) for the instructional-design framework BKT operationalizes at runtime.
- See [testing-effect](../01-learning-science/testing-effect.md) for the retrieval-practice principle that strengthens P(Lₙ) at each scheduled review.
