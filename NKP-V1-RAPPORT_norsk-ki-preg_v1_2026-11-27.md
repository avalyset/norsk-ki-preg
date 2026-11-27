# NKP v1 – rapport (norsk-ki-preg v1, 27.11.2026)

**Beslutning etter PREREG v2-regelen: den norske skillen er ikke bedre.** R-vilkåret holder i ingen variant, M3-vilkåret holder i begge. Skill v1 endrer menneskeskrevet tekst svært lite (median M3 0,002–0,003 mot 0,27–0,34 for anti-ai-writing) og legger ikke til noe innhold (0 av 80 tekster mot 4 av 80), men senker ikke markørraten i KI-tekst mer enn anti-ai-writing.

## 1. PREREG v2

`PREREG_v2.md` sha256 `1e810888865cbdd66761dce6db88178f9374a1c5ee8dda3e1f0f694e4633000c`, låst 27.11 i commit 5793a12 før skill v1, KI-generering og validering. OpenTimestamps: `PREREG_v2.md.ots` (commit 9437e54). Stemplet er sendt til tre kalendere og venter på Bitcoin-attestasjon (`ots upgrade` gjenstår). Skill v1 ble committet før første vaskekall (a43d89d). `liste_v2.json` sha256 `3cf27e29ec65df35390899f7c9226dd55e5e400d2068425497891bd9614789fd`.

## 2. Menneskelig referanse: dato og lisens

Kilde: NCC (NbAiLab/NCC), validation-shard-0001, `wikipedia_download_nbo` og `wikipedia_download_nno`. Lisensen står i NCC-kortet (`kilder/ncc/NCC_README.md`), ordrett: «| Wikipedia | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) |».

Dato: kortet oppgir ikke når Wikipedia-dumpen ble tatt. Det står bare «Build date original corpus: 21012022» og «Build data revised corpus: 10032025», og `publish_year` er 2021 for alle Wikipedia-dokumenter («When year is undetermined it is set to 2021»). Dumpen er derfor datert ut fra innholdet (AVVIK V1). Daterte omtaler av 2021 stopper i juli og august 2021. Omtaler av 2022 gjelder planlagte hendelser. Det er 0 treff på regjeringen Støre (14.10.2021), invasjonen av Ukraina, Elizabeth IIs død og ChatGPT. Vurdering: sommeren 2021, før 30.11.2022. **Kortet dokumenterer ikke datoen. Datoen er dokumentert fra innholdet.**

Utvalg (seed 2027, ett avsnitt per artikkel, 80–250 ord, prosafilter, AVVIK V2–V3): nb 1435 kandidater (20 til validering, 1415 til bygging), nn 773 (20 / 753).

## 3. liste_v2

KI: T2-faktatekster fra fase B, 35 per modell og variant (Claude Opus 5.5 og NorMistral-7B). Menneske: byggesettet ≥ 150 ord (nb 936, nn 480), AVVIK V4. Telleterskel c ≥ 20, ikke senket.

| Variant | Lemma | Bigram | Trigram | Samsvar (L/B/T) | Over terskelen før LPR-krav, lemma (Claude / NorMistral) |
|---|---|---|---|---|---|
| nb | 290 | 165 | 20 | 54/32/2 | 764 / 755 |
| nn | 107 | 64 | 4 | 15/14/1 | 388 / 383 |

**Bokmål, topp 30 lemmaer (Claude; c_KI av 35 / c_M av 936; LPR; ✓ = samsvar):** frivillig_ADJ 6/16 2,33 · alvorlig_ADJ 5/15 2,22 · fotball_NOUN 5/15 2,22 · spørsmål_NOUN 5/18 2,05 ✓ · måle_VERB 5/18 2,05 · burde_AUX 5/18 2,05 · hvilken_DET 7/25 2,04 · vanskelig_ADJ 10/36 2,01 · klubb_NOUN 6/25 1,89 · likevel_ADV 8/33 1,89 · gjelde_VERB 8/34 1,86 · lære_VERB 5/22 1,85 ✓ · oppgave_NOUN 4/18 1,84 ✓ · bety_VERB 13/55 1,84 · nivå_NOUN 4/18 1,84 · organisasjon_NOUN 5/24 1,76 ✓ · spiller_NOUN 5/24 1,76 ✓ · noen_PRON 7/33 1,76 ✓ · bane_NOUN 4/20 1,74 ✓ · kommune_NOUN 14/66 1,74 · hvordan_ADV 7/35 1,71 · aktivitet_NOUN 4/21 1,70 · tjeneste_NOUN 6/31 1,68 ✓ · svak_ADJ 3/17 1,65 · full_ADJ 3/17 1,65 · gjerne_ADV 11/57 1,65 · tilbake_ADV 5/28 1,61 · dessuten_ADV 4/23 1,61 · avstand_NOUN 4/23 1,61 · derfor_ADV 19/102 1,60

