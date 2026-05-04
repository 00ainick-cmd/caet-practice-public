---
id: blooms-revised-taxonomy
title: Bloom's Revised Taxonomy
category: 02-instructional-design
aliases: [revised-blooms-taxonomy, anderson-krathwohl-taxonomy, taxonomy-table]
evidence_strength: strong
# effect_size is null because Bloom's Revised Taxonomy is a foundational
# classification framework, not an intervention. It does not "produce" a
# learning effect on its own; it specifies WHAT cognitive level an objective,
# instructional move, or assessment item targets so other interventions
# (worked examples, retrieval, feedback) can be aimed correctly. Effect-size
# claims belong to the interventions, not to the taxonomy.
effect_size: null
key_sources:
  - "Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). A taxonomy for learning, teaching, and assessing: A revision of Bloom's taxonomy of educational objectives (Complete edition). New York: Longman."
  - "Krathwohl, D. R. (2002). A revision of Bloom's taxonomy: An overview. Theory Into Practice, 41(4), 212-218. doi:10.1207/s15430421tip4104_2"
  - "Mayer, R. E. (2002). Rote versus meaningful learning. Theory Into Practice, 41(4), 226-232. doi:10.1207/s15430421tip4104_4"
  - "Pintrich, P. R. (2002). The role of metacognitive knowledge in learning, teaching, and assessing. Theory Into Practice, 41(4), 219-225. doi:10.1207/s15430421tip4104_3"
  - "Airasian, P. W., & Miranda, H. (2002). The role of assessment in the revised taxonomy. Theory Into Practice, 41(4), 249-254. doi:10.1207/s15430421tip4104_8"
  - "Crowe, A., Dirks, C., & Wenderoth, M. P. (2008). Biology in Bloom: Implementing Bloom's taxonomy to enhance student learning in biology. CBE-Life Sciences Education, 7(4), 368-381. doi:10.1187/cbe.08-05-0024"
  - "Stanny, C. J. (2016). Reevaluating Bloom's taxonomy: What measurable verbs can and cannot say about student learning. Education Sciences, 6(4), 37. doi:10.3390/educsci6040037"
last_reviewed: 2026-04-29
applies_to: [acquisition, transfer, measurement, sequencing]
contraindicated_when:
  - learner_state.first_exposure
  - material.high_element_interactivity_no_scaffolding
  - task_type.motor_acquisition
runtime_triggers:
  - objective_drafted
  - assessment_item_drafted
  - segment_boundary
  - alignment_check_requested
  - cognitive_level_mismatch_suspected
related: [backward-design-ubd, bloom-levels-in-assessment, mastery-threshold-transfer-test-design, item-writing-rules, transfer-of-learning, schema-theory-knowledge-components, merrills-first-principles, knowledge-graph-traversal, mastery-thresholds]
---

# Bloom's Revised Taxonomy

## One-line claim

Every learning objective, instructional move, and assessment item locates on a two-dimensional matrix — a knowledge type (factual, conceptual, procedural, metacognitive) crossed with a cognitive process (remember, understand, apply, analyze, evaluate, create) — and instruction is well aligned to the degree that the objective's cell, the practice's cell, and the assessment's cell are the same cell.

## Evidence base

Bloom's Revised Taxonomy was published as Anderson and Krathwohl's (2001) book-length revision of the 1956 *Handbook* and laid out as a two-dimensional table rather than the original single hierarchy. The Knowledge dimension distinguishes Factual (terminology, isolated specifics), Conceptual (categories, principles, models, theories), Procedural (skills, algorithms, techniques, criteria for choosing them), and Metacognitive (strategy knowledge, knowledge of cognitive tasks, self-knowledge) — the last category newly admitted because the 1956 framework had no place for the demonstrable role of self-regulated learning (Anderson & Krathwohl, 2001; Pintrich, 2002, pp. 219-220). The Cognitive Process dimension renames the original six levels as gerunds (Remember, Understand, Apply, Analyze, Evaluate, Create) and reorders the top two so that Create — synthesis of a coherent whole — sits above Evaluate (Krathwohl, 2002, pp. 214-216). The operational artifact is the Taxonomy Table: a 4 × 6 grid into which any objective is classified by its verb and its noun, after which the matching cell guides what instruction and assessment must look like.

