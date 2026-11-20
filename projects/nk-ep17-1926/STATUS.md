# EP16 Sigiriya: status

Tamil title: சிகிரியா / பாறை மேல ஒரு அரண்மனை?  Target about 8 minutes (asked for by the user). Same recipe as EP15 (`projects/nk-ep15-genghis/STATUS.md` has the full pipeline, the lessons and the wipe recovery steps).

## Done (19 Nov 2026)
- Research: nine web searches, extracts only. `FACT_SHEET.md` lists every fact with **check** marks.
- Script v1: `script/script.mjs` → `SCRIPT_TA.md`. 70 lines, 6,927 characters, hook + six chapters.
- Narration: `voice-02`, `narration/N01`–`N07.mp3`, 462.4 s. `N08.mp3` (channel end card, 13.1 s) reused from EP15. Expected film length about 8 min 30 s (EP15 had 49 s without narration).
- Timings: `narration/align.json`. Two lines of N04 (q01, q02) were set by hand from the pause list, because "கீழ மேகம். கையில பூ." came out as one breath; not listened to.
- Shot list: `shots/shots.txt` → `SHOTLIST.md`, 144 pictures (`shots/counts.json`). Looks and reference texts are in `shots/expand.py`.
- Reference faces: `kashyapa`, `dhatusena`, `moggallana`, `migara` (`shots/CAST.md`), all invented.
- All 144 pictures made and checked (batches B01–B15); thirteen made again (R1: 098, 133; R2: 019, 032, 086, 096, 099, 105, 140, 142, 143; R3: 038). The redo list is empty.
- Film settings for EP16: title plates 001 → 020 → 122 in `film/title.mjs`; `HOOK_FX` for the eleven hook lines and the subscribe pop-up on N02 line 2 (the Culavamsa line) in `film/gen.mjs`.
- **Film rendered, levelled and uploaded in one turn.** Render times on 2 CPUs: TITLE 79 s, N01 355, END 86, N02 467, N03 460, N04 457, N05 341, N06 375, N07 435 (about 6 s of work per film second, 51 minutes in all). `tools/finish.sh parts` (measured -16.57 LUFS, gain +2.57 dB), `VB=1350k tools/finish.sh 720` → 511.13 s (8 min 31 s), 93.1 MB, measured -14.3 LUFS, peak -1.4 dBTP. Frames checked: title, hook, chapter card, subscribe pop-up, one frame in each chapter, end card. Not listened to.

## Next
- Nothing open in the making. Before publishing: a native read-through of the script and a listen to the narration (scratch voice `voice-02`), and the **check** items in `FACT_SHEET.md`, first of all the closing Budal quotation.
- Known small flaws kept: 008 crown low; 009 boats in an even row; 036 embankment like a stone wall; 048 no carved marks; 053 fountain a large stone ring; 064 part of the parasol bearer's face; 078 a modern-looking rail; 092 the king looks back over the howdah; 095 dust close to smoke; 119 garden plan tidier than the real site; 143 the crown lies round the manuscript.

## Chapters
| Clip | Chapter | Lines | Seconds | Pictures |
|---|---|---|---|---|
| N01 | hook | 11 | 58.1 | 001–020 |
| N02 | 01 அப்பாவும் மகனும் | 10 | 74.4 | 021–043 |
| N03 | 02 பாறை மேல ஒரு நகரம் | 10 | 73.8 | 044–066 |
| N04 | 03 மேகத்துல மிதக்கற பெண்கள் | 9 | 70.3 | 067–086 |
| N05 | 04 யானை திரும்பின நாள் | 10 | 56.2 | 087–104 |
| N06 | 05 ராவணன் கோட்டையா? | 10 | 60.1 | 105–122 |
| N07 | 06 மறுபடி வெளிச்சத்துக்கு | 10 | 69.4 | 123–144 |

## Picture rules
- No blood, no bodies, nobody shown being hurt. The old king's death is a newly bricked wall; the battle is dust and far figures; Kashyapa's death is a dagger and a crown in the grass (never the word for it in a prompt).
- The painted women are drawn clothed in a blouse (the originals are not); no surviving painting is copied.
- Monks from behind; no Buddha image.
- Legend pictures (look N) only under lines tagged belief or claim.
- No readable writing; scratched verses and manuscripts out of focus.
- Scholars, officers and present-day people from behind or as hands only.

