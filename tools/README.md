# tools

Small, dependency-free build helpers. Nothing here runs at page-view time; the
site remains fully static (`governance/SECURITY_POLICY.md`).

## build_journal.py

Regenerates the site Journal from the canonical markdown.

- **Reads:** `content/journal/*.md` (the canonical essay source).
- **Writes:** `site/journal/index.html`, `site/journal/<slug>.html` (one per
  essay), plus `site/sitemap.xml` and `site/robots.txt`.
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
