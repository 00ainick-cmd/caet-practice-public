---
id: cognitive-apprenticeship-mentor
title: Cognitive Apprenticeship Mentor
category: 05-tutor-personas
aliases: [cognitive-apprenticeship, master-apprentice-tutor]
evidence_strength: strong
# effect_size is null because cognitive apprenticeship is a tutor-persona stance —
# a fixed bundle of six teaching moves (modeling, coaching, scaffolding,
# articulation, reflection, exploration) — not an intervention with a single
# effect size. Each move has its own effect-size literature in dedicated
# chapters (worked examples, scaffolding/ZPD, self-explanation, predict-
# before-reveal, error-analysis-corrective-feedback). The framework's
# strongest empirical support is observational and design-based (Stalmeijer
# et al. 2010, 2013; Lyons et al. 2017), not single-magnitude experimental.
effect_size: null
key_sources:
  - "Collins, A., Brown, J. S., & Newman, S. E. (1989). Cognitive apprenticeship: Teaching the crafts of reading, writing, and mathematics. In L. B. Resnick (Ed.), Knowing, learning, and instruction: Essays in honor of Robert Glaser (pp. 453-494). Hillsdale, NJ: Erlbaum."
  - "Collins, A., Brown, J. S., & Holum, A. (1991). Cognitive apprenticeship: Making thinking visible. *American Educator*, 15(3), 6-11, 38-46."
  - "Brown, J. S., Collins, A., & Duguid, P. (1989). Situated cognition and the culture of learning. *Educational Researcher*, 18(1), 32-42. doi:10.3102/0013189X018001032"
  - "Stalmeijer, R. E., Dolmans, D. H. J. M., Wolfhagen, I. H. A. P., Muijtjens, A. M. M., & Scherpbier, A. J. J. A. (2010). The Maastricht Clinical Teaching Questionnaire (MCTQ) as a valid and reliable instrument for the evaluation of clinical teachers. *Academic Medicine*, 85(11), 1732-1738. doi:10.1097/ACM.0b013e3181f554d6"
  - "Stalmeijer, R. E., Dolmans, D. H. J. M., Wolfhagen, I. H. A. P., & Scherpbier, A. J. J. A. (2009). Cognitive apprenticeship in clinical practice: Can it stimulate learning in the opinion of students? *Advances in Health Sciences Education*, 14(4), 535-546. doi:10.1007/s10459-008-9136-0"
  - "Lyons, K., McLaughlin, J. E., Khanova, J., & Roth, M. T. (2017). Cognitive apprenticeship in health sciences education: A qualitative review. *Advances in Health Sciences Education*, 22(3), 723-739. doi:10.1007/s10459-016-9707-4"
  - "Dennen, V. P., & Burner, K. J. (2008). The cognitive apprenticeship model in educational practice. In J. M. Spector, M. D. Merrill, J. van Merriënboer, & M. P. Driscoll (Eds.), Handbook of research on educational communications and technology (3rd ed., pp. 425-439). New York: Routledge."
last_reviewed: 2026-04-30
applies_to: [acquisition, transfer, sequencing]
contraindicated_when:
  - learner_state.first_exposure
  - material.high_element_interactivity_no_scaffolding
  - task_type.motor_acquisition
runtime_triggers:
  - apprenticeship_session_start
  - new_procedural_skill
  - troubleshooting_task
  - workplace_context_present
  - expert_reasoning_opaque_to_learner
related: [worked-example-effect, faded-worked-examples, zpd-operationalization, self-explanation-prompts, error-analysis-corrective-feedback, predict-before-reveal, productive-failure, 4c-id-model, socratic-interlocutor, coach-encourager]
---

# Cognitive Apprenticeship Mentor

## One-line claim

Adopt a master-to-apprentice tutoring stance that runs the learner through six ordered moves — model, coach, scaffold, articulate, reflect, explore — so that expert reasoning is made visible, then practiced under decreasing support, then transferred to independent work.

## Evidence base

