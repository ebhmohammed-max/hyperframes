# EP17 "1926: ஒரு சாதாரண நாள்" (A normal day 100 years ago): status

Topic and length (about 8 minutes) chosen by the user on 20 Nov 2026. Same recipe, voice (`voice-02`) and styles as EP16. New in this film, as asked: a harder hook, a graphics layer (`film/fx.mjs`: maps, number cards, mock-ups, motion graphics) and a picture behind each chapter card.

## Done (20 Nov 2026)
- Research (web search extracts) → `FACT_SHEET.md`; many lines are marked **check**.
- Script v1: `script/script.mjs` → `SCRIPT_TA.md`, 7 clips, 69 lines, 7,189 characters.
- Narration N01–N07 with `voice-02`, 484.4 s; `narration/align.json` (0 lines flagged). `N08.mp3` (end card voice) copied from EP16.
- Shot list: 128 pictures (`shots/shots.txt` → `shots/prompts.json`, `SHOTLIST.md`).
- Map data `film/geo.json` (Natural Earth, cut to South India and Sri Lanka).
- Graphics layer `film/fx.mjs`, wired into `film/gen.mjs`, and checked on still frames of all seven clips with placeholder pictures.
- Cast reference pictures: father, mother, girl (`shots/CAST.md`).
- Pictures 001–098 generated, looked at and uploaded (batches B01–B10; 048 remade in B06). 072, 074 and perhaps 061 are to be remade at the end.

## Next
1. Pictures 099–128 (`$PY tools/batch.py <batch> <first> <last> [big …]` zips a batch and builds the review sheet), then the remakes listed under "Picture batches" (upload every batch in the turn it is made; the workspace can be wiped between turns): `python3 tools/next.py 10` prints the next prompts; save to `out/raw/NNN.jpg` (pass `out/cast/<key>.jpg` for rows with refs). Ten per turn. After each ten: `bash tools/restore.sh` (sheets and film copies), look at the sheet, `python3 tools/pack.py a b`, upload the zip to the Drive `images` folder, log it below.
2. `node film/gen.mjs N01 N02 N03 N04 N05 N06 N07 && node film/title.mjs && node film/end.mjs`; every clip must report no MISSING pictures.
3. Look at frames of the hook and of each graphic with the real pictures (`hyperframes snapshot --no-end --at … -o /tmp/x .` inside `film/Nxx`).
4. `bash tools/render.sh` (it relinks `shared/plates` to `out/img`), then `bash tools/finish.sh parts` and `VB=1350k bash tools/finish.sh 720`; upload; update this file; commit and push.

## Chapters
| Clip | Card | Lines | Seconds | Pictures | Added graphics |
|---|---|---|---|---|---|
| N01 | (hook) | 10 | 51.4 | 22 | clock, four struck-out words, split screen 2026/1926, big "27", six chapter words |
| N02 | அலாரம் இல்லாத காலை | 10 | 67.1 | 23 | clock, number card (8,300 lamps), then-and-now bars (population) |
| N03 | ஒரு அணா பயணம் | 11 | 70.1 | 18 | clock, number cards, tram ticket, coins (1 rupee = 16 annas = 192 pies) |
| N04 | பள்ளிக்கூடம் யாருக்கு? | 8 | 68.4 | 12 | 100-dot literacy grids, Presidency map, number card (14) |
| N05 | செய்தி வர நாள் ஆகும் | 10 | 75.5 | 13 | clock, newspaper, post card, telegram, number card (5 miles), Boat Mail route map over four lines |
| N06 | பேசாத சினிமா | 9 | 72.8 | 19 | clock, silent film title card, number card (1931), timeline 1926 → 1975 |
| N07 | இருபத்தேழு வயசு | 11 | 79.0 | 21 | clock, timeline (penicillin), disease words, number card, big "27", infant mortality grid, split screen 2026/2126 |

Chapter card backgrounds (`CARD_BG` in `film/gen.mjs`): N02 `mother_kolam_lamp` (039), N03 `tram_mount_road` (049), N04 `thinnai_school` (065), N05 `reader_shop_front` (076), N06 `audience_backs_screen` (090), N07 `lamp_turned_down` (107). Title: plates 001, 012, 049.

## How the graphics are driven
- Fourth field of a script line is `fx`; forms are listed at the top of `film/fx.mjs`. `only: [shot names]` keeps those pictures for the graphic; `reuse: [shot names]` borrows pictures from later chapters (hook line 8).
- Full-screen graphics (`coins`, `dots`, `map`, mock-ups `paper`, `postcard`, `telegram`) replace the pictures of that line.
- The maps move through an HTML wrapper (`#xN-cam`), not an SVG group: GSAP on SVG groups gave wrong positions.
- Spoken text must not change when `fx` fields are edited (no new narration needed).
- Test stills: point `shared/plates` at a folder with placeholders for missing pictures; `tools/render.sh` points it back to `out/img`.

## Picture rules
- See `shots/CAST.md`. No sick or dead child; child marriage only as still life; real people from behind; no readable writing.

## Open points
- Decided without asking: year 1926, city Madras, an invented family, "life expectancy 27" planted in the hook and paid off in the last chapter.
- `FACT_SHEET.md` lines marked **check**, above all: rice price, wages (figures are from about 1920), Boat Mail timing, tram fare, women's literacy in the Presidency.
- The Presidency outline and the rail route on the maps are hand-drawn and labelled approximate.
- Mock-ups carry the real names சுதேசமித்திரன் and ஆனந்த விகடன் on invented pages, labelled "மாதிரி வடிவம்".

