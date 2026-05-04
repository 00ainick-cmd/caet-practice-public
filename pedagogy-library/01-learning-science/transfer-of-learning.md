---
id: transfer-of-learning
title: Transfer of Learning
category: 01-learning-science
aliases: [transfer, near-far-transfer]
evidence_strength: strong
# effect_size is null because transfer is a foundational construct, not a single
# intervention; it is the *outcome* against which most other principles in this
# library are evaluated. Magnitudes vary by transfer distance (near vs. far on
# the Barnett & Ceci 2002 nine-dimension taxonomy) and by intervention. Effect
# sizes for transfer-promoting moves (analogical encoding, varied practice,
# preparation-for-future-learning assessment) live in their own chapters or in
# this chapter's evidence base where they bear directly on operational choices.
effect_size: null
key_sources:
  - "Barnett, S. M., & Ceci, S. J. (2002). When and where do we apply what we learn? A taxonomy for far transfer. Psychological Bulletin, 128(4), 612-637. doi:10.1037/0033-2909.128.4.612"
  - "Perkins, D. N., & Salomon, G. (1992). Transfer of learning. In T. Husén & T. N. Postlethwaite (Eds.), International encyclopedia of education (2nd ed., pp. 6452-6457). Oxford: Pergamon Press."
  - "Detterman, D. K. (1993). The case for the prosecution: Transfer as an epiphenomenon. In D. K. Detterman & R. J. Sternberg (Eds.), Transfer on trial: Intelligence, cognition, and instruction (pp. 1-24). Norwood, NJ: Ablex."
  - "Gick, M. L., & Holyoak, K. J. (1983). Schema induction and analogical transfer. Cognitive Psychology, 15(1), 1-38. doi:10.1016/0010-0285(83)90002-6"
  - "Bransford, J. D., & Schwartz, D. L. (1999). Rethinking transfer: A simple proposal with multiple implications. Review of Research in Education, 24(1), 61-100. doi:10.3102/0091732X024001061"
  - "Gentner, D., Loewenstein, J., & Thompson, L. (2003). Learning and transfer: A general role for analogical encoding. Journal of Educational Psychology, 95(2), 393-408. doi:10.1037/0022-0663.95.2.393"
  - "Sala, G., Aksayli, N. D., Tatlidil, K. S., Tatsumi, T., Gondo, Y., & Gobet, F. (2019). Near and far transfer in cognitive training: A second-order meta-analysis. Collabra: Psychology, 5(1), 18. doi:10.1525/collabra.203"
last_reviewed: 2026-04-29
applies_to: [acquisition, transfer]
contraindicated_when:
  - learner_state.first_exposure
  - learner_state.overwhelmed
  - material.high_element_interactivity_no_scaffolding
  - task_type.motor_acquisition
runtime_triggers:
  - mastery_threshold_reached
  - new_context_about_to_be_introduced
  - second_worked_example_available
  - far_transfer_assessment_due
  - certification_or_field_application_imminent
related: [analogical-bridging, worked-example-effect, faded-worked-examples, schema-theory-knowledge-components, mastery-threshold-transfer-test-design, productive-failure, interleaving, predict-before-reveal]
---

# Transfer of Learning

## One-line claim

Knowledge or skill acquired in one context applies to another only when the new context is recognized as similar on dimensions the learner has actually encoded; transfer is the *outcome* of instruction designed to surface and abstract those dimensions, not a property that emerges automatically from successful initial learning.

## Evidence base

