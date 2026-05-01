---
id: self-explanation-prompts
title: Self-Explanation Prompts
category: 04-delivery-patterns
aliases: [self-explanation-prompting, why-prompts, scaffolded-self-explanation]
evidence_strength: strong
effect_size: "Hedges' g ≈ 0.55 across 64 studies, 69 effect sizes (Bisra et al. 2018 meta-analysis); assisting/scaffolded prompt format outperforms open-prompt format (Berthold, Eysink & Renkl 2009, η² ≈ 0.18 on conceptual-knowledge post-test)"
key_sources:
  - "Chi, M. T. H., De Leeuw, N., Chiu, M.-H., & LaVancher, C. (1994). Eliciting self-explanations improves understanding. Cognitive Science, 18(3), 439-477. doi:10.1207/s15516709cog1803_3"
  - "Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F., & Winne, P. H. (2018). Inducing self-explanation: A meta-analysis. Educational Psychology Review, 30(3), 703-725. doi:10.1007/s10648-018-9434-x"
  - "Renkl, A. (1997). Learning from worked-out examples: A study on individual differences. Cognitive Science, 21(1), 1-29. doi:10.1207/s15516709cog2101_1"
  - "Aleven, V. A. W. M. M., & Koedinger, K. R. (2002). An effective metacognitive strategy: Learning by doing and explaining with a computer-based Cognitive Tutor. Cognitive Science, 26(2), 147-179. doi:10.1207/s15516709cog2602_1"
  - "Berthold, K., Eysink, T. H. S., & Renkl, A. (2009). Assisting self-explanation prompts are more effective than open prompts when learning with multiple representations. Instructional Science, 37(4), 345-363. doi:10.1007/s11251-008-9051-z"
  - "Chi, M. T. H., & Wylie, R. (2014). The ICAP framework: Linking cognitive engagement to active learning outcomes. Educational Psychologist, 49(4), 219-243. doi:10.1080/00461520.2014.965823"
  - "Rittle-Johnson, B. (2006). Promoting transfer: Effects of self-explanation and direct instruction. Child Development, 77(1), 1-15. doi:10.1111/j.1467-8624.2006.00852.x"
last_reviewed: 2026-04-30
applies_to: [acquisition, retention, transfer]
contraindicated_when:
  - learner_state.first_exposure
  - learner_state.overwhelmed
  - material.high_element_interactivity_no_scaffolding
  - task_type.motor_acquisition
runtime_triggers:
  - worked_example_studied
  - solution_step_completed
  - misconception_suspected
  - segment_boundary
  - transfer_problem_introduced
related: [self-explanation-elaborative-interrogation, worked-example-effect, faded-worked-examples, predict-before-reveal, testing-effect, error-analysis-corrective-feedback, cognitive-load-theory, schema-theory-knowledge-components]
---

# Self-Explanation Prompts

## One-line claim

Insert a targeted, generative "why" or "how" prompt at a chosen pause point in the instructional flow so the learner constructs a principle-based explanation of just-presented content before the canonical reasoning is revealed.

## Evidence base

Self-explanation prompts are the operational delivery layer of the self-explanation principle: a tutor presents a worked step, fact, or solution path, then halts the flow with a directed prompt that requires the learner to articulate the underlying reason. Chi, De Leeuw, Chiu, and LaVancher (1994) demonstrated in *Cognitive Science* that line-by-line prompting after each sentence of a circulatory-system text doubled inference-question gains over a re-read control, and that the highest-gain learners produced principle-based — not surface — explanations. Renkl (1997) sharpened the prompt-design implication in the same journal: when probability worked-examples were paired with self-explanation prompts and time-on-task was held constant, learning gains were predicted almost entirely by whether learners produced principle-based reasoning and anticipative inferences. Aleven and Koedinger (2002) translated this into a runtime delivery pattern in *Cognitive Science*: high-school geometry students working a Cognitive Tutor were prompted to select the justification (theorem, definition, postulate) for each step before the tutor accepted the move; the explainers outperformed an otherwise-identical control on transfer items even though procedural problem-solving accuracy was equivalent at training time.

