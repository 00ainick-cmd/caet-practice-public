---
id: spaced-retrieval
title: Spaced Retrieval / Distributed Practice
category: 01-learning-science
aliases: [distributed-practice, spacing-effect, spaced-practice]
evidence_strength: strong
effect_size: "Cohen's d ≈ 0.4–0.6 for spaced vs. massed (Cepeda et al. 2006 meta-analysis of 184 articles, 839 assessments); optimal inter-study interval ≈ 10–20% of the target retention interval (Cepeda et al. 2008)"
key_sources:
  - "Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. Psychological Bulletin, 132(3), 354-380. doi:10.1037/0033-2909.132.3.354"
  - "Cepeda, N. J., Vul, E., Rohrer, D., Wixted, J. T., & Pashler, H. (2008). Spacing effects in learning: A temporal ridgeline of optimal retention. Psychological Science, 19(11), 1095-1102. doi:10.1111/j.1467-9280.2008.02209.x"
  - "Bahrick, H. P. (1979). Maintenance of knowledge: Questions about memory we forgot to ask. Journal of Experimental Psychology: General, 108(3), 296-308. doi:10.1037/0096-3445.108.3.296"
  - "Karpicke, J. D., & Roediger, H. L. (2007). Expanding retrieval practice promotes short-term retention, but equally spaced retrieval enhances long-term retention. Journal of Experimental Psychology: Learning, Memory, and Cognition, 33(4), 704-719. doi:10.1037/0278-7393.33.4.704"
  - "Carpenter, S. K., Cepeda, N. J., Rohrer, D., Kang, S. H. K., & Pashler, H. (2012). Using spacing to enhance diverse forms of learning: Review of recent research and implications for instruction. Educational Psychology Review, 24(3), 369-378. doi:10.1007/s10648-012-9205-z"
  - "Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. Psychological Science in the Public Interest, 14(1), 4-58. doi:10.1177/1529100612453266"
  - "Rohrer, D., & Taylor, K. (2007). The shuffling of mathematics problems improves learning. Instructional Science, 35(6), 481-498. doi:10.1007/s11251-007-9015-8"
last_reviewed: 2026-04-29
applies_to: [acquisition, retention, transfer]
contraindicated_when:
  - learner_state.first_exposure
  - learner_state.pre_criterion_accuracy
  - material.imminent_deadline_no_spacing_room
  - task_type.single_session_one_shot
runtime_triggers:
  - new_concept_completed
  - review_window_due
  - session_start_warmup
  - certification_renewal_window_open
  - long_horizon_retention_required
related: [testing-effect, forgetting-curve, interleaving, sm2-fsrs, predict-before-reveal, desirable-difficulties]
---

# Spaced Retrieval / Distributed Practice

## One-line claim

Distributing study or retrieval attempts across multiple sessions separated in time produces substantially better long-term retention than the same total practice massed into a single session.

## Evidence base

Distributed practice — also called the spacing effect — is the finding that for a fixed amount of study time, breaking the practice into multiple sessions separated by gaps produces durably better retention than packing the same time into one session. Cepeda, Pashler, Vul, Wixted, and Rohrer's (2006) meta-analysis in *Psychological Bulletin* synthesized 839 assessments across 317 experiments in 184 articles and reported a robust spacing benefit across age groups, materials, and outcome measures. Critically, the meta-analysis showed that the inter-study interval (ISI) and the retention interval interact: the optimal gap between study sessions grows as the desired retention interval grows. Massed practice — back-to-back repetitions inside one session — consistently underperformed any non-zero gap, with the disadvantage widening as the test was pushed further out.

