# Licensed documentary audio

Four musical recordings and ten SFX acquired from pinned GitHub revisions. The primary composer/creator license pages were checked separately. See ASSET_REGISTER.json for exact sources, revisions, SHA256 and file sizes; PRIMARY_SOURCE_EVIDENCE.md for observations; YOUTUBE_AUDIO_CREDITS.txt for required publication credits.

Restore from repository root:

```sh
python scripts/episode-audit/fetch_licensed_documentary_audio.py
FFMPEG=/path/to/ffmpeg python scripts/episode-audit/mix_documentary_audio.py
```

The score uses CC BY 4.0 attribution even where the FreePD mirror declares CC0. Kenney RPG Audio is CC0. Mastering uses two-pass -16 LUFS / -1.5 dBTP normalization, restrained chapter punctuation and narration-controlled ducking. The cue sheet is recorded by the mix script in production/SOUND_MIX_REPORT.json. Only three of the ten SFX are currently used; the others are available candidates, not artificially placed foley.

The 35-minute duration, selected voice and narration order are unchanged. The mix is not a final film export and has not received subjective listening approval. Licenses permit commercial adaptations but do not guarantee Content ID immunity or YouTube monetization; other film rights are not cleared by these audio licenses.