**Nynorsk, topp 30 lemmaer (Claude; c_KI av 35 / c_M av 480; LPR; ✓ = samsvar):** korleis_ADV 9/15 2,10 · likevel_ADV 15/26 2,06 ✓ · slik_DET 12/21 2,05 · gjerne_ADV 9/17 1,98 · samstundes_ADV 7/14 1,93 · difor_ADV 11/24 1,84 · regel_NOUN 8/18 1,81 · ofte_ADJ 29/68 1,75 · fylke_NOUN 7/17 1,75 ✓ · skule_NOUN 7/17 1,75 ✓ · gjelde_VERB 6/15 1,72 · lenge_ADJ 12/30 1,70 · setje_VERB 8/22 1,62 ✓ · når_SCONJ 20/55 1,60 ✓ · leggje_VERB 11/31 1,58 · klar_ADJ 5/15 1,56 · nok_ADV 6/18 1,55 · følgje_VERB 7/22 1,49 ✓ · då_ADV 13/40 1,49 · ned_ADV 8/25 1,49 · person_NOUN 8/27 1,42 · att_ADV 7/24 1,41 · få_ADJ 5/18 1,38 · fram_ADV 12/42 1,37 ✓ · lett_ADJ 7/26 1,33 · opne_VERB 5/19 1,33 · menneske_NOUN 6/23 1,31 · den_PRON 6/23 1,31 · vise_VERB 12/45 1,30 · døme_NOUN 13/49 1,29

Lista domineres av lim- og registerord (`likevel`, `derfor`/`difor`, `samtidig`/`samstundes`, `gjerne`, `hvordan`/`korleis`, `viktig`, `bidra til`, `for eksempel`) og en del emneord. Full liste med NorMistral-tall og bigram står i `liste_v2.md`.

## 4. Validering (20 KI + 20 menneske per variant, Wikipedia-titler som emner)

KI-tekstene er 40 Claude-faktatekster, ett kall per tekst, median 222 ord. Vask: 16 partier à 5, de samme for begge skills, 32 av 32 kall svarte.

| | nb | nn |
|---|---|---|
| M1 menneske (per 1000 ord) | 110,86 | 90,62 |
| M1 KI før vask (R) | 151,80 (1,37) | 100,93 (1,11) |
| M1 KI etter skill v1 (R_no) | 151,69 (1,368) | 97,97 (1,081) |
| M1 KI etter anti-ai-writing (R_en) | 139,77 (1,261) | 93,00 (1,026) |
| **R_en − R_no, 95 % KI** | **-0,107 [-0,185; -0,039]** | **-0,055 [-0,122; 0,010]** |
| R-vilkår (nedre > 0) | nei | nei |
| M3 menneske, median: v1 / anti-ai-writing | 0,0020 / 0,3388 | 0,0027 / 0,2723 |
| **M3_no − M3_en, 95 % KI** | **-0,3500 [-0,400; -0,302]** | **-0,2511 [-0,307; -0,193]** |
| M3-vilkår (nedre ≤ 0) | ja | ja |
| M2 KI: v1 / anti-ai-writing | 0,9996 / 0,9940 | 0,9986 / 0,9925 |
| M2 menneske: v1 / anti-ai-writing | 0,9995 / 0,9866 | 0,9991 / 0,9898 |
| Uendret av v1: KI / menneske | 15 / 4 av 20 | 10 / 5 av 20 |
| Bare markorer_v0: R_no / R_en (beskrivende) | 2,708 / 2,527 | 1,353 / 1,193 |

Parret bootstrap 10 000 trekk, `default_rng(2027)`, nb før nn, R-trekk før M3-trekk. Alle R-trekk var endelige.

**Regelen anvendt mekanisk:** R-vilkåret holder i ingen variant. I nb ligger KI for R_en − R_no helt under 0, altså i favør av anti-ai-writing. I nn dekker KI 0. M3-vilkåret holder i begge. **Resultat: ikke bedre.**

Målestokken skiller nå KI fra menneske, med R før vask 1,37 (nb) og 1,11 (nn) mot 1,01 og 1,68 i fase B. Feilen ligger i skillen: grunnregelen lot 15 av 20 nb-KI og 10 av 20 nn-KI stå urørt (AVVIK V7). Når den først endrer noe, er det små stryk. anti-ai-writing skriver om alle tekstene og stryker mer, også av ord som teller i M1.

## 5. B14: tilføyelser (maskinelt, deretter klassifisert fra disk)

| Skill | Variant | Tekster | Maskintreff | Omformulering/retting | **Tilføyd** (KI / menneske) |
|---|---|---|---|---|---|
| anti-ai-writing | nb | 40 | 11 | 9 | **3** (1 / 2) |
| anti-ai-writing | nn | 40 | 3 | 2 | **1** (0 / 1) |
| norsk v1 | nb | 40 | 0 | 0 | **0** (0 / 0) |
| norsk v1 | nn | 40 | 0 | 0 | **0** (0 / 0) |

