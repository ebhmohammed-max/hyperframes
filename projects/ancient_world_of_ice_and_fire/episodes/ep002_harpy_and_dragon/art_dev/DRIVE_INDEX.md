# Episode 02 art — Drive layout

Root folder in the user's Drive: **The Long Night — 3D cinematic art**
`1F4hU9QZwz2_MUqvld_VLqw2BB6w2IKv9`

Episode folder: **Episode 02 — The Harpy and the Dragon**
`1SltSCtCl6DbqvYOaQi85KEpTdzqyZQqS`
https://drive.google.com/drive/folders/1SltSCtCl6DbqvYOaQi85KEpTdzqyZQqS

## Masters

Seventy scene masters, ten per folder, uploaded in batches so the workspace never
holds more than one batch at a time. Plates are derived locally, never stored in
Drive — they are reproducible from a master in under a second.

Parent: `1TA_QhipVZD1fimuqCLhfYXxBqGJeX7nX`

| Folder   | Scenes  | Drive ID                            |
| -------- | ------- | ----------------------------------- |
| Batch 01 | 001–010 | `1Szxuff_aFWySEGhkURjYC9L1ZCGGQ8zb` |
| Batch 02 | 011–020 | `1PyidDrkaNxyieuH-vAOWZ2axv9ObYj4n` |
| Batch 03 | 021–030 | `1SXDIHywPYU3yWR94xUeK85AkwhXiT2LY` |
| Batch 04 | 031–040 | `1DIaX2mvIuC2Py8ngNekbn5wy5XfcZ7VF` |
| Batch 05 | 041–050 | `1Qz-PoZy2pO386Yk4Qbtu5vuoCSjtXbXT` |
| Batch 06 | 051–060 | `1x8yZYuNMMPkK_ZGUA3t9un6vemfeNQkx` |
| Batch 07 | 061–070 | `1tC0XOpRG8XJUp5y_e1xs__xJoSS84vmD` |

## Working rule

1. Generate up to ten masters.
2. Upload that batch to its Drive folder and confirm each file landed.
3. Delete the local masters only after the upload is confirmed.
4. Derive that batch's plates into `art_dev/plates/` when the local master still exists.
5. Keep the workspace flat: no master set, no plate set, no rendered segments that
   have already been delivered.

Masters are 1376×768 JPEG at roughly 200 KB, so a full batch of ten is about 2 MB
and the entire seventy-master set is about 14 MB. The workspace cost of holding them
is trivial; the real space is in plates (about 104 MB) and render segments
(about 840 MB), which is why those two are the ones to keep moving.

## Reconciliation after the art-world audit (2026-11-20)

The audit replaced or re-authored 47 masters. Drive still held the pre-audit
versions of 36 of them, so the folder contents no longer matched the set that
actually built the plates. Both sides were brought back into agreement:

- **Uploaded 36 current masters** — 001, 004, 006, 007, 009, 010, 012, 013, 014,
  015, 016, 017, 019, 020, 021, 024, 025, 029, 031, 033, 035, 036, 037, 038, 039,
  041, 042, 043, 048, 052, 053, 054, 058, 061, 062, 065.
- **Trashed 36 superseded copies** — the same numbers, plus duplicate entries that
  had accumulated under 032, 042, 044, 051, 059 and 062.
- **Verified:** exactly one `NNN_master.jpg` per scene, 70 files, and every size
  matches the local master byte count. 34 masters already matched and were left
  untouched.

One stray file, `ARAL_300_Final_Orbital_Pullback_..._Closing_Master_Shot.jpg`,
belongs to episode 01 and happens to match the `_master.jpg` search; it is not
part of this set.

Rule going forward: a regenerated master is uploaded in the same turn it is made,
and the copy it replaces is trashed then — not left for a later reconciliation.
