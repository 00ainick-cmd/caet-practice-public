---
id: bloom-levels-in-assessment
title: Bloom Levels in Assessment
category: 03-assessment-science
aliases: [bloom-assessment-alignment, cognitive-level-of-items]
evidence_strength: strong
# effect_size is null because this chapter is a classification framework
# applied to assessment, not an effect-producing intervention. Item alignment
# to a target Bloom cell is a *necessary precondition* for valid measurement;
# the magnitudes of the downstream learning effects belong to the chapters on
# the interventions themselves (worked examples, retrieval, feedback, etc.),
# not to the classification act. See Krathwohl (2002) and Airasian & Miranda
# (2002) for the framework's authoritative formulation; see Momsen et al.
# (2010) and Zheng et al. (2008) for the empirical demonstration that
# misclassified items routinely undershoot or overshoot stated objectives.
effect_size: null
key_sources:
  - "Krathwohl, D. R. (2002). A revision of Bloom's taxonomy: An overview. Theory Into Practice, 41(4), 212-218. doi:10.1207/s15430421tip4104_2"
  - "Airasian, P. W., & Miranda, H. (2002). The role of assessment in the revised taxonomy. Theory Into Practice, 41(4), 249-254. doi:10.1207/s15430421tip4104_8"
  - "Mayer, R. E. (2002). Rote versus meaningful learning. Theory Into Practice, 41(4), 226-232. doi:10.1207/s15430421tip4104_4"
  - "Crowe, A., Dirks, C., & Wenderoth, M. P. (2008). Biology in Bloom: Implementing Bloom's taxonomy to enhance student learning in biology. CBE-Life Sciences Education, 7(4), 368-381. doi:10.1187/cbe.08-05-0024"
  - "Zheng, A. Y., Lawhorn, J. K., Lumley, T., & Freeman, S. (2008). Application of Bloom's taxonomy debunks the 'MCAT myth'. Science, 319(5862), 414-415. doi:10.1126/science.1147852"
  - "Momsen, J. L., Long, T. M., Wyse, S. A., & Ebert-May, D. (2010). Just the facts? Introductory undergraduate biology courses focus on low-level cognitive skills. CBE-Life Sciences Education, 9(4), 435-440. doi:10.1187/cbe.10-01-0001"
  - "Stanny, C. J. (2016). Reevaluating Bloom's taxonomy: What measurable verbs can and cannot say about student learning. Education Sciences, 6(4), 37. doi:10.3390/educsci6040037"
last_reviewed: 2026-04-29
applies_to: [measurement, decision]
contraindicated_when:
  - learner_state.first_exposure
  - material.high_element_interactivity_no_scaffolding
  - task_type.motor_acquisition
runtime_triggers:
  - assessment_item_drafted
  - test_blueprint_review
  - bloom_floor_audit
  - objective_to_item_alignment_check
  - performance_assessment_gap_detected
related: [blooms-revised-taxonomy, item-writing-rules, distractor-analysis, mastery-threshold-transfer-test-design, validity-reliability, pre-post-assessment-effect-size, backward-design-ubd, transfer-of-learning]
---

# Bloom Levels in Assessment

## One-line claim

An assessment item measures the cognitive level it actually demands of the test-taker, not the level its verb advertises; valid measurement requires that the cell of the item — knowledge type crossed with cognitive process — match the cell of the objective it claims to assess, and the test as a whole must distribute items across cells in proportion to the objectives' distribution.

## Evidence base

The revised taxonomy was designed in part to fix a measurement problem the 1956 hierarchy left open: a single dimension does not constrain item writing tightly enough to prevent objective-assessment drift. Krathwohl (2002, pp. 215-217) reframed each objective as the intersection of a Knowledge type (Factual, Conceptual, Procedural, Metacognitive) and a Cognitive Process (Remember, Understand, Apply, Analyze, Evaluate, Create) — a 4 × 6 Taxonomy Table. Airasian and Miranda (2002, pp. 250-253) carried the framework into assessment explicitly, arguing that the dual-dimension structure produces "sharper, more clearly defined assessments" and lets cell mismatches between objective and item become visible at item-review time rather than after a job-performance failure. Their operational claim is that assessment validity is largely a question of cell agreement: the item must demand the same kind of cognition the objective named, on the same kind of knowledge.

