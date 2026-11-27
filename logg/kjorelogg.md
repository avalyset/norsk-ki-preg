# Kjørelogg

- 2026-11-24: BESLUTNING.md sha256 bf251ffbdac445c73c3e3757b9275f1a4953c50edb3d81e4c9ca899e75d671a1 (commit 1e0588e), låst før datauttrekk.
- 2026-11-24: markorer_v0.json sha256 6ddb44480cf93144edf779e5d408b3693b615b9a0969c0ae15638468f31b399c (commit c6010e6), frosset før generering.
- 2026-11-24: PREREG.md sha256 f3e13a9cc266c2970ee9c3f4cf694e71c192c8fd38d7dacb1ab47398dd521df9 (commit a256f18), OTS-stemplet (PREREG.md.ots); oppgradert 2026-11-27 med 3 Bitcoin-attestasjoner.
- 2026-11-27: liste_v1.json sha256 336068c35ca1cfa967cd390e43a451d41f49b21a94743c48760c1ace4c4a298f frosset før valideringsvask (commit 11382ac).

## 2026-11-27 – DEL 2 validering og rapport
- Vask: 32/32 partier, 160 tekster (`data/b_vasket.jsonl`). Tokens: norsk 1 392 109, engelsk 1 965 141 (`subagent_tokens`).
- `skript/maal_val.py` → `resultat/validering.json`: R-vilkår nb nei (−0,076 [−0,135; −0,023]), nn nei (0,014 [−0,056; 0,079]); M3-vilkår ja i begge. **Beslutning: norsk skill ikke bedre.**
- `skript/maal_m2_val.py` → `resultat/validering_m2.json`.
- liste_v1.json sha256 336068c3…4c4a298f uendret.
- Rapport: NKP-FASEB-RAPPORT_norsk-ki-preg_v1_2026-11-27.md.

## 2026-11-27 – B12 og B14 lukket fra disk (ingen modellkall)
- `skript/tokenregnskap.py` → `resultat/tokenregnskap.json` og `resultat/tokenregnskap_hovedokt.json`: 9,6M = siste forespørsel per kall, 39,5M = dobbelttelt linjesum, dedupliserte summer 19,4M (subagenter) og 46,6M (hovedøkt).
- `skript/tilfoyelser.py` + `skript/tilfoyelser_klasse.py` → `resultat/tilfoyelser*.json`: ekte tilføyelser 4/80 (anti-ai-writing) mot 0/80 (norsk v0).

## 2026-11-27 – v1: PREREG v2 låst
- PREREG_v2.md sha256 1e810888865cbdd66761dce6db88178f9374a1c5ee8dda3e1f0f694e4633000c, commit 5793a12, OTS PREREG_v2.md.ots (3 kalendere, venter på Bitcoin-attestasjon).
- liste_v2.json sha256 3cf27e29ec65df35390899f7c9226dd55e5e400d2068425497891bd9614789fd.

## 2026-11-27 – skill v1 committet før vask: a43d89d

## 2026-11-27 – v1 validering og rapport
- Vask 32/32, 160 tekster. Beslutning PREREG v2: ikke bedre (R nb -0,107 [-0,185; -0,039], nn -0,055 [-0,122; 0,010]; M3 ja i begge). B14: v1 0/80, anti-ai-writing 4/80.
- Rapport: NKP-V1-RAPPORT_norsk-ki-preg_v1_2026-11-27.md. OTS for PREREG_v2 venter på Bitcoin.