Transfer is the central problem the rest of this library exists to solve: an instructional move that produces fluent performance on the items practiced but no improvement on novel items has produced fluency, not learning. Barnett and Ceci's (2002) review in *Psychological Bulletin* gave the field its operational vocabulary — a nine-dimension taxonomy distinguishing transfer along six *context* dimensions (knowledge domain, physical context, temporal context, functional context, social context, modality) and three dimensions of *content* (skill type, performance change measured, memory demands). Transfer is "near" when the application context matches the training context on most dimensions and "far" when it differs on many; the taxonomy is a reminder that "transfer" without a specified distance is a question without an answer (Barnett & Ceci, 2002, pp. 621-625, on the dimensional grid). Perkins and Salomon (1992) supplied the complementary mechanism distinction: *low-road* transfer is the reflexive triggering of well-practiced routines by stimuli closely resembling the training stimuli, while *high-road* transfer is the deliberate, effortful abstraction of a principle and its mindful application to a non-obviously similar situation. Low-road transfer is built by extensive varied practice on a recurring pattern; high-road transfer is built by explicit abstraction and intentional bridging.

The empirical baseline is sobering. Detterman's (1993) review in *Transfer on Trial* documented that across decades of laboratory studies, far transfer is rare under default conditions: learners who solve a target problem after studying a structurally analogous source problem typically fail to retrieve the source unless the surface features overlap — the well-known "inert knowledge" failure first demonstrated systematically by Gick and Holyoak (1983) in *Cognitive Psychology*, where only ~30% of college students spontaneously applied a story analog to Duncker's radiation problem absent an explicit hint. Two interventions reliably move the needle. Gick and Holyoak (1983, Experiment 4) showed that comparing *two* analogs and inducing a shared schema raised spontaneous transfer to roughly 75%. Gentner, Loewenstein, and Thompson (2003) generalized this in the *Journal of Educational Psychology*: across three studies on negotiation training, learners who compared two cases side-by-side transferred a learned strategy to a face-to-face exercise at roughly twice the rate of learners who studied the same two cases sequentially. The mechanism is structural alignment — comparison forces the learner to encode what the cases share *abstractly*, which is the representation that subsequently matches a novel surface.

Sala, Aksayli, Tatlidil, Tatsumi, Gondo, and Gobet's (2019) second-order meta-analysis in *Collabra: Psychology* sets the upper bound on what training-program-style interventions deliver: across working-memory training, video-game training, music training, and chess training, *near-transfer* effects are real but modest (Hedges' g ≈ 0.2-0.4), and *far-transfer* effects to general cognitive abilities collapse to near zero once active control groups are used (g ≈ 0.0-0.1). Bransford and Schwartz (1999) reframed the assessment problem in *Review of Research in Education*: traditional sequestered-problem-solving tests — "can the learner produce the target output cold?" — systematically underestimate what learning has prepared a learner to do. Their alternative, *preparation for future learning* (PFL), measures whether prior learning helps the learner *learn* something new from resources provided during the assessment, and produces transfer signals where direct-application tests show none. The operational synthesis: design for high-road transfer through explicit comparison and abstraction; assess transfer through both direct application and PFL; expect near transfer to follow from varied practice and far transfer to require deliberate instructional moves.

## When to apply

