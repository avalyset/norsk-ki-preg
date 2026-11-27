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