The empirical literature supplies two converging lines of evidence. First, Mayer (2002, pp. 226-230) drew the assessment-relevant retention-versus-transfer line through the table: items in the Remember row measure retention (recall material in the form taught), while items from Understand through Create measure transfer (use the material on a new problem). Tests that consist almost entirely of Remember items therefore predict retention but not the transfer the objectives implicitly require — Mayer's central operational point. Second, large-sample audits of real test banks consistently find this drift in practice. Crowe, Dirks, and Wenderoth (2008) classified roughly 600 college biology exam items with the Blooming Biology Tool and found that test items overwhelmingly clustered at Remember/Understand even when the courses' stated outcomes named Apply or Analyze. Momsen, Long, Wyse, and Ebert-May (2010) extended this in *CBE-Life Sciences Education* across multiple introductory biology courses: assessment items targeted lower cognitive levels in 93% of items, and the cognitive level of the syllabus's objectives was not predictive of the cognitive level of the actual assessments. The objective-to-item gap is the rule, not the exception.

Item format does not by itself fix or break cell alignment. Zheng, Lawhorn, Lumley, and Freeman (2008) demonstrated in *Science* that multiple-choice items can measure analysis, evaluation, and inference — debunking the "MCAT myth" that selected-response formats only test recall — provided the stem demands a cognitive operation rather than a recognition match. The principal known boundary condition on cell classification is verb-list overreach: Stanny (2016) analyzed 30 published "Bloom's verbs" lists and found no verb assigned to the same cell by all 30; three verbs (choose, relate, select) appeared at every level depending on the list. The classification of an item is determined by the cognitive demand of its task, not by the surface verb of its stem.

## When to apply

- **Assessment item drafted** — Before any item is added to a test bank, classify it on the Taxonomy Table (knowledge type × cognitive process) by reading the cognitive demand of the task itself. If the item's cell does not match the objective's cell, rewrite the item before reviewing distractors or psychometrics (Airasian & Miranda, 2002).
- **Test blueprint review** — Whenever a unit, certification, or course test is being assembled or reviewed, lay the cells of all items and all objectives side by side. The blueprint must distribute items across cells in proportion to the objective distribution; a Remember-heavy test for an Apply-heavy objective set is a measurement failure (Momsen et al., 2010).
- **Bloom floor audit** — When a course or program shows the symptom pattern "learners pass the tests but cannot perform on the job/exam/practical," run a Bloom-level audit on the existing item bank. The expected finding (per Momsen et al., 2010) is that the bank is over-clustered at Remember/Understand relative to the performance criterion.
- **Objective-to-item alignment check** — Whenever an objective is rewritten or a new objective is added to the curriculum, retire or rewrite items whose cells no longer match. The cell of the objective is the binding constraint.
- **Pre/post effect-size measurement** — Before computing pre/post gain on an assessment, confirm pre and post items target the same cells. Otherwise a "gain" can be an artifact of the post-test sliding to easier cells (see [pre-post-assessment-effect-size](../03-assessment-science/pre-post-assessment-effect-size.md)).
- **Performance assessment gap detected** — When an item performs anomalously (very high pass rate paired with low transfer; or very low pass rate when objective performance is fluent), the Bloom cell of the item is the first place to look — likely a recognition item posing as an Apply item, or an Apply item written without the schema the cell requires.

## When NOT to apply

