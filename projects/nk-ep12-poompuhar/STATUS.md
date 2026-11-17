# EP12 Poompuhar: status

Working title: **பூம்புகார்: கடலுக்கு அடியில நிஜமா என்ன இருக்கு?** (topic bank S3, playlist கடல் விழுங்கிய கதைகள்).
Same pipeline as EP11 (`projects/nk-ep11-karikalan/STATUS.md` has the lessons and commands).

## 16 Nov · research, script, narration, shot list

- Script v1: `script/script.mjs` → `SCRIPT_TA.md`. Hook + nine chapters, 179 lines, 13,346 characters.
- Evidence tags: I இலக்கியம் · A அகழாய்வு · S கடல் ஆய்வு · O ஆய்வாளர் கருத்து · C நிரூபிக்கப்படாத கூற்று.
- Fact sheet: `FACT_SHEET.md`. Says for each claim whether my research notes back it; 24 rows are marked **check**. The three-sources bar is met for only a few rows.
- Scratch narration, voice-02: N01–N10 = 897.6 s (N01 75.4, N02 90.2, N03 80.7, N04 85.0, N05 87.7, N06 87.6, N07 93.9, N08 100.6, N09 99.2, N10 97.2). N11 is the channel end card (13.1 s), the same file as EP10 and EP11.
- Line timings: `narration/align.json` (0 lines flagged).
- Shot list: 322 pictures (`shots/shots.txt` → `shots/prompts.json`, `SHOTLIST.md`); about one picture per 2.8 s. Cast of four in `shots/CAST.md`.
- Expected film length: about 15 min 30 s (hook, 12 s title, nine chapters, 17 s end card).

## Where files live

- Narration mp3 files are ignored by git. Copies: `<repo>/google_drive/ep12_audio/N01–N11.mp3` and the Drive zip.
- Pictures: `<repo>/google_drive/ep12_pics/raw/NNN.jpg` and `cast/<key>.jpg` (not in git); `out/raw` and `out/cast` are links made by `tools/restore.sh`.

## Still to do

1. Cast portraits (4), then pictures 001–322 in batches of 10 per message → Drive `images` folder.
2. Film: update `film/title.mjs` plates, check hook sound effects and the subscribe pop-up timing in `film/gen.mjs`, check that the long tag "நிரூபிக்கப்படாத கூற்று" fits its box; render; `tools/finish.sh`.

## Open with the user

- Scratch voice, no music, no native read-through (same as EP11).
- The script names Graham Hancock and Prof. SM. Ramasamy and says their age claims are unproven. Sources are in the fact sheet, sections 6 and 7.
- Fact sheet items marked **check**.

## Drive (16 Nov)

Folder `EP12_Poompuhar` `1fC15q9VvjorFPg5i3gPGbTCjqrg6ncm9` inside NK Documentaries.

| File | Id |
|---|---|
| EP12_SCRIPT_TA_v1.md | `1jsropJwNIHDc3t4bkrdBpX_L63Hr_vAF` |
| EP12_FACT_SHEET.md (second upload; the first, `1Nwnmj…`, is in the Drive trash) | `1MeEAkjTXwSnrHpFaqmLC-1YTVZgXQIwJ` |
| EP12_SHOTLIST_322_images.md | `1g6tGvdVnIY2b4AO_8uZVfv8BP8Pxx1FA` |
| EP12_narration_scratch_voice02.zip | `1LQN3CixbqcThLrHdwTjcawZP4wt8zPpN` |
| images/ (folder) | `17TRLcMeP345nbeyuRKVzXeyzMS_C0JRL` |
| images/EP12_cast.zip | `1aJAQOjfe_NFzCUEzoRaaCaM8oXV4O8hM` |
| images/EP12_cast_sheet.jpg | `1wv8z84qc69WO-P_hfd4k2rnuv6wBfhPf` |

## Cast (16 Nov)

Four portraits made and looked at on one sheet: karikala, poet, king, peelivalai. All kept.
Note: karikala came out with a short beard as well as the moustache, and holding a sword; his face is small in the frame (full-length shot). Kept as the reference; redo if the face drifts in pictures 037–038.

## Next

Pictures 001–322, batches of 10 (`tools/next.py`, `tools/pack.py`). Nothing generated yet.

## Not checked

- The narration was generated and aligned (0 lines flagged) but nobody has listened to it; no loudness check yet.
- No pictures made apart from the four cast portraits.

## 16 Nov · pictures started

The image tool allows 10 pictures per turn, so one batch per "continue".

