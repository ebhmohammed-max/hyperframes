# EP23 status: ஹிட்லர்: வீடில்லாதவனில் இருந்து ராட்சசன் வரை (Hitler: From Homeless to Monster)

Target 105 minutes, 12 chapters and a hook. Plan and chapter table: `OUTLINE.md`. Built and delivered chapter by chapter.

## Second review, 26 Nov 2026 (user: show his real face, young face too, film feel, say "February")

- **February:** the voice mispronounced "பிப்ரவரி". The spoken text now says "February" in English (N10, N11, N14 spoken again, aligned, 0 flagged; captions keep பிப்ரவரி). Later scripts: write "February" in `say`.
- **Faces:** the old rule (no face) is gone; see `shots/CAST.md`. Reference pictures in `out/cast/` (Drive `images/EP23_cast.zip`); `shots/prompts.json` lists the pictures to pass for each row (`python3 tools/next.py n` prints them). Hook pictures made again with faces: 004, 008, 010, 012, 017 (Drive `images/EP23_R1_images_faces_…zip`; the faceless first versions are in the B01 and B02 zips).
  - 012 (the doorway close-up) was made again from `cast/A.jpg` in the next turn and is back in the film (Drive `images/EP23_R2_images_face_012.zip`).
  - Shot rows 021–090 rewritten so that he, his parents, Kubizek, Hanisch, Dr Bloch and Morgenstern are seen from the front (38 rows changed; 8 shot names changed).
- **Film look:** 2.2:1 frame with black bars of 104 px (`BAR` in `film/gen.mjs`, also in `film/title.mjs`); evidence tag inside the top bar; captions just above the bottom bar; `SHIFT` moves a picture down when a head sits high; every picture prompt now asks for a 35mm film still composed for that crop. Added in the turn after: grain 0.15 at 24 fps, a faint flicker layer (`#p-flick`), dissolves of 0.5 and 0.9 s in the chapters (the hook keeps its hard cuts), and a low room tone under every clip (`shared/sfx/room-tone.mp3`, 100 s, −30 dB, played at 0.3).
- Hook: `EP23_1080p_00_hook_title_v3_film.mp4` is the current one (all of the above, 012 back in). `…_v2_film.mp4` and the first version stay on Drive.
- **Pictures made:** 001–048 (034 made in the turn after its failure). **030** came out upright (944×1122) and is cropped and soft: make it again when a call is free. To make: 049–053 (rest of chapter 1), 054–090 (chapter 2), 091–127 (chapter 3), 128–169 (chapter 4): `python3 tools/next.py 10` lists the next ten with their reference pictures and prompts. Ten image calls per turn is the limit, so pictures are the slow part: about 12 turns for what is planned so far.
- **Chapters 3 and 4 are written, spoken and aligned (0 flagged)**: `script/ch03.mjs` (N19–N26, 566.1 s, fact rows 96–140), `script/ch04.mjs` (N27–N34, 582.6 s, fact rows 141–188; it builds captions with a helper `L(say, tag, [[spoken, written]…], fx)`). Shot rows are written for both (091–127, 128–169), with `CARD_BG` for N19 and N27, look **W** (Western Front) and ref **S** (the soldier; likeness photograph `cast/S_photo.jpg`, shipped inside the B05 zip), look **M** (Munich 1919–1923) and ref **P** (the party speaker, from `H_photo.jpg`, "twelve years younger").

## Where it stands (26 Nov 2026)

| Part | Script | Narration | Timing | Pictures | Film | On Drive |
|---|---|---|---|---|---|---|
| Hook (N01–N02) + TITLE | done | done, 92.3 s | 0 flagged | 001–020 made (all) | part `EP23_1080p_00_hook_title_v3_film.mp4` (106 s) on Drive | narration, B01, B02, R1, R2, film |
| Ch 1 (N03–N10) | done | done, 535.9 s | 0 flagged | 021–048 made; 049–053 to make (N09, N10) | N03–N08 rendered and frames checked (copies in Drive `clips_work`); **part `…01_ch01a.mp4` (N03–N06) delivered**; `…ch01b` (N07–N10) waits for N09, N10 | narration, B03, B04, B05, clips, ch01a |
| Ch 2 (N11–N18) | done | done, 598.4 s | 0 flagged | shot rows 054–090, none generated | `node film/gen.mjs N11 … N18` works (reports missing pictures) | narration |
| Ch 3 (N19–N26) | done | done, 566.1 s | 0 flagged | shot rows 091–127, none generated | built (`film/N19`…`N26`), 576 s | narration, script, fact sheet |
| Ch 4 (N27–N34) | done | done, 582.6 s | 0 flagged | shot rows 128–169, none generated | built (`film/N27`…`N34`), 592 s | narration, script, fact sheet |
| Ch 5 (N35–N42) | drafted (switch `EP23_DRAFT`) | not yet | | shot rows not written | | |
| Ch 6 to 12 | not written | | | | | |

