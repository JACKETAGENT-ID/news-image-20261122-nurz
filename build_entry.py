#!/usr/bin/env python3
"""Draw entry.png: a classic broadsheet front page summing up
Sunday, 22 November 2026. Black ink on off-white paper, one dark-red accent.
Run: python3 build_entry.py  -> writes entry.png (1024x1024) next to this file."""

import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (17, 17, 17)
RED = (139, 26, 26)
GREY = (90, 86, 78)
CLOUD = (70, 72, 78)
RAIN = (110, 120, 135)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def center(draw, y, text, fnt, fill, x0=0, x1=W):
    w = draw.textlength(text, font=fnt)
    draw.text(((x0 + x1 - w) / 2, y), text, font=fnt, fill=fill)


def rule(draw, y, x0=36, x1=988, fill=INK, width=2):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- Masthead ----
rule(d, 26, width=4)
center(d, 40, "THE WORLD IN ONE DAY", SERIF_B(64), INK)
center(d, 118, "S U N D A Y ,  2 2  N O V E M B E R  2 0 2 6", SANS_B(24), RED)
rule(d, 158, width=4)
rule(d, 164, width=1)

# ---- Lead story ----
d.text((36, 180), "LEAD STORY  —  GAZA", font=SANS_B(20), fill=RED)
d.text((36, 208), "OPEN THE GATES", font=SERIF_B(56), fill=INK)
d.text((36, 270), "FOR GAZA AID", font=SERIF_B(56), fill=INK)
deck = ("Australia, Canada, Italy and Britain urged Israel to open aid "
        "access to Gaza, where floods have swamped shelters and cut off "
        "supplies for families already living through war.")
y = 340
for line in wrap(d, deck, SERIF(25), 952):
    d.text((36, y), line, font=SERIF(25), fill=INK)
    y += 32

# ---- Lead illustration: rain over Gaza, aid trucks on a flooded road ----
ix0, iy0, ix1, iy1 = 36, 452, 988, 566
d.rectangle([ix0, iy0, ix1, iy1], outline=INK, width=2)
d.rectangle([ix0 + 2, iy0 + 2, ix1 - 2, iy0 + 40], fill=(214, 212, 204))
for cx, cy, r in [(180, 472, 30), (240, 468, 38), (470, 472, 34),
                  (540, 468, 40), (800, 472, 36), (860, 468, 30)]:
    d.ellipse([cx - r, cy - r // 2, cx + r, cy + r // 2], fill=CLOUD)
for rx in range(ix0 + 20, ix1 - 10, 26):
    d.line([(rx, iy0 + 46), (rx - 8, iy0 + 68)], fill=RAIN, width=2)
d.rectangle([ix0 + 2, iy1 - 30, ix1 - 2, iy1 - 2], fill=(176, 188, 200))
d.line([(ix0 + 2, iy1 - 30), (ix1 - 2, iy1 - 30)], fill=INK, width=2)
for tx in (120, 430, 730):
    d.rectangle([tx, iy1 - 72, tx + 120, iy1 - 32], fill=(232, 228, 216),
                outline=INK, width=2)
    d.rectangle([tx + 84, iy1 - 60, tx + 120, iy1 - 32], fill=RED)
    d.rectangle([tx + 96, iy1 - 54, tx + 110, iy1 - 42], fill=PAPER)
    d.ellipse([tx + 14, iy1 - 40, tx + 34, iy1 - 20], fill=INK)
    d.ellipse([tx + 82, iy1 - 40, tx + 102, iy1 - 20], fill=INK)
    d.text((tx + 8, iy1 - 66), "AID", font=SANS_B(15), fill=INK)

rule(d, 586, width=3)

# ---- Five more stories: kicker + headline on one line, one-line body ----
stories = [
    ("BAHRAIN",
     "Iran strike hits Bahrain industry",
     "An Iranian strike hit an industrial facility in Bahrain, shaking the Gulf."),
    ("FRANCE",
     "Fourth weekend of cost-of-living protests",
     "France saw a fourth straight weekend of marches over the cost of living."),
    ("MEXICO",
     "Mexico captures \u2018El Chapo Isidro\u2019",
     "Mexican forces captured drug lord \u2018El Chapo Isidro\u2019, a blow to his cartel."),
    ("UNITED STATES",
     "Democrats take Congress in the midterms",
     "Democrats won Congress in the midterms, reshaping power in Washington."),
    ("TENNIS",
     "Alcaraz meets Zverev in the ATP final",
     "Carlos Alcaraz faces Alexander Zverev in the ATP final, the season\u2019s finale."),
]

y = 604
for i, (kicker, head, body) in enumerate(stories):
    kf = SANS_B(17)
    d.text((36, y), kicker, font=kf, fill=RED)
    hx = 36 + d.textlength(kicker, font=kf) + 16
    d.text((hx, y - 3), head, font=SERIF_B(25), fill=INK)
    d.text((36, y + 29), body, font=SERIF(20), fill=INK)
    if i < len(stories) - 1:
        rule(d, y + 60, fill=(200, 194, 180), width=1)
    y += 72

# ---- Footer ----
rule(d, 978, width=2)
center(d, 986, "ONE DAY \u2014 ONE PAGE \u2014 SUNDAY, 22 NOVEMBER 2026",
       SANS(15), GREY)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
img.save(out, "PNG", optimize=True)
print("wrote", out, os.path.getsize(out), "bytes")
