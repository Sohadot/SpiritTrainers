# tools

Small, dependency-free build helpers. Nothing here runs at page-view time; the
site remains fully static (`governance/SECURITY_POLICY.md`).

## build_journal.py

Regenerates the site Journal from the canonical markdown.

- **Reads:** `content/journal/*.md` (the canonical essay source).
- **Writes:** `journal/index.html`, `journal/<slug>.html` (one per essay), plus
  `sitemap.xml` and `robots.txt` — all at the repo root, where the site is served.
- Injects per-page SEO (title, description, keywords, canonical, Open Graph,
  Twitter card) and inline JSON-LD (`Article` + `BreadcrumbList` on essays,
  `Blog` on the index). JSON-LD is inline data, not an external script, so it is
  consistent with the no-external-dependency policy.

Run it after editing any journal essay or adding a new one (a Tier 2 change per
`governance/CHANGE_CONTROL.md`):

```sh
python3 tools/build_journal.py
```

Essay SEO metadata (dek, description, keywords) lives in the `ESSAYS` list at the
top of the script. To add an essay: write `content/journal/<slug>.md`, add an
entry to `ESSAYS`, rerun, and update `content/journal/README.md`.

## build_og.py

Generates on-brand Open Graph share cards (1200×630 PNG) for every page.

- **Writes:** `assets/og/*.png` — one per root page (`home`, `thesis`,
  `buyer-fit`, `brand-potential`, `acquisition`, `journal`) and one per essay
  (`<slug>.png`).
- Imports the essay list from `build_journal.py`, so essay cards stay in sync
  with the Journal automatically.
- Cards are self-hosted and referenced by `og:image` / `twitter:image` meta.
  They are fetched by social crawlers only — never loaded into the page at
  runtime — so they stay within the no-external-dependency policy. Design follows
  `BRAND_ARCHITECTURE.md`: near-black ground, one serif voice, no people or
  imagery.
- **Dependency:** Pillow (`pip install Pillow`).

```sh
python3 tools/build_og.py     # after editing a title or adding an essay
```

Run order when adding an essay: `build_journal.py` first (it injects the
`og:image` path per essay), then `build_og.py` to render the matching card.
