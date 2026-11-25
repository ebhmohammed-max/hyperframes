# EP22 status: 27 உண்மைகள்: நீங்க யாருன்னு யோசிக்க வைக்கும் (27 facts that make you question your existence)

Started 25 Nov 2026. Topic typed by the user ("27 Facts That Will Make You Question Your Existence"), length about 5 minutes, about 70 pictures. Copied from `projects/nk-ep21-kalam/` (same film code, tools and delivery pattern; `projects/nk-ep20-capstone/STATUS.md` has the full recipe).

Shape: a hook that says "you are not sitting still", then six chapters from the inside out (your body → what you are made of → time → Earth → sky → universe). One spoken line is one fact. Fact numbers are not spoken; a counter `n/27` sits in the label pill, top left (`fx.no`, new in `film/gen.mjs`). Fact 26 is new: Voyager 1 reached one light-day on 18 Nov 2026. Fact 27 pays off the hook (what happened while the video played).

## Where it stands

| Step | State |
|---|---|
| Research, script v1 (34 lines, 4,050 characters, N01–N07, 27 facts) | done: `script/script.mjs`, `SCRIPT_TA.md` |
| Fact sheet | done: `FACT_SHEET.md` (labels F E S C O; 11 points under "To check before publishing") |
| Scratch narration, voice-02 | done 25 Nov: N01–N07 new, N08 (end card) from the EP21 zip; `align.py` 0 flagged; voice about 255 s, film about 5 min |
| Shot list | done: `shots/shots.txt` 70 rows, `SHOTLIST.md`, rules in `shots/CAST.md` |
| Film code for EP22 | adapted 25 Nov: fact counter in the pill, hook sounds, card pictures, pop-up on N02 line 2 (fact 3, about 60 s in), title plates (neurons, Earth, deep field) and words |
| Pictures | **70 of 70** (B01–B07 and R1 checked 25 Nov, on Drive) |
| Stills check | done 25 Nov (44 stills: title, cards, every stat and flash word, the pop-up). The fact counter `n/27` works. One fix: 053 mirrored so the stat card no longer covers the mountain. |
| Remake pass R1 | done 25 Nov: 033 (pyramid alone), 037 (one silhouette), 046 (India facing), 048 (Tamil Nadu village), 056 (forearm only), plus 053 mirrored. First versions in `google_drive/ep22_pics/old/` (on Drive inside the B zips). |
| Render | done 25 Nov: nine clips. N04 rendered twice (037 remade again: the figure stood under the stat card) and N07 twice (`cuts: [1, 2]` on fact 23 so the sand-grain hand stays for its sentence). |
| Parts, 720p | done 25 Nov: `finish.sh parts` and `VB=2300k finish.sh 720`. Film 305.8 s (5 min 6 s), −14.3 LUFS, peak −1.3 dBFS (gain +2.41 dB); 720p file 91,901,317 bytes. |
| Upload | parts 01, 02, 04, 05 on Drive; **parts 03, 06, 07 and the 720p film still to upload** (files in `google_drive/ep22_up/` and `out/deliver/`) |

Clip voice ends (s): N01 29.0, N02 31.8, N03 41.5, N04 31.0, N05 36.7, N06 30.8, N07 54.1.

Card pictures (CARD_BG): N02 `red_cells_stream`, N03 `supernova_shell_colours`, N04 `early_earth_molten`, N05 `earth_whole_blue`, N06 `sun_surface_flares_close`, N07 `deep_field_galaxies`.

## Drive

Folder `EP22_27_Unmaigal` `1nZ0iVV5rsZPfUCGlb3LfKpoaQwk-0e1P`; `images` `1OrKmsSgpf7Sz34oGMZFwGfJERpVd0tbN`.