- **Learner is at first exposure to a high-element-interactivity concept** — Do not assess at Apply / Procedural or above before the underlying schema exists; the result is noise, not measurement (see [cognitive-load-theory](../01-learning-science/cognitive-load-theory.md), [worked-example-effect](../01-learning-science/worked-example-effect.md)). The taxonomy classifies the destination cell, not the path; assessing a cell the learner has not yet been taught measures absence of instruction, not absence of ability.
- **Material is high-interactivity with no scaffolding** — When the assessment requires integration across many interacting elements but the instruction provided no Understand-level building blocks, an Analyze or Evaluate item conflates schema gap with cognitive ability. Scaffold first; classify and assess at the target cell after.
- **Pure motor-skill acquisition phase** — The Taxonomy Table classifies cognitive demand and is built for declarative and conceptual content. Motor execution (torque-feel, swing mechanics, intubation hand-positioning) has its own bottlenecks; classify only the embedded declarative content (limit values, decision points, sequencing rules), and use a performance rubric for the motor portion (see [item-writing-rules](../03-assessment-science/item-writing-rules.md) for declarative items, [mastery-threshold-transfer-test-design](../03-assessment-science/mastery-threshold-transfer-test-design.md) for performance assessments).
- **Item is being classified by surface verb only** — Stanny (2016) showed verb lists disagree wholesale on which cell a verb claims; an item whose classification rests on its stem's verb rather than the cognitive demand of its task is unclassified.
- **Cell is being used to flatter the test** — Tagging an item "Apply" because the bank needs higher-cell items, when the task is recognition, is the most common failure mode. Do not classify aspirationally; classify by what the test-taker actually has to do.

## How to apply

- **Classify by what the test-taker must do, not by the verb in the stem** — Read the item, list the operations a successful test-taker performs (recall a fact, summarize a concept, run a procedure on a new case, judge an option against criteria, generate a novel solution), and place the item in the cell that names those operations. The verb in the stem is a hint, not a classification (Stanny, 2016; Crowe, Dirks, & Wenderoth, 2008).
- **Match the item's cell to the objective's cell, exactly** — A Remember / Factual objective gets a Remember / Factual item; an Apply / Procedural objective gets an Apply / Procedural item — typically a novel scenario the learner has not seen during instruction. Cell mismatch is the modal validity failure (Airasian & Miranda, 2002; see [blooms-revised-taxonomy](../02-instructional-design/blooms-revised-taxonomy.md) for the framework, [backward-design-ubd](../02-instructional-design/backward-design-ubd.md) for the design discipline that prevents the drift).
- **Use the right format for the cell** — Remember/Understand items work in selected-response; Apply / Procedural usually requires a scenario-based item with a novel surface; Evaluate items require comparison against criteria the learner must select; Create items require constructed response with a rubric. Multiple-choice can reach Analyze and Evaluate when the stem forces an operation, not a match (Zheng et al., 2008); free-form is required for genuine Create (see [item-writing-rules](../03-assessment-science/item-writing-rules.md)).
- **Write distractors that map to specific Bloom-level errors** — Distractors at Apply / Procedural should encode plausible procedure-misexecutions, not unrelated wrong answers; distractors at Evaluate should encode commitments to the wrong criterion. Distractors that violate the cell (a recognition foil on an Apply item) collapse the item's level (see [distractor-analysis](../03-assessment-science/distractor-analysis.md)).
- **Distribute items across cells per the blueprint** — Build the blueprint from the objectives' cells, then sample items proportionally. If 60% of the unit's objectives are Apply / Procedural, ~60% of the unit's items must be Apply / Procedural; a unit's items have no business being 90% Remember when the objectives are mostly Apply (Momsen et al., 2010, demonstrated this failure in 100+ courses).
- **Treat the Apply cell as requiring a novel surface** — An Apply item that uses the exact scenario practiced in the lesson degrades to Remember in the test-taker's mind. The cell requires application to a problem with a different surface but the same underlying structure (Mayer, 2002, on the retention-vs-transfer distinction).
- **Audit existing banks against the blueprint, then prune** — When inheriting a bank, classify every item, count cells, compare to the blueprint, and drop or rewrite items where the bank over-clusters at low cells. The expected initial finding (Momsen et al., 2010) is heavy clustering at Remember.

## Common misapplications

