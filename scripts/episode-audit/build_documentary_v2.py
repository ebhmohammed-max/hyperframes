#!/usr/bin/env python3
"""
Rise of Old Valyria — documentary cut, v2.

One film, 35:00, from the narrator's first word to the last. No trailer, no sampler,
no black frames, no paper boards: the episode's own recorded narration over the
episode's own 1050-image shot plan, with transparent title cards, date/place
plaques, four music beds cut by chapter, and an effect on every on-screen message.

  narration  EP001_COMPLETE_NARRATION_35m00s_v01.mp3   2100.024 s
  plates     assets/images/0001..1050.jpg              15 per 30 s block, 2.000 s each
  music      ancient-rite / night-vigil / ancient-winds / mana-two, one per chapter
  sfx        one cue per title card, chapter card and place plaque

Everything below is derived from those files; production/SHOT_LIST.json is the record.
"""

from __future__ import annotations

import csv
import json
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EP = ROOT / "projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria"
PROJ = EP / "documentary_v2"
SRC_IMAGES = EP / "documentary_film/assets/images"
SRC_MUSIC = EP / "cinematic_film/assets/audio/music"
SRC_SFX = EP / "cinematic_film/assets/audio/sfx"
NARRATION = EP / "story_film_35min/audio/review/EP001_COMPLETE_NARRATION_35m00s_v01.mp3"
BLOCKS = EP / "story_film_35min/narration_blocks_v02.json"
TIMING = PROJ / "production/NARRATION_TIMING.json"
SHOT_PLAN = EP / "documentary_film/production/SHOT_PLAN.csv"

FPS = 30
BLOCKS_N = 70
BLOCK = 30.0
FILM = 2100.0
PLATES_PER_BLOCK = 15
PLATE = BLOCK / PLATES_PER_BLOCK          # 2.000 s

# ------------------------------------------------------------------ music plan
# One bed per chapter, cut from the four licensed tracks. Chapter boundaries are the
# narrator's own block boundaries. Bed gain is set from a measured target, not by ear.
# Measured: the voice alone sits near -19.6 LUFS in a chapter, and a bed at -30 LUFS
# lifts the mix by only ~0.25 LU, i.e. about 10 dB under the voice. Audible, subordinate.
TARGET_BED_LUFS = -30.0
CHAPTERS = [
    # (numeral, label, title, blurb, first block, track, offset into track)
    ("I",   "Chapter One",   "The Shepherds and the Mountain", "A flock below, a rider above, and the distance between them.", 0,  "ancient-rite.mp3", 0.0),
    ("II",  "Chapter Two",   "An Older Darkness",              "Before the Freehold, the Long Night — and the memories that outlived it.", 10, "night-vigil.mp3", 0.0),
    ("III", "Chapter Three", "The World Before Valyria",       "River cities, brick empires, and a continent that was never empty.", 20, "ancient-winds-part-1.mp3", 24.0),
    ("IV",  "Chapter Four",  "Beneath the Fourteen Flames",    "Green pasture, black rock, and what the mountain kept underneath.", 30, "night-vigil.mp3", 108.0),
    ("V",   "Chapter Five",  "The First Encounter",            "A climb, a cavern, and a creature that owed nobody obedience.", 41, "mana-two-part-1.mp3", 0.0),
    ("VI",  "Chapter Six",   "The Dragonlords",                "Blood, marriage, and the forty houses that answered to no king.", 51, "ancient-rite.mp3", 0.0),
    ("VII", "Chapter Seven", "The Price of the Freehold",      "Stone above, mines below, and the people who paid for both.", 61, "ancient-winds-part-1.mp3", 300.0),
]
CHAPTER_AT_BLOCK = {c[4]: c for c in CHAPTERS}

