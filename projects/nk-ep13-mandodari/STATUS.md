# EP13 Mandodari: status

Topic in the user's words: "Untold story of ravaana and his wife". Shorter film: about 10 minutes, 198 pictures. Same pipeline as EP12 (`../nk-ep12-poompuhar/STATUS.md` has the full recipe and the lessons).

## Done on 17 Nov 2026

- Research by web search (no full texts read); see `FACT_SHEET.md`, doubts marked **check**.
- `script/script.mjs` v1: hook + 6 chapters, 108 lines, 8,778 characters. `node script/build.mjs` → `SCRIPT_TA.md`, `script/lines.json`, `narration/text/`.
- Scratch narration `voice-02`: `narration/N01.mp3` … `N07.mp3` = 597.8 s. `N08.mp3` is the channel end card audio (13.1 s, the same file as EP12's N11).
- `script/align.py` → `narration/align.json`; one line flagged for a listening check (N05 q05, a short line).
- Shot list: `shots/shots.txt` (198 rows), `shots/counts.json` (from line lengths: under 4.2 s one picture, under 8.6 s two, else three), `python3 shots/expand.py` → `shots/prompts.json`, `SHOTLIST.md`.
- Cast portraits (ravana, mandodari, maya, indrajit) made and checked; `shots/CAST.md`.
- Expected film length: 597.8 s narration + 12 s title + 17 s end card + 6 chapter cards of 2.3 s ≈ 10 min 41 s.

## Chapters

| Clip | Chapter | Lines | Seconds | Pictures |
|---|---|---|---|---|
| N01 | hook | 15 | 73.1 | 25 (001–025) |
| N02 | 01 பத்துத் தலை | 16 | 90.6 | 31 (026–056) |
| N03 | 02 மயன் மகள் | 14 | 82.3 | 27 (057–083) |
| N04 | 03 கேட்காத கணவன் | 15 | 77.5 | 26 (084–109) |
| N05 | 04 புலம்பல் | 17 | 92.8 | 30 (110–139) |
| N06 | 05 சீதையின் தாயா? | 15 | 87.1 | 28 (140–167) |
| N07 | 06 மருமகன் ராவணன் | 16 | 94.3 | 31 (168–198) |

## Drive

- Folder `EP13_Mandodari`: `1g9KaAHXx8aP1OlHJDtQP0ty4ZblHZ5qw`; subfolder `images`: `1LAGCCMejRgBeA0oPsteEccx84XnVHk0d`
- File ids: see the table at the end of this file.

## Next

1. Pictures in batches of ten: `python3 tools/next.py 10` prints the prompts; save to `<repo>/google_drive/ep13_pics/raw/NNN.jpg`; `python tools/sheet.py a b`; check; `python3 tools/pack.py a b`; upload the zip and the sheet to `images`; note the batch below; commit.
2. After a workspace reset: `git fetch` + fast-forward, `bash tools/setup.sh`, download `EP13_cast.zip` and the batch zips from Drive, `bash tools/restore.sh`.
3. Film stage, still to adapt from EP12: `film/gen.mjs` (`HOOK_FX` list for the new hook, subscribe pop-up timing in N02, `createdAt`), `film/title.mjs` (the three plates; the title text is already changed), `film/end.mjs` (uses `N08.mp3`; check the sentence timings comment). `tools/render.sh` and `tools/finish.sh` already list N01–N07.

## User correction, 17 Nov

The user sent a reference picture and said the first Hanuman "looks like small monkey". Hanuman is now always shown in full as a tall, mighty, crowned figure (cast key `hanuman`, made from the user's picture, stored as `cast/hanuman_user_ref.jpg`). Rama, Sita, Lakshmana and Shiva are still never shown by face. Pictures 002, 005, 006, 007 were remade; `shots/shots.txt` rows changed to `L@hanuman`.

## Open points

- Titles and script are drafts; no native Tamil read-through yet.
- Film is about 40 s over the 10-minute target. Cutting N07 q08–q09 (Ravana Kaviyam) would bring it to about 10 min 20 s.
- Fact sheet items marked **check**.

## Batches

| Batch | Pictures | Drive zip | Notes |
|---|---|---|---|
| cast | ravana, mandodari, maya, indrajit, hanuman | `EP13_cast.zip` `1ABYGdNUVcWcv5qNgUMg1oCrS8Ic-m6K4` (v2, with hanuman and the user's reference), Hanuman portrait `1xzVNEbzS0kuIUPoj9yLTHxpGYiVeWF_T`, sheet of the first four `1tPhfcagaC884vudSxKXSP6t-AkB4VSCx` | all accepted |
| B01 | 001–010 | `1X3gByyGcieCfZM1CmXCX66bTHV9H477y`, sheet `1klRgT21U1TCZsGR9zxHUCtQLYnQEBO_8` (v2; the first versions are in the Drive trash) | 002, 005, 006, 007 remade with the new Hanuman. 003 edge crop. 009 odd pose, kept. |
| B02 | 011–020 | `1SlDuT8jRai1OeyKzot_J8AEew4IEQ_24`, sheet `1UDo3LNvuxz-239g8pKL4mmQ4FKovHLWv` | 017 (casket looks like a coffin) in `shots/redo.txt`, cropped for now. 016 has Mughal-style arches and domes, kept as doubtful. 012: the king is in focus, kept. |
| B03 | 021–030 | `1-yt9dPlrqfLIMGikIQ5tjgU6XLxRZ1ei`, sheet `1PyM1F3Wk6Z9uvewLkuFG9em4ElxjtxsS` | 028 (comic-book style) in `shots/redo.txt`. 030 cropped to remove a sheet with print-like marks in the corner. Check sheets: `tools/big.py a b`. |
| B04 | 031–040 | `1lZ5Zo5r5PJ1Cx3Dac_J5x4wBFUXwCVFl`, sheet `1cvmbwjiQBukukbDfi5v-m8_SJrf3Zluv` | 038 (European crown) and 040 (hooded cloak) in `shots/redo.txt`. From this batch the prompts add "realistic like a film still, not a cartoon and no drawn outlines". |
| B05 | 041–050 | `1MH6DkOl0SS2LqHd7WhjILPAxtKXE7M7e`, sheet `1Up_bn9Dj8EK7XcZ4cnyRTjjCOv_UH7-I` | 050 (Shiva's foot looks old and veined) in `shots/redo.txt`. 045 cropped for a dark strip on the right. |
| B06 | 051–060 | `1Xjz3XAScvpUw6jiJfQ0A9kZTdMS4c5ZY`, sheet `1PLFbwebIhqtnjXU5jQiXq-ZAdJtXXiO-` | all ten accepted. 054 edge crop. 051 used 049 as a second reference. |
| B07 | 061–070 | `1dAALSJwBlxptbvfg27hmm_pVSf6Jf4la`, sheet `1pgn5hyIkLNmoR_PnFSfpIEoCrNtYs2V9` | all ten accepted. Young forest Ravana uses `raw/058.jpg` as reference (gold circlet, ochre dress); young Mandodari is described as "about eighteen, plain pale cream silk, white flowers in her braid, no crown" with the cast portrait (062 is the best reference for her from now on). |
| B08 | 071–080 | `1Ipz0yCHbWeU15_pFEyL6Em-5O1RR-rpH`, sheet `1_kUMmCBjC--rsAykZSgg1s-g0hI3Ab9D` | all ten accepted. 071 cropped for a dark left edge. 072 is more saturated than the rest, kept. `raw/001.jpg` works as a reference for the look of the city. |
| B09 | 081–090 | `1S4okD9cBAxHF2Ztst0h0sylGvdHhC49S`, sheet `19Llvnz_Y686FGG0DjwKByw-BKcoSPseX` | 081 (European crown) in `shots/redo.txt`. 085 edge crop. 088: Dhanyamalini changed from green to blue silk so she is not mistaken for Mandodari (`shots.txt` updated). 090: she holds his other arm, not the sword arm; kept. 087 slightly storybook in style, kept. |
| B10 v2 | 091–100, complete | `1MxQsIfD28wZq9Y8gtW0zckAlTRGAqCYj`, sheet `1JOJKCu9Tqo7ERAV-Bb-wC3m0Xd9awOKh` | Replaces the first B10 upload (nine pictures, trashed). Holds 096 (new) and the remade 098 and 100. 094 palm leaf has script-like marks that cannot be read; kept. |
| R1 (redo pass 1) | 017, 028, 038, 040, 050, 081, 096, 098, 100 | `1tV3VzBZ8IpJpH6qsLgU0aEnoCWnGObFD`, sheet `1Lt5eWKwB2t-0a2HxKe8EaQRQJKJwVYDL` | Nine pictures made again, all accepted; `shots/redo.txt` is empty. Same file names as in the batch zips B02–B05, B09, which still hold the first versions: unpack R1 last (`tools/restore.sh` does). First versions kept locally in `google_drive/ep13_pics/raw_v1/`. Crop entry for 017 removed. |

## Drive file ids

| File | Id |
|---|---|
| `EP13_SCRIPT_TA_v1.md` | `1P0cX5qGoFa1NjAAMVt1ThC74XQCCFwUn` |
| `EP13_FACT_SHEET.md` | `1f9ouyG8PtJ-pN1zwk6Odddynrhr4SzoF` |
| `EP13_SHOTLIST.md` | `1RCAS3Sb1Ho8TC3ipbePSAQ9QHhyfCuIn` |
| `EP13_narration_scratch_voice02.zip` (N01–N07 + end card N08) | `1SgZFcMdPWN2VSi_4qOawtvR13q5Drbuo` |