| Batch | Pictures | Drive zip | Sheet |
|---|---|---|---|
| B01 | 001–010 | `1teEj2jR9A5Z-lW4kMXbl7aE2v7L1O2fi` | `1yBgJc_o4EJbGOyFVL_bSAvT7j4JJ9cxI` |
| B02 | 011–020 | `10MfXidi9aX05YEEWfetCXIsCkKIbwWzy` | `1wLVofTvagFZMzYFJwF_tpKg8qyCP-_9I` |
| B03 | 021–030 | `1DKuUhRETbEWrmIczDLzVj9R02lkGqH5d` (v2 with redone 026, 028; old zip trashed) | `1-PzSN0hU9-BzymOsxzh4TNzyaFmj9_BC` |
| B04 | 031–040 | `1Y8gw05UTtuv2gGY-P8d9lH8KSP9C3iM2` | `1ES9wsABZWSCx0jlKG9VIp1De6c9jf_xY` |
| B05 | 041–050 | `1Q5_qqCB9_OGXGZItkS7VIhwNGYOpI3zl` (v2 with redone 050; old zip trashed) | `1AFlF88jRTdpZZXJNhNBOWmNzDqVKrf_Z` |
| B06 | 051–060 | `1TU3c0D2s7Nb8J4yZYxKWr_HzbV-gjHAk` | `1_MnoPYd3zORP7QWWKFfR_BEUzdmd_SPy` |
| B07 | 061–070 | `1kVHMHlyxF80rFoZ4UnoDFuyDiHCyRLjo` | `1w5BK0KqNBSAT2jk0d1fo3hj6_qChvu9r` |
| B08 | 071–080 | `19Q3tNy3OvYB_ieuKgzXtAqBEu5T7hk_D` | `16KZR8Y1aK2wnxgH0DRmKWIlKwuw34Q5m` |
| B09 | 081–090 | `1TglgZhTMxrQT8mAbRdYpm6x-DKn0eUJJ` | `1C4GSzQoRYGVYUMNoxanHwoOwKnTDGkhw` |
| B10 | 091–099 (nine; 100 failed) | `1Z4n74SyJNem50hEJOK67ePrRtO0tteUn` | `1oDQSSjHq4g1_V2TvBMziVWM1DBrOaEIx` |
| B11 | 100–109 | `1n9NjrZvKiD8fcq5yT2R4pWidIYigSyKj` | `1pVQ4li46fCtdi6I2arBxOAdIvD_W9znz` |
| B12 | 110–119 | `1QUOpB2EOr0DOoQ65jGXzY70gHXWl9Gpz` | `1imGtPIkP5FD5UkOpdyWoy0YqP8EEbQW9` |
| B13 | 120–129 | `14oujaSHPREOsEs3cmR10rK4y_5e5h149` | `1bbvwE_TUGJLnZhOJbpIvFHW7-pAqh-yV` |
| B14 | 130–139 | `176cef6Jd17Yn_M0COybWBNWz7GwbPw8M` | `1wQZVE9IVUi6q_HRGZgmvlquZTH923xr_` |
| B15 | 140–149 | `1r9Gj-GNotqsdYatewsw7MzCt-eULDj4-` | `1LDIZKebRf2Jp_wzRkr-tRnhVPH1VtzGH` |
| B16 | 150–159 | `16PeGh3TSeFAXvHCqucE9SRhS4gKdQC5y` | `1dgjC0eas4CMT2LWdgx_tWQMuuduegaKo` |
| B17 | 160–169 | `1031ch4Hb90hEyfgA21SIMO-yV575OSMa` | `1LMNUqUCvW1Go4KiyHW1wj26b2m_TlVy8` |
| B18 | 170–179 | `1DMi2ovtvA601iX_QxEwnD9pgdkqxmKdY` | `1yAGd-3yHKYhv7YLWYghFkLhIj0UVURbW` |
| B19 | 180–189 | `19SM43vo3sQsWu-jvZFOoqBvD9XTzl3tU` | `1EmVAM4z0YzSNHyUR4koaHF9GfksKbL71` |
| B20 | 190–199 | `1D5WWiPPGYrDBK6MEkDMkK-7SGzaaVUvv` | `1BB5zLZnmN5EZRQosmKFUG0gt-2V_KCOn` |
| B21 | 200–209 | `1kLp2w1q3e9Xibuhpvl90hM-BBsPKNMfW` | `1NfPMOIIMuSH_SfKp1aF0E0XlKtoENJdr` |
| B22 | 210–219 | `1T4dnP6-B9FNDrgLCOvG29qTPBgg7V3ee` | `1dA72nB2__MeeEemy5PHJlCpTh0nmuLJX` |
| B23 | 220–229 | `1Ym01E3tdUHnBzELH28jz0t57kKKkYS6B` | `1wgEvpN3gt9Em7sh7U33miB6ciBM7ONvh` |
| B24 | 230–239 | `17aGptkdBsIDbWW3sQlK2wX__X4uMLzp-` | `1pYHV12_tLrkXHvNuQsuZZhP3Bm3siD3k` |
| B25 | 240–249 | `1ow4JHPeYa0a1OLsS9uM9bsXz2xA0BOjc` | `1p_h6vKkedCBzrve37ATq9mzfl12nb0VK` |
| B26 | 250–259 | `1Z_KtqT-NfirPyUQ0iqkaYeKxV_291y61` | `1IFjqgR-6dIh3RDsIaWKA4ryDWfI-tm8_` |
| B27 | 260–269 | `1uGMV-Ocdj_ObMMpHnnLG3wFvgQmy8_-U` | `19R4CpUJVWj1sD3TiAsII1tINTQ_kjb8k` |
| B28 | 270–279 | `1xPLyDrzmqbXZrAOYHLqmThuEPfxd-Kz_` | `1V3EpM5KTP-fmkXG1-yBOMtkxXZV8t48t` |
| B29 | 280–289 | `1sVUW-5xR07E9hEuNChyZC8gpuEwbp752` | `1AdZ4dpns7k9WDGf6Et7dMZBPC_KDoVYY` |
| B30 | 290–299 | `1afe9BtKCbcA2hhUI7bAoOcG22jLWzQly` | `1YE3SZ70jHc-Vbd5rEKQxW2m6-IDd2mfk` |
| B31 | 300–308 | `1PNNhRdvwyjPdWrGUBqZ1VFtkwAu9D4B1` | `1KiCy5OjRZRfcQ4PkzmK8lbneOlMx7l2T` |
| B32 | 309–318 | `1KhQfqrrUM5uEBTz55zm3bWP6mSXMLH4-` | `1peIqGK_ifPAQn6PdvophYo8s9sJ8kmby` |
| B33 | 319–322 | `1MjX1GML-avH_xCzdJt1SPOdpTOgkSnu3` | `1RFSfr2sHQGKd67ik82dgyMy5izE_czWU` |
| R1 (redo zip) | 166, 168, 169, 173, 198, 207, 209, 223, 245, 262 | `138jVF2GUbeX54jXheIaG6oPUfw4PFgGE` | `13U5Vc4NuHm8hMAkWq7_mxvT3P9AdS_vK` |
| R2 (redo zip) | 159, 168, 188, 209, 213, 263, 272, 274, 280, 287 | `1RwfjSKCxwksOe9sF4-3c55gTS3JsB5Cz` | `12w0WU6qifkOUgZRn3RMqA6OPSYqkM_LI` |

B01 looked at on the contact sheet, and 004, 006, 007, 008 at half size: all ten kept. No writing visible at that size; not inspected at full size.

Also done: narration loudness measured on N01, N05, N10: −19.5 LUFS each, peaks about −1.5 dBTP (consistent; `finish.sh` raises the level to −14). Tag box in `film/gen.mjs` widened from 520 to 680 px for the longest tag; not rendered yet, so not seen.



## B02 (011–020)

All ten kept. Looked at on the sheet; 011 and 015 at half size.
- 011: the man's nose and moustache showed at the frame edge, and this picture stands for a living researcher's lab. The film copy is cropped to the screen and hand (`shots/crops.json`). The original in the Drive zip still shows him.
- 012, 014, 018, 019 came with black bars baked in; `sheet.py` trims them, so the film copies lose a little at the sides.
- 019: the poet matches the cast portrait.

## Workspace reset (found at the start of B02)

The workspace came back as a fresh clone at the base commit: the branch had to be fetched again, and the untracked `google_drive/` folder (narration, cast, pictures 001–010, all EP11 pictures) was gone. Recovery that worked:
1. `git fetch origin arena/d486087a-hyperframes && git merge --ff-only FETCH_HEAD`
2. Drive `download_file` on the zips (they land in `<repo>/google_drive/`): cast, each batch zip, the narration zip.
3. `bash tools/setup.sh`; unzip the narration into `google_drive/ep12_audio` and copy to `narration/`; `bash tools/restore.sh`.
So Drive is the only safe copy of pictures and audio: upload every batch before the turn ends. EP11 pictures were not restored (not needed; they are on Drive).

## B03 (021–030)

Eight kept, two to redo. Looked at on the sheet; 024, 026, 027, 028 at half size.
- **026 redo:** shows a whole two-handled amphora on a coral reef. The find was one fragment on a sandy bed.
- **028 redo:** the jars are ordinary necked pots, not torpedo jars.
- 027: a crewman's face showed at the right; the film copy is cropped to the fragment and gloved hands. Kept with a doubt: the fragment has a flared rim, and a real torpedo jar has a small plain mouth.
- The flawed 026 and 028 are in the B03 zip on Drive for now. New wording for both is in `shots/redo.txt`; they are remade in a redo pass and the zip replaced then.

## B04 (031–040)

All ten kept. Looked at on the sheet; 034, 035, 037, 038 at half size.
- 036, 037, 038: the poet and Karikala match their cast portraits (Karikala keeps the short beard).
- Kept with a doubt: 034 has two or three stave-built wooden barrels in the crowd, which do not belong in Sangam-age South India; they are small.
- 035: the palm leaves carry fine scratches that look like writing; nothing could be read at half size. Not checked at full size.

