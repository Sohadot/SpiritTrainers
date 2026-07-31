# QUALITY_GATE.md

> The checklist every change must pass before it merges. If any hard gate fails,
> the change does not ship — regardless of how good the rest of it is.

---

## Hard gates (any failure blocks the change)

### G1 — Claim boundary
- [ ] Nothing violates `CLAIM_BOUNDARY.md` §3 (the never-claim list).
- [ ] Nothing pushes the asset toward a listed non-goal in `NON_GOALS.md`.
- [ ] No claim to **create** a category/industry; only that an existing practice
      **lacks a canonical name**.
- [ ] No medical, therapeutic, or clinical claim, stated or implied.
- [ ] No religious, mystical, or metaphysical claim.
- [ ] No revenue / traffic / market-size figure stated as fact.
- [ ] No claim to have *invented* the field.
- [ ] No unapproved endorsement, affiliation, or named partnership.

### G2 — Canonical meaning
- [ ] "Spirit" is used only in the secular sense fixed in `CANONICAL_MEANING.md`.
- [ ] "Trainer" is used only as deliberate capability-building (not teach /
      preach / treat / motivate).
- [ ] "Spirit Trainers" is used as a *category*, never as a coaching service.

### G3 — No drift
- [ ] No **Drift A** (toward coaching): no "get started," "your journey," "we
      help you," service/benefit-to-a-person language.
- [ ] No **Drift B** (toward spirituality): no soul/sacred/energy/enlightenment
      language or imagery.

### G4 — Framing
- [ ] The transaction is framed as "Acquire the Category," never "Buy this
      Domain" / "Make an Offer."
- [ ] No people, nature clichés, or spiritual iconography in visuals.

### G5 — Build integrity
- [ ] The static site builds and serves with no console errors.
- [ ] All internal links resolve.
- [ ] All `data/*.json` files are valid JSON and render without error.
- [ ] The site is legible with JavaScript disabled (content is not JS-gated).

## Soft gates (should pass; a documented exception may proceed)

### S1 — Register
- [ ] Tone is observational, not promotional. No exclamation-mark hype.
- [ ] Declarative sentences; the reader is led to the name, not told to buy it.

### S2 — Subtraction
- [ ] Every element carries meaning; nothing decorative was added.
- [ ] The change removes as much as it adds where possible.

### S3 — Consistency
- [ ] Terminology matches the governing documents exactly.
- [ ] Any new data has `_version` / `_updated` provenance fields.

### S4 — Accessibility
- [ ] Sufficient contrast on the near-black ground.
- [ ] Motion respects `prefers-reduced-motion`.
- [ ] Semantic HTML; images (if any) have alt text.

## How to run the gate

1. Read the diff against G1–G3 first — meaning failures are the costly ones.
2. Serve the site locally (`cd site && python3 -m http.server`) and click every
   changed page, with and without JS, and with reduced-motion on.
3. Validate every changed JSON file.
4. For Tier 1/Tier 2 changes, confirm the `DECISION_LOG.md` entry exists.
5. Record the result. A passing gate is the merge authorization.

## Why the gate is strict about claims, not polish

Polish can be fixed after shipping. A false or off-register claim, once it
reaches a buyer, damages the credibility that gives the asset its value. The gate
is therefore heaviest exactly where the risk to value is highest: what the asset
says, not how it looks.
