---
id: desirable-difficulties
title: Desirable Difficulties
category: 01-learning-science
aliases: [desirable-difficulty, bjork-difficulties]
evidence_strength: strong
# Foundational umbrella concept; each instance (testing-effect, spaced-retrieval,
# interleaving) has its own effect-size estimate, so a single d for the umbrella is
# meaningless. See Bjork & Bjork (2011, 2020).
effect_size: null
key_sources:
  - "Bjork, E. L., & Bjork, R. A. (2011). Making things hard on yourself, but in a good way: Creating desirable difficulties to enhance learning. In M. A. Gernsbacher, R. W. Pew, L. M. Hough, & J. R. Pomerantz (Eds.), Psychology and the real world: Essays illustrating fundamental contributions to society (pp. 56-64). New York: Worth Publishers."
  - "Bjork, R. A., & Bjork, E. L. (1992). A new theory of disuse and an old theory of stimulus fluctuation. In A. F. Healy, S. M. Kosslyn, & R. M. Shiffrin (Eds.), From learning processes to cognitive processes: Essays in honor of William K. Estes (Vol. 2, pp. 35-67). Hillsdale, NJ: Erlbaum."
  - "Schmidt, R. A., & Bjork, R. A. (1992). New conceptualizations of practice: Common principles in three paradigms suggest new concepts for training. Psychological Science, 3(4), 207-217. doi:10.1111/j.1467-9280.1992.tb00029.x"
  - "Soderstrom, N. C., & Bjork, R. A. (2015). Learning versus performance: An integrative review. Perspectives on Psychological Science, 10(2), 176-199. doi:10.1177/1745691615569000"
  - "Bjork, R. A., & Bjork, E. L. (2020). Desirable difficulties in theory and practice. Journal of Applied Research in Memory and Cognition, 9(4), 475-479. doi:10.1016/j.jarmac.2020.09.003"
  - "Chen, O., Castro-Alonso, J. C., Paas, F., & Sweller, J. (2018). Undesirable difficulty effects in the learning of high-element interactivity materials. Frontiers in Psychology, 9, 1483. doi:10.3389/fpsyg.2018.01483"
  - "Yan, V. X., Bjork, E. L., & Bjork, R. A. (2016). On the difficulty of mending metacognitive illusions: A priori theories, fluency effects, and misattributions of the interleaving benefit. Journal of Experimental Psychology: General, 145(7), 918-933. doi:10.1037/xge0000177"
last_reviewed: 2026-04-29
applies_to: [acquisition, retention, transfer]
contraindicated_when:
  - learner_state.first_exposure
  - learner_state.overwhelmed
  - learner_state.pre_criterion_accuracy
  - material.high_element_interactivity_no_scaffolding
  - task_type.motor_acquisition
runtime_triggers:
  - new_concept_completed
  - review_window_due
  - practice_schedule_design
  - learner_reports_easy
  - long_horizon_retention_required
related: [testing-effect, spaced-retrieval, interleaving, cognitive-load-theory, expertise-reversal, productive-failure, forgetting-curve]
---

# Desirable Difficulties

## One-line claim

Conditions of practice that slow apparent learning and depress in-session performance — spacing, retrieval, interleaving, generation, varied contexts — produce substantially better long-term retention and transfer than conditions that maximize fluency during training.

## Evidence base

The desirable-difficulties framework is the unifying account behind several of the largest reliable durable-learning effects in cognitive psychology. Schmidt and Bjork's (1992) *Psychological Science* synthesis crossed three previously separate paradigms — motor-skill acquisition, frequency of knowledge of results, and contextual interference — and showed they shared a counter-intuitive structure: manipulations that depressed performance during training (intermittent feedback, randomized practice order, between-skill interference) consistently produced better post-training retention and transfer than manipulations that smoothed in-session performance. Bjork and Bjork's (1992) *New Theory of Disuse* supplied the mechanism: every memory has a storage strength (a stable index of how well it has been learned) and a retrieval strength (a context-bound index of how easily it comes to mind right now). Manipulations that lower retrieval strength during practice — a delay, a cue mismatch, a competing item — force more effortful retrieval next time, and that effortful retrieval is what increases storage strength. Fluent re-exposure raises retrieval strength briefly without doing much to storage; effortful retrieval after a desirable difficulty does the opposite.

