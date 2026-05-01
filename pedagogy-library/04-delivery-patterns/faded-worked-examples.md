---
id: faded-worked-examples
title: Faded Worked Examples
category: 04-delivery-patterns
aliases: [example-fading, backward-fading, completion-problems, guidance-fading]
evidence_strength: strong
effect_size: "Medium-to-large effects on near and far transfer when fading is paired with self-explanation prompts (Atkinson, Renkl & Merrill 2003, two experiments, partial-eta-squared 0.10–0.21 for transfer); adaptive fading outperforms fixed fading and unaided problem solving in Cognitive Tutor classrooms (Salden et al. 2010)"
key_sources:
  - "Renkl, A., & Atkinson, R. K. (2003). Structuring the transition from example study to problem solving in cognitive skill acquisition: A cognitive load perspective. Educational Psychologist, 38(1), 15-22. doi:10.1207/S15326985EP3801_3"
  - "Renkl, A., Atkinson, R. K., Maier, U. H., & Staley, R. (2002). From example study to problem solving: Smooth transitions help learning. The Journal of Experimental Education, 70(4), 293-315. doi:10.1080/00220970209599510"
  - "Atkinson, R. K., Renkl, A., & Merrill, M. M. (2003). Transitioning from studying examples to solving problems: Effects of self-explanation prompts and fading worked-out steps. Journal of Educational Psychology, 95(4), 774-783. doi:10.1037/0022-0663.95.4.774"
  - "Renkl, A., & Atkinson, R. K. (2004). How fading worked solution steps works — A cognitive load perspective. Instructional Science, 32(1-2), 59-82. doi:10.1023/B:TRUC.0000021815.74806.f6"
  - "Salden, R. J. C. M., Aleven, V., Schwonke, R., & Renkl, A. (2010). The expertise reversal effect and worked examples in tutored problem solving. Instructional Science, 38(3), 289-307. doi:10.1007/s11251-009-9107-8"
  - "Renkl, A. (2014). Toward an instructionally oriented theory of example-based learning. Cognitive Science, 38(1), 1-37. doi:10.1111/cogs.12086"
  - "Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. Educational Psychologist, 38(1), 23-31. doi:10.1207/S15326985EP3801_4"
last_reviewed: 2026-04-30
applies_to: [acquisition, transfer, sequencing]
contraindicated_when:
  - learner_state.first_exposure
  - learner_state.pre_criterion_accuracy
  - material.high_element_interactivity_no_scaffolding
  - task_type.motor_acquisition
runtime_triggers:
  - new_problem_type_introduced
  - worked_example_completed
  - guidance_fading_due
  - mastery_threshold_crossed
  - completion_problem_required
related: [worked-example-effect, expertise-reversal, cognitive-load-theory, self-explanation-prompts, self-explanation-elaborative-interrogation, mastery-thresholds, bayesian-knowledge-tracing, predict-before-reveal]
---

# Faded Worked Examples

## One-line claim

Replace the abrupt jump from studying a complete worked example to solving a bare problem with a graded sequence of completion problems — first the last solution step blanked, then the last two, then the last three — so the learner takes responsibility for the procedure step by step in the same order an expert would relinquish it, with self-explanation prompts at each blanked step.

## Evidence base

Faded worked examples are the operational sequencing rule that converts the static worked-example-effect into a per-segment instructional schedule. Renkl, Atkinson, Maier, and Staley (2002), in *The Journal of Experimental Education*, ran the foundational experiments across three samples (20 ninth-graders in Germany, 54 and 45 U.S. college students) on probability problems and showed that successive integration of problem-solving elements into example study — complete example, then example with one step blanked, then two steps, until the learner is solving the bare problem — produced higher near-transfer than the conventional example-problem-pair schedule. A subsequent experiment localized the mechanism: the position of the faded step did not matter, but learners learned most about the principles whose steps were faded, suggesting that the act of generating the missing step triggers principle-level self-explanation rather than passive surface re-reading. Renkl and Atkinson (2003), in the companion *Educational Psychologist* paper, framed the cognitive-load account: intrinsic load decreases as a learner's schema stabilizes, so the schedule that minimizes extraneous load shifts from full-example presentation toward independent problem solving, with completion problems bridging the two regimes.

