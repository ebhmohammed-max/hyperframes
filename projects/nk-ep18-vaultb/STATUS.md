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
1. Pictures (127 of 127 made and accepted, 14 of them remade; clips regenerated with no missing picture; film rendered and packaged; see "Film rendered" at the end): `python3 tools/next.py 10` prints the next ten prompts; after each ten, `bash tools/restore.sh`, `$PY tools/batch.py <batch> <first> <last>`, look at `google_drive/_sheet_Bnn.jpg`, upload the zip to the Drive `images` folder, add a row below, commit and push.
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
| `EP18_SHOTLIST.md` (first version; prompts for looks V and G changed after B01, upload again at the end) | `1OCNLJW5HzC42kORveijWyWykfbOhkIxP` |
| `images/EP18_cast.zip` (three reference pictures) | `1ZKnS6SVWAAyKUsi9noKyKIb_W0IIK2KN` |

## Picture batches
| Batch | Pictures | Zip on Drive | Notes |
|---|---|---|---|
| B01 | 001–007 | `EP18_B01_images_001-007.zip` `1XehplgHRQxkeW1W69qsUtlqWk4JPJ0rS` | 002–005 fine. **001, 006, 007 to be made again** (`shots/redo.txt`): faces showing in 001; carved walls, god figures and flaming torches in 006 and 007. Looks V and G tightened after this batch |
| B02 | 008–017 | `EP18_B02_images_008-017.zip` `1_V7VxBiCD3rEJQcWsrKG9QZ4IqZAw-SW` | All usable. **009 to be made again**: the chain reads as a pale ship's chain, not gold. 011 has a blank plate over the door (no writing; kept) |
| B03 | 018–027 | `EP18_B03_images_018-027.zip` `1jB_d0JnDJOWEdVQmlW0YZZjAWmVo9h_j` | All usable. **022 to be made again**: a dark standing figure shows in each doorway, but the image in this temple is one reclining figure seen in three parts; the doorways should hold lamp glow only |
| B04 | 028–037 | `EP18_B04_images_028-037.zip` `1FeWeIZbpf26jfX1Ijfd0gOp_MfJKkXqz` | All usable; the petitioner matches his reference in 035 and 036 |
| B05 | 038–047 | `EP18_B05_images_038-047.zip` `119tQ2PrpDLcNsTurS-jtYwARiJ1IqMDn` | All usable. 044 has a small wall plate (not readable). 045 shows seven men, in step with the unverified "seven-member team" of the narration |
| B06 | 048–057 | `EP18_B06_images_048-057.zip` `1Lqh__2CDb48jjcqV_2gwW_hodo5bM71Q` | All usable. 048 and 049 were written by hand (a lit store room, not the dark-vault look). 052 shows a bunch of keys, in step with the unverified "many keys" of the narration |
| B07 | 058–067 | `EP18_B07_images_058-067.zip` `1L31ULSZM5qcAEDsW8AeQ20y__OfEHB9g` | 058, 059, 062–067 usable (the firemen in 064 are seen partly in profile; invented faces). **060 and 061 to be made again**: 060 is an awkward row of five men bent over, seen from low behind; 061 has carved pillars behind the slab and a thin black strip along the top edge |
| B08 | 068–077 | `EP18_B08_images_068-077.zip` `14PHZoBIolK-fwCdc5ikphGOcx4VDqJ8h` | 069–075, 077 usable (074: the chain lies doubled and the corridor has plain pilasters; kept). **068 and 076 to be made again**: 068 is bright and over-sharpened, not "gold like stars in the dark" (it is also the N05 chapter-card background); 076, the cloth-wrapped figure, reads as a bandaged child with a face-shaped hollow |
| B09 | 078–087 | `EP18_B09_images_078-087.zip` `1eab9IECWuoWf-89JDwU7iDvEmrLORqi3` | All usable. 079: the bowl rims show little of the gem setting; 080: the diamond is nearer egg size than thumb-top size; 083: newspaper print is blurred bars, unreadable; 085: the three doorways hold only lamp glow (the model for remaking 022) |
| B10 | 088–097 | `EP18_B10_images_088-097.zip` `1ieYq9GnHi6EVCWVXK9dmJ2yfqzgBnWKn` | 088–095 usable (094 shows eight priests with bowed heads, no clear faces). **096 and 097 to be made again**: 096 is a forearm standing upright from the floor like a cut-off arm; 097, the cobra door of the legend (also the N06 chapter-card background), stands in round European crypt arches |
| B11 | 098–107 | `EP18_B11_images_098-107.zip` `1qbclPI8rcv1wHcGCUgaa2y5coqUQ28Vo` | 098, 100–107 usable (101: the men climb steps toward the doorway rather than going down; 104: the door plates form a grid of panels, a little unlike the reference). **099 to be made again**: the "sea behind the door" legend came out as a rubble-stone tower beside an open sea, which does not read |
| B12 | 108–117 | `EP18_B12_images_108-117.zip` `1IKIwZPgaE1WhffbOTcEbPkUDgPZeLQOt` | All usable. 112 shows exactly seven slips (the N07 chapter-card background); register and inventory writing is unreadable scribble; 115 is more a corridor with plain pilasters than a small room, the door small at its end. Checked by `grep`: all six `CARD_BG` names exist in `shots/shots.txt` |
| B13 | 118–127 | `EP18_B13_images_118-127.zip` `1sElo9tTqban6mL_vFwQ6Wqcx0ucSz1Q3` | 118–123, 126, 127 usable (122 shows four members and one empty chair). **124 and 125 to be made again** as a matching pair: in 124 the gold bars look like grey-brown bricks; 125 is a barrel-vaulted brick cellar, unlike 124 and unlike the granite of the rest. Remake 125 first, then 124 with the new 125 as reference |
| R1 | remakes of 001, 006, 007, 009, 022, 060, 061, 068, 076, 096 | not zipped yet (one remake zip `EP18_B99_images_remakes.zip` after R2) | 006, 007, 009, 022, 060, 061, 068, 076, 096 accepted (old versions kept in `google_drive/ep18_pics/old/`). 068 is darker but still shows heaps and a lit doorway; kept. **001 again**: six men, not five. Review sheet tool: `tools/redo_sheet.py <name> <numbers…>` |
| R2 | remakes of 001 (third and fourth try), 097, 099, 125, 124 | `EP18_B99_images_remakes.zip` `1Nee6sGu_edCJWddqT26rjIHhPEk2tDqa` (all 14 remakes; these replace the same numbers in B01–B13; copy it into `google_drive/` beside the batch zips so that `tools/restore.sh` unpacks it last) | All accepted. 001: five men around the floor slab, seen through a doorway (a spare version is `google_drive/ep18_pics/old/001_alt.jpg`). 125 and 124 are the same chamber, empty and full of gold. `shots/redo.txt` is empty |

