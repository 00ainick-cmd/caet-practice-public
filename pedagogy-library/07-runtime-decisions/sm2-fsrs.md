---
id: sm2-fsrs
title: SM-2 / FSRS
category: 07-runtime-decisions
aliases: [supermemo-sm2, free-spaced-repetition-scheduler, dsr-scheduler, spaced-repetition-algorithm]
evidence_strength: strong
# effect_size is null: SM-2/FSRS are scheduling algorithms, not pedagogical interventions —
# learning gain comes from spaced retrieval (see spaced-retrieval). Algorithm-level magnitudes
# appear as comparative log-loss/RMSE on review-prediction benchmarks (Ye et al. 2022: 12.6% cost
# reduction over SOTA; Settles & Meeder 2016: 45%+ error reduction for HLR on Duolingo).
effect_size: null
key_sources:
  - "Wozniak, P. A., & Gorzelanczyk, E. J. (1994). Optimization of repetition spacing in the practice of learning. Acta Neurobiologiae Experimentalis, 54(1), 59-62. PMID:8023714"
  - "Ye, J., Su, J., & Cao, Y. (2022). A stochastic shortest path algorithm for optimizing spaced repetition scheduling. In Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (pp. 4381-4390). New York: ACM. doi:10.1145/3534678.3539081"
  - "Cepeda, N. J., Vul, E., Rohrer, D., Wixted, J. T., & Pashler, H. (2008). Spacing effects in learning: A temporal ridgeline of optimal retention. Psychological Science, 19(11), 1095-1102. doi:10.1111/j.1467-9280.2008.02209.x"
  - "Karpicke, J. D., & Roediger, H. L. (2007). Expanding retrieval practice promotes short-term retention, but equally spaced retrieval enhances long-term retention. Journal of Experimental Psychology: Learning, Memory, and Cognition, 33(4), 704-719. doi:10.1037/0278-7393.33.4.704"
  - "Pavlik, P. I., & Anderson, J. R. (2008). Using a model to compute the optimal schedule of practice. Journal of Experimental Psychology: Applied, 14(2), 101-117. doi:10.1037/1076-898X.14.2.101"
  - "Settles, B., & Meeder, B. (2016). A trainable spaced repetition model for language learning. In Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Vol. 1, pp. 1848-1858). Berlin: ACL. doi:10.18653/v1/P16-1174"
  - "Lindsey, R. V., Shroyer, J. D., Pashler, H., & Mozer, M. C. (2014). Improving students' long-term knowledge retention through personalized review. Psychological Science, 25(3), 639-647. doi:10.1177/0956797613504302"
last_reviewed: 2026-04-30
applies_to: [sequencing, decision]
contraindicated_when:
  - learner_state.first_exposure
  - learner_state.pre_criterion_accuracy
  - material.imminent_deadline_no_spacing_room
  - task_type.single_session_one_shot
runtime_triggers:
  - new_concept_completed
  - review_window_due
  - scheduler_due_queue_built
  - grade_recorded
  - long_horizon_retention_required
  - certification_renewal_window_open
related: [spaced-retrieval, testing-effect, forgetting-curve, bayesian-knowledge-tracing, item-difficulty-discrimination, performance-factor-analysis, mastery-thresholds]
---

# SM-2 / FSRS

## One-line claim

When the runtime must decide WHEN to schedule the next retrieval of an already-learned item, compute the next-review interval from the learner's per-item review history — using SM-2's ease-factor update for low-data settings or FSRS's stability-difficulty-retrievability (DSR) model for calibrated pools — so each item is reviewed near the point where forgetting is about to set in but recall is still successful.

## Evidence base

The SuperMemo lineage operationalized the spacing effect as a per-item scheduler. Wozniak and Gorzelanczyk (1994), in *Acta Neurobiologiae Experimentalis*, derived a universal formula for inter-repetition intervals targeting a 95% retention threshold, generalizing Wozniak's earlier SuperMemo SM-2 algorithm (1985–1990) that had achieved ~92% retention on 10,255 English vocabulary items over a year of self-testing. SM-2 carries three pieces of state per card — a repetition number `n`, an ease factor `EF` (initialized at 2.5), and an interval `I` in days — and updates them from a 0–5 self-rated grade on each review: a passing grade (≥ 3) extends the interval as `I_{n+1} = I_n × EF` with `EF` adjusted by a fixed function of grade, while a failing grade resets `n` to zero and `I` to one day. The algorithm is closed-form, explainable, and runs without per-learner calibration; it remains the default scheduler in Anki's "legacy" mode and the algorithm against which modern schedulers are benchmarked.

