---
id: worked-example-effect
title: Worked Example Effect
category: 01-learning-science
aliases: [worked-examples, example-based-learning]
evidence_strength: strong
effect_size: "Hedges' g ≈ 0.48 across mathematics K-postsecondary (Barbieri et al. 2023 meta-analysis, 55 studies, 181 effect sizes); Cohen's d ≈ 0.5–1.0 in original cognitive-load experiments (Sweller & Cooper 1985; Paas & van Merriënboer 1994)"
key_sources:
  - "Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. Cognition and Instruction, 2(1), 59-89. doi:10.1207/s1532690xci0201_3"
  - "Renkl, A. (2014). Toward an instructionally oriented theory of example-based learning. Cognitive Science, 38(1), 1-37. doi:10.1111/cogs.12086"
  - "Atkinson, R. K., Derry, S. J., Renkl, A., & Wortham, D. (2000). Learning from examples: Instructional principles from the worked examples research. Review of Educational Research, 70(2), 181-214. doi:10.3102/00346543070002181"
  - "Barbieri, C. A., Miller-Cotto, D., Clerjuste, S. N., & Chawla, K. (2023). A meta-analysis of the worked examples effect on mathematics performance. Educational Psychology Review, 35(1), 11. doi:10.1007/s10648-023-09745-1"
  - "Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. Educational Psychologist, 38(1), 23-31. doi:10.1207/S15326985EP3801_4"
  - "Renkl, A., & Atkinson, R. K. (2003). Structuring the transition from example study to problem solving in cognitive skill acquisition: A cognitive load perspective. Educational Psychologist, 38(1), 15-22. doi:10.1207/S15326985EP3801_3"
  - "Chi, M. T. H., Bassok, M., Lewis, M. W., Reimann, P., & Glaser, R. (1989). Self-explanations: How students study and use examples in learning to solve problems. Cognitive Science, 13(2), 145-182. doi:10.1207/s15516709cog1302_1"
last_reviewed: 2026-04-29
applies_to: [acquisition, transfer]
contraindicated_when:
  - learner_state.high_prior_knowledge
  - material.low_element_interactivity
  - task_type.motor_acquisition
  - learner_state.post_acquisition_practice
runtime_triggers:
  - new_problem_type_introduced
  - learner_first_exposure
  - high_element_interactivity_segment
  - problem_solving_failure_observed
related: [expertise-reversal, cognitive-load-theory, faded-worked-examples, self-explanation-elaborative-interrogation, self-explanation-prompts, schema-theory-knowledge-components, productive-failure]
---

# Worked Example Effect

## One-line claim

For novices acquiring a new problem-solving schema, studying a fully worked solution produces faster, more transferable learning than attempting the problem unaided — and the advantage is largest precisely when the material has many interacting elements that would otherwise overwhelm working memory.

## Evidence base

The worked example effect is the finding that, for learners without an existing schema for a problem type, replacing some or all of their problem-solving practice with the study of fully worked solutions produces equal or better post-test performance in less time and with less cognitive effort. Sweller and Cooper (1985) demonstrated the effect across five algebra-substitution experiments in *Cognition and Instruction*: students who alternated worked examples with practice problems took roughly half as long to solve isomorphic post-test problems and made approximately one-fifth as many errors as students who practiced unaided. The mechanism Sweller and Cooper proposed — that conventional means-ends problem solving consumes working-memory resources on the search itself rather than on schema construction — became the founding empirical anchor for cognitive load theory (Sweller, Van Merriënboer & Paas, 1998).

Modern meta-analytic evidence places the effect on solid ground. Barbieri, Miller-Cotto, Clerjuste, and Chawla (2023), aggregating 55 studies and 181 effect sizes across elementary through postsecondary mathematics, reported a robust-variance-estimation Hedges' g of 0.48 favoring worked-example study over conventional problem-solving practice — roughly an 18-percentile-point advantage on average. Earlier work generalized the effect beyond mathematics: Paas and van Merriënboer (1994) replicated the pattern in geometrical computer-numerically-controlled programming, and Atkinson, Derry, Renkl, and Wortham's (2000) review in the *Review of Educational Research* synthesized findings across statistics, programming, and physics, deriving instructional principles (integrated presentation, multiple examples per problem type, surface-feature variation to signal deep structure) that hold across domains. Renkl's (2014) integrative theory in *Cognitive Science* unified the prescriptive and descriptive evidence, identifying self-explanation activity during example study as the principal mediator of learning gains — a finding originally established by Chi, Bassok, Lewis, Reimann, and Glaser (1989), who showed in physics-mechanics protocols that "good" learners self-explain example steps to principles while "poor" learners re-read examples surface-to-surface.