Running time so far: 39 min 32 s of narration (hook 1 min 32 s, chapter 1 8 min 56 s, chapter 2 9 min 58 s, chapter 3 9 min 26 s, chapter 4 9 min 43 s). Chapters 2 to 4 each run 25 to 60 s over the plan of 9 min: at this rate the film ends near 115 min, not 105. **Chapters 5 to 12 must stay at 8 min (about 7,400 characters, eight clips of 925) to land on 105**, or one of chapters 2 to 4 is trimmed later.

## Next steps

1. Pictures, 10 per turn: `python3 tools/next.py 10` → generate to `google_drive/ep23_pics/raw/NNN.jpg` (pass the listed reference pictures) → `$PY tools/sheet.py a b` → zip (`$PY tools/batch.py <batch> a b`, next batch is B06) → upload the zip to `images`. Order: 049–053, then chapter 2, 3, 4.
2. Render: `bash tools/render.sh N09 N10` once 049–053 exist (background process, about 7 min a clip when nothing else runs), upload each clip to Drive `clips_work`, then `bash tools/finish.sh part 1` as a background process (about 10 min: it makes `…ch01a.mp4` again, identical to the one on Drive, and `…ch01b.mp4`; each is encoded two-pass to 95 MB), check frames, upload `…ch01b.mp4` to the EP23 folder.
3. **Chapter 5 (N35–N42, 1924–1929) is drafted** in `script/ch05.mjs` (6,462 characters, about 7 min; fact rows 189–221) but **not narrated**: `script/script.mjs` adds it only with `EP23_DRAFT=1`. To finish it: remove that switch (plain `...ch05`), `node script/build.mjs`, speak `narration/text/N35.txt` … `N42.txt` with voice-02 → `narration/N35.mp3` …, zip and upload, `$PY script/align.py`, shot rows from 170 with `counts.json` entries and `CARD_BG` for N35, upload the script and fact sheet again. Then chapter 6 (N43–N50, 1929–1933), at most 8 minutes.
4. `film/end.mjs` needs `assets/vo/END.mp3` (the end-card voice: `N08.mp3` in the EP21 narration zip `1vyGgGAtShHWNuSAYhzF7CZbT7KDVXKay`); only for the last part.
5. 030 again (upright and soft).

## How the film code works (EP23)

- `film/gen.mjs`: chapter card (2.3 s) only on a clip with a `title`; `CARD_BG` needs one entry per chapter's first clip (`N03: "braunau_inn_evening"`); `HOOK_FX` per hook clip; a picture held over 9.5 s is split into a wide shot and closer crops at pauses; fade to black at the end of the hook and of each chapter; `reuse: [shot names]` on a line shows pictures made for another clip.
- A `stat` card stays for its whole line: give each number its own line.
- `script/build.mjs` writes `script/clips.json`; `tools/chclips.py <k>` lists the clips of part k (0 = `N01 N02 TITLE`, 12 ends with `END`).
- `tools/render.sh <clips…>` or `ch <k>` (skips clips already in `out/renders/`); `tools/finish.sh part <k>` → `out/deliver/EP23_1080p_<NN>_<name>.mp4`, or `…<name>a.mp4`, `…b.mp4` when the chapter is over about 5 minutes (prints `PART …` per file, then `PARTS-END`; a piece over 99 MB is encoded two-pass to 95 MB); `VB=… bash tools/finish.sh 720 <name> <parts…>` for the 720p copy.
- One gain for the whole film: `tools/gain.txt` = +5.46 dB (narration measured −19.46 LUFS; target −14). Do not re-measure.
- `$PY tools/stills.py [clips] --<prefix>` → still sheets; `$PY tools/frames.py video.mp4 out.jpg t1 t2 …` → frames of a render.