- **Mastery threshold reached on the trained context** — Once the learner reliably solves problems within the training distribution, the marginal value of more in-distribution practice falls; this is the moment to introduce a structurally similar problem in a different surface (different aircraft model, different word problem, different patient presentation) and explicitly bridge.
- **A second worked example with the same structure becomes available** — Gentner et al. (2003) showed comparison across two cases roughly doubles spontaneous transfer; whenever a second instance of the same principle is at hand, present them together and prompt structural comparison rather than studying them sequentially.
- **A new context is about to be introduced where the principle should generalize** — Before the learner first encounters the new context cold, prompt them to predict how the trained principle will or will not apply; this is the operational use of [predict-before-reveal](../04-delivery-patterns/predict-before-reveal.md) for transfer rather than retention.
- **Far-transfer assessment is due** — When the curriculum or certification calls for a transfer test, design it explicitly along Barnett & Ceci's nine dimensions: name which dimensions the test holds constant (modality, social context) and which it varies (physical context, knowledge domain). An undefined "transfer test" is rarely a transfer test.
- **Certification or field application is imminent** — When the learner will shortly use the skill outside training (ramp test, board exam, classroom teaching), the transfer-distance gap between training and field is the failure mode to attack now; rehearse moves that close the gap (varied surface features, embedded distractors, novel equipment configurations).
- **Two prior topics share an underlying structure** — Whenever the curriculum sequences two topics that are formally analogous (Ohm's law and fluid flow; addition and union of sets), explicit cross-topic bridging is a high-leverage moment that learners almost never do on their own (see [analogical-bridging](../04-delivery-patterns/analogical-bridging.md)).

## When NOT to apply

- **Learner has not yet achieved stable performance in the trained context** — Pushing for transfer before the within-context schema is built produces noise; the learner has nothing yet to transfer. The Gick & Holyoak (1983) result depended on first inducing a usable source schema; absent that, comparison degrades into confusion. Build mastery first (see [worked-example-effect](../01-learning-science/worked-example-effect.md)), then transfer.
- **Working memory is saturated** — Comparison-and-abstraction work is high in germane load. A learner already at effort 7+ on a 1-9 scale (see [cognitive-load-theory](../01-learning-science/cognitive-load-theory.md)) cannot do additional structural alignment; reduce extraneous load and consolidate the training-context schema before introducing transfer demands.
- **Material has high element interactivity and no scaffolding exists yet** — Cross-context comparison of complex multi-element systems (e.g., comparing two whole avionics architectures before sub-systems are understood) imposes load that swamps the comparison itself. Pre-train the components before bridging across systems.
- **Cognitive-training-style "general ability" claims** — The Sala et al. (2019) meta-analytic baseline says far transfer to general abilities (working memory, reasoning) from training programs is essentially zero. Do not promise transfer from brain-training-style interventions; the principle does not back the claim.
- **Pure motor skill acquisition phase** — Transfer in motor learning has its own distinct mechanisms (specificity of practice, contextual interference) and the verbal-conceptual moves emphasized here have limited reach into motor schemas. See [interleaving](../01-learning-science/interleaving.md) for the mechanism that does carry into motor domains.
- **Transfer test would be unfair given current instruction** — If the instruction did not address the dimensions on which the test varies (e.g., training was all multiple-choice and the test is open-response), the failure is instructional alignment, not the learner's transfer ability.

## How to apply

- **Make the structural alignment explicit, not implicit** — Do not present analogous cases and hope the learner notices. Prompt the comparison directly: "What is the same about these two cases? What is different? What feature would you use to recognize a third case as belonging to this family?" This is the Gentner et al. (2003) move; the comparison itself is what builds the transferable schema.
- **Vary surface, hold structure constant** — Use multiple problems that share a common solution principle but differ in cover story, equipment, numbers, and modality. The variability is what defeats over-specific encoding (Barnett & Ceci, 2002, on context-dimension variation as the operational lever for promoting far transfer); two examples with identical surface features build no more transfer than one.
- **Name the principle abstractly** — After two or three concrete instances, prompt or supply the abstract statement of the principle ("verify the signal at every transition where a fault could occur," "common denominator before adding"). Naming is the act that converts a pattern noticed across instances into a schema retrievable in a future surface (see [schema-theory-knowledge-components](../01-learning-science/schema-theory-knowledge-components.md)).
- **Use predict-before-reveal at the boundary of a new context** — Before the learner attempts a transfer problem, ask them to predict how (or whether) the trained principle applies; then have them attempt the problem; then reveal and discuss. The prediction makes the structural mapping observable and correctable rather than buried in silent attempt.
- **Assess transfer along named dimensions** — When designing a transfer test, write down which Barnett & Ceci dimensions the items vary on (e.g., this item changes physical context and modality; this one changes functional context and knowledge domain) and report transfer per-dimension. "The learner passed transfer" with no distance specification is uninformative.
- **Add a preparation-for-future-learning probe** — Alongside any direct-application transfer item, include a PFL item: present a brief new resource (a worked example, a manual excerpt) and ask the learner to solve a problem using it. Bransford and Schwartz (1999) showed this format detects transferable competence that sequestered tests miss; for tutors it also surfaces gaps in *learning-to-learn* skill, which is itself a transfer target.
- **Sequence varied practice with a contrast partner** — Pair each new problem type with a structurally similar but superficially different partner ([interleaving](../01-learning-science/interleaving.md)); the contrast forces structural encoding rather than surface pattern-match.

## Common misapplications

- **Treating fluent in-context performance as evidence of transfer** — A learner who solves every variant of the trained problem perfectly may still fail the same problem in a new surface. In-context mastery is a precondition for transfer, not a substitute for measuring it.
- **Surface variation without structural identity** — Changing names and numbers while keeping the surface schema intact produces near-transfer at best and often nothing; the variation must reach the dimensions on which transfer is wanted (Barnett & Ceci, 2002).
- **Single-example "transfer" instruction** — Showing one worked example and expecting transfer to a different surface is the classical Gick & Holyoak (1983) failure case (~30% spontaneous transfer). Two cases with explicit comparison is the floor, not a luxury.
- **Hint-then-claim-transfer** — If the test prompt itself names the analogy ("remember the radiation problem"), the result measures recall and mapping under instruction, not transfer. Transfer measurements should not include the bridging hint as part of the prompt.
- **Promising far transfer from cognitive-training-style products** — Working memory training, brain games, chess, and music instruction do not produce far transfer to general cognitive ability at meaningful effect sizes (Sala et al., 2019). Conflating the in-program improvement with transferable benefit is the most common public misapplication of the construct.
- **Designing transfer tests that test recognition not application** — Multiple-choice items asking the learner to recognize the principle's name in a list are not transfer tests; transfer requires producing the principle's behavior in a context where the principle is not named.

## Examples across domains

**Avionics — generalizing a transponder ramp-test diagnostic from a Mode S unit to a UAT-equipped install.**

*Setup.* A technician has reached stable performance running the IFR-6000-style ramp test on Mode S transponders for ADS-B Out compliance: they reliably interpret the trace, find the failure mode, and clear the squawk. Today the next aircraft in the shop is equipped with a UAT (978 MHz) ADS-B Out solution rather than 1090ES, and the test set, antenna position, and the message format on the trace differ. A naive expectation is that the technician will "just apply" the diagnostic; the Gick & Holyoak (1983) baseline suggests they will not, because the surface features (frequency, message structure, equipment) are what they actually encoded.

*Transfer move.* The tutor presents the Mode S procedure and the UAT procedure side-by-side as two cases, not sequentially. The structural comparison is prompted explicitly: "What is the diagnostic principle that is the same in both? What about the trace, the test set, the antenna placement is different, and which of those differences matter for the diagnosis?" The technician identifies the shared abstraction — verify the broadcast at every transition (encoder, transponder, antenna, ramp-set decode) and isolate the failing transition — and names two surface differences (frequency band, message-format-specific failure indicators) that change *how* but not *whether* each transition is verified. The tutor then has the technician predict what failure on the UAT trace would correspond to a Mode S "no Squitter at antenna" failure; only after the prediction does the actual UAT test run.

*Assessment.* The transfer test is designed along Barnett & Ceci dimensions: it changes physical context (different bench, different aircraft) and knowledge sub-domain (UAT not Mode S) but holds modality and functional context constant. A PFL probe accompanies the direct test — a one-page excerpt of an unfamiliar diversity-antenna ADS-B installation manual is provided, and the technician is asked to identify which transitions in *that* architecture would be the diagnostic check points. Performance on the PFL probe is what predicts whether the technician will adapt next month to a third architecture rather than needing the procedure re-taught from scratch.

**K-12 math — transferring fraction-addition reasoning to fraction subtraction and to the addition of algebraic fractions.**

*Setup.* A fifth-grade student has reached stable performance adding fractions with unlike denominators, having worked the canonical procedure ("find a common denominator, convert, add") through enough varied problems to be reliable. The curriculum's next stop is fraction subtraction; later in the year, algebraic fractions with literal denominators (1/x + 1/y) appear. The default move — re-teach the subtraction procedure as if it were unrelated, then do the same again for algebra — wastes the schema the student has already built and produces three procedures stored as three independent routines.

*Transfer move.* The tutor sets up the comparison directly. Two worked examples are placed side-by-side: 1/3 + 1/4 and 1/3 − 1/4. The student is prompted, "What is the same about how you set these up? Where do they diverge?" The student identifies that the common-denominator step is identical and only the final arithmetic differs. The tutor then names the abstract principle: "you can only combine parts of the same size — the rule is the same whether you are adding or subtracting." A week later, when 1/x + 1/y appears, the tutor again places it next to 1/3 + 1/4 and prompts the comparison; the student transfers the principle ("multiply the denominators to get a common one") with a single bridging move rather than treating algebraic fractions as a new topic. Predict-before-reveal is used at the algebraic boundary: "What do you think the common denominator will be when the bottoms are letters instead of numbers?"

*Assessment.* The transfer test is built per dimensions: items vary on knowledge domain (numeric vs. literal denominators) and surface (cover story, equipment) but hold modality (paper-and-pencil) constant. A PFL item presents a short worked example of *complex* fractions (a fraction with a fraction inside it) the student has never seen; the student is asked to use the example to solve a near-variant. Bransford and Schwartz's (1999) data predict that students who built the abstraction explicitly during fraction addition will use the example productively, while students who memorized the addition procedure will not — and the PFL item surfaces that difference before it shows up as collapse in the next unit.

## Quality signal

The AI tutor knows transfer instruction is producing learning when performance on items that vary the trained-context surface (Barnett & Ceci dimensions: physical context, modality, cover story) within the same structural family stays within ~10 percentage points of in-context performance, and when a PFL probe item shows the learner can use a brief new resource to solve a structurally adjacent novel problem. A weaker but faster signal is the structural-comparison response itself: when prompted to compare two analogs, the learner names a principle that abstracts both and predicts a third instance correctly more than 70% of the time. Drift below that mark indicates over-specific encoding — more varied practice with explicit comparison, not more repetition, is the next move.

## Cross-references

- See [analogical-bridging](../04-delivery-patterns/analogical-bridging.md) for the delivery pattern that operationalizes structural comparison across two cases at the moment a second analog becomes available.
- See [worked-example-effect](../01-learning-science/worked-example-effect.md) for the prerequisite — usable source schemas only form when initial encoding is supported, after which transfer becomes possible.
- See [faded-worked-examples](../04-delivery-patterns/faded-worked-examples.md) for the sequence that takes a learner from in-context fluency through varied practice toward independent transfer performance.
- See [schema-theory-knowledge-components](../01-learning-science/schema-theory-knowledge-components.md) for the long-term-memory representation transfer relies on and which abstraction-naming targets directly.
- See [mastery-threshold-transfer-test-design](../03-assessment-science/mastery-threshold-transfer-test-design.md) for how to design transfer assessments along the Barnett & Ceci dimensions and combine direct-application with PFL items.
- See [productive-failure](../04-delivery-patterns/productive-failure.md) for the related move of having learners attempt a transfer problem before instruction, which builds the discriminating features the principle's later abstraction will hang on.
- See [interleaving](../01-learning-science/interleaving.md) for the practice schedule that pairs structurally similar surface-different problems in mixed sequences to force structural encoding.
- See [predict-before-reveal](../04-delivery-patterns/predict-before-reveal.md) for the boundary move at the moment a learner first encounters a new context where the trained principle may apply.
