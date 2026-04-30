---
id: pretesting-effect
title: Pretesting Effect
category: 01-learning-science
aliases: [prequestion-effect, errorful-generation, prequestioning]
evidence_strength: strong
effect_size: "Hedges' g ≈ 0.54 specific, g ≈ 0.04 general (St. Hilaire, Chan, & Ahn 2024 preregistered meta-analysis, k = 97 specific / k = 91 general); Pan & Carpenter (2023) review reports g = 0.66 specific, g = 0.01 general; Latimier et al. (2019) head-to-head pretesting d = 0.35 vs. posttesting d = 0.74"
key_sources:
  - "Carpenter, S. K., & Toftness, A. R. (2017). The effect of prequestions on learning from video presentations. Journal of Applied Research in Memory and Cognition, 6(1), 104-109. doi:10.1016/j.jarmac.2016.07.014"
  - "Pan, S. C., & Sana, F. (2021). Pretesting versus posttesting: Comparing the pedagogical benefits of errorful generation and retrieval practice. Journal of Experimental Psychology: Applied, 27(2), 237-257. doi:10.1037/xap0000345"
  - "Richland, L. E., Kornell, N., & Kao, L. S. (2009). The pretesting effect: Do unsuccessful retrieval attempts enhance learning? Journal of Experimental Psychology: Applied, 15(3), 243-257. doi:10.1037/a0016496"
  - "Kornell, N., Hays, M. J., & Bjork, R. A. (2009). Unsuccessful retrieval attempts enhance subsequent learning. Journal of Experimental Psychology: Learning, Memory, and Cognition, 35(4), 989-998. doi:10.1037/a0015729"
  - "Latimier, A., Riegert, A., Peyre, H., Ly, S. T., Casasanto, D., & Ramus, F. (2019). Does pre-testing promote better retention than post-testing? npj Science of Learning, 4, 15. doi:10.1038/s41539-019-0053-1"
  - "Pan, S. C., & Carpenter, S. K. (2023). Prequestioning and pretesting effects: A review of empirical research, theoretical perspectives, and implications for educational practice. Educational Psychology Review, 35(4), 97. doi:10.1007/s10648-023-09814-5"
  - "St. Hilaire, K. J., Chan, J. C. K., & Ahn, D. (2024). Guessing as a learning intervention: A meta-analytic review of the prequestion effect. Psychonomic Bulletin & Review, 31(3), 919-942. doi:10.3758/s13423-023-02353-8"
last_reviewed: 2026-04-29
applies_to: [acquisition, retention]
contraindicated_when:
  - learner_state.overwhelmed
  - learner_state.no_followup_study_window
  - material.high_element_interactivity_no_scaffolding
  - task_type.transfer_to_untested_content
runtime_triggers:
  - new_segment_about_to_start
  - video_or_lecture_about_to_play
  - reading_assignment_about_to_open
  - pre_assessment_check_in
related: [testing-effect, predict-before-reveal, cognitive-load-theory, worked-example-effect, desirable-difficulties, error-analysis-corrective-feedback]
---

# Pretesting Effect

## One-line claim

Asking the learner to attempt questions on material they have not yet studied — and then immediately exposing them to the correct content — produces better retention of the directly tested information than starting with the content cold, even when nearly all initial attempts are wrong.

## Evidence base

The pretesting effect (also called the prequestion effect, prequestioning, or errorful generation) is the finding that an initial test on not-yet-studied material, followed by a correct-answer study opportunity, produces better memory for the tested content than skipping the initial test and going straight to study. Richland, Kornell, and Kao (2009) provided the foundational demonstration in *Journal of Experimental Psychology: Applied*: across five experiments, learners who tried to answer questions about an essay on vision before reading it outperformed learners who instead got extended reading time, and the advantage held even on the analytic subset where the pretest had produced no correct retrievals. Kornell, Hays, and Bjork (2009) ran the strictest test in *Journal of Experimental Psychology: LMC* by using fictional general-knowledge items and weak-associate cue words specifically engineered so participants almost never guessed correctly; the unsuccessful-retrieval condition still beat extended-study controls on the subsequent test. Carpenter and Toftness (2017) extended the finding to video presentations in *Journal of Applied Research in Memory and Cognition*: undergraduates who answered prequestions before each segment of an educational video remembered more of the directly questioned content with no harm to non-questioned content.

