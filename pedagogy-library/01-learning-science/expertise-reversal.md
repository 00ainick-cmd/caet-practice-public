---
id: expertise-reversal
title: Expertise Reversal Effect
category: 01-learning-science
aliases: [expertise-reversal-effect]
evidence_strength: strong
effect_size: "Reversal point typically at ~70% accuracy on a domain competency test; Kalyuga (2007) review reports d = 0.45–2.99 across 26 studies for high-vs-low-prior-knowledge differences on the same instructional support; Tetzlaff et al. (2025) meta-analysis of 60 studies reports d = 0.505 favoring high assistance for novices and d = -0.428 favoring low assistance for experts."
key_sources:
  - "Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. Educational Psychologist, 38(1), 23-31. doi:10.1207/S15326985EP3801_4"
  - "Kalyuga, S., Chandler, P., & Sweller, J. (1998). Levels of expertise and instructional design. Human Factors, 40(1), 1-17. doi:10.1518/001872098779480587"
  - "Kalyuga, S. (2007). Expertise reversal effect and its implications for learner-tailored instruction. Educational Psychology Review, 19(4), 509-539. doi:10.1007/s10648-007-9054-3"
  - "Nievelstein, F., van Gog, T., van Dijck, G., & Boshuizen, H. P. A. (2013). The worked example and expertise reversal effect in less structured tasks: Learning to reason about legal cases. Contemporary Educational Psychology, 38(2), 118-125. doi:10.1016/j.cedpsych.2012.12.004"
  - "Renkl, A., & Atkinson, R. K. (2003). Structuring the transition from example study to problem solving in cognitive skill acquisition: A cognitive load perspective. Educational Psychologist, 38(1), 15-22. doi:10.1207/S15326985EP3801_3"
  - "Salden, R. J. C. M., Aleven, V., Schwonke, R., & Renkl, A. (2010). The expertise reversal effect and worked examples in tutored problem solving. Instructional Science, 38(3), 289-307. doi:10.1007/s11251-009-9107-8"
  - "Tetzlaff, L., Simonsmeier, B. A., Peters, T., & Brod, G. (2025). A cornerstone of adaptivity — A meta-analysis of the expertise reversal effect. Learning and Instruction, 98, 102137. doi:10.1016/j.learninstruc.2025.102137"
last_reviewed: 2026-04-29
applies_to: [acquisition, transfer, sequencing]
contraindicated_when:
  - learner_state.first_exposure
  - learner_state.pre_criterion_accuracy
  - material.high_element_interactivity_no_scaffolding
  - task_type.ill_structured_domain
runtime_triggers:
  - mastery_threshold_crossed
  - competency_check_passed
  - prior_knowledge_assessment_high
  - worked_example_redundancy_detected
  - guidance_fading_due
related: [worked-example-effect, cognitive-load-theory, faded-worked-examples, mastery-thresholds, zpd-operationalization, bayesian-knowledge-tracing, 4c-id-model, mastery-threshold-transfer-test-design]
---

# Expertise Reversal Effect

## One-line claim

Instructional techniques that help novices learn — heavy guidance, worked examples, integrated explanations — lose their effectiveness and can actively impair learning once a learner crosses a domain-specific competency threshold (commonly around 70% accuracy on a mastery test), at which point the same learner now needs to be solving problems with reduced guidance.

## Evidence base

The expertise reversal effect, named by Kalyuga, Ayres, Chandler, and Sweller (2003) in *Educational Psychologist*, is the finding that the relative effectiveness of two instructional formats can flip as learner prior knowledge in a domain grows. The effect was initially predicted by cognitive load theory as a special case of the redundancy effect: explanations and worked-out steps that are essential scaffolding for a novice become redundant — and therefore extraneous load — for a learner who already has the relevant schema. Kalyuga, Chandler, and Sweller (1998) provided the foundational empirical demonstration in *Human Factors*: trades-apprentice electricians who were novices learned more from integrated diagram-plus-text presentations than from diagrams alone, while more experienced apprentices learned more from diagrams alone — the same instructional manipulation produced opposite effects depending on prior knowledge.

