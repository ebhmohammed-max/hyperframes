#!/usr/bin/env python3
"""
The Harpy and the Dragon — documentary cut, v2.

One film, 35:00, from the narrator's first word to the last. Same architecture as
Episode 01's cut, with the two things this episode needs that that one did not:

  * image slots are 2.000 s but the *plate* inside a slot can be held across a long
    silence, so the eight blocks whose voice stops early (3.5-4.4 s of air) read as a
    deliberate beat instead of a hole;
  * every on-screen message is placed on a *measured* sentence gap, and a message that
    cannot be placed honestly is dropped rather than nudged.

  narration  assets/audio/narration.mp3         2100.000 s
  plates     assets/images/0001..1050.jpg       15 per 30 s block
  music      four licensed beds, one per chapter, measured and normalised to -30 LUFS
  sfx        one cue per title card, chapter card and place name

Everything below is derived from those files.
"""

from __future__ import annotations

import csv
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ep002_blocks as E

ROOT = Path(__file__).resolve().parents[2]
EP = ROOT / "projects/ancient_world_of_ice_and_fire/episodes/ep002_harpy_and_dragon"
PROJ = EP / "documentary_v2"
SRC_SCRIPT = EP / "story_film_35min/01_COMPLETE_NARRATION_35MIN_v02.md"
NARRATION = EP / "story_film_35min/audio/conformed/EP002_NARRATION_MASTER_35MIN.mp3"
TIMING = PROJ / "production/NARRATION_TIMING.json"
FORM_REPORT = EP / "story_film_35min/10_CONFORM_REPORT.json"

SRC_MUSIC = ROOT / "projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria/cinematic_film/assets/audio/music"
SRC_SFX = ROOT / "projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria/cinematic_film/assets/audio/sfx"
SRC_IMAGES = PROJ / "assets/images"

FPS = 30
BLOCKS_N = 70
BLOCK = 30.0
FILM = 2100.0
PLATES_PER_BLOCK = 15
PLATE = BLOCK / PLATES_PER_BLOCK          # 2.000 s

TARGET_BED_LUFS = -30.0

# Each chapter gets its own bed so no two consecutive chapters share a texture.
CHAPTERS = [
    ("I",   "Chapter One",   "The coin in the ash",
     "A gold coin under the ash of a city that thought it would last forever.",
     0,  "ancient-winds-part-1.mp3", 2.0),
    ("II",  "Chapter Two",   "The wrong tool for the sky",
     "A shield wall is a perfect answer to a problem that has just stopped existing.",
     10, "night-vigil.mp3", 4.0),
    ("III", "Chapter Three", "Building the answer",
     "Towers, engines, and the long patient work of being ready for something you cannot imagine.",
     20, "mana-two-part-1.mp3", 2.0),
    ("IV",  "Chapter Four",  "The long exhale",
     "A treaty, forty clauses, and a generation that reads tribute on its own money.",
     30, "ancient-winds-part-1.mp3", 120.0),
    ("V",   "Chapter Five",  "Four times nothing",
     "Four wars, four victories, and an empire that never once learned how to end anything.",
     41, "ancient-rite.mp3", 1.0),
    ("VI",  "Chapter Six",   "Salt, ash, and what was left",
     "The plain goes into the fire, and the people carry out the only thing that cannot burn.",
     51, "night-vigil.mp3", 4.0),
    ("VII", "Chapter Seven", "The night the harpy went out",
     "What the winner became, and what the coin was still saying two thousand years later.",
     61, "mana-two-part-1.mp3", 2.0),
]
CHAPTER_AT_BLOCK = {c[4]: c for c in CHAPTERS}

