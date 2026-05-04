---
id: self-efficacy
title: Self-Efficacy
category: 06-motivation-engagement
aliases: [perceived-self-efficacy, task-specific-confidence]
evidence_strength: strong
effect_size: "Between-person r ≈ .38 (Stajkovic & Luthans 1998 meta-analysis, k=114, N=21,616); academic r ≈ .38 (Multon, Brown & Lent 1991, k≈70); university student GPA r ≈ .33 (Honicke & Broadbent 2016 systematic review, k=59)"
key_sources:
  - "Bandura, A. (1977). Self-efficacy: Toward a unifying theory of behavioral change. *Psychological Review*, 84(2), 191-215. doi:10.1037/0033-295X.84.2.191"
  - "Bandura, A. (1997). *Self-efficacy: The exercise of control*. New York: W. H. Freeman."
  - "Multon, K. D., Brown, S. D., & Lent, R. W. (1991). Relation of self-efficacy beliefs to academic outcomes: A meta-analytic investigation. *Journal of Counseling Psychology*, 38(1), 30-38. doi:10.1037/0022-0167.38.1.30"
  - "Stajkovic, A. D., & Luthans, F. (1998). Self-efficacy and work-related performance: A meta-analysis. *Psychological Bulletin*, 124(2), 240-261. doi:10.1037/0033-2909.124.2.240"
  - "Honicke, T., & Broadbent, J. (2016). The influence of academic self-efficacy on academic performance: A systematic review. *Educational Research Review*, 17, 63-84. doi:10.1016/j.edurev.2015.11.002"
  - "Sitzmann, T., & Yeo, G. (2013). A meta-analytic investigation of the within-person self-efficacy domain: Is self-efficacy a product of past performance or a driver of future performance? *Personnel Psychology*, 66(3), 531-568. doi:10.1111/peps.12035"
  - "Vancouver, J. B., Thompson, C. M., & Williams, A. A. (2001). The changing signs in the relationships among self-efficacy, personal goals, and performance. *Journal of Applied Psychology*, 86(4), 605-620. doi:10.1037/0021-9010.86.4.605"
last_reviewed: 2026-04-30
applies_to: [acquisition, retention, transfer]
contraindicated_when:
  - learner_state.overconfident
  - learner_state.first_exposure
  - task_type.motor_acquisition
  - material.high_element_interactivity_no_scaffolding
runtime_triggers:
  - pre_task_attempt
  - post_failure_recovery
  - new_difficult_unit_introduced
  - persistence_drop_detected
  - confidence_self_report_low
related:
  - self-determination-theory
  - goal-setting-theory
  - achievement-goal-theory
  - error-analysis-corrective-feedback
  - faded-worked-examples
  - coach-encourager
  - zpd-operationalization
---

# Self-Efficacy

## One-line claim

A learner's task-specific belief that they can execute the actions required to succeed predicts how much effort they expend, how long they persist after failure, and how much they actually learn — so the tutor must actively build that belief through enactive mastery experiences before pushing into difficulty.

## Evidence base

