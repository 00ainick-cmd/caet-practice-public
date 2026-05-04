---
id: item-writing-rules
title: Item-Writing Rules (Haladyna + Shank)
category: 03-assessment-science
aliases: [mcq-item-writing-rules, multiple-choice-item-writing, haladyna-rules]
evidence_strength: strong
# effect_size is null because item-writing rules are an operational construction
# discipline. Quantitative anchors are reported inline: Rodriguez (2005) showed
# 3-option items match 4/5-option items psychometrically; Downing (2005) and
# Tarrant & Ware (2008) found 36-75% of items in unaudited high-stakes banks
# are flawed and shift pass rates by 4-10 percentage points.
effect_size: null
key_sources:
  - "Haladyna, T. M., Downing, S. M., & Rodriguez, M. C. (2002). A review of multiple-choice item-writing guidelines for classroom assessment. *Applied Measurement in Education*, 15(3), 309-333. doi:10.1207/S15324818AME1503_5"
  - "Rodriguez, M. C. (2005). Three options are optimal for multiple-choice items: A meta-analysis of 80 years of research. *Educational Measurement: Issues and Practice*, 24(2), 3-13. doi:10.1111/j.1745-3992.2005.00006.x"
  - "Downing, S. M. (2005). The effects of violating standard item writing principles on tests and students: The consequences of using flawed test items on achievement examinations in medical education. *Advances in Health Sciences Education*, 10(2), 133-143. doi:10.1007/s10459-004-4019-5"
  - "Tarrant, M., & Ware, J. (2008). Impact of item-writing flaws in multiple-choice questions on student achievement in high-stakes nursing assessments. *Medical Education*, 42(2), 198-206. doi:10.1111/j.1365-2923.2007.02957.x"
  - "Frey, B. B., Petersen, S. W., Edwards, L. M., Pedrotti, J. T., & Peyton, V. (2005). Item-writing rules: Collective wisdom. *Teaching and Teacher Education*, 21(4), 357-364. doi:10.1016/j.tate.2005.01.008"
  - "Haladyna, T. M., & Rodriguez, M. C. (2013). *Developing and validating test items*. New York, NY: Routledge. doi:10.4324/9780203850381"
  - "Shank, P. (2021). *Write better multiple-choice questions to assess learning: Measure what matters — Evidence-informed tactics for multiple-choice questions*. Centennial, CO: Learning Peaks LLC. ISBN:9798453383993"
last_reviewed: 2026-04-29
applies_to: [measurement]
contraindicated_when:
  - task_type.motor_acquisition
  - material.uncalibrated_item_pool
  - learner_state.first_exposure
runtime_triggers:
  - mcq_item_drafted
  - item_bank_review_due
  - sme_question_intake
  - distractor_revision_pending
  - certification_blueprint_locked
related: [distractor-analysis, bloom-levels-in-assessment, validity-reliability, mastery-threshold-transfer-test-design, pre-post-assessment-effect-size, item-difficulty-discrimination, testing-effect]
---

# Item-Writing Rules (Haladyna + Shank)

## One-line claim

Construct multiple-choice items that vary only on the construct being measured: a focused stem that poses one clear problem, a single defensible key, and 2–4 plausible distractors written in parallel form, with no surface cues, negation, or "all of the above" options that let savvy test-takers score above their true ability.

## Evidence base

Haladyna, Downing, and Rodriguez (2002) reviewed 27 educational measurement textbooks published since 1990 and 27 empirical studies of item construction, distilling the convergent guidance into a 31-rule taxonomy organized around four concerns: content, formatting, style, and writing the stem and options. The taxonomy is the canonical reference for classroom and credentialing item construction; rules with strong empirical and theoretical backing (single defensible key, plausible distractors, parallel option construction, avoidance of "all/none of the above," avoidance of negative stems, vertical option layout) appear in every modern handbook (Haladyna & Rodriguez, 2013, ch. 6-9). Frey, Petersen, Edwards, Pedrotti, and Peyton (2005) independently surveyed 20 classroom-assessment textbooks and identified 40 rules with cross-textbook consensus, including 30 that overlap with the Haladyna et al. (2002) taxonomy — the redundancy across two independent reviews is the strongest available evidence that the rules represent settled professional knowledge rather than one author's preference.

