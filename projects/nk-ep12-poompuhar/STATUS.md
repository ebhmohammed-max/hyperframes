# EP12 Poompuhar: status

Working title: **பூம்புகார்: கடலுக்கு அடியில நிஜமா என்ன இருக்கு?** (topic bank S3, playlist கடல் விழுங்கிய கதைகள்).
Same pipeline as EP11 (`projects/nk-ep11-karikalan/STATUS.md` has the lessons and commands).

## 16 Nov · research, script, narration, shot list

- Script v1: `script/script.mjs` → `SCRIPT_TA.md`. Hook + nine chapters, 179 lines, 13,346 characters.
- Evidence tags: I இலக்கியம் · A அகழாய்வு · S கடல் ஆய்வு · O ஆய்வாளர் கருத்து · C நிரூபிக்கப்படாத கூற்று.
- Fact sheet: `FACT_SHEET.md` (every claim, its sources, and the items marked **check**).
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
