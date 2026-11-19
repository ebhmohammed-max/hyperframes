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

## After a full wipe of the workspace

1. `git fetch -q origin arena/d486087a-hyperframes && git reset -q --hard FETCH_HEAD` (only when the tree has no project files).
2. `bash tools/setup.sh` (builds `/tmp/hfenv.sh` and `/tmp/nkvenv`).
3. Download from Drive into `<repo>/google_drive/`: the narration zip, `EP15_cast.zip`, every `EP15_B*` and `EP15_R*` zip. Unzip the narration into `narration/`.
4. `bash tools/restore.sh`; `ln -sfn ../narration shared/vo; ln -sfn ../out/img shared/plates`.
