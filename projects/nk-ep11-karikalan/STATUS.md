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
- TODO next message: EP11_B19_sheet.jpg was NOT uploaded (Drive upload rate limit). Rebuild it (`$PY tools/sheet.py 181 190`, copy to out/up/EP11_B19_sheet.jpg) and upload it with the B20 files. B19 zip id 1wd3xdMn0x9dgV_er6a7nzGKNRxtDAoLx.

## 4 Dec
- Done: 191-200 (B20), on Drive. B19 sheet now uploaded (the TODO above is cleared). v2 overrides written for chapter 6 (N07) up to 230 (faces: 203, 205, 210, 215, 218, 222, 223; no cast refs). Redo list unchanged (048, 061, 067, 074, 095, 110, 117). B19 zip id 1wd3xdMn0x9dgV_er6a7nzGKNRxtDAoLx. Next: 201 onward.
- Kept with a doubt: 194 and 195 show a fort wall with European-looking battlements under the banner; 191 the brothers face the camera with the throne behind them.

## 5 Dec
- Done: 201-210 (B21), on Drive. 205 added to the redo list (officer in a later-period tunic and turban). 207 film copy cropped via crops.json (power lines top right in the raw picture). Redo list: 048, 061, 067, 074, 095, 110, 117, 205. B20 zip id 1XiJkIkL238GrzZTYMsNbKYWrkWNRgbec. Next: 211 onward.

## 6 Dec
- Done: 211-220 (B22), on Drive. No new redo. Redo list: 048, 061, 067, 074, 095, 110, 117, 205. B21 zip id 1SwwBB-tusFFf6b4qalK_mJw2rRz_2LqZ. Next: 221 onward; write v2 overrides for chapter 7 (N08, images 231-267) before 231.
- Kept with a doubt: 215 the three walk toward the camera instead of looking back at the house.

## 7 Dec
- Done: 221-230 (B23), on Drive. Chapter 6 (N07) complete. No new redo. Redo list: 048, 061, 067, 074, 095, 110, 117, 205. B22 zip id 1IqH086tbCHlXAy0DhKB_9hqhv5dDCNlr. Next: 231 onward; write v2 overrides for chapter 7 (N08, images 231-267) first.
- Kept with a doubt: 225 the travellers wear sleeved tunics and shoulder sacks; 228 hooded cloaks in a misty forest that looks more northern than Tamil.

## 8 Dec
- Done: 231-240 (B24), on Drive. v2 overrides written for chapter 7 (N08) up to 267 (cast refs: 236 and 238 uttama, 243 arulmozhi+uttama, 247 and 264 brothers, 258 sundara; 244 crowd; 250 brother-sister stays a silhouette because the 1971 claim has no evidence). No new redo. Redo list: 048, 061, 067, 074, 095, 110, 117, 205. B23 zip id 1LQZFH4npFQ-IkLJ25yPqBuyw-oeGvJ-3. Next: 241 onward.

## 9 Dec
- Done: 241-250 (B25), on Drive. No new redo. Redo list: 048, 061, 067, 074, 095, 110, 117, 205. B24 zip id 1tjCKQkWvbM_w87R361WuQvUX6A8HtnJu. Next: 251 onward (258 sundara ref, 264 brothers ref).

## 10 Dec
- Done: 251-260 (B26), on Drive. 255 added to the redo list (crisp Khmer-looking script fills the frame). Redo list: 048, 061, 067, 074, 095, 110, 117, 205, 255. B25 zip id 1d11PdLCOWRWr-7d-4Y9cTMfmYE3pmUjI. Next: 261 onward (264 brothers ref); write v2 overrides for chapter 8 (N09, images 268-297) before 268.
- Lesson: a square-on, evenly lit wall of letters comes out as clean Khmer; always ask for a steep raking angle and broken, lichen-covered marks.

## 11 Dec
- Done: 261-270 (B27), on Drive. Chapter 7 (N08) complete. v2 overrides written for chapter 8 (N09) up to 297 (268 Nandini invented face, 273 and 276 1950s readers, 277 brothers ref, 282 aditya ref, 290 and 291 cinema crowds; Kalki stays from behind). No new redo. Redo list: 048, 061, 067, 074, 095, 110, 117, 205, 255. B26 zip id 17sDqf28WcQDT5x-7AgTvyW1YrAbaWcNk. Next: 271 onward.
- 268 came out with her whole face visible (the veil sits on her hair), kept: Nandini is fictional.

## 12 Dec
- Done: 271-280 (B28), on Drive. 274 added to the redo list (magazine illustration came out as European monks under Gothic arches). 272 film copy cropped via crops.json (garbled Tamil-like poster lettering in the background of the raw picture). Redo list (10, exactly one message): 048, 061, 067, 074, 095, 110, 117, 205, 255, 274. B27 zip id 1Te5c78LVUEv2l3oBX-AN9o6lbrq4VH2Q. Next: 281 onward (282 aditya ref).
- Kept with a doubt: 273 magazine covers at the stall carry small blurred mastheads and painted portraits of women.
- Lesson: an "ink illustration" inside a magazine drifts to European woodcut style; name South Indian dress and granite pillars inside the illustration too. Shop interiors grow posters with pseudo-Tamil lettering; say "bare walls, no posters".

## 13 Dec
- Done: 281-290 (B29), on Drive. No new redo. Redo list (10): 048, 061, 067, 074, 095, 110, 117, 205, 255, 274. B28 zip id 1ul99sNTUEOS9t4i--3_zjJ-PjBsnPfBK. Next: 291 onward; write v2 overrides for the last chapter (N10, images 298-327) before 298.
- Kept with a doubt: 289 the palace film set looks North Indian (arched, Rajasthani) rather than Chola.