- **Tagging by verb without reading the task** — A stem that begins with "Apply…" but offers four options that name the procedure is a Remember item; the task is recognition of the named procedure. Classification by surface verb is the single most common bank-poisoning mistake (Stanny, 2016).
- **Calling a familiar scenario "Apply"** — Reusing the lesson's worked example as the assessment item demotes the cell from Apply to Remember; the test-taker matches a remembered surface, not a procedure (Mayer, 2002, on the surface-vs-structure distinction in transfer assessment).
- **Equating multiple-choice with low cell** — Format is not the same as level. Zheng et al. (2008) showed multiple-choice items can measure Analyze and Evaluate when the stem demands an operation. Conversely, a constructed-response item can sit at Remember when it asks for verbatim recall.
- **Classifying difficulty as cell** — A Remember item can be hard (obscure regulatory limit, dense distractors); a Create item can be easy (open-ended list, no criteria). The cell classifies kind of cognition; difficulty is a separate measurement (see [item-difficulty-discrimination](../07-runtime-decisions/item-difficulty-discrimination.md)).
- **Floor-clustering a test bank** — Building a bank that lives entirely at Remember/Understand because those items are easy to author. Crowe et al. (2008) and Momsen et al. (2010) document this pattern repeatedly; the bank then under-measures the program's stated objectives.
- **Skipping the Knowledge dimension** — Tagging items by Cognitive Process alone and ignoring whether they target Factual, Conceptual, Procedural, or Metacognitive knowledge. The same Apply verb attached to Factual vs. Procedural knowledge produces different items and different validity claims (Krathwohl, 2002).
- **Treating "metacognitive" objectives as decoration** — Listing Procedural / Metacognitive objectives ("knows when to escalate to a senior tech") and assessing only with Remember items on the procedure itself. The cell is teachable and assessable; it requires items that probe strategy choice, not strategy knowledge.

## Examples across domains

**Avionics — Garmin G1000 NXi MFD page-fail troubleshooting on a Cessna 182.**

*Setup.* A second-year technician has completed a module on integrated-flight-deck troubleshooting. The stated objective reads: "Given a reported MFD page-fail symptom on the G1000 NXi, isolate the failed LRU within three diagnostic steps using the cockpit reference and a Garmin GIA-equipped test harness." The shop's existing test bank contains 12 items: 10 multiple-choice on G1000 nomenclature and LRU acronyms (GIA, GDU, GDL), 2 multiple-choice asking which LRU is most likely failed for a single textbook symptom matched verbatim to the item.

*Cell map and intervention.* The objective is Apply / Procedural — execute a diagnostic algorithm on a novel symptom and isolate the failed LRU. The bank's 12 items sit at Remember / Factual (recognize an acronym) and Remember / Conceptual (match a textbook symptom-LRU pair from memory). The bank does not have a single Apply / Procedural item; the cell mismatch (Airasian & Miranda, 2002) is the entire reason the technician will pass the test and then chase the wrong LRU on the bench. The tutor rewrites: 4 of the 10 nomenclature items are dropped; in their place go 3 scenario items that each describe a *new* symptom presentation (the "page-fail" surface differs across items — flickering map, frozen attitude, dropped traffic targets) and require the technician to choose the next diagnostic step (not the failed LRU directly). Distractors encode realistic procedure-misexecutions (skip the GIA self-test, swap GDU before re-seating GDL connector). One Evaluate / Procedural item asks the technician to judge two diagnostic plans against the work-card sequence and select the one that conforms to Garmin's recommended LRU-substitution order (Zheng et al., 2008, on multiple-choice items at higher cells). One free-response Create / Procedural item asks the technician to write a three-step plan for a never-seen symptom; a rubric grades it.

*Verification.* Pre/post on the rewritten bank tracks two cells separately: Remember/Understand items (nomenclature retention) and Apply/Evaluate/Create items (procedural transfer). On the practical bench check the next week, the cell-aligned bank's Apply-item performance correlates ~r = 0.7 with bench performance, where the original recognition-only bank correlated near zero (the typical finding when blueprint cells match performance cells; Momsen et al., 2010, on the absence of correlation when they do not).

**Basketball coaching — defensive rotation and help-side decisions in a high-school varsity practice unit.**

*Setup.* A varsity head coach is teaching a unit on team defense — specifically, when to rotate, who rotates, and the reads that trigger help-side. The unit's stated objective is "On a live ball-screen action with the ball-handler attacking the middle, the help-side defender will commit to the roll, the weak-side wing will rotate to the corner, and the original on-ball defender will recover to the elbow within two passes." The current "assessment" is a written quiz: name the five spots on a half-court diagram and label "help-side" on the printed image.

