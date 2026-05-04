---
id: forgetting-curve
title: Forgetting Curve & Relearning
category: 01-learning-science
aliases: [ebbinghaus-curve, retention-curve, savings-curve]
evidence_strength: strong
# effect_size is null: foundational descriptive principle — the curve specifies the shape of
# retention loss and savings during relearning, not a single treatment-vs-control contrast.
effect_size: null
key_sources:
  - "Ebbinghaus, H. (1885/1913). Memory: A contribution to experimental psychology (H. A. Ruger & C. E. Bussenius, Trans.). New York: Teachers College, Columbia University."
  - "Murre, J. M. J., & Dros, J. (2015). Replication and analysis of Ebbinghaus' forgetting curve. PLoS ONE, 10(7), e0120644. doi:10.1371/journal.pone.0120644"
  - "Rubin, D. C., & Wenzel, A. E. (1996). One hundred years of forgetting: A quantitative description of retention. Psychological Review, 103(4), 734-760. doi:10.1037/0033-295X.103.4.734"
  - "Wixted, J. T. (2004). The psychology and neuroscience of forgetting. Annual Review of Psychology, 55, 235-269. doi:10.1146/annurev.psych.55.090902.141555"
  - "Bahrick, H. P. (1979). Maintenance of knowledge: Questions about memory we forgot to ask. Journal of Experimental Psychology: General, 108(3), 296-308. doi:10.1037/0096-3445.108.3.296"
  - "Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. Psychological Bulletin, 132(3), 354-380. doi:10.1037/0033-2909.132.3.354"
  - "Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. Psychological Science, 17(3), 249-255. doi:10.1111/j.1467-9280.2006.01693.x"
last_reviewed: 2026-04-29
applies_to: [retention, sequencing, decision]
contraindicated_when:
  - learner_state.first_exposure
  - learner_state.pre_criterion_accuracy
  - material.imminent_deadline_no_spacing_room
  - task_type.single_session_one_shot
runtime_triggers:
  - new_concept_completed
  - review_window_due
  - relearning_session_start
  - long_horizon_retention_required
  - certification_renewal_window_open
related: [spaced-retrieval, testing-effect, sm2-fsrs, desirable-difficulties, predict-before-reveal, mastery-thresholds]
---

# Forgetting Curve & Relearning

## One-line claim

Without deliberate review, retention of newly learned material decays rapidly in the first hours and days and more slowly thereafter; relearning a forgotten item is faster than learning it the first time, and that "savings" is what scheduled review converts into durable memory.

## Evidence base

The forgetting curve is the empirical description of how retention falls as a function of the time elapsed since learning. Ebbinghaus (1885/1913), serving as his own subject, learned long lists of CVC nonsense syllables to a fixed criterion and then relearned the same lists at retention intervals from 20 minutes to 31 days. He measured retention by the savings score — the proportional reduction in trials needed to relearn — and reported steep loss in the first hours (roughly half of savings gone within an hour), continuing more slowly across days, with non-trivial savings still detectable a month out. The savings method is what makes the forgetting curve tractable in practice: even when free recall is at floor, partial traces remain and resurface as faster relearning, so a "forgotten" item at +30 days is rarely a blank slate.

Murre and Dros (2015) ran the modern replication in *PLOS ONE* — the same paradigm as Ebbinghaus, with intervals of 20 min, 1 hr, 9 hr, 1 day, 2 days, and 31 days — and reproduced the curve's overall shape. The replication added a quantitative refinement: the curve is not perfectly smooth. A small but reliable upward "boost" appears starting at the 24-hour data point (Murre & Dros, 2015, fitting a boost parameter of 0.030 in Ebbinghaus's data and 0.131 in Mack's 1927 replication), consistent with overnight sleep-dependent consolidation slowing the rate of loss. Rubin and Wenzel (1996), in *Psychological Review*, fit 105 candidate two-parameter functions to 210 published retention datasets and found that the same four functions — logarithmic, power, exponential-in-square-root-of-time, and hyperbola-in-square-root-of-time — fit nearly all of them; autobiographical memory was the only major exception. The forgetting function is shaped, not arbitrary.