The meta-analytic estimate is well-established. Bisra, Liu, Nesbit, Salimi, and Winne (2018) synthesized 64 studies (69 effect sizes) in *Educational Psychology Review* and reported a random-effects mean of g ≈ 0.55 favoring self-explanation prompts over no-prompt controls, robust across subject area, age band, and inducement format. Their moderator analysis is the closest evidence the literature offers to design-level guidance: prompts produce gains for both narrative and procedural content, and the format used (open prompt vs. scaffolded vs. menu-based) modulates magnitude rather than reverses sign. The Chi and Wylie (2014) ICAP framework in *Educational Psychologist* placed self-explanation prompts at the constructive engagement tier — generating new inferences beyond presented material — and predicted (with empirical support across note-taking, concept-mapping, and self-explaining literatures) that constructive engagement outperforms active engagement, which outperforms passive exposure.

The boundary that bears most directly on prompt design is the choice between open and scaffolded prompts. Berthold, Eysink, and Renkl (2009) tested three conditions in *Instructional Science* — open prompts, assisting prompts (partial explanations with blanks), and no-prompt control — on multi-representational worked examples in probability theory. Assisting prompts produced significantly higher concept-based explanation frequency and conceptual-knowledge gains than open prompts; open prompts beat the no-prompt control but underperformed scaffolded prompts. The mechanism: open prompts demand prior schema strong enough to generate principle-based reasoning unaided; when that schema is partial, scaffolding directs explanatory effort toward the principle rather than letting it dissipate into surface paraphrase. Rittle-Johnson (2006) replicated the transfer signature in *Child Development* with elementary mathematics: children prompted to explain why solutions were correct or incorrect transferred to novel problem types regardless of whether the procedure was instructed or invented.

## When to apply

- **Worked example just studied** — Immediately after the learner finishes a complete worked
  example, before they attempt an isomorphic problem, prompt them to explain why a chosen
  principled step was taken (see [worked-example-effect](../01-learning-science/worked-example-effect.md)).
  Renkl (1997) showed example-study gains track principle-based self-explanation almost linearly.
- **Solution step completed** — Inside an interactive problem, after the learner takes a correct
  procedural step, ask them to justify it before moving to the next step. Aleven and Koedinger
  (2002) operationalized this as "explain by reference" — the tutor presents a menu of theorems,
  definitions, and postulates and the learner selects the rule that authorizes the step.
- **Misconception suspected** — When the learner gives a correct surface answer through suspect
  reasoning, "Walk me through why you did it that way" exposes the underlying model before it
  propagates (see [error-analysis-corrective-feedback](../04-delivery-patterns/error-analysis-corrective-feedback.md)).
- **Segment boundary** — At the close of a segment, prompt the learner to explain how today's
  content connects to a principle they already know. Pairs with retrieval (see
  [testing-effect](../01-learning-science/testing-effect.md)) for the strongest combined
  durability gains in the integrated literature.
- **Transfer problem introduced** — Before showing the canonical solution to a problem requiring
  extension of a known principle, prompt the learner to explain how they would adapt it.
  Rittle-Johnson (2006) reports self-explanation's largest gains on transfer items, not
  near-transfer.

## When NOT to apply

- **Learner has no usable prior knowledge of the content** — Prompting "why" without a schema
  yields confabulation. Bisra et al. (2018) shows low-prior-knowledge learners benefit most
  when prompts are paired with scaffolding, and least when prompts are open and the domain is
  unfamiliar. Build the schema first (worked example, demonstration), then prompt.
- **Cognitive load is already saturated** — When the learner shows slow responses, basic-level
  errors, or frustration on the current segment, a self-explanation prompt compounds load (see
  [cognitive-load-theory](../01-learning-science/cognitive-load-theory.md)). Reduce extraneous
  load before prompting.
- **Material is high in element interactivity with no scaffolding** — Densely interconnected new
  content consumes working memory on integration itself; layer self-explanation in once a worked
  example or partial solution has reduced load.
