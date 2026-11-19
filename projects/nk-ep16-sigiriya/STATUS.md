# EP16 Sigiriya: status

Tamil title: சிகிரியா / பாறை மேல ஒரு அரண்மனை?  Target about 8 minutes (asked for by the user). Same recipe as EP15 (`projects/nk-ep15-genghis/STATUS.md` has the full pipeline, the lessons and the wipe recovery steps).

## Done (19 Nov 2026)
- Research: nine web searches, extracts only. `FACT_SHEET.md` lists every fact with **check** marks.
- Script v1: `script/script.mjs` → `SCRIPT_TA.md`. 70 lines, 6,927 characters, hook + six chapters.
- Narration: `voice-02`, `narration/N01`–`N07.mp3`, 462.4 s. `N08.mp3` (channel end card, 13.1 s) reused from EP15. Expected film length about 8 min 30 s (EP15 had 49 s without narration).
- Timings: `narration/align.json`. Two lines of N04 (q01, q02) were set by hand from the pause list, because "கீழ மேகம். கையில பூ." came out as one breath; not listened to.
- Shot list: `shots/shots.txt` → `SHOTLIST.md`, 144 pictures (`shots/counts.json`). Looks and reference texts are in `shots/expand.py`.
- Reference faces: `kashyapa`, `dhatusena`, `moggallana`, `migara` (`shots/CAST.md`), all invented.
- Pictures 001–056 made and checked (batches B01–B06). Next: 057–066 (B07).

## Next
1. Pictures 007–144 in batches of 10 per turn: `generate_image` into `google_drive/ep16_pics/raw/NNN.jpg` (prompts from `shots/prompts.json`, adjusted by hand where the look text does not fit), then
   `tools/sheet.py a b` → look → `tools/crops.py` → `tools/pack.py a b <batch number>` → upload zip, then sheet → row below → commit and push.
   Batch numbers must be passed to `pack.py` by hand, because B01 holds only six pictures (B02 = 007–016, B03 = 017–026, …, B15 = 137–144).
2. Redo pass (`shots/redo.txt`).
3. Film: `film/title.mjs` still names EP15 picture numbers for its background plates and `film/gen.mjs` still has the EP15 `HOOK_FX` list and the EP15 line for the subscribe pop-up (line 3 of N02). Both must be set for EP16 before rendering. `tools/finish.sh` needs no change (hook, title, six chapters, end card).
4. Render, level, upload the 1080p parts and the full 720p file in one turn.

## Chapters
| Clip | Chapter | Lines | Seconds | Pictures |
|---|---|---|---|---|
| N01 | hook | 11 | 58.1 | 001–020 |
| N02 | 01 அப்பாவும் மகனும் | 10 | 74.4 | 021–043 |
| N03 | 02 பாறை மேல ஒரு நகரம் | 10 | 73.8 | 044–066 |
| N04 | 03 மேகத்துல மிதக்கற பெண்கள் | 9 | 70.3 | 067–086 |
| N05 | 04 யானை திரும்பின நாள் | 10 | 56.2 | 087–104 |
| N06 | 05 ராவணன் கோட்டையா? | 10 | 60.1 | 105–122 |
| N07 | 06 மறுபடி வெளிச்சத்துக்கு | 10 | 69.4 | 123–144 |

## Picture rules
- No blood, no bodies, nobody shown being hurt. The old king's death is a newly bricked wall; the battle is dust and far figures; Kashyapa's death is a dagger and a crown in the grass (never the word for it in a prompt).
- The painted women are drawn clothed in a blouse (the originals are not); no surviving painting is copied.
- Monks from behind; no Buddha image.
- Legend pictures (look N) only under lines tagged belief or claim.
- No readable writing; scratched verses and manuscripts out of focus.
- Scholars, officers and present-day people from behind or as hands only.

## Open points
- Scratch voice; no native Tamil read-through.
- All **check** items in `FACT_SHEET.md` are unverified; the closing quotation (the visitor Budal on the mirror wall) is given from memory of the usual translation and should be confirmed first.
- Dates 477–495 follow UNESCO; other chronologies differ by a few years.
- The film runs about 8 min 30 s, a little over the 8 minutes asked for.
- Dress of the 5th century court (bare chest, waist cloth, topknot) is a guess.