## Drive

Folder `EP23_Hitler_Veedillathavan_Mudhal`: `10ZWqHEkZTMfl6jrelOYsmAXk6uWtCjYr` (parent `1WqhshH9XcvNUna4lzyS692eidgWQfeS1`). Pictures folder `images`: `1qxd24FYRXbd2K_OqfWvzpgXaDQQfQ67U`.

| File | Id |
|---|---|
| EP23_narration_N01-N10_voice02.zip (hook and chapter 1) | `1wzvDc2gEA8zSgXoDAsW-CyV326ThswgP` |
| images/EP23_B01_images_001-010.zip | `1CNvtwG5ktJ8ngQ6p7fvM1oV4k9TVBATp` |
| images/EP23_B02_images_011-020.zip | `1KH1lDddL-EK0idBP6aKcRnc-Od6HoABM` |
| EP23_1080p_00_hook_title.mp4 | `1XI_otP6j5p9-8UvGdTlPM0X8sPc4bYoO` |
| EP23_narration_N11-N18_voice02.zip (chapter 2) | `1jgakdUY2s3gpYmHdVZTQonNh3LvC8Bh_` |
| EP23_SCRIPT_TA_hook_ch1_ch2.md | `111vHFCU-mDFx9sHi_vCKM8AQcntYNfZa` |
| EP23_FACT_SHEET_hook_ch1_ch2.md | `16pMOQ7voGhbaWTeyrBpxvT-0HDvbdF0f` |
| images/EP23_R1_images_faces_004-008-010-012-017.zip (redo: unpacks over the batch zips) | `1pm022Ys_4QL4B4gO6Ix5-c9H1eU3-QKo` |
| images/EP23_cast.zip (reference pictures → `google_drive/ep23_pics/cast/`) | `15aQXIRA92aKuxwj1dmPtSdyWbj73ZFj8` |
| EP23_narration_N10-N11-N14_February_voice02.zip (replaces those three clips; unpack after the two narration zips) | `1bY7Ux0KJvlLCbxkn1DODiFJL-f3mEP6G` |
| EP23_1080p_00_hook_title_v2_film.mp4 | `1iSiADf9AbmB7-4wXWUknUMWXgRe9nfa6` |
| images/EP23_B03_images_021-029.zip | `1lF6TpKM5q_P4r5aOdjdcWxos-R7_TB1C` |
| images/EP23_R2_images_face_012.zip (redo) | `1_YNsPKniSzj9sBRSPejDQbYifFb99S6V` |
| images/EP23_cast_v2.zip (adds `Y18.jpg`, `A18.jpg`, the new `A.jpg`; use this one) | `1kgFxrmZX3wZ5Zucv8bJgxN7Z1zqQ2E6r` |
| EP23_1080p_00_hook_title_v3_film.mp4 | `1ZUQv08d_G3ENbjFJf5NDf0r69p7KD993` |
| images/EP23_B04_images_030-039_no034.zip | `1QBM6IY0kfZMrcMWSIU6GG5sOEyBcrizt` |
| EP23_narration_N19-N26_voice02.zip (chapter 3) | `1XU-2Qvk4UHZNPB_Sq9QdGDMB9r3cmYKy` |
| EP23_SCRIPT_TA_hook_ch1-ch3.md | `1ZzlHF389mA2r5pXXV3o9_78Do4R9CuHR` |
| EP23_FACT_SHEET_hook_ch1-ch3.md | `11z-vIXX8s6p0LvTtaf91FT2Fqi2vk0KQ` |
| images/EP23_B05_images_034_040-048.zip (also holds `cast_S_photo_reference_only.jpg` → `cast/S_photo.jpg`) | `1NsUWqquvkCX1v2PFQbKynhSBAFBSpC8H` |
| EP23_narration_N27-N34_voice02.zip (chapter 4) | `11UhsJK6cpSgeZ20IemjfSThESJqrlWpX` |
| EP23_SCRIPT_TA_hook_ch1-ch4.md (current) | `1UOmMgCQKqYqHy0Jvnlr6QbHVtTG-b1T4` |
| EP23_FACT_SHEET_hook_ch1-ch4.md (current) | `1mpdZqHN19WgZiYNoJazXpR8s5f3fsw7C` |
| folder `clips_work` (rendered clips, so a wipe does not cost the render time; not for viewing) | `1x1r_EPhLK4_Y0QA2ls3ACgVcps-S9Zop` |
| clips_work/N03.mp4 | `1YVK6GmdPNa_ybb3JBTIAsZnw3z-SINd2` |
| clips_work/N04.mp4 | `1t6GOn9uXxMKpcwTVq2MUQB4vY577K8V0` |
| clips_work/N05.mp4 | `1tDB0r3I3OpiXNsUWNbmvgJRKMkkFNcsq` |
| clips_work/N06.mp4 | `1E6NF4hQtlNWwQjMEaNp3XU5qAuvkVRlF` |
| clips_work/N07.mp4 | `1q-tjKlCStImZnN0bFUFaTFPuCL2kpnKV` |
| clips_work/N08.mp4 | `1_nVkJSB11lDOHgw-se2iEtWfWcUu-egQ` |
| **EP23_1080p_01_ch01a.mp4** (chapter 1, first half: N03–N06, 303.5 s, 97.6 MB, two-pass; −12.6 LUFS, peak −2.0 dBFS) | `13P9X8HMM6z-BWDEvn6dBGzWRmNv-RnPf` |
| EP23_OUTLINE.md | `1TVRmNj24nJn1oTHJUfdluQAr5voGH_bo` |
| EP23_SCRIPT_TA_hook_ch1.md | `1Yj9njt2sHz-c0ZYLgdfzRipFGrJMsOA_` |