- **Pure motor execution phase** — Self-explanation operates on declarative and conceptual
  content. The hands-on motor loop is governed by physical practice and corrective feedback;
  verbal explanation belongs to the conceptual scaffolding around the motor task (why this
  torque, why this sequence), not the execution.
- **No reveal channel** — A prompt with no canonical-answer reveal lets plausible-sounding wrong
  models consolidate. If the runtime cannot supply or verify the correct reasoning after the
  attempt, do not prompt.

## How to apply

- **Use principle-based "why" prompts; avoid surface "what" prompts** — "Why does this step
  work?" generates the transfer-predicting explanations Renkl (1997) identified; "Describe what
  this step does" elicits paraphrase that predicts only verbatim recall. If the learner answers
  with a paraphrase, follow up with "and what underlying rule made that the right move?"
- **Scaffold the prompt when prior knowledge is partial** — Berthold, Eysink, and Renkl (2009)
  showed assisting prompts (partial explanation with blanks, e.g., "This step works because
  the ___ rule says ___") outperform open prompts when the schema is not yet stable. Open
  prompts when the schema is robust; scaffolded prompts when it is thin.
- **Pair tightly with worked examples** — The strongest single combination is worked-example
  study + immediate prompt (Renkl 1997; Aleven & Koedinger 2002). The prompt converts passive
  example study into the constructive engagement mode of ICAP (Chi & Wylie 2014).
- **Reveal the canonical reasoning every time** — Self-explanation without a reveal lets
  misconceptions consolidate. After the attempt, show the reference reasoning, name the gap if
  any, and ask the learner to restate the corrected explanation in their own words once. The
  restate-once step is what locks the corrected model.
- **One or two prompts per segment, not every line** — Chi et al. (1994) prompted line-by-line
  on a tightly-sized text, but in field tutoring frequent prompts fragment schema-building.
  Place prompts at meaningful structural breaks: after a worked step, at a segment boundary,
  before a transfer problem.
- **As expertise grows, fade from menu to scaffolded to open** — Novices benefit most from
  menu-based or assisting prompts; advanced learners benefit most from open prompts
  (expertise-reversal logic in [expertise-reversal](../01-learning-science/expertise-reversal.md));
  track this as part of [faded-worked-examples](../04-delivery-patterns/faded-worked-examples.md).

## Common misapplications

- **Treating restatement as explanation** — "Tell me what the manual said" is paraphrase;
  "Tell me why the manual specifies it that way" is explanation. Only the latter produces
  the meta-analytic effect (Bisra et al. 2018; Chi et al. 1994).
- **Prompting before encoding** — Asking a complete novice to explain "why" before they
  have any model of the system produces guesses, not learning. Build the model first.
- **Skipping the canonical-answer reveal** — A learner whose self-explanation is plausible
  but wrong will rehearse the wrong model. Always close the loop with the correct
  reasoning, even briefly.
- **Asking "what do you think?" instead of "why"** — Open-ended opinion prompts are not
  self-explanation; they generate elaboration unanchored to the source content. The
  prompt must reference the just-presented material and demand a principle.
- **Using open prompts with low-prior-knowledge learners** — Open prompts in unfamiliar
  domains produce surface paraphrase or silence (Berthold, Eysink & Renkl 2009). When in
  doubt about prior knowledge, scaffold first; remove scaffolding once the learner is
  generating principle-based responses unprompted.

## Examples across domains

**Avionics — Garmin GTN 750Xi VHF NAV/COMM RF cabling, post-install verification.**

*Setup.* A technician has just completed a worked-example walk-through of post-installation
cable-loss verification for a GTN 750Xi VOR/LOC/GS receiver: connect a calibrated signal
generator at the antenna end, inject a –80 dBm signal at 108.10 MHz, confirm the GTN reports
the expected signal strength within the cable-loss budget specified in the installation manual.

*Self-explanation prompt.* Before moving to the isomorphic GS-frequency check, the tutor asks
(assisting form, partial schema): "The cable-loss budget for this install is 6 dB. If the GTN
reports –86 dBm with a –80 dBm injected signal, the loss is acceptable because ___ — and if it
reports –92 dBm the install fails because ___." The technician fills in: acceptable means
measured loss matches budget within tolerance; failure at –92 means actual loss exceeds budget,
indicating connector or cable degradation. The tutor reveals the canonical reasoning, adds the
rule that out-of-budget loss invalidates the sensitivity assumption underlying the receiver's
published MDS, and asks the technician to restate it once. On the next isomorphic problem (a
separate ADS-B antenna line), the technician applies the principle to a different frequency
without re-prompting (Aleven & Koedinger 2002 transfer signature).

*Spacing.* The same prompt class returns at +24 hours as a transfer item: "Why would the same
–6 dB budget be too tight for a satellite-comm install at 1.6 GHz?" The learner now has to
extend the rule (cable loss scales with frequency) — the transfer payoff Bisra et al. (2018)
identifies as the family's strongest signature.

**Music performance — violin intonation in a Bach Partita lesson.**

*Setup.* A second-year violin student is working the opening Allemande of Bach Partita No. 2
in D minor. They have just worked through a phrase with their teacher, correcting a sharp
F-natural in measure 3 by lowering the second finger relative to the first. They play the
corrected phrase cleanly; the natural next move is another play-through or a re-explanation.

*Self-explanation prompt.* Instead, the teacher asks (open form, because the student has the
schema for diatonic intonation): "Why does that F-natural have to sit *lower* than
equal-tempered F-natural in this key?" The student retrieves what they know about just
intonation in melodic minor — F-natural functions as the minor third above the tonic D, and a
lowered minor third (about 16 cents below equal-tempered) gives the characteristic darker
color of D minor. The teacher confirms, adds the corollary that the same finger would be
raised in a piece centered on F major (where F is the tonic), and asks the student to restate
the rule. On measure 7, where a similar interval recurs in a different bowing but the same
harmonic function, the student adjusts intonation without prompting.

*Follow-up.* In the next lesson the teacher returns to the prompt as a transfer probe on a
contrasting Allemande in F major: "How does this change?" — forcing the student to apply the
principle, not retrieve a cached fingering. Rittle-Johnson (2006) is the closest analog:
self-explanation prompts produced their largest gains on procedural-transfer items.

## Quality signal

The AI tutor knows self-explanation prompts are landing when learner-generated explanations contain at least one principle-based reference ("because the X rule…", "because Y is the authoritative source for Z") rather than a surface restatement, on at least 70% of prompts within a segment. A second-tier signal is transfer accuracy at +24 hours: if performance on a transfer item is not at least 15 percentage points above a no-prompt baseline (the Bisra et al. 2018 g ≈ 0.55 translated to a binary outcome), the prompt format is too shallow, the prior knowledge is missing, or the canonical-answer reveal is failing to land.

## Cross-references

- See [self-explanation-elaborative-interrogation](../01-learning-science/self-explanation-elaborative-interrogation.md) for the underlying learning-science principle this delivery pattern operationalizes.
- See [worked-example-effect](../01-learning-science/worked-example-effect.md) for the example-study trigger that pairs most strongly with self-explanation prompts.
- See [faded-worked-examples](../04-delivery-patterns/faded-worked-examples.md) for the staged transition where self-explanation prompts gradually replace worked steps as the learner progresses toward independent problem solving.
- See [predict-before-reveal](../04-delivery-patterns/predict-before-reveal.md) for the closely related delivery move that combines retrieval with subsequent explanation.
- See [testing-effect](../01-learning-science/testing-effect.md) for the retrieval mechanism whose combination with self-explanation produces the largest documented durability gains.
- See [cognitive-load-theory](../01-learning-science/cognitive-load-theory.md) for the load constraint that bounds when self-explanation prompts help versus when they overwhelm.
- See [error-analysis-corrective-feedback](../04-delivery-patterns/error-analysis-corrective-feedback.md) for how to handle wrong self-explanations so the canonical reveal repairs the model rather than merely the answer.
- See [schema-theory-knowledge-components](../01-learning-science/schema-theory-knowledge-components.md) for the prior-knowledge structure that determines whether a self-explanation prompt can land at all.
