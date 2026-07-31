# SpiritTrainers

**Training the human spirit is becoming infrastructure.**

This repository is not a coaching platform and not a domain-for-sale page. It is
a **category asset** — an intellectual artifact whose subject is a name.

---

## Observation

Human development has expanded into hundreds of disciplines, certifications, and
brands. Yet no concise, category-level expression has emerged for those whose
purpose is the deliberate cultivation of human character, resilience, judgment,
and inner strength.

The practitioners exist. The institutions exist. The market exists. The
*category name* does not.

## Why this repository exists

Not a mission, not an "about." Three purposes, plainly:

1. **To test** whether *Spirit Trainers* can function as a category-level name.
2. **To document** that thesis transparently, from first principles.
3. **To present** the asset in a form suitable for strategic acquisition.

Everything in this repository serves one of those three, and nothing else.

## Thesis

Some markets exist before they have a canonical name.

> The practice is ancient.
> The institutions already exist.
> The market already exists.
> The category name does not.

*Spirit Trainers* is proposed as that name: a category-level identity for
organizations and practitioners who deliberately develop the human interior —
resilience, character, judgment, inner strength — across cultures and
institutions.

The asset does not claim to invent a field. It makes one narrow, defensible
observation and follows it to its conclusion: an existing, cross-disciplinary
practice lacks a canonical category name, and the phrase that would fill the gap
is available.

### Why a name

Some names describe companies. Some names describe products. A few names become
the language through which an entire category is understood — the words a market
reaches for before it reaches for any particular brand. Those names are not
manufactured; they are recognized, usually late, usually by whoever was paying
attention first.

*Spirit Trainers* reads like one of those names: a phrase you half-remember
already existing. That quiet sense of inevitability — *there should have been a
name like this* — is the entire asset.

---

## Read in this order

The asset is written as an argument, not a brochure. It moves from a fact, to a
claim, to its consequences. Read top to bottom:

**Observation → Thesis → Category → Implications → Acquisition**

1. [`OBSERVATION.md`](OBSERVATION.md) — the plain fact the asset rests on.
2. [`CATEGORY_THESIS.md`](CATEGORY_THESIS.md) — **the keystone.** Why this can be a *category*. Every other document derives from it.
3. [`CATEGORY_EVIDENCE.md`](CATEGORY_EVIDENCE.md) — the real "___ Trainers" series, and where this name sits in it.
4. [`SEMANTIC_POSITION.md`](SEMANTIC_POSITION.md) — pure linguistic analysis of the phrase.
5. [`NAMING_POWER.md`](NAMING_POWER.md) — why names, not products, create categories.
6. [`CANONICAL_MEANING.md`](CANONICAL_MEANING.md) — the fixed meaning of the name.
7. [`CATEGORY_POSITIONING.md`](CATEGORY_POSITIONING.md) — where it sits; one name, many markets.
8. [`NON_GOALS.md`](NON_GOALS.md) — what the asset is emphatically *not*.
9. [`BUYER_LOGIC.md`](BUYER_LOGIC.md) — who could acquire it and why.
10. [`ACQUISITION_THESIS.md`](ACQUISITION_THESIS.md) — why "acquire," not "buy."
11. [`BRAND_ARCHITECTURE.md`](BRAND_ARCHITECTURE.md) — how the name behaves as a brand.
12. [`CLAIM_BOUNDARY.md`](CLAIM_BOUNDARY.md) — the limits of what the asset claims.
13. [`ASSET_THESIS.md`](ASSET_THESIS.md) — the constitutional layer that governs the whole.
14. [`DECISION_LOG.md`](DECISION_LOG.md) — why the asset is the way it is.

> `CATEGORY_THESIS.md` is the intellectual keystone — the reference the rest is
> derived from. `ASSET_THESIS.md` is the constitutional layer — the governance
> authority. Read the keystone to understand the idea; read the constitution to
> understand the rules.

## The site

The site under [`site/`](site/) is an **interactive thesis**, not a landing page
— fully static, with no accounts, video, dashboards, or trainers. Its doctrine:
*the idea is the interface.* Deep near-black ground, a single typographic voice,
generous space, slow motion, and no people or spiritual clichés. Each scroll
poses a question or delivers a one-word answer, so the reader arrives at the name
— *Spirit Trainers* — on their own.

```sh
cd site && python3 -m http.server 8080   # then open http://localhost:8080
```

## What this asset optimizes for

- **Primary:** maximize the strategic *acquisition* value of the name.
- **Not** optimized for recurring monthly revenue; the Journal exists to build
  authority and preserve an operation path, not to be a content business.

See [`ASSET_THESIS.md`](ASSET_THESIS.md) §6 for the honest trade-off, and
[`NON_GOALS.md`](NON_GOALS.md) for the full list of what this is not.

---

## Repository map

```
SpiritTrainers/
├── README.md
│
│   ── the argument, in order ──
├── OBSERVATION.md             ← the plain fact
├── CATEGORY_THESIS.md         ← the keystone
├── CATEGORY_EVIDENCE.md
├── SEMANTIC_POSITION.md
├── NAMING_POWER.md
├── CANONICAL_MEANING.md
├── CATEGORY_POSITIONING.md
├── NON_GOALS.md
├── BUYER_LOGIC.md
├── ACQUISITION_THESIS.md
├── BRAND_ARCHITECTURE.md
├── CLAIM_BOUNDARY.md
├── ASSET_THESIS.md            ← the constitution
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
│   └── journal/               ← reference essays on names & categories
│
├── data/                      ← structured data rendered by the site
│   ├── buyers.json
│   ├── category-map.json
│   └── naming-analysis.json
│
├── static/                    ← reserved; intentionally minimal
│
└── site/                      ← the interactive thesis (self-contained)
    ├── index.html
    ├── thesis.html
    ├── buyer-fit.html
    ├── brand-potential.html
    ├── acquisition.html
    ├── journal/               ← the rendered Journal (index + 6 essays, SEO + JSON-LD)
    ├── assets/                ← style.css + app.js (no external deps)
    ├── data/                  ← deploy mirror of the JSON the site renders
    ├── sitemap.xml            ← generated; all pages
    └── robots.txt
```

> The canonical structured data lives in `/data/`. `site/data/` is a deploy
> mirror so `site/` is self-contained and can be served as its own root; keep the
> two in sync when data changes (a Tier 2 change per `CHANGE_CONTROL.md`).

## Editing

All changes follow [`governance/CHANGE_CONTROL.md`](governance/CHANGE_CONTROL.md)
and must pass [`governance/QUALITY_GATE.md`](governance/QUALITY_GATE.md) — in
particular, nothing may violate [`CLAIM_BOUNDARY.md`](CLAIM_BOUNDARY.md) or the
[`NON_GOALS.md`](NON_GOALS.md).