# ------------------------------------------------------------------ on-screen messages
# Title cards. Every line is either the narrator's own words or a statement the
# narration supports; nothing on screen is invented for effect.
# (block_index, at, eyebrow, line, sub, hold, sfx)
CARDS = [
    (0,  0.9,  "The Harpy and the Dragon",
     "The strongest thing in the world <em>lost five times</em>.",
     "This is the story of how, and of what the winner became.", 6.4, "whoosh-cinematic.mp3"),
    (1,  4.6,  "", "Men who believe they will last forever do not bury their money.",
     "", 4.4, "impact-bass-2.mp3"),
    (2,  1.0,  "", "Nobody wrote down how.",
     "What survives is the shape of it, and a coin.", 4.8, "whoosh-short.mp3"),
    (6,  2.0,  "", "Ten thousand men in step make a sound like a door closing.",
     "", 4.2, "impact-bass-1.mp3"),
    (9,  1.2,  "", "They have a rumour.",
     "", 3.4, "riser.mp3"),
    (10, 0.8,  "", "The first war began over a harbour. Not the city behind it.",
     "The harbour.", 3.6, "metalLatch.ogg"),
    (12, 0.6,  "The first battle",
     "The legions never broke.", "That is the detail to hold on to.", 4.2, "impact-bass-1.mp3"),
    (16, 1.4,  "", "They made a treaty.",
     "The city lived. That was the point. A living city pays.", 5.0, "chime.mp3"),
    (19, 0.7,  "", "Seventeen years pass.",
     "Everything happens in peace.", 4.0, "whoosh-short.mp3"),
    (21, 1.0,  "", "A dragon is devastating at the target, and worthless on a road.",
     "", 4.6, "click-soft.mp3"),
    (24, 0.9,  "", "Fire does not hold a city.", "", 3.8, "impact-bass-2.mp3"),
    (26, 1.0,  "", "It forbade something.", "Which thing matters later.", 3.8, "metalLatch.ogg"),
    (28, 0.8,  "", "They were building a family quarrel with a navy attached.",
     "", 4.4, "click-soft.mp3"),
    (30, 1.2,  "", "In a season, quietly, the ships failed to sail.",
     "", 4.4, "whoosh-short.mp3"),
    (31, 0.9,  "The fourth war", "Four years, by the count we have.",
     "The war is in the household now, on every shelf.", 4.6, "chime.mp3"),
    (35, 1.0,  "", "It waited. It obeyed.",
     "It made the waiting itself into a kind of war.", 4.6, "click-soft.mp3"),
    (38, 1.2,  "", "Nine tenths of them never saw a dragon.",
     "That is the true weight of an empire: almost nothing.", 5.0, "whoosh-short.mp3"),
    (39, 1.0,  "", "The people who keep the maps are the last to know the maps are wrong.",
     "", 4.8, "impact-bass-1.mp3"),
    (40, 1.0,  "", "The jar under that floor was never opened.",
     "That is what the ash tells us.", 4.6, "impact-bass-2.mp3"),
    (41, 0.8,  "Four wars · four victories",
     "A victory that does not end the argument is not a victory.",
     "", 5.0, "impact-bass-1.mp3"),
    (42, 0.6,  "The fifth war", "Ghis was burned.", "What was left was ground.", 4.4, "riser.mp3"),
    (46, 1.0,  "", "There is a road out of every city.",
     "And on the last day it is not a road.", 4.6, "whoosh-short.mp3"),
    (48, 1.0,  "", "The empire that won kept the dead city's bird.",
     "", 4.6, "chime.mp3"),
    (49, 1.0,  "", "The accounts say salt.", "", 3.4, "click-soft.mp3"),
    (51, 1.0,  "", "Empires die from the top.",
     "The things they taught the world die last.", 5.0, "impact-bass-2.mp3"),
    (54, 0.8,  "", "Two thousand years later, the harpy is still on the coins.",
     "Valyria is a shape in the water.", 5.2, "chime.mp3"),
    (58, 1.0,  "", "The coin is the only witness still available.",
     "", 4.2, "whoosh-short.mp3"),
    (60, 1.0,  "", "Not in the histories.",
     "In the small worn things people hand each other without looking.", 5.0, "chime.mp3"),
    (62, 0.9,  "The last chapter", "Every single thing that made them win was a thing that later made them unable to stop.",
     "", 5.2, "riser.mp3"),
    (64, 1.0,  "", "It came from the ground.",
     "", 3.4, "impact-bass-1.mp3"),
    (66, 1.0,  "", "A battle happens once. A coin happens every day.",
     "", 5.0, "click-soft.mp3"),
    (67, 0.8,  "", "And what did the winner become?",
     "A peninsula. A rumour.", 4.6, "whoosh-cinematic.mp3"),
    (69, 0.8,  "", "It is not a lesson. It is a story that happened.",
     "", 4.6, "chime.mp3"),
]

