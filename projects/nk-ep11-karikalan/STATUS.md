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
