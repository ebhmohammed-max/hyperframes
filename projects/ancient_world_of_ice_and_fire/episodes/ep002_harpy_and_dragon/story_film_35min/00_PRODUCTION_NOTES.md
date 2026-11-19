# Episode 02 — The Harpy and the Dragon

## Status

**Script: complete — v02, story-led rewrite.** 70 narration blocks, 4,939 spoken words, 35:00,
1,050 image slots at 2 seconds each. **No audio recorded. No images built.**

**v01 is superseded.** It was a well-argued essay that a viewer could leave at any chapter
break, which is exactly the problem the user named. v02 is written to `docs/STORYTELLING_CRAFT.md`.
Read the v02 files only; v01 is kept as a record of the mistake.

## What v02 changes, and why

| v01                                                   | v02                                                                                                              |
| ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Opened on Ghis's self-image                           | Opens on a coin in the ash, in a hurry, by someone who never came back                                           |
| Protagonists were "Valyria" and "Ghis" — abstractions | One coin is the through-line; it can be lost, which is what a story needs                                        |
| Narrator explained the sources a dozen times          | The honesty is one line at 01:00, turned into the film's central question, then never repeated                   |
| Every chapter ended on a lesson                       | No lessons. The coin's fate answers the question                                                                 |
| Uniform 63–83 word blocks                             | 62–85, varied deliberately, short punch blocks after long ones                                                   |
| No dramatised moment in 35 minutes                    | Scenes: the night before the battle, the officer on the wall, the negotiator's scroll, the man opening the floor |

**Central dramatic question:** how does the strongest thing in the world lose five times, and
what does the winner become? It is stated in block 3 and answered in block 67, not before.

## What it is

The five Ghiscari wars, told as a war documentary. Old Ghis — the harpy, the legions, the
stepped pyramids — against the Valyrian Freehold and its dragons. Episode 01 ends with the
two powers on the edge of exactly this struggle, so 02 is the payoff rather than a new start.

The film's argument, stated plainly in the opening and paid off at the close: Valyria won
five times and never learned to finish. Four settlements left the enemy standing and angry;
the fifth removed the enemy entirely, and taught the rest of the world what a power with no
equal is willing to do. Ghis's capital died. The harpy did not.

## Scope decisions

- **Not a battle chronicle.** The five wars have no surviving detailed record of the fighting,
  and the script says so on camera twice. It narrates the shape of the thing — an old empire,
  a young one, four incomplete victories, one that went too far — and refuses to invent duels,
  letters or hours of victory. That refusal is the same editorial line Episode 01 took with
  the missing secret of dragon mastery.
- **Slavery is not softened.** Ghis was built on it, and Valyria refined it. The film states
  both, and does not let the fifth war read as a triumph of the good.
- **Fiction status is disclosed twice** — opening and closing. The film examines an invented
  history as a historian would examine a real one, and says which parts are Martin's and
  which are this film's reading.
- **The ending is a hand-off, not a conclusion.** It closes on Ghis surviving as culture
  rather than state, and hands to the Rhoyne. It does not reuse Episode 01's closing words.

## Structure

| Chapter | Time        | Blocks | Images    | Job                                                                                   |
| ------- | ----------- | ------ | --------- | ------------------------------------------------------------------------------------- |
| II.1    | 00:00–05:00 | 01–10  | 0001–0150 | Establish Ghis as the unquestioned power, and the two ambitions that cannot coexist   |
| II.2    | 05:00–10:00 | 11–20  | 0151–0300 | The first war: why a legion is the wrong tool for a dragon, and what restraint bought |
| II.3    | 10:00–15:00 | 21–30  | 0301–0450 | The second war: engineering as an answer, and why it failed without being stupid      |
| II.4    | 15:00–20:00 | 31–40  | 0451–0600 | The long exhale: logistics, the unarmed majority, the institution nobody names        |
| II.5    | 20:00–25:00 | 41–50  | 0601–0750 | Four victories that settle nothing; what a treaty by restraint actually teaches       |
| II.6    | 25:00–30:00 | 51–60  | 0751–0900 | The fifth war: the city taken apart, the captives, the salt, and the survivors        |
| II.7    | 30:00–35:00 | 61–70  | 0901–1050 | What the world learned; the harpy as culture; the hand-off to the Rhoyne              |

## Budget and measurement

Spoken words per block: **62–85, mean 70.6** (Episode 01: 64–74, 4,883 total). At a measured
140 wpm this is 35:07 of speech before pauses — deliberately at the ceiling, because the
Episode 01 pilot showed the selected voice runs faster than the script asks for. **Every block
must be measured after synthesis, not assumed.** If blocks overrun, trim at the sentence
clause, never by cutting an image slot.

## Files

| file                                 | what                                                                  |
| ------------------------------------ | --------------------------------------------------------------------- |
| `01_COMPLETE_NARRATION_35MIN_v01.md` | the script, with cue lines and chapter headings — the source of truth |
| `02_RECORDING_SCRIPT_35MIN_v01.txt`  | spoken text only, numbered by block, for synthesis                    |
| `03_BLOCK_TIMING_PLAN.csv`           | per-block start, word count, image range, sample budget               |
| `narration_blocks_v01.json`          | machine-readable blocks, consumed by the builder                      |

## Next steps

1. Audit block word counts against the recorded Episode 01 rate; trim any block that measures long.
2. Synthesise 70 blocks, ≤10 per turn, measure each — do not re-use Episode 01 voice settings blindly.
3. Assemble to exactly 2,100.00 s at 48 kHz, verify by decoded sample count.
4. Build 1,050 image slots. Episode 01's plates are not reusable as-is; many are Valyrian and
   Ghiscari in subject and will need new material for the war chapters.
5. Render, assemble, master to −16 LUFS, ship to Drive at ≤100 MB.
