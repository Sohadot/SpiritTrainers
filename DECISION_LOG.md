# DECISION_LOG.md

> The append-only record of every material decision about this asset. New
> entries go at the top. Never edit or delete a past entry; supersede it with a
> new one that references it. This log is the memory of the asset — it is how a
> future owner understands *why* the asset is the way it is.

Format for each entry:

```
## [YYYY-MM-DD] Short title  (ID: D-NNN)
- **Decision:** what was decided
- **Rationale:** why
- **Alternatives considered:** what was rejected and why
- **Supersedes:** prior decision ID, if any
```

---

## [2026-09-04] Reframe from "missing name" to "unconsolidated category position"  (ID: D-013)
- **Decision:** Retire the framing that the phrase "Spirit Trainers" does not
  exist, was always available, or that its adoption is inevitable — and that
  acquiring it means *owning a category*. Adopt a narrower, stronger position:
  the human-development market is real but its language is **fragmented**, no
  *consolidated* category-level name has formed, and "Spirit Trainers" is
  proposed as that consolidating name — anchored by the exact-match `.com` and a
  public thesis. The transaction transfers a **category position**, not ownership
  of the words. Add a diligence layer (`PRIOR_USE_AND_CATEGORY_DILIGENCE.md`,
  `SOURCE_REGISTER.md`) disclosing prior/parallel uses of the phrase — an
  abandoned 2004 U.S. trademark application (serial 78446793, yoga/meditation,
  abandoned 2005), SIX's internal "Spirit Trainer" culture community, and a
  British-English footwear collision ("Spirit" trainers as shoes) — plus the
  evidence that the underlying practice is real and trainable. Reframe the site
  (home, thesis, buyer-fit, acquisition) and the governing set to match. Asset
  version → 0.2.0.
- **Rationale:** External diligence shows the phrase has scattered prior uses and
  a real lexical collision, so "the name does not exist / is unclaimed /
  inevitable" is both false and disprovable by the buyer in one search. A claim
  that survives the buyer's own research is worth more than one that does not.
  Shifting from *novelty value* to *position value* — owning the most strategic
  interpretation of a natural phrase before the market consolidates — is more
  honest and more defensible, which is the asset's own pricing strategy
  (`governance/PROJECT_DOCTRINE.md` §6, `CLAIM_BOUNDARY.md` §6). Surfacing the
  objection
  first, and showing why it does not defeat the thesis, is what makes the asset
  acquisition-grade rather than merely well-written.
- **Alternatives considered:**
  - *Keep the v0.1 "available and inevitable" framing* — rejected: a buyer's
    ten-minute search finds the prior uses and the footwear collision, and an
    undisclosed objection the buyer discovers costs more credibility than a
    disclosed one.
  - *Drop the name over the prior uses / collision* — rejected: none of the prior
    uses is a consolidated category identity; the position is still open, and the
    exact-match `.com` is exactly what lets an owner fix the human-development
    reading.
  - *Assert the phrase is now legally clear because the 2004 mark was abandoned* —
    rejected as an over-claim and as unauthorized legal advice; clearance is
    disclosed as the buyer's own step.
- **Supersedes:** partially supersedes **D-008** (refines "an existing practice
  lacks a canonical name" to "…lacks a *consolidated* name, though the words have
  scattered prior uses") and **D-003** (keeps the "acquire, not buy" posture but
  shifts the object from "the category" to a category *position*). Both stand
  except where narrowed here.
- **Tier / version:** Constitutional (Tier 1) refinement per
  `governance/CHANGE_CONTROL.md`, given full Tier 1 treatment (this log entry, a
  constitutional-tier change-control pass, and a full quality-gate run). Versioned
  as a **MINOR** bump to **0.2.0** under the pre-1.0 exception in
  `governance/VERSIONING_POLICY.md` §1: the canonical meaning of "Spirit" and
  "Trainer" (`CANONICAL_MEANING.md`) is unchanged and the core observation is
  preserved and strengthened, so this refinement increments the minor component
  rather than forcing a 1.0/MAJOR bump. (The prior wording of the policy — "any
  thesis change is MAJOR" — is reconciled by that explicit pre-1.0 clause, added
  in this same change.)

## [2026-07-31] Add self-hosted, on-brand Open Graph share cards  (ID: D-012)
- **Decision:** Generate 1200×630 PNG share cards for every page
  (`assets/og/*.png`) via `tools/build_og.py` (Pillow), and add `og:image` +
  `twitter:image` (`summary_large_image`) to all pages. Also added the OG block —
  and the previously-missing `canonical` — to the five root pages.