Cepeda, Vul, Rohrer, Wixted, and Pashler's (2008) follow-up in *Psychological Science* operationalized the schedule. Across more than 1,350 participants studying trivia facts with review gaps of up to 3.5 months and final tests up to a year later, the team mapped a "temporal ridgeline" — the optimal ISI as a function of the target retention interval. The rule of thumb that emerged: the best ISI is roughly 10–20% of the target retention interval for retention windows of weeks, falling to about 5% for one-year retention. Bahrick's (1979) earlier landmark paper in *Journal of Experimental Psychology: General* established that this scales out to years, not just weeks; spacing relearning sessions 30 days apart rather than 1 day apart produced an advantage that was still measurable eight years later for Spanish vocabulary. Karpicke and Roediger (2007) in *Journal of Experimental Psychology: LMC* compared expanding-interval schedules (e.g., 1, 5, 25 minutes) to equally spaced schedules and found that expanding schedules win at very short retention intervals, but equal spacing wins at longer ones — a finding that constrains naive "expanding interval" heuristics imported from spaced-repetition software folklore.

The principle compounds with retrieval. Carpenter, Cepeda, Rohrer, Kang, and Pashler's (2012) *Educational Psychology Review* synthesis showed spacing benefits hold across vocabulary, mathematics, science concepts, motor skills, and skill generalization in classroom settings. Dunlosky et al. (2013) ranked distributed practice — alongside practice testing — as one of only two techniques earning the highest "high utility" rating across age, ability, materials, and outcomes. The combination of spacing plus retrieval (see [testing-effect](../01-learning-science/testing-effect.md)) produces the largest reliable durable-learning effects in the cognitive psychology literature; spacing without retrieval still works but is dominated by spaced retrieval whenever both are operationally available.

## When to apply

- **New concept just completed** — Schedule the second exposure as a spaced revisit, not an immediate
  re-read. The first revisit lands hours-to-days later; the value of the spacing effect requires a
  gap measured in at least minutes-of-clock-time, ideally hours, between exposures.
- **Review window due** — When a scheduler (manual or algorithmic; see
  [sm2-fsrs](../07-runtime-decisions/sm2-fsrs.md)) flags an item is due, route it to retrieval in
  the current session rather than deferring or re-presenting. The spacing curve is set up around
  the review *firing*, not around inspection.
- **Session start warmup** — Open every session after the first with a brief retrieval pass over
  prior-session material before introducing new content. Two to five minutes of recall on the
  previous segment converts the gap between sessions into a spaced-retrieval episode at near-zero
  marginal time cost.
- **Long-horizon retention required** — Whenever the criterion measure is days, weeks, or months
  away (certification exam, recurrent training, ramp-day testing, end-of-season tournament),
  spacing is the highest-leverage move available. The Bahrick (1979) data showed spaced
  relearning advantages that survived years.
- **Certification renewal window opens** — For periodic recertification (avionics recurrent,
  medical CME, lifeguard renewal), distribute relearning across the weeks leading into renewal
  rather than cramming the prior weekend; Carpenter et al. (2012) documented spacing benefits
  in applied recertification-style settings.
- **Combine with retrieval whenever feasible** — Spacing applied to passive re-presentation works;
  spacing applied to retrieval works substantially better. Default to spaced retrieval, fall
  back to spaced re-presentation only when retrieval is contraindicated (see
  [testing-effect](../01-learning-science/testing-effect.md)).

## When NOT to apply

- **Learner has not yet reached criterion accuracy on the segment** — Spacing accelerates
  consolidation of stable knowledge; it does not fix encoding failures. If the learner is below
  roughly 70% accuracy in-session on the current segment, finish the encoding pass first and
  begin spacing once a baseline mental model exists. Carpenter et al. (2012) emphasize that
  spacing operates on already-encoded material.
- **First exposure to a high-element-interactivity concept** — The same boundary as the testing
  effect applies. While the learner is integrating many interacting elements for the first time,
  insert worked examples and guided practice; introduce spacing on the second pass once the
  schema is in place.
- **Imminent deadline with no real spacing room** — If the criterion test is within hours and the
  learner has not yet seen the material, the spacing schedule cannot deploy. Massed practice
  with retrieval is the operative move; flag the situation as "next time, schedule earlier" and
  do not pretend a 30-minute gap is meaningful spacing for a months-out goal.
- **Single-session one-shot tasks with no future retention requirement** — When the goal is
  performance inside the next 60 minutes and forgetting after that is acceptable (e.g., a
  one-time briefing for a non-recurring task), spacing's benefit accrues to a horizon the
  learner does not need. Mass the practice and move on.