Modern schedulers replace SM-2's heuristic ease-factor with a learned memory model. Ye, Su, and Cao (2022), in *Proceedings of KDD 2022*, formalized scheduling as a Markov decision process and trained a memory model on 220 million review logs from MaiMemo; their Stochastic-Shortest-Path Minimize-Memorization-Cost (SSP-MMC) scheduler reduced cumulative review cost at fixed retention by 12.6% over the prior best baselines. The Free Spaced Repetition Scheduler (FSRS) descends from this lineage, building on Wozniak's three-component DSR model — Difficulty (a per-item parameter on [1, 10]), Stability (the time, in days, for retrievability to fall to 90%), and Retrievability (the predicted recall probability given elapsed time and current stability). Each review updates D and S as a function of the learner's grade and the elapsed time since the last review; the next-review interval is then chosen so retrievability at review time matches a configured target (default 90% in FSRS-5). On the open-source spaced-repetition benchmark, FSRS variants outperform SM-2, half-life regression (Settles & Meeder, 2016), and Ebbinghaus-curve baselines on log-loss and RMSE for predicted recall.

The empirical defense for both algorithms rests on three converging evidence streams. First, the spacing effect itself: Cepeda et al. (2008) in *Psychological Science* showed across more than 1,350 participants that the optimal inter-study gap is roughly 10–20% of the target retention interval at week-scale and falls to ~5% at one-year scale — exactly the curvature SM-2's geometric expansion and FSRS's stability function approximate. Second, retrieval scheduling specifically: Karpicke and Roediger (2007), in *Journal of Experimental Psychology: LMC*, found that delaying the first retrieval is the dominant lever; expanding-interval schedules win short-term but equally spaced retrievals win at one-week-plus delays. Third, model-driven scheduling beats fixed schedules in classroom data: Pavlik and Anderson (2008) reported large effect-size gains for ACT-R-optimized schedules over fixed alternatives, Settles and Meeder (2016) reported 45%+ error reduction over baselines for half-life regression on Duolingo data, and Lindsey, Shroyer, Pashler, and Mozer (2014) reported a 16.5% retention gain on a one-month-delayed cumulative exam in a middle-school Spanish course using personalized adaptive review over time-matched massed review.

## When to apply

- **New concept just completed** — When the learner has answered an initial check correctly,
  schedule the first revisit through the algorithm rather than ad-hoc. SM-2 emits `I_1 = 1` day;
  FSRS emits an interval based on initial stability seeded from the first grade.
- **Review window due** — When the scheduler's due queue surfaces an item, serve it now rather
  than deferring; deferral inflates lapse risk asymmetrically because retrievability has already
  fallen below the configured target.
- **Grade recorded** — Immediately after a graded review, update per-item state (EF, n, I for
  SM-2; D, S for FSRS) and write the new due date back. Do not batch updates to session end.
- **Long-horizon retention required** — When the goal is recall in weeks-to-months (certification,
  fieldwork, downstream coursework), use the scheduler to drive review cadence rather than
  fixed-interval re-exposure (see [spaced-retrieval](../01-learning-science/spaced-retrieval.md)).
- **Certification renewal window opens** — Pre-decay items as the renewal date approaches; FSRS
  exposes a desired-retention knob that can be raised from 0.90 to 0.95 for the cert window and
  dropped back afterward.
- **Item pool large enough to leave optimization headroom** — FSRS's DSR estimates stabilize after
  roughly 4–6 reviews per card; SM-2 works from review one. Choose by available history depth.

## When NOT to apply

- **Learner is in the first-exposure encoding phase** — Schedulers operate on already-encoded
  items. Asking SM-2 or FSRS to schedule something the learner has not yet built a mental model
  for produces noise, not learning (Van Gog & Sweller, 2015 boundary; see
  [cognitive-load-theory](../01-learning-science/cognitive-load-theory.md)).
- **Pre-criterion accuracy** — If the learner has not yet passed a single graded check at all on
  this item, there is no `EF` or `S` to update meaningfully. Hold the item out of the spaced queue
  until it has crossed an initial criterion (typically two correct retrievals at short delay).
