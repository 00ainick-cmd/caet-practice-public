---
id: backward-design-ubd
title: Backward Design (UbD)
category: 02-instructional-design
aliases: [understanding-by-design, backward-planning]
evidence_strength: strong
# effect_size null: foundational design framework, not a single-treatment
# intervention. The alignment claim is supported by Biggs (1996) and the
# implementation studies cited; no single Cohen's d summarizes the framework.
effect_size: null
key_sources:
  - "Wiggins, G., & McTighe, J. (2005). Understanding by design (Expanded 2nd ed.). Alexandria, VA: Association for Supervision and Curriculum Development."
  - "Biggs, J. (1996). Enhancing teaching through constructive alignment. Higher Education, 32(3), 347-364. doi:10.1007/BF00138871"
  - "Tyler, R. W. (1949). Basic principles of curriculum and instruction. Chicago, IL: University of Chicago Press."
  - "Cho, J., & Trent, A. (2005). 'Backward' curriculum design and assessment: What goes around comes around, or haven't we seen this before? Taboo: The Journal of Culture and Education, 9(2), 105-122."
  - "Childre, A., Sands, J. R., & Pope, S. T. (2009). Backward design: Targeting depth of understanding for all learners. Teaching Exceptional Children, 41(5), 6-14. doi:10.1177/004005990904100501"
  - "Reynolds, H. L., & Kearns, K. D. (2017). A planning tool for incorporating backward design, active learning, and authentic assessment in the college classroom. College Teaching, 65(1), 17-27. doi:10.1080/87567555.2016.1222575"
  - "Uluçınar, U. (2021). Findings of qualitative studies on Understanding by Design: A meta-synthesis. International Journal of Curriculum and Instructional Studies, 11(2), 167-194."
last_reviewed: 2026-04-29
applies_to: [acquisition, transfer, sequencing]
contraindicated_when:
  - material.unstable_target_specification
  - task_type.exploratory_inquiry_emergent_outcomes
  - learner_state.outcomes_unknown_to_designer
runtime_triggers:
  - curriculum_design_started
  - module_outline_requested
  - assessment_planning_started
  - misalignment_detected_outcome_to_assessment
related: [merrills-first-principles, gagnes-nine-events, mastery-learning, bloom-levels-in-assessment, validity-reliability, mastery-threshold-transfer-test-design, transfer-of-learning]
---

# Backward Design (UbD)

## One-line claim

Design every learning experience by first specifying the desired understanding and transfer, then defining the evidence that would prove it, and only then choosing the activities — never the other way around.

## Evidence base

Backward Design, formalized in *Understanding by Design* (Wiggins & McTighe, 2005), is the operational descendant of Tyler's (1949) curriculum rationale, which insisted that any defensible educational program begin with a clear answer to "what educational purposes should the school seek to attain?" before deciding on activities, organization, or evaluation. Wiggins and McTighe restated this as a three-stage planning sequence — Stage 1 *desired results* (transfer goals, enduring understandings, essential questions, knowledge and skill targets), Stage 2 *acceptable evidence* (performance tasks plus other evidence sufficient to infer understanding), and Stage 3 *learning experiences* — and made the planner's responsibility explicit: an activity does not earn its place in a unit unless it produces evidence relevant to a Stage 2 task that itself bears on a Stage 1 result. Cho and Trent (2005), reviewing the framework's rise in *Taboo: The Journal of Culture and Education*, documented its uptake under standards-and-accountability pressure precisely because the alignment chain it imposes is checkable.

