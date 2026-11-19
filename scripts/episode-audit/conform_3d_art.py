#!/usr/bin/env python3
"""
Conform the generated 3D channel art to YouTube's specs.

The images come back at whatever aspect the generator likes (1024², 1376×768), so
this resamples and crops them to the exact banner and avatar sizes, respects the
1546×423 banner safe strip, and writes proofs at the sizes people actually see.

Outputs -> renders/channel_ln/gen/
  logo_youtube_800x800.png          channel avatar
  logo_youtube_sizes.png            the avatar at 98 / 64 / 40 / 24 px
  banner_youtube_2048x1152.jpg      banner
  banner_youtube_safe_check.png     the same, with the crop guides drawn on
  banner_youtube_mobile.jpg         what a phone shows
  banner_youtube_tv.jpg             what a TV shows
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "renders/channel_ln/gen"
OUT = SRC

MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"


def font(size):
    return ImageFont.truetype(MONO, size)


def cover(im: Image.Image, size: tuple[int, int], focus_y: float = 0.5) -> Image.Image:
    """Scale to cover the target and centre-crop; focus_y biases the vertical crop."""
    tw, th = size
    s = max(tw / im.width, th / im.height)
    im = im.resize((max(tw, int(im.width * s + 1)), max(th, int(im.height * s + 1))),
                   Image.LANCZOS)
    x = (im.width - tw) // 2
    y = int((im.height - th) * focus_y)
    return im.crop((x, y, x + tw, y + th))


def logo() -> Image.Image:
    im = Image.open(SRC / "logo_fantasy_v3.png").convert("RGB")
    # v3 is composed for the circular mask YouTube applies: the emblem is inset and the
    # wordmark is narrower than the ring, so a straight resize keeps everything inside it.
    out = im.resize((800, 800), Image.LANCZOS)
    out.save(OUT / "logo_youtube_800x800.png")

    sizes = [98, 64, 40, 24]
    pad = 22
    strip = Image.new("RGB", (sum(sizes) + pad * (len(sizes) + 1), 98 + pad * 2), (22, 22, 26))
    x = pad
    for s in sizes:
        strip.paste(out.resize((s, s), Image.LANCZOS), (x, pad))
        x += s + pad
    strip.save(OUT / "logo_youtube_sizes.png")

    # circular preview — how the avatar is actually masked
    for s in (160, 98):
        circ = Image.new("RGB", (s, s), (24, 24, 28))
        mask = Image.new("L", (s, s), 0)
        ImageDraw.Draw(mask).ellipse([0, 0, s - 1, s - 1], fill=255)
        circ.paste(out.resize((s, s), Image.LANCZOS), (0, 0), mask)
        circ.save(OUT / f"logo_circle_{s}.png")
    return out


def banner() -> Image.Image:
    im = Image.open(SRC / "banner_fantasy_v2.jpg").convert("RGB")
    W, H = 2048, 1152
    out = cover(im, (W, H), focus_y=0.5)

    # a gentle centre lift so the lettering stays crisp against the fog, plus a
    # little contrast — the render is soft by design, the title needs an edge
    out = ImageEnhance.Contrast(out).enhance(1.06)
    veil = Image.new("L", (W, H), 0)
    vd = ImageDraw.Draw(veil)
    for i in range(W):
        vd.line([(i, 0), (i, H)], fill=int(70 * max(0.0, 1 - abs(i - W / 2) / (W * 0.34)) ** 1.4))
    veil = veil.filter(ImageFilter.GaussianBlur(40))
    out = Image.composite(out, Image.new("RGB", (W, H), (4, 4, 7)), veil.point(lambda v: 255 - v))

    out.save(OUT / "banner_youtube_2048x1152.jpg", quality=94)

    sx0, sy0 = (W - 1546) // 2, (H - 423) // 2
    proof = out.copy()
    pd = ImageDraw.Draw(proof)
    pd.rectangle([sx0, sy0, sx0 + 1546, sy0 + 423], outline=(90, 210, 140), width=3)
    pd.text((sx0 + 12, sy0 + 10), "SAFE 1546x423  — all type must sit inside this",
            font=font(26), fill=(90, 210, 140))
    pd.rectangle([0, 0, W - 1, H - 1], outline=(90, 210, 140), width=3)
    pd.text((14, H - 40), "2048x1152", font=font(24), fill=(90, 210, 140))
    proof.save(OUT / "banner_youtube_safe_check.png")

    # what a phone shows, and what a TV shows
    for name, (mw, mh) in (("banner_youtube_mobile.jpg", (1235, 338)),
                           ("banner_youtube_tv.jpg", (1920, 1080))):
        mx, my = (W - mw) // 2, (H - mh) // 2
        out.crop((mx, my, mx + mw, my + mh)).save(OUT / name, quality=93)
    return out


if __name__ == "__main__":
    logo()
    banner()
    for p in sorted(OUT.glob("*youtube*")) + sorted(OUT.glob("*circle*")):
        im = Image.open(p)
        print(f"  {p.name:34s} {im.width}x{im.height}  {p.stat().st_size // 1024} KB")