The principal boundary condition is the **expertise reversal effect** (Kalyuga, Ayres, Chandler & Sweller, 2003): once a learner has constructed a usable schema for the problem type, continued worked-example study becomes redundant or actively harmful, and the advantage swings to active problem-solving practice. The transition is gradual, not binary; Renkl and Atkinson (2003) operationalize it as a *fading* procedure in which solution steps are progressively withdrawn (see [faded-worked-examples](../04-delivery-patterns/faded-worked-examples.md)). The practical implication: worked examples are a novice intervention. Apply them at first encounter with a problem type and during initial schema construction; withdraw them as mastery emerges and reverse to problem-solving practice once the learner is reliably correct unaided.

## When to apply

- **New problem type just introduced** — Before assigning the learner the first practice
  problem of a novel category, present at least one fully worked example with every solution
  step visible. The first example should land before any unaided attempt, not after the learner
  has already failed once.
- **Learner first exposure to high-element-interactivity content** — When the to-be-learned
  procedure involves multiple interacting subparts that must be coordinated (e.g., multi-step
  algebra, troubleshooting flows, clinical decision rules), worked examples free working
  memory for schema construction (Sweller, Van Merriënboer & Paas, 1998).
- **Problem-solving failure observed** — If a learner has just attempted a problem unaided and
  produced an incorrect or incomplete solution, follow with a worked example of the same or an
  isomorphic problem before re-attempting. Do not iterate failed unaided attempts; the search
  itself is consuming the load.
- **Multi-step procedure with no built-in error feedback** — When a wrong intermediate step does
  not surface a visible error until the end (e.g., misset-up integral, wrong impedance value),
  a worked example exposes the entire chain, including the steps the learner cannot
  self-diagnose.
- **Time-constrained acquisition with transfer required** — When the goal is durable,
  transferable schema and total instructional time is bounded, worked examples beat
  conventional problem-solving on both speed-to-criterion and transfer (Sweller & Cooper, 1985;
  Barbieri et al., 2023).
- **Pair with self-explanation prompts** — A worked example studied passively underperforms one
  studied with explicit prompts to explain *why* each step is taken (Chi et al., 1989; Renkl,
  2014). The combination is the operative move; neither in isolation is the full effect.

## When NOT to apply

- **Learner has already constructed a working schema for this problem type** — Continued
  worked-example study after a learner reliably solves problems unaided produces the expertise
  reversal: redundant guidance creates extraneous load and degrades performance
  (Kalyuga et al., 2003). Switch to problem-solving practice and reserve worked examples for
  novel sub-types.
- **Material has low element interactivity** — For simple, single-step procedures (recall a
  fact, apply a memorized formula to a clean input), worked examples add overhead without
  benefit. The cognitive-load advantage requires elements that *would* overwhelm working memory
  absent the worked solution.
- **Pure motor skill acquisition phase** — Studying a written or verbal account of a hand-eye
  procedure (soldering technique, surgical knot-tying, a free-throw motion) does not substitute
  for the physical practice and corrective kinesthetic feedback that motor learning requires.
  The principle applies to declarative and conceptual content, not motor execution.
- **Post-acquisition practice and retention phase** — Once acquisition is complete, retention
  depends on retrieval (see [testing-effect](../01-learning-science/testing-effect.md)) and
  spaced unaided practice, not on re-studying worked examples. Re-presenting a fully worked
  solution at this stage is restudy, which is dominated by retrieval practice for retention
  outcomes.
