# AI Tutor Pedagogy Library (Library A)

## Mission

This library is the universal pedagogy reference an AI tutor consults at runtime to decide HOW to teach any subject — avionics, basketball, mortgages, K-12 math, genealogy, or anything else. It captures the durable, replicated findings of learning science, instructional design, assessment, and motivational psychology in operational form so a tutoring agent can pick the right move at the right moment without re-deriving pedagogy from first principles. It is consumed alongside per-domain "Domain Packs" (Library B) — the domain pack supplies WHAT to teach (concepts, skills, misconceptions, worked examples), and this library supplies HOW to teach it. Together the two libraries form the defensibility argument for every instructional choice the tutor makes: when a learner asks "why are you doing it this way?" the tutor can cite a chapter here and a peer-reviewed paper behind it.

## Schema

Every chapter conforms to the schema defined in `_schema/chapter-schema.yaml` (to be added). The schema enforces YAML frontmatter (id, evidence_strength, effect_size, key_sources, runtime_triggers, contraindicated_when) and a fixed nine-section body so the runtime can reliably parse any chapter and surface its operational guidance.

## Full 50-principle index

### Category 01 — Learning Science (13 chapters)

| # | Principle | Foundational sources | Effect size |
|---|-----------|----------------------|-------------|
| 1 | Testing Effect / Retrieval Practice | Roediger & Karpicke (2006); Adesope et al. (2017) | d ≈ 0.5–0.8 |
| 2 | Spaced Retrieval / Distributed Practice | Cepeda et al. (2006) | d ≈ 0.4–0.6 |
| 3 | Interleaving | Rohrer & Taylor (2007); Brunmair & Richter (2019) | d ≈ 0.4–0.7 |
| 4 | Worked Example Effect | Sweller & Cooper (1985); Renkl (2014) | d ≈ 0.5–1.0 |
| 5 | Expertise Reversal Effect | Kalyuga et al. (2003) | reversal at ~70% mastery |
| 6 | Cognitive Load Theory | Sweller (1988); Sweller, Ayres & Kalyuga (2011) | — |
| 7 | Pretesting Effect | Carpenter & Toftness (2017); Pan & Sana (2021) | d ≈ 0.3–0.5 |
| 8 | Desirable Difficulties | Bjork & Bjork (2011) | — |
| 9 | Forgetting Curve & Relearning | Ebbinghaus (1885); Murre & Dros (2015) | — |
| 10 | Dual Coding | Paivio (1991); Mayer (2014) | d ≈ 0.3–0.5 |
| 11 | Self-Explanation & Elaborative Interrogation | Chi et al. (1994); Dunlosky et al. (2013) | d ≈ 0.4–0.6 |
| 12 | Schema Theory & Knowledge Components | Anderson (1977); Koedinger et al. (2012) | — |
| 13 | Transfer of Learning | Barnett & Ceci (2002) | — |

### Category 02 — Instructional Design (7 chapters)

| # | Principle | Foundational sources | Effect size |
|---|-----------|----------------------|-------------|
| 14 | Backward Design (UbD) | Wiggins & McTighe (2005) | — |
| 15 | Bloom's Revised Taxonomy | Anderson & Krathwohl (2001) | — |
| 16 | Merrill's First Principles | Merrill (2002, 2013) | — |
| 17 | Gagné's Nine Events | Gagné, Briggs & Wager (1992) | — |
| 18 | 5E Learning Cycle | Bybee et al. (2006); BSCS (1989) | — |
| 19 | Mastery Learning | Bloom (1968); Guskey (2010) | d ≈ 0.5 |
| 20 | 4C/ID Model | van Merriënboer & Kirschner (2018) | — |

### Category 03 — Assessment Science (6 chapters)

