# VERSIONING_POLICY.md

> How the asset is versioned. Because this is a document-asset, not software, the
> versioning tracks *meaning*, not features.

---

## 1. The asset carries a single semantic version

The asset as a whole has one version, `MAJOR.MINOR.PATCH`, recorded in the top
entry of `DECISION_LOG.md` and in the site footer.

- **MAJOR** — a change to the thesis or the canonical meaning of the name.
  Anything that would make a prior reader's understanding *wrong*. Rare, heavy,
  always logged with full rationale. (See the pre-1.0 exception below, which
  governs constitutional *refinements* made before the asset reaches 1.0.)
- **MINOR** — new material that extends the asset without changing its meaning
  (a new journal essay, a new site section, a new buyer archetype), **or** a
  pre-1.0 constitutional thesis refinement as defined below.
- **PATCH** — corrections that do not change meaning: typos, phrasing, broken
  links, styling, data fixes.

**Pre-1.0 exception (0.x.0).** Before the asset reaches 1.0, a *constitutional
thesis refinement* — a Tier 1 change that sharpens the thesis or its framing
**without** changing the canonical meaning of "Spirit" or "Trainer"
(`CANONICAL_MEANING.md`) and **without** making the core observation wrong — may
increment the **MINOR** component (0.x.0) instead of forcing a 1.0 / MAJOR bump.
It still requires full Tier 1 treatment: a `DECISION_LOG.md` entry before merge,
a `CHANGE_CONTROL.md` constitutional-tier pass, and a full `QUALITY_GATE.md` run
across all content. The rationale is that a pre-1.0 asset is still settling its
own framing, so framing refinements are expected rather than exceptional.
**After 1.0**, any change to the thesis or the canonical meaning requires a MAJOR
bump, with no exception. The v0.2 reframe (**D-013**) is classified under this
rule: a Tier 1 thesis refinement whose canonical meaning is unchanged, versioned
**0.2.0**.

The current version is **0.2.1** — the v0.2 reframe (a category *position*, not
novelty; see D-013) plus the diligence layer
(`PRIOR_USE_AND_CATEGORY_DILIGENCE.md`, `SOURCE_REGISTER.md`), with a Tier 3 patch
(D-014) reconciling two residual `ACQUISITION_THESIS.md` phrasings. Still pre-1.0
because it has not yet been reviewed by its owner as ready for external buyers.

## 2. What a MAJOR bump requires

Because MAJOR versions touch the constitutional layer, they require:

1. an explicit `DECISION_LOG.md` entry (supersede, never edit, the prior one),
2. a pass through `CHANGE_CONTROL.md` at the "constitutional" tier,
3. a re-run of the full `QUALITY_GATE.md` checklist across *all* content, since a
   meaning change can invalidate copy anywhere.

## 3. Document-level revision headers

Each governing document may carry a lightweight header when it changes:

```
<!-- rev: 2026-07-31 · asset 0.1.0 · change: initial authoring -->
```

This is optional for prose files but recommended for `CANONICAL_MEANING.md` and
`CLAIM_BOUNDARY.md`, where knowing exactly when meaning last moved matters.

## 4. Data versioning

Files in `data/` carry a `"_version"` and `"_updated"` field so the site can
display provenance and so stale data is detectable. A change to a data file that
alters what the site *asserts* (e.g. adding a buyer archetype) is a MINOR bump;
fixing a typo in a label is a PATCH.

## 5. Git is the source of truth

The semantic version is a human-readable summary; the git history is the
authoritative record. Every version bump corresponds to a commit, and every
MAJOR/MINOR bump is tagged (`v0.1.0`, `v0.2.0`, …). No version exists that is not
also a commit.

## 6. No pre-release theatre

The asset does not ship alpha/beta/rc suffixes. It is either coherent (a real
version) or it is on a working branch (no version). Half-finished meaning is
never tagged.