- **Imminent deadline with no spacing room** — When the test or fieldwork is in 24 hours, the
  scheduler's geometric expansion has nowhere to grow. Switch to a massed-then-tested loop with
  retrieval feedback; spacing requires a horizon to deliver its effect (Cepeda et al., 2008).
- **Single-session one-shot task** — A one-time tutorial with no follow-up has no future review
  to schedule. Use retrieval inside the session ([testing-effect](../01-learning-science/testing-effect.md))
  but skip the scheduler.
- **Pure motor skill acquisition** — Verbal-conceptual review schedulers were validated on
  declarative items; procedural motor execution is dominated by physical practice and feedback,
  not by spacing-of-recall (Karpicke & Roediger, 2007 was on word pairs, not motor skills).
  Schedule the declarative companion (torque values, sequencing) but not the motor execution.
- **Item pool too small for FSRS optimization** — FSRS's 19 trainable weights need ~1,000+
  reviews per learner-or-cohort to optimize; below that, run SM-2 with default constants and
  accept the precision loss until a calibration sample exists.

## How to apply

- **Default to SM-2 below 1,000 cumulative reviews per cohort** — SM-2's closed-form update is
  robust to small samples and explainable to learners. Initialize `EF = 2.5`, `n = 0`, `I = 1`;
  update per Wozniak (1990): for grade `q ≥ 3`, `EF ← max(1.3, EF + 0.1 - (5-q)·(0.08 + (5-q)·0.02))`
  and `I_{n+1} = I_n × EF`; for `q < 3`, reset `n = 0`, `I = 1`.
- **Switch to FSRS once a calibrated review log exists** — Train FSRS-5/6 weights on the cohort's
  history (open-source optimizer in `fsrs-rs`); set desired retention `r = 0.90` by default. Each
  review updates D and S; the next interval solves for elapsed time at which `R(t) = r` given
  current S. FSRS reduces log-loss vs. SM-2 on the standard benchmark (Ye et al., 2022).
- **Pin desired retention to the consequence of failure** — Default 0.90 for low-stakes practice;
  raise to 0.95 for high-stakes certification windows; drop to 0.85 for high-volume vocabulary
  where workload outweighs lapse cost. The retention knob is the runtime's primary control surface.
- **Treat lapses as state resets, not continuous decay** — Both SM-2 and FSRS shrink the interval
  sharply on a failing grade. Do not patch around this; the lapse-and-relearn cycle is what the
  scheduler is for (see [forgetting-curve](../01-learning-science/forgetting-curve.md) for why
  savings on relearning rebuild stability faster than first acquisition).
- **Cap the maximum interval per item** — Intervals can drift to years in open-ended schedules.
  Cap at the practical retention horizon (e.g., 18 months for an annual certification) so the
  item resurfaces within the policy window even if the math would defer further.
- **Combine with retrieval-modality discipline** — The schedule decides WHEN; the prompt format
  decides whether the review exercises retrieval (see
  [testing-effect](../01-learning-science/testing-effect.md) and
  [predict-before-reveal](../04-delivery-patterns/predict-before-reveal.md)). A spaced re-read is
  not a spaced retrieval.

## Common misapplications

- **Treating SM-2 ease factor as item difficulty** — `EF` is a per-card multiplier learned from
  one learner's grading; it is not the IRT `b` parameter. Mixing EF across learners or treating
  it as a static item property breaks the algorithm's assumptions.
