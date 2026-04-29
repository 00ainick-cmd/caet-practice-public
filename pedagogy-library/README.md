# AI Tutor Pedagogy Library (Library A)

## Mission

This library is the universal pedagogy reference an AI tutor consults at runtime to decide HOW to teach any subject — avionics, basketball, mortgages, K-12 math, genealogy, or anything else. It captures the durable, replicated findings of learning science, instructional design, assessment, and motivational psychology in operational form so a tutoring agent can pick the right move at the right moment without re-deriving pedagogy from first principles. It is consumed alongside per-domain "Domain Packs" (Library B) — the domain pack supplies WHAT to teach (concepts, skills, misconceptions, worked examples), and this library supplies HOW to teach it. Together the two libraries form the defensibility argument for every instructional choice the tutor makes: when a learner asks "why are you doing it this way?" the tutor can cite a chapter here and a peer-reviewed paper behind it.

## Schema

Every chapter conforms to the schema defined in `_schema/chapter-schema.yaml` (to be added). The schema enforces YAML frontmatter (id, evidence_strength, effect_size, key_sources, runtime_triggers, contraindicated_when) and a fixed nine-section body so the runtime can reliably parse any chapter and surface its operational guidance.

## Full 50-principle index

Slug column gives the canonical filename for each chapter (lowercase-kebab; cross-references in chapter frontmatter `related` and Section 9 links MUST use these exact slugs). File path is `<category>/<slug>.md`.

### Category 01 — Learning Science (13 chapters)

| # | Principle | Slug | Foundational sources | Effect size |
|---|-----------|------|----------------------|-------------|
| 1 | Testing Effect / Retrieval Practice | testing-effect | Roediger & Karpicke (2006); Adesope et al. (2017) | d ≈ 0.5–0.8 |
| 2 | Spaced Retrieval / Distributed Practice | spaced-retrieval | Cepeda et al. (2006) | d ≈ 0.4–0.6 |
| 3 | Interleaving | interleaving | Rohrer & Taylor (2007); Brunmair & Richter (2019) | d ≈ 0.4–0.7 |
| 4 | Worked Example Effect | worked-example-effect | Sweller & Cooper (1985); Renkl (2014) | d ≈ 0.5–1.0 |
| 5 | Expertise Reversal Effect | expertise-reversal | Kalyuga et al. (2003) | reversal at ~70% mastery |
| 6 | Cognitive Load Theory | cognitive-load-theory | Sweller (1988); Sweller, Ayres & Kalyuga (2011) | — |
| 7 | Pretesting Effect | pretesting-effect | Carpenter & Toftness (2017); Pan & Sana (2021) | d ≈ 0.3–0.5 |
| 8 | Desirable Difficulties | desirable-difficulties | Bjork & Bjork (2011) | — |
| 9 | Forgetting Curve & Relearning | forgetting-curve | Ebbinghaus (1885); Murre & Dros (2015) | — |
| 10 | Dual Coding | dual-coding | Paivio (1991); Mayer (2014) | d ≈ 0.3–0.5 |
| 11 | Self-Explanation & Elaborative Interrogation | self-explanation-elaborative-interrogation | Chi et al. (1994); Dunlosky et al. (2013) | d ≈ 0.4–0.6 |
| 12 | Schema Theory & Knowledge Components | schema-theory-knowledge-components | Anderson (1977); Koedinger et al. (2012) | — |
| 13 | Transfer of Learning | transfer-of-learning | Barnett & Ceci (2002) | — |

### Category 02 — Instructional Design (7 chapters)

| # | Principle | Slug | Foundational sources | Effect size |
|---|-----------|------|----------------------|-------------|
| 14 | Backward Design (UbD) | backward-design-ubd | Wiggins & McTighe (2005) | — |
| 15 | Bloom's Revised Taxonomy | blooms-revised-taxonomy | Anderson & Krathwohl (2001) | — |
| 16 | Merrill's First Principles | merrills-first-principles | Merrill (2002, 2013) | — |
| 17 | Gagné's Nine Events | gagnes-nine-events | Gagné, Briggs & Wager (1992) | — |
| 18 | 5E Learning Cycle | 5e-learning-cycle | Bybee et al. (2006); BSCS (1989) | — |
| 19 | Mastery Learning | mastery-learning | Bloom (1968); Guskey (2010) | d ≈ 0.5 |
| 20 | 4C/ID Model | 4c-id-model | van Merriënboer & Kirschner (2018) | — |

