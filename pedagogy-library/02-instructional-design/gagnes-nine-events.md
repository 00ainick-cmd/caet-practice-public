---
id: gagnes-nine-events
title: Gagné's Nine Events of Instruction
category: 02-instructional-design
aliases: [nine-events-of-instruction, gagne-events]
evidence_strength: strong
# effect_size is null because Gagné's nine events is a foundational sequencing
# framework, not a single intervention; the framework's components (recall of
# prior learning, guided practice, feedback, retrieval) each have their own
# meta-analytic effect sizes covered in their dedicated chapters. The closest
# whole-framework estimate is Li et al. (2025) in health-professions education
# (SMD 1.55 knowledge, 1.83 practice vs. lecture-only), but that contrast is
# the framework vs. minimal instruction rather than a clean component effect.
effect_size: null
key_sources:
  - "Gagné, R. M., Briggs, L. J., & Wager, W. W. (1992). Principles of instructional design (4th ed.). Fort Worth, TX: Harcourt Brace Jovanovich College Publishers."
  - "Gagné, R. M. (1985). The conditions of learning and theory of instruction (4th ed.). New York: Holt, Rinehart and Winston."
  - "Li, Y., Liang, Z., Li, Z., Yu, Y., Yang, Q., & Li, X. (2025). Effectiveness of Gagné's 9 Events of Instruction in health professions education: A systematic review and meta-analysis. Frontiers in Medicine, 12, 1522830. doi:10.3389/fmed.2025.1522830"
  - "Buscombe, C. (2013). Using Gagné's theory to teach procedural skills. The Clinical Teacher, 10(5), 302-307. doi:10.1111/tct.12051"
  - "Khadjooi, K., Rostami, K., & Ishaq, S. (2011). How to use Gagné's model of instructional design in teaching psychomotor skills. Gastroenterology and Hepatology From Bed to Bench, 4(3), 116-119."
  - "Miner, A., Mallow, J., Theeke, L., & Barnes, E. (2015). Using Gagne's 9 events of instruction to enhance student performance and course evaluations in undergraduate nursing course. Nurse Educator, 40(3), 152-154. doi:10.1097/NNE.0000000000000138"
  - "Merrill, M. D. (2002). First principles of instruction. Educational Technology Research and Development, 50(3), 43-59. doi:10.1007/BF02505024"
last_reviewed: 2026-04-29
applies_to: [acquisition, retention, transfer, sequencing]
contraindicated_when:
  - learner_state.first_exposure
  - material.high_element_interactivity_no_scaffolding
  - task_type.motor_acquisition
runtime_triggers:
  - lesson_start
  - segment_boundary
  - new_objective_introduced
  - procedural_skill_lesson_planned
  - instructional_sequence_choice
related: [merrills-first-principles, backward-design-ubd, 5e-learning-cycle, 4c-id-model, worked-example-effect, testing-effect, error-analysis-corrective-feedback, predict-before-reveal, cognitive-load-theory]
---

# Gagné's Nine Events of Instruction

## One-line claim

Sequence a lesson around nine ordered external events — gain attention, state objective, recall prior learning, present content, guide learning, elicit performance, give feedback, assess, and enhance retention and transfer — so each event deliberately triggers the internal cognitive process required for durable learning.

## Evidence base

Gagné's nine events of instruction operationalize his information-processing theory of learning: each external event is hypothesized to drive a specific internal cognitive process (attention, expectancy, retrieval to working memory, selective perception, semantic encoding, response generation, reinforcement, retrieval cueing, and generalization). The framework reached its mature form in Gagné (1985) *The Conditions of Learning and Theory of Instruction* and in Gagné, Briggs, and Wager (1992) *Principles of Instructional Design*, where the nine events were formalized as a designer's checklist for translating learning objectives into a lesson plan. The framework is not itself a learning theory but a sequencing scaffold that bundles findings from cognitive psychology — schema activation, dual coding, retrieval practice, corrective feedback — into a fixed teaching cadence (Gagné, Briggs, & Wager, 1992).

Empirical evaluation of the whole framework as one intervention has accumulated mainly in health-professions education. Li et al.'s (2025) systematic review and meta-analysis in *Frontiers in Medicine* synthesized 11 controlled studies (5 RCTs, 6 cohort, n=825) comparing instruction designed around the nine events to lecture-based learning. They reported a standardized mean difference of 1.55 (95% CI 0.81–2.29) on knowledge examinations and 1.83 (95% CI 1.19–2.47) on practical-skills assessments, plus elevated learning compliance (OR 4.92) and teaching satisfaction (OR 7.86). Heterogeneity was high (I² = 95% in cohort studies), so the magnitudes are upper-bound estimates against a weak comparator (lecture-only); the directional finding — nine-event sequences outperform unstructured lecture — is consistent across the included studies and across both knowledge and skill outcomes.