- **The "gap" is too short to qualify** — Three retrievals at 0, 30 seconds, and 60 seconds is
  not spaced practice; it is working-memory rehearsal that mostly looks spaced. Cepeda et al.
  (2006) showed gains require ISIs measured in minutes-to-days, scaled to the retention target.

## How to apply

- **Set the inter-study interval at roughly 10–20% of the target retention interval** — Cepeda
  et al. (2008) mapped the ridgeline: for a 1-week target, ISIs of ~12–24 hours; for a 1-month
  target, ~3–7 days; for a 6-month target, ~3–4 weeks; for a 1-year target, ~3 weeks (ratio
  drops to ~5% at long horizons). Treat as defaults — a learner's failed-recall history is the
  stronger signal.
- **Default to equal spacing past the first revisit; reserve expanding intervals for short
  horizons** — Karpicke & Roediger (2007) showed expanding schedules help only inside short
  retention windows; equally spaced revisits win at longer ones. Practical compromise: slight
  expansion across the first 2–3 reviews (1 day → 3 days → 7 days), then equal spacing.
- **Combine spacing with retrieval, not re-presentation** — Each scheduled revisit should be a
  retrieval attempt followed by feedback, not a passive re-read. The spacing-plus-retrieval
  combination is the highest-leverage operational pattern in the literature; see
  [testing-effect](../01-learning-science/testing-effect.md) for the retrieval mechanics and
  [predict-before-reveal](../04-delivery-patterns/predict-before-reveal.md) for the
  session-level move.
- **Hand the schedule to an algorithm when item count grows past ~20** — Manual scheduling is
  fine for a handful of items but fails to scale. Use an SM-2-derived or FSRS scheduler (see
  [sm2-fsrs](../07-runtime-decisions/sm2-fsrs.md)) once the deck or knowledge-component set
  exceeds what the tutor can track in working memory.
- **Reset the interval after a failed retrieval, but do not restart from zero** — A wrong
  answer signals the prior gap was too long; shrink the next ISI by a factor of 2–3 (e.g.,
  7 days → 2 days), do not collapse to "tomorrow." Repeated failures justify a fuller reset.
- **Interleave spacing with related items, not duplicates** — Spacing the same item is the
  spacing effect; spacing while rotating across related items adds the interleaving benefit
  on top (Rohrer & Taylor, 2007). See
  [interleaving](../01-learning-science/interleaving.md) for the rotation rules.

## Common misapplications

- **Treating session-internal repetition as spacing** — Three retrievals inside one 30-minute
  session are not spaced practice; the gap between attempts must be long enough that working
  memory is not still holding the answer. Cepeda et al. (2006) found short within-session ISIs
  produce only a fraction of the benefit of cross-session ISIs.
- **Importing spaced-repetition app intervals as gospel** — Default Anki/SuperMemo schedules
  encode SM-2's 1990s heuristics, not the empirical ridgeline. They are reasonable starting
  points, not laws of nature; a learner's actual recall outcomes drive interval adjustment, not
  the algorithm's prior.
- **Believing "expanding intervals are always better"** — A folklore claim from spaced-repetition
  forums, contradicted by Karpicke & Roediger (2007) for retention horizons beyond minutes.
  Equal spacing wins at longer horizons; expanding helps only at very short ones.
- **Cramming and calling it "compressed spacing"** — Five retrievals at 0, 5, 10, 15, 20 minutes
  are massed practice with extra steps. Spacing requires the gap to scale with the retention
  goal; minutes do not buy you months.
- **Skipping the second revisit because the first one was correct** — A correct first retrieval
  signals encoding succeeded, not that retention is consolidated. The Bahrick (1979) data
  shows spaced relearning produces durable advantages even when the learner gets the item
  right in the early pass; do not retire items prematurely.

## Examples across domains

**Avionics — recurrent training on Reduced Vertical Separation Minimums (RVSM) maintenance procedures.**