### Category 03 — Assessment Science (6 chapters)

| # | Principle | Slug | Foundational sources | Effect size |
|---|-----------|------|----------------------|-------------|
| 21 | Item-Writing Rules (Haladyna + Shank) | item-writing-rules | Haladyna et al. (2002); Shank (2014, 2017) | — |
| 22 | Bloom Levels in Assessment | bloom-levels-in-assessment | Krathwohl (2002) | — |
| 23 | Distractor Analysis | distractor-analysis | Haladyna & Rodriguez (2013) | — |
| 24 | Pre/Post Assessment & Effect Size | pre-post-assessment-effect-size | Hattie (2009); Cohen (1988) | — |
| 25 | Validity & Reliability | validity-reliability | Cronbach (1951); Messick (1989) | — |
| 26 | Mastery Threshold & Transfer Test Design | mastery-threshold-transfer-test-design | Bloom (1968); Barnett & Ceci (2002) | — |

### Category 04 — Delivery Patterns (8 chapters)

| # | Principle | Slug | Foundational sources | Effect size |
|---|-----------|------|----------------------|-------------|
| 27 | Socratic Questioning | socratic-questioning | Paul & Elder (2007); Chi (2009) | — |
| 28 | Predict-Before-Reveal | predict-before-reveal | Carpenter & Toftness (2017) | — |
| 29 | Faded Worked Examples | faded-worked-examples | Renkl & Atkinson (2003) | — |
| 30 | Self-Explanation Prompts | self-explanation-prompts | Chi et al. (1994) | — |
| 31 | Concept Mapping | concept-mapping | Novak & Cañas (2008); Nesbit & Adesope (2006) | d ≈ 0.5 |
| 32 | Error Analysis & Corrective Feedback | error-analysis-corrective-feedback | Hattie & Timperley (2007) | d ≈ 0.7 |
| 33 | Analogical Bridging | analogical-bridging | Gentner (1983); Holyoak (2012) | — |
| 34 | Productive Failure | productive-failure | Kapur (2008, 2014) | — |

### Category 05 — Tutor Personas (4 chapters)

| # | Principle | Slug | Foundational sources | Effect size |
|---|-----------|------|----------------------|-------------|
| 35 | Cognitive Apprenticeship Mentor | cognitive-apprenticeship-mentor | Collins, Brown & Newman (1989) | — |
| 36 | Socratic Interlocutor | socratic-interlocutor | Paul & Elder (2007) | — |
| 37 | Coach-Encourager | coach-encourager | Hattie & Timperley (2007); Kluger & DeNisi (1996) | — |
| 38 | Voice Style Guide & Agency-Preserving Language | voice-style-agency-preserving-language | Reeves & Nass (1996) | — |

### Category 06 — Motivation & Engagement (5 chapters)

| # | Principle | Slug | Foundational sources | Effect size |
|---|-----------|------|----------------------|-------------|
| 39 | Self-Determination Theory | self-determination-theory | Deci & Ryan (2000) | — |
| 40 | Self-Efficacy | self-efficacy | Bandura (1977, 1997) | — |
| 41 | Goal-Setting Theory | goal-setting-theory | Locke & Latham (2002) | — |
| 42 | Flow Theory | flow-theory | Csikszentmihalyi (1990); Nakamura & Csikszentmihalyi (2014) | — |
| 43 | Achievement Goal Theory | achievement-goal-theory | Ames (1992); Senko & Hulleman (2013) | — |

### Category 07 — Runtime Decisions (7 chapters)

