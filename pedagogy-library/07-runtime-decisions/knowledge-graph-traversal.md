---
id: knowledge-graph-traversal
title: Knowledge Graph Traversal
category: 07-runtime-decisions
aliases: [kc-graph-routing, prerequisite-graph-traversal, curriculum-sequencing]
evidence_strength: strong
# effect_size is null because knowledge graph traversal is a routing rule —
# a graph-search method that picks the next KC to teach given a prerequisite
# structure and per-KC mastery estimates — not a treatment whose effect is
# measured against a control. Magnitude evidence appears in the components
# the traversal composes (KC decomposition gains in Cen, Koedinger & Junker
# 2006; ITS effectiveness in VanLehn 2011, d ≈ 0.76), reported in context.
effect_size: null
key_sources:
  - "Koedinger, K. R., Corbett, A. T., & Perfetti, C. (2012). The knowledge-learning-instruction framework: Bridging the science-practice chasm to enhance robust student learning. Cognitive Science, 36(5), 757-798. doi:10.1111/j.1551-6709.2012.01245.x"
  - "Corbett, A. T., & Anderson, J. R. (1995). Knowledge tracing: Modeling the acquisition of procedural knowledge. User Modeling and User-Adapted Interaction, 4(4), 253-278. doi:10.1007/BF01099821"
  - "Brusilovsky, P., & Vassileva, J. (2003). Course sequencing techniques for large-scale web-based education. International Journal of Continuing Engineering Education and Lifelong Learning, 13(1-2), 75-94. doi:10.1504/IJCEELL.2003.002154"
  - "VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. Educational Psychologist, 46(4), 197-221. doi:10.1080/00461520.2011.611369"
  - "Cen, H., Koedinger, K. R., & Junker, B. (2006). Learning factors analysis – A general method for cognitive model evaluation and improvement. In M. Ikeda, K. Ashley, & T.-W. Chan (Eds.), Intelligent Tutoring Systems (Lecture Notes in Computer Science, Vol. 4053, pp. 164-175). Berlin: Springer. doi:10.1007/11774303_17"
  - "Pavlik, P. I., Cen, H., & Koedinger, K. R. (2009). Performance factors analysis – A new alternative to knowledge tracing. In V. Dimitrova, R. Mizoguchi, B. du Boulay, & A. Graesser (Eds.), Artificial Intelligence in Education (pp. 531-538). Amsterdam: IOS Press."
  - "Pelánek, R., & Řihák, J. (2017). Experimental analysis of mastery learning criteria. In Proceedings of the 25th Conference on User Modeling, Adaptation and Personalization (UMAP '17) (pp. 156-163). New York: ACM. doi:10.1145/3079628.3079667"
last_reviewed: 2026-04-30
applies_to: [sequencing, decision]
contraindicated_when:
  - material.uncalibrated_item_pool
  - learner_state.first_exposure
  - task_type.motor_acquisition
  - material.high_element_interactivity_no_scaffolding
runtime_triggers:
  - kc_mastered
  - prerequisite_graph_loaded
  - next_topic_decision_due
  - remediation_target_required
  - session_start_route_check
related: [schema-theory-knowledge-components, bayesian-knowledge-tracing, performance-factor-analysis, mastery-thresholds, sm2-fsrs, item-difficulty-discrimination, zpd-operationalization, transfer-of-learning]
---

# Knowledge Graph Traversal

## One-line claim

Route the learner across a directed prerequisite graph of knowledge components by picking the next KC whose prerequisites are mastered and whose own mastery probability is below threshold, so each next move sits in the narrow band where prior knowledge supports new learning and additional practice still has measurable headroom.

## Evidence base

Knowledge graph traversal operationalizes the Knowledge-Learning-Instruction framework's central commitment: that target performance decomposes into a network of named knowledge components (KCs) whose prerequisite relations are themselves the unit of instructional sequencing (Koedinger, Corbett, & Perfetti, 2012, pp. 759-768). The graph encodes "KC B requires KC A" as a directed edge; runtime traversal picks the next KC to teach by composing two signals — graph eligibility (every prerequisite KC is at or above mastery threshold) and learner need (the candidate KC's own mastery probability is below threshold). The mastery probabilities come from a per-KC estimator: Bayesian Knowledge Tracing (Corbett & Anderson, 1995, pp. 256-262) or a logistic alternative such as Performance Factors Analysis (Pavlik, Cen, & Koedinger, 2009, pp. 533-535). The traversal rule itself is a graph-search policy on top of those estimates, not a separate treatment.