Modern evidence consolidates the schedule and characterizes its boundary conditions. Atkinson, Renkl, and Merrill (2003) in the *Journal of Educational Psychology* tested fading alone against fading combined with self-explanation prompts at each blanked step; across two experiments the combination produced medium-to-large gains on both near and far transfer without increasing time on task, while fading without prompts replicated only the near-transfer advantage. Renkl and Atkinson (2004) in *Instructional Science* compared backward fading (last step blanked first) against forward fading (first step blanked first) and found backward fading produced fewer problem-solving errors during learning and better transfer. Salden, Aleven, Schwonke, and Renkl (2010), running two experiments in *Instructional Science* with the Cognitive Tutor for algebra, showed adaptive fading — triggered by per-segment competency rather than a fixed schedule — outperformed both fixed-schedule fading and pure tutored problem solving on conceptual and procedural transfer. Renkl's (2014) integrative theory in *Cognitive Science* identifies self-explanation activity at each blanked step as the principal mediator: the gap between full example and bare problem is what forces the learner to retrieve and articulate the missing principle, and that articulation is what builds transferable schema.

The principal boundary condition is the expertise gradient itself, codified as the expertise reversal effect (Kalyuga, Ayres, Chandler & Sweller, 2003). Fading too slowly past a stable schema produces redundant guidance and slows learning; fading too quickly before the schema has formed produces means-ends search and recreates the load problem worked examples were designed to avoid. The operative move is to anchor the fading rate to a measurable per-segment competency, typically a brief mastery check around 70% accuracy, and to fade adaptively rather than on a fixed calendar (Salden et al., 2010).

## When to apply

- **New problem type just introduced and one full worked example studied** — Once the learner has
  studied at least one complete worked example with self-explanation, the next item in the
  sequence is a completion problem with the last solution step blanked, not another full example
  and not a bare problem. Renkl, Atkinson, Maier & Staley (2002) frame this as the bridge step.
- **Worked example just completed and learner correct on the prompted self-explanations** — If
  the learner has explained why each step was taken at full-example study, fade the next item by
  one step. Continued full-example study at this point starts to drift toward the expertise
  reversal regime (Kalyuga et al., 2003).
- **Guidance fading due on the segment's schedule** — When a per-segment fading schedule (one
  more step blanked per pass) reaches the next step, present the next-faded item rather than
  re-presenting the prior level. Salden et al. (2010) showed adaptive fading outperforms both
  fixed fading and pure problem solving in Cognitive Tutor classrooms.
- **Per-segment mastery threshold crossed** — When a brief competency check signals the learner
  has crossed roughly 70% accuracy on the current segment, advance the fade rather than holding
  at the current level (see [mastery-thresholds](../07-runtime-decisions/mastery-thresholds.md)).
- **Completion problem required by curriculum step** — When the curriculum specifies a
  completion problem (one or more steps blanked) rather than a full example or a bare problem,
  this principle is the design rationale; pair it with a self-explanation prompt at each blanked
  step (Atkinson, Renkl & Merrill, 2003).

## When NOT to apply

- **Learner is in first exposure to the segment** — Before any full worked example has been
  studied for the current problem type, fading does not apply: there is nothing yet to fade.
  Present a complete worked example with self-explanation prompts first
  (see [worked-example-effect](../01-learning-science/worked-example-effect.md)).
- **Pre-criterion accuracy on the current segment** — If a quick diagnostic shows the learner
  below ~70% mastery on the segment, fading the next step accelerates failure rather than
  building schema. Salden et al. (2010) explicitly tied fading to per-segment understanding;
  Atkinson, Renkl & Merrill (2003) treat principle-level self-explanation success as the gate.
- **High element interactivity with no schema yet** — When the procedure involves many
  interacting elements that must be coordinated and the learner has not yet built a chunking
  schema, blanking even one step recreates the means-ends search the worked-example principle
  was designed to bypass (Renkl & Atkinson, 2003). Maintain full examples until a schema exists.
- **Pure motor-acquisition phase** — The principle is operative for declarative and conceptual
  procedures (problem-solving sequences, decision trees, reasoning chains). For motor execution
  itself (soldering, knot-tying, free-throw motion), faded examples cannot substitute for the
  physical practice and kinesthetic feedback that motor learning requires.
- **Far-transfer is the only goal and self-explanation prompts are not in the design** —
  Atkinson, Renkl & Merrill (2003) showed fading without self-explanation prompts replicated
  only near-transfer gains; for far transfer, the prompts are not optional. Without them, prefer
  pairing fading with a separate elaboration mechanism rather than running fading alone.

## How to apply

