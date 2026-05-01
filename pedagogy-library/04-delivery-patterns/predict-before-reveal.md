---
id: predict-before-reveal
title: Predict-Before-Reveal
category: 04-delivery-patterns
aliases: [prediction-prompt, predict-explain-reveal, prequestion-prompt]
evidence_strength: strong
effect_size: "Hedges' g ≈ 0.54 specific-item benefit (St. Hilaire, Chan, & Ahn 2024 preregistered meta-analysis, k = 97); generation effect d ≈ 0.40 across 86 studies (Bertsch, Pesta, Wiscott, & McDaniel 2007 meta-analysis); prequestion specific lift confirmed in classroom video at +5 min and +24 hr (Carpenter & Toftness 2017; St. Hilaire & Carpenter 2020)"
key_sources:
  - "Carpenter, S. K., & Toftness, A. R. (2017). The effect of prequestions on learning from video presentations. Journal of Applied Research in Memory and Cognition, 6(1), 104-109. doi:10.1016/j.jarmac.2016.07.014"
  - "Brod, G. (2021). Predicting as a learning strategy. Psychonomic Bulletin & Review, 28(6), 1839-1847. doi:10.3758/s13423-021-01904-1"
  - "Brod, G., Hasselhorn, M., & Bunge, S. A. (2018). When generating a prediction boosts learning: The element of surprise. Learning and Instruction, 55, 22-31. doi:10.1016/j.learninstruc.2018.01.013"
  - "Bertsch, S., Pesta, B. J., Wiscott, R., & McDaniel, M. A. (2007). The generation effect: A meta-analytic review. Memory & Cognition, 35(2), 201-210. doi:10.3758/BF03193441"
  - "St. Hilaire, K. J., & Carpenter, S. K. (2020). Prequestions enhance learning, but only when they are remembered. Journal of Experimental Psychology: Applied, 26(4), 705-716. doi:10.1037/xap0000296"
  - "Potts, R., & Shanks, D. R. (2014). The benefit of generating errors during learning. Journal of Experimental Psychology: General, 143(2), 644-667. doi:10.1037/a0033194"
  - "St. Hilaire, K. J., Chan, J. C. K., & Ahn, D. (2024). Guessing as a learning intervention: A meta-analytic review of the prequestion effect. Psychonomic Bulletin & Review, 31(3), 919-942. doi:10.3758/s13423-023-02353-8"
last_reviewed: 2026-04-30
applies_to: [acquisition, retention]
contraindicated_when:
  - learner_state.overwhelmed
  - learner_state.first_exposure
  - learner_state.no_followup_study_window
  - material.high_element_interactivity_no_scaffolding
  - task_type.motor_acquisition
runtime_triggers:
  - new_segment_about_to_start
  - reveal_about_to_occur
  - video_or_lecture_about_to_play
  - reading_assignment_about_to_open
  - new_concept_completed
related: [pretesting-effect, testing-effect, self-explanation-prompts, error-analysis-corrective-feedback, productive-failure, desirable-difficulties, cognitive-load-theory, worked-example-effect]
---

# Predict-Before-Reveal

## One-line claim

Before exposing the canonical answer, fact, or outcome, prompt the learner to commit to a specific prediction or guess; only then reveal the correct content — the act of committing to an answer, even an incorrect one, durably improves memory for what follows.

## Evidence base

Predict-before-reveal is the runtime delivery pattern that operationalizes the family of effects in which committed generation before exposure to the canonical answer improves memory for that answer. The pattern subsumes three converging literatures: the pretesting/prequestion effect (an attempt at a not-yet-studied item followed by study; Carpenter & Toftness, 2017; St. Hilaire & Carpenter, 2020), the generation effect (self-produced material outperforms read material; Bertsch, Pesta, Wiscott, & McDaniel, 2007 meta-analytic d ≈ 0.40 across 86 studies and 445 effect sizes), and unsuccessful-retrieval/errorful-generation work showing benefits even when the learner cannot possibly know the answer (Potts & Shanks, 2014; Kornell, Hays, & Bjork, 2009 cited in [pretesting-effect](../01-learning-science/pretesting-effect.md)). St. Hilaire, Chan, and Ahn's (2024) preregistered meta-analysis of 97 specific-item estimates in *Psychonomic Bulletin & Review* placed the average advantage of a pre-content prediction-then-reveal sequence at Hedges' g ≈ 0.54 over study-only on the directly predicted material.

