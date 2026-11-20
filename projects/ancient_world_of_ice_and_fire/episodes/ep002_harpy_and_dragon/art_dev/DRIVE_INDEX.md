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

## Round-2 replacement — 2026-11-20

Twenty-nine masters were replaced after the full-size audit (see
`docs/ART_WORLD_AUDIT.md`). Each new file was uploaded and the copy it replaced
trashed in the same pass, so every folder again holds exactly one master per
scene. 070 is the exception: its image is still the pre-repair denarius and
must be re-uploaded when regenerated.

| Scene | New Drive ID                        | Folder |
| ----- | ----------------------------------- | ------ |
| 005   | `1GKDximm_OdfA43fgsoIyWeLp6iToY0ax` | 01     |
| 007   | `1DV9jl8hCkoUnGWw08hjXO7MYm2Eg-h8t` | 01     |
| 009   | `1FEyV0ijF1EL898zIA50UtoThuD-0mOCA` | 01     |
| 010   | `12XNUlmMa9UeBAuN6WpU4HapTs1HB72lF` | 01     |
| 012   | `1kfZH4tFDRQzaSnp63KxoR86wyJsfOtLB` | 02     |
| 015   | `1ezxb-XRzPS7EGVM8_IU1wrbSvMwoL_19` | 02     |
| 016   | `1l2kefnDlWaM50l_pl9k_kT_hh86120F9` | 02     |
| 018   | `1BJtnVAVImZqKc74L6Hn7R5uih9i1FvNV` | 02     |
| 019   | `1fGGRkkktFmVFsE5NuyMq1z4Kys_iCbVs` | 02     |
| 023   | `1E5p-c0kXgz7na4G3lBbMbZU9_TI_FWh7` | 03     |
| 024   | `1bn6sFLzen2pCaw6jebD65GF5Aj7r6AR1` | 03     |
| 028   | `1q-6ZlYvvCse6moEb-33nXxqz-b_h17jq` | 03     |
| 029   | `1AwM64BDjtcI0ajIOfP88LY-RvRr_fv81` | 03     |
| 033   | `1ItWVbAnB-diISdc7FmNIx7IxuGkxrXRH` | 04     |
| 034   | `1vzzlOVbCXU8M09HL3uvNcAg7le0YXSk_` | 04     |
| 035   | `13NLNgB5DMUshmoZAItuTNoXybVU73Uba` | 04     |
| 042   | `1qMl5zGxhwg5ewDH5Y_jrDviFS3t1Zw1L` | 05     |
| 043   | `1pXRz9y5IT0RHDKOB95PdZNGNUbLzsXwk` | 05     |
| 044   | `1r9hQoZKtRZ-X1QU97snXlOdzYCJYKx-c` | 05     |
| 045   | `18UjFxdFCgGmnZHOp-eecRx-dgNIDoQDC` | 05     |
| 049   | `1L6uiVswNV1m6igpdckMUpuTwMPWdoonv` | 05     |
| 050   | `1_SlRnCZo7kLix5RCtI-rv9Yj0axn9okd` | 05     |
| 052   | `120AepTPjv4f8u_b7fCV78UIn1yM9T1Hk` | 06     |
| 055   | `1Ctqi6xNBadvUqKQ4Jt2OtNcKzBbH9rva` | 06     |
| 056   | `1yoxtDJ7CMoC3DvcK3EvHVUB6kIDPswrk` | 06     |
| 058   | `1WB04Y1_dQVD0A3rQqt-rUapYIa4dm9lY` | 06     |
| 065   | `1P8QRxCLtruLqq_pHutXG6ubxbqcPnwig` | 07     |
| 069   | `16VpdE3uR3RqL-I2SwoJhtc8SUIM9Xliy` | 07     |
| 070   | **pending regeneration**            | 07     |