The empirical case for the rules rests on what happens when they are violated. Downing (2005) re-scored four high-stakes medical-school exams after partitioning each item bank into "flawed" (one or more rule violations) and "standard" (rule-compliant) items: 36% to 65% of items on the four tests were flawed, flawed items were 0–15 percentage points more difficult than standard items measuring the same construct, and pass rates differed materially — across 1,221 examinees, 53% passed on the standard items while 47% passed on the flawed items, implying as many as 10–15% of students were misclassified by the construct-irrelevant variance the flaws introduced (*Advances in Health Sciences Education*, 10(2), pp. 138-141). Tarrant and Ware (2008) replicated the design on 10 summative nursing-program exam papers in Hong Kong: 47.3% of items contained flaws (range 28–75%), and recomputing the pass/fail decision against only the unflawed standard scale dropped pass rates from 94.3% to 90.6% and roughly tripled the proportion of high-scoring examinees who fell below the score-of-80 threshold (*Medical Education*, 42(2), pp. 201-203). Both papers attribute the differential to construct-irrelevant variance: flawed items partially measure test-wiseness and surface-cue sensitivity rather than the construct the test claims to measure.

The strongest single quantitative claim in the rule set is Rodriguez's (2005) meta-analysis. Pooling 80 years of research comparing 3-, 4-, and 5-option items, Rodriguez found that three-option items produce equivalent or superior reliability and discrimination relative to four- or five-option items, allow more items per fixed testing time (improving content coverage), and reduce construction effort because writing a third plausible distractor is the rate-limiting step (*Educational Measurement: Issues and Practice*, 24(2), pp. 8-11). Shank (2021) translates the academic literature into operational practitioner guidance with explicit examples of compliant and non-compliant items in workplace-learning contexts; her central operational claim — write items that test recognition of meaningful distinctions a competent practitioner would draw, not memorization of textbook wording — recovers the construct-validity argument in language an SME without psychometric training can act on.

## When to apply

- **An MCQ item has just been drafted** — Run the new item through the rule checklist before it
  enters the bank; pre-publication review is roughly 10× cheaper than post-administration item
  retirement (Haladyna & Rodriguez, 2013, ch. 6).
- **Item bank review is due** — Audit existing items against the taxonomy on a scheduled cadence
  (e.g., before each major sitting or once per year). Downing (2005) and Tarrant & Ware (2008)
  found 36–75% of items in unaudited high-stakes banks contained at least one flaw.
- **SME question intake** — Subject-matter experts authoring without formal item-writing training
  produce the highest flaw rates (Tarrant & Ware, 2008, p. 200). Apply the rules as a
  structured intake/review form on every SME submission before items go live.
- **Distractor revision pending** — When [distractor-analysis](../03-assessment-science/distractor-analysis.md)
  flags non-functioning distractors (selected by <5% of examinees) or negative point-biserials,
  rewrite using the parallelism, plausibility, and length-equivalence rules below.
- **Certification blueprint is locked** — Once content blueprint and Bloom levels are fixed (see
  [bloom-levels-in-assessment](../03-assessment-science/bloom-levels-in-assessment.md)), apply
  the rules so each item measures the targeted level, not reading speed or test-wiseness. The
  cost of a flawed item amortizes across every administration and every misclassified examinee,
  so high-stakes and reused items justify the strictest rule application.

## When NOT to apply

- **Pure motor-skill or hands-on practical evaluation** — The rules govern selected-response
  items. Evaluate procedural performance with structured rubrics (see
  [mastery-threshold-transfer-test-design](../03-assessment-science/mastery-threshold-transfer-test-design.md)),
  not MCQs.
- **First-exposure formative recall during initial encoding** — When a tutor uses retrieval as
  encoding support, short-answer or open recall outperforms rule-perfect MCQs; the rules govern
  measurement-grade items, not encoding prompts ([testing-effect](../01-learning-science/testing-effect.md)).
- **Item pool is uncalibrated and too small for analysis** — Without calibration,
  difficulty/discrimination statistics cannot validate the items; rule application is necessary
  but not sufficient. Pair with item analysis as the bank scales
  ([item-difficulty-discrimination](../07-runtime-decisions/item-difficulty-discrimination.md)).