Modern work pulls the umbrella tight around the same core. Bjork and Bjork's (2011) chapter "Making things hard on yourself, but in a good way" is the canonical statement of the framework and identifies the operational instances the runtime cares about: spacing across sessions, retrieval rather than re-presentation, interleaving rather than blocking, generation rather than passive study, and variation in surface features and contexts of practice. Soderstrom and Bjork's (2015) *Perspectives on Psychological Science* integrative review formalized the learning-versus-performance distinction at the heart of the framework: in-session performance is an unreliable index of durable learning, and the two can dissociate in either direction — learners can perform well during training and forget rapidly, or perform poorly during training and retain durably. Bjork and Bjork (2020) consolidates the practical guidance and emphasizes that motivational and metacognitive obstacles, not the empirical effects themselves, are the binding constraint on adoption in classrooms and self-study.

The boundary conditions are well characterized. Chen, Castro-Alonso, Paas, and Sweller's (2018) *Frontiers in Psychology* paper argues that desirable-difficulty manipulations stop working — and can reverse — when working memory is already saturated by high element interactivity in the material itself. The mechanism is straightforward in cognitive-load terms: a learner who lacks a stable schema cannot afford the additional load of generation, interleaving, or delayed retrieval; the difficulty becomes undesirable. Yan, Bjork, and Bjork (2016) document a separate adoption-side problem in *Journal of Experimental Psychology: General*: even after learners benefit from a desirable difficulty in a within-subject experiment, most still rate the easier condition as better for their learning, because the in-session sense of fluency feels diagnostic. Operationally, the framework requires both that the learner has a baseline schema (so the difficulty is desirable) and that the instructional system override the learner's metacognitive preference for the easier path.

## When to apply

- **New concept just completed and baseline encoded** — Once the learner can perform the target
  behavior in-session at roughly criterion accuracy, switch from fluency-maximizing practice
  (worked examples, blocked drills, re-presentation) to difficulty-introducing practice
  (retrieval, spacing, interleaving). The transition is the operative move; staying in fluent
  practice past criterion is the usual mistake.
- **Review window due** — When a spacing schedule (see
  [spaced-retrieval](../01-learning-science/spaced-retrieval.md)) fires, prefer the review form
  that introduces difficulty: retrieval rather than re-reading, interleaved rotation rather than
  item-by-item replay.
- **Practice schedule being designed** — When sequencing a multi-skill block (three
  troubleshooting tasks, three problem types, three plays), default to interleaving rather than
  blocking each skill's reps in isolation. Schmidt & Bjork (1992) showed contextual interference
  depresses in-session performance and improves post-training retention across paradigms.
- **Learner reports the material feels easy** — Subjective fluency is a documented poor predictor
  of durable learning (Yan, Bjork, & Bjork, 2016; Soderstrom & Bjork, 2015). "Felt easy" is a
  trigger to introduce difficulty (delay, generation prompt, varied context), not a green light
  to advance.
- **Long-horizon retention or transfer is the goal** — When the criterion is days-to-months out
  (certification, ramp-day testing, end-of-season tournament) or requires application to novel
  cases, the learning-vs-performance gap is largest and the desirable-difficulties moves are the
  highest leverage (Bjork & Bjork, 2011, 2020); see
  [interleaving](../01-learning-science/interleaving.md) for varied-context mechanics.

## When NOT to apply

- **Initial encoding of a high-element-interactivity concept** — Introducing generation,
  interleaving, or delayed retrieval before a baseline schema exists produces an undesirable
  difficulty: working memory is already loaded by element interactivity, and added challenge
  crowds out encoding (Chen, Castro-Alonso, Paas, & Sweller, 2018). Build the schema with
  worked examples first; introduce difficulty on the second pass.
- **Cognitive load is already saturated** — Slow responses, basic-error rate climbing, expressed
  overwhelm, or pre-assessment below ~50% on the current segment all signal that adding
  difficulty will harm rather than help. Reduce extraneous load; introduce the difficulty later.
