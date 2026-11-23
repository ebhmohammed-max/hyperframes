# EP20 status: 80 டன் கல்லு 200 அடி உயரத்துக்கு எப்படி போச்சு? (Thanjavur Big Temple, topic bank Y3)

Started 23 Nov 2026. Copied from `projects/nk-ep19-2050/` (same film code, tools and delivery pattern; read that project's STATUS.md for the full recipe).

## Where it stands

| Step | State |
|---|---|
| Research, script v1 (68 lines, N01–N07) | done: `script/script.mjs`, `SCRIPT_TA.md` |
| Fact sheet | done: `FACT_SHEET.md` (labels K A M N F O; our sums in section 4; "To check before publishing") |
| Scratch narration, voice-02 | done: N01–N07 made 23 Nov, N08 (end card) taken from the EP19 zip; `align.py` 0 flagged; voice 457.63 s, film about 503 s (8 min 23 s) |
| Shot list | done: `shots/shots.txt` 128 rows, `SHOTLIST.md` |
| Pictures | **100 of 128** (B01–B10 = 001–100: checked, on Drive) |
| Film code for EP20 | **not adapted yet**: `film/gen.mjs` (HOOK_FX, CARD_BG, subscribe pop-up line `q === 3`), `film/title.mjs` (three plates and the title words), `film/fx.mjs` if a new graphic is wanted |
| Stills checks, render, parts, 720p, upload | not started |

Clip voice lengths (s): N01 48.61, N02 65.83, N03 58.52, N04 67.03, N05 80.25, N06 55.11, N07 82.27.

## Drive

Folder `EP20_Thanjavur_80_Ton_Kallu` `1auV8wSZPKDqQpw9ulBB065f1AVV-sVxK`; `images` `1klK3N1A4Q4Olsn2CyhzMhyzek-_rkNym`.

| File | Drive id |
|---|---|
| EP20_SCRIPT_TA.md | 1OQ3KZOTpUR3qhi7x327Lc5kV8wVzjRcc |
| EP20_FACT_SHEET.md | 1Fo1VmVy5tB6hVJGZ9Ijh623jCTOvz9La |
| EP20_SHOTLIST.md | 1c2czpwFB5RpgDRQF9dvnyKeDrbjD2QWt |
| EP20_narration_scratch_voice02.zip (N01–N08) | 1RFVOpgVaqCGdvDkAEZtsKbPepHwtQdzw |

| Batch | Pictures | Drive id (images) |
|---|---|---|
| B01 | 001–010 | 1x0_eGLd37dil1u2DII1bx6QbT4koqP1z |
| B02 | 011–020 | 1LjUFRy9Z55BY9-dCfZin9mXg-pAJxeiq |
| B03 | 021–030 | 1SzRjRHmbtUXPO6HSZEYeeZpjHXq2e15s |
| B04 | 031–040 | 1dGpEhxGuV5xwGrp9nppivJKMmcyeBRAt |
| B05 | 041–050 | 1EtOejTuKuay728sqzKUbqujRWYFzpWYr |
| B06 | 051–060 | 1w45TnpqGz9sYzLj5BKZ4qpjcbdcmSm4t |
| B07 | 061–070 | 1QHpoFd_Rkzad4HnSblTl93Gu3giNG4hk |
| B08 | 071–080 | 14uAXZ6PzD-_n5otb8Ora-Fs7dBqpEwn8 |
| B09 | 081–090 | 18LYDtG-g6RLXJf8wMElm8kmWyfgRFvE5 |
| B10 | 091–100 | 1pEzWTfLFMGOA1kGdJ_suk_I_ZatuqgEA |

## Picture batches

Each turn: `$PY tools/next.py 10` (prompts) → ten `generate_image` calls into `google_drive/ep20_pics/raw/NNN.jpg` → `$PY tools/sheet.py a b; $PY tools/crops.py; $PY tools/batch.py <B> a b [two big numbers]` → view `google_drive/_sheet_E20B<nn>.jpg` (a new name each time) → upload the zip from `google_drive/ep20_up/` into `images`.

Plates the film code will need by name: title `chola_site_dawn_wide`, `ramp_elephants_legend`, `capstone_dome_close`; hook words `ramp_elephants_legend`, `palm_leaf_sums_lamp`, `inscription_base_close`, `capstone_dome_close`; chapter cards N02 `sarapallam_village_fields`, N03 `ramp_profile_long`, N04 `inscription_base_close`, N05 `dome_seams_top_view`, N06 `half_tower_short_ramps`, N07 `granite_mass_corner_wide`.

## For the redo pass

- 007 `ramp_elephants_legend`: the tower already wears its dome while the stone is still on the ramp. Make again with a flat, unfinished top (it is also a title plate).
- 012 `scholar_scaffold_top`: a second tall tower stands beside the dome. Make again: the dome is the top of the only tower, nothing higher than it in the frame.
- 033 `sand_table_ramp_hands`: the model on the table is a stepped pyramid of the Maya kind, not a South Indian tower. Make again: a small carved model of a South Indian temple tower (like the model in 010), the sand ramp long and thin.
- 034 `ramp_profile_long`: the ramp is short and steep, against the line it illustrates ("walk 100 feet, rise one foot") and it is the N03 chapter card. Make again: the tower very small at the far right, the ramp a long low line across the whole frame, barely rising.
- 061 `finial_set_on_dome`: a scene of 1010, but a present-day town with painted concrete houses lies below. Make again: only paddy fields, palms and thatched roofs below.
- 067 `scaffold_ladders_up`: came out as three panels side by side (a collage). Make again: one single continuous picture.
- 081 `tower_shadow_courtyard`: the shadow is a thin black stripe like a carpet, not the shadow of a tower, and the line it illustrates is "the shadow does fall". Make again: seen from above, the broad pointed shadow of the pyramid tower lying across the paving, the tower itself at the edge of the frame.
- 087 `visitor_steps_lookup`: two towers stand side by side. Make again: one tower only.
- 020 `tiers_carved_detail` (kept for now): a small domed shrine sits in the middle of the tiers; acceptable as detail, remake only if a spare call is left.

- Note for prompts: in legend pictures where the stone is still travelling, write that the tower top is flat and has no dome yet (done by hand for 024; the look text otherwise adds the dome).
- Note for prompts: for scenes of 1010 that are not building work (gifts, dancers, accountants) the look-C text was shortened by hand (no scaffolding, rollers or elephants), so that they do not creep into the picture.
- 062 `stonecutter_letters_hands` (kept): the carved marks look like Tamil letter shapes but form no words; they stand out in relief instead of being cut in.
- 071 `dome_segment_levers`: the raw picture has rounded black corners; `shots/crops.json` cuts 1.5 % off each edge for the film copy (the zip on Drive holds the raw picture).
- 075 `dome_plaster_stucco` (kept): one small weathered stucco figure sits in a niche at the lower left.
- 086 `folk_mural_peeling` was made with 031 as the reference picture, so the two murals match.
- 098 `spiral_ramp_tower`: rounded black corners in the raw picture, trimmed by `shots/crops.json` like 071. (All of 001–100 were tested for dark corners: only 071 and 098.)
- 092 `vimana_inside_hollow` (kept): reads as a stone passage with steps rather than a view straight up; 093 shows the stepped courses from below. If a spare call is left, remake 092 as a view straight up a square shaft.
- 025 `log_rollers_close` (kept): the stone is a squared block, not rounded.

## Open points

- Script is v1 and unheard: the hook line 7 ("கதை. கணக்கு. கல்வெட்டு. கல்லு.") is only 1.9 s for four flash words; check on stills.
- The film says the cap is in several pieces (Branfoot; The Hindu 2010) and that the number of pieces is not settled. The 80 t / 25 t and 216 ft / 196 ft pairs are explained in the fact sheet.
- The ramp sums are ours (school arithmetic, assumptions in the fact sheet).

## After a full wipe

`git fetch -q origin arena/d486087a-hyperframes && git reset -q --hard FETCH_HEAD`; `bash projects/nk-ep20-capstone/tools/setup.sh` through `start_process` (about 2.5 minutes, gives `/tmp/hfenv.sh`); download the narration zip and every picture zip from Drive into `google_drive/`, unzip the narration into `narration/`, then `bash tools/restore.sh`.