The framework's defensibility for runtime use comes from three claims that the revision argues explicitly. First, *meaningful* learning — the goal whenever transfer is wanted — requires cognitive processes beyond Remember; Mayer (2002, pp. 226-228) frames the distinction as retention (recall material in the form taught) versus transfer (use the material to solve a new problem) and argues that Understand through Create are the cells whose successful instruction produces transfer. Second, the Knowledge dimension matters independently of the Process dimension: the same verb ("apply") attached to factual knowledge ("apply the boldface limit value from Table 4-1") is operationally different from the same verb attached to procedural knowledge ("apply the troubleshooting algorithm to a fault you have not seen"), and assessments that ignore the Knowledge dimension routinely test recall of facts when the objective demanded application of a procedure (Airasian & Miranda, 2002, pp. 250-252). Third, alignment is the empirical predictor of instructional effectiveness: when the Taxonomy Table is used to locate the cells of objective, instruction, and assessment, mismatches become visible and correctable (Krathwohl, 2002, pp. 216-218; Airasian & Miranda, 2002, pp. 252-253).

The framework's principal known boundary condition is verb-list overreach. Stanny (2016) analyzed 30 published "Bloom's verb" lists and found that not one verb was assigned to the same cognitive level by all 30, and that three verbs (choose, relate, select) appeared at every one of the six levels depending on the list — i.e., the verb alone does not classify the objective; the noun (knowledge type) and the cognitive demand of the task jointly do. Crowe, Dirks, and Wenderoth (2008) operationalized this caution in the Blooming Biology Tool, a rubric that classified ~600 biology exam items by reading the question's task rather than its surface verb; raters who used the rubric agreed substantially while raters relying on verb lists alone did not. The taxonomy is a strong framework when applied to the task's *cognitive demand*; it is weak when applied to the surface verb of the objective sentence.

## When to apply

- **Objective drafted** — Whenever a learning objective is being written, classify it on the Taxonomy Table before accepting it. Identify the noun (knowledge type) and the verb-as-cognitive-demand (process). If either is ambiguous, the objective is not yet operational.
- **Assessment item drafted** — Before any item is finalized, locate it on the Taxonomy Table and confirm the cell matches the objective's cell. A "Create" objective measured by a "Remember" item is the most common alignment failure and is detectable here (Airasian & Miranda, 2002).
- **Segment boundary** — At the end of a coherent instructional segment, check whether the practice that occurred in the segment hit the cell the objective named. If the objective was Apply / Procedural and practice was Remember / Factual, the segment did not teach what it claimed.
- **Alignment check requested** — When a course, module, or lesson is being audited (curriculum review, accreditation, hand-off to a different tutor), produce the cell map: objective cell, instruction cell, assessment cell, side by side. Mismatches are the audit's findings.
- **Cognitive level mismatch suspected** — When a learner masters the assessment but cannot perform on the job, or fails the assessment despite demonstrably knowing the material, suspect a cell mismatch and check the table before redesigning content.
- **New tutor onboarding to a domain** — When a tutor is being calibrated to a domain pack (Library B), the Taxonomy Table is the lingua franca for stating what each objective in the pack actually demands cognitively, independent of the domain's surface vocabulary.

## When NOT to apply

- **Learner is at first exposure to a high-element-interactivity concept** — The taxonomy classifies the destination, not the path. Demanding Apply / Procedural performance from a learner who has not yet built the underlying schemas is a [cognitive-load-theory](../01-learning-science/cognitive-load-theory.md) failure, not a taxonomy success. Use [worked-example-effect](../01-learning-science/worked-example-effect.md) and faded examples to reach the cell, then assess at the cell.
- **Material is high-interactivity with no scaffolding present** — Classifying an objective at Analyze / Conceptual is correct but inert if the instruction supplied no Understand / Conceptual building blocks. The taxonomy will name the gap; it will not fill it.
- **Pure motor-skill acquisition phase** — Bloom's framework is built for declarative and conceptual learning. Torque-feel, swing-mechanics, and other motor skills have their own bottlenecks (proprioception, timing) that the cognitive-process levels do not capture; classifying them on the table forces a false fit. Use the table for the declarative content embedded in the motor task, not the motor execution.
- **Objective is being chosen by surface-verb only** — If the team is using a "Bloom's verbs" list to assign levels, stop. Stanny (2016) showed verbs do not classify levels reliably; classify by the cognitive demand of the task itself, not by the verb in the sentence.
- **The framework is being used to gate instruction, not align it** — Refusing to teach Remember-level content because "we want higher-order thinking" misreads the taxonomy. The lower cells are prerequisites for the upper cells; the framework's prescription is alignment of cell-to-cell, not avoidance of lower cells.

## How to apply