## 14 Dec
- Done: 291-300 (B30), on Drive. Chapter 8 (N09) complete. 297 added to the redo list (lit band reads as Egyptian hieroglyphs). v2 overrides written for the last chapter (N10) up to 327 (298 aditya, 301 brothers, 310 and 312 Rajendra invented face: about forty or thirty, broad face, thick curled moustache, tall jewelled crown, pearl necklaces; 316 arulmozhi older; 321 aditya+arulmozhi).
- Redo list (11): 048, 061, 067, 074, 095, 110, 117, 205, 255, 274, 297. Plan: 301-310, 311-320, then 321-327 plus three redos in the same message, then the other eight redos.
- B29 zip id 1zDZ53ZKoZu4Y4O3IHFM5ZYtFkVYGJlJd.
- Kept with a doubt: 295 the three inscribed slabs stand like headstones.

## 15 Dec
- Done: 301-310 (B31), on Drive. No new redo. Redo list (11): 048, 061, 067, 074, 095, 110, 117, 205, 255, 274, 297. B30 zip id 1kaPbjZQkd3Ly6vK0seOF4i4NjFVDx6TA. Next: 311-320 (316 arulmozhi ref), then 321-327 (321 aditya+arulmozhi) plus three redos.
- Note: sheet.py trimmed 202 px of dark stone off the bottom of 302 as if it were a black bar; the film copy still looks right.

## 16 Dec
- Done: 311-320 (B32), on Drive. No new redo. Redo list (11): 048, 061, 067, 074, 095, 110, 117, 205, 255, 274, 297. B31 zip id 15ou41CGxETUDXBIwOLbvgljfVxCtvwAS. Next: 321-327 (321 aditya+arulmozhi) plus three redos (suggest 297, 255, 274), then the other eight.
- 311 (royal seal, no lettering, beaded rim) worked with this wording; reuse it for redo 074.
- Kept with a doubt: 319 the ships have a Viking look (curved prows, single square sail).

## 17 Dec
- Done: 321-327 (B33). ALL 327 shot-list pictures now exist except 067 and 110 (never generated). Three redos made and swapped in: 255, 274, 297 (old versions kept in google_drive/ep11_pics/replaced/, new originals in .../redo/). B26, B28, B30 repacked locally; upload the replacements and trash the old Drive files (ids in the session log).
- Redo list (8, one message): 048, 061, 067, 074, 095, 110, 117, 205. Write each to google_drive/ep11_pics/redo/NNN.jpg, view, then copy over raw/NNN.jpg, rerun sheet.py for B05, B07, B08, B10, B11, B12, B21, pack, replace on Drive.
- After that: full film (tools/setup.sh, narration from Drive, render N01-N10, title sequence, subscribe pop-up, join, level, upload) and EP11_all_327_images_final.zip.
- B32 zip id 1y-ob01DcT6MBiuOb4UdWlfU5gDZ0qTtV.
- B33 on Drive (zip 1134mwujkBdA3Jv182YuPgNyR8V9eg-0t). B26, B28, B30 replaced on Drive with the remade 255, 274, 297 (old files trashed). trash_file input: {"input": {"file_id", "supports_all_drives": true}}; sequential uploads did not hit the rate limit.

## 18 Dec · final redo pass: all 327 pictures now exist

Remade and swapped into the store (`google_drive/ep11_pics/raw/`, old versions in `replaced/`):
048, 061, 074, 095, 117, 205; made for the first time: 067, 110. `shots/redo.txt` is now empty.
110 took two tries: the first had a mahout in a turban and waistcoat on a desert plain
(kept as `redo/110_first_try.jpg`); the second names a bare-chested mahout and palmyra palms.

Batches re-sheeted, repacked and replaced on Drive (old files trashed). New ids, zip / sheet:
- B05 041–050 `1Mf1HO1RZQdQosgEgXXPphshQnC5_XkVc` / `1yy3PJE2z5yG81X47z0xG0jS2odaX2QO_`
- B07 061–070 `1zaM04P9-GfZrPPLuwSy0-B0v85KjYCbH` / `1-9uUz7MOAZFd5AfN30jpUucH958kFfvR`
- B08 071–080 `1iOcEThkTUK91AvVBJ8ckpyP1YheGaGng` / `1ibgF1tus4DmlftpMYX-3ZfnzEk6wBvCG`
- B10 091–100 `19PBKJgfhfSl-5NrdcGqRgiYysG24gaeu` / `1HPTcHveEvU_2-bNfxM9uYa2gLLKcQ6hA`
- B11 101–110 `1Vgr4U-UsmY5LKgA67t3jgKZTylNlyv9u` / `1rWDNGfHiKm4UhsVVU-hcaSPU6uEwqfgP`
- B12 111–120 `19anWu2d0Le-ZgFedcCD4TyuB_MeclpoX` / `1VVTFvrerVN2bGd_XAKy08-7nFbqd5YtE`
- B21 201–210 `1rLa1NmdjLt-emxVX6OwhVmrP_faS46Ns` / `1XTdAk7GQ1LgnmicHKfyzbJaCxI0zcPqk`

Small things left as they are: 095 has one basket-hilted sword at the left edge; 117 has a tiny
smudge of marks on one building in the drawing; 205 is more photographic than painted and the
palm leaf is a wide sheet; 074 has an oil lamp with a glass chimney at the edge.

Next: the full video (setup, narration from Drive, clips N01–N10, title sequence, subscribe
pop-up, end card, join, levelling, 1080p parts, 720p copy, upload, one zip of all 327 pictures).
