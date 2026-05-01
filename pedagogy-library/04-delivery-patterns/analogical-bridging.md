---
id: analogical-bridging
title: Analogical Bridging
category: 04-delivery-patterns
aliases: [analogical-encoding, analogical-comparison, analogy-instruction]
evidence_strength: strong
effect_size: "Spontaneous transfer rises from ~30% (one analog) to ~75% with two-analog comparison and shared-schema induction (Gick & Holyoak 1983, Exp. 4); analogical-encoding produced ~2x transfer rate vs. sequential study (Gentner, Loewenstein & Thompson 2003); case-comparison meta-analysis Hedges' g ≈ 0.50 on transfer outcomes (Alfieri, Nokes-Malach & Schunn 2013)"
key_sources:
  - "Gentner, D. (1983). Structure-mapping: A theoretical framework for analogy. Cognitive Science, 7(2), 155-170. doi:10.1207/s15516709cog0702_3"
  - "Gick, M. L., & Holyoak, K. J. (1983). Schema induction and analogical transfer. Cognitive Psychology, 15(1), 1-38. doi:10.1016/0010-0285(83)90002-6"
  - "Gentner, D., & Markman, A. B. (1997). Structure mapping in analogy and similarity. American Psychologist, 52(1), 45-56. doi:10.1037/0003-066X.52.1.45"
  - "Catrambone, R., & Holyoak, K. J. (1989). Overcoming contextual limitations on problem-solving transfer. Journal of Experimental Psychology: Learning, Memory, and Cognition, 15(6), 1147-1156. doi:10.1037/0278-7393.15.6.1147"
  - "Gentner, D., Loewenstein, J., & Thompson, L. (2003). Learning and transfer: A general role for analogical encoding. Journal of Educational Psychology, 95(2), 393-408. doi:10.1037/0022-0663.95.2.393"
  - "Alfieri, L., Nokes-Malach, T. J., & Schunn, C. D. (2013). Learning through case comparisons: A meta-analytic review. Educational Psychologist, 48(2), 87-113. doi:10.1080/00461520.2013.775712"
  - "Holyoak, K. J. (2012). Analogy and relational reasoning. In K. J. Holyoak & R. G. Morrison (Eds.), The Oxford handbook of thinking and reasoning (pp. 234-259). New York: Oxford University Press."
last_reviewed: 2026-04-30
applies_to: [acquisition, transfer]
contraindicated_when:
  - learner_state.first_exposure
  - learner_state.overwhelmed
  - material.high_element_interactivity_no_scaffolding
  - task_type.motor_acquisition
runtime_triggers:
  - new_topic_structurally_isomorphic_to_prior
  - second_worked_example_available
  - far_transfer_target_imminent
  - misconception_traceable_to_unencoded_relation
  - abstract_principle_introduced_without_concrete_anchor
related: [transfer-of-learning, worked-example-effect, faded-worked-examples, schema-theory-knowledge-components, self-explanation-prompts, predict-before-reveal, interleaving, dual-coding]
---

# Analogical Bridging

## One-line claim

Surface a familiar source domain that shares the deep relational structure of the target concept, prompt the learner to map the corresponding parts, and use the comparison to abstract the shared schema — not to add a decorative metaphor, but to make the structural pattern that drives transfer encodable in the first place.

## Evidence base

Gentner's (1983) structure-mapping theory in *Cognitive Science* established the foundational claim that the cognitive content of an analogy is the alignment of *relations between objects* across a base and a target domain, not the alignment of object attributes. The systematicity principle predicts that learners preferentially map higher-order relations (causes, constraints, "if X then Y") rather than isolated features, and that an analogy delivers learning gains only to the extent it forces the learner to encode structure rather than surface (Gentner, 1983, pp. 162-165, on the systematicity principle). Gentner and Markman's (1997) *American Psychologist* synthesis extended this to similarity comparisons generally: aligning two examples that share underlying structure makes both their commonalities and their *alignable differences* psychologically salient, which is the mechanism by which side-by-side cases deliver more than the sum of the two cases studied alone.