- **Productive-failure design is being used deliberately** — Some instructional designs
  withhold worked examples on purpose so the learner generates partial, often incorrect
  representations that are then reconciled with the canonical solution (see
  [productive-failure](../01-learning-science/productive-failure.md)). If that is the design,
  do not pre-empt it with an upfront worked example.

## How to apply

- **Show the full solution before the first unaided attempt** — For genuinely novel problem
  types, the first encounter is example study, not problem solving. Walk the learner through
  every step including the ones an expert would skip silently. Sweller and Cooper (1985)
  interleaved example-then-problem pairs; that pattern is the workhorse.
- **Embed self-explanation prompts at each step** — At each non-obvious step, prompt the
  learner to articulate why the step is taken before revealing the next step. "What rule
  justifies moving the constant out here?" or "Why this substitution and not the other one?"
  Chi et al. (1989) showed self-explanation depth is what discriminates good learners from
  surface-readers; Renkl (2014) made it the principal mediator in his theory.
- **Use multiple examples per problem type with surface variation** — A single worked example
  anchors learning to its surface features. Two or three examples that vary the cover story
  but preserve the deep solution structure force schema abstraction (Atkinson et al., 2000;
  Paas & van Merriënboer, 1994). Do not show three identical examples; vary numbers, contexts,
  or framing.
- **Fade the worked steps as mastery emerges** — Transition from full worked example to
  backward-faded example (last step blanked, then last two, then last three) to fully unaided
  problem solving (see [faded-worked-examples](../04-delivery-patterns/faded-worked-examples.md)).
  Renkl and Atkinson (2003) operationalize this as a progressive transfer of solution
  responsibility from example to learner.
- **Integrate diagrams and text spatially** — When the example pairs a diagram with text,
  place the labels and explanations adjacent to the relevant diagram parts rather than in a
  separate caption block. The split-attention effect (Sweller, Van Merriënboer & Paas, 1998)
  eats much of the worked-example benefit when learners must mentally integrate spatially
  separated sources.
- **Watch for the reversal trigger** — When the learner solves two consecutive problems of the
  type unaided and correctly, stop showing fully worked examples for that type and switch to
  problem-solving practice or interleaved problems of related types. Continued example-feeding
  past this point produces expertise reversal.

## Common misapplications

- **Treating "watch me solve it" as a worked example** — A live demonstration where the expert
  narrates while solving is example *modeling*, not a worked example, and it suffers from the
  speed and reversibility problems of any live demo. A worked example is a static,
  learner-paced artifact the learner can re-study, segment, and self-explain to.
- **Skipping self-explanation prompts** — A worked example studied silently is a fraction of a
  worked example studied with structured self-explanation (Chi et al., 1989). The principal
  mediator of the effect is the learner's elaborative activity, not the artifact itself.
- **Continuing worked examples past the reversal point** — The single most common operational
  error. The same intervention that accelerates novice learning slows or reverses advanced
  learning. If the learner is succeeding unaided, the principle is no longer the worked
  example effect; it is now [expertise-reversal](../01-learning-science/expertise-reversal.md).
- **Showing one example and treating it as sufficient** — A single worked example anchors
  learning to its specific surface features and produces poor transfer (Atkinson et al., 2000).
  Two or three with deep-structural overlap and surface variation is the operative dose.
- **Splitting attention across diagram and text** — When the worked example is a diagram on
  one page and the explanation on the facing page, learners burn working memory integrating
  the two sources, undoing the cognitive-load advantage the principle was supposed to provide.

## Examples across domains

**Avionics — installing a Garmin GTX 345 Mode S transponder per the installation manual.**

*Setup.* A first-year apprentice has just been assigned to wire a GTX 345 transponder install on a Cessna 172, including the ARINC 429 GPS-position interface and the strap-pin programming for ICAO address and ADS-B Out emitter category. They have read the wiring chapter once. The conventional next move would be to hand them the connector kit and the harness drawing; instead the tutor presents a worked example.