Brod (2021) in *Psychonomic Bulletin & Review* synthesized the mechanism in a way the runtime can act on: predicting is not merely a synonym for retrieval. Brod argues — and Brod, Hasselhorn, and Bunge (2018) in *Learning and Instruction* show with pupillometry — that committing to a prediction prepares the encoding system to register a prediction error when the canonical answer arrives, and that registered prediction error (indexed by pupil dilation in the 2018 study) is positively correlated with subsequent memory for the correct answer. The corollary is a sharp design constraint: the reveal must follow the prediction closely enough that the prediction is still active when the canonical answer lands. St. Hilaire and Carpenter's (2020) four-experiment study in *Journal of Experimental Psychology: Applied* operationalized this with a brutal boundary condition — the prequestion benefit only obtained when the learner could *remember* the prequestion at the moment of encoding the answer; learners who forgot the prequestion got no lift. Practically, this means the prediction must remain visible (or closely followed by the reveal) until the canonical answer is presented.

The principal boundary condition is that the lift is overwhelmingly specific to the predicted content. St. Hilaire et al. (2024) reported a near-zero g ≈ 0.04 effect on non-pretested material from the same lesson; Carpenter, Rahman, and Perkins (2018) replicated the specific-only pattern in classroom lessons, and Toftness, Carpenter, Lauber, and Mickes (2018) showed the effect attenuates or disappears in authentic lecture-video conditions when the predicted content is not faithfully delivered. Predict-before-reveal is a precision instrument: it strengthens memory for exactly what the learner predicted and is wasted effort for content the prediction did not target. Pair it with retrieval practice (see [testing-effect](../01-learning-science/testing-effect.md)) when downstream transfer matters.

## When to apply

- **A new segment is about to start** — Before introducing 5–15 minutes of new material, pose
  2–4 specific predictions whose answers will appear in the upcoming content (Carpenter &
  Toftness, 2017; St. Hilaire & Carpenter, 2020).
- **A reveal is about to occur** — Whenever the next move is disclosure of a fact, value,
  name, mechanism, or outcome, intercept it: ask the learner to predict first. Converts
  passive exposure into active encoding at near-zero time cost.
- **Video or lecture is about to play** — Especially valuable for passive media; Carpenter &
  Toftness (2017) showed prequestions improve memory for directly questioned video content
  and reduce mind-wandering during the presentation.
- **Reading assignment is about to open** — Inserting predictions before expository text is
  the best-replicated context. Use 2–4 predictions, each pointing at a specific fact the
  text will explicitly state.
- **New concept just completed and the next reveal compounds it** — "Given what we just
  covered, what do you think happens when X?" A prediction before the extension's reveal
  both retrieves the prior concept and primes encoding of the new one.

## When NOT to apply

- **No reveal will occur in the same session** — The canonical answer must follow within
  minutes. St. Hilaire and Carpenter (2020) showed the benefit collapses unless the learner
  can link the answer back to the prediction at encoding.
- **Learner is at first exposure to high-element-interactivity material with no schema** —
  Demanding prediction before any model exists wastes cognitive load on guessing rather than
  encoding (see [cognitive-load-theory](../01-learning-science/cognitive-load-theory.md)).
  Build schema with worked examples (see [worked-example-effect](../01-learning-science/worked-example-effect.md))
  first; predict-before-reveal becomes appropriate once partial schema is in place.
- **Learner is overwhelmed or below working-memory capacity** — Forcing an additional
  generation step on a saturated learner adds extraneous load without buying encoding
  benefit. Reduce extraneous load first.