## Open points
- Scratch voice; no native Tamil read-through.
- All **check** items in `FACT_SHEET.md` are unverified; the closing quotation (the visitor Budal on the mirror wall) is given from memory of the usual translation and should be confirmed first.
- Dates 477–495 follow UNESCO; other chronologies differ by a few years.
- The film runs about 8 min 30 s, a little over the 8 minutes asked for.
- Dress of the 5th century court (bare chest, waist cloth, topknot) is a guess.

## Drive
| What | Id |
|---|---|
| Folder `EP16_Sigiriya` (under root `1WqhshH9XcvNUna4lzyS692eidgWQfeS1`) | `1aPOds5hqKciAaDOMqv4ecjQyo5gbR6q0` |
| Folder `EP16_Sigiriya/images` | `1F3KnwKIvXf6viLrf4DiG_e1Yz1etxrm0` |
| `EP16_Sigiriya_SCRIPT_TA_v1.md` | `1Rkp6gRiDfDt-vn7fMz-ZgZcWG_rBTHYi` |
| `EP16_Sigiriya_FACT_SHEET.md` | `1rPoFWfHH30teIQTYK5PMO4F70frANr68` |
| `EP16_Sigiriya_SHOTLIST.md` | `1qnSlIDSY8muRTxoVMIAfQNz_z-sGmbsp` |
| `EP16_narration_scratch_voice02.zip` (N01–N08) | `1-Z9aNx1XM7sLF9JR2GkNik30lnsbyvUP` |
| `images/EP16_cast.zip` | `1Z1KEUzJkrsxl1sRgS_C2aYa_zcl1DQ2k` |

### Film (folder `EP16_Sigiriya`)
| File | Drive id | Size, length |
|---|---|---|
| `EP16_Sigiriya_full_720p.mp4` | `1X8eWBMYwn_HR828ZPLxG_ne-cT4fboIV` | 93.1 MB, 511.1 s |
| `EP16_1080p_01_hook_title.mp4` | `1rMbuYBWp1c81N0nJb19AF3ZVjMPw0oEx` | 84.1 MB, 71.1 s |
| `EP16_1080p_02_ch1.mp4` | `1VvrJJGW1InOYfo3q4Tjn3u5k748RopJ-` | 63.8 MB, 77.6 s |
| `EP16_1080p_03_ch2.mp4` | `1A0r2cvUEUQc9B7m0LPDC7Zz9hn6nbftf` | 95.7 MB, 77.0 s |
| `EP16_1080p_04_ch3.mp4` | `1z-cYLPYcEDFF81b19wqKJKElC8T53-pm` | 88.9 MB, 73.5 s |
| `EP16_1080p_05_ch4.mp4` | `1fgmwRDgnFjvQEf-ygxRM7d2oKGEqhda1` | 65.6 MB, 59.3 s |
| `EP16_1080p_06_ch5.mp4` | `1pOg9YVQVZrmu-C6sxb_wEDaCnNSA3A2I` | 62.8 MB, 63.3 s |
| `EP16_1080p_07_ch6_endcard.mp4` | `1c6zCT3XLEgl56DZW5dtpAx3-Sitf9trA` | 93.3 MB, 89.6 s |

The seven 1080p parts join without re-encoding: `ffmpeg -f concat -safe 0 -i list.txt -c copy EP16_1080p_full.mp4`.

