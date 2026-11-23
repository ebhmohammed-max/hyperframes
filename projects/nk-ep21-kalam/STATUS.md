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
| Pictures | **100 of 100, all remakes done** (B01–B10 and R1 checked, on Drive). First versions of the ten remade pictures are in `google_drive/ep21_pics/old/` (on Drive only inside the B zips). |
| Film code for EP21 | adapted 23 Nov: hook sounds, card pictures, pop-up on N02 line 2, title plates (island, rocket, hill town) and words; clip folders made with `node film/gen.mjs N01 … N07 && node film/title.mjs && node film/end.mjs` |
| Stills checks | done 23 Nov (38 stills: title, cards, every stat, big number and flash word, the pop-up); one fix, see below |
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
| B02 | 011–020 | 1Zsnr8PKH2H6R48k4KxSg_OAtBd-Ln4v9 |
| B03 | 021–030 | 1F27gb1oyikUKC1ZBrrO4my2t0CQaS6og |
| B04 | 031–040 | 1fUJ1V9vfM_8DwMbtRsKDUw-xApxSqJv1 |
| B05 | 041–050 | 1pjcIpAfFw3MHzQbU5NE_q49n9RWra5vT |
| B06 | 051–060 | 1oYR30EvI7k7636LUHg68i7-ubHfyp-dN |
| B07 | 061–070 | 1cjjFpZPgXFpySUNahoCSDuQrwyhsTr7B |
| B08 | 071–080 | 13lcVok5Rz07Ogrx1i22HlRtJTxAL1HSL |
| B09 | 081–090 | 1FGoM0FRQYYhJ_DG9NP1DG2u-HOOGzIWG |
| B10 | 091–100 | 17IRuOxMNx12abRugIOVX2fmyXxa8wHai |
| R1 | remakes 002, 004, 017, 033, 043, 071, 080, 090, 095, 097 (unpack after the B zips; `restore.sh` does this) | 1nhEfpbBn1wZvKdhggbeDrpjCGPr23-jR |

## Picture batches

Each turn: `python3 tools/next.py 10` → ten `generate_image` calls to `google_drive/ep21_pics/raw/NNN.jpg` → `$PY tools/sheet.py a b` → `$PY tools/batch.py <batch> a b [two numbers to show large]` → view `google_drive/_sheet_E21Bnn.jpg` → upload the zip from `google_drive/ep21_up/` to `images` → this file → commit, push.

## For the redo pass

| Picture | Fault | Change for the remake |
|---|---|---|
| 004 `old_man_at_podium_back` | the hall is full of schoolchildren in uniform; the lecture was to management students in their twenties | say "adult postgraduate students in their twenties in everyday clothes, no children, no uniforms" |
| 017 `aide_beside_seat` | the aide's face shows in side view; the rule is no face of a real person | "both men seen strictly from behind, only the backs of their heads above the seats" |
| 033 `ashram_monk_far` | the monk sits with his back to the young man; a 1970s-style radio stands in a room of 1958 | "the monk faces the young man, both seen from the side and behind, from far; no radio, no machine of any kind" |
| 043 `rocket_liftoff_flame` | men and a jeep stand a few steps from the rocket as it lifts off | "no people and no vehicles anywhere near the pad; seen from far across the sand" |
| 071 `hall_doors_students_rise` | he walks with a stick towards doors that open on the road, so he seems to leave | "seen from the corridor through the open doors into the hall; he walks in, no walking stick; rows of adult students standing inside" |
| 080 `podium_empty_light` | the stage stands in the open air with hills behind; it must be the indoor hall (this picture is also used in the hook) | "indoors, the same lecture hall, walls and ceiling lights, no sky, no landscape" |
| 090 `one_pair_shoes` | heavy laced boots, which read as the guard's army boots; the list says a pair of shoes | "one pair of plain black leather office shoes, low, not boots" |
| 002 `hall_clock_evening` | the clock reads about six o'clock, the line says 6:35 (small in the frame) | make again once; keep if it fails again |

Kept with a small fault: 027 (the boy's face shows a little from the side, small in the frame); 048 (the doorway opens on a workshop, not clearly a press room); 056 (the jeep has a closed cab, the guard stands at its back; 055 shows the open jeep as described); 057 and 060 (he sits in the front seat; the account does not say which seat); 068 and 069 (the palace is a generic sandstone palace, not Rashtrapati Bhavan as it is); 077 (the hands that clip the microphone look old, the aide was about thirty); 089 (the three suits have open lapels, not closed collars); 092 (the aide's face shows a little from the side, small).

**Redo pass R1 done (23 Nov), sheet `_sheet_E21R1`, all ten kept:** 002 (the clock now reads close to 6:35), 004 (adult students), 017 (both men strictly from behind), 033 (monk and young man face each other across a bare hall, no radio), 043 (rocket alone, seen across sand), 071 (seen from the corridor, no stick, adult students standing), 080 (indoors, empty podium, pages on the floor), 090 (low office shoes), 095 (a long low pier bridge), 097 (the trail is high in the sky; the picture carries white dust specks like an old print).
`shots/crops.json` held three EP20 entries (071, 098, 112); emptied on 23 Nov, 071 and 098 film copies made again from the raw pictures.

## Open points

- The shot list on Drive is the first version; five flight pictures have since moved to look P (no hills in the cabin windows). Upload the final `SHOTLIST.md` at delivery.
- The script and the scratch voice have not been heard by a person.
- No face of Dr Kalam is shown (generated illustrations only; rule in `shots/CAST.md`).
- Items 1–5 of "To check before publishing" in `FACT_SHEET.md` (the two books were not opened; the possessions list is a press list).

## Stills checks (23 Nov)

Sheets `_sheet_E21S1`–`S4` and `E21T1`. All graphics correct: title words, six chapter cards with their pictures, hook flash words (the two struck words and the one that stands), the pop-up on N02 line 2, the stats, the big 9, the five struck words of N07.
One fix: in the N07 stat the large slot held "2,500 புத்தகம்" and its lower strokes ran into the line beneath; the large slot now holds only "2,500" (confirmed on `E21T1`).
The remade pictures were not in the stills (they were checked on their own sheet). After the remakes run `node film/gen.mjs N01 … N07` again only if a shot name changes (it does not); the plates are read by number.

## After a full wipe

`git fetch -q origin arena/d486087a-hyperframes && git reset -q --hard FETCH_HEAD`; `bash tools/setup.sh` (through a background process, about 2.5 minutes); download the narration zip and every picture zip listed above into `<repo>/google_drive/`; unzip the narration into `narration/`; `bash tools/restore.sh`.