The mechanism behind the shape is interference plus consolidation. Wixted (2004), in *Annual Review of Psychology*, argued that everyday forgetting is dominated by non-specific interference from intervening mental activity rather than cue-overload competition between similar items, and that recently formed memories are vulnerable until consolidated — accounting for why sleep, alcohol, and benzodiazepines affect retention of recently learned material. Two interventions reliably bend the curve. Distributed practice flattens it: Bahrick's (1979) study in *JEP: General* showed that spacing relearning sessions 30 days apart instead of 1 day apart produced a retention advantage detectable up to eight years later, and Cepeda et al.'s (2006) meta-analysis of 184 articles confirmed the spacing benefit across age, materials, and outcomes (see [spaced-retrieval](../01-learning-science/spaced-retrieval.md)). Active retrieval flattens it more: Roediger and Karpicke (2006) in *Psychological Science* showed that the gap between tested and restudied prose passages reverses by 5 minutes — restudy is briefly higher — but widens substantially across delays of two days and one week, with testing producing the durable advantage (see [testing-effect](../01-learning-science/testing-effect.md)).

## When to apply

- **New concept just completed** — Use the curve to schedule the first revisit while savings are
  still sizable. The first hours after exposure are when loss is steepest; landing a retrieval
  attempt within 24 hours captures the consolidation boost Murre & Dros (2015) documented at
  the 24-hour data point.
- **Review window due** — When a scheduler (manual or algorithmic; see
  [sm2-fsrs](../07-runtime-decisions/sm2-fsrs.md)) flags an item is due, treat the trigger as
  a forgetting-curve data point: each on-time successful retrieval flattens the next segment
  of the curve and stretches the next interval.
- **Relearning session start** — When a learner returns to material previously studied but not
  recently used (months out from initial training, recurrent training kickoff, end-of-season
  refresher), expect lower free-recall accuracy than the prior session ended at, but
  substantial savings on relearning. Plan the session as relearning, not first-encoding.
- **Long-horizon retention required** — When the criterion test is days, weeks, or months out
  (certification, fieldwork, downstream coursework), the curve dictates that one exposure is
  insufficient regardless of how well the learner performed in-session. Schedule deliberate
  review.
- **Certification renewal window opens** — For periodic recertification, bias the review
  schedule toward the early part of the window. Bahrick (1979) showed the spacing-flattened
  curve persists across years; spreading review across 4–6 weeks rather than the prior weekend
  is the operative move.

## When NOT to apply

- **Learner has not yet reached criterion accuracy on the segment** — The forgetting curve
  describes loss of *encoded* material. Forcing a "review" pass on a learner who has not yet
  reached baseline accuracy in-session does not flatten a curve; it conflates encoding failure
  with retention loss. Finish encoding (reach roughly 70%+ in-session accuracy) before planning
  review, per Cepeda et al. (2006) on the encoding-vs-retention distinction.
- **First exposure to a high-element-interactivity concept** — Same boundary as the testing
  effect: the curve becomes meaningful only once a stable mental model is in place. Use worked
  examples and guided practice for the first pass, then schedule review.
- **Imminent deadline with no real spacing room** — If the criterion test is within hours, the
  spaced-relearning schedule that exploits the curve cannot deploy. Mass the practice and flag
  the situation as "next time, schedule earlier"; do not treat a 30-minute gap as meaningful
  spacing for a months-out goal.
- **Single-session one-shot tasks with no future retention requirement** — A briefing for a
  task that will never be repeated (one-time vendor walkthrough, one-off project handoff) is
  outside the curve's operational scope; forgetting after the task is acceptable, so review
  scheduling is wasted effort.
