# EP11 status (updated 16 Nov 2026)

Done: script v1 (10 clips, 183 lines), scratch narration N01–N10 (698 s) + N11 end card (cut from the EP10 end card audio),
alignment (narration/align.json), shot list (327 pictures, SHOTLIST.md / shots/prompts.json), fact sheet,
film generator (film/gen.mjs), preview render of the first 23 s.

Pictures made: 001–030 (hook complete; N01 rendered to out/renders/N01.mp4, 69.6 s).
After tools/sheet.py always run tools/crops.py (shots/crops.json keeps faces and wrong scripts out of frame) (in out/raw and out/img; copies on Drive in EP11_Aditya_Karikalan/images).
Image generation is capped at 10 per message, speech at 10 clips per message.

Rebuild after a wipe:
  bash tools/setup.sh && . /tmp/hfenv.sh
  mkdir -p out/img shared/vo && cp narration/N*.mp3 shared/vo/ && ln -sfn ../out/img shared/plates
  (download the images zips from Drive into out/raw, then: $PY tools/sheet.py 1 10)
  node film/gen.mjs N01 --to 5 && cd film/N01 && hf lint && hf render --quality looks --output ../../out/renders/N01.mp4

End card: built (film/end.mjs → film/END, rendered to out/renders/END.mp4).
Each message: python tools/next.py → 10 prompts; generate into out/raw/NNN.jpg; $PY tools/sheet.py a b; $PY tools/pack.py a b; upload zip.
Render a clip when its pictures are complete (N01 = 001–030).
Still to build: title sequence (after the hook), subscribe pop-up in chapter 1, join + levelling to -14 LUFS, 720p copy.
N11 sentence starts (s): 0.25, 3.14, 6.19, 9.77, 11.51; ends 12.72.

## 17 Nov: user direction
- Make all pictures first, batch by batch, saved to Drive like EP10 (folder `images` id 1DTqKaOUnmmb4NGgEzj--byUxq1GCFLaD: EP11_Bxx_images_NNN-NNN.zip + EP11_Bxx_sheet.jpg); build the full video after.
- Faces allowed for kings and princes; invent consistent characters. Cast in shots/CAST.md, references in out/cast (Drive images/EP11_cast.zip id 1LpNYhX_QnFiYtMG__1uL8dfpltiwckK3). Overrides in shots/v2.txt (number|refs|subject).
- Done: cast (7), 001-030 (003, 004, 019 remade with faces). Next: 031 onward; v2 overrides written for 032-038.
- Per message: python3 tools/next.py; generate (pass out/cast/<key>.jpg for refs); $PY tools/sheet.py a b; $PY tools/crops.py; $PY tools/pack.py a b; upload zip + sheet to the images folder.
- The hook render (out/renders/N01.mp4) predates the new 003/004/019; re-render when the full video is built.

## 18 Nov
- User: not every picture needs faces; keep the series style, use faces where they help, and show kingdoms, ministers and crowds where the script allows.
- Done: 031-040 (B04). v2 overrides written up to 058. tools/next.py now prints the cast refs in brackets.
- Next: 041 onward.

## 19 Nov
- Done: 041-050 (B05), on Drive. 048 is wrong for the period (see shots/redo.txt); remakes are collected there and done in one pass after the last batch.
- Next: 051 onward.

## 20 Nov
- Done: 051-060 (B06), on Drive. v2 overrides written for chapter 2 (N03) up to 096.
- Next: 061 onward.

## 21 Nov
- Done: 061-070 (B07) except 067 (generation failed; a failed call still counts toward the 10 per message). 061 shows the readable Tamil consonant chart. Both are in shots/redo.txt with 048; tools/next.py skips numbers held there, tools/pack.py skips missing files.
- Lesson for script shots: ask for eroded, shallow, half-hidden letters at a raking angle; clean macro lettering comes out as readable modern Tamil.
- Next: 071 onward. After the last batch: redo pass (048, 061, 067 so far), then repack and replace those batch zips on Drive.

## 22 Nov
- Done: 071-080 (B08), on Drive. 071 film copy cropped (ink-bottle brand label) via shots/crops.json (values are fractions of the source). 074 (Latin-looking letters on the seal rim) added to shots/redo.txt.
- Redo pass so far: 048, 061, 067, 074. Next: 081 onward.

## 23 Nov
- Done: 081-090 (B09), on Drive. 088 changed to Aditya and Vira Pandya on clashing elephants (v2). Redo pass unchanged: 048, 061, 067, 074. Next: 091 onward.

## 24 Nov
- out/ and /tmp vanished between messages. Pictures now live in pics/raw and pics/cast (saved between sessions, not in git); out/raw and out/cast are symlinks. `bash tools/restore.sh` relinks and rebuilds out/img and the sheets (and unpacks any EP11 zips found in <repo>/google_drive/).
- Done: 091-100 (B10), on Drive. 095 (modern tunics) added to shots/redo.txt. Redo pass: 048, 061, 067, 074, 095. v2 overrides written for chapter 3 (N04) up to 124.
- Lesson: "hands only" shots drift to modern clothes; always say bare arms, bare chest, armlets, Indian straight sword with a disc pommel.
- Next: 101 onward.