## Drive
| What | Id |
|---|---|
| Folder `EP16_Sigiriya` (under root `1WqhshH9XcvNUna4lzyS692eidgWQfeS1`) | `1aPOds5hqKciAaDOMqv4ecjQyo5gbR6q0` |
| Folder `EP16_Sigiriya/images` | `1F3KnwKIvXf6viLrf4DiG_e1Yz1etxrm0` |
| `EP16_Sigiriya_SCRIPT_TA_v1.md` | `1Rkp6gRiDfDt-vn7fMz-ZgZcWG_rBTHYi` |
| `EP16_Sigiriya_FACT_SHEET.md` | `1rPoFWfHH30teIQTYK5PMO4F70frANr68` |
| `EP16_Sigiriya_SHOTLIST.md` | `1qnSlIDSY8muRTxoVMIAfQNz_z-sGmbsp` |
| `EP16_narration_scratch_voice02.zip` (N01–N08) | `1-Z9aNx1XM7sLF9JR2GkNik30lnsbyvUP` |
| `images/EP16_cast.zip` | `1Z1KEUzJkrsxl1sRgS_C2aYa_zcl1DQ2k` |

## Picture batches
| Batch | Pictures | Zip id | Sheet id | Notes |
|---|---|---|---|---|
| B01 | 001–006 | `1ZfqAutzFryj4L1437ymnfWTBU4LtqwkQ` | `1LNWq9njN2QxDZe6NzPm4edervIlar472` | all good. 005: the king stands at the right edge of the frame. |
| B02 | 007–016 | `1J46Logvqf5D9yyxdvY_tKx5jNix0IfwZ` | `1IpaSShNcaH4pQXn2iTD3TKQqVLNiS-QI` | all usable. 008: the crown came out lower than in the reference. 009: the boats stand in a very even row. 012, 013: the paintings were asked for as "a photograph of an ancient wall painting" with their own tail (no "no drawn outlines"), which worked; keep that wording for all look P pictures. |
| B03 | 017–026 | `1-13DqjuVaPym-Kfy-SWm34y__LtOshPx` | `1atzfV1da_91u7sCz2tObjCuotOk9Oe8l` | all usable. 019: the sleeve looks like a rolled shirt cuff and the scratches are sharp, though not real letters (on the redo list as optional). 022 came with black bars left and right, trimmed by `sheet.py`. 023: both princes hold their reference faces with the ages stated. |
| B04 | 027–036 | `1tJqXowUexE55E71a7iyoNejquE663KEl` | `1jbCfJQeuPl7PphFiKhzk5MrYfaqxG8hl` | all usable. 032: the crown is a low diadem, not the tall crown of 034 (on the redo list as optional). 036: the embankment looks like a stone wall and the reservoir a little like a river. 035 came with a black bar on the left, trimmed by `sheet.py`. 031 (night, many figures) stayed photographic with the "film still shot on location at night" tail. |
| B05 | 037–046 | `192Jq1X0bztl0Z0WOsKjkeEz8P2tbuiFd` | `1COL8Wfgx84KCS3TbbzkiBzjO8Qua6-95` | 038: the old man's wrists are in dark knitted sleeves like a jumper (on the redo list; for hands of that age say "bare arms, no sleeves, no cloth on the arms"). 045: the king looks down on the rock from above, not up at it. 040 came with a black bar on top, trimmed by `sheet.py`. The rest good. |
| B06 | 047–056 | `1VPR3rB_KIfztgkjCghNB_JbW-fFDupw_` | `1SND3admR_NGSxe9m6ktyOQ3MeWYhaiUW` | all good. 048 shows the drip ledge and lichen but no carved marks. 053: the fountain is a large round stone ring, not the small pierced slab of the real site. A workspace wipe before this batch was repaired (reset to the pushed branch, `setup.sh`, narration zip downloaded again, `restore.sh`); the pictures in `google_drive/ep16_pics` had survived. |

## After a full wipe of the workspace
As in EP15: `git fetch -q origin arena/d486087a-hyperframes && git reset -q --hard FETCH_HEAD`, `bash tools/setup.sh`, download the Drive zips above into `<repo>/google_drive/`, `bash tools/restore.sh`, unzip the narration zip into `narration/`, recreate the links `shared/vo` → `../narration` and `shared/plates` → `../out/img`.
