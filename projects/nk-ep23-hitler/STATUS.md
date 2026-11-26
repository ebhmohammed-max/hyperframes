# EP23 status: ஹிட்லர்: வீடில்லாதவனில் இருந்து ராட்சசன் வரை (Hitler: From Homeless to Monster)

Target 105 minutes, 12 chapters and a hook. Plan and chapter table: `OUTLINE.md`. Built and delivered chapter by chapter.

## Where it stands (26 Nov 2026)

| Part | Script | Narration | Timing | Pictures | Film | On Drive |
|---|---|---|---|---|---|---|
| Hook (N01–N02) | done | done, 92.3 s | 0 flagged | 001–010 of 20 made (N01 rows 1–10; rows 011, 012 and all of N02 to do) | not built | narration, B01 |
| Ch 1 (N03–N10) | done | done, 535.9 s | 0 flagged | shot list not written | not built | narration |
| Ch 2 to 12 | not written | | | | | |

Running time so far: 10 min 28 s of narration (hook 1 min 32 s, chapter 1 8 min 56 s).

## Next steps

1. Shot list: N01 rows 011–012, N02 (about 8 pictures), chapter 1 (about 30 pictures: looks L and V, refs B, Y, K, F). `shots/counts.json` must list every clip that has rows.
2. `film/gen.mjs` changes for the long film (not done yet):
   - chapter card only on a clip that has a `title` (now: every clip after the first); a clip without a title starts like the hook (lead 0.4 s);
   - hook effects (`HOOK_FX`) and `CARD_BG` are still EP22's: write EP23's;
   - the EP22 counter pill (`fx.no`, `FACTS`) is unused: remove the `FACTS` import;
   - a picture held longer than about 9 s is cut into two shots (wide, then a closer crop) at a pause;
   - `/^N\d\d$/` clip ids stay (N01 … N98).
3. `film/title.mjs` (title text from `TITLE` in `script/script.mjs`), `film/end.mjs` (uses `N08.mp3` as the end-card voice in EP22: EP23 needs `END.mp3`, the same end-card narration, from the EP21 narration zip `1vyGgGAtShHWNuSAYhzF7CZbT7KDVXKay`, file `N08.mp3`).
4. `tools/render.sh`, `tools/finish.sh`, `tools/stills.py` still carry EP22's clip lists: make them take a chapter (clip list from `script/lines.json`), one 1080p part per chapter, one gain for the whole film (measure on the hook and chapter 1, then keep).
5. Then per chapter: script → narration → timing → pictures → render → part to Drive.

## Drive

Folder `EP23_Hitler_Veedillathavan_Mudhal`: `10ZWqHEkZTMfl6jrelOYsmAXk6uWtCjYr` (parent `1WqhshH9XcvNUna4lzyS692eidgWQfeS1`). Pictures folder `images`: `1qxd24FYRXbd2K_OqfWvzpgXaDQQfQ67U`.

| File | Id |
|---|---|
| EP23_narration_N01-N10_voice02.zip (hook and chapter 1) | `1wzvDc2gEA8zSgXoDAsW-CyV326ThswgP` |
| images/EP23_B01_images_001-010.zip | `1CNvtwG5ktJ8ngQ6p7fvM1oV4k9TVBATp` |

## Picture checks

| Batch | Pictures | Result |
|---|---|---|
| B01 | 001–010 (N01) | all usable. Notes in `shots/CAST.md`: 008 figure walks up the steps, 009 extra small stones, 010 hat and a blank dark cloth |

## After a full wipe

Only the pushed branch survives. `out/`, `narration/*.mp3`, `/tmp` tools and `google_drive/` are gone.

1. `git fetch -q origin arena/d486087a-hyperframes && git reset -q --hard FETCH_HEAD`
2. `bash projects/nk-ep23-hitler/tools/setup.sh` as a background process (about 2.5 min), then `. /tmp/hfenv.sh` in every shell.
3. Download from Drive into `google_drive/`: every narration zip and every `EP23_B*` / `EP23_R*` picture zip in the tables above.
4. `unzip -o -q ../../google_drive/EP23_narration_*.zip -d narration/` for each narration zip; `bash tools/restore.sh` (unpacks the picture zips into `google_drive/ep23_pics/raw/NNN.jpg`, relinks `out/raw`, `shared/vo`, `shared/plates`, rebuilds `out/img`).
5. `node script/build.mjs && $PY script/align.py && python3 shots/expand.py`.
