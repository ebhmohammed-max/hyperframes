#!/usr/bin/env python3
"""
Channel identity for THE LONG NIGHT — a hybrid history channel.

The channel is not a Valyria channel, so the mark is not a Valyria prop. The name is the
point where the world's cold half and hot half meet, and the identity is built on that:

  the type is cut in two at the same place   |THE LONG| (cold)  |NIGHT| (fire)
  one ember hairline falls through the cut   - the only warm line in a cold field
  the palette is two-ended                   - pale glacial for the cold, ember for the fire

That means the mark works for a Valyria film and equally for a northern one: it never
shows a dragon, a pyramid or a person. It is type, a cut, and a light.

Outputs -> renders/channel_ln/
  logo_800x800.png            channel avatar, safe at 98 px
  logo_preview_sizes.png      the avatar at 98 / 64 / 40 / 24 px, to check legibility
  banner_thelongnight_2048x1152.jpg   banner, 1546x423 safe strip respected
  banner_safe_area_check.png  the same banner with the crop guides drawn on
  banner_mobile_crop.jpg      what a phone actually shows
  mark_dark.png / mark_light.png      the wordmark on basalt and on parchment
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[2]
EP = ROOT / "projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria"
IMAGES = EP / "documentary_v2/assets/images"
OUT = ROOT / "renders/channel_ln"

# ---------------------------------------------------------------- palette
BASALT = (7, 7, 10)
BASALT_SOFT = (14, 15, 20)
GLACIAL = (216, 228, 236)      # cold side of the wordmark
PALE = (242, 234, 217)         # parchment, for body type
EMBER = (215, 138, 60)         # the fire, and the single hairline
EMBER_HOT = (240, 176, 99)
FROST = (168, 198, 216)        # cold accent for rules on light grounds

DISPLAY = "/tmp/PlayfairDisplay.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"


def font(size: int, path: str = DISPLAY) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def tracked_w(d: ImageDraw.ImageDraw, text: str, f, tracking: float) -> float:
    return sum(d.textlength(c, font=f) for c in text) + tracking * max(0, len(text) - 1)


def tracked(d, xy, text, f, fill, tracking=0.0):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=f, fill=fill)
        x += d.textlength(ch, font=f) + tracking
    return x


def plate(name: str, size, dark: float = 1.0, desat: float = 1.0) -> Image.Image:
    im = Image.open(IMAGES / f"{name}.jpg").convert("RGB")
    sw, sh = im.size
    tw, th = size
    s = max(tw / sw, th / sh)
    im = im.resize((int(sw * s + 1), int(sh * s + 1)), Image.LANCZOS)
    x, y = (im.width - tw) // 2, (im.height - th) // 2
    im = im.crop((x, y, x + tw, y + th))
    if desat != 1.0:
        im = ImageEnhance.Color(im).enhance(desat)
    if dark != 1.0:
        im = ImageEnhance.Brightness(im).enhance(dark)
    return im


def vignette(im: Image.Image, strength: float = 0.6) -> Image.Image:
    w, h = im.size
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).ellipse([-w * .28, -h * .38, w * 1.28, h * 1.38], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(w // 8))
    dim = Image.new("RGB", (w, h), (4, 4, 7))
    return Image.composite(im, Image.blend(im, dim, strength), mask)


# ---------------------------------------------------------------- the mark

def draw_mark(im: Image.Image, cx: int, cy: int, size: int,
              kind: str = "lockup", hairline: bool = True) -> None:
    """Draw the two-part wordmark centred on (cx, cy), `size` tall per line.

    kind: "lockup"  — THE LONG over NIGHT, stacked
          "inline"  — THE LONG NIGHT on one line
          "initial" — a cut N, for the avatar
    """
    d = ImageDraw.Draw(im)

    if kind == "initial":
        # The mark: an eclipse. A cold disc and a warm disc of equal size sit inside one
        # another, offset, and the overlap is knocked back to the ground. What survives is
        # a crescent of ice on the left and a ring of fire on the right, both opening
        # around the same dark centre. Two worlds, one night, nothing drawn that belongs
        # to only one of them — and only three shapes, so it still reads at 24 px.
        r = size * 0.54
        off = size * 0.15
        lx, rx = cx - off, cx + off

        cold = Image.new("L", im.size, 0)
        ImageDraw.Draw(cold).ellipse([lx - r, cy - r, lx + r, cy + r], fill=255)
        warm = Image.new("L", im.size, 0)
        ImageDraw.Draw(warm).ellipse([rx - r, cy - r, rx + r, cy + r], fill=255)

        # Two crescents of equal weight, opening away from each other around one dark
        # centre: ice on the left limb, fire on the right. The overlap is nothing, so the
        # night sits between them and the mark holds its shape down to 24 px.
        im.paste(Image.new("RGB", im.size, GLACIAL), (0, 0), ImageChops.subtract(cold, warm))
        im.paste(Image.new("RGB", im.size, EMBER), (0, 0), ImageChops.subtract(warm, cold))
        return

    if kind == "inline":
        f = font(size)
        gap = size * 0.34
        w1 = tracked_w(d, "THE LONG", f, size * 0.02)
        w2 = tracked_w(d, "NIGHT", f, size * 0.02)
        total = w1 + gap + w2
        x = cx - total / 2
        y = cy - size * 0.62
        tracked(d, (x, y), "THE LONG", f, GLACIAL, size * 0.02)
        x2 = x + w1 + gap
        tracked(d, (x2, y), "NIGHT", f, EMBER_HOT, size * 0.02)
        if hairline:
            hy = y + size * 1.02
            d.rectangle([cx - total * 0.30, hy, cx + total * 0.30, hy + max(3, size // 70)],
                        fill=EMBER)
        return

    # stacked lockup: THE LONG (cold) over NIGHT (fire)
    f = font(size)
    fk = font(max(13, int(size * 0.22)), MONO)
    tr = size * 0.055
    w1 = tracked_w(d, "THE LONG", f, tr)
    w2 = tracked_w(d, "NIGHT", f, tr)
    block_w = max(w1, w2)

    y1 = cy - size * 1.06
    tracked(d, (cx - w1 / 2, y1), "THE LONG", f, GLACIAL, tr)
    y2 = y1 + size * 1.16
    tracked(d, (cx - w2 / 2, y2), "NIGHT", f, EMBER_HOT, tr)

    if hairline:
        hy = y1 + size * 1.02
        d.rectangle([cx - block_w * 0.62, hy, cx + block_w * 0.62, hy + max(2, size // 90)],
                    fill=EMBER)

    # the half-line over the mark: one word each side, which is the whole idea
    ky = y1 - size * 0.30
    small = max(12, int(size * 0.155))
    fks = font(small, MONO)
    left, right = "ICE", "FIRE"
    lw = tracked_w(d, left, fks, small * 0.34)
    rw = tracked_w(d, right, fks, small * 0.34)
    tracked(d, (cx - block_w * 0.50, ky), left, fks, FROST, small * 0.34)
    tracked(d, (cx + block_w * 0.50 - rw, ky), right, fks, EMBER, small * 0.34)
    _ = fk, lw


# ---------------------------------------------------------------- outputs

def logo() -> None:
    S = 800
    im = Image.new("RGB", (S, S), BASALT)
    # a whisper of ground: a cold gradient at the top, warmth at the foot
    g = Image.new("RGB", (S, S), BASALT)
    gd = ImageDraw.Draw(g)
    for i in range(S):
        t = i / S
        cold = int(16 * (1 - t) ** 2)
        warm = int(15 * t ** 3)
        gd.line([(0, i), (S, i)], fill=(7 + cold, 7 + cold + warm // 3, 10 + cold + warm))
    im = g

    draw_mark(im, S // 2, int(S * 0.46), 250, kind="initial")
    # the name, small, under the initial, so the avatar is readable even if it never
    # gets the banner for context
    d = ImageDraw.Draw(im)
    f = font(64)
    tr = 4
    w = tracked_w(d, "THE LONG NIGHT", f, tr)
    tracked(d, ((S - w) / 2, int(S * 0.755)), "THE LONG NIGHT", f, PALE, tr)
    d.rectangle([S / 2 - 96, int(S * 0.885), S / 2 + 96, int(S * 0.885) + 4], fill=EMBER)

    im.save(OUT / "logo_800x800.png")

    # legibility at the sizes it is really seen
    sizes = [98, 64, 40, 24]
    pad = 22
    strip = Image.new("RGB", (sum(sizes) + pad * (len(sizes) + 1), 98 + pad * 2), (22, 22, 26))
    x = pad
    for s in sizes:
        strip.paste(im.resize((s, s), Image.LANCZOS), (x, pad))
        x += s + pad
    strip.save(OUT / "logo_preview_sizes.png")


def banner() -> None:
    W, H = 2048, 1152
    half = W // 2

    # Two landscapes, not two scenes: a frozen valley at night on the left, a fire
    # mountain at dusk on the right. Both are landform only — no figure, no monument, no
    # prop — so the channel never looks like it belongs to one episode. Their horizons
    # meet, which is what lets the seam join them rather than cut them.
    cold = plate("0049", (half, H), dark=0.52, desat=0.30)
    warm = plate("0176", (half, H), dark=0.58, desat=0.40)
    canvas = Image.new("RGB", (W, H))
    canvas.paste(cold, (0, 0))
    canvas.paste(warm, (half, 0))

    # push both plates down to weather, and leave a pool of night in the middle for type
    pool = Image.new("L", (W, H), 0)
    ImageDraw.Draw(pool).ellipse([-W * 0.30, -H * 0.42, W * 1.30, H * 1.42], fill=255)
    pool = pool.filter(ImageFilter.GaussianBlur(W // 10))
    canvas = Image.composite(canvas, Image.new("RGB", (W, H), (5, 5, 8)),
                             pool.point(lambda v: 255 - int(v * 0.55)))

    # a cool cast on the left and an ember cast on the right, so the two ends stay legible
    cmask = Image.new("L", (W, H), 0)
    cd = ImageDraw.Draw(cmask)
    for i in range(W):
        cd.line([(i, 0), (i, H)], fill=int(120 * max(0.0, 1 - i / (W * 0.52)) ** 1.5))
    canvas = Image.composite(Image.new("RGB", (W, H), (40, 78, 116)), canvas, cmask)
    wmask = Image.new("L", (W, H), 0)
    wd2 = ImageDraw.Draw(wmask)
    for i in range(W):
        wd2.line([(i, 0), (i, H)], fill=int(128 * max(0.0, (i - W * 0.48) / (W * 0.52)) ** 1.5))
    canvas = Image.composite(Image.new("RGB", (W, H), (126, 68, 24)), canvas, wmask)
    canvas = vignette(canvas, 0.5)

    # the seam: soft, and marked by a single ember hairline so it reads as intended
    d = ImageDraw.Draw(canvas)
    d.rectangle([half - 1, 0, half + 1, H], fill=(24, 18, 14))

    sx0, sy0 = (W - 1546) // 2, (H - 423) // 2
    draw_mark(canvas, W // 2, sy0 + 423 // 2 + 2, 126, kind="lockup")

    canvas.save(OUT / "banner_thelongnight_2048x1152.jpg", quality=93)

    proof = canvas.copy()
    pdw = ImageDraw.Draw(proof)
    pdw.rectangle([sx0, sy0, sx0 + 1546, sy0 + 423], outline=(90, 210, 140), width=3)
    pdw.text((sx0 + 10, sy0 + 8), "SAFE 1546x423", font=font(26), fill=(90, 210, 140))
    proof.save(OUT / "banner_safe_area_check.png")

    mw, mh = 1235, 338
    mx, my = (W - mw) // 2, (H - mh) // 2
    canvas.crop((mx, my, mx + mw, my + mh)).save(OUT / "banner_mobile_crop.jpg", quality=92)


def wordmarks() -> None:
    for name, ground, cold, warm in (
        ("mark_dark.png", BASALT, GLACIAL, EMBER_HOT),
        ("mark_light.png", (238, 234, 224), (58, 74, 86), (150, 84, 28)),
    ):
        W, H = 1600, 620
        im = Image.new("RGB", (W, H), ground)
        d = ImageDraw.Draw(im)
        f = font(150)
        tr = 8
        w1 = tracked_w(d, "THE LONG", f, tr)
        w2 = tracked_w(d, "NIGHT", f, tr)
        y1 = 150
        tracked(d, ((W - w1) / 2, y1), "THE LONG", f, cold, tr)
        tracked(d, ((W - w2) / 2, y1 + 172), "NIGHT", f, warm, tr)
        bw = max(w1, w2)
        d.rectangle([W / 2 - bw * 0.62, y1 + 152, W / 2 + bw * 0.62, y1 + 156],
                    fill=EMBER if ground == BASALT else (196, 118, 52))
        im.save(OUT / name)


# ---------------------------------------------------------------- episode thumbnails

def _thumb(canvas: Image.Image, kicker: str, lines: list[tuple[str, str]],
           foot: str, tag: str) -> Image.Image:
    """Compose type over a plate: mono kicker, big display lines, mono footer, ember rule."""
    W, H = canvas.size
    d = ImageDraw.Draw(canvas)

    # left scrim, so the type always has a ground whatever the plate does
    scrim = Image.new("L", (W, H), 0)
    sd = ImageDraw.Draw(scrim)
    for i in range(W):
        sd.line([(i, 0), (i, H)], fill=int(214 * max(0.0, 1 - i / (W * 0.78)) ** 1.1))
    canvas = Image.composite(Image.new("RGB", (W, H), (5, 5, 8)), canvas, scrim)
    d = ImageDraw.Draw(canvas)

    x = 76
    fk = font(34, MONO)
    tracked(d, (x, 70), kicker, fk, FROST, 5)
    d.rectangle([x, 124, x + 74, 128], fill=EMBER)

    y = 210
    for text, colour in lines:
        f = font(104)
        tracked(d, (x, y), text, f, colour, 1)
        y += 118

    ff = font(32, MONO)
    tracked(d, (x, H - 104), foot, ff, (176, 184, 194), 4)

    # corner tag: ICE or FIRE, which is the channel's own grammar
    ft = font(30, MONO)
    tw = tracked_w(d, tag, ft, 5)
    tracked(d, (W - 76 - tw, 70), tag, ft, EMBER if tag == "FIRE" else FROST, 5)
    return canvas


def thumbnails() -> None:
    W, H = 1280, 720

    def bg(name: str, dark: float = 0.62, desat: float = 0.5) -> Image.Image:
        return plate(name, (W, H), dark=dark, desat=desat)

    # 01 — the film itself. Cold cliff to the left of frame, the freehold burning right.
    im = bg("0422", 0.60, 0.44)
    canvas = _thumb(im, "EPISODE ONE", [("THE RISE OF", GLACIAL), ("OLD VALYRIA", EMBER_HOT)],
                    "THE FULL 35-MINUTE DOCUMENTARY", "ICE")
    canvas.save(OUT / "thumb_ep01_rise_of_old_valyria.jpg", quality=92)

    # 02 — the question the film answers: who pays for a civilisation
    im = bg("0674", 0.58, 0.52)
    canvas = _thumb(im, "EPISODE TWO", [("WHO PAID", GLACIAL), ("FOR THE FIRE?", EMBER_HOT)],
                    "COMING NEXT", "FIRE")
    canvas.save(OUT / "thumb_template_who_paid.jpg", quality=92)

    # 03 — the missing secret, for the chapter that carries the film's turn
    im = bg("0121", 0.54, 0.46)
    canvas = _thumb(im, "CHAPTER FOUR", [("THE MISSING", GLACIAL), ("SECRET", EMBER_HOT)],
                    "THE FREEHOLD'S LAST SILENCE", "FIRE")
    canvas.save(OUT / "thumb_template_missing_secret.jpg", quality=92)

    # a contact sheet at the size YouTube really shows them
    sheet = Image.new("RGB", (3 * 400 + 4 * 24, 225 + 48), (18, 18, 22))
    xs = 24
    for n in ("thumb_ep01_rise_of_old_valyria", "thumb_template_who_paid",
              "thumb_template_missing_secret"):
        t = Image.open(OUT / f"{n}.jpg").resize((400, 225), Image.LANCZOS)
        sheet.paste(t, (xs, 24))
        xs += 424
    sheet.save(OUT / "PREVIEW_thumbs_400px.png")

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    logo()
    banner()
    wordmarks()
    thumbnails()
    print("written to", OUT)
    for p in sorted(OUT.iterdir()):
        print(" ", p.name, f"{p.stat().st_size // 1024} KB")
