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

Next: B06 = 051–060.