- **Classify by noun and verb, not by verb alone** — Read the objective and identify both the knowledge type (the *what*) and the cognitive process (the *do-what-with-it*). "Apply Ohm's law" is Apply / Conceptual; "apply the IFR-6000 ramp test procedure" is Apply / Procedural; the practice and assessment look different (Stanny, 2016; Crowe, Dirks, & Wenderoth, 2008).
- **Place the cell, then build backward** — Once the target cell is identified, [backward-design-ubd](../02-instructional-design/backward-design-ubd.md) supplies the rest: write an assessment item in that cell, then choose instruction that takes the learner from current cell to target cell. Skipping this step is how Apply objectives end up assessed by Remember items (Airasian & Miranda, 2002).
- **Use the table as a diagnostic when something is off** — When learners pass assessments but fail in performance, place the assessment items and the performance task on the table side-by-side. The cell mismatch usually localizes the failure (typically: assessment is Remember / Factual, performance demands Apply / Procedural).
- **Hit Understand before Apply for conceptual material** — Apply / Conceptual rests on Understand / Conceptual. A learner who has memorized a definition (Remember / Conceptual) but cannot summarize it in their own words has not yet reached Understand; demanding Apply now produces brittle pattern-matching (Mayer, 2002, pp. 228-230). [self-explanation-elaborative-interrogation](../01-learning-science/self-explanation-elaborative-interrogation.md) is the workhorse move for crossing into Understand.
- **Treat metacognitive knowledge as a teachable cell** — Strategy knowledge ("when do I use a divide-and-conquer trace versus a binary search of the schematic?") is Procedural × Metacognitive on the table; it is taught by surfacing strategy choices, not by hoping learners infer them (Pintrich, 2002, pp. 222-224).
- **Stage practice up the cells, not down** — A segment's practice should land at or just below the target cell. Practice exclusively at lower cells produces fluency without transfer; practice solely at the target cell from cold start produces frustration without schema (Mayer, 2002).
- **Document the cell on each objective** — Tag every objective in the domain pack with its (Knowledge, Process) cell. The runtime can then route by cell: items at Apply / Procedural go to procedural-practice modes, items at Evaluate / Conceptual go to discussion or Socratic prompts.

## Common misapplications

- **Verb-list classification** — Treating a verb list as authoritative when Stanny (2016) demonstrated those lists disagree wholesale on level. The verb suggests; the task's cognitive demand classifies.
- **Hierarchy as ladder of "good"** — Reading the six processes as a moral hierarchy ("higher-order good, lower-order bad") rather than as classification. Remember / Factual is the right cell for terminology, regulatory limits, and call-out values; teaching them as if Apply were always preferred wastes time and weakens the foundation.
- **Skipping the Knowledge dimension** — Using the six processes alone and ignoring the four knowledge types. The original 1956 hierarchy was one-dimensional; the revised taxonomy's operational power comes from the second dimension. A 1-D classification is the un-revised taxonomy in disguise (Krathwohl, 2002).
- **Mismatched assessment** — The most common operational error: an Apply / Procedural objective measured by a Remember / Factual multiple-choice item. The objective writes a check the assessment cannot cash. See [bloom-levels-in-assessment](../03-assessment-science/bloom-levels-in-assessment.md) for item-format implications by cell.
- **Treating Create as decoration** — Putting "Create" objectives into a course because the framework lists six levels. Create / Conceptual is appropriate when the domain has a genuine synthesis task; manufacturing one to "use the top of Bloom's" is theatre.
- **Conflating difficulty with cognitive level** — A Remember item can be hard (obscure fact, dense distractors) and a Create item can be easy (free-form list with no constraints). Difficulty is a separate dimension; the table classifies kind of cognition, not amount of effort.
- **Inferring metacognitive instruction from metacognitive objectives without teaching it** — Listing "self-monitor your progress" as an objective without ever modeling the strategy is a common failure mode. Metacognitive knowledge is taught explicitly (Pintrich, 2002, pp. 222-224).

## Examples across domains

**Avionics — pitot/static system leak-check on a Beechcraft King Air after a static-port repaint.**

*Setup.* A second-year technician is being trained on the periodic-maintenance leak check for the pitot-static system after the static ports have been repainted. The shop's stated objective reads: "The technician will perform the FAR 91.411-required static system leak check using a Barfield 1811NG tester." The shop's current assessment is a 10-item multiple-choice quiz on tester nomenclature and limit values. Before training begins, the tutor places the objective on the Taxonomy Table.

