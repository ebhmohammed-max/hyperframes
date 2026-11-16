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
