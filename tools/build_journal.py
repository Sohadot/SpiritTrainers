#!/usr/bin/env python3
"""Generate the site's Journal pages from the canonical markdown in
content/journal/. Self-contained output: no external deps, SEO + JSON-LD inline."""
import html, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "content/journal")
OUT = os.path.join(ROOT, "journal")  # site is served from the repo root
BASE = "https://spirittrainers.com"
os.makedirs(OUT, exist_ok=True)

# essay order + SEO metadata (dek = card subtitle, desc = meta description)
ESSAYS = [
    dict(slug="why-categories-need-names", n=1,
         title="Why Categories Need Names",
         dek="A name is an act of gathering: it turns a scatter of instances into a category people can join, study, and defend.",
         desc="Why a category is a word before it is a market — how a name gathers scattered practice into a category and becomes the coordinate system a market is measured in.",
         kw="category naming, category creation, naming strategy, brand category, positioning"),
    dict(slug="when-a-name-becomes-infrastructure", n=2,
         title="When a Name Becomes Infrastructure",
         dek="An entire market can run on a single phrase. Like good infrastructure, the word disappears from view precisely because everything depends on it.",
         desc="How a category name behaves like infrastructure — carrying a market's search, comparison, identity, and investment — and why owning that junction is worth more than a domain.",
         kw="category name, market infrastructure, naming, positioning, strategic domain, category ownership"),
    dict(slug="profession-vs-category", n=3,
         title="The Difference Between a Profession and a Category",
         dek="A profession is a role; a category is the space roles sit in. Confusing the two is the most common way people misjudge what a name is worth.",
         desc="Profession versus category: why a name that operates at category altitude is worth far more than a job title, and how to tell which altitude a phrase is at.",
         kw="profession vs category, category altitude, naming, positioning, brand strategy"),
    dict(slug="why-generic-brands-rarely-lead", n=4,
         title="Why Generic Brands Rarely Lead Categories",
         dek="The most descriptive name rarely wins. Category-leading names are not descriptions — they are compressed arguments about the space.",
         desc="Why generic, descriptive names rarely lead categories, and why the names that do are specific, ownable, and carry a non-obvious claim about the space.",
         kw="generic brand, category leader, naming strategy, descriptive name, positioning, brand naming"),
    dict(slug="the-linguistics-of-human-development", n=5,
         title="The Linguistics of Human Development",
         dek="Grit, resilience, readiness, character — a domain rich in specific words and empty of the one general word that would gather them.",
         desc="A linguistic reading of human development: the human interior as a lexical gap — abundant hyponyms, a missing hypernym — and what a true category name would be.",
         kw="linguistics of human development, lexical gap, hypernym, superordinate term, category name, resilience, character"),
    dict(slug="the-name-that-arrives-before-its-market", n=6,
         title="The Name That Arrives Before Its Market",
         dek="Some names arrive early enough to help decide what a category becomes — framing the space while its shape is still soft.",
         desc="How a name can precede its market: markets form around shared agreements made of language, so a well-placed name can frame a category while it is still forming.",
         kw="category naming, naming ahead of market, latent category, positioning, first mover naming, category framing"),
]
BY_SLUG = {e["slug"]: e for e in ESSAYS}
DATE = "2026-07-31"


def md_body_to_html(md):
    """Drop the H1 title, the italic byline, and rule lines; convert paragraphs."""
    lines = md.splitlines()
    # remove leading title (#), byline (*...*), and '---' rules
    body = []
    for ln in lines:
        s = ln.strip()
        if s.startswith("# "):
            continue
        if s == "---":
            continue
        if s.startswith("*Spirit Trainers Journal"):
            continue
        body.append(ln)
    text = "\n".join(body).strip()
    paras = re.split(r"\n\s*\n", text)
    out = []
    for p in paras:
        p = p.strip()
        if not p:
            continue
        p = html.escape(p)
        # inline: **strong** then *em* (escape already applied)
        p = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", p)
        p = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", p)
        p = p.replace("\n", " ")
        out.append(f"      <p>{p}</p>")
    return "\n".join(out)


