# Cross-Domain Expert AI Tutor — Pedagogy Library (Library A) Design

**Status:** Approved by user 2026-04-29. Ready for implementation planning.
**Author:** Brainstormed with user, written by Claude.
**Scope:** Library A only (the universal pedagogy reference). Library B (Domain Packs) and the runtime engine that consumes both libraries are out of scope for this design.

---

## 1. Goal

Build a domain-agnostic, evidence-based pedagogy reference library that an AI tutor consults at runtime to **decide how to teach** any subject — avionics, basketball, mortgages, genealogy, anything.

The library is the *brain* of the tutor. The tutor's craft and defensibility come from this library. When a customer asks "why does your AI tutor work?", you point at this library and its citations.

## 2. Architectural decision: two libraries with an adaptation layer

The full AI tutor framework has three knowledge bases, in priority order:

| Library | What | Authored by | Update cadence |
|---------|------|-------------|----------------|
| **A. Pedagogy Reference** *(this design)* | Universal evidence-based teaching principles | Curriculum/learning-science team | Yearly |
| **B. Domain Pack** *(separate design)* | Subject-specific concepts, scenarios, assessments | SME for that domain | Constantly (new ADs, new products, etc.) |
| **C. Domain Pedagogy Adaptations** *(small layer)* | Domain-specific overrides where pedagogy needs subject context | Domain SME + curriculum reviewer | As needed |

This separation is justified by:
- **Reuse:** Library A is consulted by every domain (avionics, basketball, mortgages share it 100%).
- **Authorship rates:** A updates yearly; B updates constantly; mixing them invites pedagogy decay over time.
- **Defensibility:** A claims must be defended with peer-reviewed citations; B claims must be defended with SME and source documents — different review workflows.
- **Runtime queries:** "How should I teach this?" (queries A) vs "What concept comes next?" (queries B) are different shapes; co-locating them adds filtering overhead at every query.

## 3. File schema for Library A

Every file in Library A follows the same structure. Consistency is what lets the AI query 50 files the same way.

### 3.1 YAML frontmatter (machine-readable)

```yaml
---
id: testing-effect                          # stable, lowercase-kebab
title: Testing Effect (Retrieval Practice)
category: 01-learning-science               # one of the 7 categories
aliases: [retrieval-practice, recall-practice]
evidence_strength: strong                   # strong | moderate (we filter to strong only)
effect_size: "Cohen's d ≈ 0.5–0.8"           # quantified where possible; null otherwise
key_sources:
  - "Roediger & Karpicke (2006). The power of testing memory. Perspectives on Psychological Science, 1(3), 181–210."
  - "Adesope, Trevisan & Sundararajan (2017). Rethinking the use of tests: a meta-analysis. Review of Educational Research, 87(3), 659–701."
last_reviewed: 2026-04-29
applies_to: [acquisition, retention, transfer]
contraindicated_when: [learner_overwhelmed, brand_new_concept_first_exposure]
runtime_triggers:                           # session events that should invoke this principle
  - new_concept_completed
  - segment_boundary
  - delayed_review_window_open
related: [spaced-retrieval, generative-learning, desirable-difficulties]
---
```

### 3.2 Required body sections

In order, each chapter contains:

1. **One-line claim** — single-sentence operational summary
2. **Evidence base** — multiple paragraphs covering foundational study, modern meta-analysis, effect size range, replication status, contested boundary conditions
3. **When to apply** — concrete decision rules mapped to the `runtime_triggers` frontmatter
4. **When NOT to apply** — boundary conditions and contraindications
5. **How to apply (delivery patterns)** — concrete moves; cross-references to category 04 files
6. **Common misapplications** — how tutors and AI systems get this wrong
7. **Examples across domains** — three concrete examples (avionics + basketball + mortgage) to test cross-domain generality
8. **Quality signal** — how the AI knows the principle is producing learning; what would invalidate
9. **Cross-references** — links to related Library A files