*Cell map and intervention.* The objective is Evaluate / Procedural — judge a live read and execute the corresponding rotation, choosing the right help-side action under time pressure. The current quiz lives at Remember / Factual (recognize a spot on a diagram) and Understand / Conceptual (label "help-side" given a static image). The cells do not match; the quiz cannot detect whether a player will rotate correctly in a live game. The coach rebuilds the assessment to match the cell. Three new instruments are added. (1) Apply / Procedural: a video-clip item bank — 15 short clips showing different ball-screen actions, each ending the instant before the help defender must commit; the player selects "rotate now / rotate one beat later / stay" and identifies which teammate covers the corner. Distractors encode the three highest-frequency errors (early rotate giving up the corner three; late rotate giving up the dunker spot; ball-watching with no commitment). (2) Evaluate / Procedural: paired-clip items show two live rotations on the same action; the player picks the one that conforms to the team's defensive scheme and explains why in one sentence (Zheng et al., 2008, on Evaluate-cell selected response). (3) Create / Procedural: in a live 3-on-3 walkthrough, the player calls the rotation aloud the moment the screen is set; the assistant coach scores against a three-criterion rubric (commit timing, recovery angle, communication). The Knowledge dimension is hit at Procedural across all three; the original Factual quiz is retained as a 5-minute warm-up only, not as the gate.

*Verification.* Across the next four scrimmages, the coach charts blown rotations per defensive possession. The cell-aligned assessment scores correlate with in-scrimmage rotation accuracy (the Apply video-clip score predicts roughly two-thirds of between-player variance); the original written quiz score, retained as a covariate, does not predict scrimmage performance — the same disconnect Momsen et al. (2010) documented across 77 introductory-biology courses, expressed in basketball.

## Quality signal

The AI tutor knows Bloom-level alignment is being applied well when (a) every item in the bank is tagged with a (Knowledge, Process) cell and the bank's cell distribution matches the unit objectives' cell distribution within ~10 percentage points per row and column, (b) inter-rater reliability on cell classification — two independent raters using the task's cognitive demand, not the verb (Crowe et al., 2008) — runs ~80% or higher, and (c) item-level performance correlates with criterion (job task, downstream course, certification practical) at the cell intended: Apply items predict Apply performance, Remember items predict Remember performance, and a Remember-heavy bank does not predict an Apply-heavy criterion (the modal Momsen et al., 2010 failure). When (a)-(c) hold, post-instruction gain at higher cells is interpretable as transfer; when they fail, "gain" is recognition rehearsal (Mayer, 2002).

## Cross-references

- See [blooms-revised-taxonomy](../02-instructional-design/blooms-revised-taxonomy.md) for the framework itself — the 4 × 6 Knowledge × Process table this chapter applies to assessment.
- See [item-writing-rules](../03-assessment-science/item-writing-rules.md) for stem and option construction at each cell, especially distractor families that hold the cell rather than collapsing it to recognition.
- See [distractor-analysis](../03-assessment-science/distractor-analysis.md) for the empirical follow-up: which distractors actually function and what their pattern says about which Bloom level the item is reaching.
- See [mastery-threshold-transfer-test-design](../03-assessment-science/mastery-threshold-transfer-test-design.md) for the cell-by-cell decision of where to set passing scores and how to design the transfer-cell items separately.
- See [validity-reliability](../03-assessment-science/validity-reliability.md) for why cell alignment is the construct-validity argument that makes a test mean what its blueprint says it means.
- See [pre-post-assessment-effect-size](../03-assessment-science/pre-post-assessment-effect-size.md) for why pre/post gain claims require pre and post items to occupy the same cell.
- See [backward-design-ubd](../02-instructional-design/backward-design-ubd.md) for the design discipline that prevents objective-assessment cell drift in the first place.
- See [transfer-of-learning](../01-learning-science/transfer-of-learning.md) for the empirical foundation behind Mayer's retention-versus-transfer distinction operationalized cell-by-cell here.