## After a full wipe of the workspace
`git fetch -q origin arena/d486087a-hyperframes && git reset -q --hard FETCH_HEAD`, `bash projects/nk-ep18-vaultb/tools/setup.sh`, download the Drive zips above into `<repo>/google_drive/`, `bash tools/restore.sh`, unzip the narration zip into `narration/`, recreate the links `shared/vo` → `../narration` and `shared/plates` → `../out/img`.

## Film rendered (20 Nov 2026) — uploads of the video files still owed

All nine clips rendered (`tools/render.sh`: about 6 to 7.5 s of work per film second this time, 58 minutes in all), joined and levelled
(`tools/finish.sh parts`, then `VB=1300k tools/finish.sh 720`). Measured sound of the joined film: −16.88 LUFS before, gain +2.88 dB;
the 720p file measures −14.34 LUFS, peak −1.47 dBTP. Frame sheets of every part and of the 720p file were viewed: pictures, captions,
tags, chapter cards 01–06, map, vault row, door counter, figure panels, timelines, report mock-up and end card are all correct.

| File (in `google_drive/ep18_up/` and `out/deliver/`) | Bytes | Seconds | On Drive |
|---|---|---|---|
| `EP18_1080p_01_hook_title.mp4` | 65,014,506 | 75.85 | not yet |
| `EP18_1080p_02_ch1.mp4` | 58,543,217 | 76.55 | not yet |
| `EP18_1080p_03_ch2.mp4` | 67,160,371 | 68.29 | not yet |
| `EP18_1080p_04_ch3.mp4` | 55,938,978 | 63.89 | not yet |
| `EP18_1080p_05_ch4.mp4` | 69,220,774 | 75.92 | not yet |
| `EP18_1080p_06_ch5.mp4` | 62,886,040 | 81.99 | not yet |
| `EP18_1080p_07_ch6_endcard.mp4` | 82,231,881 | 104.25 | not yet |
| `EP18_VaultB_full_720p.mp4` | 95,998,177 | 546.63 | not yet |
| `EP18_SHOTLIST.md` (final; upload as `EP18_SHOTLIST_final.md`) | 164,742 | | not yet |

The first upload attempt (eight calls at once) was refused by the connector's upload rate limit; nothing was sent. Upload them a few at
a time into the episode folder `1AWPWp9D67uhUGpXjGYwdB4rGpxa16ClN` (`content_mime_type: video/mp4`), then fill in this table.
The mp4 files are not in git and vanish in a wipe of ignored files only from `out/`; the copies in `google_drive/ep18_up/` are untracked
but not ignored... (`*.mp4` is ignored inside the project only), so they should survive like the pictures did.
