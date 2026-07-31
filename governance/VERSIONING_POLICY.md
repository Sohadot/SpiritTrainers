# VERSIONING_POLICY.md

> How the asset is versioned. Because this is a document-asset, not software, the
> versioning tracks *meaning*, not features.

---

## 1. The asset carries a single semantic version

The asset as a whole has one version, `MAJOR.MINOR.PATCH`, recorded in the top
entry of `DECISION_LOG.md` and in the site footer.

- **MAJOR** — a change to the thesis or the canonical meaning of the name.
  Anything that would make a prior reader's understanding *wrong*. Rare, heavy,
  always logged with full rationale.
- **MINOR** — new material that extends the asset without changing its meaning:
  a new journal essay, a new site section, a new buyer archetype.
- **PATCH** — corrections that do not change meaning: typos, phrasing, broken
  links, styling, data fixes.

The current version is **0.1.0** — the asset is coherent and complete in
structure, but pre-1.0 because it has not yet been reviewed by its owner as
ready for external buyers.

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
