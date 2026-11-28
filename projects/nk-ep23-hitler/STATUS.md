# EP23 status: ஹிட்லர்: வீடில்லாதவனில் இருந்து ராட்சசன் வரை (Hitler: From Homeless to Monster)

Target 105 minutes, 12 chapters and a hook. Plan and chapter table: `OUTLINE.md`. Built and delivered chapter by chapter.

## Second review, 26 Nov 2026 (user: show his real face, young face too, film feel, say "February")

- **February:** the voice mispronounced "பிப்ரவரி". The spoken text now says "February" in English (N10, N11, N14 spoken again, aligned, 0 flagged; captions keep பிப்ரவரி). Later scripts: write "February" in `say`.
- **Faces:** the old rule (no face) is gone; see `shots/CAST.md`. Reference pictures in `out/cast/` (Drive `images/EP23_cast.zip`); `shots/prompts.json` lists the pictures to pass for each row (`python3 tools/next.py n` prints them). Hook pictures made again with faces: 004, 008, 010, 012, 017 (Drive `images/EP23_R1_images_faces_…zip`; the faceless first versions are in the B01 and B02 zips).
  - 012 (the doorway close-up) was made again from `cast/A.jpg` in the next turn and is back in the film (Drive `images/EP23_R2_images_face_012.zip`).
  - Shot rows 021–090 rewritten so that he, his parents, Kubizek, Hanisch, Dr Bloch and Morgenstern are seen from the front (38 rows changed; 8 shot names changed).
- **Film look:** 2.2:1 frame with black bars of 104 px (`BAR` in `film/gen.mjs`, also in `film/title.mjs`); evidence tag inside the top bar; captions just above the bottom bar; `SHIFT` moves a picture down when a head sits high; every picture prompt now asks for a 35mm film still composed for that crop. Added in the turn after: grain 0.15 at 24 fps, a faint flicker layer (`#p-flick`), dissolves of 0.5 and 0.9 s in the chapters (the hook keeps its hard cuts), and a low room tone under every clip (`shared/sfx/room-tone.mp3`, 100 s, −30 dB, played at 0.3).
- Hook: `EP23_1080p_00_hook_title_v3_film.mp4` is the current one (all of the above, 012 back in). `…_v2_film.mp4` and the first version stay on Drive.
- **Pictures made:** 001–048 (034 made in the turn after its failure). **030** came out upright (944×1122) and is cropped and soft: make it again when a call is free. To make: 049–053 (rest of chapter 1), 054–090 (chapter 2), 091–127 (chapter 3), 128–169 (chapter 4): `python3 tools/next.py 10` lists the next ten with their reference pictures and prompts. Ten image calls per turn is the limit, so pictures are the slow part: about 12 turns for what is planned so far.
- **Chapters 3 and 4 are written, spoken and aligned (0 flagged)**: `script/ch03.mjs` (N19–N26, 566.1 s, fact rows 96–140), `script/ch04.mjs` (N27–N34, 582.6 s, fact rows 141–188; it builds captions with a helper `L(say, tag, [[spoken, written]…], fx)`). Shot rows are written for both (091–127, 128–169), with `CARD_BG` for N19 and N27, look **W** (Western Front) and ref **S** (the soldier; likeness photograph `cast/S_photo.jpg`, shipped inside the B05 zip), look **M** (Munich 1919–1923) and ref **P** (the party speaker, from `H_photo.jpg`, "twelve years younger").

## Where it stands (27 Nov 2026)