- **Pure motor-skill execution phase** — Verbal prediction does little for the kinesthetic
  acquisition of a procedure. Apply only to declarative content embedded in motor tasks
  ("predict the torque value before I show you the spec"), not to the motor execution.
- **The "prediction" is recognition disguised as generation** — Yes/no or two-option prompts
  produce a fraction of the generation effect (Bertsch et al., 2007). Either commit to a
  specific cued-recall prediction or pick a different move.

## How to apply

- **Make the prediction commitment specific and visible** — Have the learner state or write a
  specific answer ("28 V"), not a hedge. Visible commitment is what registers the prediction
  error when the reveal lands (Brod, 2021; Brod, Hasselhorn, & Bunge, 2018).
- **Reveal within seconds-to-minutes of the prediction** — St. Hilaire and Carpenter (2020)
  showed the benefit only obtains when the learner can still bring the prediction to mind
  at the moment of the reveal. Keep the prediction on screen until the reveal.
- **Pair the prediction visually with the reveal** — Present "your guess: X / correct: Y"
  side-by-side. The juxtaposition is what makes the prediction error available for
  processing; without it the canonical answer overwrites the guess silently.
- **Frame errors as the point** — "Most of these you won't know — that's the design. Take
  your best shot." Potts and Shanks (2014) showed the generation benefit holds even when the
  learner cannot possibly know the answer; framing removes the impulse to skip rather than
  guess.
- **Target one specific fact per prediction; use 2–4 per segment** — The benefit is item-
  specific (St. Hilaire et al., 2024). Pick the 2–4 highest-stakes facts; do not spread
  predictions thin across details that don't matter for the downstream criterion.
- **Follow with retrieval, not just exposure** — A prediction-then-reveal builds encoding;
  pair it with posttest retrieval (see [testing-effect](../01-learning-science/testing-effect.md))
  to consolidate retention and support transfer to untested items.

## Common misapplications

- **Revealing without making the prediction visible** — If the canonical answer is presented
  without surfacing the learner's prediction next to it, prediction error has no surface to
  land on. The Brod (2021) mechanism requires the contrast between predicted and actual at
  encoding; silent reveals discard it.
- **Long delay between prediction and reveal** — St. Hilaire and Carpenter (2020) found the
  benefit disappears entirely when the learner cannot remember the prediction at encoding.
  A 30-second gap with intervening content can wipe out the effect.
- **Treating "guess and reveal" as a substitute for instruction** — Predict-before-reveal is
  an encoding amplifier on sound instruction. It does not replace explanation, modeling, or
  worked examples for novel concepts.
- **Multiple-choice prediction with obvious answers** — Recognition with a process-of-
  elimination giveaway is not generation. Commit to a free-response or specific cued-recall
  prompt, or write distractors close enough that the learner has to commit.
- **Expecting general spillover to non-predicted content** — The g ≈ 0.04 general effect
  (St. Hilaire et al., 2024) is functionally zero. Predict-before-reveal targets only the
  items the prediction named; everything else needs separate retrieval practice.

## Examples across domains

**Avionics — calibrating an attitude heading reference system (AHRS) on the bench.**

*Setup.* A technician is about to read the calibration procedure for a Garmin GRS 77 AHRS
unit during a heading-error troubleshoot. They have used the unit operationally but never
walked through bench calibration. The procedure document opens with the magnetometer
alignment values, the post-installation hard/soft iron compensation steps, and the
acceptable residual error after calibration.

*Prediction prompt.* Before the document opens, the tutor asks three specific predictions
each tied to a value the document will state explicitly: (1) "What residual heading error
in degrees does the post-cal acceptance criterion allow?"; (2) "On which axis (X, Y, or Z)
must the bench-mount fixture be leveled to within 0.5 degrees before calibration starts?";
(3) "What ambient magnetic-field disturbance threshold (in milligauss) will cause the
calibration to abort?" The technician commits a specific number to each — typical guesses
are "1 degree," "Z axis," "100 mG," none exactly right.