- **Use backward fading by default** — Blank the last step first, then the last two, then the
  last three, until the learner is solving the bare problem. Renkl and Atkinson (2004) showed
  backward fading produced fewer learning-time errors and better transfer than forward fading,
  and the Renkl–Atkinson (2003) cognitive-load account predicts this: keeping the early
  scaffolded steps preserves the schema-building anchor while the learner takes on the
  principle-application steps.
- **Insert a self-explanation prompt at every blanked step** — At each blanked step, prompt the
  learner to articulate the principle the missing step instantiates before they fill it in.
  Atkinson, Renkl & Merrill (2003) demonstrated this is what extends the fading benefit from
  near transfer to far transfer; see
  [self-explanation-prompts](../04-delivery-patterns/self-explanation-prompts.md).
- **Trigger the next fade adaptively, not on a fixed schedule** — When the learner correctly
  fills the currently-blanked step on the first attempt, advance the fade by one more step on
  the next item. When the learner fails the blanked step, return to a less-faded item rather
  than continuing forward. Salden et al. (2010) showed this outperformed both fixed fading and
  pure problem solving in classroom Cognitive Tutor deployments.
- **Pair with a per-segment competency check before the first fade** — Run a 2–4-item rapid
  diagnostic (Kalyuga, 2007) to confirm the learner has reached roughly 70% mastery on the
  current segment before initiating fading. Below the threshold, return to full worked examples
  rather than fading.
- **Stop the schedule once the learner is solving bare problems unaided** — Two consecutive
  bare-problem successes is the operative trigger to exit the fading schedule for this segment
  and switch to interleaved problem-solving practice (see
  [expertise-reversal](../01-learning-science/expertise-reversal.md)). Continued example
  presentation past this point produces redundant guidance.
- **Restart the fading schedule for each new sub-skill** — Expertise is per-segment. When the
  curriculum advances to a sub-skill the learner has not yet practiced (different fault tree,
  different problem class), reset to a full worked example for that sub-skill regardless of
  mastery on the prior one (Salden et al., 2010).

## Common misapplications

- **Skipping the self-explanation prompt at the blanked step** — A blanked step the learner
  fills in silently is a fraction of the move studied with explicit prompts to articulate the
  principle. Atkinson, Renkl & Merrill (2003) found the prompt was the difference between
  near-only-transfer fading and near-and-far-transfer fading; treat the prompt as required, not
  optional.
- **Forward fading instead of backward fading** — Blanking the first step first leaves the
  learner without the procedural anchor needed to evaluate whether their generated first step is
  on track. Renkl and Atkinson (2004) showed forward fading produced more learning-time errors;
  default to backward fading absent a specific reason.
- **Fading on a fixed schedule rather than to per-segment competency** — The same calendar
  applied to every learner over-paces some and under-paces others. Salden et al. (2010) found
  adaptive fading beat fixed fading in two experiments; route to the next fade level on
  per-segment success, not on elapsed time or item count.
- **Treating fading as a substitute for full worked examples on first exposure** — A faded
  example presented before any complete example has been studied is just a partially worked
  problem with no schema to anchor it. The fade is the second move in the schedule, not the
  first.
- **Fading past the bare-problem point without exiting the schedule** — Once the learner is
  solving bare problems unaided on this segment, the fading schedule has done its work. Continued
  example presentation is now expertise-reversal territory (Kalyuga et al., 2003); switch to
  interleaved problem solving rather than re-introducing examples.

## Examples across domains

**Avionics — Garmin GTX 345 transponder install on a Cessna 172, transitioning from full worked example to bare-problem competency.**

*Setup.* A first-year apprentice has just completed one full worked example for the GTX 345 install: the tutor walked through the connector pinout, the ICAO-address strap-pin pattern decoded against the aircraft's hex code, the ARINC 429 wire labels, and the squat-switch ground decision, with self-explanation prompts at each non-obvious step. A 4-item competency check shows 75% accuracy on the principles. The apprentice is past the threshold; the next move is not another full example and not a bare install, but a backward-faded completion problem.

*Faded sequence.* On the second airframe (a Piper PA-28), the worked example is presented complete except the last step — the squat-switch ground decision — which is blanked. The tutor prompts: "Why is the squat-switch ground left open or grounded on this airframe — what's the principle?" The apprentice articulates the rule (open on retractable-gear airframes, grounded on fixed-gear with a specific weight-on-wheels signal) and fills in the step. On the third airframe, the last two steps are blanked: the apprentice supplies both the squat-switch decision and the ARINC 429 input port assignment. On the fourth, the last three steps are blanked. By the fifth, the apprentice produces the install package from a bare prompt, which is the exit trigger.