Biggs's (1996) *Higher Education* article on constructive alignment provides the parallel theoretical case from higher education and is the most-cited empirical foundation for the alignment claim itself: when intended outcomes, teaching activities, and assessment criteria are all aimed at the same target verb (e.g., *explain*, *apply*, *critique*), students take cues from the assessment about what to learn, the activities exercise the very performance being assessed, and reported deep-approach learning rises. The mechanism is alignment, not the specific UbD template; Wiggins and McTighe's contribution is to make alignment a planning artifact rather than a happy accident. Reynolds and Kearns (2017), reporting in *College Teaching* on a backward-design planner deployed in an undergraduate biology course, found that instructors using the tool reported better content prioritization, more frequent comprehension checks, and tighter time management compared to their pre-implementation lecture planning. Childre, Sands, and Pope (2009), writing in *Teaching Exceptional Children*, showed the framework adapts cleanly to inclusion classrooms by making the desired-evidence stage explicit about which learners must demonstrate what, preventing default-to-coverage drift.

The principal boundary condition is that backward design assumes the desired result can be specified in advance with enough fidelity to write a rubric for it. Uluçınar's (2021) meta-synthesis of 12 qualitative UbD studies in the *International Journal of Curriculum and Instructional Studies* identified the most common implementation failures as exactly this problem: teachers writing vague "understandings" with no observable evidence behind them, or skipping Stage 2 entirely and reverting to activity-first planning under time pressure. Where targets are genuinely emergent — early-stage research training, open-ended creative inquiry, exploratory ethnography — the framework's premise is violated and forcing it produces brittle plans. The framework is for instruction whose outcomes the designer can name; it is not a method for discovering what those outcomes should be.

## When to apply

- **Curriculum or module design started** — Before any activity, video, or example is chosen, run
  the three-stage sequence end-to-end on paper. Stage 1 names the transfer goal and the enduring
  understandings; Stage 2 names the performance task and other evidence; Stage 3 chooses the
  activities that build toward the task. Inverting this order is the single most common failure
  mode the framework was written to prevent (Wiggins & McTighe, 2005, ch. 1).
- **Module outline requested** — When the tutor is asked to plan a multi-session unit, the first
  artifact produced should be the Stage 1 + Stage 2 specification, not a lesson list. The lesson
  list is a Stage 3 output and is derivative.
- **Assessment planning started** — Backward design forces the assessment to be designed
  alongside the outcome, not after the unit. If the request is "write the test for unit X," treat
  it as a signal to surface unit X's Stage 1 and check whether the proposed test items actually
  evidence the named outcomes (see [bloom-levels-in-assessment](../03-assessment-science/bloom-levels-in-assessment.md)).
- **Misalignment detected between outcome and assessment** — When a tutor or reviewer notices the
  stated goal is "apply" or "analyze" but the test items are recall-only (or vice versa), back up
  to Stage 1 and re-derive Stage 2 from the outcome verb. Constructive alignment is the
  operational fix (Biggs, 1996).
- **Transfer is the criterion of success** — When the learner must use this knowledge in a
  context different from the training context (certification exam, fieldwork, real practice),
  Stage 2 must include a transfer task — not just recall items — and Stage 3 must include
  practice on that transfer task (see [transfer-of-learning](../01-learning-science/transfer-of-learning.md)).

## When NOT to apply

- **Target outcomes cannot be specified in advance** — Genuinely exploratory inquiry (e.g.,
  open-ended capstone research, art studio crit, first-pass discovery learning) violates the
  framework's premise. Specifying a Stage 2 rubric ahead of time forecloses the inquiry; use a
  formative-feedback or productive-failure pattern instead. The Uluçınar (2021) synthesis flags
  this as a recurring source of implementation friction.
- **Goals are unstable or under negotiation** — If stakeholders are still debating what the
  course should produce, running backward design now will produce a plan that has to be
  rebuilt next month. Resolve the goal-setting conversation first; backward design is a
  planning method, not a goal-discovery method.
- **The "outcome" is itself unknown to the designer** — Tutors authoring on a topic they do not
  yet understand cannot write a defensible Stage 1. The fix is research, not a UbD template
  filled with placeholder verbs.
- **Single-event, low-stakes interaction** — A five-minute clarification, a single-question
  follow-up, or a one-off office-hours visit does not need a three-stage plan. The framework's
  overhead is justified at the unit and module scale, not at the turn scale.