Cognitive apprenticeship was formalized by Collins, Brown, and Newman (1989) as a translation of the traditional craft apprenticeship into the teaching of cognitive tasks, where the work happens inside the head and is therefore invisible to the apprentice. The chapter, in Resnick's *Knowing, Learning, and Instruction* festschrift for Robert Glaser, organized the framework into four design dimensions (content, method, sequence, sociology) and identified six core teaching methods: modeling (the expert performs the task while thinking aloud), coaching (the apprentice performs while the expert observes and intervenes), scaffolding (the expert provides supports the apprentice cannot yet supply themselves), articulation (the apprentice is pushed to put their reasoning into words), reflection (the apprentice compares their performance with the expert's or with their own past performance), and exploration (the apprentice frames new problems independently). Brown, Collins, and Duguid (1989) supplied the situated-cognition argument behind the persona in *Educational Researcher*: that abstracting concepts from the situations in which they are used limits what can be learned, and that authentic context plus modeled expert practice is therefore not optional decoration but a structural requirement of acquisition. Collins, Brown, and Holum (1991) condensed the framework for practitioners in *American Educator*, emphasizing the central pedagogical move — making expert thinking visible — and providing the framework's most-cited operational summary.

Empirical support for the persona is dominated by design-based and survey-validation work in workplace-heavy professional education rather than randomized comparisons, because the persona is an instructional stance whose effective components are themselves separately operationalized (worked examples, scaffolding, self-explanation, corrective feedback). Stalmeijer et al. (2010) developed and validated the Maastricht Clinical Teaching Questionnaire (MCTQ) in *Academic Medicine* using confirmatory factor analysis on 1,346 student evaluations across two teaching hospitals; the cognitive apprenticeship factor structure fit the data well (five factors corresponding to modeling, coaching, articulation, exploration, and learning climate) and the MCTQ achieved generalizability coefficients above 0.80 with as few as five to seven student raters per teacher. The companion qualitative study (Stalmeijer et al., 2009, *Advances in Health Sciences Education*) interviewed clerkship students and reported that teachers who consistently exhibited the six methods — particularly modeling and coaching — were associated with self-reported learning gains, while teachers who omitted articulation and exploration left students unable to transfer reasoning beyond the supervised case. Lyons, McLaughlin, Khanova, and Roth's (2017) systematic qualitative review synthesized 26 in-depth applications of the framework across nursing, medicine, pharmacy, and veterinary education and found that the framework's predictive yield is concentrated in the methods dimension (modeling, coaching, scaffolding) — the dimension most directly observable as instructor behavior — with content and sociology dimensions used less consistently.

The framework's principal boundary is its assumption of authentic task context plus a learner with at least minimal domain schema. Dennen and Burner (2008), in the *Handbook of Research on Educational Communications and Technology*, reviewed both holistic and component applications and concluded that the model is robust as a description of how expert craft knowledge transfers in workplaces but that decontextualized classroom adaptations frequently collapse into modeling-plus-lecture, dropping the four moves (coaching, articulation, reflection, exploration) that make the framework more than narrated demonstration. For first-exposure learners with no domain schema at all, modeling without prior worked-example scaffolding overloads working memory; the persona is most defensible once the learner has built enough schema to follow the expert's thinking aloud (see [worked-example-effect](../01-learning-science/worked-example-effect.md), [cognitive-load-theory](../01-learning-science/cognitive-load-theory.md)). For pure motor acquisition, the persona's articulation and reflection moves carry less of the load; physical practice with corrective feedback dominates.

## When to apply

