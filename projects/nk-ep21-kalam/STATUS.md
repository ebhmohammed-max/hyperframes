# EP21 status: அப்துல் கலாமின் கடைசி நாள் (A.P.J. Abdul Kalam, 27 July 2015)

Started 23 Nov 2026. Topic chosen by the user ("APJ Abdul Kalaam"), length about 6–7 minutes. Copied from `projects/nk-ep20-capstone/` (same film code, tools and delivery pattern; that project's STATUS.md has the full recipe, the wipe recovery and the stills-check method).

Angle: the last day as the frame (flight, hill road, the guard, the stage), with three flashbacks (the newspaper boy, ninth of 25, the 1979 failure and Satish Dhawan), ending on what he left behind and his question "what will you be remembered for?".

## Where it stands

| Step | State |
|---|---|
| Research, script v1 (54 lines, 5,814 characters, N01–N07) | done: `script/script.mjs`, `SCRIPT_TA.md` |
| Fact sheet | done: `FACT_SHEET.md` (labels U S F P O; "To check before publishing") |
| Scratch narration, voice-02 | done 23 Nov: N01–N07 new, N08 (end card) from the EP20 zip; `align.py` 0 flagged; voice about 391 s, film about 420 s (7 min) |
| Shot list | done: `shots/shots.txt` 100 rows, `SHOTLIST.md`, rules in `shots/CAST.md` |
| Pictures | **10 of 100** (B01 checked, on Drive) |
| Film code for EP21 | **not adapted yet**: `film/gen.mjs` (HOOK_FX, CARD_BG, pop-up line, titles "EP20"→"EP21"), `film/title.mjs` (three plates, title words அப்துல் கலாம் · கடைசி நாள்), `film/end.mjs` (ids); clip folders `film/N01…N07, TITLE, END` to be made |
| Stills checks | not started |
| Render, parts, 720p, upload | not started |

Clip voice ends (s): N01 43.0, N02 55.7, N03 37.5, N04 58.2, N05 73.0, N06 63.0, N07 58.8.

Planned card pictures (CARD_BG): N02 `airliner_monsoon_climb`, N03 `young_man_selection_gate`, N04 `control_room_1979`, N05 `jeep_three_soldiers`, N06 `stage_podium_wide`, N07 `modest_room_door_open`.

## Drive

Folder `EP21_Abdul_Kalam_Kadaisi_Naal` `1TXMKW_de6RjNOJ7r-cEQnA2Lz7JYevHH`; `images` `1rp_9bvilp2voomLnTVR66mzVNq3BeM71`.

| File | Drive id |
|---|---|
| EP21_SCRIPT_TA.md | 1_N5PTL9Il4jmSpjGiBSLgXTOXD6Yn-Ju |
| EP21_FACT_SHEET.md | 1VuF6vvj4X9mh5dXigNGQzl3iKVkl7wCQ |
| EP21_SHOTLIST.md | 1J0ht77U41y30GXn8TmeiXox5EwgfmwBM |
| EP21_narration_scratch_voice02.zip (N01–N08) | 1vyGgGAtShHWNuSAYhzF7CZbT7KDVXKay |

| Batch | Pictures | Drive id (images) |
|---|---|---|
| B01 | 001–010 | 1oEU-0GXiRgsXqq5joqiBqal0YgMkmTD3 |

## Picture batches

Each turn: `python3 tools/next.py 10` → ten `generate_image` calls to `google_drive/ep21_pics/raw/NNN.jpg` → `$PY tools/sheet.py a b` → `$PY tools/batch.py <batch> a b [two numbers to show large]` → view `google_drive/_sheet_E21Bnn.jpg` → upload the zip from `google_drive/ep21_up/` to `images` → this file → commit, push.

## For the redo pass

| Picture | Fault | Change for the remake |
|---|---|---|
| 004 `old_man_at_podium_back` | the hall is full of schoolchildren in uniform; the lecture was to management students in their twenties | say "adult postgraduate students in their twenties in everyday clothes, no children, no uniforms" |
| 002 `hall_clock_evening` | the clock reads about six o'clock, the line says 6:35 (small in the frame) | make again once; keep if it fails again |

## Open points

- The script and the scratch voice have not been heard by a person.
- No face of Dr Kalam is shown (generated illustrations only; rule in `shots/CAST.md`).
- Items 1–5 of "To check before publishing" in `FACT_SHEET.md` (the two books were not opened; the possessions list is a press list).

## After a full wipe

`git fetch -q origin arena/d486087a-hyperframes && git reset -q --hard FETCH_HEAD`; `bash tools/setup.sh` (through a background process, about 2.5 minutes); download the narration zip and every picture zip listed above into `<repo>/google_drive/`; unzip the narration into `narration/`; `bash tools/restore.sh`.