# ------------------------------------------------------------------ on-screen messages
# Title cards. Spoken under the narrator, transcribed from the narration itself, so the
# screen never asserts anything the voice does not say. (block, at-offset, eyebrow, line,
# sub, hold, sfx)
CARDS = [
    (0,  5.2, "Rise of Old Valyria", "How did the shepherds become <em>dragonlords</em>?",
     "And who paid for the world they built?", 5.2, "whoosh-cinematic.mp3"),
    (1,  1.0, "", "No chronicle gives us the first shepherd's name.",
     None, 4.0, "whoosh-short.mp3"),
    (1, 14.6, "", "First came discovery. Then the struggle to possess it.",
     None, 5.0, "whoosh-short.mp3"),
    (2,  1.2, "Dating the rise", "≈ 5,000 years before the Conquest",
     "Later histories place it here. The distance has blurred the count.", 5.6, "impact-bass-1.mp3"),
    (2, 17.0, "", "Beyond those fragile records: the Long Night.",
     None, 5.0, "whoosh-short.mp3"),
    (3,  1.4, "Along the Rhoyne", "A world waiting for the dawn",
     "Salvation remembered as voices joining against the night.", 5.0, "cloth1.ogg"),
    (4,  1.6, "Yi Ti", "The Blood Betrayal",
     "The Amethyst Empress, the Bloodstone Emperor, and a world cast into darkness.", 5.4, "impact-bass-2.mp3"),
    (5,  2.0, "", "The continent was not empty.",
     "It already held worlds of its own. Valyria began at their margins.", 5.4, "whoosh-short.mp3"),
    (6,  1.4, "Asshai", "Beside the River Ash",
     "Stone that seems to swallow light. Remember its name.", 5.0, "metalLatch.ogg"),
    (7,  1.4, "Old Ghis", "The harpy and the thunderbolt",
     "Brick pyramids above a civilization of conquest and wealth.", 5.0, "cloth1.ogg"),
    (8,  1.6, "Grazdan the Great", "The lockstep legions",
     "Many soldiers moving like one. And an economy built on slavery.", 5.2, "impact-bass-1.mp3"),
    (10, 1.2, "", "Before the Doom shattered it",
     "Coast, pasture and volcanic heights belonged to one country.", 5.0, "whoosh-short.mp3"),
    (11, 1.4, "The Fourteen Flames", "Ordinary lives beneath extraordinary forces",
     "The people below could not command those mountains.", 5.2, "cloth1.ogg"),
    (13, 1.6, "", "Another kind of wealth, under the pasture",
     "Gold and silver. Obsidian. And a price for entering.", 5.0, "whoosh-short.mp3"),
    (14, 1.4, "Firewyrms", "A country within a country",
     "Valyria's wealth rested above an underworld capable of killing.", 5.2, "impact-bass-2.mp3"),
    (15, 1.4, "", "Their story began with people, not gods.",
     "A flock to guide, a gate to mend, wool to prepare.", 5.2, "whoosh-short.mp3"),
    (16, 1.6, "", "Silver-gold hair, eyes in shades of purple",
     "A recognizable heritage — and a destiny later claimed for it.", 5.0, "cloth1.ogg"),
    (19, 1.6, "", "A herdsman climbs toward dark rock",
     "Somewhere within the Fourteen Flames, people met the creatures that would change the world.", 5.4, "whoosh-cinematic.mp3"),
    (21, 1.2, "", "A living creature in its own domain",
     "A cavern is shelter, not a stable.", 5.0, "whoosh-short.mp3"),
    (23, 1.2, "", "A predator they could neither fence out nor handle",
     "Danger before opportunity.", 5.0, "impact-bass-1.mp3"),
    (26, 1.4, "", "Where had the dragons come from?",
     "The mountains became a birthplace, and the creatures an inheritance.", 5.2, "whoosh-short.mp3"),
    (27, 1.4, "Qarth", "Two moons, and one that cracked like an egg",
     "A fable, not an astronomical record.", 5.0, "cloth1.ogg"),
    (28, 1.4, "Ib · Sothoryos", "Dragon bones far from Valyria",
     "The question widens beyond one peninsula.", 5.0, "whoosh-short.mp3"),
    (30, 1.2, "The eastern tradition", "The secret did not begin with Valyrian shepherds",
     "Knowledge, it says, travelled west from the Shadow.", 5.4, "impact-bass-1.mp3"),
    (33, 1.4, "", "The bond is real. Its origins remain unclear.",
     "We can measure the change without possessing its lost instructions.", 5.2, "whoosh-short.mp3"),
    (34, 1.4, "Dragonbinding", "Horns that seem as threatening as they are promising",
     None, 4.8, "metalLatch.ogg"),
    (36, 1.4, "Septon Barth", "Blood magic, long after the beginnings",
     "Speculation, not proof of an invented ceremony.", 5.0, "cloth1.ogg"),
    (38, 1.4, "", "Approach became acceptance.",
     "And acceptance made riding possible.", 5.0, "whoosh-cinematic.mp3"),
    (39, 1.2, "", "The wings open. The ledge falls away.",
     None, 4.4, "impact-bass-2.mp3"),
    (41, 1.4, "The dragonlords", "Families who rode dragons",
     "A flock can be counted. A dragon changes what its rider can demand.", 5.2, "impact-bass-1.mp3"),
    (43, 1.4, "Blood of the dragon", "Close-kin marriage",
     "A custom for preserving a ruling line — not proof of how bonding works.", 5.2, "cloth1.ogg"),
    (45, 1.4, "The Freehold", "No king. Forty families.",
     "Authority exists only when rivals accept it.", 5.2, "impact-bass-1.mp3"),
    (48, 1.4, "", "Forty great dragonlord families",
     "Their competition: wealth, lineage, ambition — and the creatures they commanded.", 5.4, "whoosh-short.mp3"),
    (49, 1.4, "House Targaryen", "Far from the greatest of that company",
     "Their later survival should not shrink this civilization to one house.", 5.2, "cloth1.ogg"),
    (51, 1.2, "", "Arts others could not readily reproduce",
     "The creature becomes part of the civilization's built world.", 5.2, "whoosh-short.mp3"),
    (52, 1.4, "", "Stone shaped as if it were wax",
     None, 4.6, "cloth1.ogg"),
    (55, 1.4, "The roads", "Straight, durable, fused stone",
     "Reach made permanent.", 5.0, "whoosh-short.mp3"),
    (57, 1.4, "Gold and silver", "The mines",
     "Other people's bodies bore the cost of wealth.", 5.2, "impact-bass-2.mp3"),
    (59, 1.4, "", "Some rose into the sky. Others were driven underground.",
     "The Freehold's freedom and its bondage were parts of the same civilization.", 5.6, "impact-bass-1.mp3"),
    (61, 1.2, "", "Both built their greatness through conquest and slavery",
     "Not freedom against tyranny — power against power.", 5.4, "whoosh-short.mp3"),
    (63, 1.2, "The coming struggle", "The lockstep legion beside the dragonrider",
     "Discipline against wings.", 5.0, "impact-bass-1.mp3"),
    (67, 1.6, "", "Not a simple ascent from weakness into glory",
     "Beauty and brutality grew together beneath the same wings.", 5.4, "whoosh-cinematic.mp3"),
    (69, 6.2, "End of Chapter One", "The shepherds had become <em>dragonlords</em>.",
     "Next: the legions of Old Ghis.", 8.0, "whoosh-cinematic.mp3"),
]