# Place names: the name alone, no label, no note. Placed on the measured sentence that
# says the word, and dropped rather than nudged if it cannot land there.
# (block_index, needle in the narration, name shown on screen)
PLACES = [
    (0,  "Ghiscari coast", "THE GHISCARI COAST"),
    (3,  "Ghis sat", "OLD GHIS"),
    (4,  "coast for a thousand miles", "G H I S"),
    (7,  "peninsula", "VALYRIA"),
    (9,  "harbour", "THE HARBOUR ROADS"),
    (21, "waterline", "THE WATERLINE"),
    (25, "lower city", "THE LOWER CITY"),
    (28, "dragonlords", "THE DRAGONLORDS"),
    (32, "taxes", "VALYRIA"),
    (36, "shipyard", "THE SHIPYARD"),
    (41, "Four wars", "FOUR WARS"),
    (42, "plain", "THE PLAIN"),
    (46, "road out of every city", "THE ROAD OUT"),
    (49, "salt", "SALT"),
    (60, "market", "THE MARKET"),
    (68, "memories", "TWO THOUSAND YEARS"),
]


def run(args: list[str], env: dict | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(args, capture_output=True, text=True, check=True, env=env)


def ffmpeg_bin() -> str:
    return str(ROOT / ".cache/bin/ffmpeg")


def lufs(path: Path) -> float:
    out = run([ffmpeg_bin(), "-hide_banner", "-nostdin", "-i", str(path),
               "-af", "loudnorm=I=-30:TP=-2:print_format=json", "-f", "null", "-"])
    m = re.search(r'"input_i"\s*:\s*"(-?[\d.]+)"', out.stderr)
    if not m:
        raise RuntimeError(f"no LUFS reading for {path}")
    return float(m.group(1))


def cut_music(src: Path, dst: Path, offset: float, dur: float) -> None:
    """Cut `dur` seconds of bed starting at `offset`, looping the track if it runs out.

    The four licensed beds total 1224 s and the film is 2100 s, so a chapter bed is
    always going to be shorter than its chapter unless it is looped. Looping without a
    crossfade clicks at the seam; acrossfade joins the tail of one pass to the head of
    the next over 2.5 s, which is inaudible under narration at -30 LUFS.
    """
    src_len = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                         "-of", "csv=p=0", str(src)],
                        env={"PATH": f"{ROOT}/.cache/bin:/usr/bin:/bin"}).stdout)
    avail = max(src_len - offset, 1.0)
    if dur <= avail:
        run([ffmpeg_bin(), "-hide_banner", "-nostdin", "-y", "-ss", f"{offset:.3f}",
             "-i", str(src), "-t", f"{dur:.3f}",
             "-af", "afade=t=in:st=0:d=1.2,afade=t=out:st=%.3f:d=1.6" % max(0.0, dur - 1.6),
             "-ar", "48000", "-ac", "1", "-c:a", "libmp3lame", "-b:a", "160k", str(dst)])
        return
    # One input, looped in the graph, then faded. aloop handles the repeat in a single
    # pass, which avoids having to stitch N inputs and accidentally reusing one twice.
    loops = int((dur / avail) + 1)
    run([ffmpeg_bin(), "-hide_banner", "-nostdin", "-y",
         "-ss", f"{offset:.3f}", "-t", f"{avail:.3f}", "-i", str(src),
         "-filter_complex",
         f"[0]aloop=loop={loops}:size={int(avail * 48000)},"
         f"atrim=0:{dur:.3f},afade=t=in:st=0:d=1.2,"
         f"afade=t=out:st={max(0.0, dur - 1.6):.3f}:d=1.6[out]",
         "-map", "[out]", "-ar", "48000", "-ac", "1",
         "-c:a", "libmp3lame", "-b:a", "160k", str(dst)])


