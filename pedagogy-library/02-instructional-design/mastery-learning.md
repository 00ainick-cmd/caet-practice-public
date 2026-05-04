---
id: mastery-learning
title: Mastery Learning
category: 02-instructional-design
aliases: [bloom-mastery-learning, learning-for-mastery]
evidence_strength: strong
effect_size: "Cohen's d ≈ 0.5 on aligned criterion measures (Kulik, Kulik, & Bangert-Drowns 1990 meta-analysis of 108 studies; Hattie 2009 reports d = 0.57). The Bloom 2-sigma claim is excluded; this chapter uses the conservative modern estimate per Guskey (2010)."
key_sources:
  - "Bloom, B. S. (1968). Learning for mastery. *Evaluation Comment*, 1(2), 1-12. (Center for the Study of Evaluation of Instructional Programs, UCLA)."
  - "Guskey, T. R. (2010). Lessons of mastery learning. *Educational Leadership*, 68(2), 52-57."
  - "Kulik, C. C., Kulik, J. A., & Bangert-Drowns, R. L. (1990). Effectiveness of mastery learning programs: A meta-analysis. *Review of Educational Research*, 60(2), 265-299. doi:10.3102/00346543060002265"
  - "Guskey, T. R., & Pigott, T. D. (1988). Research on group-based mastery learning programs: A meta-analysis. *Journal of Educational Research*, 81(4), 197-216. doi:10.1080/00220671.1988.10885824"
  - "Block, J. H., & Burns, R. B. (1976). Mastery learning. *Review of Research in Education*, 4, 3-49. doi:10.3102/0091732X004001003"
  - "Slavin, R. E. (1987). Mastery learning reconsidered. *Review of Educational Research*, 57(2), 175-213. doi:10.3102/00346543057002175"
  - "Guskey, T. R. (2007). Closing achievement gaps: Revisiting Benjamin S. Bloom's 'Learning for Mastery'. *Journal of Advanced Academics*, 19(1), 8-31. doi:10.4219/jaa-2007-704"
last_reviewed: 2026-04-29
applies_to: [acquisition, retention, sequencing, decision]
contraindicated_when:
  - material.unstable_target_specification
  - task_type.exploratory_inquiry_emergent_outcomes
  - learner_state.fixed_calendar_no_remediation_window
runtime_triggers:
  - unit_design_started
  - formative_assessment_completed
  - mastery_threshold_evaluated
  - corrective_cycle_required
  - second_assessment_scheduled
related: [backward-design-ubd, mastery-thresholds, mastery-threshold-transfer-test-design, error-analysis-corrective-feedback, testing-effect, spaced-retrieval, pre-post-assessment-effect-size, gagnes-nine-events, merrills-first-principles]
---

# Mastery Learning

## One-line claim

Hold the criterion fixed and let time vary: organize instruction into short units, after each unit administer a formative check, and require any learner below the mastery threshold to receive method-change corrective instruction and a second parallel assessment before advancing.

## Evidence base

Bloom (1968) reframed Carroll's model of school learning into a teaching strategy: if aptitude is mostly the *time* a learner needs to reach a fixed criterion, then holding instructional time constant guarantees variation in achievement, while holding the criterion constant and varying time produces near-uniform mastery. The strategy specified four operative moves — diagnostic pre-assessment, short instructional units (one to two weeks), a formative ("Formative A") assessment after each unit, and corrective instruction plus a second parallel ("Formative B") assessment for any learner below threshold (Bloom, 1968, *Evaluation Comment*, pp. 4-9). Block and Burns (1976) reviewed the first decade of trials in *Review of Research in Education* and identified two distinct implementations — Bloom's group-based "Learning for Mastery" (LFM) and Keller's individually-paced "Personalized System of Instruction" (PSI) — both producing reliable achievement gains over conventional instruction across 27 retention studies running 5 weeks to 15 months.

Modern meta-analytic evidence sets the effect at approximately d = 0.5 on aligned criterion measures, well below Bloom's original 2-sigma claim but durable across grade levels and content. Kulik, Kulik, and Bangert-Drowns (1990) synthesized 108 controlled evaluations and reported a mean examination-score gain of 0.50 standard deviations (LFM and PSI combined; range 0.50-0.58 across subgroups), with stronger effects for weaker students within a class (*RER*, 60(2), pp. 274-278). Guskey and Pigott (1988) meta-analyzed 46 group-based studies and confirmed consistent positive effects on achievement, retention, and student affect regardless of class size. Hattie (2009) placed mastery learning at d = 0.57 in *Visible Learning*, above the 0.40 hinge across roughly 800 meta-analyses. Guskey (2010, pp. 53-55) treated this conservative effect as the contemporary baseline and traced Response-to-Intervention, formative-assessment practice, and standards-based grading back to Bloom's original four moves.

