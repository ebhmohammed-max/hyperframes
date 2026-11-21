# EP19 — 2050-ல் உலகம் எப்படி இருக்கும்? (What will the world be like in 2050?)

Status on 21 Nov 2026: **script, narration, shot list and graphics plan done; pictures 59 of 127 made.** Not rendered yet.

Topic and length were set by the user: their own topic, about 8 minutes. Project copied from `../nk-ep18-vaultb` (same tools, same look).

## What exists

- `script/script.mjs` v1: 70 lines in seven clips (hook + six chapters). `SCRIPT_TA.md`, `script/lines.json` and `narration/text/` are built from it with `node script/build.mjs`.
- `FACT_SHEET.md`: every figure with source, year and scenario; five points to check before publishing.
- Narration N01–N07 with the scratch voice `voice-02`: 464.4 s. `narration/align.json`: 70 lines, 0 flagged. `N08.mp3` (end card voice) is the same file as in EP16–EP18.
- `shots/shots.txt`: 127 pictures, 0 count mismatches (`python3 shots/expand.py`). One reference picture (`nila`, `shots/CAST.md`).
- Clips generate without error: `node film/gen.mjs N01 … N07`, `node film/title.mjs`, `node film/end.mjs`.

## Shape

| Clip | Chapter | Lines | Narration s | Pictures |
|---|---|---|---|---|
| N01 | Hook: Nila is born tonight; two things are already decided | 10 | 56.0 | 001–018 |
| N02 | 01 · 970 கோடி பேர் (people) | 9 | 49.8 | 019–032 |
| N03 | 02 · நரைக்கும் உலகம் (ageing: first decided item) | 11 | 72.6 | 033–051 |
| N04 | 03 · நகரம், தண்ணி, சோறு (city, water, food) | 10 | 69.5 | 052–069 |
| N05 | 04 · வேலை, காசு, கரண்ட் (work, money, power) | 10 | 72.7 | 070–089 |
| N06 | 05 · உடம்பு என்ன சொல்லுது (health) | 8 | 56.8 | 090–102 |
| N07 | 06 · ஒரு சாண் கடல் (sea: second decided item, then the open question) | 12 | 87.0 | 103–127 |

Expected film length: about 8 min 35 s (narration 464 s + title 12 s + six chapter cards + end card 17 s).

The loop: the hook says two things about 2050 are already decided. Chapter 2 pays the first (everyone who will be 60 in 2050 is already born), chapter 6 pays the second (10–25 cm of sea-level rise by 2050 in every scenario). Everything else is said to be open; the film ends on a question to the viewer.

On-screen labels (new set for this episode): U ஐ.நா. கணிப்பு · R ஆய்வு கணிப்பு · S ஒரு பாதை, கணிப்பு இல்ல · F பதிவான உண்மை · O கருத்து · I கற்பனை காட்சி.

Graphics used (`film/fx.mjs`): `vs` bars ×5, `stat` cards ×11, `big` number ×4, hundred `dots` ×3 (full screen; the dots can now grow, 55 → 68), `flash` words ×4 (one struck out), `line` ×2, `split` ×1 (two possible mornings in 2050).

## Picture batches