*Reveal and follow-up.* The document opens with the technician's three guesses pinned at
the top of the screen. As each canonical value appears in the procedure, the tutor pulls
the corresponding guess down next to it side-by-side ("your guess: 1° / correct: 0.5°") so
the prediction error registers at encoding (Brod, 2021). The reveal happens within 90
seconds of the prediction so the prediction is still in working memory (St. Hilaire &
Carpenter, 2020). A retrieval pass on the same three values plus two transfer questions
("would a 0.7° residual pass on a non-pitch-stabilized installation? why or why not?")
runs at the end of the session and again at +24 hours via spaced retrieval (see
[testing-effect](../01-learning-science/testing-effect.md)).

**Culinary apprenticeship — first encounter with classical French mother sauces.**

*Setup.* An apprentice cook is about to read a 15-minute reference on the five French
mother sauces (béchamel, velouté, espagnole, sauce tomate, hollandaise). They have made
sauces on the line but never formally studied the classification. The reference will name
each mother sauce, its base liquid, its thickening agent, and one canonical derivative.

*Prediction prompt.* Before opening the reference, the tutor asks four specific
predictions whose answers all appear verbatim in the document: (1) "What thickening agent
defines a velouté — flour roux, egg yolk, or butter emulsion?"; (2) "Which mother sauce is
the parent of sauce béarnaise?"; (3) "What single base liquid is shared by velouté and
espagnole?"; (4) "Which mother sauce uses no thickening agent at all?" The apprentice
commits a specific answer to each — typically gets one or two right and guesses on the
rest, the errorful-generation pattern Potts and Shanks (2014) studied.

*Reveal and follow-up.* The reference opens with the apprentice's four guesses visible.
Each canonical answer is presented next to the corresponding guess so the contrast lands
at encoding. The instructor pauses on the wrong predictions to make the mechanism
explicit ("you guessed butter emulsion — that's hollandaise; velouté is roux-thickened
because it's stock-based, not emulsion-based"). Within the same shift, the apprentice
makes a velouté on the line and is quizzed (retrieval, not prediction) on the four facts
again; a third pass at the start of the next shift, +24 hours later, closes the spacing
loop and converts the specific-item lift into durable retention.

## Quality signal

The runtime knows predict-before-reveal is producing learning when, on a delayed
posttest at +24 hours, accuracy on directly predicted items exceeds accuracy on matched
non-predicted items from the same segment by Hedges' g > 0.4 — within the band St.
Hilaire et al. (2024) and Bertsch et al. (2007) predict for the specific effect. A
faster in-session signal: on an immediate posttest after the segment, accuracy on
predicted items should exceed non-predicted matched items by ≥ 10 percentage points;
a smaller gap means either the prediction was too vague (recognition rather than specific
generation) or the reveal was not paired with the prediction visibly enough for prediction
error to register.

## Cross-references

- See [pretesting-effect](../01-learning-science/pretesting-effect.md) for the underlying learning-science principle predict-before-reveal operationalizes at the delivery level.
- See [testing-effect](../01-learning-science/testing-effect.md) for the post-encoding retrieval operation that complements prediction and dominates it on transfer measures.
- See [self-explanation-prompts](../04-delivery-patterns/self-explanation-prompts.md) for the closely related delivery pattern that follows reveals (rather than precedes them) with elaboration.
- See [error-analysis-corrective-feedback](../04-delivery-patterns/error-analysis-corrective-feedback.md) for how to handle the wrong predictions this pattern reliably produces.
- See [productive-failure](../04-delivery-patterns/productive-failure.md) for the broader pedagogical frame in which committed wrong attempts before the canonical answer accelerate learning.
- See [cognitive-load-theory](../01-learning-science/cognitive-load-theory.md) for the load constraints that determine when prediction prompts help versus harm encoding.
- See [worked-example-effect](../01-learning-science/worked-example-effect.md) for the alternative front-of-segment move when the learner has no schema yet and prediction would be premature.
