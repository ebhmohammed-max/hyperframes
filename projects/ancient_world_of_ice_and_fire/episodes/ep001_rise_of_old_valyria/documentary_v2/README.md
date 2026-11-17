# Rise of Old Valyria — documentary cut v2

35:00. One film. The narrator's first word to the narrator's last.

This replaces the 5-minute "Part One" proof, which the user rejected: it was a trailer,
a title sequence and one chapter, not the film. v2 is the film.

## What it is made of

| piece     | source                                                | how it is used                                                 |
| --------- | ----------------------------------------------------- | -------------------------------------------------------------- |
| narration | `EP001_COMPLETE_NARRATION_35m00s_v01.mp3`, 2100.024 s | plays whole, from 0:00, unedited                               |
| pictures  | `documentary_film/assets/images/0001…1050.jpg`        | **all 1050**, in shot-plan order, 2.000 s each                 |
| music     | four licensed beds                                    | one bed per chapter, cut to length, crossfaded at the seams    |
| effects   | 24 files                                              | one cue per title card, chapter card and place plaque: 81 cues |

Nothing else is in the frame. No trailer, no title sequence, no archive boards, no
black cards, no chapter dividers that stop the picture. The image stays up for all
35 minutes.

## The rules the user set, and where they are implemented

**"Transparent title card with SFX."** Every card is type over the moving plate —
no panel, no box, no background fill. Two layers only: a rule, an optional eyebrow, the
line, an optional sub. Each opens on a measured pause in the voice and carries its own
effect (`CARDS` in the builder, 43 cards, 43 cues).

**"Whenever the narrator mentions year/time/place, show them."** 31 plaques
(`PLACES`), opened on the _measured_ sentence that names the place. Examples: ESSOS —
SOUTHERN COAST, YI TI, ASSHAI, OLD GHIS, THE FOURTEEN FLAMES, QARTH, IB · SOTHORYOS,
THE FREEFOLD, HOUSE TARGARYEN, THE LOCKSTEP LEGIONS, THE FIVE WARS.

The script is deliberately careful about numbers — it says "roughly five thousand
years", "thousands of years", "centuries" — so the plaques repeat the narration's own
hedging ("≈ 5,000 years before the Conquest", not a fake precise date).

**"Background music too loud — reduce it, and use several for different scenarios."**
Seven chapter beds, which is the most scenario variety the four available tracks allow:

| chapter                          | bed                          | gain  | measured bed level |
| -------------------------------- | ---------------------------- | ----- | ------------------ |
| I The Shepherds and the Mountain | ancient-rite                 | 0.214 | −30 LUFS           |
| II An Older Darkness             | night-vigil                  | 0.182 | −30 LUFS           |
| III The World Before Valyria     | ancient-winds                | 1.396 | −30 LUFS           |
| IV Beneath the Fourteen Flames   | night-vigil (later window)   | 0.174 | −30 LUFS           |
| V The First Encounter            | mana-two                     | 0.288 | −30 LUFS           |
| VI The Dragonlords               | ancient-rite (later loop)    | 0.214 | −30 LUFS           |
| VII The Price of the Freehold    | ancient-winds (later window) | 1.380 | −30 LUFS           |

Gain is not guessed. Each chapter bed is cut out of its track, measured on its own
(the beds vary by up to 18 LUFS across their length, so one file-wide figure is wrong),
then normalised to −30 LUFS. Measured on the mix: voice alone is −19.6 LUFS, voice + bed
is −19.6 LUFS, i.e. the bed sits about 10 dB under the voice and lifts the programme by
~0.25 LU. In the rejected cut the bed was at effectively −45 LUFS — inaudible.

**"Start at the very beginning of the narrator's story, nothing more."** The film's first
frame is the narrator's first word (voice onset 0.16 s). There is no cold open, no
trailer, no "coming up" card. Chapter cards appear _over_ the picture while the
narration continues; they never pause it.

## How the timing is known rather than assumed

The 30-second blocks are a script structure, not a pause — the voice runs straight
through the block boundaries. So nothing is placed by character count:

`measure_narration_timing.py` decodes the master once to 16 kHz, computes a 20 ms RMS
envelope, merges sub-200 ms holes (plosive closures, breath), and then snaps a
character-length prior for each sentence onto the nearest measured gap (±3 s, order
preserved). Output: `production/NARRATION_TIMING.json`, 391 sentences with real
start/end times. Every card and plaque is placed from that file.

## Verification

`hyperframes check`: **0 errors, 0 warnings** (33 findings fixed along the way:
type floor, plaque collisions, gsap `immediateRender`, media fit).

Frames verified by snapshot at 6/130/672/1180/1930/2090 s — type over image, no boxes,
no overflow.

## Render

Measured on this machine: **6.3 s of wall clock per second of film**. The full film is
therefore ~3h45m, so it is rendered in seven chapter chunks (`render_documentary_v2.sh`),
each 15–35 min, resumable, with a 2 s overlap that assembly trims.

## Files

- `production/SHOT_LIST.json` — every scene, card, plaque and cue with its time
- `production/NARRATION_TIMING.json` — measured sentence map of the voice
- `production/BED_LEVELS.json` — measured level of each chapter bed
- `scripts/episode-audit/build_documentary_v2.py` — the builder
- `scripts/episode-audit/measure_narration_timing.py` — the timing measurement
- `scripts/episode-audit/render_documentary_v2.sh` — the chunked render
