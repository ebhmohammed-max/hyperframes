#!/usr/bin/env python3
"""
Channel artwork for Ancient World of Ice and Fire.

Everything is drawn from the film's own palette and the renderer's own bundled font, so
the channel page and the frames look like the same channel:

  basalt   #07070A      parchment #F2EAD9      ember #D78A3C

Outputs (renders/channel/):
  banner_2048x1152.jpg      channel banner, with the 1546x423 safe strip respected
  avatar_800x800.png        the numeral mark
  thumb_valyria_1280x720.jpg  template B — the land
  thumb_paid_1280x720.jpg     template A — the figure
  thumb_secret_1280x720.jpg   template C — the object
  PREVIEW_trio.png          all three thumbnails as they appear at 168x94
"""

from __future__ import annotations

import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[2]
EP = ROOT / "projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria"
IMAGES = EP / "documentary_v2/assets/images"
OUT = ROOT / "renders/channel"

BASALT = (7, 7, 10)
PARCH = (242, 234, 217)
EMBER = (215, 138, 60)
EMBER_HOT = (240, 176, 99)

DISPLAY = "/tmp/PlayfairDisplay.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(size: int, path: str = DISPLAY) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def plate(name: str, size: tuple[int, int], dark: float = 1.0) -> Image.Image:
    """A film plate, cover-cropped to size, optionally darkened."""
    im = Image.open(IMAGES / f"{name}.jpg").convert("RGB")
    sw, sh = im.size
    tw, th = size
    scale = max(tw / sw, th / sh)
    im = im.resize((int(sw * scale + 1), int(sh * scale + 1)), Image.LANCZOS)
    x = (im.width - tw) // 2
    y = (im.height - th) // 2
    im = im.crop((x, y, x + tw, y + th))
    if dark != 1.0:
        im = ImageEnhance.Brightness(im).enhance(dark)
    return im


