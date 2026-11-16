# Before the Dragons — The Rise of Old Valyria

## Cinematic Part One — 5:00

Built with this repository's own HyperFrames toolchain (`packages/cli`, `packages/core`,
`packages/producer`, `packages/engine`, `packages/lint`), compiled from source at
`0.8.223`. No external video editor, no browser-recording tool.

- Project: `projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria/cinematic_film`
- Build: `hyperframes render <project> -q looks` (1080p, 30 fps, 9,000 frames)
- Gate: `hyperframes check` → 0 errors, 0 warnings

## What the five minutes are

| Time      | Section          | What it does                                                                    |
| --------- | ---------------- | ------------------------------------------------------------------------------- |
| 0:00–1:01 | Trailer          | Nine cuts, four intertitles, cut on the music's four-second bars. No narration. |
| 1:01–1:18 | Title sequence   | The name lands, then "Coming in this episode" lists Chapters I–VII.             |
| 1:18–1:24 | Chapter card     | Chapter One.                                                                    |
| 1:24–4:24 | Documentary body | Recorded narration (blocks B001–B006) over plates, with four archive boards.    |
| 4:24–5:00 | Outro            | End of Part One, what Part Two opens with, credits.                             |

## The archive board

The explanation device. A dark desk lit from above; paper artifacts, photographic
prints with their own captions, pins, tape and a punched index card. Boards carry the
argument while the narration runs, so the film stops being a slideshow of stills:

1. **01 — Fourteen mountains over a flock** (1:54): the evidence is a landscape, not a chronicle.
2. **02 — Dating the rise** (2:26): the "≈5,000 years" figure, marked approximate.
3. **03 — Three traditions, one catastrophe** (2:58): the Blood Betrayal, marked as tradition.
4. **04 — At the margins, not the centre** (3:33): the chapter's thesis, stated then tested.

## Sound

- **Narration**: the episode's already-recorded track, blocks B001–B006, exactly 3:00.
- **Music**: Ancient Rite (trailer), Night Vigil (body bed at 0.15 under the voice),
  Ancient Rite (outro). Kevin MacLeod, CC BY 4.0.
- **SFX**: 33 cues, every one tied to a title card, intertitle, board artifact or
  transition. Cues are placed with a lane allocator so no two overlapping sounds share
  an audio lane. Pixabay Content Licence; some from Kenney CC0.

## Cue discipline

Every cut and board is cued to measured narration, not estimated:
`.cache/narration-gaps.json` holds the silence gaps found by ffmpeg `silencedetect`
over the recorded voice, and the scene starts derive from them.

## Files

- `production/SFX_CUE_SHEET.json` — every scene and every sound with its time.
- `production/SFX_DURATIONS.json` — measured length of each effect file.
- `scripts/episode-audit/build_cinematic_film.py` — the generator; rebuilds all 26 scenes.
- `scripts/episode-audit/verify_cinematic_coverage.py` — fails on a hole in the timeline.

## Delivery

`renders/CINEMATIC_PART1_FINAL_1080p.mp4` — 78,187,247 B, 300.000 s, 1920×1080 30 fps.
Measured on the delivered file: **−16.1 LUFS integrated, −2.4 dBTP true peak**.

Getting the true peak legal took one measured correction rather than an assumed one.
The master measures −1.64 dBTP and needs +2.67 dB to reach −16 LUFS; a limiter ceiling
of 0.822 (−1.7 dBFS) still delivered −0.6 dBTP, because the AAC encode lifts one dense
moment at 2:27 by about 1.5 dB. A sweep on that window settled the ceiling at 0.630,
which delivers −2.4 dBTP across the whole file. The script records the reasoning inline.

Rendered from HyperFrames 0.8.223 in this repository: `hyperframes render -q looks`
with segmented capture, about 23 minutes for 9,000 frames. `hyperframes check` passes
with 0 errors and 0 warnings.

## Honest limits

- Part One covers Chapter One only. Chapters II–VII are scripted and their narration is
  recorded, but they are not in this cut.
- The plates are reconstructions of a legendary place; the boards say so where the
  record is thin ("Approximate", "Tradition", "Reconstruction").
- Narration was not re-recorded for this cut. The trailer is deliberately wordless.
