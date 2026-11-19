# EP15 Genghis Khan: status

Topic in the user's words: "Genghis Khan: The Man Who Conquered the World", about 10 minutes. Same pipeline as EP14 (`../nk-ep14-bhangarh/STATUS.md`; the full recipe and lessons are in `../nk-ep12-poompuhar/STATUS.md`).

## Done on 19 Nov 2026

- Research by web search (extracts only, no full pages); see `FACT_SHEET.md`, doubts marked **check**.
- `script/script.mjs` v1: hook + 6 chapters, 89 lines, 8,625 characters. `node script/build.mjs` → `SCRIPT_TA.md`, `script/lines.json`, `narration/text/`.
- Scratch narration `voice-02`: `narration/N01.mp3` … `N07.mp3` = 564.0 s. `N08.mp3` is the channel end card audio (13.1 s, same file as EP14).
- `script/align.py` → `narration/align.json`; no line flagged.
- Shot list: `shots/shots.txt` (178 rows), `shots/counts.json` (under 4.2 s one picture, under 8.6 s two, else three), `python3 shots/expand.py` → `shots/prompts.json`, `SHOTLIST.md`.
- Reference pictures (khan, temujin, temujin_boy, borte, hoelun, jamukha) made and looked at on one sheet; `shots/CAST.md`. The first `temujin_boy` looked like a girl and was made again with a shaved crown and forelock.
- `film/title.mjs` adapted (title செங்கிஸ் கான், subtitle உலகத்தை ஜெயிச்ச மனிதன்?, plates 014, 017, 007: look at them once those pictures exist). `film/gen.mjs` adapted (`HOOK_FX` for the 12 hook lines; subscribe pop-up on line 3 of N02).
- Expected film length: 564 s narration + 12 s title + 17 s end card + chapter cards ≈ 10 min 14 s.

## Chapters

| Clip | Chapter | Lines | Seconds | Pictures |
|---|---|---|---|---|
| N01 | hook | 12 | 64.4 | 22 (001–022) |
| N02 | 01 டெமுஜின் | 13 | 90.7 | 27 (023–049) |
| N03 | 02 நண்பனே எதிரி | 13 | 77.2 | 26 (050–075) |
| N04 | 03 புது படை, புது சட்டம் | 12 | 71.7 | 21 (076–096) |
| N05 | 04 ஒரு வணிகக் கூட்டம் | 13 | 71.2 | 24 (097–120) |
| N06 | 05 அழிவோட கணக்கு | 12 | 90.9 | 26 (121–146) |
| N07 | 06 மறைஞ்ச கல்லறை | 14 | 98.0 | 32 (147–178) |

## Picture rules for this episode

- No blood, no bodies, nobody shown being hurt. The massacres are told in words; the pictures show riders, dust, far smoke, empty streets.
- Genghis Khan's face is invented (no portrait was made in his lifetime) and the film says so in the last chapter. The 1278 portrait is never copied.
- Other real people from behind or far away; clergy from behind.
- No readable writing; maps only as props without lettering.

## Open points

- The script has had no native Tamil read-through; the title and the name spellings are drafts. The subtitle carries a question mark because the film answers "no, not the world".
- **check** items in `FACT_SHEET.md`, mainly: that Temüjin punished Jamukha's betrayers first (N03 line 11, from memory only), the three Yassa rules (N04 line 9), "he could not read", Nishapur's year, Behter as the *elder* brother and Qasar's part, "for centuries nobody could enter" Burkhan Khaldun.
- Pictures can be made only 10 per turn.

## Drive

- Folder `EP15_GenghisKhan`: `1Qc4pD53sKGZp0KeLsWsCND_HzCd-bNYO`; subfolder `images`: `1b92JrqauMAodX2OslcHZo9uWjgAg69UV`

| File | Id |
|---|---|
| `EP15_narration_scratch_voice02.zip` (N01–N08) | `1PRIHZrmmoM3zDFF2mI-El7QrWsTTBWu4` |
| `EP15_SCRIPT_TA_v1.md` | `130yXA6nK0oljQSYMVljmPs-QXSNPauVX` |
| `EP15_FACT_SHEET.md` | `1VKY7snINfLh2GS-IbnsXaSBnqbrUmVML` |
| `EP15_SHOTLIST.md` | `1J54sVl7352b3Wkk1Nxiy1RNjpgnDzvue` |
| `images/EP15_cast.zip` | `1ZdNerNVq_6LGZfChZkgrF_4QiKIVntj9` |

## Batches