def vignette(im: Image.Image, strength: float = 0.55) -> Image.Image:
    """Darken the edges so type always sits on something calm."""
    w, h = im.size
    mask = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(mask)
    d.ellipse([-w * 0.25, -h * 0.35, w * 1.25, h * 1.35], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(w // 8))
    dim = Image.new("RGB", (w, h), (4, 4, 6))
    return Image.composite(im, Image.blend(im, dim, strength), mask)


def rule(d: ImageDraw.ImageDraw, xy, length: int, width: int = 4, color=EMBER):
    x, y = xy
    d.rectangle([x, y, x + length, y + width], fill=color)


def tracked(d, xy, text, f, fill, tracking=0):
    """Draw text with letter-spacing; PIL has none, so advance per glyph."""
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=f, fill=fill)
        x += d.textlength(ch, font=f) + tracking
    return x


# ---------------------------------------------------------------- banner

def banner() -> None:
    W, H = 2048, 1152
    base = plate("0621", (W, H), dark=0.62)          # mountains, smoke, room on the left
    base = vignette(base, 0.6)
    im = base.copy()
    d = ImageDraw.Draw(im)

    # The safe strip YouTube guarantees on every device: 1546 x 423, centred.
    sx0 = (W - 1546) // 2
    sy0 = (H - 423) // 2
    sy1 = sy0 + 423

    # Type sits inside it, pinned to the lower half of the strip.
    f_kick = font(34, MONO)
    f_name = font(126)
    f_sub = font(44)

    x = sx0 + 40
    yb = sy1 - 40
    d.text((x, yb - 150), "", font=f_name, fill=PARCH)
    name_y = yb - 148

    tracked(d, (x, name_y - 62), "THE DEEP PAST, TOLD LIKE HISTORY", f_kick, EMBER_HOT, 5)
    d.text((x, name_y), "Ancient World", font=f_name, fill=PARCH)
    d.text((x, name_y + 128), "of Ice and Fire", font=f_name, fill=PARCH)
    rule(d, (x + 4, name_y + 300), 300)
    d.text((x + 4, name_y + 324), "DOCUMENTARY", font=font(38, MONO), fill=(206, 197, 178))

    im.save(OUT / "banner_2048x1152.jpg", quality=92)


# ---------------------------------------------------------------- avatar

def avatar() -> None:
    S = 800
    im = Image.new("RGB", (S, S), BASALT)
    d = ImageDraw.Draw(im)

    # numeral mark: the chapter numeral, italic, at 12% parchment, crossed by one ember rule
    f = ImageFont.truetype(DISPLAY, 520)
    txt = "I"
    tw = d.textlength(txt, font=f)
    d.text(((S - tw) / 2, S * 0.16), txt, font=f, fill=(60, 57, 51))
    d.rectangle([S * 0.22, S * 0.70, S * 0.78, S * 0.70 + 8], fill=EMBER)

    im.save(OUT / "avatar_800x800.png")

    # the same mark at sidebar size, to prove it survives
    im.resize((98, 98), Image.LANCZOS).save(OUT / "avatar_preview_98.png")


# ---------------------------------------------------------------- thumbnails

def thumb_land(name: str, out: str, title_lines: list[str], plate_id: str) -> None:
    """Template B: landscape full-bleed, title bottom-left on a basalt field."""
    W, H = 1280, 720
    im = plate(plate_id, (W, H), dark=0.72)
    im = vignette(im, 0.5)
    d = ImageDraw.Draw(im)

    # basalt field behind the title, so the words never fight the picture
    field_h = 210 if len(title_lines) == 1 else 290
    grad = Image.new("RGB", (W, field_h), BASALT)
    mask = Image.new("L", (W, field_h), 0)
    md = ImageDraw.Draw(mask)
    for i in range(field_h):
        md.line([(0, i), (W, i)], fill=int(240 * (i / field_h) ** 0.7))
    im.paste(grad, (0, H - field_h), mask)
    d = ImageDraw.Draw(im)

    f = font(96)
    y = H - field_h + 34
    for i, line in enumerate(title_lines):
        d.text((64, y + i * 104), line, font=f, fill=PARCH)
    rule(d, (66, y - 16), 132)
    im.save(OUT / out, quality=92)


def thumb_figure(out: str, title: str, plate_id: str, kicker: str) -> None:
    """Template A: one person, title top-left."""
    W, H = 1280, 720
    im = plate(plate_id, (W, H), dark=0.78)
    im = vignette(im, 0.45)
    d = ImageDraw.Draw(im)
    f = font(104)
    fk = font(34, MONO)
    tracked(d, (64, 58), kicker, fk, EMBER_HOT, 6)
    d.text((64, 108), title, font=f, fill=PARCH)
    rule(d, (66, 242), 150)
    im.save(OUT / out, quality=92)


def thumb_object(out: str, title: str, plate_id: str) -> None:
    """Template C: macro of the object, small centred title, hairline ember frame."""
    W, H = 1280, 720
    im = plate(plate_id, (W, H), dark=0.66)
    im = vignette(im, 0.62)
    d = ImageDraw.Draw(im)
    d.rectangle([40, 40, W - 40, H - 40], outline=EMBER, width=3)
    f = font(92)
    tw = d.textlength(title, font=f)
    d.text(((W - tw) / 2, H - 190), title, font=f, fill=PARCH)
    im.save(OUT / out, quality=92)


def trio() -> None:
    """Show all three at the size they are actually seen in a feed."""
    names = ["thumb_valyria_1280x720.jpg", "thumb_paid_1280x720.jpg",
             "thumb_secret_1280x720.jpg"]
    tw, th = 168, 94
    pad = 26
    im = Image.new("RGB", (tw * 3 + pad * 4, th + pad * 2 + 44), (24, 24, 28))
    d = ImageDraw.Draw(im)
    f = font(28, SANS)
    for i, n in enumerate(names):
        t = Image.open(OUT / n).resize((tw, th), Image.LANCZOS)
        x = pad + i * (tw + pad)
        im.paste(t, (x, pad))
        d.text((x, pad + th + 10), f"thumbnail {i + 1}", font=f, fill=(190, 186, 176))
    im.save(OUT / "PREVIEW_trio.png")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    banner()
    avatar()
    thumb_land("valyria", "thumb_valyria_1280x720.jpg",
               ["Rise of", "Old Valyria"], "0621")
    thumb_figure("thumb_paid_1280x720.jpg", "Who Paid?", "0800", "THE MINES")
    thumb_object("thumb_secret_1280x720.jpg", "The Missing Secret", "0561")
    trio()
    print("channel artwork written to", OUT)
    for p in sorted(OUT.iterdir()):
        print(" ", p.name, f"{p.stat().st_size // 1024} KB")