- **Rationale:** Links shared with strategic buyers should present an on-brand
  card, not a blank preview; and the root pages lacked canonical/OG entirely. The
  cards follow `BRAND_ARCHITECTURE.md` (near-black ground, one serif voice, no
  people or imagery) so social previews match the asset's register.
- **Alternatives considered:**
  - *Render cards with a headless browser (Playwright/Chromium)* — rejected:
    heavier and unnecessary; Pillow gives full control with one dependency.
  - *A single generic share image for all pages* — rejected: per-page cards carry
    each page's line and are stronger for sharing specific essays.
- **Note:** cards are fetched by social crawlers only, never loaded at runtime, so
  they stay within `SECURITY_POLICY.md`.
- **Supersedes:** none.

## [2026-07-31] Serve the site from the repository root  (ID: D-011)
- **Decision:** Promote the static site out of `site/` to the repository root, so
  `index.html` and its pages sit at the top level. Added `.nojekyll`; kept
  `CNAME` (spirittrainers.com). Removed the now-redundant `site/data/` mirror —
  the canonical `data/` is now the path the site fetches. Updated
  `tools/build_journal.py` to write `journal/`, `sitemap.xml`, and `robots.txt`
  at the root.
- **Rationale:** GitHub Pages served the repo root and, finding no root
  `index.html`, rendered `README.md` at the custom domain — so visitors saw the
  README instead of the site. Serving from the root fixes this with no Pages
  setting change and matches the canonical URLs and sitemap already authored
  (`spirittrainers.com/thesis.html`, `/journal/…`).
- **Alternatives considered:**
  - *Move the site to `/docs` and switch the Pages source* — rejected: requires a
    GitHub settings change the repo cannot make itself, and offers no benefit over
    root given the canonicals are already root-relative.
  - *A root `index.html` redirect into `site/`* — rejected: breaks the
    root-relative canonical URLs and adds a redirect hop.
- **Supersedes:** adjusts the deployment detail of D-004 (the site's doctrine is
  unchanged; only its location moved).

## [2026-07-31] Adopt the intellectual-paper spine  (ID: D-006)
- **Decision:** Structure the asset and the site as an argument —
  **Observation → Thesis → Category → Implications → Acquisition** — rather than a
  product layout (About / Mission / Vision / Features). Add `OBSERVATION.md` as the
  pre-thesis fact, and make `CATEGORY_THESIS.md` the explicit keystone from which
  the other documents derive (`ASSET_THESIS.md` remains the constitutional layer).
- **Rationale:** A sovereign asset should read as a reasoned paper that leads the
  reader to the conclusion, not a startup brochure. The spine makes the thesis feel
  like a logical result rather than a claim. Aligns with the Sohadot method
  (thesis → structure → interface).
- **Alternatives considered:** Keeping a conventional README/marketing structure —
  rejected: reads as a product, undercuts the "category artifact" positioning.
- **Supersedes:** none (refines the presentation of D-001).

## [2026-07-31] Center everything on Category Naming, never coaching  (ID: D-007)
- **Decision:** The asset's subject is *category naming*, not coaching, therapy,
  wellbeing, or training method. The home and thesis surfaces are kept free of the
  word "coaching"; it appears only where a buyer archetype is named on a deep page.
- **Rationale:** If a visitor reads "coaching" in the first minute, the asset loses
  the distinctiveness that separates it from a thousand development sites.
- **Alternatives considered:** Framing around the practice (training the interior) —
  kept as *support*, but demoted below the naming argument, which is what makes the
  asset unique.
- **Supersedes:** reinforces `CLAIM_BOUNDARY.md` Drift A.

## [2026-07-31] Never claim to create a category; only that one lacks a name  (ID: D-008)
- **Decision:** All copy uses the disciplined framing: *an existing,
  cross-disciplinary practice lacks a canonical category name* — never "we are
  creating a new industry/category."
- **Rationale:** The modest claim is more honest and more defensible, and therefore
  more credible to a strategic buyer. Over-claiming invites dismissal.
- **Alternatives considered:** "Creating the category of Spirit Trainers" —
  rejected as an over-claim that damages credibility.
- **Supersedes:** none.

## [2026-07-31] Add the naming/linguistics document layer  (ID: D-009)
- **Decision:** Add `OBSERVATION.md`, `CATEGORY_EVIDENCE.md`, `NAMING_POWER.md`,
  `SEMANTIC_POSITION.md`, and `NON_GOALS.md` to the governing set.