The empirical anchor for instruction is Gick and Holyoak (1983) in *Cognitive Psychology*. College students who studied a single source story (a general's military strategy) and then attempted Duncker's radiation problem transferred the convergence solution at roughly 30% absent an explicit hint to use the source. Studying *two* source analogs and being prompted to compare them — extracting a schema for the convergence principle — raised spontaneous transfer to roughly 75% (Gick & Holyoak, 1983, Experiment 4). Catrambone and Holyoak (1989) replicated and extended the effect across a context shift and a one-week delay, showing that the gains survived realistic conditions when the comparison was supported by structure-oriented questions and three rather than two source analogs. Gentner, Loewenstein, and Thompson (2003) generalized the finding outside laboratory toy problems: across three studies on negotiation training in the *Journal of Educational Psychology*, MBA students who compared two cases side-by-side transferred a learned strategy to a face-to-face exercise at roughly twice the rate of students who studied the same two cases sequentially.

Alfieri, Nokes-Malach, and Schunn's (2013) meta-analysis in *Educational Psychologist* synthesized 57 case-comparison studies and reported a mean Hedges' g of 0.50 favoring comparison conditions on transfer outcomes, with the effect robust across age groups and domains but moderated by instructional support: comparisons paired with explicit relational prompts ("what is the same about how these two work?") substantially outperformed unsupported comparisons. Holyoak (2012) compiled the boundary conditions in *The Oxford Handbook of Thinking and Reasoning*: analogical reasoning is heavily working-memory-bound, fails for novices who lack the schemas needed to recognize structural matches, and produces noise rather than learning when the source domain is itself only weakly understood. The operational synthesis: analogy is a transfer-and-abstraction tool, not an introduction tool — it works once the learner has a workable representation of *one* of the two domains.

## When to apply

- **A new topic is structurally isomorphic to a topic the learner already understands** — When
  the target principle (e.g., voltage divider, fraction equivalence, supply-and-demand
  equilibrium) shares a deep structure with a prior topic the learner has already mastered,
  surface the alignment explicitly and prompt the learner to map the corresponding parts. This
  is the signature trigger.
- **A second worked example with the same structure becomes available** — Per Gentner et al.
  (2003), comparison across two cases roughly doubles spontaneous transfer; whenever a second
  instance of the same principle is at hand, present the two side-by-side and prompt structural
  comparison rather than studying them sequentially.
- **A far-transfer target is imminent** — When the certification or field application requires
  applying the principle to a novel surface (different aircraft model, different word problem
  framing, different patient presentation), pre-rehearsing the structural mapping closes the
  surface-to-structure gap that otherwise breaks transfer.
- **A misconception traces to an unencoded relation** — When a learner consistently errs in a
  way that suggests they encoded surface features but missed the relational structure (e.g.,
  adding numerators *and* denominators because the surface "looks like" addition), an analogy
  that foregrounds the unencoded relation is higher-leverage than restating the rule.
- **An abstract principle is being introduced without a concrete anchor** — A formal definition
  delivered cold (Ohm's law as `V = IR`, conservation of momentum as a vector equation) is hard
  to encode without an interpretive frame. A familiar analog (water flow, a row of billiard
  balls) provides the encoding scaffold; the analog is then *retired* once the formal
  representation is fluent — see Section 5.

## When NOT to apply

- **Learner is in the initial encoding phase of either the source or the target** — Analogical
  mapping is itself a working-memory-heavy operation (Holyoak, 2012); adding it on top of
  unfinished encoding produces noise. Build a workable representation of the target with worked
  examples first, *then* bridge to make the structure transferable.
- **Cognitive load is already saturated** — If the learner is showing signs of overwhelm (slow
  responses, errors on basics, expressed frustration), introducing a second domain to map
  against the first compounds the load. Reduce extraneous load first; bridge once headroom
  returns.
- **The target task is high element-interactivity with no scaffolding** — Mapping across two
  complex systems simultaneously when neither has been chunked into manageable units invites
  surface-level mapping (object-to-object) instead of relational mapping, which is worse than no
  analogy at all (Gentner, 1983).
- **The skill being taught is primarily motor acquisition** — Analogical bridging operates on
  declarative and conceptual representations. The motor-execution component of a procedural task
  (soldering, instrument scan, free-throw form) is built by physical practice and corrective
  feedback; the analogy applies only to the embedded conceptual content ("why does this step
  come before that one?").
- **The source domain is itself only weakly understood by the learner** — A bad analogy is worse
  than no analogy. If the learner does not have a stable mental model of the base domain, the
  comparison cannot do its work; pick a different source or build the source first.

## How to apply

- **Lead with structural mapping prompts, not surface description** — Do not say "this is like
  X"; ask "what corresponds to X in this new system, and what plays the role of Y?" The
  retrieval of the mapping is where the schema gets built. The exemplar prompt format is from
  Catrambone & Holyoak (1989): structure-oriented questions outperformed surface-description
  questions even when both kept the learner attending to the source.
- **Use two analogs whenever possible, not one** — Gick and Holyoak (1983, Experiment 4) and
  Gentner et al. (2003) both showed the comparison-induction effect is roughly twice as large
  with two source instances as with one. If two analogs exist (two ramp tests, two fraction
  problems, two negotiation cases), present them together and prompt explicit comparison; see
  [worked-example-effect](../01-learning-science/worked-example-effect.md) for the underlying
  load-management rationale.
- **Make alignable differences explicit, not just commonalities** — Per Gentner & Markman
  (1997), structural alignment surfaces *both* what the two systems share and where they diverge
  in the same dimension. Naming the alignable differences ("voltage corresponds to pressure, but
  voltage can be negative — pressure cannot") is what protects against over-mapping.
- **Retire the analog once the formal representation is fluent** — Analogies are scaffolds.
  Persistent reliance on the source ("water flowing through a pipe") prevents the learner from
  operating in the target representation directly, and surface features of the source can become
  misconceptions in the target (e.g., believing electrons accumulate at a junction the way water
  does). Plan the analog's exit from the start.
- **Couple bridging with self-explanation** — A structural mapping prompt is half the move; the
  other half is having the learner articulate *why* the mapping holds. See
  [self-explanation-prompts](../04-delivery-patterns/self-explanation-prompts.md) for the prompt
  format that combines mapping with elaboration.
- **For far-transfer goals, bridge across surface variation deliberately** — Per Catrambone &
  Holyoak (1989), transfer survives a context shift only when the learner has been pushed to
  encode the structure abstractly. Vary the surface (different aircraft system, different
  problem cover story) while holding the structure constant; this is the operational meaning of
  [interleaving](../01-learning-science/interleaving.md) for transfer.

## Common misapplications

- **Decorative metaphors that the learner does not have to map** — "Memory is like a filing
  cabinet" delivered as a one-liner does no learning work; the learner has to *do* the mapping
  for the schema to form. If the prompt is "now tell me what corresponds to a folder in your
  memory," it is bridging; if it is just description, it is rhetoric.
- **Using a surface-similar source that shares features but not structure** — An analogy that
  resembles the target on surface features but not on the relational structure ("a heart is like
  a pump because they're both round") teaches a wrong abstraction. Pick the source for
  structural fidelity, not familiarity alone (Gentner, 1983; Gentner & Markman, 1997).
- **Letting the analog persist into the formal-representation phase** — When the learner can
  solve target problems fluently but still narrates "the water flowing through the wire," the
  source is now drag rather than scaffold and is likely to leak surface features into the target
  (the "electrons accumulate" misconception). Plan and execute the retirement.
- **Bridging at first exposure** — Pre-encoding analogies impose a mapping load before either
  representation is stable. The pretesting effect is a different mechanism (see
  [pretesting-effect](../01-learning-science/pretesting-effect.md)); analogical bridging is a
  transfer mechanism that operates on already-encoded material.
- **One-shot bridging without comparison** — A single analog with no second instance and no
  prompt for explicit alignment is the lowest-yield form of the technique (Gick & Holyoak,
  1983). If only one analog is available, at minimum prompt the learner to articulate the
  structural correspondence aloud rather than receiving it as a description.

## Examples across domains

**Avionics — bridging from RF transmission line theory to digital data bus topology during an installation walk-through.**

*Setup.* A technician has a stable mental model of RF transmission lines on a coaxial antenna feed (characteristic impedance, standing waves, the consequences of impedance mismatch at a connector). They are now learning ARINC 429 and ARINC 664 data bus installation rules and keep treating the bus as "just wires" — sloppy on stub length, indifferent to termination, surprised when a long unterminated stub causes intermittent bit errors at the receiver.

*Bridging move.* Instead of restating the installation rule, the tutor sets up two cases side-by-side: a coaxial feed with a known impedance mismatch at the antenna, and an ARINC 429 stub that exceeds the maximum allowed length without proper termination. The prompt is structural: "What corresponds to the antenna mismatch on the data bus side? What plays the role of the standing wave when bits get reflected off an unterminated stub?" The technician maps reflection coefficient onto bit-error mechanism, characteristic impedance onto bus impedance, and termination resistor onto the matched load they already know works on RF. The tutor calls out one alignable difference: "RF mismatch degrades a continuous signal; data bus mismatch corrupts discrete bits — same mechanism, different observable failure."

*Follow-up.* The analog is retired before the next install: on the second ARINC bus job, the tutor asks the technician to specify the termination value from the bus impedance directly, without invoking the RF source. The analogy did its work; persisting in it would now risk leaking RF habits (e.g., variable impedance on the trace) into a domain where they do not apply.

**K-12 math — bridging from whole-number division to fraction division in a fifth-grade tutoring session.**

*Setup.* A student is fluent on whole-number division (12 ÷ 3 = 4 because "how many 3s fit into 12") and on fraction multiplication (½ × ¼ = 1/8). They have just been shown that ½ ÷ ¼ = 2, and the procedural rule "invert and multiply." The student executes the procedure but cannot explain why dividing by a smaller fraction yields a *larger* answer — and tomorrow's quiz will include a word problem where the rule alone will not save them.

*Bridging move.* The tutor presents two cases together: "12 ÷ 3 = 4 — how many groups of 3 fit into 12?" and "½ ÷ ¼ = 2 — how many groups of ¼ fit into ½?" The prompt is structural: "What corresponds to 'groups of 3' in the second problem? What plays the role of the dividend?" The student maps the divisor onto "the size of one group" and the quotient onto "the count of groups." The tutor calls out the alignable difference: "When the group is smaller than the whole, the count goes up — that's why a smaller divisor gives a bigger answer." The student now has a relational structure ("count of group-sized pieces in the dividend") that the procedural rule slots into rather than replaces.

*Follow-up.* In the next session, the same prompt is reused on a word-problem variant ("how many ⅓-cup servings are in ¾ of a cup?"); the student abstracts the same structure across the new surface. Per Alfieri, Nokes-Malach, and Schunn (2013), case comparisons of this kind produce on average Hedges' g ≈ 0.5 on transfer measures — closely matching the gain the tutor is targeting on next week's word-problem section.

## Quality signal

The AI tutor knows analogical bridging is producing learning when, on a near-transfer item that varies the surface (different aircraft system, different word-problem cover story) but holds structure constant, the learner's accuracy is at least 15 percentage points higher than on a parallel surface-varying item where no bridging occurred. A faster in-session signal is whether the learner can correctly name the structural correspondences when prompted (`"what corresponds to X in this new problem?"`) — a learner who can articulate the mapping has built the schema; one who can only restate the surface description has not.

## Cross-references

- See [transfer-of-learning](../01-learning-science/transfer-of-learning.md) for the transfer-distance taxonomy and the high-road / low-road distinction that frames why bridging is the central transfer move.
- See [worked-example-effect](../01-learning-science/worked-example-effect.md) for the load-management rationale behind presenting two analogs side-by-side rather than one at a time.
- See [faded-worked-examples](../04-delivery-patterns/faded-worked-examples.md) for how to retire the analog as the learner gains fluency in the target representation.
- See [schema-theory-knowledge-components](../01-learning-science/schema-theory-knowledge-components.md) for the underlying account of the abstract structure that bridging is meant to induce.
- See [self-explanation-prompts](../04-delivery-patterns/self-explanation-prompts.md) for the prompt format that combines structural mapping with the elaboration that makes the mapping explicit.
- See [interleaving](../01-learning-science/interleaving.md) for varying surface features systematically once the structural schema is in place.
- See [predict-before-reveal](../04-delivery-patterns/predict-before-reveal.md) for the move that opens a bridging episode by surfacing what the learner expects the target to do.