The modern meta-analytic picture is unusually consistent on the headline claim and unusually clear on its boundary. St. Hilaire, Chan, and Ahn's (2024) preregistered meta-analysis in *Psychonomic Bulletin & Review* aggregated 97 specific-effect estimates and reported a moderate Hedges' g ≈ 0.54 advantage of pretesting over study-only on directly pretested content, with a virtually nonexistent g ≈ 0.04 effect on non-pretested content (k = 91). Pan and Carpenter's (2023) narrative review in *Educational Psychology Review* converged on the same split: g ≈ 0.66 for specific (directly tested) content versus g ≈ 0.01 for general (untested) content. Pan and Sana (2021) showed in five experiments (n = 1,573) in *Journal of Experimental Psychology: Applied* that pretesting was competitive with — and on overall scores exceeded — posttesting on expository text passages, with the advantage holding across multiple-choice and cued-recall formats and with or without correct-answer feedback.

The principal boundary condition is transfer. Latimier et al. (2019) in *npj Science of Learning* directly compared pretesting to posttesting on a 7-day delayed retention test: pretesting produced a real but modest benefit (d = 0.35) versus a substantially larger posttesting benefit (d = 0.74), and only posttesting produced reliable transfer to previously untested questions. The operational implication is sharp: pretesting is a high-value front-of-segment move for the specific content named in the prequestion stem, but it is not a substitute for retrieval practice after encoding (see [testing-effect](../01-learning-science/testing-effect.md)) when the goal is durable transfer to novel items.

## When to apply

- **A new segment is about to start** — Before introducing a coherent block of new material
  (5–15 minutes of reading, video, or lecture), pose 2–4 prequestions whose answers will
  appear in the upcoming content. The pretest plus subsequent study delivers the
  specific-content benefit (Carpenter & Toftness, 2017; Pan & Carpenter, 2023).
- **Video or lecture is about to play** — Especially valuable for passive media, where attention
  drift is the default failure mode. Carpenter & Toftness (2017) showed prequestions improve
  memory for directly questioned video content; subsequent work ties part of the mechanism to
  reduced mind-wandering during the presentation.
- **Reading assignment is about to open** — Inserting prequestions before expository text is
  the best-replicated context. Richland et al. (2009) and Pan & Sana (2021) both used
  expository passages and found robust benefits at 5-minute and 48-hour retention intervals.
- **Pre-assessment check-in needed and a study window follows** — When the tutor wants both
  diagnostic information and a learning lift, a pretest delivers both: incorrect responses
  surface specific gaps, and the attempt improves memory once the answers are studied. The
  study window must be present — without it, this collapses to a cold quiz.
- **Errors are cheap and feedback is immediate** — Pretesting requires that incorrect attempts
  be corrected within the same session. If the architecture supports immediate canonical
  answer reveal, the conditions for the effect are in place.

## When NOT to apply

- **No follow-up study window will occur in the same session** — The pretesting effect requires
  the learner to encounter the correct content shortly after the failed retrieval attempt. A
  pretest with no subsequent study is an uninformed quiz; the meta-analytic benefit (St.
  Hilaire et al., 2024) is conditional on the post-pretest study phase taking place.
- **Goal is transfer to untested content rather than retention of tested content** — Latimier
  et al. (2019) showed pretesting did not promote transfer to previously untested items, while
  posttesting did. If the criterion task involves novel application, use posttest retrieval
  practice (see [testing-effect](../01-learning-science/testing-effect.md)) instead.
- **Material is high element-interactivity and the learner is at first exposure** — As with
  retrieval practice generally, demanding generation before any schema exists wastes cognitive
  load on guessing rather than encoding. Use worked examples first (see
  [worked-example-effect](../01-learning-science/worked-example-effect.md)), then introduce
  pretesting once partial schema is in place.
