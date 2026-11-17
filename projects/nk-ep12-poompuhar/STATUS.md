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

Redo list so far: 026, 028, 050, 166, 168, 169, 173, 198, 207, 209, 223, 245 (twelve). Plan: B26 = 250–259 … B32 = 310–319; B33 = 320–322 plus seven redos; B34 = the other redos plus doubtful pictures worth a second try (first choices: 159, 188, 151, 213).

Next: B26 = 250–259 (`tools/pack.py 250 259 26`).
