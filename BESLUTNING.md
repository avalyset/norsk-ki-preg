# BESLUTNING – låst før datauttrekk (2026-11-24)

## Regel (ordrett)

«For hver variant (nb, nn): forholdet R = markørrate i KI-tekst etter vask / markørrate i menneskelig tekst, med 95 % bootstrap-KI (10 000 trekk, seed 2026). Er nedre KI-grense for R over 1 i minst én variant, trengs en målt norsk liste (fase B). Ellers holder dagens skill for norsk.»

## Operasjonalisering (låst sammen med regelen)

1. Markørrate = samlet antall markørtreff / samlet antall ord × 1000, slått sammen over alle tekster i gruppen (poolet rate). Ord = tokens som matcher `\w+` (Unicode) etter NFC.
2. Markører = alle elementer i `markorer_v0.json` (frosset før generering). Hvert treff teller 1.
3. «KI-tekst etter vask» = Claude-fortsettelsene (20 per variant) etter vask med anti-ai-writing v2.1.0. Lokal modell inngår ikke i beslutningen (beskrivende).
4. «Menneskelig tekst» = de ekte andre halvdelene (fasit) av alle 50 avsnitt per variant, uvasket.
5. Bootstrap: i hvert av 10 000 trekk trekkes tekster med tilbakelegging uavhengig i hver gruppe (samme gruppestørrelse), R beregnes som forholdet mellom poolede rater. `numpy.random.default_rng(2026)`, ett felles generatorobjekt, nb før nn. 95 % KI = 2,5- og 97,5-persentil.
6. Er menneskeraten 0 i et trekk og KI-raten > 0, settes R = +∞ for det trekket; er begge 0, R = 1.
7. Fase B trengs hvis nedre KI-grense > 1 for nb ELLER nn. Ellers: dagens skill holder for norsk (på dette markørsettet).
8. Regelen anvendes mekanisk. M2–M4 er beskrivende og påvirker ikke beslutningen.
