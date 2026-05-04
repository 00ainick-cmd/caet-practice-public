---
id: self-explanation-elaborative-interrogation
title: Self-Explanation & Elaborative Interrogation
category: 01-learning-science
aliases: [self-explanation, elaborative-interrogation, why-questions]
evidence_strength: strong
effect_size: "Hedges' g ≈ 0.55 across 64 studies, 69 effect sizes (Bisra et al. 2018 meta-analysis, Educational Psychology Review); Dunlosky et al. (2013) rated both techniques 'moderate utility' across age, ability, materials, and outcome"
key_sources:
  - "Chi, M. T. H., De Leeuw, N., Chiu, M.-H., & LaVancher, C. (1994). Eliciting self-explanations improves understanding. Cognitive Science, 18(3), 439-477. doi:10.1207/s15516709cog1803_3"
  - "Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques: Promising directions from cognitive and educational psychology. Psychological Science in the Public Interest, 14(1), 4-58. doi:10.1177/1529100612453266"
  - "Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F., & Winne, P. H. (2018). Inducing self-explanation: A meta-analysis. Educational Psychology Review, 30(3), 703-725. doi:10.1007/s10648-018-9434-x"
  - "Pressley, M., Wood, E., Woloshyn, V. E., Martin, V., King, A., & Menke, D. (1992). Encouraging mindful use of prior knowledge: Attempting to construct explanatory answers facilitates learning. Educational Psychologist, 27(1), 91-109. doi:10.1207/s15326985ep2701_7"
  - "Rittle-Johnson, B. (2006). Promoting transfer: Effects of self-explanation and direct instruction. Child Development, 77(1), 1-15. doi:10.1111/j.1467-8624.2006.00852.x"
  - "Wong, R. M. F., Lawson, M. J., & Keeves, J. (2002). The effects of self-explanation training on students' problem solving in high-school mathematics. Learning and Instruction, 12(2), 233-262. doi:10.1016/S0959-4752(01)00027-5"
  - "Renkl, A. (1997). Learning from worked-out examples: A study on individual differences. Cognitive Science, 21(1), 1-29. doi:10.1207/s15516709cog2101_1"
last_reviewed: 2026-04-29
applies_to: [acquisition, retention, transfer]
contraindicated_when:
  - learner_state.first_exposure
  - learner_state.overwhelmed
  - material.high_element_interactivity_no_scaffolding
  - task_type.motor_acquisition
runtime_triggers:
  - worked_example_studied
  - new_fact_presented
  - segment_boundary
  - misconception_suspected
  - transfer_problem_introduced
related: [testing-effect, worked-example-effect, self-explanation-prompts, predict-before-reveal, faded-worked-examples, schema-theory-knowledge-components, cognitive-load-theory, error-analysis-corrective-feedback]
---

# Self-Explanation & Elaborative Interrogation

## One-line claim

Prompting the learner to explain WHY a fact is true or HOW a procedural step works — in their own words, before moving on — produces durably better understanding and transfer than reading or being told the same content for the same amount of time.

## Evidence base

Self-explanation and elaborative interrogation are two closely related study moves that converge on the same mechanism: forcing the learner to integrate new information with prior knowledge by generating an explanation. Chi, De Leeuw, Chiu, and LaVancher (1994) provided the canonical demonstration in *Cognitive Science*: eighth-graders prompted to self-explain after each line of a circulatory-system text outperformed an otherwise-identical re-reading control on both factual recall and inference questions, with the effect concentrated on the items that required combining facts the text presented separately. The effect generalized rapidly from expository text to worked examples — Renkl (1997) showed in *Cognitive Science* that learning gains from worked algebra examples were predicted by self-explanation quality (principle-based reasoning, anticipation of next steps) even after controlling for time on task, and that successful learners cluster into "principle-based explainers" and "anticipative reasoners". The parallel literature on elaborative interrogation, reviewed by Pressley, Wood, Woloshyn, Martin, King, and Menke (1992) in *Educational Psychologist*, established that prompting "Why would that be true?" after each presented fact produced substantial gains over reading-control across a range of fact-learning tasks for both children and adults.