- **Pure motor-skill maintenance with established standards** — When the outcome and rubric are
  already specified by external authority (e.g., FAA practical test standards for a maneuver),
  the planner consumes the existing Stage 1 and Stage 2 rather than re-deriving them; force-fit
  re-derivation wastes time and risks drifting from the official standard.

## How to apply

- **Write the transfer goal in observable verbs first** — Before anything else, complete the
  sentence "By the end of this unit the learner will independently use their learning to ___ in
  ___ contexts" with verbs from [bloom-levels-in-assessment](../03-assessment-science/bloom-levels-in-assessment.md).
  Vague verbs ("understand", "appreciate") are a Stage 1 failure signal.
- **Distinguish enduring understandings from facts** — Enduring understandings are
  transferable claims (e.g., "transponders confirm identity by exchanging interrogation/reply
  pairs whose timing encodes range") that survive after specific facts fade. Facts and skills
  belong in the knowledge/skill row of Stage 1, not the understandings row.
- **Design the Stage 2 performance task before any Stage 3 activity** — A complete Stage 2 task
  has: a realistic role/audience/situation/product specification, a rubric tied to the Stage 1
  understanding, and at least one source of "other evidence" (quizzes, observations) that
  triangulates the performance task (Wiggins & McTighe, 2005, GRASPS framework).
- **Run the WHERETO audit on Stage 3** — Each lesson should *Where, Hook, Equip, Rethink,
  Evaluate, Tailor, Organize*. Activities failing two or more letters rarely earn their place.
- **Audit the alignment chain explicitly** — For every Stage 3 activity, name the Stage 2
  evidence it builds toward; for every Stage 2 element, name the Stage 1 result it evidences.
  Activities that do not chain back to a Stage 1 result are candidates for cutting (constructive
  alignment, Biggs, 1996).
- **Treat misalignment as a Stage 1 problem first** — If assessment items and activities feel
  mismatched, fix the outcome statement before tweaking the items. Most reported "test problems"
  in the Reynolds & Kearns (2017) data trace upstream to a Stage 1 verb the assessment did not
  match.

## Common misapplications

- **Activity-first planning dressed in UbD vocabulary** — Choosing favorite activities and then
  back-fitting outcomes to justify them inverts the framework. The Cho & Trent (2005) review
  documented this as the most frequent failure mode in the early-2000s adoption wave.
- **Stage 2 collapsed to a multiple-choice quiz** — A quiz is a piece of *other evidence* in the
  framework, not a performance task. Outcomes phrased as "apply" or "analyze" require an
  authentic task; collapsing Stage 2 to recognition items breaks the alignment chain.
- **"Understandings" written as topics, not claims** — "The learner will understand
  transponders" is a topic, not an understanding. "The learner will understand that
  transponders distinguish aircraft by interrogation timing, so a stuck reply locks the
  airspace" is a claim and is testable.
- **Treating UbD as a one-time artifact** — Filling the template once at unit launch and never
  revisiting it produces stale plans. The Uluçınar (2021) synthesis identified failure-to-revisit
  as a primary degradation pathway.
- **Expanding the framework into unstable-target territory** — Forcing UbD onto open-ended inquiry
  or emergent-curriculum work where outcomes legitimately cannot be pre-specified yields hollow
  Stage 1 statements that bind nothing downstream.

## Examples across domains

**Avionics — three-session unit on Mode S transponder ramp testing.**

*Stage 1 (desired results).* Transfer goal: the technician independently ramp-tests a Mode S
transponder install (e.g., GTX 345) on an unfamiliar airframe and determines pass/fail against
the manufacturer test card. Enduring understanding: "Mode S replies encode aircraft identity and
altitude, so test failures localize to the offending field — not the radio." Knowledge: reply
formats, test-set cabling for the IFR-6000 / T-47. Skill: interpret the reply trace and decide
go/no-go.

*Stage 2 (evidence).* Performance task — the technician performs a full ramp test on a shop
mock-up, narrating each step and identifying a planted fault (a corrupted ICAO address in a
configuration file). Rubric scores test-card adherence, fault isolation accuracy, and the
verbal explanation. Other evidence: a 10-item quiz on reply formats, an oral check on which
field a given symptom would localize to.

*Stage 3 (learning experiences).* Session one teaches reply formats and the trace display;
session two is a faded worked example on a known-good install (see
[merrills-first-principles](../02-instructional-design/merrills-first-principles.md));
session three is the planted-fault performance task. Each step is chosen because it builds
toward the Stage 2 task — not because lecture-then-lab is the default.

**Emergency medicine training — two-week unit on adult sepsis recognition for first-year residents.**

*Stage 1 (desired results).* Transfer goal: on an unselected ED patient with vital-sign
abnormality, the resident independently identifies sepsis criteria, initiates the bundle within
the one-hour window, and revises the differential as labs return. Enduring understanding:
"Sepsis is a syndrome diagnosed by clinical pattern over time, not by any single lab — so
serial reassessment beats waiting for the perfect lab." Knowledge: SIRS/qSOFA/Sepsis-3 criteria,
the bundle elements. Skill: revise differential with new data.

*Stage 2 (evidence).* Performance task — a high-fidelity simulation in which the resident
manages two consecutive ED arrivals (one septic, one mimicker, order randomized), narrating the
differential aloud, ordering the bundle when appropriate, and revising at the 30-minute lab
return. Rubric scores time-to-bundle, accuracy of differential revision, and the verbal
reasoning. Other evidence: chart-stimulated recall on three real cases the resident managed in
the prior week, and a 15-item key-features test on sepsis mimickers.

*Stage 3 (learning experiences).* A one-hour case-based session on Sepsis-3 criteria and the
one-hour bundle; two sessions of low-fidelity vignettes alternating septic and non-septic
presentations (see [interleaving](../01-learning-science/interleaving.md)); the high-fidelity
simulation as the Stage 2 task; chart-stimulated recall during the next shift to consolidate
transfer (see [transfer-of-learning](../01-learning-science/transfer-of-learning.md)). Each
activity is selected because it produces practice on the differential-revision skill the
performance task evaluates.

## Quality signal

The AI tutor knows backward design is doing its job when, for every Stage 3 activity in a plan,
it can name in one sentence the Stage 2 evidence the activity builds toward and the Stage 1
result that evidence supports — and when no Stage 2 element is left dangling without a Stage 1
ancestor. A weaker but faster signal is verb-match: the dominant verb in the Stage 1 outcome
statement appears in the rubric criteria of the Stage 2 task. Verb mismatch (Stage 1 says
"apply", rubric scores "recall") is a high-precision signal of broken alignment.

## Cross-references

- See [merrills-first-principles](../02-instructional-design/merrills-first-principles.md) for the activation–demonstration–application–integration sequence that often instantiates Stage 3.
- See [gagnes-nine-events](../02-instructional-design/gagnes-nine-events.md) for an event-level instructional sequence that fits inside a single Stage 3 lesson.
- See [mastery-learning](../02-instructional-design/mastery-learning.md) for the criterion-referenced advancement rule that pairs naturally with Stage 2 performance tasks.
- See [bloom-levels-in-assessment](../03-assessment-science/bloom-levels-in-assessment.md) for the verb-level taxonomy that disciplines Stage 1 outcome statements.
- See [validity-reliability](../03-assessment-science/validity-reliability.md) for the measurement constraints any Stage 2 evidence package must satisfy.
- See [mastery-threshold-transfer-test-design](../03-assessment-science/mastery-threshold-transfer-test-design.md) for the threshold and transfer-test logic that operationalizes "acceptable evidence."
- See [transfer-of-learning](../01-learning-science/transfer-of-learning.md) for the transfer construct that motivates Stage 1 transfer goals.