- **Learner is already overwhelmed or below working-memory capacity for the segment** —
  Forcing an additional generation step on a saturated learner adds extraneous load (see
  [cognitive-load-theory](../01-learning-science/cognitive-load-theory.md)) without buying
  encoding benefit. Reduce extraneous load before adding pretesting.
- **The "prequestion" is really just a topic preview disguised as a question** — Yes/no
  recognition prompts ("Do you know what an altimeter is?") do not invoke errorful generation.
  Commit to a generative cued-recall attempt or use a different pre-segment move.

## How to apply

- **Write 2–4 short-answer or specific cued-recall prequestions per segment** — Multiple-choice
  and cued recall both work (Pan & Sana, 2021), but the prompt must require commitment to a
  specific answer. Open-ended "what do you think this is about?" framing is too diffuse; the
  prequestion must point at a specific fact or concept the upcoming segment will state.
- **Reveal canonical answers within the same session, ideally within minutes** — The follow-up
  study phase is what converts the unsuccessful attempt into encoding. Pan & Carpenter (2023)
  emphasize the post-pretest study opportunity is non-negotiable; without it, the benefit
  collapses.
- **Tell the learner errors are expected** — Frame the pretest explicitly: "Most of these you
  won't know — that's the point. Take your best shot, then watch how the answer lands."
  Kornell, Hays, & Bjork (2009) showed the benefit holds when the learner cannot possibly
  know the answer; framing removes fear of being "wrong" and prevents skipping.
- **Target the prequestion at the specific content you most need retained** — Because the
  effect is overwhelmingly specific (St. Hilaire et al., 2024; Pan & Carpenter, 2023),
  prequestions are a precision instrument. Spend the pretest on the 3–4 highest-stakes facts
  in the upcoming segment, not on incidental details.
- **Pair pretesting with posttest retrieval rather than substituting for it** — Pretesting
  strengthens encoding of the specific items; posttest retrieval (see
  [testing-effect](../01-learning-science/testing-effect.md)) consolidates retention and
  supports transfer. Latimier et al. (2019) is explicit the two operations are complementary;
  the strongest delivery pattern uses both.
- **Use the prequestion responses as live diagnostic data** — Items answered correctly need
  less subsequent study time; items missed signal where to expand the explanation. The
  diagnostic value is a free byproduct of the learning intervention.

## Common misapplications

- **Skipping the post-pretest study phase** — The single most damaging error. A pretest with
  no answer reveal is a cold assessment, and St. Hilaire et al. (2024) frame the post-attempt
  encoding episode as the operative mechanism without which the effect does not occur.
- **Treating the pretest as if it produces the same gains as a posttest** — It does not.
  Latimier et al. (2019) showed posttesting produced both larger retention effects (d = 0.74
  vs. 0.35) and the only reliable transfer to untested items. Pretesting is additive to
  posttesting, not a substitute.
- **Expecting general benefits to non-pretested material** — A persistent misapplication. The
  g ≈ 0.04 general effect (St. Hilaire et al., 2024) is functionally zero. Pretesting helps
  the items in the prequestion stem; rolling it out broadly on the assumption that the rest
  of the segment also gets a lift wastes time.
- **Conflating prequestions with retrieval practice** — Pretesting precedes encoding;
  retrieval practice follows it. Confusing the two leads to misattributed evidence and
  incorrect dosing. See [testing-effect](../01-learning-science/testing-effect.md) for the
  post-encoding operation.
- **Using pretesting as a performance test for grading** — The literature studies pretesting
  as a learning intervention with low-stakes attempts; using it as a graded diagnostic raises
  learner anxiety, suppresses guessing, and undoes the errorful-generation mechanism that
  drives the benefit (Kornell, Hays, & Bjork, 2009).

## Examples across domains

**Avionics — initial training on TCAS II resolution-advisory logic.**

*Setup.* A technician is about to watch a 12-minute reference video on the TCAS II
resolution-advisory (RA) decision logic — sense selection, vertical-rate envelopes,
coordination between two TCAS-equipped aircraft, and the inhibit conditions below 1000 ft
AGL. They have seen TCAS only as an end-user installer and have no working model of the
internal decision tree.