Modern evidence places the effect on solid empirical ground. Kalyuga's (2007) narrative review in *Educational Psychology Review* synthesized 26 studies and reported high-vs-low-prior-knowledge effect-size differences for the same support manipulation ranging from d = 0.45 to d = 2.99, with the reversal pattern replicating across domains (electrical engineering, mathematics, physics, anatomy) and modalities (text, diagrams, multimedia, simulation). Tetzlaff, Simonsmeier, Peters, and Brod's (2025) meta-analysis in *Learning and Instruction* — 176 effect sizes from 60 experiments with 5,924 participants — confirmed the pattern at scale: high-assistance instruction beat low-assistance instruction for low-prior-knowledge learners (d = 0.505) while low-assistance beat high-assistance for high-prior-knowledge learners (d = -0.428). The effect was asymmetric: providing assistance to novices produced larger gains than withholding assistance from experts produced, which has direct operational implications for default policy when expertise is uncertain.

The principle pairs tightly with the worked example effect (see [worked-example-effect](../01-learning-science/worked-example-effect.md)). Renkl and Atkinson (2003) framed the operational sequence: present complete worked examples while learners are novices, then fade individual solution steps as expertise grows, then transition to independent problem solving. Salden, Aleven, Schwonke, and Renkl (2010) tested this in *Instructional Science* using a Cognitive Tutor for algebra; adaptively faded worked examples — fading triggered by individual student understanding rather than a fixed schedule — outperformed both fixed-schedule fading and pure problem solving. The Renkl–Atkinson sequencing rule and adaptive fading rest on a measurable expertise threshold — typically a competency test in the ~70% mastery range — at which redundant guidance flips from helpful to harmful. Boundary condition: Nievelstein, van Gog, van Dijck, and Boshuizen (2013) found no expertise reversal in less-structured domains (legal case reasoning), where worked examples remained effective for advanced learners as well; the effect is robust in well-structured procedural and conceptual domains and weaker or absent in ill-structured ones.

## When to apply

- **Mastery threshold crossed** — When a competency check shows the learner has reached approximately 70% accuracy on the
  current segment's mastery test (see [mastery-thresholds](../07-runtime-decisions/mastery-thresholds.md)), the runtime
  should fade worked-example guidance and transition the learner toward independent problem solving. The Tetzlaff et al.
  (2025) effect direction flips around this point.
- **Prior-knowledge assessment is high** — At session entry or topic entry, if a quick diagnostic places the learner above
  the redundancy threshold for this segment, default to low-assistance presentation (problems and questions) rather than
  high-assistance presentation (worked examples and integrated explanations). Kalyuga, Chandler, and Sweller (1998) showed
  experienced learners are slowed by redundant explanations.
- **Worked-example redundancy detected** — When an experienced learner expresses impatience with worked examples
  ("just let me try one"), skips ahead, or completes them faster than the model time, the runtime should treat this as a
  reversal-point signal and switch to problem solving with thinning guidance.
- **Guidance fading due** — When a faded-worked-example schedule (see
  [faded-worked-examples](../04-delivery-patterns/faded-worked-examples.md)) reaches the next fading step, route the
  learner to that step rather than re-presenting the full worked example. Salden et al. (2010) showed adaptive fading
  outperforms both fixed fading and pure problem solving.
- **Cross-segment carryover** — When a learner has crossed mastery on a prerequisite segment, do not re-present its
  worked examples when invoking the prerequisite knowledge in a downstream segment; cite or recall the result, do not
  re-explain.

## When NOT to apply

- **Learner is in first exposure to the segment** — Until a stable mental model exists, removing guidance forces the
  learner to fall back on means-ends search, which spikes extraneous load and can cement misconceptions. Keep worked
  examples and integrated explanations until the competency check confirms the threshold has been crossed (Kalyuga et al.,
  2003).
- **Pre-criterion accuracy on the current segment** — If a quick diagnostic puts the learner below ~70% mastery, the
  reversal has not yet happened; reducing guidance will degrade learning, not advance it. The asymmetry in
  Tetzlaff et al. (2025) — assistance helps novices more than independence helps experts — argues for erring toward
  guidance when expertise is uncertain.
