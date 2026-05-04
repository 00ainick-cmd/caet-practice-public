---
id: concept-mapping
title: Concept Mapping
category: 04-delivery-patterns
aliases: [concept-maps, knowledge-maps, node-link-diagrams]
evidence_strength: strong
effect_size: "Hedges' g ≈ 0.58 overall for learning with concept maps vs. comparison conditions, with construction (g = 0.72) outperforming study-only (g = 0.43) (Schroeder, Nesbit, Anguiano & Adesope 2018, 142 effects, n = 11,814); earlier Nesbit & Adesope (2006) reported d ≈ 0.4–0.7 across 67 effects depending on use and comparison; retrieval practice outperforms concept-map study by d ≈ 1.50 on delayed inference tests (Karpicke & Blunt 2011)"
key_sources:
  - "Nesbit, J. C., & Adesope, O. O. (2006). Learning with concept and knowledge maps: A meta-analysis. *Review of Educational Research*, 76(3), 413-448. doi:10.3102/00346543076003413"
  - "Schroeder, N. L., Nesbit, J. C., Anguiano, C. J., & Adesope, O. O. (2018). Studying and constructing concept maps: A meta-analysis. *Educational Psychology Review*, 30(2), 431-455. doi:10.1007/s10648-017-9403-9"
  - "Novak, J. D., & Cañas, A. J. (2008). The theory underlying concept maps and how to construct and use them. Technical Report IHMC CmapTools 2006-01 Rev 01-2008. Florida Institute for Human and Machine Cognition."
  - "Karpicke, J. D., & Blunt, J. R. (2011). Retrieval practice produces more learning than elaborative studying with concept mapping. *Science*, 331(6018), 772-775. doi:10.1126/science.1199327"
  - "O'Donnell, A. M., Dansereau, D. F., & Hall, R. H. (2002). Knowledge maps as scaffolds for cognitive processing. *Educational Psychology Review*, 14(1), 71-86. doi:10.1023/A:1013132527007"
  - "Ruiz-Primo, M. A., & Shavelson, R. J. (1996). Problems and issues in the use of concept maps in science assessment. *Journal of Research in Science Teaching*, 33(6), 569-600. doi:10.1002/(SICI)1098-2736(199608)33:6<569::AID-TEA1>3.0.CO;2-M"
  - "Mintzes, J. J., Wandersee, J. H., & Novak, J. D. (1997). Meaningful learning in science: The human constructivist perspective. *Educational Psychologist*, 32(4), 405-414. doi:10.1207/s15326985ep3204_4"
last_reviewed: 2026-04-30
applies_to: [acquisition, retention, transfer]
contraindicated_when:
  - learner_state.first_exposure
  - learner_state.high_prior_knowledge
  - material.high_element_interactivity_no_scaffolding
  - task_type.motor_acquisition
runtime_triggers:
  - new_topic_with_many_interrelated_concepts
  - misconception_diagnosis_needed
  - segment_summary_required
  - prior_knowledge_assessment
  - cross_topic_integration_point
related: [dual-coding, schema-theory-knowledge-components, self-explanation-prompts, predict-before-reveal, testing-effect, transfer-of-learning, cognitive-load-theory, expertise-reversal]
---

# Concept Mapping

## One-line claim

Asking the learner to externalize a topic as a node-link diagram — concepts in boxes, labeled relationships on the lines, hierarchically organized around a focus question — produces measurable gains in retention and transfer when the learner constructs the map themselves, and surfaces misconceptions and missing links that no prose summary or recognition test will reveal.

## Evidence base

Concept maps were introduced by Novak and colleagues in the 1970s as a tool to externalize Ausubel's idea that meaningful learning occurs when new propositions are subsumed into a hierarchically organized cognitive structure (Mintzes, Wandersee, & Novak, 1997, pp. 408-411). The canonical construction rules — concepts in nodes, labeled linking phrases on the connecting lines, hierarchical layout from general at the top to specific below, cross-links between branches — and the theoretical grounding in assimilation theory and constructivist epistemology are laid out in Novak and Cañas (2008). The defining feature, distinguishing concept maps from mind maps and other free-form diagrams, is that every line carries a labeled relation; the map represents propositions, not just associations, and is therefore evaluable for accuracy.