Modern meta-analytic evidence places the combined family on solid ground. Bisra, Liu, Nesbit, Salimi, and Winne (2018) synthesized 64 studies (69 effect sizes) in *Educational Psychology Review* and reported a random-effects mean of g ≈ 0.55 favoring self-explanation prompts over no-prompt controls, with the advantage robust across subject area (mathematics, science, text comprehension), age band, and inducement format (open prompts, scaffolded prompts, menu-of-explanations prompts). Wong, Lawson, and Keeves (2002) showed in *Learning and Instruction* that the largest gains for self-explanation-trained ninth-graders studying a new geometry theorem appeared on far-transfer items — problems requiring extension to types not seen in the training material — not on near-transfer items. Rittle-Johnson (2006) replicated this transfer advantage in *Child Development* with elementary students learning mathematical equivalence: self-explanation promoted transfer regardless of whether the procedure was directly instructed or invented. Dunlosky, Rawson, Marsh, Nathan, and Willingham (2013) reviewed both techniques in *Psychological Science in the Public Interest* and rated each "moderate utility" — below distributed practice and practice testing only because the boundary conditions are tighter, not because the within-condition effects are smaller.

The principal boundary condition is prior knowledge. The strategy works by integrating new content into an existing knowledge structure; when the structure is absent, prompts to explain produce confusion rather than learning. Pressley et al. (1992) and subsequent work consistently find that the elaborative-interrogation effect requires enough prior knowledge to generate a plausible answer to "why" — without it, learners either guess wildly or simply parrot the source. The corollary is that during initial encoding of a complex, unfamiliar concept, self-explanation prompts compete for the working-memory resources the learner needs to build the mental model in the first place; build the model with worked examples or guided explanation, then prompt the learner to explain.

## When to apply

- **Worked example just studied** — Immediately after the learner finishes studying a worked
  solution, before they attempt an isomorphic problem, prompt explanation of WHY each
  principled step was taken (see
  [worked-example-effect](../01-learning-science/worked-example-effect.md)). This is the
  highest-leverage trigger in the literature: example-based learning gains track
  self-explanation quality almost linearly (Renkl, 1997).
- **New fact presented within a connected body of knowledge** — When the learner is told a
  fact that should slot into an existing schema (e.g., a new troubleshooting heuristic that
  follows from system architecture they already know), follow it with "Why does that make
  sense given what you already know about X?" — the elaborative-interrogation prompt
  (Pressley et al., 1992).
- **Segment boundary** — At the close of a lesson segment, before moving on, ask the learner
  to explain how today's content fits with last session's. This combines retrieval (see
  [testing-effect](../01-learning-science/testing-effect.md)) with elaboration and
  produces the strongest combined gains in the integrated literature.
- **Misconception suspected** — When the learner gives a correct answer through suspect
  reasoning, "Walk me through why you did it that way" exposes the underlying model so it
  can be repaired before it propagates to a downstream problem.
- **Transfer problem introduced** — Before showing the canonical solution to a transfer
  problem, prompt the learner to explain how they would adapt a known principle. Wong et al.
  (2002) and Rittle-Johnson (2006) both found self-explanation's largest effects on transfer
  items, not on near-transfer.

## When NOT to apply

- **Learner is encountering the content for the first time with no usable prior knowledge** —
  A "why" prompt without a knowledge base to draw on yields confabulation. Build the schema
  first (worked example, demonstration, guided explanation), then prompt explanation. This
  is the elaborative-interrogation prior-knowledge boundary documented since Pressley et al.
  (1992).
- **Cognitive load is already saturated** — If the learner is showing slow responses,
  basic-level errors, or overt frustration on the current segment, self-explanation prompts
  compound the load. Reduce extraneous load (split-attention, redundant text, complex
  notation) first; then prompt.