- **High-element-interactivity material with no scaffolding** — When the current segment requires juggling many
  interacting elements simultaneously and no schema yet exists to chunk them, the expertise threshold for this segment is
  much higher than for low-interactivity material. Do not assume threshold crossing transfers from a simpler segment.
- **Ill-structured domain** — In ill-structured tasks (legal reasoning, ethical case analysis, complex clinical
  judgment), worked examples appear to remain effective for advanced learners. Nievelstein et al. (2013) found no reversal
  in legal-case reasoning. Default to maintaining example-based instruction longer in such domains.
- **Cross-domain transfer assumption** — High prior knowledge in domain X does not imply expertise in domain Y, even if
  the surface features are similar. Re-assess the current segment's mastery before fading guidance.

## How to apply

- **Pair with worked examples and use a competency check as the switch** — present complete worked examples until the
  learner reaches ~70% accuracy on a brief mastery test for that segment, then fade. Pair this chapter with
  [worked-example-effect](../01-learning-science/worked-example-effect.md); the two principles are operational complements.
- **Use adaptive fading, not a fixed schedule** — when the threshold is crossed, drop one solution step at a time rather
  than removing all guidance at once. The Renkl–Atkinson fading sequence (complete example → one step blanked → two steps
  blanked → … → bare problem) is the canonical operationalization (Renkl & Atkinson, 2003); Salden et al. (2010) found
  adaptive fading beats fixed-schedule fading.
- **Run rapid expertise diagnostics, not just final mastery tests** — a 2–4 item diagnostic at segment entry is enough to
  decide whether to start at "worked example" or "problem solving" for that segment. Kalyuga (2007) reviews several rapid
  measurement procedures including first-step-only solutions and confidence-rated retrieval.
- **Default to assistance when uncertain** — the Tetzlaff et al. (2025) asymmetry says novice-with-assistance gains
  (d = 0.505) exceed expert-without-assistance gains (d = 0.428) in absolute magnitude. When a learner's expertise on the
  current segment is ambiguous, present the worked example and let them skip it if they choose, rather than withholding
  the example.
- **Detect implicit reversal signals** — completing worked examples in less than the model time, expressed impatience,
  unsolicited self-explanation that anticipates the next step, and high accuracy on intermediate prompts all signal that
  the learner has crossed the threshold for this segment. Update the segment's expertise estimate and shift to problem
  solving (see [bayesian-knowledge-tracing](../07-runtime-decisions/bayesian-knowledge-tracing.md)).
- **Re-engage scaffolds when the learner crosses into a new sub-skill** — expertise is segment-specific. When the
  curriculum advances to a sub-skill the learner has not yet practiced, restore worked examples for that sub-skill even
  if the learner is past the threshold on the prior one. Cross-segment expertise does not transfer automatically.

## Common misapplications

- **Treating expertise as a global trait** — "This learner is advanced" is too coarse. Expertise is per-segment;
  fade guidance based on segment-specific mastery checks, not on a global skill rating or course-level performance.
- **Fading too early on an unfamiliar variant** — A learner who has mastered standard transponder ramp tests on one model
  has not necessarily mastered them on a different model with a different fault tree. Re-check before fading.
- **Removing all guidance at the threshold** — The reversal point is the boundary between "worked example" and
  "faded worked example", not between "worked example" and "bare problem". Drop one step at a time.
- **Skipping the competency check to save time** — Without a measured threshold, the runtime is guessing. Even a 3-item
  check protects against fading too early (which costs the worked-example effect) or too late (which costs the
  expertise-reversal effect). Both errors are real and both are measurable.
- **Generalizing from ill-structured to well-structured (or vice versa)** — Nievelstein et al. (2013) showed legal-case
  reasoning shows no reversal; mathematics and physics show strong reversals. Do not import the threshold or the fading
  schedule across structural classes of task.

## Examples across domains

**Avionics — adapting transponder ramp-test instruction across an apprentice's progression.**

*Setup.* An avionics apprentice has just completed a guided block on the IFR-6000 ramp test for a Mode S transponder. The
tutor has presented one fully-worked-out test sequence and walked the apprentice through it once. A 5-item competency
check covers reply-rate verification, squitter format identification, ICAO address read-back, the diplexer-failure trace
pattern, and pass/fail criteria.