Tilføyelsene fra anti-ai-writing, ordrett:
- nb-ki-0003: «Ifølge Giorgio Vasari gjorde han dette etter å ha hørt noen tilskrive skulpturen en annen kunstner.». «Ifølge en kjent fortelling» → «Ifølge Giorgio Vasari»
- nb-wiki-0003: «Statuen ble bestilt av den franske kardinalen Jean de Bilhères, som var den franske kongens utsending i Roma.». «som representerte Michelangelo i Roma» → «som var den franske kongens utsending i Roma» (endret påstand)
- nn-wiki-0003: «Mykje av den moderne kvantefeltteorien kjem frå han, mellom anna ein variasjonsmetode og rørslelikningane for kvantefelt.». «differensiell form av fysisk integrering» → «ein variasjonsmetode», «kvantekostnadene» → «ladningskvantet» o.a. (påstander byttet ut fra egen kunnskap)
- nb-wiki-0007: «Nederst i bygda ligger Aune, ved grensa mot Surnadal, bare 45 moh., mens grensa mot Orkland lengst oppe i bygda ligger på 280 moh.». «grensa mot Meldal» → «grensa mot Orkland» (endret påstand fra egen kunnskap, ikke fanget maskinelt) Ikke fanget maskinelt.

Skill v1 hadde 0 maskintreff i alle 80 tekstene, og ingen tilføyelse ble funnet ved lesing. Én av de fire anti-ai-writing-tilføyelsene ble funnet utenom maskinen (AVVIK V9).

## 6. Forbruk (sum per forespørsel, deduplisert på message.id)

| Ledd | Kall | Forespørsler | Input | Cache-skriving | Cache-lesing | Output | Sum | Uten cache-lesing |
|---|---|---|---|---|---|---|---|---|
| KI-generering (41 kall  ett per tekst + ett nytt forsøk) | 41 | 41 | 82 | 1 717 671 | 42 940 | 69 005 | 1 829 698 | 1 786 758 |
| Vask  skill v1 | 16 | 54 | 108 | 863 333 | 2 339 397 | 153 932 | 3 356 770 | 1 017 373 |
| Vask  anti-ai-writing | 16 | 62 | 124 | 1 230 381 | 3 218 313 | 390 808 | 4 839 626 | 1 621 313 |
| Hovedøkt (10:03–10:41Z) | 1 | 56 | 114 | 1 125 208 | 18 318 473 | 92 776 | 19 536 571 | 1 218 098 |
| **Alt** | | 213 | 428 | 4 936 593 | 23 919 123 | 706 521 | **29 562 665** | **5 643 542** |

Hvilket mål som tilsvarer forbruk mot Max, kan ikke avgjøres fra loggene (AVVIK B12). Ingen betalte API-er, ingen nøkler, ingen push. Lokalt: Stanza og e5-small på CPU, NCC-strømming (gratis).

## 7. AVVIK (v1, fullstendig i AVVIK.md)

- V1 Wikipedia-datoen står ikke i NCC-kortet. Datert fra innholdet til sommeren 2021. **Godtar ikke Eirik dette, faller v1 bort.**
- V2 «Avsnitt» = innledende prosablokk, fordi NCC-teksten ikke har linjeskift.
- V3 Kjentordterskel 0,70 for nn (simplemma-dekning 74 %).
- V4 liste_v2: 35 KI-tekster per modell (med de tidligere valideringsemnene), byggesettet ≥ 150 ord.
- V5 Rensing av overskriftslinjer og «---»-merknader i KI-tekstene. Holsdagen besvart på andre forsøk.
- V6 Terskelen i grunnregelen er kalibrert på byggesettet (optimistisk).
- V7 Skill v1 lot 25 av 40 KI-tekster stå urørt. Det er hovedgrunnen til at R-vilkåret feiler.
- V8 Rester av markup i valideringsavsnittene gir høyere M3 for anti-ai-writing.
- V9 anti-ai-writing endrer fakta fra egen kunnskap. Én av fire tilføyelser ble funnet utenom maskinen.
- V10 Forbruket i hovedøkta er målt til kjøretidspunktet.

## 8. Hva resultatet betyr

Regelen gir «ikke bedre» for andre gang. Men regelen måler bare én ting, om skillen fjerner flere listeord enn anti-ai-writing. På de to andre målene er skill v1 klart best: den endrer nesten ikke menneskeskrevet tekst (M3 median 0,002–0,003, M2 ≥ 0,998), og den legger aldri til innhold. anti-ai-writing endret fakta i 4 av 80 tekster. Avgjørelsen om hva som skal skje videre, ligger i neste prompt.
