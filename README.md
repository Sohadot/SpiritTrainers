# SpiritTrainers

**Training the human spirit is becoming infrastructure.**

This repository is not a coaching platform and not a domain-for-sale page. It is
a **category asset**: a set of governing documents and a static, philosophical
site that argue a single idea —

> Some markets exist before they have a canonical name. *Spirit Trainers* is
> proposed as one of those names: a category-level identity for organizations
> that deliberately develop human resilience, character, judgment, and inner
> strength across cultures and institutions.

The activity is ancient. The name is available. This asset makes the case.

---

## Read in this order

The asset is written thesis-first. To understand it, read top to bottom:

1. [`ASSET_THESIS.md`](ASSET_THESIS.md) — the founding document. Start here.
2. [`CATEGORY_THESIS.md`](CATEGORY_THESIS.md) — why this can be a *category*.
3. [`CANONICAL_MEANING.md`](CANONICAL_MEANING.md) — the fixed meaning of the name.
4. [`CATEGORY_POSITIONING.md`](CATEGORY_POSITIONING.md) — where it sits; one name, many markets.
5. [`BUYER_LOGIC.md`](BUYER_LOGIC.md) — who could acquire it and why.
6. [`ACQUISITION_THESIS.md`](ACQUISITION_THESIS.md) — why "acquire," not "buy."
7. [`BRAND_ARCHITECTURE.md`](BRAND_ARCHITECTURE.md) — how the name behaves as a brand.
8. [`CLAIM_BOUNDARY.md`](CLAIM_BOUNDARY.md) — what the asset must never claim.
9. [`DECISION_LOG.md`](DECISION_LOG.md) — why the asset is the way it is.

## Repository map

```
SpiritTrainers/
├── README.md                  ← you are here
├── ASSET_THESIS.md            ← founding document
├── CATEGORY_THESIS.md
├── CATEGORY_POSITIONING.md
├── CANONICAL_MEANING.md
├── BUYER_LOGIC.md
├── ACQUISITION_THESIS.md
├── BRAND_ARCHITECTURE.md
├── CLAIM_BOUNDARY.md
├── DECISION_LOG.md
│
├── governance/                ← how the asset is maintained
│   ├── PROJECT_DOCTRINE.md
│   ├── VERSIONING_POLICY.md
│   ├── CHANGE_CONTROL.md
│   ├── QUALITY_GATE.md
│   └── SECURITY_POLICY.md
│
├── content/                   ← source text for the site + journal
│   ├── thesis.md
│   ├── missing-category.md
│   ├── buyer-fit.md
│   ├── brand-potential.md
│   ├── acquisition.md
│   └── journal/               ← reference-grade essays
│
├── data/                      ← structured data rendered by the site
│   ├── buyers.json
│   ├── category-map.json
│   └── naming-analysis.json
│
├── static/                    ← static assets (kept intentionally minimal)
│
└── site/                      ← the built static site (self-contained)
    ├── index.html             ← the interactive thesis (home)
    ├── thesis.html
    ├── buyer-fit.html
    ├── brand-potential.html
    ├── acquisition.html
    ├── assets/                ← style.css + app.js (no external deps)
    └── data/                  ← deploy mirror of the JSON the site renders
```

> The canonical structured data lives in `/data/`. `site/data/` is a deploy
> mirror so `site/` is self-contained and can be served as its own root; keep
> the two in sync when data changes (a Tier 2 change per `CHANGE_CONTROL.md`).

## The site

The site under [`site/`](site/) is fully static — no accounts, no video, no
dashboards, no trainers. Its doctrine: **the idea is the interface.** Deep
near-black ground, a single typographic voice, generous space, slow motion, and
no people or spiritual clichés. Each scroll poses a question or delivers a
one-word answer, so the reader arrives at the name — *Spirit Trainers* — on their
own.

To preview locally:

```sh
cd site && python3 -m http.server 8080
# then open http://localhost:8080
```

## What this asset optimizes for

- **Primary:** maximize the strategic *acquisition* value of the name.
- **Not** optimized for recurring monthly revenue; the Journal exists to build
  authority and preserve an operation path, not to be a content business.

See [`ASSET_THESIS.md`](ASSET_THESIS.md) §6 for the honest trade-off.

## Contributing / editing

All changes follow [`governance/CHANGE_CONTROL.md`](governance/CHANGE_CONTROL.md)
and must pass [`governance/QUALITY_GATE.md`](governance/QUALITY_GATE.md) — in
particular, nothing may violate [`CLAIM_BOUNDARY.md`](CLAIM_BOUNDARY.md).