- **Tuning intervals manually after each review** — The point of the scheduler is to remove
  human heuristics from the timing decision. Manual adjustments ("this seems too soon, push it
  out") inject noise the algorithm was designed to avoid (Pavlik & Anderson, 2008).
- **Running expanding-interval schedules at long retention horizons** — Karpicke and Roediger
  (2007) showed equally spaced retrieval beats expanding retrieval at week-plus delays. SM-2's
  geometric expansion is fine when the early intervals are already non-trivial; aggressive
  early-expansion schedules underperform at long delays.
- **Ignoring desired-retention as a control surface** — Many implementations leave `r = 0.90`
  forever. The 0.85 / 0.90 / 0.95 dial is how the runtime trades workload against lapse
  probability and is the cleanest knob for stakes-based personalization.
- **Mixing motor and declarative items in the same queue** — The scheduler's evidence base is
  declarative recall. Motor execution items in the same queue will appear scheduled but the
  spacing won't drive the relevant learning; they should be sequenced by procedural-practice
  rules, not DSR.
- **Not retraining FSRS weights as the cohort grows** — DSR weights drift with content and
  population. Retrain at least quarterly once the review log exceeds the calibration threshold;
  stale weights silently degrade to SM-2-grade predictions.

## Examples across domains

**Avionics — recurring G1000 NXi configuration card review for a Part 145 shop.**

*Setup.* A shop uses a tablet-based card deck for the G1000 NXi: GIA-63W discrete-IO pin map,
GTX-345R squitter timing, GFC-700 servo torque limits, weight-and-balance config codes,
software part-number cross-reference. Twelve technicians review the deck before any
installation that touches the avionics suite; 18 months of per-technician review logs exist.

*Schedule.* The runtime serves SM-2 for the first month a technician is on the deck (log too
thin for FSRS optimization), then promotes them to FSRS-5 once they cross 200 reviews. Desired
retention is pinned at 0.95 for the 30 days preceding any IA renewal and 0.90 the rest of the
year. A technician who lapses on the GIA-63W pin-map card sees it again at ~1 day, then
expanding through ~3, 7, 14, 30; FSRS adjusts each step from grade plus elapsed time, so a
hard-but-correct grade 3 grows the interval less than an easy grade 5. Maximum interval is
capped at 365 days so no card can drift past one annual recurrent cycle.

*Quality signal.* On the 30-day-delayed bench check, technicians on the spaced schedule answer
92–95% correct vs. 78% for the prior fixed-monthly-quiz cohort — within the range Lindsey et
al. (2014) found for personalized review over generic-spaced review.

**Software engineering onboarding — distributed-systems primitive review for a backend hire.**

*Setup.* A backend engineering org runs a 12-week onboarding with a deck of ~180 cards covering
distributed systems primitives: Raft phases, Paxos vs. Raft trade-offs, MVCC isolation
boundaries, Kafka partition rebalance triggers, gRPC deadline propagation rules, and the
team's internal idempotency-key conventions. Cards seed during weeks 1–4 from architecture
sessions; reviews continue through end-of-quarter.

*Schedule.* The platform runs FSRS-5 from day one (cohort's prior review log is large enough
to have trained weights). Desired retention is 0.90 for general primitives and 0.95 for
idempotency conventions, where ambiguity has caused two prior production incidents. A hire
who fails the Raft "log truncation on leader change" card on day 6 sees it again at +1 day,
+3, +9, +21; the gRPC deadline-propagation card, graded easy on day 4, jumps to +6 days,
+18, +50. Maximum interval is capped at 180 days; desired retention drops to 0.85 after
week 12 to ease workload as the hire moves into project work.

*Quality signal.* At the 90-day post-onboarding code-review checkpoint, the spaced cohort
produces zero idempotency-related review escalations vs. ~1 per hire in the
fixed-content-review baseline; FSRS log-loss on actual recall stays at or below the
benchmark target.

## Quality signal

The scheduler is calibrated when (a) empirical recall rate at served-due-date matches configured
desired retention within ±2 percentage points across the cohort, and (b) per-learner workload
stays within the agreed envelope (typically 4–10 minutes/day at FSRS defaults). If recall is
below target, retrain weights or raise the maximum-interval cap; if workload is above envelope,
desired retention is too high for the deck size or the cohort's encoding strength.

## Cross-references

- See [spaced-retrieval](../01-learning-science/spaced-retrieval.md) for the underlying spacing principle the schedulers operationalize on a per-item timing axis.
- See [testing-effect](../01-learning-science/testing-effect.md) for the retrieval-format discipline that determines whether each scheduled review actually exercises memory.
- See [forgetting-curve](../01-learning-science/forgetting-curve.md) for the descriptive curve FSRS's stability and retrievability functions parameterize.
- See [bayesian-knowledge-tracing](../07-runtime-decisions/bayesian-knowledge-tracing.md) for the per-skill mastery estimator that complements per-item scheduling when reviews are too sparse for DSR.
- See [item-difficulty-discrimination](../07-runtime-decisions/item-difficulty-discrimination.md) for IRT-based item selection that pairs with these schedulers on the WHAT-to-serve axis.
- See [performance-factor-analysis](../07-runtime-decisions/performance-factor-analysis.md) for an alternative skill-level estimator that uses spaced practice history without per-card DSR state.
- See [mastery-thresholds](../07-runtime-decisions/mastery-thresholds.md) for the cut-score logic that decides when an item leaves the spaced queue entirely.