*Reversal application.* The apprentice scores 4 of 5 (80%). The tutor takes this as a threshold crossing for the
"standard Mode S ramp test" segment and switches to a faded worked example: the next test sequence is presented with the
diplexer-failure diagnosis step blanked out, and the apprentice is asked to fill it in before the rest of the example
unfolds. Two sequences later, only the pass/fail decision remains; one sequence after that, the apprentice solves a full
test from a bare prompt. When the curriculum advances to ADS-B Out compliance verification — a related but distinct
sub-skill with its own fault tree — the tutor restores complete worked examples for that segment because mastery on the
prior segment does not transfer.

*Follow-up.* The next session opens with a 2-item rapid expertise diagnostic on the ADS-B Out segment. If the apprentice
scores at or above the threshold, the tutor skips the worked example for that sub-skill; if below, it presents the
worked example and re-checks after one practice attempt. Salden et al. (2010) reported adaptive fading of this kind
producing learning gains over fixed fading roughly equivalent to a half-letter-grade improvement on a posttest.

**Mortgage and financial services sales — coaching a loan officer through pricing-conversation training.**

*Setup.* A new loan officer is learning to handle the rate-shopping phase of a customer conversation: when a buyer says
"I have a quote 0.25 points lower from another lender, can you match?" The training program has presented one complete
worked example — a transcript with the senior officer's responses and an annotated explanation of why each move builds
trust, surfaces value, and protects margin. A 4-item competency check follows: identify the value-anchoring move, name
the disqualifying assumption to test, choose the correct rate-and-fee comparison framework, and select the closing pivot.

*Reversal application.* The officer scores 3 of 4 (75%). The trainer treats this as a threshold crossing for the
"rate-match objection" segment and switches to a faded example: the next role-play transcript is complete except for
the value-anchoring move, which the officer must supply before reading the rest. Two role-plays later, only the closing
pivot is omitted. By the fourth, the officer responds live to a simulated buyer with no script. When the curriculum
advances to the "appraisal-came-in-low" objection — same selling skill, different fault tree, different anchor — the
trainer restores a complete worked example because the segment-specific schema for that objection has not yet been built.

*Follow-up.* The trainer opens the next session with a 2-item rapid diagnostic on the appraisal-low segment to decide
whether to begin at "worked example" or "faded example", consistent with the Renkl and Atkinson (2003) sequencing rule
and the asymmetry Tetzlaff et al. (2025) reports — when uncertain, default to providing the example.

## Quality signal

The AI tutor knows the expertise-reversal switch is calibrated when the per-segment posttest scores of learners faded
out of worked examples at the ~70% threshold meet or exceed those of learners kept on full worked examples for the same
total time, and when the time-to-mastery for those faded learners is reduced by at least 15%. A weaker but faster signal:
on a faded example, the learner correctly fills in the omitted step on the first attempt at least 70% of the time; if
first-attempt accuracy on the omitted step falls below 50%, the fade was too aggressive and the learner had not in fact
crossed the threshold for this segment.

## Cross-references

- See [worked-example-effect](../01-learning-science/worked-example-effect.md) for the paired principle that supplies the
  default novice-phase instruction this chapter fades.
- See [cognitive-load-theory](../01-learning-science/cognitive-load-theory.md) for the theoretical mechanism — redundant
  guidance becomes extraneous load once a schema exists.
- See [faded-worked-examples](../04-delivery-patterns/faded-worked-examples.md) for the concrete delivery pattern that
  operationalizes the reversal at the segment level.
- See [mastery-thresholds](../07-runtime-decisions/mastery-thresholds.md) for the runtime rule that decides when the
  ~70% reversal point has been crossed.
- See [bayesian-knowledge-tracing](../07-runtime-decisions/bayesian-knowledge-tracing.md) for the per-segment expertise
  estimate that triggers fading without a separate competency check.
- See [zpd-operationalization](../07-runtime-decisions/zpd-operationalization.md) for the broader framework of matching
  task difficulty to current capability that the reversal threshold operationalizes.
- See [mastery-threshold-transfer-test-design](../03-assessment-science/mastery-threshold-transfer-test-design.md) for
  how to design the competency check whose result triggers the reversal.
