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

## Open points

- Titles and script are drafts; no native Tamil read-through yet.
- Film is about 40 s over the 10-minute target. Cutting N07 q08–q09 (Ravana Kaviyam) would bring it to about 10 min 20 s.
- Fact sheet items marked **check**.

## Batches

| Batch | Pictures | Drive zip | Notes |
|---|---|---|---|
| cast | ravana, mandodari, maya, indrajit | `EP13_cast.zip` `1r-tgA5zX_NpZyBY7aJpQfBMwQItAfuDG`, sheet `1tPhfcagaC884vudSxKXSP6t-AkB4VSCx` | all four accepted |

## Drive file ids

| File | Id |
|---|---|
| `EP13_SCRIPT_TA_v1.md` | `1P0cX5qGoFa1NjAAMVt1ThC74XQCCFwUn` |
| `EP13_FACT_SHEET.md` | `1f9ouyG8PtJ-pN1zwk6Odddynrhr4SzoF` |
| `EP13_SHOTLIST.md` | `1RCAS3Sb1Ho8TC3ipbePSAQ9QHhyfCuIn` |
| `EP13_narration_scratch_voice02.zip` (N01–N07 + end card N08) | `1SgZFcMdPWN2VSi_4qOawtvR13q5Drbuo` |