| # | Principle | Foundational sources | Effect size |
|---|-----------|----------------------|-------------|
| 21 | Item-Writing Rules (Haladyna + Shank) | Haladyna et al. (2002); Shank (2014, 2017) | — |
| 22 | Bloom Levels in Assessment | Krathwohl (2002) | — |
| 23 | Distractor Analysis | Haladyna & Rodriguez (2013) | — |
| 24 | Pre/Post Assessment & Effect Size | Hattie (2009); Cohen (1988) | — |
| 25 | Validity & Reliability | Cronbach (1951); Messick (1989) | — |
| 26 | Mastery Threshold & Transfer Test Design | Bloom (1968); Barnett & Ceci (2002) | — |

### Category 04 — Delivery Patterns (8 chapters)

| # | Principle | Foundational sources | Effect size |
|---|-----------|----------------------|-------------|
| 27 | Socratic Questioning | Paul & Elder (2007); Chi (2009) | — |
| 28 | Predict-Before-Reveal | Carpenter & Toftness (2017) | — |
| 29 | Faded Worked Examples | Renkl & Atkinson (2003) | — |
| 30 | Self-Explanation Prompts | Chi et al. (1994) | — |
| 31 | Concept Mapping | Novak & Cañas (2008); Nesbit & Adesope (2006) | d ≈ 0.5 |
| 32 | Error Analysis & Corrective Feedback | Hattie & Timperley (2007) | d ≈ 0.7 |
| 33 | Analogical Bridging | Gentner (1983); Holyoak (2012) | — |
| 34 | Productive Failure | Kapur (2008, 2014) | — |

### Category 05 — Tutor Personas (4 chapters)

| # | Principle | Foundational sources | Effect size |
|---|-----------|----------------------|-------------|
| 35 | Cognitive Apprenticeship Mentor | Collins, Brown & Newman (1989) | — |
| 36 | Socratic Interlocutor | Paul & Elder (2007) | — |
| 37 | Coach-Encourager | Hattie & Timperley (2007); Kluger & DeNisi (1996) | — |
| 38 | Voice Style Guide & Agency-Preserving Language | Reeves & Nass (1996) | — |

### Category 06 — Motivation & Engagement (5 chapters)

| # | Principle | Foundational sources | Effect size |
|---|-----------|----------------------|-------------|
| 39 | Self-Determination Theory | Deci & Ryan (2000) | — |
| 40 | Self-Efficacy | Bandura (1977, 1997) | — |
| 41 | Goal-Setting Theory | Locke & Latham (2002) | — |
| 42 | Flow Theory | Csikszentmihalyi (1990); Nakamura & Csikszentmihalyi (2014) | — |
| 43 | Achievement Goal Theory | Ames (1992); Senko & Hulleman (2013) | — |

### Category 07 — Runtime Decisions (7 chapters)

| # | Principle | Foundational sources | Effect size |
|---|-----------|----------------------|-------------|
| 44 | Bayesian Knowledge Tracing | Corbett & Anderson (1995) | — |
| 45 | Performance Factor Analysis | Pavlik, Cen & Koedinger (2009) | — |
| 46 | SM-2 / FSRS | Wozniak (1990); FSRS (2022) | — |
| 47 | Knowledge Graph Traversal | Koedinger et al. (2012) | — |
| 48 | ZPD Operationalization | Vygotsky (1978) | — |
| 49 | Mastery Thresholds | Bloom (1968) | — |
| 50 | Item Difficulty & Discrimination | Lord (1980); Embretson & Reise (2000) | — |

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

## Authoring discipline

Every chapter cites peer-reviewed sources only. Every citation is verified — author, year, journal, page range, and DOI all checked against the published abstract before commit, and the cited claim must match what the abstract actually says. Contested or weakly replicated principles are excluded rather than included with caveats. Target length is 120–200 lines per chapter — this is a runtime reference, not a textbook chapter, so prose is reserved for the evidence base and operational sections lean on bullets. When a finding has a known boundary condition, the chapter states it explicitly in section 4 ("When NOT to apply") rather than burying it.