# Dates and places, shown as a plaque when the narrator names them.
PLACES = [
    (0,  "the Iron Throne",             "WESTEROS",                    "the throne this story begins before"),
    (0,  "Aegon Targaryen",             "AEGON TARGARYEN",             "a conqueror centuries away"),
    (0,  "southern Essos",              "ESSOS — SOUTHERN COAST",      "the peninsula's continent"),
    (2,  "Aegon's Conquest",            "THE CONQUEST",                "the dating zero point"),
    (2,  "the Long Night",              "THE LONG NIGHT",              "older than the count"),
    (3,  "the Rhoyne",                  "THE RHOYNE",                  "the river of the first memory"),
    (3,  "Mother Rhoyne",               "MOTHER RHOYNE",               "mother of the river peoples"),
    (4,  "the traditions of Yi Ti",     "YI TI",                       "a different account, far east"),
    (4,  "the Amethyst Empress",        "THE AMETHYST EMPRESS",        "murdered by her brother"),
    (6,  "Asshai",                      "ASSHAI",                      "beside the River Ash"),
    (7,  "Old Ghis",                    "OLD GHIS",                    "the empire of brick"),
    (8,  "Grazdan the Great",           "GRAZDAN THE GREAT",           "founder of Ghiscari greatness"),
    (10, "the Lands of the Long Summer", "THE LANDS OF THE LONG SUMMER", "the peninsula before the Doom"),
    (11, "the Fourteen Flames",         "THE FOURTEEN FLAMES",         "the mountains of the peninsula"),
    (26, "Qarth",                       "QARTH",                       "a city, and a fable of two moons"),
    (28, "Ib and Sothoryos",            "IB · SOTHORYOS",              "dragon bone far from Valyria"),
    (30, "the Shadow",                  "THE SHADOW",                  "an eastern tradition of teachers"),
    (34, "dragonbinding",               "DRAGONBINDING",               "horns, bands and inscriptions"),
    (35, "the ironborn",                "THE IRONBORN",                "a horn that kills the man who sounds it"),
    (36, "Septon Barth",                "SEPTON BARTH",                "blood magic, written much later"),
    (38, "a mountain ledge",            "THE FIRST ASCENT",            "the imagined threshold"),
    (42, "the dragonlords",             "THE DRAGONLORDS",             "a caste, not a coronation"),
    (43, "Close-kin marriage",          "BLOOD OF THE DRAGON",         "a custom, not a proof"),
    (45, "The Freehold",                "THE FREEFOLD",                "no king, many houses"),
    (48, "Forty great dragonlord families", "40 FAMILIES",             "the centre of Valyrian power"),
    (49, "the Targaryens",              "HOUSE TARGARYEN",             "not the greatest of that company"),
    (55, "Valyrian roads",              "THE FUSED-STONE ROADS",       "reach made permanent"),
    (57, "the mineral wealth",          "GOLD AND SILVER",             "the price paid below"),
    (63, "Old Ghis",                    "OLD GHIS",                    "the empire across the water"),
    (65, "the lockstep legion",         "THE LOCKSTEP LEGIONS",        "discipline against wings"),
    (69, "five wars",                   "THE FIVE WARS",               "the next chapter"),
]