## B05 (041–050)

Nine kept, one to redo. Looked at on the sheet; 041, 043, 045–050 at half size.
- **050 redo:** the ship is a three-masted European galleon of about 1600. This is the Purananuru line about ships entering without lowering sail, so the ship is the subject. In `shots/redo.txt`.
- Kept with a doubt: 041, the ship at the left edge has European-looking rigging and a stern castle (the horses are the subject). 047, the bales sit on modern-looking slatted pallets. 048, the Mediterranean merchant looks medieval rather than Roman.
- To stop more galleons, the port, dusk and storybook settings in `shots/expand.py` now say ships are single-masted with one square sail. `prompts.json` and `SHOTLIST.md` were regenerated, so the recorded prompts for the port pictures already made (before 051) carry that sentence although it was not in the prompt actually used.

Redo list so far: 026, 028, 050.

## B06 (051–060)

All ten kept. Looked at on the sheet; 051, 055, 056, 057 at half size.
- The ship wording worked: every ship in this batch is single-masted.
- Kept with a doubt: 051 shows a spoked ship's wheel on deck (a much later invention). 055, the geographer is seen from behind but part of his bearded profile shows.
- 056: the map's marks could not be read at half size; not checked at full size.

Redo list so far: 026, 028, 050. Chapter 01 (N02) pictures are complete with this batch.

## B07 (061–070)

All ten kept. Looked at on the sheet; 064, 066, 067, 068 at half size.
- 066–068: the king and Peelivalai match their cast portraits; the tale pictures come out in a flatter storybook style, clearly different from the port pictures, as intended.
- Kept with a doubt: 065, the palace is a large domed stone fort on a cliff, more like a much later North Indian fort than anything on the Tamil coast (it is a storybook picture for the tale).
- Five pictures needed bars trimmed (062, 063, 064, 069, 070).

## Second workspace reset (found at the start of B07)

This time the files were all there (including `google_drive/`), but git was back at the base commit with `projects/` showing as untracked, and `/tmp` was empty. Fix that worked:
1. `git fetch origin arena/d486087a-hyperframes && git reset -q FETCH_HEAD` (working tree untouched; status then clean).
2. `bash tools/setup.sh`; `cp ../../google_drive/ep12_audio/N*.mp3 narration/`; `bash tools/restore.sh`.
`tools/pair.py` (half-size view of up to four film copies: `python tools/pair.py 066 067` → `/tmp/pair.jpg`) is now in the repo.

Redo list so far: 026, 028, 050.

## B08 (071–080)

All ten kept. Looked at on the sheet; 072, 073, 077, 080 at half size.
- 072, 073: the king matches his cast portrait.
- 077 (the mythic wave with the goddess shape) came with a rounded dark frame; the film copy is cropped 3% in from each edge (`shots/crops.json`).
- Kept with a doubt: 079, the flooded city shows a tall many-storeyed temple gateway of a kind built about a thousand years after the Sangam age. The city in 077 and 079 is stone and flat-roofed, unlike the brick-and-thatch port in the daylight pictures. Both are storybook pictures for the tale.
- Also kept with a doubt (added a turn late): 072 has a domed palace building at the right edge (a later style); 078 still shows lit lamps and fairly calm water, though the shot asked for lamps going out; 080 the ascetic, meant as Manimekalai seen from behind, has a shaved head and reads as a monk.

## B09 (081–090)

