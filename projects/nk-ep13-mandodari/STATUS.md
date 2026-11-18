# EP13 Mandodari: status

Topic in the user's words: "Untold story of ravaana and his wife". Shorter film: about 10 minutes, 198 pictures. Same pipeline as EP12 (`../nk-ep12-poompuhar/STATUS.md` has the full recipe and the lessons).

## Done on 17 Nov 2026

- Research by web search (no full texts read); see `FACT_SHEET.md`, doubts marked **check**.
- `script/script.mjs` v1: hook + 6 chapters, 108 lines, 8,778 characters. `node script/build.mjs` → `SCRIPT_TA.md`, `script/lines.json`, `narration/text/`.
- Scratch narration `voice-02`: `narration/N01.mp3` … `N07.mp3` = 597.8 s. `N08.mp3` is the channel end card audio (13.1 s, the same file as EP12's N11).
- `script/align.py` → `narration/align.json`; one line flagged for a listening check (N05 q05, a short line).
- Shot list: `shots/shots.txt` (198 rows), `shots/counts.json` (from line lengths: under 4.2 s one picture, under 8.6 s two, else three), `python3 shots/expand.py` → `shots/prompts.json`, `SHOTLIST.md`.
- Cast portraits (ravana, mandodari, maya, indrajit) made and checked; `shots/CAST.md`.
- Expected film length: 597.8 s narration + 12 s title + 17 s end card + 6 chapter cards of 2.3 s ≈ 10 min 41 s.

## Chapters

| Clip | Chapter | Lines | Seconds | Pictures |
|---|---|---|---|---|
| N01 | hook | 15 | 73.1 | 25 (001–025) |
| N02 | 01 பத்துத் தலை | 16 | 90.6 | 31 (026–056) |
| N03 | 02 மயன் மகள் | 14 | 82.3 | 27 (057–083) |
| N04 | 03 கேட்காத கணவன் | 15 | 77.5 | 26 (084–109) |
| N05 | 04 புலம்பல் | 17 | 92.8 | 30 (110–139) |
| N06 | 05 சீதையின் தாயா? | 15 | 87.1 | 28 (140–167) |
| N07 | 06 மருமகன் ராவணன் | 16 | 94.3 | 31 (168–198) |

## Drive

- Folder `EP13_Mandodari`: `1g9KaAHXx8aP1OlHJDtQP0ty4ZblHZ5qw`; subfolder `images`: `1LAGCCMejRgBeA0oPsteEccx84XnVHk0d`
- File ids: see the table at the end of this file.

## Film: done on 18 Nov 2026

**EP13 is complete.** Film length 10 min 47 s (646.7 s): N01 hook 74.1 s, title 12 s, N02–N07 93.8 / 85.5 / 80.6 / 95.9 / 90.2 / 97.4 s, end card 17 s.

- `film/title.mjs`: plates 001 (Lanka under the moon) → 011 (the king and his ten-head shadow) → 079 (Mandodari on the terrace, under the title). Subtitle size reduced from 74 to 60 px, because the longer EP13 subtitle ran to the frame edges.
- `film/gen.mjs`: `HOOK_FX` rewritten for this hook (impact on line 0, 4, 6, 14; riser through line 10 with an impact on its last word; whooshes on 2, 5, 8, 13). Subscribe pop-up left on N02 line 5 (the ten-head relief).
- `film/end.mjs`: unchanged (same end card audio as EP12).
- Render: `bash tools/render.sh`, about 5.9 s of work per film second this time (68 minutes in all).
- `bash tools/finish.sh parts` → seven 1080p parts; measured −16.54 LUFS, gain +2.54 dB (`out/deliver/gain.txt`). Part 7 was over 100 MB and was recompressed (x264 crf 20).
- `VB=1000k bash tools/finish.sh 720` → `EP13_Mandodari_full_720p.mp4`, 89.4 MB, 1280×720, 30 fps, −14.3 LUFS, peak −0.9 dBTP.
- Checked on frame sheets only (title, hook, chapter 1, chapter 6, end card, the joins). **Nobody has watched or listened to the whole film from start to end.**

| File on Drive (folder `EP13_Mandodari`) | Id | Size |
|---|---|---|
| `EP13_Mandodari_full_720p.mp4` | `1t7YkkYqng6BMnnzWj_dYcj8wS9v3br_1` | 89.4 MB |
| `EP13_1080p_01_hook_title.mp4` | `1SA-UoFIzwsRrFfoFVi_vM7VwLSnrcvt1` | 81.2 MB |
| `EP13_1080p_02_ch1.mp4` | `1c84j831hOQBKzPGkIJFrwBTKEI54XNGn` | 88.6 MB |
| `EP13_1080p_03_ch2.mp4` | `1oiMu4WdwDLHlLzhqxaZmS1d_GsKoTtQA` | 79.7 MB |
| `EP13_1080p_04_ch3.mp4` | `12YQjvhGwAIZ9TXwu2IclfL4DnPD-Jg3X` | 73.1 MB |
| `EP13_1080p_05_ch4.mp4` | `1gcQBm6zaAznzJcwj75tuDLXP-7VbJy5X` | 81.1 MB |
| `EP13_1080p_06_ch5.mp4` | `1fDOR9bRh7cSN83gjMDmYNi9D89tn4vIz` | 78.7 MB |
| `EP13_1080p_07_ch6_endcard.mp4` | `1K5gto9JFP8CGibrIjte_EwstKzGcZ2nU` | 62.0 MB |

To rebuild after a workspace reset: `git fetch` + fast-forward, `bash tools/setup.sh`, download `EP13_cast.zip`, the batch zips and the narration zip from Drive into `<repo>/google_drive/`, `bash tools/restore.sh`, unzip the narration into `narration/`, then `node film/gen.mjs N01 N02 N03 N04 N05 N06 N07 && node film/title.mjs && node film/end.mjs && bash tools/render.sh && bash tools/finish.sh parts && VB=1000k bash tools/finish.sh 720`.

## User correction, 17 Nov

The user sent a reference picture and said the first Hanuman "looks like small monkey". Hanuman is now always shown in full as a tall, mighty, crowned figure (cast key `hanuman`, made from the user's picture, stored as `cast/hanuman_user_ref.jpg`). Rama, Sita, Lakshmana and Shiva are still never shown by face. Pictures 002, 005, 006, 007 were remade; `shots/shots.txt` rows changed to `L@hanuman`.

## Open points

- Titles and script are drafts; no native Tamil read-through yet.
- Film is about 40 s over the 10-minute target. Cutting N07 q08–q09 (Ravana Kaviyam) would bring it to about 10 min 20 s.
- Fact sheet items marked **check**.

## Batches

| Batch | Pictures | Drive zip | Notes |
|---|---|---|---|
| cast | ravana, mandodari, maya, indrajit, hanuman | `EP13_cast.zip` `1ABYGdNUVcWcv5qNgUMg1oCrS8Ic-m6K4` (v2, with hanuman and the user's reference), Hanuman portrait `1xzVNEbzS0kuIUPoj9yLTHxpGYiVeWF_T`, sheet of the first four `1tPhfcagaC884vudSxKXSP6t-AkB4VSCx` | all accepted |
| B01 | 001–010 | `1X3gByyGcieCfZM1CmXCX66bTHV9H477y`, sheet `1klRgT21U1TCZsGR9zxHUCtQLYnQEBO_8` (v2; the first versions are in the Drive trash) | 002, 005, 006, 007 remade with the new Hanuman. 003 edge crop. 009 odd pose, kept. |
| B02 | 011–020 | `1SlDuT8jRai1OeyKzot_J8AEew4IEQ_24`, sheet `1UDo3LNvuxz-239g8pKL4mmQ4FKovHLWv` | 017 (casket looks like a coffin) in `shots/redo.txt`, cropped for now. 016 has Mughal-style arches and domes, kept as doubtful. 012: the king is in focus, kept. |
| B03 | 021–030 | `1-yt9dPlrqfLIMGikIQ5tjgU6XLxRZ1ei`, sheet `1PyM1F3Wk6Z9uvewLkuFG9em4ElxjtxsS` | 028 (comic-book style) in `shots/redo.txt`. 030 cropped to remove a sheet with print-like marks in the corner. Check sheets: `tools/big.py a b`. |
| B04 | 031–040 | `1lZ5Zo5r5PJ1Cx3Dac_J5x4wBFUXwCVFl`, sheet `1cvmbwjiQBukukbDfi5v-m8_SJrf3Zluv` | 038 (European crown) and 040 (hooded cloak) in `shots/redo.txt`. From this batch the prompts add "realistic like a film still, not a cartoon and no drawn outlines". |
| B05 | 041–050 | `1MH6DkOl0SS2LqHd7WhjILPAxtKXE7M7e`, sheet `1Up_bn9Dj8EK7XcZ4cnyRTjjCOv_UH7-I` | 050 (Shiva's foot looks old and veined) in `shots/redo.txt`. 045 cropped for a dark strip on the right. |
| B06 | 051–060 | `1Xjz3XAScvpUw6jiJfQ0A9kZTdMS4c5ZY`, sheet `1PLFbwebIhqtnjXU5jQiXq-ZAdJtXXiO-` | all ten accepted. 054 edge crop. 051 used 049 as a second reference. |
| B07 | 061–070 | `1dAALSJwBlxptbvfg27hmm_pVSf6Jf4la`, sheet `1pgn5hyIkLNmoR_PnFSfpIEoCrNtYs2V9` | all ten accepted. Young forest Ravana uses `raw/058.jpg` as reference (gold circlet, ochre dress); young Mandodari is described as "about eighteen, plain pale cream silk, white flowers in her braid, no crown" with the cast portrait (062 is the best reference for her from now on). |
| B08 | 071–080 | `1Ipz0yCHbWeU15_pFEyL6Em-5O1RR-rpH`, sheet `1_kUMmCBjC--rsAykZSgg1s-g0hI3Ab9D` | all ten accepted. 071 cropped for a dark left edge. 072 is more saturated than the rest, kept. `raw/001.jpg` works as a reference for the look of the city. |
| B09 | 081–090 | `1S4okD9cBAxHF2Ztst0h0sylGvdHhC49S`, sheet `19Llvnz_Y686FGG0DjwKByw-BKcoSPseX` | 081 (European crown) in `shots/redo.txt`. 085 edge crop. 088: Dhanyamalini changed from green to blue silk so she is not mistaken for Mandodari (`shots.txt` updated). 090: she holds his other arm, not the sword arm; kept. 087 slightly storybook in style, kept. |
| B10 v2 | 091–100, complete | `1MxQsIfD28wZq9Y8gtW0zckAlTRGAqCYj`, sheet `1JOJKCu9Tqo7ERAV-Bb-wC3m0Xd9awOKh` | Replaces the first B10 upload (nine pictures, trashed). Holds 096 (new) and the remade 098 and 100. 094 palm leaf has script-like marks that cannot be read; kept. |
| R1 (redo pass 1) | 017, 028, 038, 040, 050, 081, 096, 098, 100 | `1tV3VzBZ8IpJpH6qsLgU0aEnoCWnGObFD`, sheet `1Lt5eWKwB2t-0a2HxKe8EaQRQJKJwVYDL` | Nine pictures made again, all accepted; `shots/redo.txt` is empty. Same file names as in the batch zips B02–B05, B09, which still hold the first versions: unpack R1 last (`tools/restore.sh` does). First versions kept locally in `google_drive/ep13_pics/raw_v1/`. Crop entry for 017 removed. |
| B11 | 101–110 | `1ssMkHOks56Va9yeLxHwx356D0o7UzDMO`, sheet `1a0Y_SLuSp3R7J7l8rOCcplGGolQXtSDB` | All ten accepted, no crops, nothing for redo. Kept with a doubt: 104 Indrajit's chariot is a plain dark boxy car, closer to a carriage than a war chariot. Chapter 3 (to 109) complete; 110 opens chapter 4. |
| B12 v2 | 111–120, complete | `1P_hbk6pIFu6ypwldndBSY38mk9aXw5I-`, sheet `1G6iLIBmjELi3hOBO7cnXkqBfEYxH5n8q` | Replaces the first B12 upload (trashed). Holds 112 (new, gentler wording passed moderation) and the remade 114 (Indra as an older king with ordinary skin, no halo, face hidden). 115 vanara bridge: tiny upright figures with tails, kept. 116 Rama from behind. |
| B13 | 121–130 | `1ZWK3G0RkXpC2SImBO34VpFXRkVtLXBZB`, sheet `1MCg08y3oQbl2Z1sS9UltI5YJYzAOjMy4` | All ten accepted; none blocked (gentler wording for 124 and 125: armour only, "resting", no "fallen"). 129 rounded corners cropped. Kept with doubts: 124 helmet has a Roman-looking crest; 126 a little smooth and illustrated; 127 Vibhishana in a kurta-like white dress; 123 slightly illustrated, crowned shadow reads. |
| B14 | 131–140 | `1pMf9DUL03WzVx_mizT_PaFeP6OT9hVMk`, sheet `1IRLs-b0Yh8Q5iUSERibvfJZgGj6NRwOX` | All ten accepted, none blocked, no crops. 139 made as a veil-covered shape under a banner seen from far away (no figures). 131: armour and a forearm at the bottom edge, no face. 138 slightly illustrated, kept. Chapter 4 (to 139) complete; 140 opens chapter 5. |
| B15 | 141–150 | `142-EOsrI2nhAt0z2ZYEjXUl9wMlzeN7_`, sheet `1fMFLDoQQwdRPdMUzM0f5-UlAQukUmM8_` | All ten accepted, none blocked, no crops (150 edge trimmed by `sheet.py`). Kept with doubts: 141 the baby looks some months old, and the window has a glazed look; 150 the lamp looks like a later metal lantern. Babies in 141, 143, 148 with faces small or hidden. |
| B16 | 151–160 | `1JGZi3ZimN73KlS8nB2Uw9F6q9QEKP_vW`, sheet `1V3dpVonNpjsRmyCm9V9v9m__rOf7uf2R` | All ten accepted, none blocked, no crops. Kept with doubts: 154 grove background is in the same storybook style as 087 (its reference), unlike the rest; 151 casket is a long open box with a glow; 157 leaves have script-like marks that cannot be read. Sita in 154 only from behind. |
| B17 | 161–170 | `1UFKH5Z8w8-Re6GcQWyOPCOB4wijVJ_n1`, sheet `1Nlw3-S66Cq5euYP61Hz05EzNPWIn_YFu` | All ten accepted, none blocked. 170 right edge (dark tree trunk like a bar) cropped. Kept with a doubt: 167 the city is darker and more like a fairy-tale castle than the Lanka of 001. Chapter 5 (to 167) complete; 168 opens chapter 6. |
| B18 | 171–180 | `1vxiWAvxXQ4UPNFfT3F8p9DkKyygtcXgq`, sheet `1ve4UuyNy8-BC76W9R4YKedSy9jbJKf_w` | All ten accepted, none blocked, no crops. Present-day places (Mandore, Mandsaur, Bisrakh) are imagined views, not photographs of the real sites; people only from behind or hands. 178: the statue's row of heads may count nine, not ten; kept. |
| B19 | 181–190 | `1j402kkGZtqC3WWQ2SSzO3Tcev5mIFljP`, sheet `1Oi6vrpjRDx7q3sQjZ51CZxa-f0d_XnCn` | All ten accepted, none blocked, no crops. Kept with doubts: 183 shows the old woman's mouth and chin in profile at the top-left corner (eyes not shown); 188 pages show blurred lines that cannot be read; 181 wall patterns are kolam-like drawings, not writing. Next and last picture turn: 191–198 plus redo 112 and 114 (ten calls), redo zip R2. |
| B20 | 191–198 | `1wnKJSb4r4E2j58cEL3oFFkvLUi4IpjZJ`, sheet `1ZkoQkgwZgnJnvszikPHdJ4je8r59AxO7` | All eight accepted, none blocked, no crops. Kept with doubts: 197 the two leaves stand upright like sticks; 191 a dark out-of-focus shape at the left edge. **All 198 pictures are made; `shots/redo.txt` is empty.** Next: film build (`film/gen.mjs`, `title.mjs`, `end.mjs`, render). |

## Drive file ids

| File | Id |
|---|---|
| `EP13_SCRIPT_TA_v1.md` | `1P0cX5qGoFa1NjAAMVt1ThC74XQCCFwUn` |
| `EP13_FACT_SHEET.md` | `1f9ouyG8PtJ-pN1zwk6Odddynrhr4SzoF` |
| `EP13_SHOTLIST.md` | `1RCAS3Sb1Ho8TC3ipbePSAQ9QHhyfCuIn` |
| `EP13_narration_scratch_voice02.zip` (N01–N07 + end card N08) | `1SgZFcMdPWN2VSi_4qOawtvR13q5Drbuo` |