The evidence that this composition produces durable learning runs through two literatures. Brusilovsky and Vassileva (2003) demonstrated in *International Journal of Continuing Engineering Education and Lifelong Learning* that prerequisite-driven course sequencing in adaptive hypermedia generated individualized learning paths whose efficiency depended on the fidelity of the prerequisite graph; their DCG and CoCoA systems showed that page-order delivery — material in source-manual order rather than prerequisite order — degraded outcomes (Brusilovsky & Vassileva, 2003, pp. 78-87). VanLehn's (2011) review in *Educational Psychologist* synthesized the cumulative ITS evidence: step-based and substep-based intelligent tutoring systems, which by design route students through prerequisite KC graphs, achieved a mean effect of d = 0.76 versus no-tutoring controls — close to the d = 0.79 he found for human one-on-one tutors (VanLehn, 2011, pp. 209-213). When KCs were aggregated into coarse "topics" rather than tracked individually, prediction accuracy fell and remediation became diffuse (Cen, Koedinger, & Junker, 2006, pp. 167-172).

The framework has well-documented boundary conditions. Cen, Koedinger, and Junker (2006) showed that an incorrect KC decomposition — wrong granularity, missing prerequisites, conflated KCs — propagates through the traversal and produces sequences that look adaptive but are not; their Learning Factors Analysis procedure exists precisely to detect and repair such mis-decompositions against student data. Pelánek and Řihák (2017) reported in *UMAP '17* that mastery-threshold choices dominate routing behavior more than the modeling technique itself: too low advances learners with shallow knowledge; too high, learners loop on already-mastered KCs while down-graph topics starve. The traversal is only as good as the graph it walks and the threshold at each node — both must be maintained against learner data.

## When to apply

- **A KC is mastered** — When the per-KC estimator crosses the advancement threshold (e.g.,
  BKT P(L) ≥ 0.95 or three correct in a row per Pelánek & Řihák), recompute eligibility and
  pick the next KC whose prerequisites all meet threshold and whose own mastery is below it.
- **Prerequisite graph loaded for a new domain** — At module start the graph is the curriculum;
  traversal selects an entry KC with no unmet prerequisites. The manual's chapter order is a
  hint, not the schedule.
- **Next-topic decision due** — When the runtime must decide what to teach next and a KC graph
  exists, route through the graph rather than a fixed sequence.
- **Remediation target required** — When a downstream KC fails repeatedly, traverse upstream
  to find prerequisites whose mastery has decayed or was never high; remediate upstream before
  re-attempting the failing KC.
- **Session start route check** — Recompute mastery on key prerequisites (forgetting between
  sessions degrades them — see
  [forgetting-curve](../01-learning-science/forgetting-curve.md)) before resuming traversal; a
  KC mastered last week may need a retrieval probe before the graph treats it as eligible.

## When NOT to apply

- **The KC graph is uncalibrated** — A graph encoded once from a source manual and never
  tested against learner response patterns is a hypothesis, not a prerequisite structure. Cen,
  Koedinger, and Junker (2006) showed mis-decomposed KCs and missing edges propagate through
  the traversal; route only after Learning Factors Analysis (or equivalent) confirms the
  structure predicts errors.
- **Learner is at first exposure with no schemas yet built** — Traversal assumes some KCs are
  mastered so others become eligible. With no entry-KC mastery the eligible set collapses to
  the root; pre-training and worked examples are the right move
  ([worked-example-effect](../01-learning-science/worked-example-effect.md)), not graph search.
- **Pure motor-skill acquisition phase** — Procedural-motor execution does not decompose into
  declarative KCs the traversal can route over. Conceptual scaffolding around the motor task
  can be graph-routed; the motor skill itself is governed by feedback loops outside this rule.
- **Material is high-element-interactivity with no scaffolding** — When every probe item taps
  three KCs at once the traversal cannot disambiguate which prerequisite failed. Build
  separable probes first ([schema-theory-knowledge-components](../01-learning-science/schema-theory-knowledge-components.md))
  or accept that the domain needs holistic 4C/ID-style task-class progression instead.