| # | Principle | Slug | Foundational sources | Effect size |
|---|-----------|------|----------------------|-------------|
| 44 | Bayesian Knowledge Tracing | bayesian-knowledge-tracing | Corbett & Anderson (1995) | — |
| 45 | Performance Factor Analysis | performance-factor-analysis | Pavlik, Cen & Koedinger (2009) | — |
| 46 | SM-2 / FSRS | sm2-fsrs | Wozniak (1990); FSRS (2022) | — |
| 47 | Knowledge Graph Traversal | knowledge-graph-traversal | Koedinger et al. (2012) | — |
| 48 | ZPD Operationalization | zpd-operationalization | Vygotsky (1978) | — |
| 49 | Mastery Thresholds | mastery-thresholds | Bloom (1968) | — |
| 50 | Item Difficulty & Discrimination | item-difficulty-discrimination | Lord (1980); Embretson & Reise (2000) | — |

## Deliberately excluded (with reasons)

The following frameworks are intentionally absent. They are popular in education circles but fail the library's evidence bar.

- **Learning styles (VAK, auditory/visual/kinesthetic, etc.)** — Disconfirmed by Pashler, McDaniel, Rohrer & Bjork (2008). No evidence that matching instruction to a learner's claimed "style" improves outcomes.
- **Multiple Intelligences (Gardner)** — Theoretically influential but lacks the empirical foundation required for runtime decision-making. No replicable effect size on instructional design.
- **Brain-based learning** — Mostly recycled neuromyths (left-brain/right-brain, 10% of brain, "critical periods" misapplications). The reproducible parts are already covered by cognitive load theory and dual coding.
- **Growth Mindset** — Excluded under the "skip contested" filter. Foundational claims (Dweck) generated large effects in the original studies; classroom intervention effects shrank substantially in Sisk et al. (2018) meta-analysis. Promising direction but not yet stable enough to operationalize for an AI tutor.
- **Bloom's 2-Sigma** — The specific 2σ tutoring claim has not replicated under modern conditions. The mastery learning concept survives in chapter #19, which uses the more conservative Guskey (2010) effect estimates.
- **10,000-Hour Rule** — A popular misrepresentation of Ericsson's deliberate practice research. Deliberate practice itself is sound, but the round-number rule is a pop-science distortion.
- **Universal Design for Learning (UDL)** — Strong philosophy and useful design heuristic but mixed empirical evidence on whether the framework itself (vs. its individual components) produces measurable learning gains.
- **Specific gamification claims** — Effect sizes too variable across studies and contexts to support a runtime principle. Where game elements work, the underlying mechanism is already captured (feedback, goal-setting, self-efficacy).

## Schema conventions

Tag values in `contraindicated_when` (and any other state-predicate fields the schema later adds) use the form `category.predicate` — a lowercase category prefix, a dot, and a lowercase snake_case predicate. The categories define the dimension being asserted; the predicate is the specific state on that dimension. This makes the tags queryable by category and keeps colloquial phrasing out of the controlled vocabulary.

Current category prefixes:

- `learner_state.*` — properties of the learner at the moment the principle would be applied (e.g., `learner_state.overwhelmed`, `learner_state.first_exposure`).
- `material.*` — properties of the content being learned (e.g., `material.high_element_interactivity_no_scaffolding`).
- `task_type.*` — properties of the learning activity itself (e.g., `task_type.motor_acquisition`).

Add a new category prefix only when an existing one is genuinely the wrong dimension; do not introduce synonyms. `runtime_triggers` and `applies_to` use simpler forms (event-name underscore strings and phase labels respectively) because they are not state predicates.

## Authoring discipline

Every chapter cites peer-reviewed sources only. Every citation is verified — author, year, journal, page range, and DOI all checked against the published abstract before commit, and the cited claim must match what the abstract actually says. Contested or weakly replicated principles are excluded rather than included with caveats. Target length is 120–200 lines per chapter — this is a runtime reference, not a textbook chapter, so prose is reserved for the evidence base and operational sections lean on bullets. When a finding has a known boundary condition, the chapter states it explicitly in section 4 ("When NOT to apply") rather than burying it.