CSS = r"""
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

/* transparent title card — type over the image, no panel, no box */
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

/* the year / the place — an overline plaque, also transparent */
.plaque{position:absolute;z-index:9;left:132px;top:104px;pointer-events:none;
  padding:0 0 0 24px;border-left:3px solid var(--ember);max-width:1010px;
  background:none}
.plaque .pl{font-family:var(--mono);font-size:28px;letter-spacing:.30em;color:var(--ember-hot);
  text-transform:uppercase;margin:0 0 9px}
.plaque .pv{font-family:var(--display);font-size:46px;line-height:1.1;color:#fdf8ec;margin:0;
  text-wrap:balance}
.plaque .pn{font-family:var(--serif);font-size:28px;color:#cec5b1;margin:9px 0 0}

/* chapter card — type over the image, not a black frame */
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


# ------------------------------------------------------------------ helpers

def lufs(path: Path) -> float:
    """Integrated loudness of a whole file, measured, not guessed."""
    env = dict(shutil.os.environ)
    env["PATH"] = f"{ROOT}/.cache/bin:" + env.get("PATH", "")
    p = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", str(path), "-af", "ebur128=peak=true", "-f", "null", "-"],
        capture_output=True, text=True, env=env,
    )
    tail = p.stderr.rsplit("Integrated loudness", 1)[-1]
    m = re.search(r"I:\s*(-?\d+\.\d+) LUFS", tail)
    if not m:
        raise RuntimeError(f"could not measure {path}")
    return float(m.group(1))


def cut_music(src: Path, dst: Path, offset: float, dur: float) -> None:
    """Cut the chapter's bed out of a licensed track and make it the right length.

    The four licensed beds are 113-589 s and the chapters are 240-330 s, so a plain
    cut would sometimes stop short. Stream-loop the source and crossfade the loop
    point, so the bed covers the chapter with no seam and no silence.
    """
    env = dict(shutil.os.environ)
    env["PATH"] = f"{ROOT}/.cache/bin:" + env.get("PATH", "")
    fade = 6.0
    # loop the source until it is comfortably longer than the chapter, then trim
    subprocess.run(
        ["ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", f"{offset:.3f}",
         "-stream_loop", "3", "-i", str(src),
         "-af", f"afade=t=in:st=0:d={fade},afade=t=out:st={dur - fade:.3f}:d={fade}",
         "-t", f"{dur:.3f}", "-c:a", "libmp3lame", "-b:a", "128k",
         "-ar", "48000", str(dst), "-y"], check=True, env=env)


def sentences(text: str) -> list[str]:
    return [s for s in re.split(r"(?<=[.?!])\s+", text.strip()) if s]


def sentence_start(timing: dict, block: int, needle: str) -> tuple[float, float]:
    """Start and end (absolute seconds) of the measured sentence naming `needle`.

    Measured by measure_narration_timing.py: the sentence spans sit on real gaps in
    the voice, so a card opened here appears on the pause before the name is spoken.
    """
    for s in timing["blocks"][block]["sentences"]:
        if needle.lower() in s["text"].lower():
            return s["start"], s["end"]
    return -1.0, -1.0


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


# ------------------------------------------------------------------ build

def main() -> None:
    blocks = json.loads(BLOCKS.read_text())
    timing = json.loads(TIMING.read_text())
    plan = list(csv.DictReader(SHOT_PLAN.open()))
    assert len(blocks) == BLOCKS_N, len(blocks)
    assert len(plan) == 1050, len(plan)

    (PROJ / "compositions").mkdir(parents=True, exist_ok=True)
    (PROJ / "production").mkdir(exist_ok=True)
    for d in ("images", "audio/music", "audio/sfx"):
        (PROJ / "assets" / d).mkdir(parents=True, exist_ok=True)

    # ---- assets: the 1050 plates, the voice, the beds, the effects
    for p in sorted(SRC_IMAGES.glob("*.jpg")):
        dst = PROJ / "assets/images" / p.name
        if not dst.exists():
            shutil.copy2(p, dst)
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
    gsap = EP / "cinematic_film/assets/gsap.min.js"
    if not (PROJ / "assets/gsap.min.js").exists():
        shutil.copy2(gsap, PROJ / "assets/gsap.min.js")

    # ---- music: cut each chapter's bed out of the licensed track, then measure the
    # slice and normalise it. Measuring the whole file is wrong: these beds vary by
    # 8 LUFS across their length, so a file-wide figure under- or over-cuts a chapter.
    BED_DIR = PROJ / "assets/audio/bed"
    BED_DIR.mkdir(parents=True, exist_ok=True)
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

    # ---- scenes
    scenes: list[dict] = []
    sfx: list[dict] = []
    for i in range(BLOCKS_N):
        sid = f"b{i + 1:03d}"
        t0 = i * BLOCK
        text = blocks[i]
        plates = plan[i * PLATES_PER_BLOCK:(i + 1) * PLATES_PER_BLOCK]

        body, js = [], []
        body.append('  <div class="stage">')
        for k, p in enumerate(plates):
            pid = f"{sid}-p{k:02d}"
            img = Path(p["scene_id"]).name.replace("VAL-EP001-IMG", "") + ".jpg"
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
        # grade + grain once over the whole block
        body.append('    <div class="grade"></div>')
        body.append('    <div class="grain"></div>')
        n_g = max(2, int(BLOCK / 5))
        for g in range(n_g):
            dx, dy = GRAIN[g % len(GRAIN)]
            js.append(f'  tl.set(".grain",{{x:{dx},y:{dy}}},{g * BLOCK / n_g:.3f});')

        # chapter card, over the first plate of the chapter
        ch = next((c for c in CHAPTERS if c[4] == i), None)
        if ch:
            num, label, title, blurb = ch[0], ch[1], ch[2], ch[3]
            cid = f"{sid}-ch"
            body.append(f'  <div id="{cid}" class="chapter"><div class="inner">'
                        f'<p class="num">{num}</p><p class="lbl">{label}</p>'
                        f'<h1>{title}</h1><p>{blurb}</p><div class="rule"></div></div></div>')
            js.append(f'  tl.fromTo("#{cid}",{{opacity:0}},{{opacity:1,duration:.7,ease:"power2.out",immediateRender:false}},0.35);')
            js.append(f'  tl.to("#{cid}",{{opacity:0,duration:.8,ease:"power2.in"}},4.4);')
            js.append(f'  tl.fromTo("#{cid} .rule",{{scaleX:0}},{{scaleX:1,duration:1.1,ease:"power2.out"}},0.8);')
            sfx.append(dict(file="riser.mp3", start=t0 + 1.2, vol=0.26))
            sfx.append(dict(file="impact-bass-1.mp3", start=t0 + 4.6, vol=0.34))

        # ---- on-screen messages, one at a time -------------------------------
        # Title cards and place plaques share the screen, so they are scheduled as a
        # single timeline: a message never opens while another is still up, and no
        # message opens within 5.5 s of a chapter card. (Three simultaneous overlays
        # shipped in the first draft; this is the fix.)
        msgs = []   # (at, hold, kind, payload)
        for c in CARDS:
            if c[0] != i:
                continue
            _, off, eyebrow, line, sub, hold, fx = c
            off = max(0.35, off - 0.35)      # open a beat before the line it quotes
            msgs.append([off, hold, "card", dict(eyebrow=eyebrow, line=line, sub=sub, fx=fx)])

        for (b, needle, place, note) in PLACES:
            if b != i:
                continue
            s_start, s_end = sentence_start(timing, i, needle)
            if s_start < 0:
                continue
            at = s_start - t0
            hold = max(3.4, min(6.2, (s_end - s_start) + 2.0))
            msgs.append([at, hold, "place", dict(place=place, note=note)])

        msgs.sort(key=lambda m: m[0])
        floor = 5.5 if ch else 0.0
        cursor = floor
        kept = []
        for at, hold, kind, payload in msgs:
            at = max(at, cursor)
            if at > 24.0:                    # keep every message clear of the block edge
                continue
            hold = min(hold, 29.2 - at)
            if hold < 2.6:
                continue
            cursor = at + hold + 0.35        # a 0.35 s breath between messages
            kept.append((at, hold, kind, payload))

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
                body.append(f'  <div id="{pid}" class="plaque" style="opacity:0">'
                            f'<p class="pl">Place</p>'
                            f'<p class="pv">{payload["place"]}</p>'
                            f'<p class="pn">{payload["note"]}</p></div>')
                js.append(f'  tl.fromTo("#{pid}",{{opacity:0,x:-22}},'
                          f'{{opacity:1,x:0,duration:.55,ease:"power3.out",immediateRender:false}},{at:.2f});')
                js.append(f'  tl.to("#{pid}",{{opacity:0,duration:.45}},{at + hold:.2f});')
                sfx.append(dict(file="metalLatch.ogg", start=t0 + at, vol=0.22))

        body.append('  </div>')
        (PROJ / "compositions" / f"{sid}.html").write_text(
            scene_shell(sid, BLOCK, "\n".join(body), "\n".join(js)))
        scenes.append(dict(id=sid, start=t0, dur=BLOCK, plates=len(plates)))

    # ---- audio: voice, seven beds, effects on their own lanes
    audio = [f'  <audio id="narr" src="assets/audio/narration.mp3" data-start="0" '
             f'data-duration="{FILM:.1f}" data-volume="1.0" data-track-index="20"></audio>']
    for k, c in enumerate(CHAPTERS):
        num, blk = c[0], c[4]
        start = blk * BLOCK
        end = (CHAPTERS[k + 1][4] * BLOCK) if k + 1 < len(CHAPTERS) else FILM
        dur = end - start
        g = bed_gain(f"ch_{num}.mp3")
        audio.append(
            f'  <audio id="mus-{num}" src="assets/audio/bed/ch_{num}.mp3" '
            f'data-start="{start:.1f}" data-duration="{dur:.1f}" '
            f'data-volume="{g}" data-fade-in="3.0" data-fade-out="3.0" '
            f'data-track-index="19"></audio>')

    # lane allocation: no two overlapping cues share a lane
    lanes: list[float] = []
    for c in sorted(sfx, key=lambda x: x["start"]):
        dur = SFX_DUR.get(c["file"], 2.0)
        for li, busy in enumerate(lanes):
            if busy <= c["start"] + 0.01:
                lanes[li] = c["start"] + dur
                c["lane"] = 21 + li
                break
        else:
            lanes.append(c["start"] + dur)
            c["lane"] = 21 + len(lanes) - 1
    for k, c in enumerate(sfx):
        audio.append(f'  <audio id="sfx{k:03d}" src="assets/audio/sfx/{c["file"]}" '
                     f'data-start="{c["start"]:.3f}" data-duration="{SFX_DUR.get(c["file"], 2.0):.3f}" '
                     f'data-volume="{c["vol"]}" data-track-index="{c["lane"]}"></audio>')

    hosts = "\n".join(
        f'  <div id="{s["id"]}" class="clip" data-composition-id="{s["id"]}" '
        f'data-composition-src="compositions/{s["id"]}.html" data-start="{s["start"]:.3f}" '
        f'data-duration="{s["dur"]:.3f}" data-width="1920" data-height="1080" '
        f'data-track-index="1" data-track-kind="graphics"></div>' for s in scenes)

    index = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Rise of Old Valyria — Chapter One</title>
<script src="assets/gsap.min.js"></script>
<style>
{CSS}
  #film {{ position: relative; width: 1920px; height: 1080px; overflow: hidden; background: #07070a; }}
  #film > .clip:not(audio) {{ position: absolute; inset: 0; }}
  .stage {{ position: absolute; inset: 0; overflow: hidden; }}
</style>
</head>
<body>
<div id="film" data-composition-id="film" data-width="1920" data-height="1080" data-fps="30"
     data-start="0" data-duration="{FILM:.1f}">
{hosts}
{chr(10).join(audio)}
</div>
<script>
window.__timelines = {{ "film": gsap.timeline({{ paused: true }}) }};
</script>
</body>
</html>
"""
    (PROJ / "index.html").write_text(index)
    (PROJ / "hyperframes.json").write_text(json.dumps(
        {"$schema": "https://hyperframes.heygen.com/schema.json",
         "name": "rise-of-old-valyria-documentary", "skill": "hyperframes"}, indent=2))

    shot_list = dict(
        film_seconds=FILM, fps=FPS, scene_count=len(scenes), image_slots=1050,
        narration=dict(file="assets/audio/narration.mp3", duration=2100.024),
        chapters=[dict(num=c[0], title=c[2], first_block=c[4], start=c[4] * BLOCK,
                       track=c[5], offset=c[6], volume=bed_gain(f'ch_{c[0]}.mp3')) for c in CHAPTERS],
        bed_levels=beds, bed_target_lufs=TARGET_BED_LUFS,
        cards=[dict(block=c[0] + 1, at=round(max(0.3, c[1] - 0.35), 2),
                    line=re.sub("<[^>]+>", "", c[3]), hold=c[5], sfx=c[6]) for c in CARDS],
        places=[dict(block=b + 1, needle=n, place=p, note=note) for b, n, p, note in PLACES],
        sfx=sfx,
    )
    (PROJ / "production/SHOT_LIST.json").write_text(json.dumps(shot_list, indent=1))
    print(f"{len(scenes)} scenes · {len(sfx)} sfx cues · {FILM:.0f}s · beds "
          + ", ".join(f"{k} {v}->{bed_gain(k)}" for k, v in beds.items()))


SFX_DUR = {}
for p in sorted(SRC_SFX.iterdir()):
    pass


def read_durations() -> None:
    """Measured length of every effect, so `data-duration` never runs past the file."""
    env = dict(shutil.os.environ)
    env["PATH"] = f"{ROOT}/.cache/bin:" + env.get("PATH", "")
    for p in sorted(SRC_SFX.iterdir()):
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                              "-of", "csv=p=0", str(p)], capture_output=True, text=True, env=env)
        SFX_DUR[p.name] = round(float(out.stdout.strip()), 3)


if __name__ == "__main__":
    read_durations()
    main()