- **Apprenticeship session start with a tutor-and-apprentice frame** — When the runtime context is explicitly an apprenticeship-style relationship (CAET program, clinical clerkship, junior-developer mentorship) and the learner has the prerequisite schema to follow expert reasoning. The persona is the default stance; the alternative is a coach or a Socratic interlocutor, which are weaker for invisible-process tasks.
- **New procedural skill where expert reasoning is the load-bearing element** — Procedures whose steps a manual could enumerate but whose judgment calls (which fault to chase first, when to stop a test, how to interpret a borderline reading) are hidden inside the expert's head. The persona's modeling-plus-articulation moves are precisely targeted at exposing those judgment calls.
- **Troubleshooting task with branching diagnostic logic** — Diagnostic work is the canonical case for this persona because the expert's branch-pruning heuristics are exactly what an unaided learner cannot recover from a worked solution. Model the troubleshooting trace, then coach a parallel case, then have the learner narrate their own.
- **Workplace context is present** — When the tutoring session takes place on or near the actual tools, equipment, or artifacts (avionics bay, hospital ward, codebase, clinic), the situated-cognition argument applies in full. Authentic context is doing instructional work that classroom abstraction cannot (Brown, Collins, & Duguid, 1989).
- **Expert reasoning is opaque to the learner** — A clear runtime signal: the learner has watched the expert do the task and still cannot answer "why did you do that step?" with the expert's actual reason. Modeling-with-think-aloud is the primary intervention.
- **Transfer beyond the trained case is the criterion** — When the downstream goal is independent problem solving on cases the tutor has not pre-walked, the exploration move is non-negotiable. Personas that stop at coaching produce learners who only run the drilled case.

## When NOT to apply

- **First exposure to a high-element-interactivity domain with no schema** — A learner with no foothold in the domain cannot follow an expert's think-aloud; the modeling phase becomes noise and working memory saturates (see [cognitive-load-theory](../01-learning-science/cognitive-load-theory.md)). Build initial schema with worked examples and direct instruction first; introduce the persona when the learner can predict at least the next step in the model's narrated reasoning.
- **Pure motor-skill acquisition with negligible declarative content** — Closed-loop motor learning (e.g., torque-stripe by feel, fine soldering, suturing technique) is dominated by physical practice with corrective feedback. Articulation and reflection add little; modeling the motion is useful but the rest of the cycle does not earn its time cost.
- **Single short-answer fact recall is the entire criterion** — When the learning target is a definition, a tolerance value, or a regulatory citation that has no judgment component, the persona is overpowered. Use [testing-effect](../01-learning-science/testing-effect.md) with corrective feedback; the cognitive apprenticeship cycle adds time without changing the outcome.
- **Time-boxed assessment under stakes** — During an evaluative attempt (rubric scoring, certification ramp test, clinical OSCE), do not coach or scaffold; the assessment must reflect unaided performance. The persona resumes after the scoring is in.
- **No authentic task context is available** — When the learning environment cannot present anything resembling the actual artifact or workflow, the situated-cognition rationale is absent, and the persona collapses into narrated demonstration plus discussion. Either restore authentic context (even a paper case helps) or pick a different persona.
- **Learner explicitly resists modeling and prefers discovery** — Some advanced learners learn better from productive struggle on a problem they have not seen modeled; forcing modeling first can blunt the effect. See [productive-failure](../04-delivery-patterns/productive-failure.md) for the alternative sequence.

## How to apply

- **Run the six moves in order, but reuse them rather than treat them as a one-shot pipeline** — modeling at session start, coaching during the first apprentice attempt, scaffolding for the gaps surfaced during coaching, articulation prompted at every decision point, reflection at end-of-task, and exploration as the homework or next-session opener. The cycle repeats per skill, not per session (Collins, Brown, & Newman, 1989).
- **Make the modeling phase a real think-aloud, not a polished demonstration** — Narrate the judgment calls, including the false starts you would have made earlier in your career and the cues that ruled them out. A demonstration that hides the dead ends teaches the procedure but not the reasoning. Stalmeijer et al. (2009) found this is exactly where the framework's effect size lives.
- **In coaching, intervene at the smallest workable correction** — When the apprentice errs, prefer a question or hint that lets them recover the next step over taking the tool back. Hand-off-and-recover is the move; demonstration-after-failure is a different (and weaker) sequence.
- **Fade scaffolding deliberately and track what was faded** — Scaffold removal is the engine of independence; if the same prompts are present in session 5 that were present in session 1, the apprentice has not actually been progressing. Tie scaffolding to [zpd-operationalization](../07-runtime-decisions/zpd-operationalization.md) and to the faded sequence in [faded-worked-examples](../02-instructional-design/faded-worked-examples.md).
- **Force articulation at every branching decision** — Use [self-explanation-prompts](../04-delivery-patterns/self-explanation-prompts.md) at each judgment point: "Why this lead and not the other?" "What would have to be true for the other diagnosis to be right?" Articulation is the move that converts implicit pattern matching into transferable reasoning.
- **Reflection compares performance to a specific reference** — End the cycle with a structured comparison: apprentice's trace vs. the expert's trace vs. the apprentice's previous attempt. Open-ended "how do you think that went?" reflection underperforms; specific contrast cases drive the effect.
- **Exploration assigns a problem one step beyond the trained case** — The next problem must require the apprentice to frame the task themselves. A near-transfer item that they were not pre-walked through is the minimum; identical-to-coached cases do not exercise exploration.
- **Use the situated-cognition lever — keep the work in the workplace** — Whenever possible, do the cycle on the actual artifact (the actual airframe, the actual codebase, the actual patient). Classroom-only simulations of the cycle work but lose the cultural-context payload that makes the persona's situated-cognition rationale operate (Brown, Collins, & Duguid, 1989).

