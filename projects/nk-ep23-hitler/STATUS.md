# EP23 status: ஹிட்லர்: வீடில்லாதவனில் இருந்து ராட்சசன் வரை (Hitler: From Homeless to Monster)

Target 105 minutes, 12 chapters and a hook. Plan and chapter table: `OUTLINE.md`. Built and delivered chapter by chapter.

## Where it stands (26 Nov 2026)

| Part | Script | Narration | Timing | Pictures | Film | On Drive |
|---|---|---|---|---|---|---|
| Hook (N01–N02) + TITLE | done | done, 92.3 s | 0 flagged | 001–020 made (all) | built; render of TITLE, N01, N02 → `out/renders/`; part `EP23_1080p_00_hook_title.mp4` (106.4 s, 80.5 MB) made, frames checked, uploaded | narration, B01, B02 |
| Ch 1 (N03–N10) | done | done, 535.9 s | 0 flagged | shot rows written (33 rows, 021–053), none generated | `node film/gen.mjs N03 … N10` works (reports missing pictures) | narration |
| Ch 2 to 12 | not written | | | | | |

Running time so far: 10 min 28 s of narration (hook 1 min 32 s, chapter 1 8 min 56 s). Film lengths: N01 43.5 s, N02 50.8 s, TITLE 12 s, chapter 1 546 s.

## Next steps

1. Pictures 021–053, 10 per turn: `python3 tools/next.py 10` → generate to `google_drive/ep23_pics/raw/NNN.jpg` → `$PY tools/sheet.py a b` → `$PY tools/batch.py <batch> a b` → upload the zip to `images`.
2. Render chapter 1: `bash tools/render.sh ch 1` as a background process (about 6 s per film second: 55 min, so over two turns: N03–N06, then N07–N10), then `bash tools/finish.sh part 1`, upload.
3. Chapter 2 (N11–N18) as `script/ch02.mjs`, import it in `script/script.mjs`, `node script/build.mjs`, narration, `$PY script/align.py`.
4. `film/end.mjs` needs `assets/vo/END.mp3` (the end-card voice: `N08.mp3` in the EP21 narration zip `1vyGgGAtShHWNuSAYhzF7CZbT7KDVXKay`); only for the last part.

## How the film code works (EP23)

- `film/gen.mjs`: chapter card (2.3 s) only on a clip with a `title`; `CARD_BG` needs one entry per chapter's first clip (`N03: "braunau_inn_evening"`); `HOOK_FX` per hook clip; a picture held over 9.5 s is split into a wide shot and closer crops at pauses; fade to black at the end of the hook and of each chapter; `reuse: [shot names]` on a line shows pictures made for another clip.
- A `stat` card stays for its whole line: give each number its own line.
- `script/build.mjs` writes `script/clips.json`; `tools/chclips.py <k>` lists the clips of part k (0 = `N01 N02 TITLE`, 12 ends with `END`).
- `tools/render.sh <clips…>` or `ch <k>` (skips clips already in `out/renders/`); `tools/finish.sh part <k>` → `out/deliver/EP23_1080p_<NN>_<name>.mp4`; `VB=… bash tools/finish.sh 720 <name> <parts…>` for the 720p copy.
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
| EP23_OUTLINE.md | `1TVRmNj24nJn1oTHJUfdluQAr5voGH_bo` |
| EP23_SCRIPT_TA_hook_ch1.md | `1Yj9njt2sHz-c0ZYLgdfzRipFGrJMsOA_` |

## Picture checks

| Batch | Pictures | Result |
|---|---|---|
| B02 | 011–020 (N01 rows 11–12, N02) | all usable |
| B01 | 001–010 (N01) | all usable. Notes in `shots/CAST.md`: 008 figure walks up the steps, 009 extra small stones, 010 hat and a blank dark cloth |

## After a full wipe

Only the pushed branch survives. `out/`, `narration/*.mp3`, `/tmp` tools and `google_drive/` are gone.

1. `git fetch -q origin arena/d486087a-hyperframes && git reset -q --hard FETCH_HEAD`
2. `bash projects/nk-ep23-hitler/tools/setup.sh` as a background process (about 2.5 min), then `. /tmp/hfenv.sh` in every shell.
3. Download from Drive into `google_drive/`: every narration zip and every `EP23_B*` / `EP23_R*` picture zip in the tables above.
4. `unzip -o -q ../../google_drive/EP23_narration_*.zip -d narration/` for each narration zip; `bash tools/restore.sh` (unpacks the picture zips into `google_drive/ep23_pics/raw/NNN.jpg`, relinks `out/raw`, `shared/vo`, `shared/plates`, rebuilds `out/img`).
5. `node script/build.mjs && $PY script/align.py && python3 shots/expand.py`.
