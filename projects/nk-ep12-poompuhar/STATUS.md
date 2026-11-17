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
| B03 | 021–030 | `1uhbeJKvbOKlxG9-y9kVTzlQ-g1xhdZRY` | `1sj-z6cJK3aGIlbUVe9Ev6u2vcqfEqibz` |
| B04 | 031–040 | `1Y8gw05UTtuv2gGY-P8d9lH8KSP9C3iM2` | `1ES9wsABZWSCx0jlKG9VIp1De6c9jf_xY` |
| B05 | 041–050 | `13_4gL2hzyi7-Mh48PYiW3js4ubHUvLuO` | `1NJCUIcPllvC60RSK_mw250fVhhtUSekN` |
| B06 | 051–060 | `1TU3c0D2s7Nb8J4yZYxKWr_HzbV-gjHAk` | `1_MnoPYd3zORP7QWWKFfR_BEUzdmd_SPy` |
| B07 | 061–070 | `1kVHMHlyxF80rFoZ4UnoDFuyDiHCyRLjo` | `1w5BK0KqNBSAT2jk0d1fo3hj6_qChvu9r` |
| B08 | 071–080 | `19Q3tNy3OvYB_ieuKgzXtAqBEu5T7hk_D` | `16KZR8Y1aK2wnxgH0DRmKWIlKwuw34Q5m` |
| B09 | 081–090 | `1TglgZhTMxrQT8mAbRdYpm6x-DKn0eUJJ` | `1C4GSzQoRYGVYUMNoxanHwoOwKnTDGkhw` |
| B10 | 091–099 (nine; 100 failed) | `1Z4n74SyJNem50hEJOK67ePrRtO0tteUn` | `1oDQSSjHq4g1_V2TvBMziVWM1DBrOaEIx` |
| B11 | 100–109 | `1n9NjrZvKiD8fcq5yT2R4pWidIYigSyKj` | `1pVQ4li46fCtdi6I2arBxOAdIvD_W9znz` |
| B12 | 110–119 | `1QUOpB2EOr0DOoQ65jGXzY70gHXWl9Gpz` | `1imGtPIkP5FD5UkOpdyWoy0YqP8EEbQW9` |
| B13 | 120–129 | `14oujaSHPREOsEs3cmR10rK4y_5e5h149` | `1bbvwE_TUGJLnZhOJbpIvFHW7-pAqh-yV` |
| B14 | 130–139 | `176cef6Jd17Yn_M0COybWBNWz7GwbPw8M` | `1wQZVE9IVUi6q_HRGZgmvlquZTH923xr_` |

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

Redo list so far: 026, 028, 050.

Next: B15 = 140–149 (`tools/pack.py 140 149 15`).