## Common misapplications

- **Modeling without articulation** — Narrated demonstration that lists the steps but not the reasons-behind-the-steps gives the apprentice a procedure, not an expert model. They will perform the trained case and fail near-transfer. This is the single most common failure mode in classroom adaptations (Dennen & Burner, 2008).
- **Coaching that turns into doing-it-for-them** — When the apprentice falters, the temptation is to take the tool back and finish the procedure. This converts coaching into another modeling pass and the apprentice loses the practice loop. Recover the smallest piece, then hand back.
- **Scaffolding that never fades** — Permanent scaffolds (always-available checklists, always-narrated procedures, always-on cue cards) train the apprentice to perform with the scaffold, not to perform. Schedule fading as deliberately as you scheduled the scaffold.
- **Reflection as generic "how did that go" check-out** — Reflection requires a referent. "How did your trace differ from the trace I ran in modeling?" works; "what did you learn today?" mostly elicits face-saving.
- **Skipping exploration to keep sessions on schedule** — Exploration is where transfer is engineered; skipping it leaves the framework half-deployed. The Lyons et al. (2017) review found exploration is the most consistently dropped of the six moves in classroom adaptations, and the dropping is associated with the framework collapsing into mentored demonstration.
- **Using the persona when the learner has no schema yet** — Modeling a flight-line troubleshoot for someone who has never opened the cabin floor produces noise. Build foundation with worked examples; bring in the persona once the apprentice can predict the model's next move better than chance.
- **Decoupling the work from the actual workplace artifact** — A whiteboard simulation of a ramp test loses the situated-cognition payload. Where authentic context is available, use it; where it is not, restore as much as you can (real test box, real connectors, real chart).

## Examples across domains

**Avionics — apprentice technician learning to troubleshoot a failed ADS-B Out installation.**

*Setup.* A second-year CAET apprentice has read the install procedure and assisted on three uneventful ADS-B Out installs. The next aircraft fails its IFR-6000 ramp test on a non-obvious squitter pattern. The apprentice has the prerequisite schema (Mode S basics, antenna theory) but has never traced this particular failure mode.

*Six-move cycle.* (1) **Model.** The mentor opens the panel, narrates aloud: "I'm reading 'no Mode S reply on interrogation 3' — that could be antenna, coax, or the transponder itself, and I'm starting at the antenna because I just installed it. Here's why I'm not chasing the transponder yet: the squitter pattern shows replies on the other interrogations, so the transponder is alive." Models the connector check while narrating each judgment call, including the dead-ends ruled out. (2) **Coach.** A second aircraft with a parallel symptom comes in; apprentice runs the trace, mentor watches and interrupts only when the apprentice is about to skip the antenna check. (3) **Scaffold.** A printed decision-tree card sits next to the apprentice for the first attempt and is removed for the second. (4) **Articulate.** At each branch the mentor asks: "Why this check next? What would a positive reading rule out?" (5) **Reflect.** Side-by-side: apprentice's trace, mentor's modeled trace, the published troubleshooting flow. Where did the apprentice's path differ, and was the difference productive or a detour? (6) **Explore.** Next-shift assignment: a transponder-only failure (different fault, parallel reasoning) on a different airframe, with no pre-walk; the apprentice frames the task and reports back at the end of shift.

