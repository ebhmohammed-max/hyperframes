# EP19 — 2050-ல் உலகம் எப்படி இருக்கும்? (What will the world be like in 2050?)

Status on 21 Nov 2026: **script, narration, shot list and graphics plan done; all 127 pictures made, remakes done; render started 22 Nov.** Not rendered yet.

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
| B07 | 060–069 | `EP19_B07_images_060-069.zip` `1GdF-46QUNxaiQ6IRO2drqks9iclMPOW9` | all usable |
| B08 | 070–079 | `EP19_B08_images_070-079.zip` `1ytz9CvwLi2p6KRvNR8dxnxcFCVdt7FgL` | all usable; 070 shows a sliver of Nila's cheek in shadow (kept) |
| B09 | 080–089 | `EP19_B09_images_080-089.zip` `1cruW7LXpj1yWy_uQlBD8X0oLqG6V8ap8` | all usable |
| B10 | 090–099 | `EP19_B10_images_090-099.zip` `1XcwBUP_d8ry1_nhA5keJ3-klALQSYjP_` | all usable; 092 remake (eye chart letters readable) |
| B11 | 100–109 | `EP19_B11_images_100-109.zip` `15WijqiuINaex2o1XPvZg89NVdUOG6FhU` | all usable |
| B12 | 110–119 | `EP19_B12_images_110-119.zip` `1eYJSDjpCYN7INTFttRRzRbH7ibV5_bpB` | all usable; 114 shows four people, not five (the voice gives no count; kept) |
| B13 | 120–127 without 123 | `EP19_B13_images_120-127_no123.zip` `1kVz6Ksj-jJFt2BglmQ9Bu4unj4oeskxM` | all usable; 123 (grey window) still to make, with 122 as reference |
| R1 | remakes 004, 019, 043, 092 | `EP19_R1_images_004-019-043-092.zip` `1hvTKw3kXO_IoCAJa1Pd5pxR0HpBpMpBN` | 004 woman's hands with bangles; 019 packed crossing; 043 plain frame, no garland; 092 the same picture with the eye chart blurred locally (no new generation) |
| R2 | 123 | `EP19_R2_images_123.zip` `1XvN7JpKPvnqXp0QO_J4KW7Su31yYh-L-` | the grey window, made from 122; the two halves of the split match |

Next: `$PY tools/next.py 10`, ten `generate_image` calls per turn into `out/raw/NNN.jpg` (rows marked `[nila]` get `out/cast/nila.jpg` as reference), then `bash tools/restore.sh`, `$PY tools/batch.py <batch> <first> <last> [two numbers to show large]`, view `google_drive/_sheet_E19Bnn.jpg`, upload the zip to the `images` folder, commit.

## Drive

Root "NK Documentaries" `1WqhshH9XcvNUna4lzyS692eidgWQfeS1` → **`EP19_2050_Ulagam_Eppadi_Irukkum` `1mWB79izepuz-ARO95VQW4E3gtwJpFQs7`**, `images` folder `1tKNhl0BGv4x3fCn_Zn-V3KmVIGBnvq55`.

| File | Drive id |
|---|---|
| `EP19_SCRIPT_TA.md` | `19jxtj5PKo5LR7fc5xTLhxWw5K0mCwt6x` |
| `EP19_FACT_SHEET.md` | `1-NPWFelfdEGy1CtFWY60XRbJ2O1m_fHr` |
| `EP19_narration_scratch_voice02.zip` (N01–N08) | `1FhnLkFI8zuoPej9ibT7U0HOBa7paHyjz` |
| `EP19_SHOTLIST.md` | `1XV0XrEUCgTCzNiDgHvJl2dTzdhZ1aSQD` |

## Delivery (22 Nov 2026)

Render of all nine clips done (about 75 minutes on 2 CPUs; 6 to 11.6 s of work per film second). Film length 513.5 s. Sound gain +2.57 dB with a limiter.