NAV = '''  <header class="topbar">
    <a class="mark" href="../index.html">Spirit&nbsp;Trainers</a>
    <nav>
      <a href="../thesis.html">Thesis</a>
      <a href="../buyer-fit.html">Buyer&nbsp;Fit</a>
      <a href="../brand-potential.html">Brand</a>
      <a href="index.html"{jcur}>Journal</a>
      <a href="../acquisition.html">Acquire</a>
    </nav>
  </header>'''

FOOTER = '''  <footer>
    <span>Spirit Trainers</span>
    <span class="v">A category asset · v0.1.0</span>
    <a href="../acquisition.html">Acquire the category →</a>
  </footer>'''


def essay_page(e):
    url = f"{BASE}/journal/{e['slug']}.html"
    body = md_body_to_html(open(os.path.join(SRC, e["slug"] + ".md")).read())
    prev_next = ""
    idx = e["n"] - 1
    links = []
    if idx > 0:
        p = ESSAYS[idx - 1]
        links.append(f'<a class="backlink" href="{p["slug"]}.html">← {html.escape(p["title"])}</a>')
    links.append('<a class="backlink" href="index.html">All essays</a>')
    if idx < len(ESSAYS) - 1:
        nx = ESSAYS[idx + 1]
        links.append(f'<a class="backlink" href="{nx["slug"]}.html">{html.escape(nx["title"])} →</a>')
    prev_next = '\n        '.join(links)

    ld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": e["title"],
        "description": e["desc"],
        "articleSection": "Spirit Trainers Journal",
        "keywords": e["kw"],
        "url": url,
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "datePublished": DATE,
        "dateModified": DATE,
        "inLanguage": "en",
        "author": {"@type": "Organization", "name": "Spirit Trainers"},
        "publisher": {"@type": "Organization", "name": "Spirit Trainers"},
        "isPartOf": {"@type": "Blog", "name": "Spirit Trainers Journal",
                     "url": f"{BASE}/journal/"},
    }
    crumbs = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Spirit Trainers", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Journal", "item": BASE + "/journal/"},
            {"@type": "ListItem", "position": 3, "name": e["title"], "item": url},
        ],
    }
    t = html.escape(e["title"])
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{t} — Spirit Trainers Journal</title>
  <meta name="description" content="{html.escape(e['desc'])}" />
  <meta name="keywords" content="{html.escape(e['kw'])}" />
  <meta name="author" content="Spirit Trainers" />
  <meta name="color-scheme" content="dark" />
  <link rel="canonical" href="{url}" />
  <meta property="og:type" content="article" />
  <meta property="og:site_name" content="Spirit Trainers Journal" />
  <meta property="og:title" content="{t}" />
  <meta property="og:description" content="{html.escape(e['desc'])}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:locale" content="en" />
  <meta property="article:section" content="Spirit Trainers Journal" />
  <meta property="article:published_time" content="{DATE}" />
  <meta property="article:modified_time" content="{DATE}" />
  <meta name="twitter:card" content="summary" />
  <meta name="twitter:title" content="{t}" />
  <meta name="twitter:description" content="{html.escape(e['desc'])}" />
  <link rel="stylesheet" href="../assets/style.css" />
  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
  <script type="application/ld+json">{json.dumps(crumbs, ensure_ascii=False)}</script>
</head>
<body>
{NAV.format(jcur='')}

  <main>
    <article>
      <header class="essay-head wrap">
        <p class="eyebrow">Spirit Trainers Journal · Essay {e['n']:02d}</p>
        <h1>{t}</h1>
        <div class="byline">
          <span>On names &amp; categories</span>
          <time datetime="{DATE}">Spirit Trainers</time>
        </div>
        <div class="rule"></div>
      </header>

      <div class="prose wrap">
{body}
      </div>
    </article>

    <div class="essay-foot">
      <div class="wrap" style="display:flex;gap:1.4rem 2.4rem;flex-wrap:wrap;justify-content:space-between">
        {prev_next}
      </div>
    </div>
  </main>

