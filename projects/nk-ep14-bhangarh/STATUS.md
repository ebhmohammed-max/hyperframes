# EP14 Bhangarh: status

Topic in the user's words: "Bhangarh Fort", about 10 minutes. Same pipeline as EP13 (`../nk-ep13-mandodari/STATUS.md`; the full recipe and lessons are in `../nk-ep12-poompuhar/STATUS.md`).

## Done on 18 Nov 2026

- Research by web search (extracts only, no full pages); see `FACT_SHEET.md`, doubts marked **check**.
- `script/script.mjs` v1.1: hook + 6 chapters, 94 lines, 8,756 characters. `node script/build.mjs` → `SCRIPT_TA.md`, `script/lines.json`, `narration/text/`.
  - v1.1: chapter 5 (N06) rewritten after the board was read from a photograph. It has three rules (no entry before sunrise or after sunset; no cattle; do not harm the kewda trees), not the two that most websites quote.
- Scratch narration `voice-02`: `narration/N01.mp3` … `N07.mp3` = 588.0 s (N06 recorded again for v1.1). `N08.mp3` is the channel end card audio (13.1 s, same file as EP13).
- `script/align.py` → `narration/align.json`; no line flagged.
- Shot list: `shots/shots.txt` (185 rows), `shots/counts.json` (under 4.2 s one picture, under 8.6 s two, else three), `python3 shots/expand.py` → `shots/prompts.json`, `SHOTLIST.md`.
- Reference pictures (ratnavati, singhia, gate, bazaar, palace, temple, board) made and looked at on one sheet; `shots/CAST.md`.
- Tools, kit and film generators copied from EP13 and renamed to EP14. **Still to adapt before the film:** `film/gen.mjs` (`HOOK_FX`, subscribe pop-up line), `film/title.mjs` (three plates, title and subtitle text, check the width).
- Expected film length: 588 s narration + 12 s title + 17 s end card + 6 chapter cards of 2.3 s ≈ 10 min 31 s.

## Chapters

| Clip | Chapter | Lines | Seconds | Pictures |
|---|---|---|---|---|
| N01 | hook | 13 | 74.8 | 26 (001–026) |
| N02 | 01 ஒரு முழு நகரம் | 14 | 86.9 | 27 (027–053) |
| N03 | 02 நிழல் சாபம் | 13 | 73.1 | 23 (054–076) |
| N04 | 03 ரத்னாவதி | 13 | 76.3 | 24 (077–100) |
| N05 | 04 பதிவு சொல்றது | 14 | 93.1 | 29 (101–129) |
| N06 | 05 அந்த பலகை | 14 | 99.4 | 31 (130–160) |
| N07 | 06 கதை ஏன் சாகல | 13 | 84.4 | 25 (161–185) |

## Picture rules for this episode

- No ghost or apparition in any picture. The film's point is that there is none on record.
- Guru Balu Nath (honoured at a shrine on the site) and all real rulers: never by face.
- Ratnavati and Singhia are legend figures with invented faces.
- The board's lettering is never readable in a picture; the real wording goes on screen as text in the edit.
- Web photographs of the site (`<repo>/google_drive/ep14_pics/webref/`) were used only to see what the places look like. They are not in the film and were not given to the picture tool.

## Open points

- The script has had no native Tamil read-through; the title is a draft.
- **check** items in `FACT_SHEET.md`, mainly: "80 km" (sources say 83–88), "9,000 houses" (one source), Sariska's area, the night animals, the ASI officer's statement, the 30 % famine figure, "டெல்லியில அக்பர் ஆட்சி".
- The board wording was read from a small photograph.

## Drive

- Folder `EP14_Bhangarh`: `1TYhdz_IVwEkR7oLt5nHhZQXhdW5MKc8l`; subfolder `images`: `1B7qz5mFGGS2nxRrNIwISD0MFbql1jOtR`

| File | Id |
|---|---|
| `EP14_SCRIPT_TA_v1.1.md` | `1NHF1I1Ax53GKqZ-_hWpfdLEC-f4DXLke` |
| `EP14_FACT_SHEET.md` | `1CCpsKseSPKx7V9oKTp5Jz91eyb50YN6g` |
| `EP14_SHOTLIST.md` | `1_Hju9gt-MYYW3kPSt8tPD2Jkr3IGl75O` |
| `EP14_narration_scratch_voice02.zip` (N01–N08) | `1fLGT2pq4Y2YLC2MZMFxSiBFEuifTTztR` |
| `images/EP14_cast.zip` | `1HqlManPTUV4dVNwURJkkIFI3ep4FH-QR` |
| `images/EP14_cast_sheet.jpg` | `1xazMwa71ZuYo44pDyaCK4MWFKPJwOVxI` |

## Batches