Two meta-analyses anchor the effect size. Nesbit and Adesope (2006) synthesized 67 effects from 55 studies (n = 5,818) in the *Review of Educational Research*, reporting that learning with concept maps produced reliable gains over text-only and lecture-only comparisons, with means ranging from small to large depending on whether learners constructed maps versus studied prepared maps and on the comparison treatment (Nesbit & Adesope, 2006, pp. 425-435). Schroeder, Nesbit, Anguiano, and Adesope (2018) updated and broadened the synthesis in *Educational Psychology Review*, pooling 142 effects (n = 11,814) and reporting an overall Hedges' g of 0.58, with map construction (g = 0.72) outperforming map study (g = 0.43) and the advantage holding across STEM and non-STEM domains, K–12 through postsecondary, and against multiple comparison conditions including reading, lecture, and discussion. O'Donnell, Dansereau, and Hall's (2002) review in *Educational Psychology Review* clarified the mechanism: knowledge maps offload spatial structure to the visual channel and benefit low-prior-knowledge and low-verbal-ability learners disproportionately, but only when learners actively process the map (annotation, summarization, generation) rather than passively viewing it.

The principal boundary condition was demarcated by Karpicke and Blunt (2011) in *Science*. Across two experiments with college students learning expository science texts, retrieval practice (free-recall study cycles) produced final-test recall and inference performance roughly 1.5 standard deviations above elaborative study with concept mapping at one-week delay, including when the criterial test was itself a concept-mapping task. The finding does not invalidate concept mapping; it constrains it. Mapping is an encoding/elaboration operation, not a retrieval operation, and study-with-maps without a retrieval phase cannot match retrieval practice on long-delay outcomes. Concept mapping pays its largest dividends when the act of mapping is itself effortful generation — building the map from memory, repairing a wrong link, defending a cross-link — and when it is followed by retrieval practice on the same propositions (see [testing-effect](../01-learning-science/testing-effect.md)). Ruiz-Primo and Shavelson (1996) further sharpened the assessment use case: low-directed maps (learner picks concepts, links, and structure) are sensitive to misconceptions but unreliable across raters; higher-directed maps (concepts and structure provided, learner supplies links) trade some sensitivity for reliability.

## When to apply

- **New topic spans many interrelated concepts** — When the target content is a system, taxonomy,
  or causal network with at least 6–10 concepts and non-trivial relationships, ask the learner to
  map the structure rather than narrate it; construction is where the largest effects sit
  (Schroeder et al., 2018, g = 0.72).
- **Misconception diagnosis is needed** — Maps externalize what the learner believes the structure
  is. Wrong links, missing nodes, and miscategorized cross-links are visible in seconds; the same
  errors are nearly invisible in free recall or multiple-choice (Mintzes et al., 1997).
- **Segment summary is required** — At the close of a multi-concept lesson, a concept map is a
  denser summary than a paragraph and forces the learner to commit to specific relations.