*Setup.* A shop technician is approaching the end of their two-year RVSM maintenance
authorization cycle. Recurrent training requires procedural competence on altimeter
static-port calibration, ADC self-test interpretation, and tolerance verification — material
originally learned 18 months ago and used intermittently since. The shop's traditional
approach is a single 8-hour cram day the week before renewal.

*Spacing schedule.* Replace the cram with a distributed schedule across the 6 weeks leading
into renewal. Week 1: a 30-minute retrieval session on static-port calibration tolerances and
the three failure modes that drive a "fail" verdict. Week 3: a 20-minute retrieval on ADC
self-test bit-pattern interpretation, plus a re-prompt on the Week 1 material. Week 5: a
30-minute combined retrieval covering both prior topics plus the tolerance-verification
sequence, with corrective feedback on every miss. Week 6 (renewal week): one final 45-minute
combined pass. The ISIs (~14 days) sit near the Cepeda et al. (2008) ridgeline for a
6-week-to-2-year retention target, and the format is retrieval-with-feedback rather than
re-reading. The technician walks into the practical with an additional roughly d ≈ 0.5
expected retention advantage on the procedural items versus the cram-day baseline (Cepeda
et al., 2006 meta-analytic average).

**Basketball coaching — installing a new pick-and-roll defensive coverage across a season.**

*Setup.* A high-school varsity coach is installing a new "ICE" pick-and-roll defensive
coverage in the second week of preseason. Players must recognize the action, call the
coverage, and execute the rotation by the conference opener (six weeks out) and retain
it through playoffs three months later. The traditional approach: hammer the install in
three consecutive practices and assume it sticks.

*Spacing schedule.* The install lesson goes in on Monday of Week 1, with massed walk-through
reps that day to encode the rotations (cognitive-load reasoning: the players are first
exposure, so spacing comes after baseline accuracy is reached). On Tuesday of Week 1,
12 minutes of live retrieval drills (call-and-execute) close the encoding pass. Week 2
opens with a 10-minute warm-up that reproduces the same call-and-execute scenario from
memory before any new material — session-start retrieval over the 6-day gap. Week 3 adds
a video-recognition retrieval (clip plays, players freeze and call the coverage) plus
two reps. Week 5 spaces in another live retrieval block. Once conference play starts,
the coverage cycles back into the warm-up rotation every 7–10 days through the season,
with reset-after-miss when a game shows the rotation breaking down. The 6-week ISI cadence
sits inside the Cepeda et al. (2008) ridgeline for a season-long (~5-month) retention
target, and Carpenter et al. (2012) explicitly documents spacing benefits for motor-skill
generalization tasks of this kind.

## Quality signal

Spacing is producing learning when retrieval accuracy on each scheduled revisit lands inside roughly 70–90% — within the desirable-difficulty band. Accuracy chronically above 90% signals the intervals are too short (the gap is not buying anything; lengthen the next ISI by ~50%). Accuracy chronically below 70% signals the intervals are too long for current consolidation (shrink the next ISI by a factor of 2 and confirm the underlying encoding is sound). A successful spacing schedule should also show cumulative retention on retired items at +30 days exceeding the same items' retention without spacing by Cohen's d > 0.3, the Cepeda et al. (2006) meta-analytic floor.

## Cross-references

- See [testing-effect](../01-learning-science/testing-effect.md) for the retrieval mechanics that combine with spacing to produce the largest durable-learning effects in the literature.
- See [forgetting-curve](../01-learning-science/forgetting-curve.md) for the underlying retention curve that motivates why spaced revisits beat massed re-exposure.
- See [interleaving](../01-learning-science/interleaving.md) for how to rotate across related items inside a spaced schedule.
- See [sm2-fsrs](../07-runtime-decisions/sm2-fsrs.md) for the algorithmic schedulers that operationalize spacing once item counts grow past manual tracking.
- See [predict-before-reveal](../04-delivery-patterns/predict-before-reveal.md) for the session-level retrieval pattern that turns each scheduled revisit into a productive recall attempt.
- See [desirable-difficulties](../01-learning-science/desirable-difficulties.md) for the broader framework that spaced retrieval instantiates.