- **The "review" is a passive re-read with no retrieval** — Re-exposure without retrieval
  produces a flatter subjective sense of mastery without flattening the actual retention curve
  much (Roediger & Karpicke, 2006). If the format cannot be retrieval-with-feedback, the
  intervention is mostly hygiene, not curve-bending.

## How to apply

- **Schedule the first revisit inside the steep-loss window** — The curve falls fastest in the
  first hours and the first day. A retrieval attempt at end-of-session and a second attempt at
  +24 hours captures the interval where forgetting is most preventable, and lands across the
  consolidation boost Murre & Dros (2015) documented overnight.
- **Flatten subsequent intervals using the spacing ridgeline** — After the first revisit, hand
  the schedule to spacing rules: ISI ≈ 10–20% of the target retention interval (Cepeda et al.,
  2008, summarized in [spaced-retrieval](../01-learning-science/spaced-retrieval.md)). The
  curve dictates the *need* for review; the spacing literature dictates *when*.
- **Make every revisit a retrieval-with-feedback, not a re-read** — Roediger & Karpicke (2006)
  showed that across delays of two days to one week, retrieval-with-feedback flattens the
  curve substantially more than re-study at equal time. Default to active recall; see
  [predict-before-reveal](../04-delivery-patterns/predict-before-reveal.md) for the delivery
  pattern.
- **Treat relearning trials as diagnostic, not punitive** — When a learner fails a delayed
  retrieval, the savings are often still present (faster re-acquisition than the original
  pass), even though free recall failed. Use that asymmetry: re-teach quickly, do not restart
  from zero, then shrink the next ISI by a factor of 2–3.
- **Use savings, not free recall alone, as the retention measure when stakes allow** — When
  diagnosing whether material has truly been lost, time-to-relearn is a more sensitive measure
  than yes/no free recall (Ebbinghaus, 1885/1913, on the savings method). A learner who needs
  five minutes to re-acquire what originally took thirty has retained substantial structure.
- **Push relearning sessions farther apart, not closer, after a successful pass** — Each
  on-time correct retrieval is evidence the curve is flatter than the schedule assumed.
  Stretch the next ISI by 50–100% rather than holding it constant; this is what the
  SM-2/FSRS family of schedulers operationalizes (see
  [sm2-fsrs](../07-runtime-decisions/sm2-fsrs.md)).

## Common misapplications

- **Treating the curve as a fixed numerical formula** — Rubin & Wenzel (1996) found four
  different two-parameter functions fit retention data nearly equally well across 210 datasets;
  no single equation is "the" forgetting curve. Use the curve as a *shape* that motivates
  spaced review, not as a clock that says "review at hour 20.7".
- **Assuming a forgotten item is fully gone** — Free-recall failure does not mean zero
  retention. Ebbinghaus's savings method (and every replication since) shows residual structure
  that resurfaces during relearning; treating relearning as first-time learning wastes the
  savings.
- **Reviewing too early** — Reviewing inside the first 5 minutes (or restudying right after the
  initial exposure) lands at the top of the curve where retention is still near-ceiling. The
  intervention has nothing to flatten and is mostly working-memory rehearsal. Wait long enough
  for the curve to do real work.
- **Reviewing too late, then declaring the principle "didn't work"** — If the first revisit lands
  weeks after exposure with no intermediate reinforcement, savings are smaller and the session
  resembles first-time learning. The principle did not fail; the schedule did.
- **Confusing the curve with a one-time intervention** — One review at +24 hours is helpful but
  not sufficient for months-out retention. The curve is flattened by *repeated* spaced
  retrieval, not a single timed nudge. Plan the schedule, not just the next session.

## Examples across domains

**Avionics — annual recurrent training on Pitot-Static system leak-test procedures.**

*Setup.* A bench technician completes initial training on FAR Part 43 Appendix E
pitot-static leak-test procedures during onboarding — including allowable leak rates,
test-set hookup sequence, and the case-drain isolation step that guards against
overpressure damage. Twelve months later, the FAA-required recurrent check is approaching
and the technician has performed only two leak tests in the intervening year. The shop's
default move is a single 4-hour cram session the day before the practical.