### Drive ids, images folder 1DTqKaOUnmmb4NGgEzj--byUxq1GCFLaD
cast 1LpNYhX_QnFiYtMG__1uL8dfpltiwckK3 | B01 1JLVnWq0zQ3j6RXWUn4_ImN8SOkhl6fu- | B02 1wmpQx4LcdK0iMyntNbR6lG_5MqgvzbAP | B03 1U4OkSy14ufWEQ-0vZEFLiNtWrtXsaT2m | B04 1UYjc_EtIo81uImQRvOBhl6ZBQMM2QFFl | B05 1TcHvLyPLVh0H7sB3T8wYounPFx9P5Bmc | B06 1Ofrd5WM5eNktSF-fp8HM4Wvj6mRX-TlW | B07 1LnW6rAtkH4G9IvhVRMEZBfQe9eweYd5U | B08 1al_My7dfHgHw2LIE3d6_6aL3NPP-iSFi | B09 1ajO4n26N42OMfoYkN7YDp39k9jBU_cfa

## 25 Nov
- Done: 101-109 (B11), on Drive; 110 blocked by content moderation (counts toward the 10) and held. Redo pass: 048, 061, 067, 074, 095, 110. B10 zip id 1DE5ji8Tw_4oqHF2gNImmtvhDLF7eJZ4B.
- Narration mp3s and shared/vo are gone locally; before the film build download EP11 narration zip 1ySpKl5S2s3zTWNM4fyKnWZjaxCSgAOhu and N11 1GKCHE4FoUZxruNrU9Dg90FsHo9eCegqO.
- Next: 111 onward.

## 26 Nov
- Found the rule: files ignored by git (out/, pics/, *.zip, *.mp3) are NOT kept between messages; untracked files that are not ignored are kept; the local git history is rebuilt on the base commit each time (fix: `git fetch origin <branch> && git reset --soft origin/<branch> && git reset`, then commit as usual).
- Pictures now live in <repo>/google_drive/ep11_pics/raw/NNN.jpg and .../cast/<key>.jpg (outside the project .gitignore, never added to git). Generate straight into that folder. `bash tools/restore.sh` relinks out/raw and out/cast and rebuilds out/img and sheets.
- Done: 111-120 (B12), on Drive. 117 (English masthead) on the redo list. Redo pass: 048, 061, 067, 074, 095, 110, 117. B11 zip id 1v0_2RrQF1vfgzlY4vCyWjjj5RO-gcsvq.
- Next: 121 onward (124 uses refs sundara, kundavai, arulmozhi).

## 27 Nov
- The google_drive/ep11_pics store survived between messages (118 pictures and cast were intact).
- Done: 121-130 (B13), on Drive. 126 film copy cropped (European leaded window). v2 overrides written for chapter 4 (N05) up to 160. B12 zip id 1cf4XEiz5rs1VGHUSwiLxBkY99iq8OFTj.
- Redo pass unchanged: 048, 061, 067, 074, 095, 110, 117. Next: 131 onward.

## 28 Nov
- Done: 131-140 (B14), on Drive. Nothing new on the redo list (048, 061, 067, 074, 095, 110, 117). B13 zip id 1cw1XYteJnm14Dahzfnu6h65CyQTsfPZ_. Next: 141 onward.

## 29 Nov
- Done: 141-150 (B15), on Drive. Redo list unchanged (048, 061, 067, 074, 095, 110, 117). B14 zip id 14BnTVGbI6QhqGtOIpN9MUGFPZByXvX4h. Next: 151 onward (157 uses refs kundavai, arulmozhi).

## 30 Nov
- Done: 151-160 (B16), on Drive. Redo list unchanged (048, 061, 067, 074, 095, 110, 117). B15 zip id 1K44xyg4RLuFPziQ3BkL15aGjdbqNMb-r. Next: 161 onward; write v2 overrides for chapter 5 (N06, images 165-197) first.

## 1 Dec
- Done: 161-170 (B17), on Drive. v2 overrides written for chapter 5 (N06) up to 197 (brothers ref for 184, 186, 188, 191, 197). Redo list unchanged (048, 061, 067, 074, 095, 110, 117). B16 zip id 1WMhslxLOezKgQVZWUUNR9bUqb_beR_xV. Next: 171 onward.

## 2 Dec
- Done: 171-180 (B18), on Drive. Redo list unchanged (048, 061, 067, 074, 095, 110, 117). B17 zip id 1GFajERzbSC6gk23lw63jXnaGDIKbHYqv. Next: 181 onward (184, 186, 188 use the brothers ref).

## 3 Dec
- Done: 181-190 (B19), on Drive. Redo list unchanged (048, 061, 067, 074, 095, 110, 117). B18 zip id 1f0FTVTnyaij_p4d9vKsrI3FK-o0me9Sx. Next: 191 onward (191, 197 use the brothers ref); write v2 overrides for chapter 6 (N07, images 198-230) first.
