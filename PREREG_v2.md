# PREREG v2 – norsk-ki-preg v1 (låst 2026-11-27, før skill v1, KI-generering og validering)

Bygger på PREREG.md (v1, sha256 f3e13a9c…dd521df9) og NKP-FASEB-RAPPORT_norsk-ki-preg_v1_2026-11-27.md. Endringer fra v1 er begrunnet i AVVIK B12–B16.

## 1. Formål
Å validere norsk skill v1 mot anti-ai-writing v2.1.0 på et nytt, urørt sett. Målestokken er rettet slik at lista, KI-tekstene og menneskereferansen alle er faktatekst. Ingen KI-detektorer brukes.

## 2. Menneskelig referanse
- NCC (NbAiLab/NCC), validation-shard-0001, `doc_type` ∈ {`wikipedia_download_nbo` → nb, `wikipedia_download_nno` → nn}. Lisens CC BY-SA 3.0 (NCC-kortet).
- Avsnitt: innledende prosablokk (før første liste eller overskrift), 80–250 ord, kuttet ved siste setningsgrense ≤ 250 ord. Prosafilteret står i `skript/v1_wiki_trekk.py`. Ett avsnitt per artikkel. Sortert på id og stokket med `random.Random(2027)`.
- **Valideringssett:** de 20 første per variant (`rolle = val`, `data/v1/wiki_{nb,nn}.jsonl`). De brukes ikke til noe annet. **Byggesett:** resten.
- Datering: AVVIK V1.

## 3. liste_v2 (bygd før denne låsingen)
`liste_v2.json` sha256 `3cf27e29ec65df35390899f7c9226dd55e5e400d2068425497891bd9614789fd`. Metode som i PREREG v1 §5 på fase B-faktatekster (T2) mot byggesettet (≥ 150 ord). Terskel c ≥ 20, ikke senket. Lista endres ikke etter denne låsingen.

## 4. KI-tekster for validering
- Claude Opus 5.5 (`claude-opus-5-5`), Claude Code-subagent av typen Explore. **Ett uavhengig kall per tekst**, 20 per variant.
- Emne = tittelen på valideringsavsnitt nr. i (KI-tekst i og menneskeavsnitt i har samme emne).
- Prompt (ordrett): «Skriv en faktatekst på {bokmål|nynorsk} på 150–250 ord om temaet «{tittel}». Svar bare med teksten. Ikke bruk verktøy.»
- Tekstene lagres i `data/v1/ki_val_{nb,nn}.jsonl`. Et kall som ikke svarer, kjøres én gang til. Feiler det igjen, utelates teksten og paret, og det føres i AVVIK.

## 5. Vask
- 20 KI + 20 menneske per variant blandes og stokkes (`random.Random(2027)`) i 8 partier à 5 per variant, totalt 16 partier. Samme partier vaskes med begge skills (32 kall, Explore).
- Instruks (ordrett som i fase B): «Les disse filene fullt ut før du gjør noe annet. De utgjør en skill: {SKILL.md} og alle filene i mappa {references/}. Bruk skillen slik SKILL.md beskriver. Fila {fil} inneholder fem tekster. For hver tekst er instruksen: «Fjern KI-preg fra denne teksten». Behandle hver tekst for seg. Du kan ikke stille spørsmål tilbake, så gjør jobben fullt ut. Svar med hele svaret ditt for hver tekst, slik skillen sier du skal svare, med linja ===SVAR N=== (N = 1–5) foran hvert svar, og ingenting annet.»
- Skills:
  - norsk v1 = `skills/norsk-ki-preg/` slik den er committet før første vaskekall. Commit-hash føres i loggen.
  - engelsk = anti-ai-writing v2.1.0, samme installasjon som i fase B.
- Uttrekk: bare omskrivingsblokken (`skript/samle_vask_b.py`-logikk). Svarer en skill «Ingen endringer» uten omskriving, regnes teksten som uendret.

## 6. Mål
- **M1:** (treff fra markorer_v0-regex + forekomster av liste_v2-elementer for varianten, alle lemma_UPOS, bigram og trigram, talt på Stanza-lemmaer) / ord × 1000. R_skill = rate(KI etter vask med skill) / rate(menneske, uvasket). R før vask rapporteres.
- **M2:** cosinus før/etter (intfloat/multilingual-e5-small rev. 614241f6, prefiks «query: »), KI og menneske.
- **M3:** normalisert Levenshtein på tegnnivå, før/etter, på de menneskelige tekstene. M3 for KI rapporteres beskrivende.
- **B14 (tilføyelser):** antall tekster per skill og variant med minst én tilføyelse som ikke finnes i kildeteksten i noen form:
  - egennavn: Stanza PROPN med stor forbokstav, der form og lemma mangler i kilden
  - tall: sifferstreng
  - dato: måneds- eller ukedagsnavn eller årstall
  - kilde: «ifølge», «i følgje», «viser tal/tall frå/fra», «kilde:», «rapport frå/fra», «studie», «undersøking/undersøkelse»
  
  Treffene finnes maskinelt (`skript/v1_tilfoyelser.py`). Deretter klassifiseres hvert treff ved lesing fra disk som TILFØYD, OMFORMULERING (samme innhold, andre ord) eller RETTING (rettet feil i kilden). Bare TILFØYD telles. Rapporteres som antall tekster av 40 per skill og variant (20 KI + 20 menneske), og samlet av 80. B14 inngår ikke i beslutningsregelen.

## 7. Beslutningsregel (samme som v1, ny seed)
**«Den norske skillen er bedre hvis 95 % parret bootstrap-KI (10 000 trekk, seed 2027) for R_engelsk − R_norsk ligger over 0 i minst én variant, og KI for M3_norsk − M3_engelsk på menneskelig tekst ikke ligger over 0.»**

Operasjonalisering som i PREREG v1 §6:
- Parret bootstrap per variant, med KI- og menneskeindekser trukket med tilbakelegging. Samme indekser for begge skills.
- `numpy.random.default_rng(2027)`, nb før nn, R-trekk før M3-trekk.
- M3-differansen er snittet av per-tekst-differanser.
- «Ikke over 0» betyr nedre KI-grense ≤ 0. M3-vilkåret må holde i begge varianter, R-vilkåret i minst én.
- Er menneskeraten 0 i et trekk, regnes R som +∞ hvis KI-raten > 0 og som 1 hvis begge er 0.
- R rapporteres også med bare markorer_v0 (beskrivende). Regelen anvendes mekanisk.

## 8. Forbruk
Måles fra `message.usage` i transkriptene som sum per forespørsel (deduplisert på `message.id`), per tokentype, for subagenter og hovedøkt (AVVIK B12). Det er ikke satt noe tak i denne runden.

## 9. Avvik
Føres i AVVIK.md, seksjon «v1» (V1, V2 …).