- **Rationale:** These deepen the asset's true differentiator — that its value is
  linguistic and category-theoretic, not operational. `NON_GOALS.md` in particular
  prevents misreading from the first contact.
- **Alternatives considered:** Folding these into existing files — rejected: each
  deserves standalone authority and citation.
- **Supersedes:** none.

## [2026-07-31] Repoint the Journal at names & categories  (ID: D-010)
- **Decision:** The Journal is elevated to *part of the thesis* and writes about
  names, categories, and positioning — not about training the interior. Replaced the
  three training-centric seed essays with: *Why Categories Need Names*, *When a Name
  Becomes Infrastructure*, *The Difference Between a Profession and a Category*, and
  *Why Generic Brands Rarely Lead Categories*.
- **Rationale:** Essays about language and category formation reinforce what makes
  the asset unique; essays about training would make it read like a development blog.
- **Alternatives considered:** Keeping the training-focused essays — rejected as
  off-thesis. (They were removed, not merely deprecated.)
- **Supersedes:** D-005 (redefines the Journal's subject; the "reference not
  frequency" principle from D-005 stands).

## [2026-07-31] Establish the asset as a category document, not a platform  (ID: D-001)
- **Decision:** Build SpiritTrainers.com as a conceptual "category acquisition"
  asset — a set of governing thesis documents plus a static philosophical site —
  rather than an operating coaching platform.
- **Rationale:** The name's greatest value is latent (what it *means* and could
  *become*), not operational. A platform would consume time and carry uncertain
  return; a category document maximizes acquisition value and fits the
  sovereign-asset method (thesis → structure → interface). See `ASSET_THESIS.md`.
- **Alternatives considered:**
  - *Full coaching platform* — rejected: high cost, needs staff/video/members,
    uncertain return, dilutes the name into one more competitor.
  - *"Premium domain for sale" landing page* — rejected: caps value at the domain
    market's ceiling and attracts flippers, not strategic buyers.
- **Supersedes:** none.

## [2026-07-31] Fix the canonical meaning to prevent drift  (ID: D-002)
- **Decision:** Adopt `CANONICAL_MEANING.md` as the fixed definition of "Spirit"
  (secular inner character/resilience, not religion/mysticism) and "Trainer"
  (deliberate capability-building, not teaching/therapy/motivation).
- **Rationale:** A category name is only durable if its meaning is stable.
  Ambiguity would let the name drift toward spirituality (losing cross-cultural
  reach) or coaching (collapsing into a competitor).
- **Alternatives considered:** Leaving meaning open for the buyer — rejected: an
  undefined name is worth less and is easy to dismiss.
- **Supersedes:** none.

## [2026-07-31] Frame the transaction as "Acquire the Category"  (ID: D-003)
- **Decision:** The site and all buyer materials use "Acquire the Category," never
  "Buy this Domain" / "Make an Offer."
- **Rationale:** The framing determines the valuation basis (strategic vs.
  commodity) and filters for strategic buyers. See `ACQUISITION_THESIS.md`.
- **Alternatives considered:** Conventional domain-marketplace framing — rejected
  for the reasons in `ACQUISITION_THESIS.md` §2.
- **Supersedes:** none.

## [2026-07-31] Adopt an idea-is-the-interface visual doctrine  (ID: D-004)
- **Decision:** The site uses a near-black ground, a single white typographic
  voice, generous negative space, slow motion, and **no** people, nature
  clichés, or spiritual iconography. Each scroll poses a question or delivers a
  one-word answer, leading the reader to arrive at the name themselves.
- **Rationale:** Differentiates the asset from every coaching/self-help site and
  embodies the thesis that the idea itself is the product. See
  `BRAND_ARCHITECTURE.md`.
- **Alternatives considered:** Conventional hero + features + CTA layout —
  rejected: indistinguishable from the category it must rise above.
- **Supersedes:** none.

## [2026-07-31] Seed a reference Journal, not a blog  (ID: D-005)
- **Decision:** Include `content/journal/` as a small set of deep, reference-grade
  essays (not frequent, casual blog posts) to raise authority and preserve an
  operation path — without turning the asset into a content business.
- **Rationale:** Compounds acquisition value and search authority while staying
  inside the claim boundary. Honestly noted: it does not create recurring
  revenue by itself.
- **Alternatives considered:** No editorial layer — rejected: leaves authority
  and search value on the table. A high-frequency blog — rejected: off-register
  and operationally heavy.
- **Supersedes:** none.