## Picture batches
| Batch | Pictures | Zip id | Sheet id | Notes |
|---|---|---|---|---|
| B01 | 001–006 | `1ZfqAutzFryj4L1437ymnfWTBU4LtqwkQ` | `1LNWq9njN2QxDZe6NzPm4edervIlar472` | all good. 005: the king stands at the right edge of the frame. |
| B02 | 007–016 | `1J46Logvqf5D9yyxdvY_tKx5jNix0IfwZ` | `1IpaSShNcaH4pQXn2iTD3TKQqVLNiS-QI` | all usable. 008: the crown came out lower than in the reference. 009: the boats stand in a very even row. 012, 013: the paintings were asked for as "a photograph of an ancient wall painting" with their own tail (no "no drawn outlines"), which worked; keep that wording for all look P pictures. |
| B03 | 017–026 | `1-13DqjuVaPym-Kfy-SWm34y__LtOshPx` | `1atzfV1da_91u7sCz2tObjCuotOk9Oe8l` | all usable. 019: the sleeve looks like a rolled shirt cuff and the scratches are sharp, though not real letters (on the redo list as optional). 022 came with black bars left and right, trimmed by `sheet.py`. 023: both princes hold their reference faces with the ages stated. |
| B04 | 027–036 | `1tJqXowUexE55E71a7iyoNejquE663KEl` | `1jbCfJQeuPl7PphFiKhzk5MrYfaqxG8hl` | all usable. 032: the crown is a low diadem, not the tall crown of 034 (on the redo list as optional). 036: the embankment looks like a stone wall and the reservoir a little like a river. 035 came with a black bar on the left, trimmed by `sheet.py`. 031 (night, many figures) stayed photographic with the "film still shot on location at night" tail. |
| B05 | 037–046 | `192Jq1X0bztl0Z0WOsKjkeEz8P2tbuiFd` | `1COL8Wfgx84KCS3TbbzkiBzjO8Qua6-95` | 038: the old man's wrists are in dark knitted sleeves like a jumper (on the redo list; for hands of that age say "bare arms, no sleeves, no cloth on the arms"). 045: the king looks down on the rock from above, not up at it. 040 came with a black bar on top, trimmed by `sheet.py`. The rest good. |
| B06 | 047–056 | `1VPR3rB_KIfztgkjCghNB_JbW-fFDupw_` | `1SND3admR_NGSxe9m6ktyOQ3MeWYhaiUW` | all good. 048 shows the drip ledge and lichen but no carved marks. 053: the fountain is a large round stone ring, not the small pierced slab of the real site. A workspace wipe before this batch was repaired (reset to the pushed branch, `setup.sh`, narration zip downloaded again, `restore.sh`); the pictures in `google_drive/ep16_pics` had survived. |
| B07 | 057–066 | `1VACR7-hp7vf1BUJILW0BCLTulfVfClH7` | `1vauxL7x6RFs4KomxmW0SBcEYq5ci5Unh` | all good; the tall crown held in 062, 063 and 064 (the wording "tall tapering gold crown set with red stones" works better than "tall gold crown"). 064: part of the parasol bearer's face shows behind the king. |
| B08 | 067–076 | `1Aa5hcNQJE-QVX42HNC8sX2KVSVhEkhvD` | `1Z6g5JJQf6-oGn1_Xa2p4IBS0P6ii7Zwz` | all good; every painted woman came out clothed (069, 070, 073 and 074 checked at full size or on the sheet). 074 shows the sky women at full length lying on the clouds, not from the waist up. 072: the painted band on the cliff is smaller than "right across the cliff". |
| B09 | 077–086 | `1O6KE9MUMPKTuelcE0bpSXEFb9ZacWiM3` | `1458KDe4GWhkPyK6Qf0L9PI-JmBPcGave` | 086: the painting behind the conservator looks like a European church fresco of a veiled woman (on the redo list; in pictures with a person, the painting needs the full Sigiriya wording). 078: a modern-looking rail on the walkway. 082: the notes are scribble, not readable. 079: bare forearm, as asked. The rest good. |
| B10 | 087–096 | `1ELAvY1_Pm9WOM_8TOwnQS0jjM1yenEer` | `1Wppno_235XYCIXwQOsRS94EjxZQhMSJn` | references: 087, 092, 096 `kashyapa` (aged, grey beard; crown held), 088, 089 `moggallana` (aged, bearded). 096: a second riderless elephant behind the king, howdah reads like a chair (optional redo). 092: the king looks back over the howdah toward his army. 095: the dust clouds are heavy, close to smoke. No fighting in any picture. |
| B11 | 097–106 | `11X2vvw9AJzpoJmCi-5uRbWBE9H1_VCbs` | `1bdKs0OM5RoMbwp-FOl1_nuZkkbVlgmp7` | reference: 098 `moggallana`. 098: no crown on the new king (redo list, needed). 099: modern iron rail before the lion stair, one paw only (optional redo). 105: the legend palace has domes and spires like a fairy-tale castle, not a South Asian one. 097 shows the sheathed dagger and the fallen crown only. Monks from behind in 099, 100, 103; no Buddha image. The rest good. |
| B12 | 107–116 | `1LJ6OkIY4rmZjnTfyY18FzE1sGBhRgyDs` | `1Iy7y3ycC7zH-wzdcPaM0Ogrf9lixCraN` | all good. 107, 108: the legend pictures hold a South Asian look with the wording "ancient South Asian style, tiered pavilion roofs … no European castle towers and no pointed spires" (use it if 105 is redone). 109: bare forearms, as asked. 113: a little of the woman's cheek shows. Monks from behind in 115, 116; no Buddha image. |
| B13 | 117–126 | `1z_t8dRurSfJDbeaYKoBKVAhj2EvMUsnA` | `1kvOqv5fd5_Rwpfaaw2OgRTvdCbk3nrcw` | reference: 121 `kashyapa` (crown held, face in profile). All good. 121: both lion paws with the stair, plastered white (a better view than 099). 124: the handwriting is scribble, not readable. 119: the garden plan is tidier than the real site. Monks from behind in 120. |
| B14 | 127–136 | `1PyzQhzLyauWn2yQQyD20TZh9k3hZhvnl` | `17ap-ce7SKRvu3fvcUMvdp3UExwbQ-li8` | 133: the wall beside the traveller is covered with bold white chalk-like scrawls in sharp focus (redo list, needed; write "smooth wall, almost bare, only a few faint hairline scratches"). 134: one short line apart from the crowd, as asked, unreadable. 129: the two paws are seen from between brick walls, grooves in the rock above. 132, 136: rails kept on purpose (present day). The rest good. |
| B15 | 137–144 | `1Mo4w_ZLcNK9qhvmLW24-wwc5tf8yR5xW` | `18wkvGM5TP6rG5w2OeD11QbTLA8xv7vBD` | references: 137, 142 `kashyapa`. To redo: 140 (northern conifer forest behind the blank stone), 142 (wide low diadem, not the tall crown; weak light and shadow split), 143 (European spiked crown, spouted lamp). Good: 137, 138, 139, 141 (blank face, bare forearm), 144. In a close portrait or a still life the crown wording alone did not hold: add "like a tall cone, not a ring of points". |
| R1 | redo: 098, 133 | `1CBYhUU83EAkcCeN_ybulPdSUQ4FUjZxn` (`EP16_R1_images_098-133.zip`) | `1OxaOd6U87H6yH5LodG9DGn9CTecYxzJy` (`EP16_R1_sheet.jpg`) | both made again and taken: 098 Moggallana now wears a tall gold crown; 133 the wall is smooth and glossy with only faint scratches. They replace the B11 and B14 ones (`restore.sh` unpacks `EP16_R*` zips after the batch zips). First versions kept locally in `google_drive/ep16_pics/old/`. |
| R2 | redo: 019, 032, 086, 096, 099, 105, 140, 142, 143 | `1d_MGvdsh0hYzkk2Q6_4hEaeerznGZs-L` (`EP16_R2_images_019-143.zip`) | `1ScUHWgFiUdf7zgcHNy6Br_qWoJZGbAUj` (`EP16_R2_sheet.jpg`) | all nine made again and taken: 019 bare wrist with a thread, faint scratches; 032 and 142 tall cone crown (142 with the light and shadow split); 086 painting in the Sigiriya manner; 096 one elephant, the king alone; 099 both paws, no rail in front; 105 palace in South Indian temple style; 140 dry-zone trees, palmyra palms and the rock behind; 143 period crown and open dish lamp (the crown lies round the manuscript). **038 failed** ("Image generation failed", not a block) and still shows the knitted sleeves: make it first in the next turn. Crown wording that held in close views: "shaped like a tall cone rising high above his forehead, not a low band and not a ring of points". First versions kept locally in `google_drive/ep16_pics/old/`. |
| R3 | redo: 038 | `1ZtlZP79qTfAMG0cSr5qp_DcqBMh48XjC` (`EP16_R3_images_038-038.zip`) | none | 038 made again and taken: bare wet forearms, a plain gold ring, the lake behind. The redo list is empty. |

## After a full wipe of the workspace
As in EP15: `git fetch -q origin arena/d486087a-hyperframes && git reset -q --hard FETCH_HEAD`, `bash tools/setup.sh`, download the Drive zips above into `<repo>/google_drive/`, `bash tools/restore.sh`, unzip the narration zip into `narration/`, recreate the links `shared/vo` → `../narration` and `shared/plates` → `../out/img`.