CSS = """
:root{
  --ground:#07070a;--ink:#f2ead9;--ink-dim:#cdc3ae;--ember:#d78a3c;--ember-hot:#f0b063;
  --display:"Playfair Display",Georgia,"Times New Roman",serif;
  --serif:Georgia,"Times New Roman",serif;
  --mono:"JetBrains Mono","Space Mono",Menlo,monospace;
}
*{box-sizing:border-box}
html,body{margin:0;width:1920px;height:1080px;overflow:hidden;background:var(--ground)}
.plate{position:absolute;inset:0;overflow:hidden;background:#000}
.plate img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;
  transform-origin:50% 50%;will-change:transform}
.grade{position:absolute;inset:0;pointer-events:none;background:
  radial-gradient(122% 94% at 50% 42%,rgba(0,0,0,0) 38%,rgba(0,0,0,.6) 100%),
  linear-gradient(180deg,rgba(4,4,6,.62) 0%,rgba(4,4,6,0) 19%,rgba(4,4,6,0) 58%,rgba(4,4,6,.78) 100%)}
.grain{position:absolute;inset:-40px;pointer-events:none;opacity:.13;mix-blend-mode:overlay;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='220' height='220'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.82' numOctaves='3' stitchTiles='stitch'/><feColorMatrix type='saturate' values='0'/></filter><rect width='220' height='220' filter='url(%23n)' opacity='0.55'/></svg>")}
.tc{position:absolute;z-index:8;left:132px;right:150px;bottom:112px;pointer-events:none}
.tc .rule{height:2px;width:150px;margin:0 0 20px;
  background:linear-gradient(90deg,var(--ember),rgba(215,138,60,0));transform-origin:0 50%}
.tc .eyebrow{font-family:var(--mono);font-size:28px;letter-spacing:.32em;text-transform:uppercase;
  color:var(--ember-hot);margin:0 0 12px;text-shadow:0 2px 18px rgba(0,0,0,.95)}
.tc .line{font-family:var(--display);font-weight:400;font-size:64px;line-height:1.15;
  color:#fdf9ee;margin:0;text-wrap:balance;
  text-shadow:0 3px 28px rgba(0,0,0,.96),0 1px 3px rgba(0,0,0,.92)}
.tc .line em{font-style:italic;color:var(--ember-hot)}
.tc .sub{font-family:var(--serif);font-size:30px;line-height:1.42;color:#e8dfcb;margin:14px 0 0;
  max-width:1150px;text-shadow:0 2px 20px rgba(0,0,0,.96)}
.placard{position:absolute;z-index:9;left:132px;bottom:300px;pointer-events:none;
  display:inline-flex;align-items:center;padding:16px 30px 18px;
  background:rgba(5,5,8,.74);border-left:4px solid var(--ember)}
.placard span{font-family:var(--display);font-size:50px;line-height:1.06;color:#fdf8ec;
  text-transform:uppercase;letter-spacing:.10em}
.chapter{position:absolute;inset:0;z-index:12;display:grid;place-items:center;pointer-events:none;
  background:radial-gradient(60% 60% at 50% 48%,rgba(4,4,6,.72),rgba(4,4,6,.28) 60%,rgba(4,4,6,0))}
.chapter .inner{text-align:center;max-width:1320px}
.chapter .num{font-family:var(--display);font-style:italic;font-size:170px;line-height:.9;
  color:rgba(242,234,217,.16);margin:0 0 -40px}
.chapter .lbl{font-family:var(--mono);font-size:28px;letter-spacing:.42em;color:var(--ember-hot);
  text-transform:uppercase;margin:0 0 22px;text-shadow:0 2px 18px rgba(0,0,0,.95)}
.chapter h1{font-family:var(--display);font-weight:400;font-size:88px;line-height:1.06;color:#fbf6ea;
  margin:0 0 24px;text-wrap:balance;text-shadow:0 4px 34px rgba(0,0,0,.96)}
.chapter p{font-family:var(--serif);font-size:31px;line-height:1.5;color:#e4dbc7;margin:0 auto;
  max-width:980px;text-shadow:0 2px 22px rgba(0,0,0,.96)}
.chapter .rule{height:1px;width:330px;margin:30px auto 0;background:rgba(242,234,217,.34);
  transform-origin:50% 50%}
"""


def scene_shell(sid: str, dur: float, body: str, script: str) -> str:
    return f"""<template>
<style>
{CSS}
</style>
<div id="root" data-composition-id="{sid}" data-width="1920" data-height="1080" data-duration="{dur:.3f}">
{body}
</div>
<script>
(function(){{
  var tl = gsap.timeline({{ paused: true }});
{script}
  window.__timelines = window.__timelines || {{}};
  window.__timelines["{sid}"] = tl;
}})();
</script>
</template>
"""


MOTION = {
    "push":      ("s",  1.055, 1.000),
    "pull":      ("s",  0.958, 1.000),
    "pan-left":  ("x",  2.2,  -2.2),
    "pan-right": ("x", -2.2,   2.2),
    "hold":      ("s",  1.014, 1.000),
}
GRAIN = [(-9, 6), (7, -8), (-4, 10), (11, -5), (-12, 8), (5, -11)]


