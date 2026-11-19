# Episode 02 — recording pilot v02

**Listen to this first:** `audio/pilot/EP002_PILOT_150s.mp3` — 2 min 30 s, five blocks back to back on the film clock.

Each block sits in its own 30-second slot with silence where the pictures go, so what you hear is the pacing the finished film will have, not a trailer edit.

| Block                             | Slot        | Words | Speech in slot | Delivered wpm | Tempo applied |
| --------------------------------- | ----------- | ----- | -------------- | ------------- | ------------- |
| 01 — the coin in the ash          | 00:00–00:30 | 64    | 26.61 s        | 144.3         | none          |
| 12 — the noise above the cloud    | 05:30–06:00 | 70    | 28.92 s        | 145.2         | none          |
| 19 — the pay chest spills         | 09:00–09:30 | 72    | 26.19 s        | 165.0         | none          |
| 30 — the tribute stops            | 14:30–15:00 | 66    | 28.62 s        | 138.4         | none          |
| 59 — the buyer in the next street | 29:00–29:30 | 62    | 26.91 s        | 138.2         | none          |

**Mean 146.2 wpm, zero pitch-correction, zero truncation.** Episode 01 needed a 7.8 % tempo lift on its opening block to hit 30 s; this script does not need any. Every word that was written is the word that gets spoken.

## Why the five

They are not the five best. They are the five that would expose a problem if one existed:

- **01** is the opening — the only block where a slow read is a virtue, and the only one carrying the coin's first appearance.
- **12** is the longest-sentence block in Chapter II. It is the one that would overrun if the prose were too dense.
- **19** is the densest narrative turn in the film — four things happen in thirty seconds.
- **30** is a chapter break, where the film has to change gear without a narrator's gear change.
- **59** is the smallest block, and the one that carries the film's quietest idea.

## What the pilot proved, and what it changed

**Word count is not the predictor of overrun. Clause length is.**

Block 19 is the _longest_ block in the pilot at 72 words and runs 26.2 s. Block 12 is two words shorter and runs 28.9 s. The difference is that block 19 is built from short sentences and block 12 has one 44-word sentence in it. So the ceiling is not "72 words"; it is **"no sentence longer than about 25 words at a chapter's emotional peak."**

All 70 blocks were then scored on words-per-sentence weighted by block length. Four blocks sit far above the rest and will need a breath mark (an ellipsis, never a written pause instruction) if the recording run shows them pushing 29 s:

- B66 — 22.0 words per sentence
- B68 — 21.7 words per sentence
- B54 — 17.8 words per sentence
- B64 — 17.2 words per sentence

Nothing needs rewriting now. This is a list to watch during the recording run, not a defect.

**Projection at pilot pace: 1,924 seconds of speech across 70 blocks — 32:04 of a 35:00 film.** That leaves 176 seconds of air for chapter cards, title stings and the two places the film deliberately stops talking. Episode 01 ran the same margin and landed at exactly 35:00.

## The mechanical contract

- Every block is **1,440,000 mono samples at 48 kHz, 16-bit PCM = 30.000000 s exactly.** WAV is the timing authority; the MP3 is a preview and its container duration is not.
- Silence is digital zero, appended at the tail only. No fades, no compression, no loudness mastering in the pilot.
- Peak levels −0.6 to −1.5 dBFS. Mean delivery level is set later in the mix, not here.
- Word sequences were tokenised and compared against the script after synthesis. All five match. This compares _submitted text_, not recognised speech; no forced alignment was run.
- `scripts/episode-audit/conform_ep002_pilot.py` reproduces every number above.

## What has not been done

- The remaining **65 blocks are not recorded.**
- **No listening QC.** Nothing here has been heard by a human. That is what this file is for.
- No music, no sound design, no image sync — the pilot is voice on a silent clock.
- No voice approval. `voice-02` was auto-assigned when the audition was skipped. If it is not the Episode 01 narrator, say so now and it costs five blocks to change, not seventy.

## The one question

Does this voice, at this pace, hold you for two and a half minutes?

If yes, the remaining 65 blocks record in six batches and the film enters image assembly. If not, the fix is a re-record of five blocks, and I would rather do it now.