| Batch | Pictures | Zip id | Sheet id | Notes |
|---|---|---|---|---|
| B01 | 001–010 | `1-axuM4wvc5GM3T2-i32ytP5LQbaJvqc3` | `16eslyo5DAhi1EBV46lLhIHiHIFD55FMy` | 003 to redo: the board came out as a smeared panel without lettering. Board wording in `shots/expand.py` strengthened after this. 004: lettering soft and unreadable, emblem invented (not the state emblem), kept. |
| B02 | 011–020 | `1Rtz2g0O1O-Z-gaCZuKUlEzWZ9hDZST2K` | `1fx1OzSafkqHVN7ncvNWQgWdAoyzgzkWx` | all kept. 015 flagged by the edge check only because the walls are dark. Ratnavati (017) and Singhia (018) match their reference pictures. |
| B03 | 021–030 | `11RkHqTWGQySWUEsb4GFyZsUIznxvo82k` | `1zxdvsYFYm0g0Dqy58O5f6ZpDUzy69nmB` | 026 to redo (came out as a drawn illustration with outlines). 021: the board has lettering now. 023 flagged by the edge check only for dark corners. 028: courtiers sit in rows, kept. |
| B04 | 031–040 | `1fdMGym1bK_mJEiXbiIb9kWnGBYTDJD89` | `1nCCW6Q5-1swSaDPuUgHKyG7usSw4GtZL` | all kept. 037 (bird's-eye view): the town sits on a rise with the palace at the top and shows one clear wall ring, not three; the three rings are clear in 039. Prompts for 032, 033, 038 written by hand as a town under construction. |
| B05 | 041–050 | `1GK66gM3_1MizU-1hr7GxJbIPKDYcHDTs` | `15VSGJV57w9ixSfLdQVFhhyTpqlNFf1QL` | all kept. Temple (044, 045) and palace (047, 048) match their reference pictures; 048 shows the palace whole and taller. |
| B06 | 051–060 (057 missing) | `1-cFLkjNz8OPRvmNvt0YlWA2qzbdjnah9` | `1MeCvMtCCEbtexDQ0Ilr8_fcxCpC9ycIM` | 057 not made: the picture tool failed once and the turn limit was used up; on the redo list. 054 (elders at the fire): some faces show in the firelight, small and invented; kept. Hermit in 059 from behind, king's face hidden. Prompts 056–060 written by hand (valley without a town). |
| B07 | 061–070 | `1cv3QgWDC0fr5jsDvGRpJQfRzoxegxeMh` | `1Ohbr1k6y7p7LzKs7c4Kccv5dxe63Ny6N` | all kept. 069: the hermit's hair is wrapped in a cloth, not coiled (seen from behind, kept). 064, 065, 067: the palace sits higher on the hill than in the reference. All ten prompts written by hand from the shot list. |
| B08 | 071–080 | `1HatR092Z_OxGmSdj_oWylxJkR4Bsjj9a` | `1PUZfAU0mPJUwmLJGvSYC0wqFyUy0c8Hq` | all kept. Ratnavati (078–080) matches her reference picture. 072: frame cut at chest height, one chin shows at the top edge. |
| B09 | 081–090 | `1i_K_kAReDnmFwxnuKM5VQ0MiF3QyFffM` | `1VvZGbpR1A-MCha1a6NErlmiHGkeww6VL` | all kept. Singhia (082–084, 086) and Ratnavati (089) match their reference pictures. The bottle in 089 is rounder and larger than in 076 and 087. 081 flagged by the edge check only for a bright window corner. |
| B10 | 091–100 | `10T0qHUhOL6eKMTdKmDlLLQvhJfBMNSZP` | `1QuaJPmuKkd-3HIAyS4KiwJbMSDzEccfM` | all kept. 092: the boulder shows as a dark round shape at the top edge with its shadow on the ground; nobody is hurt in any picture. Chapters hook to 03 (N01–N04) are complete except 003, 026, 057. |
| B11 | 101–110 | `1gN1IgtW24Il0dwrEErISwhufTxh7gNVF` | `1M29feugSs9PtFpEYBVd7mFBSRADArgv-` | all kept. Gateway in 107 and 109 matches the reference. 105: the palace far behind the half-shut bazaar already looks worn. 109: the elephants are hard to make out in the dust. |
| B12 | 111–120 | `1nHqKZVld_RPAo1GGIy5hyyTmSZO4Nvyj` | `11QOW8bexDf3yUnUf8J4orwx9YdpEZVrM` | nine kept; **119 to redo** (looks like a present-day photo: grey cement, buttoned shirt, modern trowel). 113 came with a rounded dark photo border, trimmed 3 % on each side in `shots/crops.json`; its stepwell is a larger, more intricate one than Bhangarh's. No suffering shown in the famine pictures. |

## Next

1. Pictures, ten per turn: `python3 tools/next.py 10` → `generate_image` to `google_drive/ep14_pics/raw/NNN.jpg` → `/tmp/nkvenv/bin/python tools/sheet.py a b`, `big.py a b` → look → `crops.py` → `python3 tools/pack.py a b` → upload zip and sheet to `images` → table above → commit.
2. Film: adapt `film/gen.mjs`, `film/title.mjs`; `. /tmp/hfenv.sh`; generate, `bash tools/render.sh` (about an hour), `bash tools/finish.sh parts`, `VB=1000k bash tools/finish.sh 720`; upload in the same turn.