## Picture checks

| Batch | Pictures | Result |
|---|---|---|
| B05 | 034, 040–048 (N05, N07, N08, N09) | all usable, 16:9, no lettering. 041: he stands in the middle of the Ring with the opera house behind, looking at the camera (the row asked for him small in the street): kept. 043: his hat near the top (`SHIFT` 60). 044: the youth in the exam hall reads early twenties rather than eighteen. 042, 047: the doctor is the same bearded actor in both (`SHIFT` 24, 30). |
| B04 | 030–039 without 034 | usable. 030 upright format, soft (redo). 035: blurred sign shapes over two shops, not readable. 037, 039: hats near the top (`SHIFT` 64 and 30). The youth matches picture 008. |
| B03 | 021–029 (N03, N04) | all usable. 023: the mother looks nearer forty than twenty-eight; the father stands high in the frame (`SHIFT` 50). 028: the "meadow" is a dry field at the edge of a village. |
| R2 | 012 | same young face as 004; good |
| B02 | 011–020 (N01 rows 11–12, N02) | all usable |
| B01 | 001–010 (N01) | all usable. Notes in `shots/CAST.md`: 008 figure walks up the steps, 009 extra small stones, 010 hat and a blank dark cloth |

## After a full wipe

Only the pushed branch survives. `out/`, `narration/*.mp3`, `/tmp` tools and `google_drive/` are gone.

1. `git fetch -q origin arena/d486087a-hyperframes && git reset -q --hard FETCH_HEAD`
2. `bash projects/nk-ep23-hitler/tools/setup.sh` as a background process (about 2.5 min), then `. /tmp/hfenv.sh` in every shell.
3. Download from Drive into `google_drive/`: every narration zip and every `EP23_B*` / `EP23_R*` picture zip in the tables above.
4. `unzip -o -q ../../google_drive/EP23_narration_*.zip -d narration/` for each narration zip; `bash tools/restore.sh` (unpacks the picture zips into `google_drive/ep23_pics/raw/NNN.jpg`, relinks `out/raw`, `shared/vo`, `shared/plates`, rebuilds `out/img`).
5. `node script/build.mjs && $PY script/align.py && python3 shots/expand.py`.
6. Rendered clips: download every `N??.mp4` of the Drive folder `clips_work` and `mv ../../google_drive/N??.mp4 out/renders/` (`tools/render.sh` skips clips that are there). Regenerate the film folders first: `node film/gen.mjs N03 N04 …`.