Two boundary conditions are well-documented. Slavin (1987) ran a best-evidence synthesis and found that group-based mastery learning produced essentially zero effect on standardized achievement tests despite the gains on experimenter-made measures (*RER*, 57(2), pp. 175-200); Anderson and Burns (1987) and Kulik et al. (1990) responded that the mismatch between an aligned criterion test and a generic standardized test is itself the point of mastery learning, not a flaw in the evidence. The second boundary is structural: mastery learning requires a calendar with slack for correctives. When the schedule cannot bend, holding the criterion fixed forces some learners off the back of the unit and the strategy degrades into ordinary instruction with extra grading. The chapter treats both as scope conditions rather than disqualifications.

## When to apply

- **Unit design started for hierarchical content** — When downstream content depends on earlier
  content (algebra before calculus, ohm's law before troubleshooting, regulations before
  installation), structure the unit on Bloom's four moves: pre-assessment, short segments,
  Formative A, correctives, Formative B. Hierarchical dependencies are where the largest
  mastery effects appear (Kulik et al., 1990, pp. 280-283).
- **Formative assessment completed and learners are below threshold** — A Formative A result
  showing any learner under the mastery threshold (typically 80-90% on the unit's criterion
  test) is the runtime trigger for corrective instruction; without a corrective branch the
  strategy collapses into ordinary instruction.
- **Mastery threshold evaluated and the unit gates the next** — When the current unit is a
  prerequisite for downstream content, do not advance below-threshold learners on time. Issue
  correctives plus a Formative B before advancement (Guskey, 2010, pp. 54-55).
- **Corrective cycle required** — When errors on Formative A cluster around identifiable
  sub-skills (not random), correctives that target *those* sub-skills with a different
  instructional approach produce reliable gains; same-method re-teaching does not (Guskey,
  2007, pp. 18-22).
- **Long-delay retention is the criterion** — Block and Burns (1976) reported d ≈ 0.67 retention effects across 27 studies running 5 weeks to 15 months when correctives were enforced; for any program where the learner must retain across that horizon (certification, fieldwork, downstream coursework), mastery learning is the right organizing strategy.
- **Achievement-gap reduction is an explicit goal** — Effects are largest for the lowest pre-test quartile (Kulik et al., 1990; Guskey, 2007), the population that least tolerates a fixed-time / variable-criterion structure.

## When NOT to apply

- **Target performance cannot be specified concretely enough to write a criterion test** —
  Mastery learning depends on a Stage-2 evidence specification (see
  [backward-design-ubd](../02-instructional-design/backward-design-ubd.md)). If "what counts
  as mastery" cannot be operationalized as observable criteria, the threshold is fictional and
  the Formative A/B cycle has nothing to discriminate against.
- **Open-ended exploratory or creative inquiry** — When the desired outcome is divergent
  generation, novel synthesis, or genuine discovery, a fixed criterion is the wrong target;
  forcing a mastery threshold here produces convergence on the assessor's expected answer
  rather than the inquiry the activity was meant to provoke.
- **Schedule has no remediation slack** — A class or program on a fixed calendar with no
  time allocated for correctives and a re-test cannot run mastery learning; the strategy
  degrades to "we noticed you didn't pass and moved on anyway." Either rebuild the calendar
  to include correctives or pick a different organizing strategy.
- **Material is a small set of isolated facts with no transfer demand** — Memorizing a
  resistor color code or a phonetic alphabet does not need a mastery cycle around it;
  retrieval and spacing ([testing-effect](../01-learning-science/testing-effect.md),
  [spaced-retrieval](../01-learning-science/spaced-retrieval.md)) carry the load and the unit
  structure adds overhead without payoff.
- **The summative measure is a generic standardized test misaligned with the unit's criterion** — Slavin (1987) showed effects collapse on misaligned generic tests; if the high-stakes measure is misaligned, fix the alignment ([validity-reliability](../03-assessment-science/validity-reliability.md)) before investing in a mastery cycle that will not move the metric being judged on.

## How to apply