### 3.3 Depth target

**Full chapter depth (8–15 pages each).** Comprehensive academic-grade reference material:
- 5–10 peer-reviewed citations per file with DOIs
- Effect sizes from meta-analyses (Cohen's d or equivalent)
- Theoretical mechanisms explained (cognitive process accounts)
- Multiple replication notes; mention contested camps where relevant
- Multi-domain examples in every file (forces principle author to test cross-domain generality)

Aggregate scope: ~50 files × ~12 pages = 500–750 pages of authored content.

## 4. The 50-principle index

Approved 2026-04-29 with the user. Filtered for **strict evidence** (peer-reviewed sources, meta-analyses preferred); contested principles excluded.

### Category 01 — Learning Science (13 principles)

1. Testing Effect / Retrieval Practice
2. Spaced Retrieval / Distributed Practice
3. Interleaving
4. Worked Example Effect
5. Expertise Reversal Effect
6. Cognitive Load Theory
7. Pretesting Effect
8. Desirable Difficulties (Bjork)
9. Forgetting Curve & Relearning
10. Dual Coding (Paivio, Mayer)
11. Self-Explanation & Elaborative Interrogation
12. Schema Theory & Knowledge Components
13. Transfer of Learning

### Category 02 — Instructional Design (7 principles)

14. Backward Design (Wiggins & McTighe)
15. Bloom's Revised Taxonomy
16. Merrill's First Principles of Instruction
17. Gagné's Nine Events of Instruction
18. 5E Learning Cycle
19. Mastery Learning
20. 4C/ID Model

### Category 03 — Assessment Science (6 principles)

21. Item-Writing Rules (Haladyna + Shank)
22. Bloom Levels in Assessment
23. Distractor Analysis
24. Pre/Post Assessment & Effect Size
25. Validity & Reliability
26. Mastery Threshold & Transfer Test Design

### Category 04 — Delivery Patterns (8 principles)

27. Socratic Questioning
28. Predict-Before-Reveal
29. Faded Worked Examples
30. Self-Explanation Prompts
31. Concept Mapping
32. Error Analysis & Corrective Feedback
33. Analogical Bridging
34. Productive Failure (Kapur)

### Category 05 — Tutor Personas (4 principles)

35. Cognitive Apprenticeship Mentor
36. Socratic Interlocutor
37. Coach-Encourager
38. Voice Style Guide & Agency-Preserving Language

### Category 06 — Motivation & Engagement (5 principles)

39. Self-Determination Theory (Deci & Ryan)
40. Self-Efficacy (Bandura)
41. Goal-Setting Theory (Locke & Latham)
42. Flow Theory (Csikszentmihalyi)
43. Achievement Goal Theory

### Category 07 — Runtime Decisions / Adaptive Algorithms (7 principles)

44. Bayesian Knowledge Tracing (BKT)
45. Performance Factor Analysis (PFA)
46. SM-2 / FSRS Spaced Repetition Algorithms
47. Knowledge Graph Traversal & Prerequisite Ordering
48. Zone of Proximal Development Operationalization
49. Mastery Thresholds in Adaptive Systems
50. Item Difficulty & Discrimination (CTT/IRT)

### Deliberately excluded

| Excluded | Reason |
|---|---|
| Learning styles (VAK, etc.) | Disconfirmed by Pashler et al. (2008) |
| Multiple Intelligences (Gardner) | Weak empirical foundation for independent intelligences |
| Brain-based learning | Mostly neuromyths; doesn't replicate |
| Growth Mindset | Core construct survives but classroom-intervention effects have shrunk in Sisk et al. (2018) — per user's "skip contested" filter |
| Bloom's 2-Sigma claim | Specific 2σ claim hasn't replicated; mastery-learning concept survives in #19 |
| 10,000-Hour Rule | Popular misrepresentation of Ericsson's deliberate-practice research |
| Universal Design for Learning (UDL) | Strong philosophy; mixed empirical evidence for specific component claims |
| Specific gamification claims | Effect sizes too variable; not strong-evidence enough |

## 5. Development approach (5-phase)

```
Phase 1 — INDEX           ✓ Complete (this doc).

Phase 2 — EXEMPLAR        Author one gold-standard chapter end-to-end at full
                          depth. testing-effect.md (~12 pages). Sets the
                          quality bar for everything else.
                          → User reviews and signs off before scaling.

Phase 3 — SPEC            Distill the exemplar into:
                            (a) Schema spec (machine-readable + frontmatter rules)
                            (b) Quality checklist (what makes a chapter "good")
                            (c) Citation discipline rules (no fabrication, real DOIs)
                            (d) Authoring brief for parallel agents

Phase 4 — PARALLEL        Dispatch ~50 sub-agents (one per principle), each
                          given the exemplar, the spec, the principle name,
                          and citation rules. Concurrent authoring.

Phase 5 — VERIFICATION    Three review passes:
                            (a) Citation pass — verify every reference against
                                published literature via web search.
                            (b) Consistency pass — cross-file claims don't
                                contradict.
                            (c) Gap pass — user spot-checks coverage.
```

## 6. Quality criteria

A Library A file is "good" when:

- **Citations:** ≥ 5 peer-reviewed sources with full reference; meta-analyses preferred for effect-size claims; DOIs included where applicable.
- **No fabrication:** Every cited paper actually exists, has the cited authors, and supports the cited claim. (Phase 5 verification pass enforces.)
- **Effect size quantified** where the literature provides one (Cohen's d, Hedges' g, or odds ratios). Frontmatter `effect_size` field non-null unless the principle is foundational/qualitative.
- **Operational sections** ("when to apply" / "when not" / "how to apply") give the AI executable decision rules, not platitudes.
- **Cross-domain examples** present in every file — at minimum avionics + one non-avionics. This forces the author to test that the principle generalizes.
- **Boundary conditions stated** — every chapter explicitly identifies when the principle fails or reverses.
- **Frontmatter complete** — every required field populated; runtime_triggers and related fields use canonical IDs that match other files.

## 7. File layout

```
pedagogy-library/
├── README.md                                # library overview, schema reference
├── _schema/
│   ├── chapter-schema.yaml                  # JSON schema for frontmatter
│   ├── quality-checklist.md                 # the gating criteria
│   └── citation-rules.md                    # what counts as a real citation
├── 01-learning-science/
│   ├── testing-effect.md
│   ├── spaced-retrieval.md
│   └── ... (13 files)
├── 02-instructional-design/
│   └── ... (7 files)
├── 03-assessment-science/
│   └── ... (6 files)
├── 04-delivery-patterns/
│   └── ... (8 files)
├── 05-tutor-personas/
│   └── ... (4 files)
├── 06-motivation-engagement/
│   └── ... (5 files)
└── 07-runtime-decisions/
    └── ... (7 files)
```

Total: 50 chapter files + 3 schema files + 1 README.

## 8. Out of scope (not designed here)

- **Library B canonical schema** for Domain Packs. Avionics Library B exists *in spirit* in `tools/training_pipeline/enrichment/*.json` but needs refactor. Separate design.
- **The runtime engine** that queries Library A + B and decides next moves during a session. Separate design.
- **Library C (domain adaptations)** for cases where pedagogy needs domain-specific tuning. Will emerge organically; design when needed.
- **Web/UI/CLI for the tutor.** Separate design.
- **Annual review process** for Library A maintenance. To be defined after the library exists.
- **SME peer-review pass** of each chapter by a real learning scientist. Optional follow-on commission.

## 9. Implementation handoff

This design is approved. Next step: invoke `superpowers:writing-plans` to convert into a detailed task-by-task implementation plan starting with Phase 2 (the exemplar).