- **Mastery threshold is mis-specified** — Pelánek and Řihák (2017) showed threshold choice
  dominates routing. Without thresholds validated on cohort data (does P(L) = 0.95 predict
  retention at +7 days?), the graph advances too early or loops too long; calibrate first.

## How to apply

- **Compute the eligible-KC frontier on every routing decision** — Eligible = (every
  prerequisite mastery ≥ threshold) AND (own mastery < threshold). Recompute after each scored
  response; advancing one KC reshapes the frontier.
- **Pick from the frontier by readiness, not arbitrarily** — Prefer the KC nearest the working
  edge (smallest gap to threshold) or with the largest downstream fan-out so the unblocked
  subgraph widens fastest after mastery. Pure topological order ignores both.
- **Use one per-KC mastery estimator the graph can query** — BKT (Corbett & Anderson, 1995)
  gives P(L) per KC from binary responses; PFA (Pavlik, Cen, & Koedinger, 2009) uses logistic
  regression and handles multi-KC items cleanly. Pick one — mixing muddies threshold
  semantics.
- **Calibrate the advancement threshold on cohort data** — Pelánek and Řihák (2017) found
  threshold choice swamps estimator choice. Set it against retention at the target delay
  (predicting +7-day recall ≥ 80%) rather than picking P(L) = 0.95 by convention.
- **Traverse upstream for remediation before downstream re-attempts** — When KC X fails after
  ostensible mastery, query mastery on X's prerequisites; decayed upstream KC is the usual
  culprit. Remediate upstream, then retry X.
- **Re-probe prerequisites at session start** — Run a brief retrieval probe on the immediate
  prerequisites of the next eligible KC; if any has slipped, route there first. Pair with
  [sm2-fsrs](../07-runtime-decisions/sm2-fsrs.md) for scheduling.
- **Maintain the graph against student data** — When residuals are systematically explained by
  an unlisted prerequisite, add the edge; when responses split cleanly within one KC, split it
  (Cen, Koedinger, & Junker, 2006). The graph is a living artifact.

## Common misapplications

- **Treating page order as prerequisite order** — Source manuals are written for authoring
  convenience, not prerequisite topology. A textbook's chapter sequence frequently violates
  the actual graph; trusting page order is the most common silent degradation.
- **Routing on aggregate "topic mastery"** — A learner at 80% on a topic test has mastered
  four of five KCs. The topic average advances them to a downstream topic dependent on the
  missing fifth; per-KC tracking surfaces this, topic averages hide it (Cen, Koedinger, &
  Junker, 2006).
- **Frozen graphs that ignore residual error patterns** — A graph authored once and never
  updated accumulates wrong edges. Learning Factors Analysis exists because graphs are
  hypotheses; treat them as such.
- **Greedy single-step routing without horizon** — Picking the nearest-edge KC every step can
  starve down-graph KCs whose prerequisites stay perpetually one short. Look one or two hops
  ahead when ties are close, or randomize within the top-k.
- **Thresholds set by convention, not calibration** — Pelánek and Řihák (2017) showed routing
  depends more on the threshold than on the estimator; uncalibrated thresholds route on noise.
- **Confusing transfer with prerequisite mastery** — A learner can pass graph-internal probes
  and still fail novel-context problems if KCs are surface-bound
  ([transfer-of-learning](../01-learning-science/transfer-of-learning.md)).

## Examples across domains

**Avionics — installing a Garmin GTN 750 navigator with GPS-source assertion to an existing GTX 33ES transponder.**

*Setup.* The shop's training platform encodes the GTN 750 install as ~40 KCs: pinout
interpretation, antenna-isolation calculations, RAIM/SBAS configuration, GPS-source
assertion, ADS-B Out compliance fields (NIC/NACp), and IFR-6000 ramp verification. The
technician arrives with three KCs mastered (basic pinout, breaker selection, antenna
placement); the rest unknown.

*Traversal.* The frontier of KCs whose only prerequisite is "basic pinout" is power/ground
harness, MFD interconnect, dataport configuration. The runtime picks "power/ground harness"
first — six KCs unblock on its mastery. After BKT P(L) crosses 0.95 on three correct probes,
the frontier expands to include "GPS-source pinout to GTX 33ES". The technician fails
repeatedly on "ADS-B NIC/NACp asserted" three KCs downstream; the runtime traverses upstream
and finds "GPS source asserts integrity" — a listed prerequisite — decayed to P(L) = 0.62
between sessions. Remediating that node and re-attempting the downstream KC passes.