## Drive
| What | Id |
|---|---|
| Folder `EP17_1926_Oru_Saadharana_Naal` (under root `1WqhshH9XcvNUna4lzyS692eidgWQfeS1`) | `14H9Jax-G66f0oyS3vF6QyrSpSUsvKJlY` |
| Folder `EP17_…/images` | `1DR9Un3pxa9HtVO_IWhfFxbhORRL3qMSY` |
| `EP17_1926_SCRIPT_TA_v1.md` | `1mE9wGxOvx7dh9aPZyzCvedCPxDWndhc1` |
| `EP17_1926_FACT_SHEET.md` | `1bxTTsLc4kG04AtztcAZUClD8sF88Nd-p` |
| `EP17_1926_SHOTLIST.md` | `1lqct2aqnLGRe-R3BE9dAk0JPodUNU49g` |
| `EP17_narration_scratch_voice02.zip` (N01–N08) | `1zISq7AY7-RUMdD5JafCBiNjarIHw2cb9` |
| `images/EP17_cast.zip` | `1ei7-lg5HWbN9sbFa4HouD4QkcbW8w-go` |

## Picture batches
| Batch | Pictures | Drive id | Notes |
|---|---|---|---|
| B01 | 001–010 | `16xGDScGvfxRA0gUeC2y1Q7Q4AQ1F4o-U` | made twice: the first seven were lost in a workspace wipe before upload; all ten fine |
| B02 | 011–020 | `1Px2QIFfCGfB4bMZl9RK1bJD3LEolydbi` | all fine; 012 has dark window shutters down both edges (crop if it shows in the split screen); 017 shows the baby out of focus behind the hands |
| B03 | 021–030 | `1v-_tSjMUtr46d8U-HtD5Xm0nWMHfVf_U` | all fine; 021 (family, three refs) matches the cast pictures |
| B04 | 031–040 without 036 | `1q6X5_4RH09wM6buXC2OltYNtBzIHboNG` | 036 failed once ("Image generation failed") and the turn limit stopped the retry: make it first next turn and put it in the B05 zip; the other nine fine (035 shows the whole woman, not hands only) |
| B05 | 036, 041–049 | `15SpmNLj7AVQAO9m9dhef9cQB7j70vwWY` | 036 now made (it is in this zip, not in B04). **048 to redo**: readable shop signs ("Sri Rama Stores", "Ceylon Tea House") and a flatter, illustrated look; remake it first next turn with the same prompt plus "the shop fronts are plain, with no signboards, no name boards and no lettering of any kind" and put the new file in the B06 zip. 049 (title and N03 card plate) fine, the tram carries a small number. 036 shows a man sitting in the background |
| B06 | 048 (remake), 050–058 | `1CHTCvm9TKpGgk0BIfrNChEs9naP6TvAf` | all fine. The 048 here replaces the one in the B05 zip (when restoring, unzip the batches in order so this one wins). Batches from here on run 059–068, 069–078 … 119–128 |
| B07 | 059–068 | `1giWdS48vSoEAOagB9jJtkaOqj--YJ0tg` | all usable. 061 (bus): the body looks later than 1926 (more like the 1940s) and it carries a small number plate "T401"; kept, remake only if there is a spare slot or the user asks. 067 (girl, ref) matches; three adults stand in the background. 065 (N04 card plate) fine |
| B08 | 069–078 | `1x4I-u_LPlw9AGg4Hv87Hkbeh7Uo_zqq6` | eight fine (076, the N05 card plate, is good). **072 and 074 to redo: the turbans came out in the Punjabi style** (coloured turbans in the council, a bearded man in a dark turban at the signboard; the woman in 072 has her head covered). See "Remakes" below |
| B09 | 079–088 | `1rSzofRyz8GWc2SkMnJm26UsImORjkCGx` | all usable. 080: the wireless box stands beside the cloth (the cloth covers the horn). 083: the steamer is a small launch with a blue ensign. 085: the wing shape is a little odd. 088 (father, ref) matches |
| B10 | 089–098 | `1b1F6Ob3tzLXJusUjHi6UDl7SH7QQri_U` | all fine (090, the N06 card plate, is good). 092 was generated with the reworded head-cloth text instead of "turban" and came out right. 094: the crowd stands facing the projector, in its beam |

### Remakes (do them in the turn after picture 128, then go straight on to the render)

The word "turban" as the main feature of a figure pulls the picture towards North India. In a remake, and in any coming prompt where the main figure wears one, write "a white cloth wound loosely round the head in the Tamil way, moustache, no beard" instead.

| Picture | Why | Change to the prompt |
|---|---|---|
| 072 | council chamber full of coloured Punjabi turbans; the woman's head is covered | "Madras in South India, 1926 … Tamil men in black coats, most with white head-cloths or bare-headed with oiled hair, no beards, no coloured turbans … one Tamil woman in a white sari with her hair in a bun, head uncovered" |
| 074 | the farm worker looks Sikh (dark turban, beard) | "a Tamil farm worker, bare-chested, in a short veshti with a white cloth wound round his head, moustache, no beard" |
| 061 | bus body looks 1940s, number plate "T401" | optional, since the turn is needed anyway: "a small motor bus of the early 1920s built on a lorry chassis, spoked wheels, upright radiator, open wooden sides, canvas roof, no number plate" |

The remade files go into one more zip (`EP17_B14_remakes.zip`); when restoring from Drive unzip it last.

## After a full wipe of the workspace
`git fetch -q origin arena/d486087a-hyperframes && git reset -q --hard FETCH_HEAD`, `bash projects/nk-ep17-1926/tools/setup.sh`, download the Drive zips above into `<repo>/google_drive/`, `bash tools/restore.sh`, unzip the narration zip into `narration/`, recreate the links `shared/vo` → `../narration` and `shared/plates` → `../out/img`. Map data can be rebuilt from Natural Earth (`world-atlas` countries 10m and the 50m admin-1 GeoJSON), but `film/geo.json` is in git.
