#!/usr/bin/env python3
"""Generate on-brand Open Graph share cards (1200x630 PNG) for every page.
Self-hosted under assets/og/. No people, no imagery — the word is the image,
consistent with BRAND_ARCHITECTURE.md. Dependency: Pillow only."""
import os
from PIL import Image, ImageDraw, ImageFont
from build_journal import ESSAYS  # safe: build_journal guards its run under __main__

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets/og")
os.makedirs(OUT, exist_ok=True)

W, H = 1200, 630
M = 96                      # margin
GROUND = (6, 6, 8)
INK = (244, 243, 239)
DIM = (155, 154, 162)
FAINT = (86, 85, 93)
ACCENT = (233, 230, 221)
LINE = (34, 34, 40)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"


def font(size):
    return ImageFont.truetype(SERIF, size)


def tracked_width(d, text, f, tr):
    if not text:
        return 0
    return sum(d.textlength(c, font=f) + tr for c in text) - tr


def draw_tracked(d, xy, text, f, fill, tr):
    x, y = xy
    for c in text:
        d.text((x, y), c, font=f, fill=fill)
        x += d.textlength(c, font=f) + tr


def wrap(d, text, f, maxw):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit_title(d, text, maxw, avail_h, sizes=(84, 76, 68, 60, 54, 48, 42)):
    """Largest size whose wrap fits <=4 lines and inside avail_h."""
    for s in sizes:
        f = font(s)
        lines = wrap(d, text, f, maxw)
        lh = int(s * 1.18)
        if len(lines) <= 4 and len(lines) * lh <= avail_h:
            return f, lines, s, lh
    s = sizes[-1]
    f = font(s)
    return f, wrap(d, text, f, maxw), s, int(s * 1.18)


def card(path, eyebrow, title, right_label):
    img = Image.new("RGB", (W, H), GROUND)
    d = ImageDraw.Draw(img)
    maxw = W - 2 * M

    # top-left mark + hairline
    draw_tracked(d, (M, 90), "SPIRIT TRAINERS", font(26), DIM, 6)
    d.line([(M, 142), (M + 300, 142)], fill=LINE, width=1)

    # eyebrow (tracked, faint) + short accent rule
    eb_y = 198
    draw_tracked(d, (M, eb_y), eyebrow.upper(), font(24), FAINT, 5)
    d.line([(M, eb_y + 42), (M + 54, eb_y + 42)], fill=ACCENT, width=2)

    # title band, vertically centered within it
    band_top, band_bottom = 284, 476
    avail_h = band_bottom - band_top
    tf, lines, size, lh = fit_title(d, title, maxw, avail_h)
    block_h = len(lines) * lh
    ty = band_top + max(0, (avail_h - block_h) // 2)
    for ln in lines:
        d.text((M, ty), ln, font=tf, fill=INK)
        ty += lh

    # bottom rule + footer row
    foot_f = font(26)
    by = H - M - 6
    d.line([(M, by - 34), (W - M, by - 34)], fill=LINE, width=1)
    d.text((M, by), "spirittrainers.com", font=foot_f, fill=DIM)
    rw = d.textlength(right_label, font=foot_f)
    d.text((W - M - rw, by), right_label, font=foot_f, fill=FAINT)

    img.save(path, "PNG", optimize=True)
    return os.path.basename(path)


PAGES = [
    ("home", "A category asset", "Training the human spirit is becoming infrastructure.", "A category asset"),
    ("thesis", "The Thesis", "The activity is ancient. The name is missing.", "A category asset"),
    ("buyer-fit", "Buyer Fit", "Who could own this category?", "A category asset"),
    ("brand-potential", "Brand Potential", "The name behaves like an institution.", "A category asset"),
    ("acquisition", "Acquisition", "Acquire the category.", "A category asset"),
    ("journal", "The Journal", "Essays on names, categories, and positioning.", "Spirit Trainers Journal"),
]


def main():
    made = []
    for name, eb, title, right in PAGES:
        made.append(card(os.path.join(OUT, name + ".png"), eb, title, right))
    for e in ESSAYS:
        made.append(card(os.path.join(OUT, e["slug"] + ".png"),
                         f"Journal · Essay {e['n']:02d}", e["title"],
                         "Spirit Trainers Journal"))
    print(f"wrote {len(made)} OG cards into assets/og/")


if __name__ == "__main__":
    main()
