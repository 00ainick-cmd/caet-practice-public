# Citation Rules

Discipline that every chapter author must follow. The library's defensibility argument rests on
every citation being real, on-point, and verifiable. A single fabricated or misattributed
citation undermines the trust the runtime places in this library.

## Allowed sources

- **Peer-reviewed journal articles** — the default. Prefer high-impact venues
  (*Psychological Science*, *Science*, *Review of Educational Research*,
  *Educational Psychology Review*, *Cognition and Instruction*, etc.).
- **Seminal book chapters from established academic publishers** — Cambridge, Oxford, MIT Press,
  Routledge, Springer, Erlbaum/Taylor & Francis. Prefer chapters that are themselves cited in
  the journal literature.
- **Position papers and standards from learned societies** — APA, AERA, NRC/NAS, ICAO, FAA,
  IOM/NAM. Cite the report by its formal title.
- **Meta-analyses and systematic reviews** — required for any effect-size claim. Always prefer
  a meta-analytic estimate over a single primary study when one exists.

## Disallowed sources

- **Wikipedia** — useful for finding references to chase down; never cite directly.
- **Personal blogs** — rare exception only for active researchers' professional academic blogs
  (e.g., Daniel Willingham's "Science and Education", Cedar Riener's posts) and only when no
  peer-reviewed equivalent exists. Flag these for explicit reviewer approval in the chapter.
- **EdTech vendor marketing** — Khan Academy, Coursera, ed-tech-startup whitepapers. The
  underlying research, if real, is published elsewhere; cite that.
- **Social media** — LinkedIn posts, Twitter/X threads, Substack, Medium, podcasts, YouTube.
  Cite the underlying paper instead.
- **Textbooks for empirical claims** — textbooks are appropriate for definitions and framework
  exposition, but every effect-size or empirical claim must cite the primary research.
- **"Personal communication"** — not in this library. If the claim cannot be cited from
  published work, drop the claim.
- **Predatory journals** — check Beall's List or DOAJ status when uncertain about a venue.

## Citation format

Use full APA-style citations in the `key_sources` frontmatter array. Each citation includes:

- **Author(s)** — last name, then initials. Multiple authors separated by commas with `&`
  before the last.
- **Year** — in parentheses, e.g., `(2017)`.
- **Title** — sentence case, no quotation marks.
- **Journal** — italicized via markdown `*Journal Name*`. Volume(issue), page range.
- **DOI** — as the last element when the publisher provides one, formatted as
  `https://doi.org/10.xxxx/xxxx` or the legacy `doi:10.xxxx/xxxx` form (the exemplar uses both
  conventions; either is acceptable).

Example (from the exemplar):

> Roediger, H. L., & Karpicke, J. D. (2006). The power of testing memory: Basic research and
> implications for educational practice. *Perspectives on Psychological Science*, 1(3),
> 181-210. doi:10.1111/j.1745-6916.2006.00012.x

## Verification rule

Every citation MUST be web-searchable and confirmed before commit. The author MUST run a
`WebSearch` for `<first_author> <year> <title_keywords>` and verify three things:

1. The paper exists at the cited venue with the cited authors and year
2. The DOI resolves (if one is provided)
3. **The abstract or accessible content supports the specific claim being made** — not just
   the topic in general

If any of the three fails, **drop the claim**. If the claim is essential to the chapter, find
a different citation that genuinely supports it. Do not fudge.

## Effect-size discipline

When citing an effect size:

- Quote the actual number from the meta-analysis or empirical paper — do not paraphrase a
  range from memory.
- Use Cohen's d, Hedges' g, or odds ratio as the source paper reports it. Do not silently
  convert between metrics.
- Include the source in the same sentence: e.g., `"d ≈ 0.5–0.8 (Adesope et al., 2017)"`.
- Distinguish lab from classroom estimates where the source paper does — the magnitude
  difference is real and matters operationally.
- For foundational principles where no single effect size is meaningful (cognitive load
  theory, schema theory), set `effect_size: null` in frontmatter rather than inventing one.

## Replication discipline

The library admits only strong, well-replicated findings. When a chapter discusses a
replication, contested finding, or known boundary condition:

- Cite the actual replication paper, not the original. The replication is what bears on the
  current evidence base.
- State the contested camp's verdict accurately. Do not present settled science as contested,
  and do not present contested findings as settled.
- If a once-classic finding has been disconfirmed (learning styles, growth mindset at scale,
  Bloom's 2-sigma at scale), the principle does not get a chapter. See README "Deliberately
  excluded".

## The Bertilsson lesson (DOI verifies but abstract doesn't)

During the exemplar's authoring an initial draft cited Bertilsson et al. (2021) for the claim
that short-answer outperforms multiple-choice. The DOI checked out
(`doi:10.1177/1475725720973494`) and the year and journal matched — but reading the abstract
revealed the paper was a Swahili-Swedish word-pair *individual-differences* study, not a
format-comparison study. The cited claim was not what the paper was actually about. The
citation was dropped and Roediger & Butler (2011) was used instead, which genuinely makes the
short-answer-vs-multiple-choice point.

**Lesson:** DOI verification is necessary but not sufficient. The abstract must support the
specific claim being attached to the citation. A real paper used for the wrong claim is
indistinguishable from a fabricated one in terms of damage to the library's credibility.
