# Episode 02 — documentary build

Same contract as Episode 01: 35:00, 70 blocks of 30 s, 1,050 plates at 2.000 s, transparent
title cards each with an effect, place names in step with the voice, music measured and
kept under the narration.

## What is new in this cut

**Long holds.** Eight blocks have the voice stopping 3.5–4.4 s before the slot ends, and
this build does not cut pictures over silence. On any block with a residual gap of 2.6 s
or more, the last plate is held for the whole gap with a 1.2 % drift, so the silence lands
on a still image instead of three orphaned cuts. 24 blocks qualify.

**Every message sits on measured audio.** `measure_ep002_timing.py` decodes the master and
finds the real gaps, then maps the script's 387 sentences onto them. A place name opens on
the measured second in which that word is spoken, and is **dropped** rather than nudged if
it cannot land there. A title card that would collide is dropped too — the previous cut's
rule, kept.

**One premixed audio track.** The renderer's own mixer writes a 2100 s float32 WAV, which
this box cannot hold; that is what killed the first render attempt at 96 %. `mix_ep002_audio.py`
builds the identical mix in under two minutes and the render is now a pure picture job.

## Numbers

|              |                                   |
| ------------ | --------------------------------- |
| Scenes       | 70                                |
| Plates       | 1,050 (all of them, 2.000 s each) |
| Title cards  | 33                                |
| Place names  | 16                                |
| Effect cues  | 52                                |
| Chapter beds | 7, each normalised to −30 LUFS    |
| Long holds   | 24 blocks                         |
| Voice        | −19.71 LUFS                       |
| Mix          | −18.48 LUFS                       |

Beds lift the programme by **1.2 LU** against the voice alone, i.e. they sit about 11 dB
under it. That is the level the Episode 01 mix was approved at.

## The bed library is the one real constraint

The four licensed tracks total 1,224 s and the film is 2,100 s, so **every chapter bed is
looped**. The loop is built with `aloop` and the seam is inside a continuous bed at −30 LUFS
under narration, so it is not audible; but it is a fact about this episode that Episode 01
did not have, and the next episode should licence more music rather than loop less.

## Place names — read this before judging them

Sixteen names are set on screen. They are placed on the measured word, not on a timer.
Where the narration hedges, the screen does not sharpen it: the coin's city is shown as
`OLD GHIS` only once the voice has named it, and the end card reads `TWO THOUSAND YEARS`
because that is the figure the script actually says.

## Files

| file                                                          | what it is                                            |
| ------------------------------------------------------------- | ----------------------------------------------------- |
| `01_COMPLETE_NARRATION_35MIN_v02.md` (in `story_film_35min/`) | the script, the single source                         |
| `scripts/episode-audit/ep002_blocks.py`                       | the only parser; refuses a block containing a heading |
| `scripts/episode-audit/build_ep002_script.py`                 | regenerates recording script, timing plan, block JSON |
| `scripts/episode-audit/measure_ep002_timing.py`               | measured sentence map from the real audio             |
| `scripts/episode-audit/mix_ep002_audio.py`                    | voice + 7 beds + 52 cues → one track                  |
| `scripts/episode-audit/build_ep002_documentary.py`            | builds the 70 compositions and `index.html`           |
| `scripts/episode-audit/render_ep002_documentary.sh`           | chunked render, resumable                             |

Generated media (plates, audio, compositions) is gitignored and rebuilds from the above.