| File | Drive id |
|---|---|
| EP22_SCRIPT_TA.md | 1UD_2qDBTM9Y8gz6qnK5vn6fksHrtRjLU |
| EP22_FACT_SHEET.md | 1AtEtYPxfEMLEj_oPuo1VpcgOJQN7g6Oy |
| EP22_SHOTLIST.md | 1bBjbUxBdEPeKb0lEiS4cbyCGPdzJUFDo |
| EP22_narration_scratch_voice02.zip (N01–N08) | 14fANm_fOsMIgdPF2GOmotoG9SIGMP5W9 |
| images/EP22_B01_images_001-010.zip | 1XclkvuetFn0LP1NwY38qTS7pyqLggriW |
| images/EP22_B02_images_011-020.zip | 1ofAuuQ4OcUNMRetTEuRFnQz_v1t7NLge |
| images/EP22_B03_images_021-030.zip | 1--E2DDRTHgJ3j5yXSmnywzHeJ7_x6wGM |
| images/EP22_B04_images_031-040.zip | 1TrwRrc8NrWRqxlShIEfuQ2h7J4LyD4Wz |
| images/EP22_B05_images_041-050.zip | 1B2kCLlLztxwM1kIw7eTh1uCQvvgRWreV |
| images/EP22_B06_images_051-060.zip | 1GUmTaB0iaP9d2yBx3_UEKhmxQvQDBi0G |
| images/EP22_B07_images_061-070.zip | 1eTwZSjUnTOoI3JC2nx4s_9MbDt8k_mn4 |
| images/EP22_R1_images_remakes.zip (033, 037, 046, 048, 053, 056: unpack after the B zips) | 1fQ4ih7WvOdPDqM4hug9nPbVgL2m9doU4 |
| EP22_SHOTLIST_final.md | 1Cugg1g4aG4Pvtq-1FrBMDUzZRvv6SNsD |
| EP22_FACT_SHEET_final.md | 1TMQYI4DAz_PMODVSpR_-xa9bzkKVRwi4 |
| images/EP22_R2_images_remakes.zip (037 second remake: unpack last) | 1kUfrtyaLkHAOR0gJQCbbHP260-0wjUDp |
| 1080p 01 hook + title (42.3 s) | 1NRQv8rbZkOyqjwCczizXz4GDaOaeRUWL |
| 1080p 02 ch1 (35.3 s) | 1WwARDLXlIGUbw6n7qYMIUO5bd4PowZtr |
| 1080p 03 ch2 (45.1 s) | **not uploaded yet** (upload limit reached 25 Nov) |
| 1080p 04 ch3 (34.5 s) | 19SFtECwIL0hYia29JV6P6gmNDjH3QjOE |
| 1080p 05 ch4 (40.1 s) | 1TdUZziqrmtoLsyogXvrciYJSpN8oZslw |
| 1080p 06 ch5 (34.3 s) | **not uploaded yet** |
| 1080p 07 ch6 + end card (74.5 s) | **not uploaded yet** |
| EP22_27Facts_full_720p.mp4 (305.8 s, 91,901,317 bytes) | **not uploaded yet** |

## After a full wipe

`git fetch -q origin arena/d486087a-hyperframes && git reset -q --hard FETCH_HEAD`; `bash tools/setup.sh` (through a background process, about 2.5 minutes; then check that `/tmp/hfenv.sh` exists. If pip stops on a hash mismatch, run `/tmp/nkvenv/bin/pip install --no-cache-dir imageio-ffmpeg pillow numpy` and run `setup.sh` again); download the narration zip and every picture zip listed above into `<repo>/google_drive/`; unzip the narration into `narration/`; `bash tools/restore.sh`; `node film/gen.mjs N01 N02 N03 N04 N05 N06 N07 && node film/title.mjs && node film/end.mjs`.

## Picture batches

Recipe per batch: `python3 tools/next.py 10` → ten `generate_image` calls to `google_drive/ep22_pics/raw/NNN.jpg` → `$PY tools/sheet.py a b` → `$PY tools/batch.py <batch> a b` → look at `google_drive/_sheet_E22Bnn.jpg` → upload the zip to `images` → commit.

| Batch | Pictures | Check |
|---|---|---|
| B01 | 001–010 (hook, first cells) | all usable; no writing, no faces. 005 (body outline) is a small figure on black: fine behind a caption, crop in if it looks empty in the stills check. |
| B02 | 011–020 (chapter 1 body; atoms, first light) | all usable; no writing, no faces. 015: the bulb lies on the table and is small in the frame (crop in if needed). 020 shows the first light as a burst, an artist's picture, not how the early universe looked. Looks **A** (organs and atoms) and **K** (space, no stars) added to `shots/expand.py` for 016, 018, 020. |
| B03 | 021–030 (chapter 2 rest; young Earth, the clock) | all usable; no writing, no faces. 030: the clock has tick marks only and reads just before twelve. 028: the crowd is seen from behind, in near silhouette. |
| B04 | 031–040 (chapter 3 time; chapter 4 opening) | no writing, no faces. **Remake 033** (two extra pyramids behind the new Great Pyramid: wrong for the date) and **037** (two figures instead of one). 039: the Moon sits in front of the Earth, close; kept. 036 moved from look S to O. |
| B05 | 041–050 (chapter 4 Earth; chapter 5 opening) | no writing, no faces. **Remake 046** (globe shows the Americas; it is also the N05 card and a title plate) and **048** (European-looking houses). Kept with a note: 043 the early shark is drawn like a modern shark, the sea floor is busy; 044 the first trees look partly like palms. |
| B06 | 051–060 (chapter 5 sky; chapter 6 opening) | no writing. **Remake 056** (the side of a face shows; he does not match the viewer). Kept with a note: 059 Andromeda is drawn far brighter and larger than the faint smudge the eye sees; 051 the Earth dot is larger than true scale. 055 moved to look K. |
| B07 | 061–070 (chapter 6 universe, close) | all usable; no faces. Kept with a note: 066 the path behind the Earth is a straight flare, so the Earth looks a little like a comet; 068 the ward wall has notice sheets with blurred marks (check in the stills); 069 the pale dot is very small. |

## Running time and fact 27

Clip lengths (s): N01 30.2, TITLE 12, N02 35.3, N03 45.0, N04 34.4, N05 40.1, N06 34.2, N07 57.5, END 17: **305.8 s (5 min 6 s)**. Fact 27 begins about 270 s in: 29.78 km/s x 270 = 8,040 km; 3.8 million cells/s x 270 = 1.03 billion; 4.2 births/s x 270 = 1,130. The spoken 8,000 km, 100 crore cells and 1,000 babies hold.