- **Material is high in element interactivity with no scaffolding** — Densely interconnected
  new content (e.g., a multi-stage signal-processing chain encountered raw) consumes working
  memory on the integration itself; layer self-explanation in once a worked example or
  partial solution has reduced load (see
  [cognitive-load-theory](../01-learning-science/cognitive-load-theory.md)).
- **Pure motor skill acquisition phase** — Self-explanation operates on declarative and
  conceptual content. The hands-on motor learning loop (perceive → execute → adjust) is
  governed by physical practice and corrective feedback, not verbal explanation, though the
  conceptual scaffolding around the motor task (why this torque, why this sequence) is fair
  game.
- **No-feedback channel** — Self-explanation without a subsequent reveal of whether the
  explanation was correct can lock in plausible-sounding wrong models. Pair every
  self-explanation with a check against the canonical reasoning, even if brief.

## How to apply

- **Use open "why" or "how" prompts; avoid yes/no recognition** — "Why does the radio mute
  when you depress the PTT?" is generative; "Does the radio mute when you depress the PTT?
  (yes/no)" is recognition. The Bisra et al. (2018) meta-analysis found open-prompt formats
  outperformed closed/menu formats on average, though both beat no-prompt controls.
- **Prompt principle-based, not surface-based, explanation** — "Explain why this step works"
  beats "describe what this step does". Renkl (1997) showed principle-based self-explanations
  predict transfer; surface re-statements predict only verbatim recall. If the learner gives
  a surface paraphrase, follow up with "and what underlying rule made that the right move?"
- **Pair with worked examples for novices** — The strongest single combination in the
  literature is worked-example study + self-explanation prompts (see
  [self-explanation-prompts](../04-delivery-patterns/self-explanation-prompts.md) for the
  operational pattern). Solo problem-solving + self-explanation does not match it for
  novices.
- **Provide a canonical answer after the attempt** — Self-explanation without a reveal lets
  misconceptions consolidate. Show the reference reasoning, name the gap if there is one,
  and ask the learner to restate the corrected explanation in their own words once.
- **Use elaborative interrogation for fact-dense material** — When the content is many
  discrete facts that should connect to existing knowledge (regulatory limits,
  specifications, classifications), the "why is that true given what you know?" prompt is
  the more efficient form. Pressley et al. (1992) report effects across age groups for this
  format on factual recall measured at 24 hours and beyond.
- **Calibrate prompt difficulty to ~70–85% answerable** — Like retrieval practice,
  self-explanation prompts that the learner cannot answer at all are demoralizing and
  produce confabulation; prompts they answer instantly without effort drop to recognition.
  Adjust until the learner is generating plausible answers most of the time but has to work
  for them.

## Common misapplications

- **Treating restatement as explanation** — "Tell me what the manual said" is paraphrase;
  "Tell me why the manual specifies it that way" is explanation. Only the latter produces
  the meta-analytic effect (Bisra et al., 2018; Chi et al., 1994).
- **Prompting before encoding** — Asking a complete novice to explain "why the AHRS uses
  three accelerometers" before they have any model of an AHRS produces guesses, not
  learning. Build the model first; explain second.
- **Skipping the canonical-answer reveal** — A learner whose self-explanation is wrong but
  plausible will rehearse the wrong model. Always close the loop with the correct reasoning,
  even briefly.
- **Asking after every single sentence** — Chi et al. (1994) prompted line by line, but their
  text was carefully sized; in field tutoring, prompting too frequently fragments the
  schema-building process. One or two well-placed prompts per segment outperform
  line-by-line interrogation in most settings.
- **Confusing "why" with "what do you think?"** — Open-ended opinion prompts are not
  self-explanation; they generate elaboration without anchoring to the source content. The
  prompt must reference the just-presented material.

## Examples across domains

**Avionics — Garmin G1000 PFD reversionary mode during AHRS failure.**