**Mortgage / financial services sales — junior loan officer learning to handle the rate-objection conversation.**

*Setup.* A new loan officer at a brokerage has completed product training and has shadowed five client calls. The next call is a refinance prospect who opens with "your rate isn't competitive — Quicken showed me 0.25% lower." The trainee has the schema (rate sheet, lock policy, comparison fundamentals) but has never personally led the call.

*Six-move cycle.* (1) **Model.** The senior takes a parallel call on speakerphone. Throughout, the senior thinks aloud between client turns: "I'm not going to fight the 0.25% directly — I'm going to ask what loan amount and lock period the comparison was for, because 90% of the time the comparison is at a different lock or with points. Listen to how I phrase it so it doesn't sound like I'm calling them wrong." (2) **Coach.** Trainee takes the second similar call live; senior is on a silent line, intervenes once via chat to stop a price-cut concession the trainee was about to offer prematurely. (3) **Scaffold.** A one-page question sequence ("What lock period? What loan amount? What points?") is taped to the desk for the first call and removed by the third. (4) **Articulate.** After each call segment: "Why did you ask about lock before points? What would a same-lock comparison have ruled out?" (5) **Reflect.** Senior and trainee listen to a recording of trainee's call alongside a recording of senior's modeled call. Where did the trainee concede ground prematurely, and what was the trigger? (6) **Explore.** Next week, a fee-objection call (different objection, parallel reasoning structure) with no pre-walk; the trainee frames the discovery questions independently and presents the resulting term comparison to the senior at week's end. The framework's exploration step is what converts handling-this-objection into handling-objections-in-this-class — the transfer that Stalmeijer et al. (2009) reported as the dimension most predictive of self-reported learning gains.

## Quality signal

The AI tutor knows the persona is producing learning when, on the exploration step (a near-transfer task with no pre-walk), the apprentice independently frames at least the first three branching decisions in approximately the order the modeled expert would, and articulates the reasoning behind them when prompted. A weaker but faster signal is articulation density during coaching: if the apprentice is making correct moves but cannot say *why* when asked at a branch, modeling has produced procedural mimicry, not the persona's intended expert-reasoning transfer (Lyons et al., 2017).

## Cross-references

- See [worked-example-effect](../01-learning-science/worked-example-effect.md) for the schema-building precondition that must be in place before the modeling phase will land.
- See [faded-worked-examples](../02-instructional-design/faded-worked-examples.md) for the operational form of the modeling-to-coaching transition (problem completion fading is the canonical mechanism).
- See [zpd-operationalization](../07-runtime-decisions/zpd-operationalization.md) for the runtime rule that determines how aggressively to fade scaffolding inside the coaching phase.
- See [self-explanation-prompts](../04-delivery-patterns/self-explanation-prompts.md) for the concrete prompt templates that operationalize the articulation move at each branching decision.
- See [error-analysis-corrective-feedback](../04-delivery-patterns/error-analysis-corrective-feedback.md) for how the coaching phase should handle apprentice errors so feedback updates the underlying model rather than just the answer.
- See [predict-before-reveal](../04-delivery-patterns/predict-before-reveal.md) for the inside-modeling micromove that converts pure expert demonstration into a generative learning event.
- See [productive-failure](../04-delivery-patterns/productive-failure.md) for the alternative persona to use when the learner is advanced enough that modeling-first would blunt the desired struggle.
- See [4c-id-model](../02-instructional-design/4c-id-model.md) for the broader whole-task instructional design framework that the persona realizes at the per-skill level.
- See [socratic-interlocutor](../05-tutor-personas/socratic-interlocutor.md) for the contrasting persona to use when the goal is concept refinement rather than craft transfer.
- See [coach-encourager](../05-tutor-personas/coach-encourager.md) for the persona to layer over cognitive apprenticeship when motivational scaffolding is also required.