Smaller single-site studies converge on the same pattern. Miner et al. (2015) reported significant gains in instructor-effectiveness ratings (p < .001) and a five-percentage-point lift in the lowest course grade across three semesters of a prelicensure nursing course redesigned around the events. Buscombe (2013) and Khadjooi, Rostami, and Ishaq (2011) describe applied lesson plans for procedural skills (bone-marrow aspirate; peritoneal-drain insertion) where every event maps to a concrete instructor move, illustrating the framework's strongest use case: well-defined procedural skills with declarative scaffolding around them. The case studies are not RCTs and should not be treated as effect-size evidence on their own; they bear on the framework's *operational tractability* — that any instructor can run the cycle end-to-end in a single lesson — rather than on its magnitude of effect.

The framework's principal boundary is its origin in declarative and well-defined-procedural learning. Merrill (2002), in *Educational Technology Research and Development*, argued in his First Principles synthesis that event-by-event sequences under-specify the conditions of effective learning when the goal is complex, ill-defined, or whole-task performance — for those goals, problem-centered sequences (4C/ID, Merrill's First Principles, productive failure) outperform discrete-event scaffolds. The nine events also assume content is being transmitted to a learner with at least minimal background; for genuine first exposure to a high-element-interactivity domain, event 5 (guidance) collapses into worked-example-driven instruction and the rest of the sequence becomes a wrapper. Treat the nine events as a robust default cadence for declarative-plus-procedural learning, not a universal recipe for all instruction.

## When to apply