*Pretest prompt.* Before the video plays, the tutor asks four short prequestions whose
answers all appear explicitly in the video: (1) "When two TCAS units coordinate an
encounter, what determines which aircraft climbs and which descends?"; (2) "Below what
AGL altitude is a Descend RA inhibited?"; (3) "What does TCAS do when it cannot resolve
coordination — what category of RA does it issue?"; (4) "What is the maximum vertical
rate change a Corrective RA will demand?" The technician guesses on three and partially
answers one — the errorful-generation pattern Kornell, Hays, & Bjork (2009) studied.

*Follow-up.* Each pretest item appears in the video; when its answer surfaces, the tutor
pauses 3 seconds and overlays the pretested question with the canonical answer
side-by-side so the encoding moment lands against the failed attempt. After the video, a
posttest retrieval pass on the same four items plus two transfer items closes the loop.
The pretest contributes the Carpenter & Toftness (2017) specific-content lift on those
four facts; the posttest covers the transfer condition where Latimier et al. (2019) showed
pretesting alone is insufficient.

**Genealogy research — first encounter with an 1880–1900 federal census reading workflow.**

*Setup.* A researcher new to U.S. federal census records is about to read a 20-minute
reference document on the 1880, 1890, and 1900 enumerations: the columns each year added
(mother tongue, naturalization status, year of immigration), the 1890 fragmentary-survival
problem, and the Soundex coverage rules. They have used Ancestry.com casually but never
worked the columns directly; the document is dense with year-specific exceptions easy to
confuse in actual research.

*Pretest prompt.* The tutor poses three prequestions whose answers appear verbatim in
the document: (1) "Which census year first asked respondents how many years they had been
in the United States?"; (2) "Approximately what percentage of the 1890 federal census
population schedules survives today, and why?"; (3) "Which census years are included in
the standard published Soundex indexes for genealogical research?" The researcher commits
a guess on each — typical guesses are "1900," "50%," and "all of them," none exactly correct.

*Follow-up.* The document is opened, and the tutor highlights each answer in place ("1900
census added the year of immigration"; "less than 1% of 1890 population schedules survived
the 1921 Commerce Department fire"; "Soundex covers 1880, 1900, 1910, and partial 1920
only"). Each highlight is paired with the researcher's prior guess so the correction lands
against the wrong answer rather than over a blank slate — the Richland, Kornell, & Kao
(2009) errorful-generation pattern. A posttest at session end and a spaced revisit at +24
hours (see [spaced-retrieval](../01-learning-science/spaced-retrieval.md)) handle the
transfer-to-novel-items case the prequestion alone does not cover.

## Quality signal

Pretesting is producing learning when, on a delayed test (≥24 hours later), accuracy on directly pretested items exceeds accuracy on matched non-pretested items from the same study session by Hedges' g > 0.4 — within the band the St. Hilaire et al. (2024) and Pan & Carpenter (2023) meta-analyses predict for the specific effect. A faster in-session signal: on a posttest immediately after the study segment, accuracy on pretested items should exceed accuracy on equivalent non-pretested items by at least 10–15 percentage points; smaller gaps suggest the prequestions were too vague (recognition rather than specific cued recall) or the post-pretest study phase did not adequately surface the canonical answers.

## Cross-references

- See [testing-effect](../01-learning-science/testing-effect.md) for the post-encoding retrieval operation that is complementary to pretesting and dominates it on transfer measures.
- See [predict-before-reveal](../04-delivery-patterns/predict-before-reveal.md) for the runtime delivery pattern that operationalizes pretesting at the start of segments.
- See [cognitive-load-theory](../01-learning-science/cognitive-load-theory.md) for the load constraints that determine when pretesting helps versus harms encoding.
- See [worked-example-effect](../01-learning-science/worked-example-effect.md) for the alternative front-of-segment move when material is high element-interactivity and the learner has no schema yet.
- See [desirable-difficulties](../01-learning-science/desirable-difficulties.md) for the broader framework under which errorful generation is one productive difficulty.
- See [error-analysis-corrective-feedback](../04-delivery-patterns/error-analysis-corrective-feedback.md) for how to handle the wrong answers a pretest reliably produces.