- **Pre-criterion accuracy on the segment** — Below roughly 70% in-session accuracy, the
  learner has not yet built the storage strength that desirable difficulty is supposed to
  consolidate. Bjork & Bjork (2011) treat baseline encoding as a precondition; finish the
  encoding pass before switching modes.
- **Pure motor-acquisition phase** — While the learner is first stabilizing a motor pattern,
  randomized order or delayed feedback suppresses the practice volume needed for baseline
  acquisition. Schmidt & Bjork (1992) frames the desirable-difficulty schedule as
  *post-encoding* practice, not the encoding of brand-new motor patterns.
- **Imminent deadline with no spacing room** — If the criterion test is hours away, a
  desirable difficulty applied now trades performance the learner needs for retention they no
  longer need. Use the time to consolidate; flag for next-time scheduling.

## How to apply

- **Pick the right instance, not the umbrella** — "Apply desirable difficulties" is not an
  executable instruction; "introduce a 24-hour spacing gap before the next retrieval" is.
  Translate the framework into a specific operational instance: see
  [testing-effect](../01-learning-science/testing-effect.md) for retrieval,
  [spaced-retrieval](../01-learning-science/spaced-retrieval.md) for spacing, and
  [interleaving](../01-learning-science/interleaving.md) for rotation across related items.
- **Confirm baseline encoding before introducing difficulty** — In-session accuracy of roughly
  70-85% on the current segment is the operational gate. Below that, finish the encoding pass.
  Above ~90% with no effort, increase difficulty (longer delay, harder distractor, fuller
  interleave) — the learner is past the productive band.
- **Override the metacognitive illusion explicitly** — Yan, Bjork, & Bjork (2016) showed
  learners often prefer the easier (less effective) condition even after benefiting from the
  harder one. When a learner reports a manipulation feels less productive, surface the gap
  between in-session feel and delayed-retention performance and name the illusion. Do not
  capitulate to "let's go back to re-reading."
- **Calibrate to the desirable band** — Aim for effortful but successful retrieval, roughly
  70-85% accuracy. Chronic failure means undesirable for this learner-material pairing (Chen
  et al., 2018); chronic 100% means it is too easy to be doing work.
- **Stack the instances when the load budget allows** — Spacing + retrieval + interleaving
  compounds; the combination produces the largest reliable durable-learning effects in the
  literature (Bjork & Bjork, 2011, 2020). Stack only after baseline encoding is in place.

## Common misapplications

- **Introducing difficulty before encoding is stable** — The most common mistake. A learner
  asked to retrieve, generate, or interleave before a baseline schema exists fails, becomes
  frustrated, and the manipulation reverses (Chen et al., 2018). Confirm encoding first.
- **Treating "harder" as identical to "desirable"** — Difficulty is desirable only when it
  forces effortful retrieval of an already-encoded representation. Random extra steps,
  unnecessary disfluency, and punitive timing constraints are difficulty without the
  storage-strength payoff. Bjork & Bjork (2020) is explicit that the desirable label requires
  a learning benefit.
- **Reading short-term performance dips as failure** — A drop in in-session accuracy when
  switching from blocked to interleaved or from massed to spaced is the expected signature of
  the manipulation working, not a sign to revert. Soderstrom & Bjork (2015) is built around
  this trap.
- **Letting the learner's preference drive the schedule** — Learners reliably prefer fluent
  conditions even after benefiting from harder ones (Yan, Bjork, & Bjork, 2016). Outsourcing
  the schedule to learner preference reproduces the illusion.
- **Stacking difficulties past load tolerance** — Spacing + retrieval + interleaving + varied
  contexts + generation, all at once on a learner still building the schema, is undesirable.
  Add one instance at a time; keep the learner inside the productive band.

## Examples across domains

**Avionics — training a second-year shop technician across three Garmin GTN 650Xi navigator install variants.**

*Setup.* The technician has just completed three guided installs of the GTN 650Xi
back-to-back on a single airframe — clean-sheet, upgrade-from-430, dual-650Xi — getting the
third unaided. Conventional next move: another blocked morning on the same variant. The
desirable-difficulties move: switch to interleaving with delayed retrieval.