*Calibration.* Cohort data (n = 1,800 prior technicians) showed +7-day recall at 84% at
P(L) = 0.95 and plateauing past 0.97, so the threshold stays. The graph was revised when
residuals showed "antenna-isolation calculation" splitting into near-field and far-field
subgroups (Cen, Koedinger, & Junker, 2006); the "ADS-B antenna placement" edge was rewired
to far-field only.

**Genealogy research — tracing a Famine-era Irish-immigrant ancestor across U.S. census, naturalization, and parish records.**

*Setup.* A volunteer at a county genealogical society is learning to evaluate primary
sources. The KC graph encodes ~25 KCs: primary vs. derivative sources, 19th-century
secretary-hand conventions, census ditto marks and abbreviations, naturalization declaration
vs. petition, Catholic parish baptismal registers by townland, and the five components of
the Genealogical Proof Standard. The volunteer arrives with "primary vs. derivative"
mastered; the rest unknown.

*Traversal.* The opening frontier — KCs whose only prerequisite is "primary vs. derivative" —
is ditto-mark conventions, naturalization document types, parish-register Latin
abbreviations. The runtime picks ditto-mark conventions first; four downstream KCs
(decade-over-decade household tracking, surname variation, immigration-year inference) depend
on it. After mastery, the volunteer attempts "GPS reasonably exhaustive search" four KCs
downstream and fails: the prerequisite "Irish townland-to-civil-parish mapping" sits at
P(L) = 0.40, never having been probed. The runtime traverses upstream, remediates townland
mapping on three new instances (Skibbereen → Creagh civil parish), and the search succeeds.

*Calibration.* The cohort is small (~120 volunteers/year) and most probes touch two or three
KCs at once, so PFA was chosen over BKT for multi-KC handling (Pavlik, Cen, & Koedinger,
2009, pp. 533-535). The threshold was retuned against next-session retention; P(L) = 0.95
over-advanced and was lowered to a logit-equivalent predicting +14-day recall ≥ 80%. The
graph was revised when residuals showed secretary-hand reading split between census clerks
(English) and parish priests (Latin/Irish) — into two KCs.

## Quality signal

Graph traversal is working when (a) downstream KC failure rates correlate with upstream mastery — learners who mastered prerequisite A succeed on dependent KC B at a rate at least 20 percentage points above those who did not, confirming the edge A → B is load-bearing; (b) advancing past the threshold predicts retention at the target delay within ~10 percentage points (Pelánek & Řihák, 2017); and (c) the eligible-KC frontier stays in a 3–8 KC band. A frontier collapsing to one means the graph is overly chained; ballooning past 15 means the prerequisite encoding is too sparse to constrain routing.

## Cross-references

- See [schema-theory-knowledge-components](../01-learning-science/schema-theory-knowledge-components.md) for the underlying KC decomposition the traversal walks; the graph is a routing structure on top of that decomposition.
- See [bayesian-knowledge-tracing](../07-runtime-decisions/bayesian-knowledge-tracing.md) for the per-KC mastery estimator the traversal queries to decide eligibility.
- See [performance-factor-analysis](../07-runtime-decisions/performance-factor-analysis.md) for the logistic alternative that handles multi-KC items more cleanly than BKT.
- See [mastery-thresholds](../07-runtime-decisions/mastery-thresholds.md) for how to set the advancement cut-point that gates traversal across each edge.
- See [sm2-fsrs](../07-runtime-decisions/sm2-fsrs.md) for the spacing scheduler that re-probes upstream KCs across days and weeks so traversal can detect decay between sessions.
- See [item-difficulty-discrimination](../07-runtime-decisions/item-difficulty-discrimination.md) for picking the probe item once the traversal has selected the next KC.
- See [zpd-operationalization](../07-runtime-decisions/zpd-operationalization.md) for the working-edge framing the eligible-KC frontier operationalizes.
- See [transfer-of-learning](../01-learning-science/transfer-of-learning.md) for why threshold-passing on graph-internal probes does not guarantee transfer; varied-context retrieval is a separate gate.