*Adaptive control and follow-up.* If the apprentice fails the blanked step on any item, the tutor returns to a less-faded item before advancing rather than holding at the failed level. When the curriculum advances to ADS-B Out compliance verification — a related sub-skill with its own fault tree — the schedule resets to a full worked example for that segment, consistent with Salden et al. (2010) and the per-segment expertise rule from Kalyuga et al. (2003). Self-explanation prompts at each blanked step throughout, per Atkinson, Renkl & Merrill (2003).

**L2 (second-language) acquisition — an intermediate Spanish learner mastering the subjunctive in noun clauses with verbs of doubt.**

*Setup.* An adult intermediate learner of Spanish has just been introduced to the subjunctive in noun clauses governed by verbs of doubt ("dudar que," "no creer que," "es dudoso que…"). The tutor presents one complete worked example: "Dudo que ella tenga tiempo." The construction is unpacked step by step — the matrix verb of doubt, the subordinator "que," the subjunctive form "tenga," and the principle that doubt in the matrix triggers subjunctive in the embedded clause. Self-explanation prompts elicit the principle at each step. A 4-item recognition check shows the learner identifies subjunctive triggers correctly on 3 of 4.

*Faded sequence.* The next item is a backward-faded completion problem: "No creo que él ___ (saber) la respuesta." The matrix-verb identification, the subordinator, and the principle are visible; only the conjugation of "saber" into "sepa" is blanked. The tutor prompts: "Why does this slot take subjunctive — what's the rule?" The learner articulates "doubt in the matrix triggers subjunctive in the embedded clause" and supplies "sepa." The next item blanks both the conjugation and the form selection rationale. The next blanks the subordinator selection too. By the fifth item the learner produces a full subjunctive sentence from an English prompt with no scaffolding.

*Adaptive control and follow-up.* When the learner fails the blanked conjugation on a stem-changing verb, the tutor returns to a less-faded item with a regular verb before advancing. When the curriculum moves to a different trigger class (verbs of emotion: "alegrarse de que," "temer que…"), the schedule resets to a complete worked example for that class — the per-segment expertise rule, since the trigger semantics differ even though the morphology is shared (Kalyuga et al., 2003; Salden et al., 2010). Self-explanation prompts at every blanked step throughout, per Atkinson, Renkl & Merrill (2003), which is what extends the gains beyond near transfer.

## Quality signal

The fading schedule is producing learning when (a) first-attempt accuracy on the currently-blanked step exceeds 70% — Salden et al. (2010) tie this to the adaptive-fading trigger, and Atkinson, Renkl & Merrill (2003) report transfer effects in this range — and (b) when the learner advances from full example to bare problem in fewer total items than a fixed example-problem-pair schedule for the same segment. A faster signal: principle-level articulation at the blanked step. If the learner can fill in the missing step but cannot state the principle that justifies it, the self-explanation prompt is failing to activate the mediator and the fading benefit is reverting to the near-transfer-only pattern Atkinson, Renkl & Merrill (2003) document for fading without prompts.

## Cross-references

- See [worked-example-effect](../01-learning-science/worked-example-effect.md) for the underlying acquisition principle that this delivery pattern operationalizes across the expertise gradient.
- See [expertise-reversal](../01-learning-science/expertise-reversal.md) for the boundary condition the fading schedule is designed to manage — redundant guidance becomes extraneous load once a schema exists.
- See [cognitive-load-theory](../01-learning-science/cognitive-load-theory.md) for the theoretical mechanism — fading manages intrinsic and extraneous load as the learner's schema stabilizes.
- See [self-explanation-prompts](../04-delivery-patterns/self-explanation-prompts.md) for the prompt patterns that activate the principal mediator at each blanked step.
- See [self-explanation-elaborative-interrogation](../01-learning-science/self-explanation-elaborative-interrogation.md) for the broader why-question literature that the prompt-at-each-blanked-step rule rests on.
- See [mastery-thresholds](../07-runtime-decisions/mastery-thresholds.md) for the per-segment competency check that triggers the next fade level.
- See [bayesian-knowledge-tracing](../07-runtime-decisions/bayesian-knowledge-tracing.md) for the per-segment expertise estimate that supports adaptive (rather than fixed) fading.
- See [predict-before-reveal](../04-delivery-patterns/predict-before-reveal.md) for the closely related delivery pattern that converts a single step into a generative retrieval at minimal time cost.
