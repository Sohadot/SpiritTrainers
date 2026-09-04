<!-- rev: 2026-09-04 · asset 0.2.0 · change: initial authoring (v0.2 diligence layer) -->

# SOURCE_REGISTER.md

> The external evidence behind the asset's factual claims, in one place. Every
> statement of outside fact in `PRIOR_USE_AND_CATEGORY_DILIGENCE.md` traces to a
> row here, so a buyer can verify each one directly rather than taking the
> asset's word for it. Verifiability is the point: the asset states only what a
> reader can independently check.
>
> **Discipline:** no figure, market size, or outcome is asserted as fact
> anywhere in this asset (`CLAIM_BOUNDARY.md` §3, `governance/QUALITY_GATE.md`
> G1). This register records *existence and status* facts and points at
> *published research*; it does not launder estimates into claims.

---

## How to read this file

Each row records: what the source supports, the source itself, where to find it,
when it was last checked, and how confident the check was. "Verified" means the
primary or an authoritative secondary record was read directly on the date
shown. Statuses (especially trademark statuses) are point-in-time and should be
re-checked before any transaction closes.

## Register

### S-01 — Abandoned U.S. trademark application "SPIRIT TRAINERS"
- **Supports:** `PRIOR_USE…` §2.1 — a 2004 filing for a narrow yoga/meditation
  offering, abandoned in 2005; no live registration resulted.
- **Record:** USPTO trademark application, serial no. **78446793**, mark
  "SPIRIT TRAINERS," Intl. Class 041, filed 7 July 2004, applicant Jeffrey D.
  Bader (assoc. William M. Donnelly); status **dead / abandoned** (14 Sep 2005,
  failure to respond).
- **Where (locator):** USPTO TSDR status record, primary —
  `https://tsdr.uspto.gov/#caseNumber=78446793&caseType=SERIAL_NO&searchType=statusSearch`.
  Public mirror — `https://www.trademarkia.com/spirit-trainers-78446793`.
  Stable identifier: **U.S. serial no. 78446793**.
- **Checked:** 2026-09-04. **Confidence:** Verified (status record read: mark
  "SPIRIT TRAINERS", filed 2004-07-07, dead/abandoned 2005-09-14).
- **Caveat:** point-in-time; a dead application is not a clearance opinion. Other
  filings and common-law uses may exist. Not legal advice.

### S-02 — "SIX Spirit Trainer" internal culture community
- **Supports:** `PRIOR_USE…` §2.2 — an institution already uses the exact phrase
  for people who develop its human/cultural interior (an internal HR role, not a
  category brand).
- **Record:** ADVANCE (University of St. Gallen, HSG) best-practice report on
  SIX's culture change via its "SIX Spirit Trainer" community.
- **Where (locator):** ADVANCE HSG best-practice report —
  `https://www.advance-hsg-report.ch/en/best-practices/new-culture-change-via-the-six-spirit-trainer-community/`
  (University of St. Gallen). The phrase "SIX Spirit trainer" appears in the body
  text (~40 internal volunteer trainers; values/inclusion workshops).
- **Checked:** 2026-09-04. **Confidence:** Verified (report page read; exact
  phrase confirmed present).
- **Caveat:** cited as corroboration only. No endorsement, affiliation, or
  partnership with SIX or HSG is claimed or implied.

### S-03 — "Spirit" footwear (British-English lexical collision)
- **Supports:** `PRIOR_USE…` §2.3 — "Spirit" + "trainers" has an unrelated,
  everyday reading in British English (a sneaker), a real ambiguity the v0.1
  framing understated.
- **Record:** Hotter (UK footwear brand, Lancashire) markets a women's lace-up
  trainer named "Spirit."
- **Where (locator):** Hotter brand site — `https://www.hotter.com/` (search
  "Spirit"); retailer product listing with a stable product code —
  `https://www.eskisfootwear.co.uk/hotter-spirit-womens-lace-up-trainers---soft-pink-103355-p.asp`
  (product code 103355).
- **Checked:** 2026-09-04. **Confidence:** Verified (product listings read).
- **Caveat:** unrelated domain; used to document the collision, not a competitor
  in human development.

### S-04 — Resilience / character-strengths training is real and trainable
- **Supports:** `PRIOR_USE…` §3 — the underlying activity is studied and
  effective under many scattered labels; what it lacks is a consolidated name.
- **Record:** peer-reviewed randomized controlled trials and meta-analyses of
  workplace and first-responder resilience-training programs (character-strength,
  cognitive, and emotional components), reporting measurable effects.
- **Where (locators):** representative peer-reviewed studies, each identified by
  DOI/PMID and PMC record:
  - "Resilience@Work Mindfulness Program: Results From a Cluster Randomized
    Controlled Trial With First Responders," *J Med Internet Res*, 2019 — PMID
    **30777846**, DOI **10.2196/12894**, PMC6399574
    (`https://pmc.ncbi.nlm.nih.gov/articles/PMC6399574/`).
  - "Team Resilience Training in the Workplace: E-Learning Adaptation,
    Measurement Model, and Two Pilot Studies," *JMIR Ment Health*, 2018 — PMID
    **29720362**, DOI **10.2196/mental.8955**, PMC5956157
    (`https://pmc.ncbi.nlm.nih.gov/articles/PMC5956157/`).
- **Checked:** 2026-09-04. **Confidence:** Verified (both records read: titles,
  journals, years, PMIDs, and DOIs confirmed). These are cited as examples of a
  broader literature; specific effect sizes are **not** asserted by this asset.
- **Caveat:** cited to establish that the practice is real and trainable — not to
  quantify outcomes, which the asset never does.

---

## Maintenance

- Re-verify S-01 (trademark status) and re-run a fresh phrase search before any
  transaction closes; record the new date here.
- Add a new row for any prior/parallel use discovered later; never delete a row —
  supersede it with a dated note, consistent with the append-only spirit of
  `DECISION_LOG.md`.
- If a source can no longer be located, mark the row **stale** with the date
  rather than removing it.
