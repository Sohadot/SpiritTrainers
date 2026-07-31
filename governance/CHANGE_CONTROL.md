# CHANGE_CONTROL.md

> How changes enter the asset. The controls are proportional: the closer a change
> gets to the *meaning* of the name, the heavier the process.

---

## 1. Three tiers of change

Every change is classified into one tier. The tier decides the process.

### Tier 1 — Constitutional
Touches the thesis or the canonical meaning:
`ASSET_THESIS.md`, `CATEGORY_THESIS.md`, `CANONICAL_MEANING.md`,
`CLAIM_BOUNDARY.md`.

- Requires a `DECISION_LOG.md` entry **before** merge, with rationale and
  rejected alternatives.
- Requires a MAJOR version consideration (`VERSIONING_POLICY.md`).
- Requires a full `QUALITY_GATE.md` pass across *all* content, because meaning
  changes can invalidate copy anywhere.
- Never merged in the same change as unrelated edits.

### Tier 2 — Substantive
Adds or reframes material without changing meaning:
positioning, buyer logic, brand architecture, new journal essays, new site
sections, data that changes what the site asserts.

- Requires a `DECISION_LOG.md` entry if the change is material.
- Requires a `QUALITY_GATE.md` pass on the affected content.
- MINOR version bump.

### Tier 3 — Editorial
Does not change meaning: typos, phrasing, styling, link fixes, data label fixes.

- No decision-log entry required.
- Lightweight `QUALITY_GATE.md` check (claim-boundary + build still works).
- PATCH version bump.

## 2. The change lifecycle

```
propose → classify tier → draft on a branch → quality gate → (log if T1/T2)
        → review → merge → version bump → tag if MAJOR/MINOR
```

No change skips the quality gate. Tier 1 changes additionally cannot be
self-approved: the founding owner (or a delegate named in writing) signs off.

## 3. Branch discipline

- All work happens on a branch; `main` always holds a coherent asset.
- One branch, one coherent change. Do not mix a Tier 1 meaning change with Tier 3
  typo fixes.
- Branch names describe the change, not the person.

## 4. What can never change quietly

The following require a Tier 1 process even if the diff looks small:

- the canonical name itself,
- the definition of "Spirit" or "Trainer,"
- the "acquire, not buy" framing,
- anything in `CLAIM_BOUNDARY.md` §3 (the never-claim list).

A one-word edit to any of these is still a constitutional change.

## 5. Emergency corrections

If live content violates `CLAIM_BOUNDARY.md` (e.g. an accidental medical or
religious claim), it may be removed immediately without the full process — a
takedown is always allowed. The *replacement* text then re-enters through the
normal tier for that content, and the incident is logged.

## 6. Provenance

Every merged change is traceable to a commit, and every Tier 1/Tier 2 change is
traceable to a decision-log entry. If you cannot answer "why was this changed and
by what authority," the change has not actually completed.