*Application.* Two days later the practice block rotates the three variants in randomized
order, with the technician asked to predict from memory which GAD 29 / GTP 59 wiring delta
applies before the harness is opened. In-session accuracy drops from 100% on the prior
blocked rep to roughly 70% on the interleaved-and-delayed rep — the expected signature of
the difficulty working (Schmidt & Bjork, 1992; Soderstrom & Bjork, 2015). The tutor names
the dip explicitly so the technician does not misread it as regression.

*Spacing.* A second interleaved-retrieval pass lands at +7 days, a third at +21 days. By the
+21-day pass, accuracy on identifying the correct install path from a customer ticket
exceeds the all-blocked control — the combined effect Bjork & Bjork (2011, 2020) describe
for stacked instances of the framework.

**Culinary apprenticeship — a second-year saucier apprentice learning the five French mother sauces.**

*Setup.* The apprentice has just completed a blocked rotation on béchamel: three production
runs the same morning, each cleaner than the last, the third restaurant-grade. Traditional
next move: a blocked morning on velouté, then espagnole, through the five mother sauces.
The desirable-difficulties move swaps blocking for interleaving with delayed retrieval and
varied pairings.

*Application.* Two days later the chef calls for four sauces in unannounced rotation across
the shift — béchamel, velouté, béchamel, hollandaise — with no recipe card on the line. The
apprentice must retrieve the roux ratio, temperature window, and failure-mode signature for
each before starting. In-session performance drops below the prior blocked rep — broken
hollandaise on the first attempt, slightly grainy béchamel on the third — and the apprentice
reports the practice felt worse than the blocked morning (Yan, Bjork, & Bjork, 2016
illusion). The chef calls the dip out: "This is what learning the *difference* between these
sauces feels like."

*Variation and spacing.* Across the next three weeks the chef interleaves the five sauces
with 3-7 day gaps between same-sauce exposures, varies the protein paired with each sauce
(so no fixed ingredient cue), and runs an unannounced +30-day retrieval check where the
apprentice produces two sauces from memory with no recipe. By end-of-quarter the
apprentice's accuracy under unfamiliar pairings exceeds the all-blocked cohort's by the
margin Schmidt & Bjork (1992) and Soderstrom & Bjork (2015) predict for varied-and-spaced
practice on a transfer criterion.

## Quality signal

The framework is producing learning when delayed-retention performance (at +24 hours, +7 days, +30 days) on items practiced under desirable-difficulty conditions exceeds matched items practiced under fluent conditions, even when in-session performance on the difficulty conditions is lower. A faster signal: when a learner reports a manipulation felt harder than the easy alternative AND delayed-retrieval accuracy is comparable or higher, the manipulation is in the productive band. When in-session accuracy under the difficulty drops below ~50% or the learner shows signs of overwhelm, the difficulty is undesirable for the current learner-material pairing and should be reduced (Chen et al., 2018).

## Cross-references

- See [testing-effect](../01-learning-science/testing-effect.md) for the retrieval instance — the most heavily replicated and largest single-effect instance of the framework.
- See [spaced-retrieval](../01-learning-science/spaced-retrieval.md) for the spacing instance and the spacing-plus-retrieval interaction that produces the largest combined effects.
- See [interleaving](../01-learning-science/interleaving.md) for the contextual-interference instance and rotation rules across related items.
- See [cognitive-load-theory](../01-learning-science/cognitive-load-theory.md) for the load-based account of when difficulty becomes undesirable (Chen et al., 2018).
- See [expertise-reversal](../01-learning-science/expertise-reversal.md) for the high-expertise boundary, where worked examples become inefficient and difficulty becomes desirable.
- See [productive-failure](../04-delivery-patterns/productive-failure.md) for a related but distinct pattern where pre-instruction problem-solving creates a desirable difficulty for subsequent direct instruction.
- See [forgetting-curve](../01-learning-science/forgetting-curve.md) for the retention dynamics that motivate why fluent re-exposure underperforms effortful retrieval.