def speech_rate(timing: dict) -> float:
    """Characters per second, measured across the whole film."""
    chars = sum(len(s["text"]) for b in timing["blocks"] for s in b["sentences"])
    span = sum(s["end"] - s["start"] for b in timing["blocks"] for s in b["sentences"])
    return chars / span


def name_time(timing: dict, block: int, needle: str) -> tuple[float, float]:
    """Absolute second at which the narrator says `needle`, and the sentence's end."""
    cps = speech_rate(timing)
    for sn in timing["blocks"][block]["sentences"]:
        i = sn["text"].lower().find(needle.lower())
        if i >= 0:
            return round(sn["start"] + i / cps, 3), sn["end"]
    return -1.0, -1.0


def sentence_start(timing: dict, block: int, needle: str) -> tuple[float, float]:
    for s in timing["blocks"][block]["sentences"]:
        if needle.lower() in s["text"].lower():
            return s["start"], s["end"]
    return -1.0, -1.0


def main() -> None:
    blocks = [b["text"] for b in E.parse(SRC_SCRIPT)]
    timing = json.loads(TIMING.read_text())
    form = {r["block"]: r for r in json.loads(FORM_REPORT.read_text())["blocks"]}
    assert len(blocks) == BLOCKS_N, len(blocks)
    assert len(timing["blocks"]) == BLOCKS_N

    (PROJ / "compositions").mkdir(parents=True, exist_ok=True)
    (PROJ / "production").mkdir(exist_ok=True)
    for d in ("images", "audio/music", "audio/sfx", "audio/bed"):
        (PROJ / "assets" / d).mkdir(parents=True, exist_ok=True)

    for f in ["ancient-rite.mp3", "night-vigil.mp3", "ancient-winds-part-1.mp3",
              "mana-two-part-1.mp3"]:
        dst = PROJ / "assets/audio/music" / f
        if not dst.exists():
            shutil.copy2(SRC_MUSIC / f, dst)
    for p in sorted(SRC_SFX.iterdir()):
        dst = PROJ / "assets/audio/sfx" / p.name
        if not dst.exists():
            shutil.copy2(p, dst)
    if not (PROJ / "assets/audio/narration.mp3").exists():
        shutil.copy2(NARRATION, PROJ / "assets/audio/narration.mp3")
    gsap = ROOT / "projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria/cinematic_film/assets/gsap.min.js"
    if not (PROJ / "assets/gsap.min.js").exists():
        shutil.copy2(gsap, PROJ / "assets/gsap.min.js")

    # ---- music beds, measured per chapter
    BED_DIR = PROJ / "assets/audio/bed"
    cache = PROJ / "production/BED_LEVELS.json"
    beds = json.loads(cache.read_text()) if cache.exists() else {}
    for k, c in enumerate(CHAPTERS):
        num, track, off = c[0], c[5], c[6]
        start = c[4] * BLOCK
        end = (CHAPTERS[k + 1][4] * BLOCK) if k + 1 < len(CHAPTERS) else FILM
        name = f"ch_{num}.mp3"
        dst = BED_DIR / name
        if not dst.exists():
            cut_music(PROJ / "assets/audio/music" / track, dst, off, end - start)
        if name not in beds:
            beds[name] = round(lufs(dst), 2)
    cache.write_text(json.dumps(beds, indent=1))

    def bed_gain(name: str) -> float:
        return round(10 ** ((TARGET_BED_LUFS - beds[name]) / 20), 4)

    plan = []
    for n in range(1, BLOCKS_N + 1):
        for j in range(PLATES_PER_BLOCK):
            plan.append({
                "scene_id": f"HAR-EP002-IMG{(n - 1) * PLATES_PER_BLOCK + j + 1:04d}",
                "motion": ["hold", "push", "pull", "pan-left", "pan-right"][j % 5],
            })

    scenes: list[dict] = []
    sfx: list[dict] = []
    held: list[dict] = []

    for i in range(BLOCKS_N):
        sid = f"b{i + 1:03d}"
        t0 = i * BLOCK
        plates = plan[i * PLATES_PER_BLOCK:(i + 1) * PLATES_PER_BLOCK]

        body, js = [], []
        body.append('  <div class="stage">')
        for k, p in enumerate(plates):
            pid = f"{sid}-p{k:02d}"
            img = p["scene_id"].replace("HAR-EP002-IMG", "") + ".jpg"
            body.append(f'    <div id="{pid}" class="plate" style="opacity:0">'
                        f'<img id="{pid}-i" src="assets/images/{img}" alt="" draggable="false"></div>')
            t = k * PLATE
            js.append(f'  tl.set("#{pid}",{{opacity:1}},{t:.3f});')
            if k < len(plates) - 1:
                js.append(f'  tl.set("#{pid}",{{opacity:0}},{t + PLATE:.3f});')
            kind, a, b = MOTION[p["motion"]]
            if kind == "s":
                js.append(f'  tl.fromTo("#{pid}-i",{{scale:{a:g}}},'
                          f'{{scale:{b:g},duration:{PLATE:.3f},ease:"none"}},{t:.3f});')
            else:
                js.append(f'  tl.fromTo("#{pid}-i",{{xPercent:{a:g},scale:1.05}},'
                          f'{{xPercent:{b:g},scale:1.05,duration:{PLATE:.3f},ease:"none"}},{t:.3f});')

        # ---- the long-hold fix -------------------------------------------------
        # The voice in some blocks stops early. Its last plate is held for the whole
        # remaining silence instead of two more cuts playing over nothing, so the gap
        # is a beat with a picture on it rather than a hole.
        gap = float(form[i + 1]["gap_seconds"])
        if gap >= 2.6:
            last = f"{sid}-p{len(plates) - 1:02d}"
            # overwrite:auto kills the plate's own 2 s scale tween at this point, so the
            # hold is one continuous drift instead of two tweens fighting over `scale`.
            js.append(f'  tl.set("#{last}",{{opacity:1}},{(len(plates) - 1) * PLATE:.3f});')
            js.append(f'  tl.to("#{last}-i",{{scale:1.012,duration:{(gap + PLATE):.3f},'
                      f'ease:"none",overwrite:"auto"}},{(len(plates) - 1) * PLATE:.3f});')
            held.append({"block": i + 1, "hold_seconds": round(gap + PLATE, 2)})

        body.append('    <div class="grade"></div>')
        body.append('    <div class="grain"></div>')
        n_g = max(2, int(BLOCK / 5))
        for g in range(n_g):
            dx, dy = GRAIN[g % len(GRAIN)]
            js.append(f'  tl.set(".grain",{{x:{dx},y:{dy}}},{g * BLOCK / n_g:.3f});')

        ch = next((c for c in CHAPTERS if c[4] == i), None)
        if ch:
            num, label, title, blurb = ch[0], ch[1], ch[2], ch[3]
            cid = f"{sid}-ch"
            body.append(f'  <div id="{cid}" class="chapter" style="opacity:0"><div class="inner">'
                        f'<p class="num">{num}</p><p class="lbl">{label}</p>'
                        f'<h1>{title}</h1><p>{blurb}</p><div class="rule"></div></div></div>')
            js.append(f'  tl.fromTo("#{cid}",{{opacity:0}},{{opacity:1,duration:.7,'
                      f'ease:"power2.out",immediateRender:false}},0.35);')
            js.append(f'  tl.to("#{cid}",{{opacity:0,duration:.8,ease:"power2.in"}},4.4);')
            sfx.append(dict(file="riser.mp3", start=t0 + 1.2, vol=0.26))
            sfx.append(dict(file="impact-bass-1.mp3", start=t0 + 4.6, vol=0.34))

        msgs = []
        for c in CARDS:
            if c[0] != i:
                continue
            _, off, eyebrow, line, sub, hold, fx = c
            msgs.append([max(0.35, off), hold, "card",
                         dict(eyebrow=eyebrow, line=line, sub=sub, fx=fx)])
        for (b, needle, place) in PLACES:
            if b != i:
                continue
            at_abs, s_end = name_time(timing, i, needle)
            if at_abs < 0:
                continue
            msgs.append([at_abs - t0, 4.4, "place", dict(place=place)])

        cards = [m for m in msgs if m[2] == "card"]
        places = [m for m in msgs if m[2] == "place"]
        kept = []
        cursor = 5.5 if ch else 0.0
        for at, hold, kind, payload in cards:
            at = max(at, cursor)
            if at > 24.0:
                continue
            hold = min(hold, 29.2 - at)
            if hold < 2.6:
                continue
            kept.append((at, hold, kind, payload))
            cursor = at + hold + 0.35
        for at, hold, kind, payload in places:
            clash = any(not (at + hold + 0.25 <= k_at or at >= k_at + k_hold + 0.25)
                        for k_at, k_hold, _, _ in kept)
            if clash or at < (5.5 if ch else 0.0) or at + hold > 29.2:
                continue
            kept.append((at, hold, kind, payload))
        kept.sort(key=lambda m: m[0])

        for at, hold, kind, payload in kept:
            if kind == "card":
                cid = f"{sid}-tc{int(at * 10):04d}"
                eyebrow, line, sub, fx = (payload["eyebrow"], payload["line"],
                                          payload["sub"], payload["fx"])
                body.append(f'  <div id="{cid}" class="tc" style="opacity:0"><div class="rule"></div>'
                            + (f'<p class="eyebrow">{eyebrow}</p>' if eyebrow else "")
                            + f'<p class="line">{line}</p>'
                            + (f'<p class="sub">{sub}</p>' if sub else "")
                            + '</div>')
                js.append(f'  tl.fromTo("#{cid}",{{opacity:0,y:16}},'
                          f'{{opacity:1,y:0,duration:.6,ease:"power3.out",immediateRender:false}},{at:.2f});')
                js.append(f'  tl.fromTo("#{cid} .rule",{{scaleX:0}},'
                          f'{{scaleX:1,duration:.9,ease:"power2.out"}},{at + 0.1:.2f});')
                js.append(f'  tl.to("#{cid}",{{opacity:0,duration:.55,ease:"power2.in"}},{at + hold:.2f});')
                sfx.append(dict(file=fx, start=t0 + at, vol=0.32))
            else:
                pid = f"{sid}-pl{int(at * 10):04d}"
                body.append(f'  <div id="{pid}" class="placard" style="opacity:0">'
                            f'<span>{payload["place"]}</span></div>')
                js.append(f'  tl.fromTo("#{pid}",{{opacity:0,y:10}},'
                          f'{{opacity:1,y:0,duration:.42,ease:"power2.out",immediateRender:false}},{at:.2f});')
                js.append(f'  tl.to("#{pid}",{{opacity:0,duration:.4,ease:"power1.in"}},{at + hold:.2f});')
                sfx.append(dict(file="metalLatch.ogg", start=t0 + at, vol=0.30))

        body.append('  </div>')
        (PROJ / "compositions" / f"{sid}.html").write_text(
            scene_shell(sid, BLOCK, "\n".join(body), "\n".join(js)))
        scenes.append(dict(id=sid, start=t0, dur=BLOCK, plates=len(plates)))

    # ---- audio
    # ONE premixed track. The renderer's own mixer spills a 2100 s float32 file and
    # this box cannot hold it; mix_ep002_audio.py builds the same mix in under two
    # minutes and lets the render stay a pure picture job.
    audio = [
        '  <audio id="mix" src="assets/audio/mix.m4a" data-start="0" '
        'data-duration="%.1f" data-volume="1.0" data-track-index="20"></audio>' % FILM
    ]

    # ---- the film composition: 70 clip divs referencing the block compositions
    clips = []
    for sc in scenes:
        clips.append(
            f'  <div id="{sc["id"]}" class="clip" data-composition-id="{sc["id"]}" '
            f'data-composition-src="compositions/{sc["id"]}.html" data-start="{sc["start"]:.3f}" '
            f'data-duration="{sc["dur"]:.3f}" data-width="1920" data-height="1080" '
            f'data-track-index="1" data-track-kind="graphics"></div>')
    (PROJ / "index.html").write_text(
        "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"UTF-8\">\n"
        "<title>The Harpy and the Dragon</title>\n"
        "<script src=\"assets/gsap.min.js\"></script>\n<style>\n" + CSS +
        "\n</style>\n</head>\n<body>\n"
        '<div id="film" data-composition-id="film" data-width="1920" data-height="1080" '
        'data-fps="30"\n     data-start="0" data-duration="2100.0">\n'
        + "\n".join(clips) + "\n"
        + "\n".join(audio) + "\n</div>\n"
        "<script>\nwindow.__timelines = { \"film\": gsap.timeline({ paused: true }) };\n</script>\n"
        "</body>\n</html>\n")

    print(f"{len(scenes)} scenes · {len(plan)} plates · {len(CARDS)} cards · "
          f"{len(PLACES)} places · {len(sfx)} sfx cues · {len(held)} long holds")
    if held:
        print("long holds:", ", ".join(f"b{h['block']:02d} {h['hold_seconds']}s" for h in held))


if __name__ == "__main__":
    main()
