# EP23 status: ஹிட்லர்: வீடில்லாதவனில் இருந்து ராட்சசன் வரை (Hitler: From Homeless to Monster)

Target 105 minutes, 12 chapters and a hook. Plan and chapter table: `OUTLINE.md`. Built and delivered chapter by chapter.

## Second review, 26 Nov 2026 (user: show his real face, young face too, film feel, say "February")

- **February:** the voice mispronounced "பிப்ரவரி". The spoken text now says "February" in English (N10, N11, N14 spoken again, aligned, 0 flagged; captions keep பிப்ரவரி). Later scripts: write "February" in `say`.
- **Faces:** the old rule (no face) is gone; see `shots/CAST.md`. Reference pictures in `out/cast/` (Drive `images/EP23_cast.zip`); `shots/prompts.json` lists the pictures to pass for each row (`python3 tools/next.py n` prints them). Hook pictures made again with faces: 004, 008, 010, 012, 017 (Drive `images/EP23_R1_images_faces_…zip`; the faceless first versions are in the B01 and B02 zips).
  - 012 (the doorway close-up) was made again from `cast/A.jpg` in the next turn and is back in the film (Drive `images/EP23_R2_images_face_012.zip`).
  - Shot rows 021–090 rewritten so that he, his parents, Kubizek, Hanisch, Dr Bloch and Morgenstern are seen from the front (38 rows changed; 8 shot names changed).
- **Film look:** 2.2:1 frame with black bars of 104 px (`BAR` in `film/gen.mjs`, also in `film/title.mjs`); evidence tag inside the top bar; captions just above the bottom bar; `SHIFT` moves a picture down when a head sits high; every picture prompt now asks for a 35mm film still composed for that crop. Added in the turn after: grain 0.15 at 24 fps, a faint flicker layer (`#p-flick`), dissolves of 0.5 and 0.9 s in the chapters (the hook keeps its hard cuts), and a low room tone under every clip (`shared/sfx/room-tone.mp3`, 100 s, −30 dB, played at 0.3).
- Hook: `EP23_1080p_00_hook_title_v3_film.mp4` is the current one (all of the above, 012 back in). `…_v2_film.mp4` and the first version stay on Drive.
- **Pictures made:** 001–029 (hook; chapter 1 clips N03 and N04). `out/renders/` has TITLE, N01, N02, N03, N04 in the current look. Next pictures: 030–039 (`python3 tools/next.py 10`; the youth Y now passes `Y18.jpg` and `A18.jpg`).

## Where it stands (26 Nov 2026)

| Part | Script | Narration | Timing | Pictures | Film | On Drive |
|---|---|---|---|---|---|---|
| Hook (N01–N02) + TITLE | done | done, 92.3 s | 0 flagged | 001–020 made (all) | built; render of TITLE, N01, N02 → `out/renders/`; part `EP23_1080p_00_hook_title.mp4` (106.4 s, 80.5 MB) made, frames checked, uploaded | narration, B01, B02 |
| Ch 1 (N03–N10) | done | done, 535.9 s | 0 flagged | shot rows written (33 rows, 021–053), none generated | `node film/gen.mjs N03 … N10` works (reports missing pictures) | narration |
| Ch 2 (N11–N18) | done | done, 598.4 s | 0 flagged | shot rows written (37 rows, 054–090), none generated | `node film/gen.mjs N11 … N18` works (reports missing pictures) | narration |
| Ch 3 to 12 | not written | | | | | |

Running time so far: 20 min 27 s of narration (hook 1 min 32 s, chapter 1 8 min 56 s, chapter 2 9 min 58 s). Film lengths: N01 43.5 s, N02 50.8 s, TITLE 12 s, chapter 1 546 s, chapter 2 609 s. Chapter 2 runs about a minute over its plan (8–9 min): later chapters must stay at 8.5 min to end near 105.

## Next steps

1. Pictures 021–053, 10 per turn: `python3 tools/next.py 10` → generate to `google_drive/ep23_pics/raw/NNN.jpg` → `$PY tools/sheet.py a b` → `$PY tools/batch.py <batch> a b` → upload the zip to `images`.
2. Render chapter 1: `bash tools/render.sh ch 1` as a background process (about 6 s per film second: 55 min, so over two turns: N03–N06, then N07–N10), then `bash tools/finish.sh part 1` as a background process (it cuts the chapter into `…ch01a.mp4` and `…ch01b.mp4` and sizes each under 100 MB), upload both.
3. Pictures 054–090 (chapter 2), then render chapter 2 (`CARD_BG` already has N11).
4. Chapter 3 (N19–N26, 1914–1918) as `script/ch03.mjs`: search first (Salzburg 5 Feb 1914 unfit; Odeonsplatz 2 Aug 1914; List Regiment, dispatch runner; Iron Cross 2nd class Dec 1914, 1st class 4 Aug 1918 proposed by Hugo Gutmann; wounded on the Somme Oct 1916; gassed near Ypres Oct 1918, Pasewalk, 11 Nov 1918). Import it in `script/script.mjs`, `node script/build.mjs`, narration, `$PY script/align.py`.
5. `film/end.mjs` needs `assets/vo/END.mp3` (the end-card voice: `N08.mp3` in the EP21 narration zip `1vyGgGAtShHWNuSAYhzF7CZbT7KDVXKay`); only for the last part.

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
| EP23_1080p_00_hook_title_v3_film.mp4 | `HOOKV3ID` |
| EP23_OUTLINE.md | `1TVRmNj24nJn1oTHJUfdluQAr5voGH_bo` |
| EP23_SCRIPT_TA_hook_ch1.md | `1Yj9njt2sHz-c0ZYLgdfzRipFGrJMsOA_` |

## Picture checks

| Batch | Pictures | Result |
|---|---|---|
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