| Batch | Pictures | Drive file (in `images`) | Notes |
|---|---|---|---|
| cast | `nila` | `EP19_cast.zip` `1TvmKSx96mV-A0v0RUOY5diBljPwDZEN-` | |
| B01 | 001–009 | `EP19_B01_images_001-009.zip` `11tOggwU-QtIT4zkkbF-DUDj_3peU-HdT` | all usable; 004 the hands look like a man's (line is about Nila): remake candidate |
| B02 | 010–019 | `EP19_B02_images_010-019.zip` `10od336EGh6qUIC0aLxCnZo734ywacDpA` | all usable; 019 the crossing is not crowded enough for the "crowd" word and the title: remake candidate |
| B03 | 020–029 | `EP19_B03_images_020-029.zip` `1c1axdb0QZUhkx4h9eoivkxihhDMUodGa` | all usable |
| B04 | 030–039 | `EP19_B04_images_030-039.zip` `1XCYLxZCz-sds8kQfOgEkXp5-lswvc3wG` | all usable; 034 (grandmother at 79) was made with 033 (at 55) as reference so the two match |
| B05 | 040–049 | `EP19_B05_images_040-049.zip` `1jkAZPKlPmPa1_pREzlW2-6SPO7gTmbxC` | all usable; 043 the garland on the school photograph reads as a memorial picture in a Tamil home: remake without it |
| B06 | 050–059 | `EP19_B06_images_050-059.zip` `1HKbUbQxusDiJ6YJ7z3kLiDR4IwhJnLjq` | all usable; 050 made with `nila` and 034 as references |

Next: `$PY tools/next.py 10`, ten `generate_image` calls per turn into `out/raw/NNN.jpg` (rows marked `[nila]` get `out/cast/nila.jpg` as reference), then `bash tools/restore.sh`, `$PY tools/batch.py <batch> <first> <last> [two numbers to show large]`, view `google_drive/_sheet_E19Bnn.jpg`, upload the zip to the `images` folder, commit.

## Drive

Root "NK Documentaries" `1WqhshH9XcvNUna4lzyS692eidgWQfeS1` → **`EP19_2050_Ulagam_Eppadi_Irukkum` `1mWB79izepuz-ARO95VQW4E3gtwJpFQs7`**, `images` folder `1tKNhl0BGv4x3fCn_Zn-V3KmVIGBnvq55`.

| File | Drive id |
|---|---|
| `EP19_SCRIPT_TA.md` | `19jxtj5PKo5LR7fc5xTLhxWw5K0mCwt6x` |
| `EP19_FACT_SHEET.md` | `1-NPWFelfdEGy1CtFWY60XRbJ2O1m_fHr` |
| `EP19_narration_scratch_voice02.zip` (N01–N08) | `1FhnLkFI8zuoPej9ibT7U0HOBa7paHyjz` |
| `EP19_SHOTLIST.md` | `1XV0XrEUCgTCzNiDgHvJl2dTzdhZ1aSQD` |

## Changes after the first upload

- 21 Nov: N03 line 4 was split in two (Tamil Nadu, then Sri Lanka) so that each has its own number card; the narration audio is unchanged. The script is now 70 lines; N03 lines after it moved up by one. Picture numbers did not change, but the file names inside the zips B04–B06 still carry the old line numbers for 041–051 (the number at the front is what counts). `EP19_SCRIPT_TA_v2.md` on Drive replaces `EP19_SCRIPT_TA.md`.
- Graphics checked on stills for N01–N04 (chapter cards, bars, number cards, timeline, hundred dots incl. the growing 55 → 68, big number, subscribe pop-up): all correct.

## Open points

- Five figures rest on press reports only: list at the end of `FACT_SHEET.md`.
- The voice is a scratch voice; nobody has listened to it. A Tamil speaker should read the script once.
- Chapter 4 uses a 2030 jobs figure because no credible 2050 figure exists; the narration says so.

## After a full wipe of the workspace

1. `git fetch -q origin arena/d486087a-hyperframes && git reset -q --hard FETCH_HEAD`
2. `bash projects/nk-ep19-2050/tools/setup.sh` through a background process (builds `/tmp/hf`, `/tmp/nkvenv`, `/tmp/chromium`, `/tmp/hfenv.sh`); then `. /tmp/hfenv.sh` in every shell.
3. Download from the Drive folder into `<repo>/google_drive/`: the narration zip (unzip into `narration/`), `EP19_cast.zip` and every `EP19_B*_images_*.zip` from `images`.
4. `bash tools/restore.sh` (relinks `out/raw` and `out/cast`, unpacks the zips, rebuilds `out/img`).