- **Format mandated by external standard differs from the rules** — Some authorities prescribe
  five mandatory options or negative stems for safety items. Comply with the external standard,
  document the deviation, and audit the resulting items more aggressively for empirical flaws.
- **Construct genuinely requires divergent thinking or production** — Multi-select, ranking,
  short-answer, or constructed-response measure constructs MCQs cannot. Pick the right format
  first; do not force an open construct into a closed one to apply this chapter.

## How to apply

- **Write the stem as a complete question or partial sentence that poses one problem** — the
  examinee should be able to attempt an answer before reading the options. Strip irrelevant
  context and embedded clues. If the stem alone does not communicate the question, rewrite
  (Haladyna et al., 2002, rules 7-12).
- **Use 3 or 4 options, 1 defensible key and 2–3 plausible distractors** — Rodriguez (2005)
  showed three-option items match four/five-option items in reliability and discrimination
  while permitting more items per fixed time. Add a fourth only when a fourth genuinely
  plausible distractor exists; do not pad with implausible filler.
- **Make distractors plausible from real misconceptions** — derive them from common errors,
  prerequisite confusions, or surface analogies the construct is meant to discriminate. An ideal
  distractor draws roughly equal selection from low-ability examinees and <50% from high-ability
  examinees ([distractor-analysis](../03-assessment-science/distractor-analysis.md)).
- **Keep options parallel in form, length, grammar, and specificity** — the longest option is
  correct ~60-70% of the time in untrained item writers (Haladyna & Rodriguez, 2013, ch. 8).
  Equalize length to within ±25% of the median so examinees choose on construct grounds.
- **Eliminate "all of the above," "none of the above," and negative stems where possible** —
  "all of the above" lets partial knowledge score correct; "none of the above" tests recognition
  of incorrectness; negative stems inflate reading load and breed flaws (Haladyna et al., 2002,
  rules 19-22). Where a negative stem is unavoidable, capitalize and bold the negation.
- **Run a flaw audit before items go live** — Apply the Haladyna et al. (2002) 31-rule or Frey
  et al. (2005) 40-rule checklist as a structured review form with two independent reviewers and
  a third on disagreement. Tarrant & Ware (2008, p. 200) audited 50-item exams in under three
  reviewer-hours.
- **Match the item to the targeted Bloom level** — Application/analysis items use a novel
  scenario; recognition items use textbook wording. A "what is the formula" stem cannot measure
  application regardless of distractor count
  ([bloom-levels-in-assessment](../03-assessment-science/bloom-levels-in-assessment.md)).

## Common misapplications

- **"Trick" distractors built from synonyms or fine grammar distinctions** — Distractors should
  represent substantive misconceptions, not require parsing subtle wording. Items whose flaw is
  "the examinee misread one word" measure reading attention, not the construct (Downing, 2005,
  on construct-irrelevant variance).
- **The longest option is correct** — Untrained authors over-elaborate the key. Equalize length
  to within ±25%; if the key needs qualifications, distribute matching length across distractors
  (Haladyna & Rodriguez, 2013, ch. 8).
- **Distractor recycled from the stem with one word swapped** — Negation flips and single-word
  transformations create surface-cue items that high-ability examinees solve by elimination
  without engaging the construct. Distractors should encode different misconceptions.
- **Embedded clue: stem contains a keyword that appears verbatim only in the key** — Lexical
  overlap leaks the answer. Rewrite the stem or the key so no surface match remains (Haladyna
  et al., 2002, rule 12).
- **"All of the above" used because the author could not write a fourth distractor** — The
  highest-frequency lazy-fallback flaw in Tarrant & Ware (2008, p. 202). Drop to a three-option
  item per Rodriguez (2005) instead.
- **Bank not audited because items came from the SME** — SME-authored items have higher flaw
  rates than psychometrician-reviewed items (Tarrant & Ware, 2008). Domain expertise is not
  expertise in item construction; audit applies equally.
- **Treating "more options = more rigorous"** — Five-option items neither raise reliability nor
  discrimination above three-option items but do increase cost and reading load (Rodriguez,
  2005). Rigor lives in construct match and distractor plausibility, not option count.

## Examples across domains

**Avionics — recertification MCQ for a Mode S transponder ramp-test procedure.**

*Setup.* The item bank for a CAET Mode S transponder recertification module has just received
12 SME-authored items covering IFR-6000 ramp-test interpretation. Two items are flagged in the
intake review; the rest get a structured Haladyna 31-rule audit before going live.

