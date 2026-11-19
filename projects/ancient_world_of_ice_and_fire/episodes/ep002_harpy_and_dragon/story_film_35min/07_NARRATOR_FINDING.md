# The narrator is the problem, not the pacing

**Listen:** `audio/pilot/EP002_VOICE_COMPARISON.mp3` — three clips of the same writing, back to back.

| Clip | What it is                                              |
| ---- | ------------------------------------------------------- |
| 1    | Block 09 as rendered, voice-02 speaking naturally       |
| 2    | Block 09 pulled back to Episode 01's pace (tempo 0.855) |
| 3    | Block 02, the same treatment                            |

I built the metronome rig you approved (Option B) so this could be measured rather than argued. Then it rejected every take, and the reason is worth more than the fix.

## What the measurement says

I extracted the reference from the film you actually approved. Episode 01's delivered blocks, analysed with the same silence detector:

- **articulation 161.5 wpm** (speaking rate, pauses excluded)
- **pause share 16.8 %** of each block
- 11–15 pauses per block
- speech filling 26.9–29.4 s of each 30 s slot

Voice-02, ten blocks:

- **articulation mean 197.2 wpm** (range 186–208)
- pause share 8–22 %, erratic
- **1.22× the speed of the Episode 01 narrator**

That ratio is not a coincidence, and it is not something a script can absorb. To fill 28.8 s at Episode 01's speaking rate you need **78 words per block**. This script has 62–68. Getting there means adding 10–16 words to all seventy blocks — a different film at a different density, not a tuning pass.

The engine is also non-deterministic: the identical text rendered three times gave 21.79 s, 22.94 s and 22.73 s. So "render until it fits" was never a real method. It works on Episode 01 only because that voice happened to be slow enough that most takes landed near the slot without help.

## Why I will not just slow this voice down

I could. Tempo 0.855 puts block 09 at 28.71 s — mathematically perfect. But pull a voice 15 % slow and it stops being a performance and becomes a stretched recording. The breaths stretch with it, the consonants smear, and it is audible within ten seconds.

Clip 2 and 3 of the comparison are that experiment. Play them against clip 1 and decide for yourself — but I expect you will hear exactly what I hear, which is a man being slowed down.

## What actually resolves this

The whole problem exists because **I could not verify that voice-02 was the Episode 01 narrator**, and recorded 15 blocks before that was settled. That was my error, and it is the one thing here I would undo.

The fix is to establish one narrator, once, and then build all 70 blocks on it:

1. **Audition two candidates** against this script's actual opening, with the delivery instruction being _slow, low, documentary — the pace of the Episode 01 film_.
2. Render one test block per candidate and measure articulation. I need something near **161 wpm, not 197**.
3. Only the candidate that lands there gets the remaining work.
4. If neither does, the third option is to have Ep02 recorded on the same voice service and settings that produced Episode 01, and that is a decision about tooling, not text.

**What has been wasted so far:** 15 blocks of a film that needs 70. Everything else from this session survives — the script, the seven chapters, the parser, the timing plan, the metronome rig, and the reference measurements are all reusable with a different voice.

**What has not been wasted:** knowing that Episode 01's film runs at 161.5 wpm articulation and 16.8 % pause share. That number did not exist before today, and it is the acceptance test for whoever narrates Episode 02 — and every episode after it.