- **Specify the mastery threshold as an observable, defensible criterion before authoring the
  unit** — Pick the level (typically 80-90% on the criterion test) using
  [mastery-thresholds](../07-runtime-decisions/mastery-thresholds.md). The threshold is a
  decision rule, not an aspiration; the runtime must be able to evaluate it without judgment
  calls.
- **Decompose the unit into one- to two-week segments** — Bloom (1968) and Guskey (2010) are
  explicit on length: longer units accumulate too many sub-skill failures to diagnose;
  shorter ones fragment the content. One to two weeks is the empirical sweet spot in the
  meta-analytic studies.
- **Author Formative A and Formative B as parallel forms aligned to the unit's criterion** —
  Same blueprint, same difficulty, different items. Without parallel forms the second
  assessment measures item memorization rather than mastery; with them, it measures whether
  the corrective produced learning. See
  [pre-post-assessment-effect-size](../03-assessment-science/pre-post-assessment-effect-size.md)
  for the alignment discipline.
- **Plan correctives by error pattern using a different instructional method, not a
  re-teach** — Guskey (2007, 2010) is emphatic: correctives must use a *different* approach
  than the original lesson — worked example after explanation, hands-on after diagram, peer
  tutoring after solo practice. Same-method re-teaching produces small or null gains;
  method-change correctives produce the meta-analytic effect. See
  [error-analysis-corrective-feedback](../04-delivery-patterns/error-analysis-corrective-feedback.md).
- **Schedule Formative B 1-3 days after correctives, with a +7-to-+14-day spaced check** —
  Use [spaced-retrieval](../01-learning-science/spaced-retrieval.md) to confirm the threshold
  held over a standard forgetting interval rather than over an hour. Without the spaced
  check, "mastery" is indistinguishable from short-term cramming.
- **Use Formative A diagnostically, not summatively** — No grade, no rank-order; just a classification of which sub-skills are below threshold for whom. Treating Formative A as a summative grade collapses the strategy back to conventional grading and destroys the diagnostic signal the corrective cycle depends on.
- **Provide enrichment for at-threshold learners** — While below-threshold learners receive correctives, at-threshold learners need substantive extension activities, not busywork (Guskey, 2010, pp. 55-56). Without this, the strategy creates a perverse incentive to underperform on Formative A.

## Common misapplications

- **Calling repeated re-testing "mastery learning"** — A unit where learners may take the same test until they pass, with no diagnostic, no correctives, and no parallel forms, is a retesting policy. Without correctives the only mechanism left is item memorization (Guskey, 2010, p. 53).
- **Holding time constant and pretending the criterion varied** — A unit that ends on a fixed date and reports each learner's percentage is conventional instruction even if it uses the language of mastery. The defining move is letting time vary; without that, nothing is varying.
- **Same-method re-teaching as "correctives"** — Re-running the original lesson with louder voice or slower pace is the most common implementation failure (Guskey, 2007); the meta-analytic effect requires a *different* instructional approach, not the same lesson at a different volume.
- **Confusing the mastery threshold with the Bloom 2-sigma claim** — The 2σ tutoring effect has not replicated under modern conditions and is excluded from this library (see README "Deliberately excluded"). The 0.5σ effect in Kulik et al. (1990) and Hattie (2009) is the empirically defensible estimate; treating mastery learning as a 2σ intervention overpromises and undermines the evidence base.
- **Skipping Formative B to save calendar time** — Without the second parallel assessment the corrective cycle is open-loop. Learners exit the unit with no evidence the corrective worked, and downstream content built on the unit fails for diagnosable reasons.
- **Treating the threshold as negotiable per learner** — Per-learner thresholds that drift downward to keep pace with the calendar are no different from a percentage grade; the defining property is that the criterion is fixed and time is variable, not the inverse.

## Examples across domains

**Avionics — a one-week shop unit on transponder altitude-encoder calibration.**

*Setup.* The unit's mastery criterion is "configure, calibrate, and verify a Mode S
transponder altitude encoder against an IFR-6000 ramp tester to FAA AC 43-6C tolerance, and
correctly interpret the resulting trace." The technician has worked through a one-day
classroom session and a half-day bench lab. The conventional move is to grade the lab and
advance; mastery learning replaces that move with a Formative A/B cycle.

*Formative A and correctives.* On day three the technician takes Formative A — a 12-item
check with three calibration scenarios scored against the AC-43-6C decision table. Threshold
is 10 of 12, including all three trace-interpretation items. A first-pass result of 8 of 12
with both errors clustered on "encoder data discrepancy at FL180" triggers correctives:
instead of a re-read of the procedure, the instructor pairs the technician with a shop
senior for a 90-minute hands-on walk-through of a deliberately mis-set encoder, with reasoning
narrated at each diagnostic step. Method-change is the operative move (Guskey, 2007, p. 21).