| Batch | Pictures | Zip id | Sheet id | Notes |
|---|---|---|---|---|
| B01 | 001–012 | `1yqwpHF9MSrOxiuyPZ2miXKHv1LS039x4` | `1qhf97XCt5byK7XO52gQ23Ufqt-FGWusI` | 011 and 012 came with a thin black bar on top: cropped in `shots/crops.json`. An earlier zip of 001–002 only (`1APuH6LVIAT_DFe_luSsl7XZT3Dlyg4jb`) is still in the folder and can be deleted |
| B02 | 013–022 | `1YtYtVs9E_zxTqsTKbn_ilPCPrXAufUYz` | `1QLm2rgrsFA6mqJ4O_G2e2D8UCwfwIsyS` | hook complete. 016: the pen lines are invented marks, not a real script |
| B03 | 023–032 | `1WXdNmjK6oLrCm6GYhyJFUsmreWbrmzN8` | `16NfkOoMLaeBzNI0bMMOQptv2ocfrFddk` | 029 to redo (glass kerosene lamp and bookshelves; listed in `shots/redo.txt`). 026 and 031 sit in a library of a later age, kept as symbolic. Still-life wording in `shots/expand.py` tightened after this |
| B04 | 033–042 | `1bI9bd1jHFtTMNckX5Qw5gQ9ZeL-VDN4y` | `1ja9vz4jfBLjZYXXCnROUSt-tIq3sZ--_` | all kept. The Behter scene is told with a quarrel (041) and a bow left in the grass (042); no violence shown |
| B05 | 043–052 without 044 | `1YNd2XXj8bUpPsw3fS8KWArxLZBwmecDS` | `1vLRU-N-6J5hulWYcL6V6DIMhy-pT_Lzp` | 044 failed once; made in the next turn from behind with the board as a yoke on the shoulders (`EP15_B05_images_044-044.zip`, `1kJgYIR-hDu301UPftcSlddFXNVihdRje`). 045: the head in the river has a full head of hair, not the shaved crown (seen from behind at night, kept). 050: the wedding guests wear present-day festival dress, kept for now, a candidate for the redo pass |
| B06 | 053–061 | `1IbeT4ezV2bPfxQtY0xDvuTA_J5SyWKGk` | `1447gWsY6R4mB9gLU8zIw40RVT_Sypli-` | to redo: 054 (glass lamps), 058 and 059 (came out as drawn illustrations). The rest kept |
| B07 | 062–071 without 067 | `1DtxItqohvZP2aBulVd4PU4XenbdwHOu7` | `1dJd9_3Hz_eY9tCwK2IY_BlPk8b_H9ZEA` | 067 was blocked by content moderation (chiefs kneeling before a rider); rewritten in `shots/shots.txt` as bows laid on the grass and made in the next turn (`EP15_B07_images_067-067.zip`, `1B0FDj66WVerhoBNomUpTzJhxm9NDC1xr`). 069 to redo (ages wrong). 071 cropped to remove a lantern at the left edge |
| B08 | 072–080 | `13-UT3FpV4edIbfzRYIGI4Cu7uceXImRm` (078 on its own: `1YzFJ0BHPkTer2pOTnrs0vUGR7cg3FKXV`, `EP15_B08_images_078-078.zip`) | `1cJFTvfRqbpwqnsKZMo5T93POuoh1y1Nc` | 078 (squad of ten riders) made on the second try with the B09 batch. All kept. Chapters 1 and 2 are complete apart from the redo list |
| B09 | 081–089 | `1rCGNYpSXtoCCf7k2r1dwpGMG_BLwGhcB` | `1d5UwHaAftktoD0J2dK6jD2NHmX57Mk7r` | All nine kept on the first try (082, 085, 087 with reference faces; 085 and 087 used the cropped 071 as the reference for Temüjin in his forties). 087: the young warrior has short cropped hair, seen from behind, kept. Next: 090–099 |
| B10 | 090–099 | `16P47zLXfdS3z20eZDQ-U-uv46FJLWmVt` | `1nqB2eHxlZnKIXohgNzicVCxeqAXt5iwz` | All ten made on the first try. **096 and 098 → redo** (096: the khan's beard and hat do not match the reference; 098: palms and onion domes behind a Tangut city). Kept with small flaws: 092 and 093 (pen marks run across the page, unreadable; the boys have short present-day haircuts), 099 (the wall has brick battlements like the later Ming wall). 098 was written with standing envoys and resting camels, not kneeling men, to avoid the moderation block of 067. Chapter 3 is complete apart from the redo list. Next: 100–109 |
| B11 | 100–109 | `1eQm0UO5HZMG9FMqmX62bwqXj_UboTbAP` | `1IGITBo88BcgsUxiYiQBETl2eXVH7_P6N` | All ten kept on the first try. 104 (goods on the carpet) had a present-day glass window in the top left corner: crop entry in `shots/crops.json`. Next: 110–119 |

## Picture lessons so far

- Interiors and still lifes: say "small clay or bronze oil lamps only, no glass lamps, no bookshelves", or a 19th-century kerosene lamp appears (029, 054).
- Night scenes with many figures turn into drawn illustrations (058, 059). For those, drop "Painted-realism concept art" and write "a photographic film still shot on location at night, real people and real horses, not an illustration, not a painting".
- Crowds drift to present-day festival dress (050): name plain undyed wool and felt, no brocade, no bright sashes.
- A thin black bar on the top edge (011, 012): crop entry in `shots/crops.json`.
- One failed call counts against the limit of 10 pictures per turn.
- `tools/sheet.py` rebuilds `out/img` without the crops: always run `tools/crops.py` after it.
- Kneeling captives before an armed rider get blocked (067): show laid-down weapons instead.
- With two reference faces in one picture the ages drift (069): state each man's age and beard colour.

## After a full wipe of the workspace

1. `git fetch -q origin arena/d486087a-hyperframes && git reset -q --hard FETCH_HEAD` (only when the tree has no project files).
2. `bash tools/setup.sh` (builds `/tmp/hfenv.sh` and `/tmp/nkvenv`).
3. Download from Drive into `<repo>/google_drive/`: the narration zip, `EP15_cast.zip`, every `EP15_B*` and `EP15_R*` zip. Unzip the narration into `narration/`.
4. `bash tools/restore.sh`; `ln -sfn ../narration shared/vo; ln -sfn ../out/img shared/plates`.