- **Lesson start for a single, bounded objective** — When the segment of instruction targets one clearly-stated learning outcome (declarative knowledge, a defined procedure, a discrete skill) and the learner has prerequisite knowledge, sequence the lesson around the nine events as the default scaffold.
- **Segment boundary inside a longer course** — Each new sub-topic gets its own pass through the events. The events are designed to repeat per objective, not per course; a 60-minute lesson with three objectives runs the cycle three times, not once.
- **New objective introduced in a curriculum** — When a curriculum-design step calls for translating an objective into instruction, the nine events are the operational template. Pair with [backward-design-ubd](../02-instructional-design/backward-design-ubd.md) for objective derivation and use the events for the lesson-level realization.
- **Procedural-skill lesson with a learner who has the prerequisites** — The framework has its strongest empirical support in well-defined procedural skills (psychomotor procedures, equipment operation, defined diagnostic readings) where the steps and the success criterion are both specifiable (Buscombe, 2013; Khadjooi et al., 2011).
- **Instructional sequence choice for a verbal/intellectual skill** — When picking among sequencing frameworks for verbal information or intellectual skills (Gagné's own learning-outcome categories), the nine events are the default; pivot to [merrills-first-principles](../02-instructional-design/merrills-first-principles.md) or [4c-id-model](../02-instructional-design/4c-id-model.md) only if the goal is whole-task complex performance.

## When NOT to apply

- **Genuine first exposure to a high-element-interactivity domain** — When the learner has no schema for the domain at all and the content interleaves many simultaneously interacting elements, jumping to event 6 (elicit performance) before adequate worked examples invites overload (see [cognitive-load-theory](../01-learning-science/cognitive-load-theory.md), [worked-example-effect](../01-learning-science/worked-example-effect.md)). Build initial schemas with worked examples first; run the nine events once a foundation exists.
- **Pure motor-skill acquisition with negligible declarative content** — Events 2 (state objective), 3 (recall prior learning), and 4 (present content) add little to early motor acquisition where physical practice with corrective feedback dominates. Keep events 6 and 7 (perform, feedback) and treat the rest as optional preamble.
- **Open-ended, ill-defined, or transfer-heavy whole-task instruction** — Real-world problem solving, design tasks, and ill-defined troubleshooting are not well served by a fixed event-by-event sequence; use a problem-centered framework instead (Merrill, 2002). Forcing the nine events on these goals produces artificially linear lessons that strip the productive struggle out of the task.
- **Constructivist or inquiry-driven segments where prior recall would prime the wrong answer** — When the instructional move is to let learners hit a productive failure or generate a hypothesis before the canonical content is introduced, event 3 (stimulate recall of prior learning) and event 4 (present content) intentionally come later or in a different form. Don't fight the design; pick a framework whose sequence matches it.
- **One-shot reminders, refreshers, or just-in-time job aids** — A 30-second on-the-job recall prompt is not a lesson and should not be padded into a nine-event sequence. Run events 6–7 (perform, feedback) only.

## How to apply

- **Plan one objective, one pass through all nine events** — Write the objective first (Bloom-level + observable performance + criterion), then map each event to a concrete classroom or runtime move. The events are the agenda for *one* objective; multi-objective lessons run the cycle once per objective (Gagné, Briggs, & Wager, 1992).
- **Make event 1 a relevance hook, not a gimmick** — A relevant problem, a near-miss case, or a surprising data point gains attention; a flashy animation does not (Buscombe, 2013). The hook should foreshadow the objective so attention transfers into expectancy at event 2.
- **State objectives in observable, criterion-referenced form** — "By the end of this lesson, you will correctly identify three Mode S replies on a ramp-tester trace within 30 seconds" beats "understand ADS-B." Event 2 sets the success criterion the learner will judge themselves against.
- **For event 3, use [predict-before-reveal](../04-delivery-patterns/predict-before-reveal.md) on a prerequisite item** — Prompting recall before presenting new content reactivates the schema the new material will attach to and surfaces gaps before they cause downstream failure. Free recall or a brief generative prompt outperforms a recap slide.
- **Pair event 4 (present content) with event 5 (guidance) using a worked example** — The pure presentation of declarative content fades fast; a worked example with explicit step-by-step guidance is the operational form of "present + guide" for any procedural objective (see [worked-example-effect](../01-learning-science/worked-example-effect.md)).
- **At event 6, demand generative performance, not recognition** — Have the learner produce, narrate, or perform; recognition checks ("which of these is correct?") under-deliver on the testing-effect mechanism that gives event 6 its power (see [testing-effect](../01-learning-science/testing-effect.md)).
- **Event 7 feedback is corrective and explanatory, not just right/wrong** — Tell the learner what was right, what was wrong, *and the mechanism* so the schema updates rather than just the answer (see [error-analysis-corrective-feedback](../04-delivery-patterns/error-analysis-corrective-feedback.md)).
- **Event 8 (assess) uses a different item than event 6** — Practice items and assessment items must differ; reusing the practice item collapses event 8 into recognition of a recent answer.
- **Event 9 schedules a delayed retrieval and an analogical transfer prompt** — Plan one delayed retrieval (next session) and one application to a near-but-different context. This is where transfer is engineered; skipping event 9 leaves the framework half-deployed.
- **Match the event 1 hook to the learner's actual stake in the objective** — A new-hire technician needs a different attention move than a senior tech retraining for an STC update. The hook should connect the objective to a problem the specific learner has actually faced or will face within their next month of work; abstract relevance loses to concrete stake.
- **Use the same criterion language at events 2, 6, and 8** — The objective stated at event 2 should be the rubric scored at event 8; if the wording drifts, learners optimize for whichever criterion they last heard. Lock the criterion at event 2 and reuse it verbatim.

## Common misapplications

- **Running the nine events once for a multi-objective lesson** — A 90-minute lesson with four objectives requires four passes, not one stretched cycle. Stretching the cycle dilutes events 6–9 to the point of disappearing.
- **Treating event 9 as a one-line "summary slide"** — A one-line recap is not retention or transfer engineering. Event 9 is a delayed retrieval plus a near-transfer prompt; if neither is scheduled, the lesson stops at event 8 and the framework's retention argument is unmet.
- **Collapsing events 4 and 5 into "show the slides"** — Pure content presentation without explicit guidance (worked examples, modeling, pointing out what to attend to) leaves the learner to discover structure themselves. Most documented framework failures trace to this collapse.
- **Skipping event 3 because "they should already know this"** — Even when the prerequisite is genuinely covered, a brief recall prompt at event 3 reactivates the schema in working memory and surfaces stale knowledge. Skipping it makes event 4 land on a cold schema.
- **Treating the nine events as a checklist rather than a cadence** — The point is the cognitive process each event triggers, not the bullet getting ticked. An "event 1" that does not actually capture attention is decorative; an "event 6" that does not actually elicit generative performance is busywork.
- **Forcing the framework onto ill-defined or whole-task instruction** — When the goal is complex problem solving, the artificial linearity strips out the productive struggle. Switch frameworks rather than bend the events into a shape they were not designed for (Merrill, 2002).
- **Building the event-1 hook from generic motivation rather than the lesson's own content** — A motivational quote, a stock-photo title slide, or a "here's why this matters" speech that does not foreshadow the objective creates expectancy for the wrong content. The hook is part of the cognitive sequence, not a warm-up act for it.

## Examples across domains

**Avionics — installing a TSO-C145 GPS antenna and verifying signal integrity.**

*Setup.* A second-year apprentice has installed several pitot-static components but never a TSO-C145 GPS antenna. The objective is: "Install the antenna per the IPC, then verify SNR and figure-of-merit on the GTN navigator within IFR-tolerances on the first attempt." The learner has the prerequisite avionics-bay layout knowledge; the procedure is well-defined; declarative and procedural content are interleaved.

*Nine-event sequence.* (1) Open with a one-photo case of a recent install where wrong torque on a coax connector cost a 14-day return-to-shop. (2) State the criterion: SNR > 35 and FOM ≤ 2 within five minutes of power-on, no rework. (3) Predict-before-reveal: "Where on the airframe would you expect the antenna mount to be approved, and why?" Reveal the IPC location with the rationale. (4) Present the install procedure as a worked example, calling out the three failure-driving steps explicitly. (5) Walk through the worked install on the trainer airframe with explicit guidance pointing at the gotchas. (6) Apprentice performs the install on a second trainer airframe while narrating each torque check. (7) Tutor gives corrective feedback on the one rotational orientation error the apprentice made and explains why the multipath pattern matters. (8) Apprentice installs on a third bay, this time with the assessor scoring against the rubric (different bay, same criterion). (9) +1 day: 90-second free-recall on the three failure-driving steps. +5 days: install a different but mechanically similar antenna (e.g., XM/SiriusXM) on the same airframe to force near-transfer.

**Genealogy research — extracting and reconciling a 1900 U.S. census household.**

*Setup.* A volunteer researcher has read about census records but has never personally extracted and reconciled one against other sources. The objective is: "Given a 1900 U.S. federal census image, extract every household member into the project's Lineage data model and flag any field that contradicts prior evidence in the family tree." Prerequisite: familiarity with the data model fields and one prior session on handwriting in early-1900s scripts.

*Nine-event sequence.* (1) Open with a real reconciliation conflict: "This child's age differs by three years between the 1900 census and the 1910 census — which document is wrong, and how would you tell?" (2) State the criterion: every household member entered with at least name, relationship, age, birthplace, and one source citation; every contradiction with the existing tree flagged with a reasoned note. (3) Recall prior: "What were the four columns from last week's handwriting practice that change meaning when the enumerator's hand drifts?" Reveal the answer key. (4) Present the worked example — the tutor extracts one household end-to-end, narrating each field choice and each judgment call where the script is ambiguous. (5) Guidance: tutor stays alongside as the researcher extracts the second household, prompting at each ambiguity ("what does the enumerator's marginal note tell you here?"). (6) Researcher extracts the third household independently, narrating decisions. (7) Tutor gives line-by-line feedback on the two fields the researcher misread, explaining the rule for distinguishing the two glyphs. (8) Researcher extracts a fourth household solo against the rubric. (9) +1 day: free-recall on the rubric checklist. +7 days: extract a 1910 census household (the form differs slightly) to force near-transfer to a different schedule. The transfer item directly probes the generalization that event 9 is supposed to engineer.

## Quality signal

The AI tutor knows the nine-event sequence is producing learning when, on the event-8 assessment, the learner meets the event-2 criterion on a previously-unseen item without instructor scaffolding, AND when at the +1-day delayed retrieval the learner recalls the criterion-defining steps with at least 80% accuracy. A failure of event 9 specifically — on-target event-8 performance but sub-50% delayed retrieval — signals that retention/transfer engineering was skipped and that the lesson stopped at event 8.

## Cross-references

- See [merrills-first-principles](../02-instructional-design/merrills-first-principles.md) for the problem-centered framework that complements (and partially supersedes) the nine events for whole-task complex learning.
- See [backward-design-ubd](../02-instructional-design/backward-design-ubd.md) for the objective-derivation step that should precede the nine events; the events realize what UbD specifies.
- See [worked-example-effect](../01-learning-science/worked-example-effect.md) for the operational form of events 4–5 (present + guide) when the objective is procedural.
- See [testing-effect](../01-learning-science/testing-effect.md) for why event 6 must be generative retrieval rather than recognition, and for the spacing logic event 9 should follow.
- See [error-analysis-corrective-feedback](../04-delivery-patterns/error-analysis-corrective-feedback.md) for how to deliver event 7 so the learner updates the underlying model, not just the answer.
- See [predict-before-reveal](../04-delivery-patterns/predict-before-reveal.md) for the concrete delivery pattern that operationalizes event 3 (recall of prior learning).
- See [cognitive-load-theory](../01-learning-science/cognitive-load-theory.md) for the boundary condition that determines when events 4–5 must lean on worked examples instead of presentation-plus-guidance prose.