*Formative B and spacing.* Two days later the technician takes Formative B — same blueprint,
parallel items, different aircraft tail number in the scenario. A pass advances them to the
next unit (ADS-B Out compliance) which depends on this one. A second spaced check at +14
days during the next shop session confirms the corrective held across a standard retention
window. Kulik et al. (1990) report d ≈ 0.5 for this structure on aligned criterion tests;
Block and Burns (1976) report d ≈ 0.67 retention effects at delays in this range.

**L2 (second-language) acquisition — an A2-to-B1 Spanish unit on the preterite/imperfect
contrast for an adult-learner course.**

*Setup.* The mastery criterion is "in a 12-item production task and an 8-item comprehension
task, correctly select preterite vs. imperfect in narrative past contexts at 90% accuracy,
with errors not concentrated on any single usage rule (completed event, repeated past state,
simultaneous backgrounded action, time-bounded duration)." The unit runs across two weeks of
a community-college evening course; a conventional design would lecture, drill, and move on
to the next tense. The mastery design holds the criterion fixed.

*Formative A and correctives.* End of week one, learners take Formative A — the 20-item
diagnostic. A learner at 14 of 20 with five of six errors on "repeated past state vs.
completed event in time-bounded contexts" triggers a method-change corrective: rather than
re-reading the rule, the instructor assigns a 30-minute paired oral activity in which the
learner narrates a scripted week-long routine to a partner who interrupts with completed
events; the partner narrates back, and the learner transcribes the contrast. The corrective
uses production and listening rather than rule explanation — exactly the method-change move
Guskey (2007) identified as load-bearing.

*Formative B and spacing.* Three days later Formative B uses parallel items in a different
narrative context (a workplace anecdote rather than a vacation). A pass advances the learner
to the imperfect-subjunctive unit; a second spaced check at +10 days, embedded as the
warm-up of the next session, confirms retention. Hattie (2009) reports d = 0.57 for
mastery-learning implementations of this structure; Guskey and Pigott (1988) confirm
consistent affective gains (self-efficacy, course satisfaction) alongside the achievement
effect, which matters in adult L2 contexts where attrition is the modal failure mode.

## Quality signal

The AI tutor knows mastery learning is producing learning when (a) Formative B pass rates after correctives exceed Formative A pass rates by Cohen's d > 0.4 on the same blueprint, (b) the gain is largest in the lowest pre-test quartile (Kulik et al., 1990, pp. 280-283), and (c) a spaced check at +7 to +14 days holds the threshold for at least 80% of learners who passed Formative B. A negative signal: if Formative B pass rate is statistically indistinguishable from Formative A, the corrective is using the same method as the original instruction or no method-change occurred — the meta-analytic effect requires a *different* instructional approach (Guskey, 2007).

## Cross-references

- See [backward-design-ubd](../02-instructional-design/backward-design-ubd.md) for the Stage-2 evidence specification that lets a mastery threshold be operationalized; without a defensible criterion test, mastery learning has nothing to evaluate.
- See [mastery-thresholds](../07-runtime-decisions/mastery-thresholds.md) for the runtime decision rule that converts a Formative A score into an advance/remediate determination.
- See [mastery-threshold-transfer-test-design](../03-assessment-science/mastery-threshold-transfer-test-design.md) for the discipline of writing parallel Formative A/B forms that probe the same construct.
- See [error-analysis-corrective-feedback](../04-delivery-patterns/error-analysis-corrective-feedback.md) for the move that turns a Formative A error pattern into a method-change corrective rather than a re-teach.
- See [testing-effect](../01-learning-science/testing-effect.md) and [spaced-retrieval](../01-learning-science/spaced-retrieval.md) for the retention mechanisms that the Formative A/B cycle and the +14-day spaced check exploit.
- See [pre-post-assessment-effect-size](../03-assessment-science/pre-post-assessment-effect-size.md) for the Formative A → Formative B effect-size calculation the runtime uses to detect when correctives are not working.
- See [gagnes-nine-events](../02-instructional-design/gagnes-nine-events.md) and [merrills-first-principles](../02-instructional-design/merrills-first-principles.md) for the lesson- and course-level frameworks that mastery learning composes with at the unit level.