| Part | Script | Narration | Timing | Pictures | Film | On Drive |
|---|---|---|---|---|---|---|
| Hook (N01–N02) + TITLE | done | done, 92.3 s | 0 flagged | 001–020 made (all) | part `EP23_1080p_00_hook_title_v3_film.mp4` (106 s) on Drive | narration, B01, B02, R1, R2, film |
| Ch 1 (N03–N10) | done | done, 535.9 s | 0 flagged | 021–053 made (all) | **all eight clips rendered and checked**; parts `…01_ch01a.mp4` (N03–N06) and `…01_ch01b.mp4` (N07–N10) | narration, B03–B06, clips, ch01a, ch01b |
| Ch 2 (N11–N18) | done | done, 598.4 s | 0 flagged | shot rows 054–090, all made | N11–N18 all rendered and checked (N13 rendered again with the new 067 and `cuts` on its bench/café/convent line) (in `clips_work`); parts ch02a (N11–N14) and ch02b (N15–N18) packaged | narration |
| Ch 3 (N19–N26) | done | done, 566.1 s | 0 flagged | shot rows 091–127, none generated | built (`film/N19`…`N26`), 576 s | narration, script, fact sheet |
| Ch 4 (N27–N34) | done | done, 582.6 s | 0 flagged | shot rows 128–169, none generated | built (`film/N27`…`N34`), 592 s | narration, script, fact sheet |
| Ch 5 (N35–N42) | done (27 Nov) | done, 438.2 s | 0 flagged | shot rows 170–209 (look **G**, ref **Q**), none generated | `node film/gen.mjs N35 … N42` works; `CARD_BG` N35 set | narration, script, fact sheet |
| Ch 6 (N43–N50) | done (27 Nov) | done, 383.7 s | 0 flagged | shot rows 210–244 (look **D**, ref **H**), none generated | `node film/gen.mjs N43 … N50` works; `CARD_BG` N43 set | narration, script, fact sheet |
| Ch 7 (N51–N58) | done (27 Nov) | done, 374.8 s | 0 flagged | shot rows 245–279 (look **X**, ref **H**), none generated | `node film/gen.mjs N51 … N58` works; `CARD_BG` N51 set | narration, script, fact sheet |
| Ch 8 (N59–N66) | done (27 Nov) | done, 456.3 s | 0 flagged | shot rows 280–324 (look **X**, ref **H**), none generated | `node film/gen.mjs N59 … N66` works; `CARD_BG` N59 set | narration, script, fact sheet |
| Ch 9 (N67–N73; N74 unused) | done (27 Nov) | done, 400.0 s | 0 flagged | shot rows 325–361 (look **X**, ref **H** in five), none generated | `node film/gen.mjs N67 … N73` works; `CARD_BG` N67 set | narration, script, fact sheet (rows 372–413, check points 39–43) |
| Ch 10 (N75–N81; N82 unused) | done (27 Nov) | done, 517.4 s (N81 narrated again 27 Nov: children's figure 15 lakh, as in the hook) | 0 flagged | shot rows 362–409 (looks **X**, **O**; ref **H** in two), none generated | `node film/gen.mjs N75 … N81` works; `CARD_BG` N75 set | narration, script, fact sheet (rows 414–460, check points 44–49) |
| Ch 11 (N83–N90) | done (27 Nov; N90 added to lengthen: Warsaw, Paris, the rockets, the call-up) | done, 576.5 s | 0 flagged | shot rows 410–459 (looks **X**, **O**; ref **H** in six), none generated | `node film/gen.mjs N83 … N90` works; `CARD_BG` N83 set | narration, script, fact sheet (rows 461–506 with 504a–e, check points 50–56, 63) |
| Ch 12 (N91–N98) | done (27 Nov; N92 added to lengthen; Dresden said as three days; N98's closing lines reuse the hook's pictures) | done, 596.0 s | 0 flagged | shot rows 460–499 (looks **X**, **O**; ref **H** in six, from behind or far), none generated; reused in N98: 003, 004, 013, 018, 019, 203, 212, 322, 406, 408 | `node film/gen.mjs N91 … N98` works; `CARD_BG` N91 set | narration, script, fact sheet (rows 507–558 with 513a–h, check points 57–62, 64) |

**The whole narration is recorded: 101 min 53 s** (hook 1 min 32 s, chapter 1 8 min 56 s, chapter 2 9 min 58 s, chapter 3 9 min 26 s, chapter 4 9 min 43 s, chapter 5 7 min 18 s, chapter 6 6 min 24 s, chapter 7 6 min 15 s, chapter 8 7 min 36 s, chapter 9 6 min 40 s, chapter 10 8 min 37 s, chapter 11 9 min 37 s, chapter 12 9 min 56 s). With the title card, twelve chapter cards (2.3 s each) and the end card the film lands near 103 min (asked for: 1 h 45 min). Pictures: 499 rows; 001–203 made; 204–499 to make. Renders: N03–N33, N35 and the END card done and on Drive; parts through ch04a (N27–N30) delivered. N34 waits only for picture 164 (make it first next turn, then render N34 and package part ch04b = N31–N34; download N31–N33 from `clips_work` first; N34 also uses 094 from the B10 zip). N36 waits for 175–179. After the wipe of 27 Nov (15:28 UTC) only what the current turn needs is restored: download the narration zip of the chapter being rendered, the cast zip, B05 (for `S_photo.jpg`) and the batch zips of the pictures in use. A missing mp3 makes a render fail at once.

## Next steps

1. Pictures, 10 per turn: `python3 tools/next.py 10` → generate to `google_drive/ep23_pics/raw/NNN.jpg` (pass the listed reference pictures) → `$PY tools/sheet.py a b` → zip (`$PY tools/batch.py <batch> a b`, next batch is B13 (`$PY tools/batch.py 13 116 125`); B12 = 107–115 is made (116 failed once: make it first); `batch.py` stops at a missing picture, so zip by hand when a number in the range failed) → upload the zip to `images`. Order: chapter 3 from 107, then chapters 4, 5, 6, 7, 8, 9, 10, 11 (to 459), then chapter 12's once its shot rows exist. 344 pictures are still to make (116–459). A picture that comes back upright is centre-cropped by `tools/sheet.py`; set its window by hand in `TOP` there (108 is cropped to the dog and the hands). For pictures of him after 1910 change the age in the prompt by hand (twenty-four in 1913–1914, twenty-five from August 1914; hair cut, chin shaved, full dark moustache); chapter 3 soldier pictures need `S_photo.jpg` (in the cast zip / batch zips via `tools/restore.sh`).
2. Render: a clip can be rendered as soon as its pictures exist (`node film/gen.mjs <clip>` prints what is missing; `bash tools/render.sh <clips>` as a background process, 6 to 8 min a clip). Upload each clip to Drive `clips_work`. A part is packaged by hand from the clips at hand with `bash tools/part.sh <name> <clips…>` (for example `bash tools/part.sh 03_ch03a N19 N20 N21 N22`; as a background process, wait for `PARTS-END`), so earlier clips need not be downloaded again: ch01a = N03–N06, ch01b = N07–N10. Chapter 2: N11–N15 are rendered; **`EP23_1080p_02_ch02a.mp4` = N11–N14 is packaged and uploaded** (291.53 s, 97.7 MB, two-pass x264 at 2477k, −12.6 LUFS). N16, N17 and N18 are rendered and uploaded (long holds: 078 in N16 about 30 s, 082 in N17 about 33 s, 088 in N18 about 25 s). **`EP23_1080p_02_ch02b.mp4` = N15–N18 is packaged and uploaded** (317.37 s, 97.8 MB, two-pass x264 at 2260k, −12.6 LUFS). Chapter 2 is complete as film. Chapter 3: N19–N22 rendered and uploaded (091–108; the dog picture 108 holds for about 25 s in N22); N23 (109–113) rendered and uploaded (the bread queue 111 holds about 25 s); **`EP23_1080p_03_ch03a.mp4` = N19–N22 is packaged and uploaded**; ch03b = N23–N26 when N24–N26 exist. N24 needs 116 and 117 (it has 114, 115).
3. **Chapter 5 (N35–N42, 1924–1929) is written, narrated (438.2 s = 7 min 18 s) and aligned** (27 Nov 2026). The "big lie" line in N40 now says that the book gives it as his enemies' method. Its 40 pictures (170–209) are not made. **Chapter 6 (N43–N50, 1929–1933) is written, narrated (383.7 s = 6 min 24 s) and aligned** (27 Nov 2026); its 35 pictures (210–244) are not made. **Chapter 7 (N51–N58, 1933–1934) is written, narrated (374.8 s = 6 min 15 s) and aligned** (27 Nov 2026); its 35 pictures (245–279) are not made. **Chapter 8 (N59–N66, 1934–1938) is written, narrated (456.3 s = 7 min 36 s) and aligned** (27 Nov 2026); its 45 pictures (280–324) are not made. **Chapter 9 (N67–N73, 1939–1941) is written, narrated (400.0 s = 6 min 40 s) and aligned** (27 Nov 2026); its 37 pictures (325–361) are not made. **Chapter 10 (N75–N81, 1941–1945) is written, narrated (513.0 s = 8 min 33 s) and aligned** (27 Nov 2026); its 48 pictures (362–409) are not made; they show places, objects, trains and documents, nothing graphic. **Chapter 11 is narrated and aligned (27 Nov).** **Chapter 12 (N91–N98) is drafted, not narrated**: read it once more against the fact sheet (check points 57–62, 64), remove the `EP23_DRAFT` gate in `script/script.mjs`, `node script/build.mjs`, narrate N91–N98 (8 speech calls; "February" stays in English in the spoken text of N92), zip, upload, align, then write shot rows from 460 (look X, ref H far and never heroic; nothing graphic), set `CARD_BG` N91, change the fact-sheet heading, upload script and fact sheet. After chapter 12: the end card (`film/end.mjs`).
4. `film/end.mjs` needs `assets/vo/END.mp3` (the end-card voice: `N08.mp3` in the EP21 narration zip `1vyGgGAtShHWNuSAYhzF7CZbT7KDVXKay`); only for the last part.
5. 030 again (upright and soft).

## How the film code works (EP23)

- `film/gen.mjs`: chapter card (2.3 s) only on a clip with a `title`; `CARD_BG` needs one entry per chapter's first clip (`N03: "braunau_inn_evening"`); `HOOK_FX` per hook clip; a picture held over 9.5 s is split into a wide shot and closer crops at pauses; fade to black at the end of the hook and of each chapter; `reuse: [shot names]` on a line shows pictures made for another clip.
- A `stat` card stays for its whole line: give each number its own line.
- `script/build.mjs` writes `script/clips.json`; `tools/chclips.py <k>` lists the clips of part k (0 = `N01 N02 TITLE`, 12 ends with `END`).
- `tools/render.sh <clips…>` or `ch <k>` (skips clips already in `out/renders/`); `tools/finish.sh part <k>` → `out/deliver/EP23_1080p_<NN>_<name>.mp4`, or `…<name>a.mp4`, `…b.mp4` when the chapter is over about 5 minutes (prints `PART …` per file, then `PARTS-END`; a piece over 99 MB is encoded two-pass to 95 MB); `VB=… bash tools/finish.sh 720 <name> <parts…>` for the 720p copy.
- One gain for the whole film: `tools/gain.txt` = +5.46 dB (narration measured −19.46 LUFS; target −14). Do not re-measure.
- `$PY tools/stills.py [clips] --<prefix>` → still sheets; `$PY tools/frames.py video.mp4 out.jpg t1 t2 …` → frames of a render.

## Drive

Folder `EP23_Hitler_Veedillathavan_Mudhal`: `10ZWqHEkZTMfl6jrelOYsmAXk6uWtCjYr` (parent `1WqhshH9XcvNUna4lzyS692eidgWQfeS1`). Pictures folder `images`: `1qxd24FYRXbd2K_OqfWvzpgXaDQQfQ67U`.

| File | Id |
|---|---|
| EP23_narration_N01-N10_voice02.zip (hook and chapter 1) | `1wzvDc2gEA8zSgXoDAsW-CyV326ThswgP` |
| images/EP23_B01_images_001-010.zip | `1CNvtwG5ktJ8ngQ6p7fvM1oV4k9TVBATp` |
| images/EP23_B02_images_011-020.zip | `1KH1lDddL-EK0idBP6aKcRnc-Od6HoABM` |
| EP23_1080p_00_hook_title.mp4 | `1XI_otP6j5p9-8UvGdTlPM0X8sPc4bYoO` |
| EP23_narration_N11-N18_voice02.zip (chapter 2) | `1jgakdUY2s3gpYmHdVZTQonNh3LvC8Bh_` |
| EP23_SCRIPT_TA_hook_ch1_ch2.md | `111vHFCU-mDFx9sHi_vCKM8AQcntYNfZa` |
| EP23_FACT_SHEET_hook_ch1_ch2.md | `16pMOQ7voGhbaWTeyrBpxvT-0HDvbdF0f` |
| images/EP23_R1_images_faces_004-008-010-012-017.zip (redo: unpacks over the batch zips) | `1pm022Ys_4QL4B4gO6Ix5-c9H1eU3-QKo` |
| images/EP23_cast.zip (reference pictures → `google_drive/ep23_pics/cast/`) | `15aQXIRA92aKuxwj1dmPtSdyWbj73ZFj8` |
| EP23_narration_N10-N11-N14_February_voice02.zip (replaces those three clips; unpack after the two narration zips) | `1bY7Ux0KJvlLCbxkn1DODiFJL-f3mEP6G` |
| EP23_1080p_00_hook_title_v2_film.mp4 | `1iSiADf9AbmB7-4wXWUknUMWXgRe9nfa6` |
| images/EP23_B03_images_021-029.zip | `1lF6TpKM5q_P4r5aOdjdcWxos-R7_TB1C` |
| images/EP23_R2_images_face_012.zip (redo) | `1_YNsPKniSzj9sBRSPejDQbYifFb99S6V` |
| images/EP23_cast_v2.zip (adds `Y18.jpg`, `A18.jpg`, the new `A.jpg`; use this one) | `1kgFxrmZX3wZ5Zucv8bJgxN7Z1zqQ2E6r` |
| EP23_1080p_00_hook_title_v3_film.mp4 | `1ZUQv08d_G3ENbjFJf5NDf0r69p7KD993` |
| images/EP23_B04_images_030-039_no034.zip | `1QBM6IY0kfZMrcMWSIU6GG5sOEyBcrizt` |
| EP23_narration_N19-N26_voice02.zip (chapter 3) | `1XU-2Qvk4UHZNPB_Sq9QdGDMB9r3cmYKy` |
| EP23_SCRIPT_TA_hook_ch1-ch3.md | `1ZzlHF389mA2r5pXXV3o9_78Do4R9CuHR` |
| EP23_FACT_SHEET_hook_ch1-ch3.md | `11z-vIXX8s6p0LvTtaf91FT2Fqi2vk0KQ` |
| images/EP23_B05_images_034_040-048.zip (also holds `cast_S_photo_reference_only.jpg` → `cast/S_photo.jpg`) | `1NsUWqquvkCX1v2PFQbKynhSBAFBSpC8H` |
| EP23_narration_N27-N34_voice02.zip (chapter 4) | `11UhsJK6cpSgeZ20IemjfSThESJqrlWpX` |
| EP23_SCRIPT_TA_hook_ch1-ch4.md (current) | `1UOmMgCQKqYqHy0Jvnlr6QbHVtTG-b1T4` |
| EP23_FACT_SHEET_hook_ch1-ch4.md (current) | `1mpdZqHN19WgZiYNoJazXpR8s5f3fsw7C` |
| folder `clips_work` (rendered clips, so a wipe does not cost the render time; not for viewing) | `1x1r_EPhLK4_Y0QA2ls3ACgVcps-S9Zop` |
| clips_work/N03.mp4 | `1YVK6GmdPNa_ybb3JBTIAsZnw3z-SINd2` |
| clips_work/N04.mp4 | `1t6GOn9uXxMKpcwTVq2MUQB4vY577K8V0` |
| clips_work/N05.mp4 | `1tDB0r3I3OpiXNsUWNbmvgJRKMkkFNcsq` |
| clips_work/N06.mp4 | `1E6NF4hQtlNWwQjMEaNp3XU5qAuvkVRlF` |
| clips_work/N07.mp4 | `1q-tjKlCStImZnN0bFUFaTFPuCL2kpnKV` |
| clips_work/N08.mp4 | `1_nVkJSB11lDOHgw-se2iEtWfWcUu-egQ` |
| clips_work/N09.mp4 | `1Y7wM8_3P7DYccZGkbAqOZkRzcWUEPBth` |
| clips_work/N10.mp4 | `11-_ovtOPJCjCJrGlqaQgHYtGQqXxXp7G` |
| clips_work/N11.mp4 | `1YJzKfTlGRegA4sZsje0cBRAh4PA5Kvco` |
| clips_work/N12.mp4 | `1M97nOFvqj7MLaGQ_ps2Fxl6EFdsGkBi1` |
| clips_work/N13.mp4 (**outdated**: old 067, pictures one sentence late) | `1fInytKjmc5Y7L9jcBdhJ1lh4ZFuoBlgM` |
| clips_work/N13_v2.mp4 (current N13; restore it as `out/renders/N13.mp4`) | `1lcGTzXMxVvy_zpNw7wwDTrkW8kaMw70C` |
| clips_work/N14.mp4 | `1VTxBucpAXSP4K65jjJ5ncDj5Y9c8zcyW` |
| clips_work/N15.mp4 | `1-EXnGlRJUWtkrxYabTgbVItNtmHSZmes` |
| clips_work/N16.mp4 | `1Priz3yzi6CvY4X4Sr3ArL2jN-yfyr0qb` |
| clips_work/N17.mp4 | `1WrExjLXt_i0bFtkyy8_EUlGn52Y-KTma` |
| clips_work/N18.mp4 | `11igLfUw1yExLpVptcFQrpMq3bB26YYVy` |
| clips_work/N19.mp4 | `1CBqMOqoJfA5sQuF_sKB9bEe0KragmHVy` |
| clips_work/N20.mp4 | `10fpUlUJx8ccbzfvcc9TTKxREMrSW19_G` |
| clips_work/N21.mp4 | `10hL74L55QcJudxaLStcEWvhwq-vgJqOX` |
| clips_work/N22.mp4 | `1fjh7INe8MX2bmpuz0lADitVjJgcztU2d` |
| clips_work/N23.mp4 | `1CB-v59mj0lUaYVJOhEACwXNX0jEnQEXR` |
| clips_work/N24.mp4 (58.9 s, frames checked) | `1NfzydEa5cHRDHFkFavtQBpvBo5bx-yXL` |
| clips_work/N25.mp4 (68.8 s, frames checked) | `1CtWmPgYNX_5tWDQgeAG6DmDD3tPRLKLe` |
| clips_work/N26.mp4 (73.4 s, frames checked) | `18Bg0v-wR8d25niOYfWWwGe_d4k9rm_6H` |
| clips_work/N27.mp4 (75.1 s, chapter 4 card, frames checked) | `1SlSDSuMWtjLQXPoheFXYsBul9bLh4Lff` |
| clips_work/N28.mp4 (66.8 s, frames checked) | `1NAkoQ1t5VNAukxnHlPpukNhePWUq1t6_` |
| clips_work/N29.mp4 (71.5 s, frames checked; the card picture 142 holds about 25 s at the end) | `1BY6tGEgUQmpWYnVTKgtSOLV35DaGZytV` |
| clips_work/N30.mp4 (76.1 s, frames checked; 143 holds about 25 s at the start) | `1KyButnofIDmx280NRl2on9L9h4jpxaZ2` |
| clips_work/N31.mp4 (69.4 s, frames checked) | `1w-_6gwq-iVWpqYYjVbfJ1H1-7_cag72W` |
| clips_work/N32.mp4 (72.4 s, frames checked) | `1KQf4P4KQQ31oP0sBpFk5F7f4E9F9WHGk` |
| clips_work/N33.mp4 (70.0 s, frames checked; the second number panel sits over the old man's face in 161) | `1ml6t1jElOiE87y61hzF4_Fzo8BEjxRVK` |
| clips_work/N34.mp4 (91.4 s, 14 pictures, "16 + 4" panel, frames checked) | `1xanooHs3CIp75EDPf4gHAdngAl9DrSuZ` |
| clips_work/N35.mp4 (60.6 s, chapter 5 card, frames checked) | `1iShwQtmmUjk-XrkgV_-ojC4XE9iwi4UV` |
| clips_work/N36.mp4 (66.2 s, "9,473" panel, frames checked) | `1V9dKh1C9WL9q2RARZDM5scRKRkM4vrAl` |
| clips_work/N37_v2.mp4 (current N37, 55.3 s; restore it as `out/renders/N37.mp4`; line 5 now reuses the prison-gate picture 183 for its first sentence, then 184) | `1vWdfEmNPuo7a4WU0s6-TwtoX9GlHFk5C` |
| clips_work/N37.mp4 (first cut, superseded: the "photo by the car" sentence ran over the sealed door 184) | `17HJ83SL-5CajsAMuA3kEgRnxpJdOrk0Z` |
| clips_work/N38.mp4 (54.1 s, "2 வருஷம்" panel, frames checked) | `1IaJv2lw5yTD4m5AWdOxHdD-yMejlF_Zv` |
| clips_work/N39.mp4 (57.4 s, frames checked) | `167kf7G_MEeHIPySuhm6PaYeUn1AQUdfr` |
| clips_work/N40.mp4 (53.9 s, "பெரிய பொய்" big word, frames checked; 199 holds about 20 s) | `1a-tW7RTTLmoxWXghQCWHmz-Pf4mp4vhs` |
| **EP23_1080p_05_ch04a.mp4** (N27–N30, 289.5 s, 97.7 MB, two-pass 2496k, −12.6 LUFS, peak −2.1 dBFS) | `1tYmLDCoAZqqcZR96cX2aeSxxTE9u5DN5` |
| **EP23_1080p_06_ch04b.mp4** (N31–N34, 303.2 s, 97.7 MB, two-pass 2374k, −12.6 LUFS, peak −2.1 dBFS) | `1l0TppTHtAD-d16AGdcCSTinxA1RY3Xoi` |
| **EP23_1080p_07_ch05a.mp4** (N35–N38 with N37 v2, 236.3 s, 97.7 MB, two-pass 3102k, −12.7 LUFS, peak −2.0 dBFS) | `1hu7CwOYjt4TAb8jbFlGPJdmd3Ib0GpYq` |
| **EP23_1080p_04_ch03b.mp4** (N23–N26, 270.0 s, 97.6 MB, two-pass 2690k, −12.7 LUFS, peak −2.0 dBFS) | `1_KwM-4wIJ6p-b7Ik2lL8npuAvomH5hXa` |
| clips_work/END.mp4 (end card, 17 s; goes after N98) | `15pE38DggQb_Qe1lWhyrc-Px3IFvcsAPe` |
| EP23_END.mp3 (end card voice; restore as `narration/END.mp3`, then `node film/end.mjs`) | `1_p33LqXaqK0mR9JVFEkpmuCQtr2jYy_z` |
| **EP23_1080p_03_ch03a.mp4** (N19–N22, 306.5 s, 97.7 MB, two-pass 2347k, −12.6 LUFS, peak −2.0 dBFS) | `1tIP3FT-R0ybGOx3rjPQjTXTg1OAR74YC` |
| EP23_1080p_02_ch02b.mp4 (N15–N18, 317.37 s, 97.8 MB, −12.6 LUFS) | `1nkvTo75fOzbmpJZu1wdZHd29ibiTitRf` |
| EP23_1080p_02_ch02a.mp4 (N11–N14) | `1Cdvz5LCzyoO1nP9TblYi3G2ncWvo8zmA` |
| images/EP23_B08_images_069-077_plus_067.zip | `1UpbZ4KYi-x-sn2gGfKMyzP49O1fom7fJ` |
| EP23_narration_N51-N58_voice02.zip (chapter 7) | `14lss1jJmII4ma_qe7H2UgUKEytyH38Q8` |
| EP23_narration_N59-N66_voice02.zip (chapter 8) | `1wVruNzHxDPLbHys2YmxYtxI6exNnxaux` |
| images/EP23_B09_images_079-087.zip | `1Drs7TniBruf1-L9pRZWTB4j3fwBAT_PE` |
| EP23_SCRIPT_TA_hook_ch1-ch8.md (superseded) | `1Gthcc-rKuTubAWodgCyrAQOrXfkn4o0S` |
| EP23_FACT_SHEET_hook_ch1-ch8.md (superseded) | `11IRDZiQgJAiiZoizatYDI75mtbTf2UsT` |
| EP23_narration_N67-N73_voice02.zip (chapter 9) | `1GDoTXdYq54xfgnpByd8jzYbWXswA01Lm` |
| images/EP23_B10_images_078_088-096.zip | `17ckVStq8sa8MyDG_0z7hGqBrA3Pt_H8A` |
| EP23_SCRIPT_TA_hook_ch1-ch9.md (superseded) | `1pQvEBcKpe1mfFfUh47KCNtr55Bi5Vzjj` |
| EP23_FACT_SHEET_hook_ch1-ch9.md (superseded) | `1ixmlxB4bbEhdFCrcnKGWdceetmfZSHZD` |
| EP23_narration_N75-N81_voice02.zip (chapter 10, outdated N81) | `1HRjWpndwFOLnjc4XZQ_0GhWv1O1eZ0o6` |
| EP23_narration_N75-N81_voice02_v2.zip (chapter 10, **current**) | `19jacLS2oOMGd03VzcA_dMLrQHg7WssRl` |
| images/EP23_B11_images_097-106.zip | `1hU-sL3Z4dhsgYQ3mwSmNk1WjzjzbYJaM` |
| images/EP23_B12_images_107-115.zip | `1Yx8MqgS6KflIHdhcNwTd_oY7gREA2QiJ` |
| images/EP23_B13_images_116-125.zip | `1mQMxW_SvtGc09mTr9dEaZK_wojIzXJbT` |
| images/EP23_B14_images_126-135.zip | `1NmpDeJbCg-7AHKmcVvkMLL4kErIMNhoR` |
| images/EP23_B15_images_136-145.zip | `1btEVIdMCuG8sNcIU7tFUQuXDVhjNVCjY` |
| images/EP23_B16_images_146-155.zip | `1yypvSLcaCaH4wAryIcq_GGwmwj4uGrWV` |
| images/EP23_B17_images_156-163.zip | `1qktnazaGnt0aGifMG5W-1YlEHo1mu9T2` |
| images/EP23_B18_images_165-165.zip | `18vWV-tOPD4_Hsw2VjD3XL62wbfHMxwfk` |
| images/EP23_B19_images_166-174.zip | `1CQHb_rUTzMOLpMImYdbQxLE8a93Fx8N9` |
| images/EP23_B20_images_175-183.zip | `10HbFG0vts-GXnRElD8sAANqqZVzzQN35` |
| images/EP23_B21_images_164-164.zip (164, third try, retouched) | `1DfSmAGwxIFXqozFVlCGGGC53R0GbA8Pf` |
| images/EP23_B22_images_184-193.zip | `1INHCvh7ILoiZ6sXER8FmnoaQEmj8hZ5H` |
| images/EP23_B23_images_194-203.zip | `1ji16Nbtwh8Qzx6l7FtO7mphaw_XQc9rp` |
| EP23_narration_N91-N98_voice02.zip (chapter 12) | `12LlOqm9X1avBw2l2uSyD7rg1GakAHTi5` |
| EP23_SCRIPT_TA_full_hook_ch1-ch12.md (**current**, whole script) | `1w7XuOOldd5xNXfvYW7By30zSqCxfztQo` |
| EP23_FACT_SHEET_full_hook_ch1-ch12.md (**current**, whole fact sheet) | `1u8NolbtgSom1fM0qRNdJA6_Tz0PZl9Ul` |
| EP23_narration_N83-N90_voice02.zip (chapter 11) | `1S8m_jOtBfDi7pm1UTPJ7G8IbaYo3xrxp` |
| EP23_SCRIPT_TA_hook_ch1-ch11.md (outdated) | `1m1dYtvHx9ujXYHPM2lzaHyYxv2TfCTa5` |
| EP23_FACT_SHEET_hook_ch1-ch11_ch12draft.md (outdated) | `1Rw-ZkJLNmlbAsacGfClAidJ7yQw4kCOO` |
| EP23_SCRIPT_TA_hook_ch1-ch10.md (outdated) | `1pyEt0UjNZqEF636kiXwPTuFPQtPV9856` |
| EP23_SCRIPT_TA_hook_ch1-ch10_v2.md (outdated) | `1GFjXqzFwm7be2zagO19bGDNOtAD8xJ3W` |
| EP23_FACT_SHEET_hook_ch1-ch10.md (outdated) | `1sxy6b_gkitytHyvcmmYKqKrsC7Tk5Dll` |
| EP23_FACT_SHEET_hook_ch1-ch10_ch11draft.md (outdated) | `1YrrgG7urZ33v9x00iibg11V4BleAWg8R` |
| images/EP23_B07_images_059-068.zip | `1eGOogpT4j9lKmpJFioFBVu_izbgyAi6N` |
| EP23_narration_N43-N50_voice02.zip (chapter 6) | `1perI5PRRJoAI9AKwg_HW9-FT9Pb65N6w` |
| EP23_SCRIPT_TA_hook_ch1-ch6.md (current) | `1KRvaRxb3thGt1veMxQmtznyJ5lc0XLmb` |
| EP23_FACT_SHEET_hook_ch1-ch6.md (current) | `1OV-SfH6ToL_2He8DW5VNQdQQtBcueVmi` |
| **EP23_1080p_01_ch01b.mp4** (N07–N10, 4 min 0 s = 239.7 s, 97.7 MB, −12.6 LUFS) | `1z30R5aOpeSCyGllOWqiqHAGOwSBAyQ21` |
| images/EP23_B06_images_049-058.zip | `1yzHhZaB2Q_ad8rc8O0JRXzNMz7tLhyjV` |
| EP23_narration_N35-N42_voice02.zip (chapter 5) | `1IkyG5VliTynQ1RwBl0qIP1K3Ye7Emtam` |
| EP23_SCRIPT_TA_hook_ch1-ch5.md (current) | `15VSeOL4o8PN7A4hAgWgSEHiIWDOW-kuC` |
| EP23_FACT_SHEET_hook_ch1-ch5.md (current) | `13R_wIMP_GQA5laTzFfksz2jlquC1WuW8` |
| **EP23_1080p_01_ch01a.mp4** (chapter 1, first half: N03–N06, 303.5 s, 97.6 MB, two-pass; −12.6 LUFS, peak −2.0 dBFS) | `13P9X8HMM6z-BWDEvn6dBGzWRmNv-RnPf` |
| EP23_OUTLINE.md | `1TVRmNj24nJn1oTHJUfdluQAr5voGH_bo` |
| EP23_SCRIPT_TA_hook_ch1.md | `1Yj9njt2sHz-c0ZYLgdfzRipFGrJMsOA_` |

## Picture checks

- B11 (097–106), 27 Nov: all kept (first batch with the soldier reference `S_photo.jpg`, which comes from the B05 zip). 102 gives him a small moustache instead of the wide one of the war years; 106 crops the top of his head; 103 shows a researcher's face (fine, modern archive).
- B23 (194–203), 28 Nov: all kept, all wide (1376×768). Checked close: 194 handwriting and 196 print cannot be read; 197 posters are blank red sheets. Weak: 197 the tram looks later than the 1920s and carries a small route number; 200 he stands facing the camera rather than looking at the hall; 203 the small stack is hard to pick out.
- B22 (184–193), 28 Nov: all kept, all wide (1376×768). Checked close: 186 cinema canopy is blank, 190 map has no lettering, 192 men are plain (no badges). Weak: 192 the eight men have nearly the same face; 193 the small man looks ahead rather than sideways at him. 187 was made without the reference photo (he is a tiny far figure).
- 28 Nov state: renders N03–N40 and END are done and uploaded; parts through `07_ch05a` are uploaded. Next: pictures 204–213 (N41 = 201–205, N42 = 206–209, N43 from 210), renders N41 and N42, part `08_ch05b` = N39–N42.
- B20 (175–183) and B21 (164), 28 Nov (after a full wipe): all kept, all wide. **164, third try: arms down, dust falling from the ceiling.** One helmeted man at the door had a plain red armband and a small chest mark: both painted out by hand in the raw file before zipping (the file in B21 is the retouched one). 178: the map has no lettering. 179: the books in the window are blank.
- B19 (166–174), 27 Nov (after a third wipe): all kept, all wide. 172 shows him with one fist on his chest in the courtroom (as asked). **164 was made on the second try but rejected by me**: it came out 1167×912 with his open hand raised straight up (reads as a salute) and a red band on a listener's arm; kept only as `google_drive/ep23_pics/rejected/164_salute.jpg`, not uploaded. The row in `shots.txt` now asks for both arms down, just after the shot. N34 still waits for 164.
- `film/gen.mjs`: a line with `reuse` and pictures of its own now shows the reused pictures first and then its own (N34 line 4: 094, then 167; N50 line 2 will show 243 after the two reused ones). N02 keeps the old behaviour.
- B17 (156–163) and B18 (165), 27 Nov (after a second wipe): all kept, all wide (163 and 165 are 1536×688, cropped at the sides). **164 (the man on a chair with a pistol in the beer hall) was declined by the content filter and is not made**: try again without the weapon in the foreground (seen from far across the hall, one arm up, plaster dust falling from the ceiling, armed men at the doors), or reuse 165. N34 waits for 164 and 166–169.
- B16 (146–155), 27 Nov (after a wipe): all kept, all wide (152 is 1536×688, cropped at the sides). In 146 some listeners hold up mugs and fists; in 151 the back of his head in front of the mirror is lighter than the reflection.
- B15 (136–145), 27 Nov: all kept, all wide (143 is 1536×688, cropped at the sides). First pictures with the 1919–1923 look (138, 140, 144: dark suit, small moustache, from `H_photo.jpg` "about fifteen years younger"). In 136 and 143 (still a soldier in 1919) the moustache is already small; 137 shows handwriting on the page (blurred).
- Continuity in N26: 123 shows a very wide moustache, 126 a narrow one, in the same clip; remake 126 when a call is free, then render N26 and part ch03b again. The captain in 132 (N27) looks like a well-known film actor; remake if wanted.
- B14 (126–135), 27 Nov: all kept, all wide (128 is 1536×688, cropped at the sides). 126 and 131 give him a narrow moustache instead of the wide one of 1918–1919; in 127 the light on the lips came out orange; 132 has no cigarette; 130 shows him with a beard shadow.
- B13 (116–125), 27 Nov: all kept; all came back wide (the referenced prompts now begin "Wide landscape frame, wider than tall."). 123 is 1536×688 and is cropped at the sides. 116 gives him a narrow moustache; 123 a wide one and a face older than twenty-nine; 120 shows the bandaged men with moustaches but none is clearly him; 125 shows officers at a telephone, not him (as asked).
- B12 (107–115), 27 Nov: all kept; 116 failed once and is not made. 108 and 114 came back upright (880×1192): 108 is cropped by hand to the dog, the mess tin and the hands (his face, with a small moustache, is left out); 114 is centre-cropped (fingers on the pocket). 113 gives him a curled moustache and a fuller face. 115: the adjutant's uniform reads khaki-brown rather than field-grey.
- B10 (078, 088–096), 27 Nov: all kept. 089 shows a gateway with a sculpture group on top (reads as Berlin rather than Munich's Königsplatz gate); 091 gives him round glasses in the door gap (small, dark); 093 shows only the backs of the crowd and a car far off.
- B09 (079–087), 27 Nov: all kept. 078 failed in generation and is still to make (N16 waits for it). In 080 the crowd and the platform are hard to see.
- B08 (069–077 and 067 again), 27 Nov: all kept. 067 now shows him in a thin jacket without an overcoat (he is first in the queue).
- B07 (059–068), 27 Nov: all kept. 059 and 061 read mid-twenties with a clear moustache (the youth is nineteen there); in 067 he is first in the queue, not third.
- B06 (049–058), 27 Nov: all kept. 055 and 057 show an upright piano where the script says grand piano (Kubizek's was a grand); 057 reads older than nineteen. Redo 057 if a call is free.

| Batch | Pictures | Result |
|---|---|---|
| B05 | 034, 040–048 (N05, N07, N08, N09) | all usable, 16:9, no lettering. 041: he stands in the middle of the Ring with the opera house behind, looking at the camera (the row asked for him small in the street): kept. 043: his hat near the top (`SHIFT` 60). 044: the youth in the exam hall reads early twenties rather than eighteen. 042, 047: the doctor is the same bearded actor in both (`SHIFT` 24, 30). |
| B04 | 030–039 without 034 | usable. 030 upright format, soft (redo). 035: blurred sign shapes over two shops, not readable. 037, 039: hats near the top (`SHIFT` 64 and 30). The youth matches picture 008. |
| B03 | 021–029 (N03, N04) | all usable. 023: the mother looks nearer forty than twenty-eight; the father stands high in the frame (`SHIFT` 50). 028: the "meadow" is a dry field at the edge of a village. |
| R2 | 012 | same young face as 004; good |
| B02 | 011–020 (N01 rows 11–12, N02) | all usable |
| B01 | 001–010 (N01) | all usable. Notes in `shots/CAST.md`: 008 figure walks up the steps, 009 extra small stones, 010 hat and a blank dark cloth |

## After a full wipe

Only the pushed branch survives. `out/`, `narration/*.mp3`, `/tmp` tools and `google_drive/` are gone.

1. `git fetch -q origin arena/d486087a-hyperframes && git reset -q --hard FETCH_HEAD`
2. `bash projects/nk-ep23-hitler/tools/setup.sh` as a background process (about 2.5 min), then `. /tmp/hfenv.sh` in every shell.
3. Download from Drive into `google_drive/`: every narration zip and every `EP23_B*` / `EP23_R*` picture zip in the tables above.
4. `unzip -o -q ../../google_drive/EP23_narration_*.zip -d narration/` for each narration zip; `bash tools/restore.sh` (unpacks the picture zips into `google_drive/ep23_pics/raw/NNN.jpg`, relinks `out/raw`, `shared/vo`, `shared/plates`, rebuilds `out/img`).
5. `node script/build.mjs && $PY script/align.py && python3 shots/expand.py`.
6. Rendered clips: download every `N??.mp4` of the Drive folder `clips_work` and `mv ../../google_drive/N??.mp4 out/renders/` (`tools/render.sh` skips clips that are there). Regenerate the film folders first: `node film/gen.mjs N03 N04 …`.

## Chapter 12 research notes (search of 27 Nov 2026; now in the fact sheet, rows 507–558)

Pages: en.wikipedia.org (Last will and testament of Adolf Hitler), military-history.fandom.com (Death of Adolf Hitler), berlin-escape.com, weesp.dk, historyrise.com.

- 16 Jan 1945 he moved into the bunker under the Chancellery garden and never left Berlin again. 19 Mar: the "Nero" order to destroy bridges, railways, factories and food stores; Speer worked quietly against it.
- 16 Apr: the Soviet attack across the Oder. 20 Apr, his 56th birthday: the first Soviet shells on Berlin; Göring, Himmler, Goebbels and Ribbentrop came, most then left; he decorated boys of the Hitler Youth in the garden (the sources differ on the date: 20 March, 20 or 22 April; say "in those days").
- 22 Apr, afternoon conference: told that Steiner's attack had not happened, he broke down, said for the first time that the war was lost, blamed the generals, and said he would stay and shoot himself. Goebbels brought his wife and six children into the bunker.
- 25–27 Apr: Berlin encircled and cut off. 28 Apr: a BBC/Reuters report of Himmler's offer to surrender to the western Allies; he ordered his arrest. (Göring's telegram of 23 Apr was not in the results: from memory.)
- Night of 28–29 Apr: married Eva Braun in the map room; dictated the private will and the political testament to Traudl Junge, signed 04:00 on 29 Apr. The testament denies that he wanted war in 1939, blames the Jews, names Dönitz president and Goebbels chancellor. 29 Apr: news of Mussolini's death.
- 30 Apr about 15:30: a shot; he had shot himself, she had taken cyanide; fewer than 40 hours married. The bodies were carried up, doused with about 200 litres of petrol and burned in the garden. Soviet troops were a few hundred metres away.
- 1 May: the Goebbels couple had their six children killed and then killed themselves. 2 May: Berlin surrendered (Weidling). 8 May: the unconditional surrender took effect. "A thousand years" lasted twelve.
