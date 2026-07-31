# Spirit Trainers Journal

> Part of the thesis, not a side blog. The Journal is a small body of
> reference-grade essays about **names, categories, and positioning** — the
> forces the whole asset turns on. It is deliberately *not* about training,
> wellbeing, or self-improvement. Its subject is the same as the asset's: how a
> word becomes the identity of a category.

## What the Journal is

- **An extension of the argument.** Each essay develops one facet of *why names
  make categories* — the premise the asset rests on. The essays could stand in
  front of any category-naming thesis; that generality is the point.
- **Reference, not frequency.** A few durable essays, closer to position papers
  than posts.
- **On-register and on-boundary.** Every essay obeys `CLAIM_BOUNDARY.md` and
  `NON_GOALS.md`: no coaching pitch, no spiritual claim, no medical claim, no
  invented figures, no "how to improve yourself."

## What the Journal is *not*

- Not motivational or self-help writing ("how to be happy" is out of scope).
- Not about the mechanics of training the human interior.
- Not SEO filler, and not tied to any author's personality.

## Essays

| # | Title | On |
|---|-------|----|
| 1 | [Why Categories Need Names](why-categories-need-names.md) | names as an act of gathering |
| 2 | [When a Name Becomes Infrastructure](when-a-name-becomes-infrastructure.md) | the load-bearing economics of a category word |
| 3 | [The Difference Between a Profession and a Category](profession-vs-category.md) | altitude: role vs. space |
| 4 | [Why Generic Brands Rarely Lead Categories](why-generic-brands-rarely-lead.md) | why descriptive names don't lead |
| 5 | [The Linguistics of Human Development](the-linguistics-of-human-development.md) | the missing hypernym; the lexical gap |
| 6 | [The Name That Arrives Before Its Market](the-name-that-arrives-before-its-market.md) | naming ahead of consolidation |
| 7 | [Why the Best Names Feel Inevitable](why-names-feel-inevitable.md) | recognition; absent vs. missing; fit |
| 8 | [The Defensibility of a Category Name](the-defensibility-of-a-category-name.md) | the moat: rivals must position against the word |

Each rendered essay carries inline internal links and a **Related reading** block
that cross-links the Journal and points back to the thesis and acquisition pages.

The site renders each essay at `/journal/<slug>.html` (served from the repo
root); the markdown here is the canonical source. Run `tools/build_journal.py` to
regenerate the rendered pages (keep the two in sync — a Tier 2 change).

Note that every title is about **language, categories, and positioning** — not
about training itself. That is what keeps the Journal part of *this* asset rather
than one more development blog.

## Adding an essay

Adding a Journal essay is a Tier 2 change (`governance/CHANGE_CONTROL.md`): it
must pass the full `QUALITY_GATE.md`, stay inside `NON_GOALS.md`, add a row to the
table above, and — if it introduces any new framing — a `DECISION_LOG.md` entry.
