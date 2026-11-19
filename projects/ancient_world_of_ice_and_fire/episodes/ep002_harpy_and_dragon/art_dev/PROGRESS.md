# Episode 02 art progress

**19 of 70 scene masters complete — 285 of 1,050 plates.**

Verified no gaps: scenes 001–019 are all present, all uploaded to Drive, all
confirmed by directory listing.

## Done

| Batch | Scenes  | Drive folder                        | Status                                 |
| ----- | ------- | ----------------------------------- | -------------------------------------- |
| 01    | 001–010 | `1Szxuff_aFWySEGhkURjYC9L1ZCGGQ8zb` | 10/10 uploaded                         |
| 02    | 011–020 | `1PyidDrkaNxyieuH-vAOWZ2axv9ObYj4n` | 9/10 uploaded — **010 is in batch 01** |

Correction to the folder naming: the folders were created as ranges but the
actual generation ran 001–010 then 011–019, so scene 010 sits in batch 01 and
batch 02 holds 011–019. Folder titles are cosmetic; **file names are the
authority** and every file is `NNN_master.jpg`, so nothing is lost. Rename the
folders later or ignore the off-by-one.

## Next

Batch 03 = scenes 020–029. Art directions already written for all seventy in
`scripts/episode-audit/ep002_scene_directions.py`, so no thinking is needed,
only generation.

## Rule being followed

Generate ten, upload ten, confirm they landed, keep going. Plates are derived
locally from masters (about 104 MB for the full set) and are reproducible, so
they never go to Drive. Drive holds masters only, about 14 MB for all seventy.

## State after batch 03

**29 of 70 masters — 435 of 1,050 plates.**

Scenes 001–019 exist locally. Scenes 020–029 were uploaded to Drive and then
deleted locally, so **their plates are built but their source masters are
Drive-only.** That is fine as long as nothing needs re-deriving, and it is a
real gap if something does.

The rule that caused it was too aggressive. Deleting a master after upload
saves 200 KB and costs the ability to rebuild a plate. From batch 04 on, the
masters stay: seventy masters total about 14 MB, which is nothing next to the
104 MB of plates they generate or the 840 MB of render segments.

Recovery path if a Drive-only master is ever needed: it is in the Drive folder
named in DRIVE_INDEX.md, file `0NN_master.jpg`.
