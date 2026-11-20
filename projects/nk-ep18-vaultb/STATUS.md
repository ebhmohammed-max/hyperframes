# EP18 "பத்மநாபசுவாமி கோயில்: திறக்காத கதவு (B நிலவறை)" (the door nobody opened): status

Topic and length (about 8 minutes) chosen by the user on 20 Nov 2026 (topic bank T1, playlist புதையல் வேட்டை). Same recipe, voice (`voice-02`) and styles as EP17, including the harder hook, the graphics layer (`film/fx.mjs`) and a picture behind each chapter card. The recipe itself is described in `projects/nk-ep17-1926/STATUS.md` and the lessons in `projects/nk-ep12-poompuhar/STATUS.md`.

## Done (20 Nov 2026)
- Research (nine web searches, read as extracts) → `FACT_SHEET.md`, with nine doubts listed at the end.
- Script v2: `script/script.mjs` → `SCRIPT_TA.md`, 7 clips, 70 lines, 7,249 characters.
- Narration N01–N07 with `voice-02`, 497.86 s; `narration/align.json` (0 lines flagged). `N08.mp3` (end card voice) as in EP16 and EP17.
- Shot list: 127 pictures (`shots/shots.txt` → `shots/prompts.json`, `SHOTLIST.md`); rules in `shots/CAST.md`.
- Reference pictures: temple tower, iron door, petitioner from behind (`out/cast/`).
- Graphics added to `film/fx.mjs`: door counter (`step`), six doors A to F (`vaults`), map of Thiruvananthapuram (`map: "tvm"`), audit page mock-up (`mock: "report"`). Checked on still frames without pictures.
- All nine clips generate (`film/gen.mjs`, `title.mjs`, `end.mjs`); film length 546.5 s (9 min 7 s).

## Next
1. Pictures: `python3 tools/next.py 10` prints the next ten prompts; after each ten, `bash tools/restore.sh`, `$PY tools/batch.py <batch> <first> <last>`, look at `google_drive/_sheet.jpg`, upload the zip to the Drive `images` folder, add a row below, commit and push.
2. When all 127 are in: `node film/gen.mjs N01` … `N07`, `node film/title.mjs`, `node film/end.mjs`; look at stills; `bash tools/render.sh` (background process, about 75 minutes on 2 CPUs).
3. `bash tools/finish.sh parts`, then `VB=1300k bash tools/finish.sh 720` (the film is 13 s longer than EP17, so a little lower than EP17's 1350k); frame sheets; upload the eight files; final status.

## Chapters
| Clip | Card | Lines | Seconds | Pictures | Added graphics |
|---|---|---|---|---|---|
| N01 | (hook) | 10 | 62.8 | 21 (+6 reused) | giant "1 லட்சம் கோடி ரூபாய்", three rumours, six chapter words |
| N02 | கடவுளுக்கு எழுதி வச்ச நாடு | 10 | 73.4 | 14 | map, number cards (18 அடி, 1750), six doors A to F |
| N03 | ஒரு மனுஷன், ஒரு வழக்கு | 9 | 65.1 | 16 | timeline Jan, May, June 2011 |
| N04 | மூணாவது கதவு | 10 | 60.7 | 16 | door counter 1/3, 2/3, 3/3 (turns red when the latch jams) |
| N05 | நட்சத்திரம் மாதிரி தங்கம் | 10 | 72.8 | 21 | number cards (1,00,000 coins; ₹90,000 கோடி +, "no official value") |
| N06 | பாம்பா? பூட்டா? | 10 | 78.8 | 20 | "மந்திரம்", "பாம்பு" struck out |
| N07 | எத்தனை தடவை? | 11 | 84.1 | 19 | giant "7", audit page mock-up, timeline |

Title card: "B நிலவறை" / "திறக்காத கதவு · பத்மநாபசுவாமி கோயில்". Subscribe pop-up: N02, line 5.

## Picture rules
See `shots/CAST.md`. In short: everything under the temple is an illustration (no photographs exist); the god is never shown clearly; real people only from behind or as hands; legends in their own dream-like look; the iron door always plain; no readable writing.

## Open points
- The doubts in `FACT_SHEET.md`, above all two phrases that are already recorded: "ஏழு பேர் கொண்ட குழு" (N03 line 5) and "பல சாவி போட்டு" (N04 line 0). Changing either means new narration for that chapter.
- The pictures of the vault and the treasure follow written descriptions. A viewer may take them for photographs, so the description under the video should say they are illustrations.
- Sound will again be measured, not heard.

## Drive
Root "NK Documentaries" `1WqhshH9XcvNUna4lzyS692eidgWQfeS1` → folder `EP18_Padmanabhaswamy_Vault_B` `1AWPWp9D67uhUGpXjGYwdB4rGpxa16ClN` → `images` `107fpnq6KliPPPrmtMSfE2kLiQ_UpYn-c`.

| File | Drive id |
|---|---|
| `EP18_narration_scratch_voice02.zip` (N01–N08) | `1k1niWSfD489oe_3Z0c0GDzt10c5RoQqu` |
| `EP18_SCRIPT_TA.md` | `1ZA1A4f0EplAZzyRDFpFgGTtV6BDshJDM` |
| `EP18_FACT_SHEET.md` | `1RQYtaiw7E6mPCqJbUeTpu7UxZWsq4MWU` |
| `EP18_SHOTLIST.md` | `1OCNLJW5HzC42kORveijWyWykfbOhkIxP` |
| `images/EP18_cast.zip` (three reference pictures) | `1ZKnS6SVWAAyKUsi9noKyKIb_W0IIK2KN` |

## Picture batches
| Batch | Pictures | Zip on Drive | Notes |
|---|---|---|---|

## After a full wipe of the workspace
`git fetch -q origin arena/d486087a-hyperframes && git reset -q --hard FETCH_HEAD`, `bash projects/nk-ep18-vaultb/tools/setup.sh`, download the Drive zips above into `<repo>/google_drive/`, `bash tools/restore.sh`, unzip the narration zip into `narration/`, recreate the links `shared/vo` → `../narration` and `shared/plates` → `../out/img`.