*Worked example.* The tutor opens an annotated install package from a previous identical airframe — the completed connector pinout, the ICAO-address strap-pin pattern decoded against the aircraft's hex code, the ARINC 429 wire labels, and a side-by-side of the wiring drawing and the installed harness photo. At each non-obvious step, the tutor prompts a self-explanation: "Why is the GPS position connected to ARINC 429 input port 1 rather than port 2 here?" "Why is the squat-switch ground left open on this airframe?" The apprentice reads, articulates the reason, and only then sees the next step. A second worked example covers a different airframe (Piper PA-28) with the same transponder, surfacing which decisions are airframe-specific and which are GTX-345-specific.

*Fading.* On the third install of the same equipment, the tutor blanks the strap-pin pattern and asks the apprentice to derive it from the ICAO address; on the fourth, the connector pinout is also blanked. By the fifth, the apprentice is producing the install package unaided, which is the reversal trigger to stop showing worked examples for this equipment and shift to problem-solving practice on the next transponder model. Barbieri et al. (2023) report g ≈ 0.48 in mathematics; the boundary-crossing replication into structured technical procedure (Paas & van Merriënboer, 1994) suggests a similar magnitude here.

**Emergency medicine — third-year resident learning the workup for undifferentiated chest pain.**

*Setup.* A third-year resident is rotating through the ED for the first time and has read the ACS / PE / aortic-dissection / pneumothorax differential framework once in a textbook. They have not yet worked up an actual undifferentiated chest-pain patient under attending supervision. The conventional next move would be to assign them a real patient and watch what happens; instead the attending starts with a worked example.

*Worked example.* The attending walks through a fully documented prior case — vitals, history, ECG, troponin, D-dimer, CXR, the actual decision tree the senior resident applied, the disposition, and the post-disposition outcome. At each branch point the attending prompts: "Why did we order a D-dimer here even though the Wells score was low?" "What feature of the ECG drove the cath-lab activation?" The resident articulates the reasoning before seeing the next branch. A second worked example covers a case that initially looked similar but turned out to be an aortic dissection, surfacing which surface features were misleading and which deep features distinguished the two.

*Fading.* On the resident's first live patient, the attending hands off everything except the final disposition decision. On the second, the attending also hands off the imaging-vs-no-imaging call. By the fourth or fifth case, the resident is running the workup unaided and the attending is supervising rather than scaffolding — the reversal trigger to stop providing worked cases and switch to live problem solving with retrospective debriefing. The Renkl (2014) integrative theory and Chi et al. (1989) self-explanation findings predict the gain over the "throw them in the pool" alternative is largest precisely on the high-element-interactivity decision branches, which is where novice ED residents most often anchor on the wrong feature.

## Quality signal

The AI tutor knows worked examples are producing learning when (a) time-to-correct-unaided-solution on isomorphic post-examples is at least 30% faster than the no-example control, consistent with Sweller and Cooper's (1985) original ~50% reduction, and (b) self-explanation depth — operationalized as the proportion of solution steps the learner can justify with a domain principle when prompted — exceeds 60%. If self-explanation depth stalls below that, the learner is reading the example surface-only, and the intervention is being undermined by the missing mediator.

## Cross-references

- See [expertise-reversal](../01-learning-science/expertise-reversal.md) for the boundary
  condition: the same intervention that accelerates novice learning slows or reverses advanced
  learning, with the operative trigger being the learner's emerging schema.
- See [cognitive-load-theory](../01-learning-science/cognitive-load-theory.md) for the
  foundational mechanism: worked examples reduce extraneous load from means-ends search,
  freeing working memory for schema construction.
- See [faded-worked-examples](../04-delivery-patterns/faded-worked-examples.md) for the
  operationalized transition from full worked example to unaided problem solving.
- See [self-explanation-prompts](../04-delivery-patterns/self-explanation-prompts.md) for the
  prompt patterns that activate the principal mediator of worked-example learning gains.
- See [self-explanation-elaborative-interrogation](../01-learning-science/self-explanation-elaborative-interrogation.md) for the broader literature on why-questions during study.
- See [schema-theory-knowledge-components](../01-learning-science/schema-theory-knowledge-components.md) for the construct that worked examples are designed to build.
- See [productive-failure](../01-learning-science/productive-failure.md) for the contrasting
  design philosophy that deliberately withholds worked examples to provoke generative
  engagement.