- **Prior knowledge needs to be surfaced** — Before introducing material that builds on existing
  schema, ask for a quick map of what the learner already knows; the map is both a baseline and
  a scaffold the new concepts will hook into (Novak & Cañas, 2008; O'Donnell et al., 2002).
- **Cross-topic integration point** — When two previously separate units must now be connected
  (e.g., transponder operation + ADS-B compliance), an updated map with cross-links between the
  branches makes the integration explicit rather than hoped-for.

## When NOT to apply

- **Learner is in first exposure to the constituent concepts** — Mapping requires concepts to map.
  Asking a learner to map content they have not yet encoded produces structurally empty diagrams
  and frustration (Novak & Cañas, 2008, on the "expert skeleton" prerequisite). Build the basic
  propositions first, then map.
- **Learner already has a robust schema for the domain** — A senior technician who has internalized
  the system gets little from drawing it again; the redundant scaffold imposes load without
  learning gain. See [expertise-reversal](../01-learning-science/expertise-reversal.md). Switch to
  retrieval and transfer tasks instead.
- **Content has high element interactivity and no scaffolding is yet in place** — Free-form mapping
  of densely interconnected new material overloads working memory before any structure has formed.
  Use a partially completed (expert-skeleton) map or a worked-example map first; have the learner
  extend rather than originate.
- **Pure motor-skill acquisition** — Procedural motor learning (soldering technique, intubation
  hand mechanics, instrument fingering) is not what mapping addresses. The declarative content
  embedded in such tasks (failure modes, decision rules) can be mapped; the motor execution
  cannot.
- **Long-delay retention is the criterion and no retrieval phase will follow** — Mapping alone
  does not produce the long-delay gains retrieval practice does (Karpicke & Blunt, 2011, d ≈ 1.50).
  If the criterion is one-week-plus retention, mapping must be paired with retrieval; mapping in
  isolation is the wrong tool for that goal.

## How to apply

- **Anchor every map in a focus question** — Before any nodes are placed, name the question the
  map answers (e.g., "What signals must be present for a Mode S transponder to reply correctly?").
  The focus question disciplines inclusion: any concept that does not bear on the question is
  cut. Maps without focus questions degenerate into association webs (Novak & Cañas, 2008).
- **Prefer construction over study; require labeled links** — The construction advantage is
  approximately g = 0.72 versus g = 0.43 for studying prepared maps (Schroeder et al., 2018).
  Every line must carry a linking phrase ("causes", "depends on", "is a type of"); unlabeled
  arrows do not encode propositions and forfeit most of the effect.
- **Start novices with an expert-skeleton map** — Provide 6–10 anchor concepts in a partial
  hierarchy and have the learner add links and additional concepts (Novak & Cañas, 2008, on
  expert-skeleton concept maps). The scaffold prevents structurally empty maps without removing
  the generative work.
- **Pair the map with retrieval practice on the propositions** — After construction, close the map
  and ask the learner to free-recall five propositions it asserted, then re-open and check. This
  converts the encoding gain of mapping into a retention gain (see
  [testing-effect](../01-learning-science/testing-effect.md)) and addresses the Karpicke & Blunt
  (2011) boundary directly.
- **Score for cross-links and explanatory propositions, not node count** — A map with three branch
  cross-links and labeled causal relationships is a better signal of integration than a map with
  thirty unconnected nodes. Use a structural rubric (Ruiz-Primo & Shavelson, 1996) emphasizing
  proposition validity and cross-link quality over total nodes.
- **Treat the map as an iterated thinking artifact, not a one-shot deliverable** — Have the
  learner revise as new concepts arrive, repair wrong links when feedback identifies them, and
  annotate cross-links with one-sentence justifications (see
  [self-explanation-prompts](../04-delivery-patterns/self-explanation-prompts.md)).
- **Withdraw the scaffold as expertise grows** — Once the learner can reconstruct the structure
  from memory and reason fluently across branches, drop mapping; persisting it adds load without
  learning (see [expertise-reversal](../01-learning-science/expertise-reversal.md)).

## Common misapplications

- **Unlabeled arrows or word webs masquerading as concept maps** — A diagram with nodes and
  unlabeled lines is a mind map, not a concept map; it does not encode propositions and is not
  what the meta-analyses measured (Novak & Cañas, 2008). The labeled relation is load-bearing.
- **Studying a teacher-prepared map instead of constructing one** — Study-only mapping recovers
  about 60% of the construction effect (g = 0.43 vs 0.72; Schroeder et al., 2018). If retention
  is the goal, learners must build, not browse.
- **Using maps as a substitute for retrieval practice on long-delay outcomes** — Karpicke and
  Blunt (2011) showed concept-map study lost to retrieval practice by roughly d = 1.50 at one
  week. Mapping is encoding; retrieval is consolidation. Use both, in that order.
- **Grading maps by node or link count alone** — Quantity is a poor proxy; the diagnostic signal
  lives in the labeled propositions and the cross-links between branches (Ruiz-Primo &
  Shavelson, 1996).
- **Forcing free-form mapping on novices in a high-interactivity domain** — Without an expert
  skeleton, a first-encounter map collapses into noise (Novak & Cañas, 2008). Provide structure
  first, fade it as schema forms.

## Examples across domains

**Avionics — mapping the ADS-B Out compliance chain for a second-year apprentice.**

*Setup.* The apprentice has spent two sessions on Mode S transponders, GPS position sources, and
ADS-B Out reporting requirements. They can recite the components but cannot answer "if GPS HFOM
degrades during a flight, which compliance parameters fail and in what order?" The prerequisites
are encoded; the integration is not.

*Mapping move.* The tutor supplies an expert-skeleton map with six anchor nodes (GPS source,
HFOM, NIC, NACp, transponder, ground receiver) and the focus question "What must be true for
the broadcast to remain 2020-compliant?" The apprentice adds labeled links: "GPS source
*provides* HFOM"; "HFOM *determines* NIC"; "NIC *must exceed* threshold for compliance"; plus a
cross-link from "transponder failure" back to "broadcast absent". They repair two wrong links
(initially had NACp driving NIC; in fact each is computed independently) when the tutor probes
"what does the receiver actually see if HFOM degrades but NACp holds?" The repair surfaces a
misconception that would have passed a multiple-choice item.

*Follow-up.* The apprentice closes the map and free-recalls five propositions; the tutor checks
and reveals the two missed. A second retrieval at +24 hours before they touch the IFR-6000 ramp
tester binds the map structure to the hardware workflow. The construction-then-retrieval sequence
recruits both the encoding gain (Schroeder et al., 2018) and the retention gain
(Karpicke & Blunt, 2011) that mapping alone forfeits.

**Manufacturing quality control — mapping a root-cause analysis for a quality engineer in training.**

*Setup.* A quality engineer in their first month on the line has been taught the 5-Whys, fishbone
(Ishikawa) categories, and basic statistical process control. A recent defect spike on a
CNC-machined part — diameter out of tolerance on 3% of units — was traced to tool wear on one
operation. The engineer can list the tools and categories but cannot connect "operator-reported
chatter at week 6" to "Cp drop at week 7" to "out-of-tolerance defects at week 8" as a causal
chain.

*Mapping move.* The tutor frames a focus question: "What chain of evidence connects the operator's
chatter report to the diameter-out-of-tolerance defects?" The engineer maps the six Ishikawa
categories and overlays the timeline events with directed labeled links: "tool wear *causes*
chatter"; "chatter *precedes* dimensional drift"; "dimensional drift *manifests as* Cp reduction";
"Cp below 1.33 *correlates with* defect-rate spike". The cross-link the engineer initially
misses — between "preventive maintenance interval" (Method) and "tool-wear progression"
(Machine) — is exactly the systemic finding the corrective action will address; surfacing it
turns a single-cause investigation into a process-control insight.

*Follow-up.* The engineer revises the map after walking the line and interviewing the operator,
adding a cross-link from "shift-change handoff" to "early-symptom reporting" that the original
analysis missed. They then close the map and write five sentences explaining the chain; the tutor
compares the sentences against the propositions and flags two relationships the prose omitted.
At the next investigation, the engineer starts with a focus question and partial map rather than
a fishbone in isolation — the mapping habit, not the specific diagram, is what transferred
(Mintzes et al., 1997).

## Quality signal

The AI tutor knows concept mapping is producing learning when (a) the learner-constructed map contains at least one propositionally valid cross-link between branches, (b) the learner can free-recall ≥70% of the asserted propositions after closing it, and (c) post-mapping performance on transfer items requiring integration across branches exceeds a no-map control by Hedges' g ≈ 0.4 — within the range Schroeder et al. (2018) report for construction-based use. A faster proxy: if the learner repairs at least one wrong link during the session, the diagnostic value of the map has been realized regardless of final score.

## Cross-references

- See [dual-coding](../01-learning-science/dual-coding.md) for the mechanism by which a coordinated visual representation strengthens encoding alongside the verbal channel.
- See [schema-theory-knowledge-components](../01-learning-science/schema-theory-knowledge-components.md) for the cognitive architecture that concept maps externalize and that the focus question disciplines.
- See [testing-effect](../01-learning-science/testing-effect.md) for the retrieval phase that must follow construction to convert encoding into long-delay retention.
- See [self-explanation-prompts](../04-delivery-patterns/self-explanation-prompts.md) for the elaborative prompts that pair naturally with map-construction and surface the reasoning behind each link.
- See [predict-before-reveal](../04-delivery-patterns/predict-before-reveal.md) for the move that asks learners to draft a map before exposure to the canonical structure.
- See [expertise-reversal](../01-learning-science/expertise-reversal.md) for the boundary at which the mapping scaffold begins to harm rather than help.
- See [transfer-of-learning](../01-learning-science/transfer-of-learning.md) for the cross-link work that mapping makes visible and that bears on far transfer.
- See [cognitive-load-theory](../01-learning-science/cognitive-load-theory.md) for the working-memory framework that explains why expert-skeleton scaffolds outperform free-form mapping for novices.
