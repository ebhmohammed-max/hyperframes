# EP23 picture rules

No reference pictures. People are held together by fixed descriptions in `shots/expand.py` (`REF`).

- Every picture is an illustration made for this film. None is a photograph or a record.
- **Hitler's real face is shown** (user's instruction, 26 Nov 2026; before that the rule was "no face of a real person"). Every picture is still a made image in the style of a film still, never a period photograph. Each ref passes a reference picture to the image tool (`out/cast/`, listed in `shots/expand.py` `REFIMG`):
  - **H** the man in his forties → `H_photo.jpg`, a photograph of about 1933 (credo.library.umass.edu), used as likeness reference only.
  - **B** the boy of about eleven → `B_photo.jpg`, the school photograph of about 1900 (Getty), likeness reference only.
  - **Y** the youth of seventeen to nineteen (Linz 1906 to Vienna 1908) → `Y.jpg`, made from the two photographs. `A18.jpg` (= picture 008, eighteen, on the Academy steps) is the same young face and may be passed too.
  - **A** the young man of twenty (Vienna 1909, homeless) → `A.jpg` (= picture 004, made from 008 so the face stays the same). `A_old.jpg` is the first attempt: it reads as a man near forty, do not use it.
  - No authentic photograph of him between 1900 and 1914 was found, so Y and A are reconstructions between the school picture and the adult face. Say so if asked.
  - **K** mother, **F** father → `K.jpg`, `F.jpg`: invented actors of the right type and dress, not likenesses.
- He is never lit like a hero and no picture celebrates him: the adult is shown cold, in shadow, or small against what he caused.
- **Frame:** the film runs in 2.2:1 with black bars of 104 px. Compose with the head clear of the top and bottom edges; `film/gen.mjs` `SHIFT` moves a picture down when a head sits too high.
- **No flags, emblems, symbols, insignia, armbands or salutes** in any picture, in any chapter. Uniforms, where they must appear, are plain dark shapes seen from far or from behind. The pictures name no party; the narration and the cards do.
- **No readable writing**: no signboards, posters, newspapers with letters, documents with letters. Every number, name, date and source is set in the edit (`film/fx.mjs`).
- **Nothing graphic.** Not shown: bodies, wounds, executions, the inside of a camp in use, the suicide. Empty places stand for them: a queue, a railway track, a pile of shoes, a gate seen from far, an empty room.
- **Nothing that celebrates him.** Crowds and rallies are seen from far, at night or in shadow, and the mood is a warning. He is never lit like a hero and never shown larger than the people he harmed.
- Real buildings (the Vienna Academy, the Reichstag, the Brandenburg Gate) appear from far and are not exact.
- Looks keep the times apart: **L** Upper Austria 1889–1907 (small town, lamp light); **V** Vienna 1907–1913 (winter, gas lamps, stone); **X** what came later, 1933–1945 (far, dark); **S** still lifes; **O** setting given in the subject. More looks are added with their chapters (the trenches, Munich, Berlin, the war, the bunker).

## Kept with a note

- 008: the small figure walks up the Academy steps towards the closed doors (the shot list says he walks away). The picture still reads as "the door stayed shut".
- 009: a few smaller stones stand behind the two gravestones.
- 010: the man on the balcony wears a hat; a dark blank cloth is carried in the crowd.