*Application.* Treat the interval as a forgetting-curve problem. At month 11 (4 weeks
out), the tutor opens with a savings-style retrieval: "Without the IA on the bench,
walk me through the case-drain isolation step and tell me what failure mode that step
prevents." Free recall is partial — the technician gets the sequence but stalls on the
overpressure failure mode — and relearning takes 18 minutes vs. the original 45. That
savings number is the data: the underlying schema is intact, only details have decayed.
A second retrieval at week 13 covers tolerance values; a third at week 14 covers the
full hookup sequence end-to-end. Each session is retrieval-with-feedback, each ISI is
~7 days (≈10% of the 12-month-since-original target), and each correct pass stretches
the next interval. The recurrent practical at week 15 is performance, not first-time
testing — exactly what Bahrick's (1979) Spanish-vocabulary data predicted for
distributed relearning over months.

**L2 (second-language) acquisition — adult learner consolidating Spanish A2 vocabulary.**

*Setup.* An adult Spanish learner has just finished an A2-level unit on past-tense
verb conjugations (preterite vs. imperfect) and a 60-item lexical set on family,
food, and travel. They have completed the unit's exercises with ~85% accuracy and feel
"done." The criterion is a placement test in three months, after which they need to
hold the material for a year of B1 study where the verbs and vocabulary will be assumed.

*Application.* The curve dictates that 85% in-session accuracy will erode sharply
across the first week without intervention; Bahrick's (1979) Spanish data shows
distributed relearning is what produces multi-year retention. The tutor builds a
schedule around the curve: a +24-hour retrieval covering the highest-frequency 20
items and the preterite-vs-imperfect contrast (across the Murre & Dros 2015
consolidation boost), then ISIs at +3 days, +1 week, +3 weeks, +6 weeks, +10 weeks,
with retrieval as production ("Translate this sentence using the imperfect") rather
than recognition. Correct items move to longer ISIs; missed items get the next ISI
cut to 2 days and the conjugation re-explained. By the placement test, retention is
above the unit-end 85% rather than below, because each on-time retrieval flattened
the next segment of the curve. After the test, the same items rotate into B1 review
at ~3-week ISIs to hold the year-long horizon Bahrick's data targets.

## Quality signal

The forgetting curve is being managed when delayed-retrieval accuracy at each scheduled revisit holds above ~70% and the savings score (time-to-relearn relative to first learning) shrinks across successive sessions, indicating consolidation is outpacing decay. A failing schedule shows the opposite signature: revisit accuracy chronically below 60% and savings near zero (relearning takes nearly as long as original learning), meaning intervals are too long for the consolidation rate or the prior pass did not actually reach criterion. Cumulative retention at +30 days on items reviewed under the schedule should exceed retention on unreviewed control items by a margin consistent with the Cepeda et al. (2006) meta-analytic floor of d ≈ 0.4.

## Cross-references

- See [spaced-retrieval](../01-learning-science/spaced-retrieval.md) for the inter-study-interval rules that operationalize how to flatten the curve across sessions.
- See [testing-effect](../01-learning-science/testing-effect.md) for the active-recall mechanism that flattens the curve substantially more than passive re-exposure.
- See [sm2-fsrs](../07-runtime-decisions/sm2-fsrs.md) for the algorithmic schedulers that turn the curve into per-item review-due timestamps once item counts exceed manual tracking.
- See [desirable-difficulties](../01-learning-science/desirable-difficulties.md) for the broader framework that locates spaced relearning among the conditions that slow apparent learning while improving long-term retention.
- See [predict-before-reveal](../04-delivery-patterns/predict-before-reveal.md) for the session-level delivery pattern that turns each scheduled revisit into a retrieval rather than a re-read.
- See [mastery-thresholds](../07-runtime-decisions/mastery-thresholds.md) for the criterion-accuracy gate that distinguishes encoding failure from retention loss when interpreting low revisit scores.