| File | Drive id |
|---|---|
| `EP19_1080p_01_hook_title.mp4` (69.1 s) | `1hyJbUmzCKpenFW1RsV6cxxYozIbUHeVX` |
| `EP19_1080p_02_ch1.mp4` (53.0 s) | `1kwH4yhXBPkdVGXyRkTGKkI_lzeSfVN4F` |
| `EP19_1080p_03_ch2.mp4` (75.8 s) | `1lthXgRJdypG2Y3ESUzzlApR_kobsn0ex` |
| `EP19_1080p_04_ch3.mp4` (72.7 s) | `1Ihkuh95MzQBMyPvCCR5MpENSI8b6N54t` |
| `EP19_1080p_05_ch4.mp4` (75.9 s) | `1PQoovLq08-yuLIlELPjNMJDSEURGjc_A` |
| `EP19_1080p_06_ch5.mp4` (60.0 s) | `1UA3ASOVifSpNUB7ol8qlWcbwMuXUNDfD` |
| `EP19_1080p_07_ch6_endcard.mp4` | PENDING7 |
| `EP19_2050_full_720p.mp4` | PENDING720 |
| `EP19_FACT_SHEET_v2.md` | `1vvyEoQBodRR35ZVmwYv2p1oNV7FPixAW` |
| `EP19_SCRIPT_TA_v2.md` | `13Bevry85WRmhYiSVf01yxEgQ3qaGv74z` |

N07 was rendered twice: the first render broke the caption "10-ல" at its hyphen; `film/gen.mjs` now keeps such tokens on one line (checked on the renders: no other caption was affected).

## Changes after the first upload

- 21 Nov: N03 line 4 was split in two (Tamil Nadu, then Sri Lanka) so that each has its own number card; the narration audio is unchanged. The script is now 70 lines; N03 lines after it moved up by one. Picture numbers did not change, but the file names inside the zips B04–B06 still carry the old line numbers for 041–051 (the number at the front is what counts). `EP19_SCRIPT_TA_v2.md` on Drive replaces `EP19_SCRIPT_TA.md`.
- 21 Nov: N07 graphics checked on stills (chapter card, 10–25 செ.மீ, 19.7 செ.மீ, 76%, big 21.6 கோடி, 80% வரை, the three flash words, the two-window split with its left half): all correct; the right half of the split waits for 123.
- 21 Nov: N06 graphics checked on stills (chapter card, hundred dots, sugar bars, big 3.9 கோடி, 9.2 கோடி card): all correct.
- 21 Nov: N05 graphics checked on stills. Two fixes: the 2035/2050 timeline labels ran into each other (now three short points: 2020, 2035, 2050); the IEA card now reads "~90%" because the report says "almost 90%" (the voice says 90%).
- Graphics checked on stills for N01–N04, all pictures in place (chapter cards, bars incl. the water bars, number cards, timeline, hundred dots incl. the growing 55 → 68, big numbers, subscribe pop-up): all correct. Note for stills: film time in N02–N07 = voice time + 2.3 s (chapter card).

## Open points

- Five figures rest on press reports only: list at the end of `FACT_SHEET.md`.
- The voice is a scratch voice; nobody has listened to it. A Tamil speaker should read the script once.
- Chapter 4 uses a 2030 jobs figure because no credible 2050 figure exists; the narration says so.

## After a full wipe of the workspace

1. `git fetch -q origin arena/d486087a-hyperframes && git reset -q --hard FETCH_HEAD`
2. `bash projects/nk-ep19-2050/tools/setup.sh` through a background process (builds `/tmp/hf`, `/tmp/nkvenv`, `/tmp/chromium`, `/tmp/hfenv.sh`); then `. /tmp/hfenv.sh` in every shell.
3. Download from the Drive folder into `<repo>/google_drive/`: the narration zip (unzip into `narration/`), `EP19_cast.zip` and every `EP19_B*_images_*.zip` and `EP19_R*_images_*.zip` from `images` (`download_file` with only `file_id` saves them there).
4. `bash tools/restore.sh` (relinks `out/raw` and `out/cast`, unpacks the zips, rebuilds `out/img`).