*Flaw and revision.* The flagged item reads: "Which of the following is NOT a Mode S reply
displayed during a normal Class A1 transponder ramp test? a) DF11 b) DF17 c) DF4 with altitude
squittering d) all of the above" — negative stem plus "all of the above." Revision: "During a
normal Class A1 transponder ramp test, which Mode S reply appears in the analyzer trace?" with
options "a) DF11 acquisition squitter b) DF17 extended squitter c) DF4 surveillance reply
d) DF20 Comm-A reply." The defensible key is DF4; the others occur in ADS-B Out or Comm-A test
modes, not Class A1.

*Audit outcome.* Across the 12 items, 5 had at least one flaw (42%, near the 47% rate Tarrant
& Ware 2008 documented in nursing). Three were rewritten to three-option items per Rodriguez
(2005). The next sitting's pass rate matched the prior reference-test pass rate within 1 point;
the prior bank's flaw-driven pass-rate inflation (~5 points) disappeared.

**Manufacturing quality control — ISO 9001 internal-auditor certification item bank review.**

*Setup.* A medical-device manufacturer's ISO 9001 internal-auditor certification uses a
200-item bank covering ISO 9001:2015 clauses, root-cause analysis, and CAPA documentation,
authored by quality-engineering SMEs over three years and never formally audited. A Frey et al.
(2005) 40-rule audit is commissioned before the next certification cycle.

*Flaw and revision.* Representative flawed item: "All of the following are required elements of
a CAPA report EXCEPT: a) root-cause statement b) corrective action plan c) verification of
effectiveness d) the auditor's personal opinion of the supplier" — negative stem and an
implausible distractor (d) that collapses the item to recognition. Revision: "After a CAPA
verification of effectiveness fails, the next required action under ISO 9001:2015 clause 10.2
is: a) reissue the corrective action with revised root-cause analysis b) close the CAPA and
document residual risk c) escalate to the supplier without further analysis d) defer
reverification to the next audit." Three plausible distractors from common auditor errors; key
is (a). Bloom level shifts from recognition to application of clause 10.2.

*Audit outcome.* Of 200 items, 89 (44.5%) had at least one rule violation — within Tarrant &
Ware's (2008) 28–75% range. After a 12-week two-reviewer revision sprint, 71 items were
rewritten and 18 retired. Mean point-biserial discrimination rose from 0.21 to 0.34 and items
below the 0.20 floor dropped from 38% to 9% — the construct-validity gain Downing (2005)
attributed to flaw removal in medical exams.

## Quality signal

A bank is rule-compliant when (a) two independent reviewers agree on rule conformity for ≥95% of items on a Haladyna et al. (2002) 31-rule audit, (b) item-analysis discrimination (point-biserial `r_pb`) ≥ 0.30 on at least 80% of administered items with `r_pb < 0.20` on no more than 5%, and (c) repeating the audit after recomputation against only the unflawed subset shifts pass rates by less than 2 percentage points (Downing 2005 and Tarrant & Ware 2008 found 4–10 point shifts on unaudited banks). Item-level signal during construction: option-length range across distractors and key within ±25% of the median, no negation in the stem, and three-option default unless a fourth genuinely plausible distractor exists.

## Cross-references

- See [distractor-analysis](../03-assessment-science/distractor-analysis.md) for the empirical diagnostics that confirm whether constructed distractors are functioning.
- See [bloom-levels-in-assessment](../03-assessment-science/bloom-levels-in-assessment.md) for matching item construction to the cognitive level the certification blueprint targets.
- See [validity-reliability](../03-assessment-science/validity-reliability.md) for the construct-irrelevant-variance framing the rules are designed to suppress.
- See [mastery-threshold-transfer-test-design](../03-assessment-science/mastery-threshold-transfer-test-design.md) for how rule-compliant items support defensible pass/fail decisions.
- See [item-difficulty-discrimination](../07-runtime-decisions/item-difficulty-discrimination.md) for the IRT parameters that depend on rule-compliant construction to be interpretable.
- See [testing-effect](../01-learning-science/testing-effect.md) for the encoding-time use of retrieval prompts, which is governed by different (lower) format rigor than measurement-grade items.