Bandura (1977) introduced self-efficacy in *Psychological Review* as task-specific judgments of personal capability that mediate the gap between knowing what to do and doing it. The construct is deliberately narrow: it is not global self-esteem, not domain-general confidence, but a forecast about a particular performance under particular conditions. Bandura specified four sources, ordered by potency: (1) **enactive mastery experience** (succeeding on the actual task), (2) **vicarious experience** (watching a similar other succeed), (3) **verbal persuasion** (credible feedback from a respected source), and (4) **physiological and affective states** (interpreting one's own arousal as readiness or threat). His 1997 monograph synthesized two decades of follow-up evidence and extended the model to academic, occupational, clinical, and athletic domains, establishing that successful enactive experience is roughly an order of magnitude more potent than persuasion alone.

Meta-analytic evidence places the effect on solid empirical ground. Multon, Brown, and Lent (1991) synthesized roughly 70 studies in the *Journal of Counseling Psychology* and reported an average correlation of r ≈ .38 between self-efficacy beliefs and academic performance, with a similar magnitude for academic persistence. Stajkovic and Luthans's (1998) *Psychological Bulletin* meta-analysis of 114 studies (k = 157, N = 21,616) found r = .38 between self-efficacy and work performance, with the relationship strengthening for low-complexity tasks and attenuating but remaining positive for high-complexity work. Honicke and Broadbent's (2016) systematic review in *Educational Research Review* covered 59 university-population studies from 2003-2015 and reported a moderate population correlation with grade-point average; effort regulation, deep processing strategies, and goal orientation partially mediated the link.

The principal boundary condition is the difference between *between-person* and *within-person* effects. Sitzmann and Yeo's (2013) meta-analysis in *Personnel Psychology* found that while self-efficacy is reliably correlated with performance across people, the within-person corrected correlation drops to ρ = .06 once linear performance trajectories are partialled out — meaning past performance drives self-efficacy more than self-efficacy drives subsequent performance. Vancouver, Thompson, and Williams (2001) showed in *Journal of Applied Psychology* that under stable task conditions, an upward perturbation in self-efficacy can *reduce* subsequent effort and performance via overconfidence-induced complacency. The operational implication is sharp: efficacy must be calibrated to actual capability, not inflated; and persuasion or false praise that outruns mastery evidence will backfire.

## When to apply

- **Pre-task attempt** — Before the learner attempts a task at the edge of their current skill, briefly elicit and shore up efficacy: confirm the relevant prior mastery, name the immediate sub-step, and surface the evidence that they can do it. Low pre-task efficacy predicts truncated effort and premature quitting.
- **Post-failure recovery** — Immediately after a substantive failure, learners' efficacy estimates drop disproportionately. Re-establish efficacy by isolating what *did* work, attributing the failure to a specific correctable cause, and scheduling a near-term success-likely retry rather than a harder challenge.
- **New difficult unit introduced** — When the curriculum steps up in conceptual or procedural difficulty, schedule an early enactive-mastery win on a graded sub-task before the full demand lands. The first success on the new unit anchors efficacy for the harder problems that follow.
- **Persistence drop detected** — When time-on-task, retry counts, or completion rates fall below the learner's prior baseline on equivalent material, treat it as an efficacy signal, not (yet) a knowledge gap. Investigate what the learner believes about their capability before re-teaching content.
- **Confidence self-report low** — When the learner reports doubt ("I don't think I can do this"), do not respond with verbal persuasion alone (the weakest of the four sources); structure a concrete graded success, then refer to it.

## When NOT to apply

- **Learner is overconfident relative to demonstrated capability** — When a learner's stated efficacy outruns their performance evidence (Vancouver et al., 2001; Sitzmann & Yeo, 2013), additional efficacy-building moves *worsen* performance by reducing effort. The correct response is calibration: surface the gap with objective performance data before any further encouragement.
- **First exposure to a complex new concept** — Demanding a confidence judgment or asking the learner to "trust they can do this" before they have even built a mental model creates noise. Build the schema first (worked examples, guided explanation); efficacy work belongs at the *application* boundary, not the encoding boundary.
- **Pure motor-acquisition phase with no declarative content** — Self-efficacy interventions help most when the learner can articulate what to do; in early motor learning where the bottleneck is perceptual-motor calibration, efficacy talk substitutes for the physical practice and feedback that actually drive the gain.
- **High-element-interactivity content without scaffolding** — Telling a novice they can do a 12-step procedure they have never broken down inflates efficacy without supplying the structure that would make it true. Decompose the task first, then build efficacy on each component.
- **Praise would be evidence-free** — Verbal persuasion only works when the source is credible and the message is specific (Bandura, 1997). Generic affirmations ("you're doing great!") that the learner can see do not match their actual work erode tutor credibility and depress efficacy on the next task.

## How to apply

- **Engineer the enactive mastery experience first** — The single highest-leverage move is to schedule an early, genuine success on a sub-task the learner can solve with current resources (Bandura, 1997). Decompose the target task until you find one rung the learner clears unaided, let them clear it, and explicitly name it as evidence of capability before stepping up.
- **Use vicarious experience with a similar-other coping model** — When mastery experience is not yet available, show the learner a relevant peer (real or recorded) working through the task — preferably a *coping* model who initially struggles and recovers, not a *mastery* model who breezes through. Coping models produce larger efficacy gains in observers who themselves expect to struggle.
- **Make verbal persuasion specific and tied to evidence** — "Your torque-sequence on the previous install was clean — the procedure transfers" beats "you've got this." Cite the exact prior performance, name the transferable component, and predict the next step is within reach. Persuasion that the learner cannot reconcile with their own evidence is discounted instantly.
- **Reframe arousal as readiness, not threat** — Pre-performance jitters are routinely interpreted as evidence of incapability. A short reframe — "what you're feeling is your system getting ready, not breaking down" — converts the same physiological signal into an efficacy input rather than a threat signal (Bandura, 1997, on physiological-state attribution).
- **Set proximal sub-goals, not just distal goals** — Distal goals ("pass the certification") are too far from action to feed efficacy; proximal sub-goals ("get this one ramp test trace clean today") generate the success evidence efficacy is built from. See [goal-setting-theory](../06-motivation-engagement/goal-setting-theory.md) for the proximal/distal trade-off.
- **Calibrate efficacy to performance, not above it** — After each task, ask the learner to rate their efficacy for the next equivalent task and compare to actual performance. If predicted > actual repeatedly, surface the gap; if predicted < actual repeatedly, surface the evidence of competence. The aim is accurate self-knowledge, not maximum confidence.
- **Use mastery framing in error analysis** — When the learner errs, attribute the error to a specific correctable cause ("you skipped the antenna-isolation check, which is a fixable step") rather than a global trait ("you're rushing"). See [error-analysis-corrective-feedback](../04-delivery-patterns/error-analysis-corrective-feedback.md).

## Common misapplications

- **Inflated praise as a substitute for mastery experience** — Telling a learner "you can do this!" without engineering an actual success is the most common failure mode. It produces a brief mood lift, no efficacy gain, and lower effort on the next attempt (Vancouver et al., 2001).
- **Treating self-efficacy as global self-esteem** — Generic "build their confidence" interventions miss that efficacy is task-specific. A learner can have high efficacy for ramp testing and low efficacy for soldering; collapsing them into one "confidence" score loses all operational signal.
- **Persuasion from a non-credible source** — Encouragement from a tutor the learner does not yet trust, or a tutor who has previously praised work the learner knew was sloppy, is discounted. Build credibility through accurate calibration first; spend persuasion capital second.
- **Mastery-model demonstrations to a struggling learner** — Showing a flawless expert performance to a learner who expects to struggle activates social comparison in the wrong direction and depresses efficacy. Use a coping model in this state.
- **Ignoring overconfidence as a problem** — Treating efficacy as monotonically good. When predicted performance chronically outruns actual performance, the right move is *calibration*, not more encouragement (Sitzmann & Yeo, 2013).

## Examples across domains

**Avionics — first solo VHF NAV/COM bench installation on a Garmin GTN 650Xi.**

*Setup.* A second-year apprentice has assisted on three GTN 650Xi installations under a senior technician and now must complete the rack-up, harness termination, and post-installation configuration solo before a sign-off. They tell the tutor "I don't know if I can wire the harness without him watching."

*Application.* The tutor names this as low pre-task efficacy and engineers an enactive-mastery rung first: pull the harness pinout sheet from the previous job (which the apprentice terminated under supervision and the senior signed off as clean), and ask the apprentice to walk through which connector positions they did themselves. The apprentice identifies six of nine — concrete prior evidence. The tutor then frames the new install as "the same nine pins, plus the audio-panel jumpers we covered Tuesday — you've already done the hard part." Proximal sub-goal: get the connector backshell torqued and continuity-checked before lunch, defer the post-config menu until after.

*Spacing.* After the connector passes continuity, the tutor explicitly logs it as efficacy evidence ("that's two clean harness terminations on Garmin nav/com hardware now") so the next install lands on a thicker base. A check-in at the start of the next install asks the apprentice to predict their own success rate on the harness and compares to the actual outcome — calibration, not just encouragement. The intervention rides the r ≈ .38 self-efficacy/work-performance correlation Stajkovic and Luthans (1998) reported for moderate-complexity tasks.

**Music performance — adult intermediate piano student preparing a Chopin Nocturne for a recital.**

*Setup.* An adult amateur returning to piano has played simpler pieces in studio for the teacher but never performed for an audience. Two weeks before a small student recital they tell the teacher "I'm going to forget the middle section and freeze." The teacher recognizes this as the physiological-arousal-as-threat misattribution Bandura (1997) describes plus low task-specific efficacy for *performing* (distinct from playing alone).

*Application.* Mastery rung: schedule three "performance simulations" in the next two weeks — first for the teacher alone (already a known success), then for a single trusted listener, then for two listeners. Each is a graded enactive success that builds efficacy specifically for the act of performing under observation. Vicarious component: show a recording of an intermediate adult amateur (a coping model, audibly nervous, who recovers from a small slip mid-piece) rather than a Horowitz performance. Reframe: "the heart-rate jump you'll feel walking out is the same one you felt last Tuesday before the studio run-through, and that one went fine — your body is loading, not failing."

*Follow-up.* Each simulation closes with a calibration question: "predict your error count for the next run-through" then compare to actual. The teacher avoids generic "you'll be great" persuasion in favor of specific, evidence-tied statements ("the bridge into the recap was solid in three of the last four run-throughs"). The intervention targets task-specific performance efficacy, not global musical confidence — Bandura's (1997) specificity rule applied.

## Quality signal

The tutor knows self-efficacy work is producing learning when (a) the learner's predicted-success
ratings track actual performance within ±15 percentage points across three consecutive tasks
(calibration) and (b) post-failure retry latency stays within 20% of pre-failure attempt rate
rather than collapsing. A faster proxy: persistence on the *first* hard problem after a difficulty
step-up; if the learner abandons the problem before the third attempt, efficacy is the bottleneck
regardless of what they say about it.

## Cross-references

- See [goal-setting-theory](../06-motivation-engagement/goal-setting-theory.md) for proximal vs. distal goals as the structural feed for enactive mastery experience.
- See [self-determination-theory](../06-motivation-engagement/self-determination-theory.md) for competence as one of three basic needs and how efficacy interacts with autonomy and relatedness.
- See [error-analysis-corrective-feedback](../04-delivery-patterns/error-analysis-corrective-feedback.md) for attributing errors in ways that protect rather than puncture efficacy.
- See [faded-worked-examples](../04-delivery-patterns/faded-worked-examples.md) for the scaffolding pattern that engineers graded enactive successes.
- See [coach-encourager](../05-tutor-personas/coach-encourager.md) for the persona that operationalizes credible, specific verbal persuasion.
- See [zpd-operationalization](../07-runtime-decisions/zpd-operationalization.md) for picking task difficulty that produces success-with-effort, the efficacy sweet spot.
- See [achievement-goal-theory](../06-motivation-engagement/achievement-goal-theory.md) for how mastery vs. performance goal orientations interact with efficacy gains (mastery framing protects efficacy through failure; performance framing makes efficacy fragile to comparison).