*Setup.* A technician is studying the troubleshooting flow for an attitude-heading reference
system fault on a G1000-equipped airframe. They have just read the procedure: when the AHRS
fails, the system displays a red X over the attitude indicator, transmits a fault to the
integrated avionics unit, and the pilot manually selects reversionary mode on the display
controller. The technician confirms they understand the steps.

*Self-explanation prompt.* Instead of moving to the next procedure, the tutor asks: "Why does
the system require *manual* selection of reversionary mode rather than automatic switching
when the AHRS fails?" The technician retrieves what they know about certification logic and
pilot authority, proposes that automatic switching could mask intermittent faults the pilot
needs to be aware of, and the tutor reveals the canonical reason — the certification basis
treats display-source selection as a pilot-authority function, and automatic switching would
also create ambiguity about which sensor data is currently driving the symbology. The
technician restates the corrected reasoning once. The next time they encounter a
reversionary-mode question on a different airframe, the principle transfers because it is
anchored to a rule, not a memorized step.

**Manufacturing quality control — first-article inspection of a CNC-machined bracket.**

*Setup.* A quality apprentice is being trained on first-article inspection (FAI) for a
precision-machined aluminum bracket. They have just walked through the AS9102 form fields
and the CMM measurement protocol with their lead, and got every step right on the
demonstration part. The natural next move is another worked example or a re-read of the
work instruction.

*Elaborative-interrogation prompt.* The lead instead asks: "Why does the FAI process require
a separate dimensional report for the *first* part off the new fixture, when the production
parts that follow will only be sampled?" The apprentice explains, drawing on what they
already know about tooling drift and process capability — the first part validates that the
fixture, program, and tool offsets together produce a part within tolerance, so any later
sample only needs to confirm the process has not drifted. The lead confirms, adds the
regulatory layer (AS9100D requires documented first-article verification before serial
production), and asks the apprentice to restate it. On the next bracket variant the
apprentice catches a fixture-design issue during FAI because they now apply the rule, not
the form. Wong et al. (2002) is the closest analog in the literature: self-explanation
produced its largest gains on far-transfer items requiring extension of a learned principle
to new problem types.

## Quality signal

The AI tutor knows self-explanation is producing learning when learner-generated explanations on a follow-up transfer item — measured 24 hours after the prompt — exceed control-group accuracy by at least 15 percentage points (in line with the Bisra et al. 2018 g ≈ 0.55 estimate translated to a binary transfer outcome). A faster in-session signal is principle-based justification: the learner spontaneously offers a rule-anchored reason ("because the AHRS is the authoritative source for…") rather than a surface paraphrase on the second similar item without being prompted. Absence of either signal across two segments means the prompt is too easy, the prior knowledge is missing, or the canonical-answer reveal is failing to land.

## Cross-references

- See [worked-example-effect](../01-learning-science/worked-example-effect.md) for the example-study trigger that pairs most strongly with self-explanation prompts.
- See [self-explanation-prompts](../04-delivery-patterns/self-explanation-prompts.md) for the concrete delivery pattern that operationalizes the principle inside a tutoring loop.
- See [predict-before-reveal](../04-delivery-patterns/predict-before-reveal.md) for the closely related move that combines prediction with subsequent explanation.
- See [testing-effect](../01-learning-science/testing-effect.md) for retrieval, the complementary memory mechanism — combining retrieval with self-explanation produces the largest documented gains in the integrated literature.
- See [cognitive-load-theory](../01-learning-science/cognitive-load-theory.md) for the load constraint that bounds when self-explanation prompts help versus when they overwhelm.
- See [faded-worked-examples](../04-delivery-patterns/faded-worked-examples.md) for the staged transition where self-explanation gradually replaces worked steps as the learner progresses toward independent problem solving.
- See [schema-theory-knowledge-components](../01-learning-science/schema-theory-knowledge-components.md) for the prior-knowledge structure that determines whether self-explanation can land at all.
- See [error-analysis-corrective-feedback](../04-delivery-patterns/error-analysis-corrective-feedback.md) for how to handle wrong self-explanations so the canonical answer reveals the model rather than just the error.