All ten kept. Looked at on the sheet and all ten at half size; the manuscripts in 083, 084 and the desk in 087 at full size.
- 081–088 close N03 (the "no date" beats, the sea drawn back, the grandmother's story); 089, 090 open N04, the 1960s dig.
- 087 had a faded wall map of India at the left edge; the film copy is cropped to x 0.20–1.00, y 0.10–0.90 (`shots/crops.json`), which removes it.
- 083, 084: the palm leaves carry rows of script-like marks; not readable at full size.
- Kept with a doubt: 085 has torches and lamps in what is meant to be grey daylight (the setting text adds "moonlight and lamp glow"); 087 shows a small broken pot, not a single sherd, and scribbled note pages; 088 the square is already dug, not just marked; 089, 090 show labourers' faces (small, invented, no real person); 090 the supervisor wears a pith helmet.
- 088–090 came out in a flatter, more illustrated style than the photographic 082 and 087.

## B10 (091–099; 100 not made)

Nine made and kept. The call for 100 failed ("Image generation failed") and the failed call used up the tenth slot of the turn, so 100 moves to the next batch. From here the batches run 100–109, 110–119, … ; pack them with the batch number as a third argument (`tools/pack.py 100 109 11`).
Looked at all nine at half size.
- 091–096, 098: the 1960s dig (trenches, silted channel, brick wall, wharf platform with channel and blackened posts, wood sample). 097: the wharf in use in ancient times. 099: 1960s dating lab.
- Film-copy crops added in `shots/crops.json`: 092, 098, 099 had a rounded dark frame (3–3.5% inset); 094 showed a labourer's face large in the frame, so it is cropped to x 0.30–0.97, y 0.33–1.00 (hands, brush and brick wall; 915 px wide source, slightly soft).
- Kept with a doubt: 097 has a square battlemented stone tower in the background and two-storey tiled houses that look colonial; 091 shows the archaeologist's face in part profile under the hat; 092 shows labourers' faces (invented); 093 has two 1960s jeeps and is in the flatter illustrated style; 099 shows radio valves and dial meters, a loose stand-in for a radiocarbon lab.

## B11 (100–109)

All ten made and kept (100 worked on the second try). Looked at all ten at half size.
- 100: posts driven in ancient times; 101–103, 107: the 1960s dig (curved reservoir wall, monastery cells, footprint slab, archaeologist at dusk); 104 square copper coins; 105 brick on manuscript; 106 crop marks from the air; 108, 109 the monastery in use.
- Film-copy crops added in `shots/crops.json`: 100 had a black bar along the top; 108 had a thin dark frame all round.
- Kept with a doubt: 109 the footprint slab carries carved swastikas next to the wheels and lotuses (they do occur on ancient Buddha-footprint slabs, but some viewers may read them wrongly; the slab is also far more ornate than the plain one in 103); 108 the monastery has a carved stone temple tower of a later, Hindu-temple style and the monks carry bowls in a row like a Southeast Asian alms round; 101 the reservoir wall is tall and deep, the real one is only a few courses; 106 the crop marks are very neat rectangles (the script only says remains lie under the fields); 100 is in the flatter illustrated style; 107 pith helmet again.

## B12 (110–119)

The workspace was reset again before this batch (third time; the "files kept, git and /tmp lost" kind). Fixed with the same recipe; nothing lost. Note: `restore.sh` rebuilds sheets on the 001–010 grid (`sheet_091_100`, `sheet_101_110`), which is harmless.
New helper: `tools/edges.py A B` flags film copies with a black bar or dark rounded frame.

All ten made and kept. Looked at all ten at half size.
- 110, 111: the boy saint singing and the shore temple; 112, 113: soil layers and sorted sherds; 114, 117: the later town; 115, 116: the sea eating the town's edge; 118: diver going in; 119 opens N05 (survey boat).
- Film-copy crops added in `shots/crops.json`: 113 showed part of a present-day man's face at the right edge; 117 had black bars top and bottom.
- Kept with a doubt: 114 has a tall, heavily carved temple gateway of a later style than the period meant, and is in the flatter illustrated style; 110 the small shrine is very ornate for the 7th century; 117 the ruined walls in the distance look like a European castle ruin; 119 has hills behind the coast (this coast is flat delta) and film scratches at the right edge; 118 the diver is shown already in the water beside the boat.

## B13 (120–129)

Prompt change before this batch: the two "survey at sea" settings in `shots/expand.py` (1990 and present day) now say "the shore a flat low line of palms with no hills or mountains" (119 had hills). `prompts.json` and `SHOTLIST.md` regenerated; 37 rows changed, so the recorded prompts for 006, 025, 027, 118, 119 carry a sentence that was not in the prompt actually used.

All ten made and kept. Looked at all ten at half size; the chart in 122 and the ship in 120 at full size (no readable writing; 120 flies a small Indian flag).
- 120–123: the survey ship, the institute in Goa, the team with a chart, the senior archaeologist; 124: divers at the Gujarat site; 125–127, 129: brickwork and ring wells in the surf; 128: a well in use in ancient times.
- The coast is flat in 120, 122, 123: the new wording works.
- Film-copy crop added in `shots/crops.json`: 124 had a dark rounded frame. 120 came letterboxed (1376×581 after trimming), so its film copy is enlarged more than usual.
- Kept with a doubt: 127 and 128 show wells built of bricks, not the stacked terracotta rings meant (126 and 129 are right); 128 also has a wooden pulley frame and is in the flatter illustrated style; 123 the senior archaeologist is seen from behind but a grey-bearded cheek shows beside the binoculars (the line is about a real, named man); 121 the institute looks old and run-down; 124 is in a comic-book style.

## B14 (130–139)

All ten made and kept. Looked at all ten at half size.
- 130: wall and jar rim on the foreshore; 131–135: the shallow dives (divers, river mouth with a dive-flag buoy, dressed blocks, the half-round block with a notch, a sherd lifted from the sand); 136, 137: sherds sorted on deck and under a magnifier; 138: a potter in ancient times; 139: the chart recorder.
- Film-copy crops added in `shots/crops.json`: 136 and 137 had a dark rounded frame.
- Kept with a doubt: 131, 134, 135 show corals and reef growth on the seabed (the real bed here is sand and mud); 133 one block seems to carry a faint carved panel; 135 the "sherd" is a large piece of a pot; 137 the sherd has scratched lines that could be taken for marks (not readable); 131 is in an inked comic style and 138 in the flatter illustrated style.

## B15 (140–149)

Prompt change before this batch: the underwater setting in `shots/expand.py` now says "a bare seabed of sand and silt with only thin weed, no coral reef" (131, 134, 135 had corals). `prompts.json` and `SHOTLIST.md` regenerated; 59 rows changed, so the recorded prompts for 002–005, 013, 021, 024, 026, 131, 133–135 carry a sentence that was not in the prompt actually used. Watch the U-shape pictures: their subject text says "heavily overgrown", the setting now says "thin weed".

All ten made and kept. Looked at all ten at half size; the dial in 148 at full size (marks, not readable numbers).
- 140: the sonar trace with the buried valley; 141: the ancient river from above; 142–145: the wreck and the lead ingots; 146: the 1790s merchant ship; 147: anchor beside old blocks; 148, 149: depth gauge and sounding line.
- No coral in 142, 143, 147, 149: the new wording works (148 still has some blurred growth).
- Film-copy crops added in `shots/crops.json`: 140, 143, 144, 146 had black bars or a dark rounded frame; 145 showed a crewman's face large in the frame, so it is cropped to x 0.22–0.86, y 0.36–1.00 (hands, brush, ingot in the tray; slightly soft).
- Kept with a doubt: 142 the wreck is a nearly whole hull skeleton (the real one is scattered remains); 146 has a low hill behind the palms (its prompt has no "no hills" sentence); 147 the "blocks" are rounded boulders; 141 shows a large town and many ships, in the flatter illustrated style.

## B16 (150–159)

All ten made and kept. Looked at all ten at half size; the logbook and wall maps in 153 at full size.
- 150, 151: heading further out, deeper water (end of N05); 152–159 open N06: the vessel towing a cable, the logbook, the towfish, the sonar printout with three blotches, the distant coast, the sounding line, three divers descending, the first sight of the curved ridge.
- Film-copy crops added in `shots/crops.json`: 156 and 157 had a black bar or dark rounded frame.
- 153: the logbook pages are scribble, not readable; two small blurred wall maps at the top right (one vaguely like the subcontinent) were left in.
- Kept with a doubt: **159** the curved ridge reads as a rough stone wall about as tall as the diver and only some 20 m across (rule: low overgrown ridge, never clear walls; the reported height is 1–2 m, the length 85 m) — compare with the later U-shape pictures before the film is cut; 151 the "faint curved shape" looks like a small object, not a large ridge, and is in an inked style; 150 and 152 show a rusty trawler-like ship, 120 showed a white research vessel; 157 the sailor's face shows in part profile.

## B17 (160–169)

Prompt changes before and after this batch (all in the repo, `prompts.json` and `SHOTLIST.md` regenerated):
- `shots/expand.py`: U-shape pictures from 160 on (underwater rows whose subject says "ridge", except `level_rows_hint` and `natural_beachrock`) get the sentence "The ridge is a low rounded bank about as high as a man, thickly coated in marine growth, with no cut blocks and no built masonry." (159 looked like a built wall.)
- `shots/shots.txt`: rows 174, 211, 265 no longer say "horseshoe"; the sketches are described as a survey plan of a U-shaped bank, "not a horse's shoe" (168, 169 came out as iron horseshoes).

Ten made; seven kept, three for redo. Looked at all ten at half size; the sketches in 168, 169 at full size.
- Good: 160 (two divers with a tape), 161 (whole U-shape from above with a tiny diver), 162 (diver and scale pole beside it), 163 (compass), 164 (two unequal arms), 165 (marine growth close up), 167 (hand fanning silt). The ridge is a low, rounded, overgrown bank in all of them: the new sentence works.
- **Redo 166**: the "level rows" are three clean flat steps like a staircase. **Redo 168, 169**: the sketches are drawings of an iron horse's shoe with nail holes. New wording for all three is in `shots/redo.txt`.
- Film-copy crops added in `shots/crops.json`: 163, 166, 168 had a black bar or dark rounded frame.
- Kept with a doubt: 161 the U-shape looks about 25 m across against the diver, the script says 85 m; 163 has colourful growth close to coral.

## B18 (170–179)

Ten made; nine kept, one for redo. Looked at all ten at half size; the papers in 172, 173 at full size.
- Good: 170 (slack tape), 171 (diver in murk), 172 (typed report, blurred and unreadable), 174 (the ridge alone, a low overgrown bank), 175 (three pebbles), 176 (natural beach rock in block-like pieces), 177 (mason setting a block), 178 (hourglass on wet stone), 179 (curved shore wall at dusk).
- **Redo 173**: the plan sketch is now right (a U-shaped band, not a horseshoe) but it carries readable invented English labels ("Seafloor Bank A", "Bank B", "Shelf Edge", "Bank C (unmapped)", "depth"). New wording in `shots/redo.txt`; row 210 (clipboard sketch) now also says "no labels, no words, no letters, no numbers".
- Film-copy crops added in `shots/crops.json`: 177 (dark rounded corners); 179 came with dark bands top and bottom that the trim missed, cropped to x 0.17–0.925, y 0.125–0.88.
- Kept with a doubt: 170 the tape is a modern yellow pocket tape measure; 179 lamps stand on the wall; 175 and 178 have a kerosene lantern / later-style carved arches in the dark room behind.

## B19 (180–189)

All ten made and kept. Looked at all ten at half size; the laptop screen and map in 187 at full size (greeked text, an invented island; nothing readable).
- 180–184 close N06: the sagging delta-mud cutaway, sherd and charcoal in a dish, the empty sample bag, the ridge fading into dark, plain books and video cassettes. 185–189 open N07 (the 2001 visit): the writer on the beach from behind, the film crew loading, the writer's desk, the fantasy drowning city, the mixed dive team with a film camera.
- Film-copy crop added in `shots/crops.json`: 187 showed the writer's face in profile at the right edge (the line is about a living, named man), cropped to x 0–0.84, y 0.16–1.00 (desk, laptop, hands).
- Kept with a doubt: 188 the "imagined city" is a European Gothic fantasy city with spires and castles (it is meant as a book-cover fantasy, but it is far from anything Indian); 186 has hills behind the harbour, shows two crew faces in part profile and looks like dusk, not morning; 180 is drawn as a painted block with a dark empty corner at the bottom right; 189 one diver's beard shows under the mask.

## B20 (190–199)

Ten made; nine kept, one for redo. Looked at all ten at half size; 191 shelves and 197 figures at full size (shelf labels are scribbles, nothing readable; no face shows in 197).
- Good: 190 (film lights on the low ridge), 191 (geologist's office, man from behind), 192 (monitor: southern India with a pale band of extra land, no labels), 193 (ice sheet calving), 194 (sea creeping over a plain, drowned trees), 195 (dry plain with a low rock ridge, sea far off), 196 (the same ridge drowned), 197 (writer in a wetsuit filmed on deck, both from behind), 199 (pot with three holes).
- **Redo 198**: the "fantasy builders" came out as fur-clad people raising tall standing stones under snowy cliffs. Wrong for a warm South Indian shore and unlike the low ridge. New wording in `shots/redo.txt` (cloth wraps, palms, a low U-shaped bank, no snow, no furs, no standing stones). The prompt used said "a large U-shaped curved row of rough stones" in place of "a horseshoe of rough stones"; `shots/shots.txt` now says the same.
- Film-copy crop added in `shots/crops.json`: 191 (3% inset; pale frame line at top and left).
- Kept with a doubt: 191 the map on the monitor is a green coast that looks like eastern England, not India (192 right after shows India); 194 has low hills on the horizon; 195 the ridge is a rocky hill, larger than "low"; 193 mountains behind the ice.

## B21 (200–209)

Ten made; eight kept, two for redo. Looked at all ten at half size; the gauge in 204, the camp in 207 and the heads in 209 at full size.
- `shots/expand.py` Ice Age setting reworded before this batch: "a warm wide dry coastal plain of scrub and scattered trees … no snow, no ice … wearing only simple hide loincloths, no furs" (the old "cold pale sky … animal skins" gave snow and furs in 198). Rows 010, 194, 195, 206, 207, 208, 234, 242, 243, 245 changed in `prompts.json`; 010, 194, 195 were made with the old wording.
- Good: 200 (torch on the overgrown lump), 201 (delta from the air), 202 (mud bank slumping, roots bare), 203 (palms fallen in the surf), 204 (depth gauge and blank slate; dial blurred, not readable), 205 (rod and stopped watch, blank dial), 206 (microliths in a palm), 208 (rock shelter with ash).
- **Redo 207**: the camp came out as a flat textbook illustration, with bare-chested women in the foreground, large polished spearheads and a hafted hammer. New wording: small dim figures at dusk, hide wraps, no metal.
- **Redo 209**: the Indian scientist's face is in clear profile and the European man's bearded cheek shows; they stand for real living people. New wording: three backs at the rail, no faces.
- Film-copy crop added in `shots/crops.json`: 208 (3.5% inset; white rounded frame).
- Kept with a doubt: 206 and 208 look like African savanna (flat-topped acacias); 206 has hills behind.

## B22 (210–219)

All ten made and kept. Looked at all ten at half size; the sketch in 210, the camera in 211 and the head in 213 at full size.
- 210–218 close N07 (the 2001 visit): the archaeologist's sketch (a thick U-shaped band, no labels: the "only the drawing" wording works), the interview camera, men hauling a block, the writer looking into the water, the empty sample bag, the empty dish, the level balance, the ridge alone, the closed book and mask. 219 opens N08 (the wake fading at dusk).
- **211 raw picture edited**: the camera carried a readable "SONY" and an "SX" badge. Both were painted over in `google_drive/ep12_pics/raw/211.jpg` (two small patches at raw x 1002–1029, y 216–228 and x 1036–1063, y 239–266); the zip on Drive holds the edited picture. The untouched original is not kept.
- Film-copy crop added in `shots/crops.json`: 212 (x 0–0.74, y 0.20–0.94) to cut out a temple tower in the background.
- Prompts used differ slightly from `prompts.json`: 213 added "his face not visible"; 219 said "fading dusk light" in place of "soft morning light".
- Kept with a doubt: 213 the writer's bearded jaw shows in shadowed profile, and the boat is a small canoe on a backwater, not a sea boat; 210 the archaeologist is a woman (the script does not say); 211 big ships on the horizon; 212 hills behind.

## B23 (220–229)

Ten made; nine kept, one for redo. Looked at all ten at half size; the screens in 222 and 228, the notebooks in 229 and the head in 223 at full size (screen menus and handwriting are scribbles, nothing readable).
- Good: 220 (university building among rain trees, students from behind), 221 (press room from the back, speakers too small to recognise), 222 (lab with four seabed-map monitors), 224 (survey ship in cutaway with a fan of sound beams), 225 (relief map on a monitor), 226 (open sea, no land), 227 (deep, almost black seabed), 228 (straight-edged shapes on a seabed map, a finger tracing), 229 (pen outlining a long rectangle on a printed map).
- **Redo 223**: the professor's face shows in clear profile; he stands for a real living person. New wording: seen from directly behind, no part of the face.
- Film-copy crop added in `shots/crops.json`: 224 (3% inset; rounded film frame).
- Prompt used for 226 dropped the "shore a flat low line of palms" sentence (the subject says no land in sight).
- Kept with a doubt: 225 the relief map has round craters and looks like a planet's surface more than a seabed; 220 is in a flatter illustrated style; 229 has an old lantern on a modern lab desk; 224 the seabed under the ship is rocky canyon, not flat shelf.

## B24 (230–239)

All ten made and kept. Looked at all ten at half size; corners of 234 and the cropped 232 at full size.
- 230–232 the imagined harbour, docks and lighthouse as pencil sketches (no labels on any of them; rows 230, 231, 232, 235 in `shots/shots.txt` now carry the "only the drawing … no labels, no words, no letters, no numbers" wording that was used), 233 a round bump on the map, 234 the Ice Age shoreline with tiny figures (warm, no snow), 235 a rising pencil line on graph paper (no numbers), 236 a monitor with India's outline and a dashed second shoreline, 237 the ridge from one side, 238 empty sample tubes, 239 dive gear unused on a jetty.
- Film-copy crops added in `shots/crops.json`: 232 (3.5% inset; rounded film frame), 234 (2.5% inset; dark rounded top corners).
- Kept with a doubt: 230 the imagined harbour is drawn as a European-looking port town with towers and bridges (it is meant as "only a sketch"); 236 the dashed line runs only along the east coast; 238 the tubes look frosted, not clearly empty; 234 flat-topped acacias again.

## B25 (240–249)

Ten made; nine kept, one for redo. Looked at all ten at half size; the newspapers in 240 and 241, the spear in 242, the canoe in 245 and the corners of 248 at full size (newsprint and masthead are blurred, nothing readable).
- Good: 240 (three archaeologists from behind over sherds, one with a newspaper), 241 (folded newspaper, spectacles, trowel), 242 (hunter in grass, spear tipped with small stone barbs, deer far off), 243 (tiny blades beside ash), 244 (dream image of an empty stone harbour in mist), 246 (natural seabed ridges and channels from above), 247 (bare hand on rough stone, torch), 248 (crew lowering a coring tube), 249 (villagers from behind at sunset).
- **Redo 245**: a modern leather handbag sits in the middle of the dugout canoe. New wording: only a fibre net and a wooden spear in the canoe, no bags.
- Film-copy crops added in `shots/crops.json`: 243 (3.5% inset; rounded film frame), 246 (3% inset; dark frame).
- Prompts used differ slightly from `prompts.json`: 240 said "seen from directly behind, no faces visible"; 249 said "warm sunset light" in place of "soft morning light".
- Kept with a doubt: 240 the left man's face shows in shadowed part profile, and the newspaper is held open, not folded; 244 the dream harbour looks like a medieval European stone dock with chains; 243 is in a flatter illustrated style; 247 the hand wears a ring; 245 also has hills behind the lagoon.

## B26 (250–259)

All ten made and kept. Looked at all ten at half size; the crews in 253, 256, 259 and the cropped 250 at full size.
- 250–253 close N08: the ring well on the beach (stacked one-piece rings: the "not of bricks" wording works), the brick wharf with its posts, the dive boat, divers stepping off. 254–259 open N09 (the new dives): the red bound document, today's shore with a breakwater, the team over a chart, cadets carrying cases, ten divers on deck, the yellow robot lowered.
- Film-copy crop added in `shots/crops.json`: 250 (x 0.31–1.00, y 0.22–0.91) because the child's face showed in profile; the film copy keeps the well and the child's arm on the rim.
- Prompts used differ slightly from `prompts.json`: 250 added "made of stacked one-piece fired-clay rings and not of bricks"; 256, 257, 258 added "no faces visible".
- Kept with a doubt: 253 three boat crew face the camera at small size, and the divers seem to step onto the water; 256 heads are bent over the chart with faces in shadow; 259 one crewman's bearded cheek shows in shadow; 251 has a wheelbarrow and baskets left in the trench.

## B27 (260–269)

Ten made; nine kept, one for redo. Looked at all ten at half size; the blocks in 262 and the cropped 261, 264, 266 at full size.
- Good: 260 (yellow robot over the seabed), 261 (old chart with pencil crosses and a GPS unit; no labels), 263 (oval mound with a diver), 264 (laptop sonar with a U-shaped blotch and an oval blotch, a hand pointing; no labels), 265 (dive boat under monsoon clouds, flag buoy), 266 (coast with a temple tower from the boat), 267 (divers with a white grid frame), 268 (one broken jar piece in the sand, a gloved hand), 269 (a whole torpedo jar: tall, straight-sided, no neck, no handles; the wording works).
- **Redo 262**: the "blocks found again" carry stepped carved mouldings like temple architecture. The script (N09 q4) only says the spots marked thirty years ago were found again. New wording: plain rough worn blocks, no carving.
- Film-copy crops added in `shots/crops.json`: 261 (x 0.16–1, y 0.16–1; a man's nose and moustache showed at the top left), 264 (x 0.30–0.90, y 0.40–1.00; the operator's whole face showed; the film copy keeps the arm, hand and laptop), 266 (3% inset; black bar at the top).
- Prompts used differ from `prompts.json`: 261 (blank GPS screen, chart with no words or numbers), 264 (screen with no labels, numbers or menus), 268 (one piece, not a whole jar), 269 (straight-sided, no neck, not an amphora; the "men in long plain tunics" part left out).
- Kept with a doubt: 263 the oval mound looks like a low ring wall of stacked stones (like 159); 265 has film scratches and a flatter painted look; 268 the piece is large, close to half a pot.

## B28 (270–279)

Ten made; eight kept, two for redo. Looked at all ten at half size; 270, 277 and the cropped 273 at full size.
- Good: 270 (torpedo jars in rows in a ship's hold, a sailor at a rope seal), 271 (Gulf ship in a strong wind, one mast), 273 (gloved hands with a caliper on the jar piece), 275 (porters carrying jars down a gangplank, an officer watching), 276 (the piece under a magnifier lamp), 277 (broken edge close up), 278 (one ring-well rim with a diver and scale rod), 279 (four ring rims in a line; both are one-piece rings, the wording works).
- **Redo 272**: the find lies on the cloth as a whole necked pot. The script (N09 q8) says one broken piece of a jar.
- **Redo 274**: flat illustrated style with modern details (jars on wooden shipping pallets, a modern checked head cloth with a cord, a shoulder bag), and the jars are wide-mouthed storage pots.
- Film-copy crop added in `shots/crops.json`: 273 (x 0–0.77, y 0.23–1.00; a man's bearded face showed at the top right).
- Prompts used differ from `prompts.json`: jars described as "tall straight-sided torpedo-shaped … with no necks and no handles" (270, 271, 274, 275); 271 "a single mast"; 272, 273, 276 "one … broken jar fragment"; 272 "no faces visible"; 278, 279 "a single one-piece fired-clay ring and not made of bricks".
- Kept with a doubt: 271 and 275 are in a flatter illustrated style and their jars have short necks (vases, not torpedo jars); 270 has a few necked, lidded jars in the corner; 273 the piece is large, close to the top half of a pot; 277 faint painted marks on the sherd surface; 275 the officer wears an orange robe and turban.

## B29 (280–289)

Ten made; nine kept, one for redo. Looked at all ten at half size; 285, 288 and the cropped 287 at full size (marks on the manuscript and brick in 288 are scribbles, nothing readable).
- Good: 281 (laptop with a buried channel, a hand tracing it; no face, no labels), 282 (sherds in rows on long tables, hands only), 283 (limestone block with a square socket beside a blue-green glazed sherd), 284 (a sherd on a coloured seabed map; no labels), 285 (three finds in a row), 286 (gloved hands taking a scraping into a tube), 287 (potter's hands on the wheel), 288 (manuscript, brick and mask on three cloths from above), 289 (the port in golden light from a watchtower, flat coast). 284–287 close N09; 288–289 open N10.
- **Redo 280**: the wells along the river came out built of bricks, in a flat illustrated style, although the prompt said one-piece rings and not bricks. New wording describes each lining as a smooth seamless clay tube.
- Film-copy crop added in `shots/crops.json`: 287 (x 0.22–0.87, y 0.33–0.98): the picture came as a whole potter with black bars top and bottom; the film copy is the close view of hands and pot the shot asked for.
- Prompts used differ from `prompts.json`: 280 (ring wording), 281 and 282 and 286 (hands only, no face), 284 (map without words), 285 (three small finds named one by one), 289 ("seen from a high watchtower above a flat river-mouth coast with no hills" in place of "from a low hill").
- Kept with a doubt: 287 is in a heavy painted, comic-like style; 285 the "black-and-red" sherd has a painted geometric pattern and the well-ring piece looks like a pot rim; 283 a flask stands on the table.
- The port setting has drifted into a flat illustrated style in 274, 275, 280, 287 (289 is fine). For the remaining port rows consider starting the prompt with "Photorealistic".

## B30 (290–299)

Ten made; all ten kept. Looked at all ten at half size, and 290, 291, 292, 294, 298 again after cropping.
- Good: 290 (the wave with a faint goddess over the sleeping town, mural style), 291 (red-cloth bundle beside a guttering lamp), 292 (the excavated brick wharf at dawn with post stumps), 293 (low brick cells of the monastery, a visitor from behind), 294 (street with a granite temple gateway, the sea close behind), 295 (one-piece ring-well rim with fish inside), 296 (bricks showing through the sand), 297 (sunbeams on low brick walls and a broken pot), 298 (diver hovering over the overgrown ridge), 299 (ridge surface in torch light).
- Film-copy crops added in `shots/crops.json`: 290 and 292 (both came with a rounded film frame; trimmed 3–4 % all round), 294 (black bars top and bottom).
- Prompts used differ from `prompts.json`: 292 ("soft early dawn light", a long low platform of large flat bricks with post stumps), 293 (rows of small cells only knee high; visitor "seen from directly behind"), 294 ("Photorealistic", ox carts, flat coast), 295 (one-piece ring wording), 297 ("only a few courses high"), 298 ("low overgrown curved ridge" in place of "horseshoe ridge").
- Kept with a doubt: 291 a steel tumbler stands at the right edge; 293 the monastery is a very large regular grid of cells; 294 the gateway is richly carved; 297 the wall is close to a metre high and the pot has handles like an amphora; 298 the growth on the ridge includes fan shapes like coral.

## B31 (300–308; 309 not made)

Nine made, all nine kept. **309 was not made**: its generation call failed and the limit of ten image calls per turn was already used, so 309 moves to B32. Looked at all nine at half size; 301 after cropping and details of 303, 304, 308 at full size.
- Good: 300 (an empty steel tray in a shaft of light), 301 (sketches pushed to the edge, a real sherd in the lamp light), 302 (the tide sliding up a flat beach at dusk), 303 (researchers at a tripod coring rig on the beach, faces turned away), 304 (split sediment core, dark mud against pale sand, a gloved hand at the boundary), 305 (tiny spiral shells through a microscope), 306 (a white wave line on the horizon beyond a low shore town, seen from inland), 307 (a dry abandoned river bed curving through rice fields, the living river beyond), 308 (close view of the mud and shell-sand boundary).
- Film-copy crop added in `shots/crops.json`: 301 (x 0.18–1.00, y 0.08–0.90: the sketch sheets filled the left third; now they sit at the edge and the sherd is near the centre).
- Prompts used differ from `prompts.json`: 301 ("ancient harbour wall and a tall beacon tower", sheets carry only drawings), 302 ("fading dusk light" in place of the morning-light setting), 303 ("seen from directly behind, no part of any face visible", no logos), 304 (hand only, no rulers), 305 (no scale bar), 306 ("Photorealistic", low brick and thatch houses, flat fields), 307 (pale sand bed through rice fields, flat delta), 309 prepared with "hands only … plain stone shore temple standing on dry sand well above the waterline, plain white border".
- Kept with a doubt: 300 the tray is a canteen meal tray with compartments, and a bicycle stands in the dark behind; 301 the sketch shows a European-style lighthouse and fort, and the sherd is half a small pot; 303 a faint low headland on the horizon; 304 the boundary runs across the core but the pale part is coarse gravelly sand.

## B32 (309–318)

Ten made; all ten kept. Looked at all ten at half size; 312 after cropping and details of 313 and 317 at full size.
- Good: 309 (old hands holding a faded photograph of a small shore temple on dry sand), 310 (the same kind of small temple standing in the surf), 311 (grey-haired archaeologist from behind watching a temple half in the water), 312 (a wave dragging old bricks down the beach), 313 (a plain coast chart with one small corner shaded, a hand on it), 314 (wide empty sea with one small buoy), 315 (tanks, ropes and cases ready on a jetty at dawn), 316 (a gloved hand reaching toward something reddish in a gap in the ridge), 317 (a sherd in a diver's open palm in torch light), 318 (notebook with a long and a short column of tally strokes).
- Film-copy crop added in `shots/crops.json`: 312 (rounded film-frame corners; trimmed 2.5 % all round).
- Prompts used differ from `prompts.json`: 309 (hands only, plain stone temple, white border without writing), 310 and 311 ("small plain stone" temple, flat shore; 311 "seen from directly behind"), 313 (plain hand-drawn coast outline, no labels, hand only), 315 (unmarked gear, wooden boat), 316 (hand only, "low overgrown ridge"), 317 ("one broken piece and not a whole pot"), 318 (tally strokes only, no words or numbers).
- Kept with a doubt: 317 the glove is thick and caked with silt and the fingers point at the camera, so the hand reads as lumpy at first glance; 309–311 the temple looks like a small carved granite shrine in the Pallava style; 316 the growth on the ridge has some coral-like shapes.

## B33 (319–322 and redos 026, 028, 050, 166, 168, 169)

Ten made; all ten kept. **All 322 pictures now exist.** Looked at all ten at half size; details of 166, 169, 320 at full size.
- New, good: 319 (bare hands brushing an old brick), 320 (the port at sunset from high above, lamps, single-masted ships, flat coast), 321 (the U-shaped bank from directly above with a diver's torch at its centre), 322 (calm sea at dusk with one small boat).
- Redone, good: 026 (diver kneeling on bare sand lifting one large curved pale shard; no amphora, no reef), 028 (rows of tall straight-sided torpedo jars leaning in racks, potter from behind), 050 (single-masted ship with a matting sail and steering oars entering the river mouth), 166 (a rough line of stones in the growth with a gloved hand; no steps), 168 (two notebooks, one long narrow U-band plan and one short wide one; no labels), 169 (diver drawing a U-band plan on a slate; no labels).
- The old versions are kept in `google_drive/ep12_pics/raw_old/` (untracked). The old film-copy crops for 166 and 168 were removed from `shots/crops.json`. Rows done are marked "# DONE in B33" in `shots/redo.txt`.
- Prompts used: redo subject + the row's setting and style tail; added "Photorealistic" (028, 050, 320), "seen from directly behind" (028), the ridge sentence (166), "carry only the drawings: no labels, no words, no letters, no numbers" (168, 169); 321 "low overgrown U-shaped bank … seen from directly above" in place of "horseshoe ridge"; 322 "fading dusk light"; 319 hands only.
- Kept with a doubt: 319 the brick is a rough slab; 321 the bank is a neat small U, about 15 m across by the diver's size (the real one is 85 m long); 166 a few of the stones are roughly squared; 169 the diver has no hood.
- Drive: B33 zip and sheet uploaded. B03 and B05 zips and sheets replaced (old ones moved to trash). B17 zip and sheet were rebuilt locally but not uploaded (Drive upload rate limit), and were then lost in the workspace reset before R1 (see below).

## Fourth workspace reset (found at the start of R1) and the new way of storing redone pictures

The workspace came back as a fresh clone at the base commit again: `google_drive/` (all 322 raw pictures, cast, narration, `raw_old`), `out/` and `/tmp` were gone. Fixed so far: `git fetch origin arena/d486087a-hyperframes && git merge --ff-only FETCH_HEAD`; `bash tools/setup.sh`; `out/raw` and `out/cast` links made by hand. **Lost for good: the redone 166, 168, 169 from B33** (their rebuilt B17 zip had not reached Drive); they were made again in R1. Everything else is on Drive.

**Restored later in the same turn:** Drive `download_file` on all 33 batch zips, `EP12_cast.zip` and the narration zip (35 calls, all went through; they land in `<repo>/google_drive/`); the R1 redo zip copied from `out/up/` into `google_drive/`; narration unzipped into `google_drive/ep12_audio` and copied to `narration/`; `bash tools/restore.sh` → "pictures: 322, cast: 4", 322 film copies in `out/img`, crops applied. Checked: the R1 pictures on disk are the redone ones; 026, 028, 050 are the redone ones (B03 and B05 v2). Not restored: `raw_old/` (old versions; not needed) and `out/up/` files of earlier batches (they are on Drive).

If it happens again: the same recipe, plus `download_file` on every redo zip (R1 `138jVF2GUbeX54jXheIaG6oPUfw4PFgGE`, later ones in the table).

New rule: redone pictures no longer go into rebuilt batch zips. They go to Drive as **redo zips** `EP12_Rn_images_redo_*.zip` (same file names as in the batch zips) in the same turn they are made. `tools/restore.sh` now unpacks the redo zips after the batch zips, so the redone pictures win. The batch zips B17, B18, B20, B21, B23, B25, B27, B28, B29 on Drive stay as they are (old versions inside). At the end one zip of all 322 final pictures is uploaded, as for EP11. `tools/crops.py` now skips pictures that are not on disk.

## R1 (redos 166, 168, 169, 173, 198, 207, 209, 223, 245, 262)

Ten made. Looked at all ten at half size; details of 209 and 223 at full size. Eight are good; two are better than before but go round once more.
- Good: 166 (a rough line of stones in the growth, gloved hand; no steps), 169 (diver drawing a small U-band plan on a slate), 173 (hand with a pencil above a U-band plan; no labels), 198 (dreamlike figures piling stones into a low bank on a misty palm shore; no snow, no furs, no standing stones), 207 (small figures round a fire by a rock shelter, hide shelters), 223 (grey-haired professor from directly behind pointing at a seabed map screen; no labels), 245 (two men paddling a dugout with a net and a wooden spear; no bag), 262 (diver over plain overgrown blocks; no mouldings).
- **Again 168**: one notebook shows a short wide U, but the other shows a closed oval ring, not a U.
- **Again 209**: the three men stand at the rail with their backs to the camera, but the two Indian men still show cheek and jaw in rear profile, and a cliffed headland stands on the horizon.
- Film-copy crop added: 207 (black bars top and bottom; 3 % all round).
- Kept with a doubt: 207 and 245 have an African-savanna look (flat-topped thorn trees; 207 has low hills far off); 245 the spear has a broad point; 262 the blocks are quite regular rectangles; 169 the plan is small in the frame.
- Drive: `EP12_R1_images_redo_166-262.zip` and `EP12_R1_sheet.jpg` uploaded (ids in the table).

## R2 (redos 168, 209, 272, 274, 280 and doubtful 159, 263, 188, 213, 287)

Ten made; all ten taken. **The redo list is empty: all 322 pictures are final unless the user asks for changes.** Looked at all ten at half size; 213 against its old version and 272 at full size. Old versions are in `google_drive/ep12_pics/raw_old/` (untracked).
- 168: two notebooks, a long narrow U and a short wide U, both open at one end, no labels.
- 209: three men at the rail from directly behind (two in sun hats, one in a wetsuit hood), open sea to a flat horizon, no land.
- 272: one curved pale shard on a padded cloth, the crew round it from the shoulders down. Film-copy crop (x 0.04–0.96, y 0.08–0.96) removes two chins at the top edge and a thin dark line at the bottom.
- 274: photoreal wharf; the trader in a plain turban and tunic bargains with a Tamil merchant beside pale jars leaning on a timber rail; no pallets, no bag.
- 280: three wells with smooth one-piece clay rims on the river bank, a man and a woman drawing water.
- 159: a low overgrown bank curving round, a small diver with a torch; no wall face.
- 263: a low rounded overgrown mound with a diver; no ring of stones.
- 188: the imagined drowned city is now stepped stone terraces among palms under a red sky (no Gothic spires).
- 213: the writer from behind at the stern, open sea at sunset (the old one was a small figure on a backwater with houseboats).
- 287: photoreal close view of clay-covered hands shaping a pot rim on the wheel; the old crop was removed.
- Kept with a doubt: 274 the jars still have short flared necks (they read as tall vases); 213 the man's ear, cheek and stubble show from behind (no eye, nose or mouth); 188 the terraces look Mesoamerican; 272 a small pale mark is stitched on the cloth; 280 the rims are wide and low like big basins.
- Drive: `EP12_R2_images_redo_159-287.zip` and `EP12_R2_sheet.jpg` uploaded (ids in the table). Restore order: batch zips, then R1, then R2 (168 and 209 are in both; R2 wins).

## Edge pass (done with R2)

`tools/edges.py 1 322` flagged twenty film copies, most from the early batches made before the check existed. Seventeen had a thin dark line at the top or bottom or rounded film-frame corners: 009, 016, 021, 024, 037, 038, 039, 041, 043, 045, 048, 051, 064, 071, 080, 084, 105. Each got a 3.5 % inset crop in `shots/crops.json`; all seventeen were looked at afterwards and are clean. Still flagged and left alone because the dark edge is part of the picture: 064 (dark desk edge), 168 (dark room corners), 230, 236, 248.

Next (no more pictures to make):
1. `film/title.mjs` `const P` still has EP11 picture numbers; `film/end.mjs` uses N11; links `shared/plates`, `shared/vo` are missing; check the subscribe pop-up and hook sounds in `film/gen.mjs`.
2. Listen to the narration; decide the open script edits (see FACT_SHEET.md and the list in this file); a text change means a new clip and new timings.
3. Render the film parts, `tools/finish.sh`, upload the film and one zip of all 322 final pictures.