{FOOTER}

  <script src="../assets/app.js"></script>
</body>
</html>
'''


def index_page():
    url = f"{BASE}/journal/"
    items = []
    for e in ESSAYS:
        items.append(
            f'''      <a href="{e['slug']}.html">
        <span class="n">Essay {e['n']:02d}</span>
        <h2>{html.escape(e['title'])}</h2>
        <p class="dek">{html.escape(e['dek'])}</p>
      </a>''')
    listing = "\n".join(items)
    ld = {
        "@context": "https://schema.org",
        "@type": "Blog",
        "name": "Spirit Trainers Journal",
        "description": "Reference essays on names, categories, and positioning — the forces a category asset turns on.",
        "url": url,
        "inLanguage": "en",
        "publisher": {"@type": "Organization", "name": "Spirit Trainers"},
        "blogPost": [
            {"@type": "BlogPosting", "headline": e["title"],
             "description": e["desc"], "url": f"{BASE}/journal/{e['slug']}.html",
             "datePublished": DATE}
            for e in ESSAYS
        ],
    }
    desc = ("Reference essays on names, categories, and positioning — why names "
            "constitute categories, when a name becomes infrastructure, and the "
            "linguistics of human development.")
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Journal — Spirit Trainers</title>
  <meta name="description" content="{html.escape(desc)}" />
  <meta name="keywords" content="category naming, naming strategy, positioning, category creation, lexical gap, brand category, human development" />
  <meta name="author" content="Spirit Trainers" />
  <meta name="color-scheme" content="dark" />
  <link rel="canonical" href="{url}" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Spirit Trainers Journal" />
  <meta property="og:title" content="Spirit Trainers Journal" />
  <meta property="og:description" content="{html.escape(desc)}" />
  <meta property="og:url" content="{url}" />
  <meta name="twitter:card" content="summary" />
  <link rel="stylesheet" href="../assets/style.css" />
  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
{NAV.format(jcur=' aria-current="page"')}

  <main>
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">The Journal</p>
        <h1>Essays on names, categories, and positioning.</h1>
        <p class="lede measure">Part of the thesis, not a side blog. Each essay develops one facet of a single idea: how a word becomes the identity of a category.</p>
      </div>
    </section>

    <section style="padding-top:0">
      <div class="wrap">
        <nav class="journal-list" aria-label="Journal essays">
{listing}
        </nav>
      </div>
    </section>
  </main>

{FOOTER}

  <script src="../assets/app.js"></script>
</body>
</html>
'''


for e in ESSAYS:
    open(os.path.join(OUT, e["slug"] + ".html"), "w").write(essay_page(e))
open(os.path.join(OUT, "index.html"), "w").write(index_page())
print("wrote", len(ESSAYS), "essay pages + index into journal/")

# ---- sitemap.xml + robots.txt ----
urls = [f"{BASE}/", f"{BASE}/thesis.html", f"{BASE}/buyer-fit.html",
        f"{BASE}/brand-potential.html", f"{BASE}/acquisition.html",
        f"{BASE}/journal/"] + [f"{BASE}/journal/{e['slug']}.html" for e in ESSAYS]
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    pr = "1.0" if u.endswith("/") and "journal" not in u else ("0.9" if u == f"{BASE}/journal/" else "0.7")
    sm.append(f"  <url><loc>{u}</loc><lastmod>{DATE}</lastmod><priority>{pr}</priority></url>")
sm.append("</urlset>")
open(os.path.join(ROOT, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
open(os.path.join(ROOT, "robots.txt"), "w").write(
    "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % BASE)
print("wrote sitemap.xml + robots.txt")