*Cell map and intervention.* The objective is Apply / Procedural — the verb "perform" with the noun "leak check procedure". The current assessment sits in Remember / Factual — recognition of nomenclature and limits. The cells do not match: passing the assessment does not predict performing the check. The tutor proposes a parallel-cell assessment (an actual or simulated tester run scored against accept/reject criteria) and rebuilds practice up the cells: Remember / Factual ("what is the maximum allowable leak rate at 1,000 feet altitude differential?"), then Understand / Conceptual ("explain *why* a 100-foot/minute leak fails — what does it imply about the static pressure reaching the altimeter?"), then Apply / Procedural on the bench tester with corrective feedback. The procedural Metacognitive cell is hit explicitly: "when you see an out-of-tolerance reading, what do you check first and why?" — strategy knowledge that is otherwise absorbed accidentally or not at all (Pintrich, 2002).

*Verification.* On the practical, the technician's first three runs produce two correct accept/reject calls and one missed leak diagnosed in post-test review. Cell-aligned assessment surfaces the gap; the prior multiple-choice quiz would have rated the technician "ready" while the bench performance was not.

**Mortgage / financial services sales — pricing a refinance for a customer with mixed credit, two income streams, and a recent foreclosure on a co-signed property.**

*Setup.* A new loan officer at a mid-size lender is being onboarded on conforming-conventional refinance pricing. The training objective is "Quote a refinance rate and product mix that meets investor guidelines and the customer's payment goal." The compliance team's existing assessment is an open-book multiple-choice quiz on Fannie Mae/Freddie Mac eligibility cutoffs and LLPA tables. The supervisor sits the objective on the Taxonomy Table during onboarding design.

*Cell map and intervention.* The objective is Evaluate / Procedural with a Create / Procedural component when product mixing is required — the loan officer must judge multiple program options against guidelines *and* construct a payment-and-product combination the customer will accept. The current assessment sits in Remember / Factual (recognize the cutoff numbers) and at most Apply / Factual (look up an LLPA value). The cell mismatch is the entire reason new officers pass the quiz and then quote losing scenarios in front of customers. The supervisor adds two parallel-cell exercises: a structured price-and-justify task on five anonymized real applications graded against the actual investor lock that came back, and a paired Create / Procedural exercise where the officer must build two product combinations (e.g., 30-year fixed vs. 7/1 ARM with rate buy-down) and defend the trade-off. Metacognitive Procedural is taught explicitly: "what cue tells you to *stop* trying to fit conforming and route to non-QM?" — the strategy decision that is the difference between a closed loan and a wasted week.

*Verification.* Across the next ten live applications the new officer's quote-to-lock variance drops from ±37 basis points to ±9 basis points and the rate of mid-process program switches falls by half. The Apply-and-Evaluate-cell practice produced transfer; the prior Remember-cell assessment would never have surfaced the gap.

## Quality signal

The AI tutor knows the Taxonomy Table is being used well when the cell of every active objective, the cell of the practice the learner just completed, and the cell of the next assessment item all agree — and when, in cases of learner failure, the cell map localizes the failure to a specific mismatch (assessment cell ≠ objective cell, or practice cell ≠ assessment cell) rather than producing a vague "the learner needs more practice." A weaker but faster confirmatory signal is that classifications survive rater check: when two raters classify the same objective independently using the task's cognitive demand (Crowe, Dirks, & Wenderoth, 2008) they agree on the cell at least ~80% of the time. If raters disagree below that rate, the objective is under-specified, not the rubric — rewrite the objective.

## Cross-references

- See [backward-design-ubd](../02-instructional-design/backward-design-ubd.md) for the design process that places the assessment in the same cell as the objective before any instruction is written.
- See [bloom-levels-in-assessment](../03-assessment-science/bloom-levels-in-assessment.md) for item-format and stem-design implications of each cell on the Taxonomy Table.
- See [mastery-threshold-transfer-test-design](../03-assessment-science/mastery-threshold-transfer-test-design.md) for how the cell distinction between retention and transfer maps onto separate test designs.
- See [item-writing-rules](../03-assessment-science/item-writing-rules.md) for how stem and option construction differ across cells (Remember vs. Apply vs. Evaluate).
- See [transfer-of-learning](../01-learning-science/transfer-of-learning.md) for the empirical evidence behind Mayer's (2002) retention-vs-transfer distinction the table operationalizes.
- See [schema-theory-knowledge-components](../01-learning-science/schema-theory-knowledge-components.md) for the long-term-memory architecture that the Knowledge dimension's four types sit on top of.
- See [merrills-first-principles](../02-instructional-design/merrills-first-principles.md) for a complementary instructional model that aligns naturally with cell-targeted practice.
- See [knowledge-graph-traversal](../07-runtime-decisions/knowledge-graph-traversal.md) for how the runtime can route between cells when remediation or stretch is needed.
- See [mastery-thresholds](../07-runtime-decisions/mastery-thresholds.md) for how cell-tagged items determine which performance bar advances or remediates a learner at each cognitive level.
