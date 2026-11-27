# liste_v2 – målt KI-overbruk i norsk faktatekst (bokmål og nynorsk)

Versjon v2, 27.11.2026. `liste_v2.json` sha256 `3cf27e29ec65df35390899f7c9226dd55e5e400d2068425497891bd9614789fd`.

## Slik er lista laget

- KI-tekster: faktatekstene (T2) fra fase B, 35 per modell og variant (25 fritekst-emner + 10 tidligere valideringsemner), fra Claude Opus 5.5 og NorMistral-7B. Ingen ny generering.
- Menneskereferanse: innledende prosaavsnitt fra NCC `wikipedia_download_nbo`/`_nno` (CC BY-SA 3.0), byggesettet, bare avsnitt på minst 150 ord for å matche KI-lengden (nb 936, nn 480). De 20 valideringsavsnittene per variant er ikke brukt.
- Mål som i PREREG v1 §5: Stanza-lemma med UPOS, lemma-bi- og trigram innen setning, prevalens over tekster med Jeffreys-glatting, LPR = ln(p_KI/p_M). Inntak: LPR ≥ ln 2 og c_KI + c_M ≥ 20 for minst én modell. Egennavn og tall er utelatt. «Samsvar» = passerer for begge modeller.
- Telleterskelen ble ikke senket (≥ 50 elementer per variant ved 20).

## Antall elementer

| Variant | Lemma | Bigram | Trigram | Samsvar (lemma/bigram/trigram) | Over terskelen før LPR-krav (Claude / NorMistral, lemma) |
|---|---|---|---|---|---|
| nb | 290 | 165 | 20 | 54/32/2 | 764 / 755 |
| nn | 107 | 64 | 4 | 15/14/1 | 388 / 383 |

## Forbehold

1. Små KI-utvalg (35 per modell). En prevalens på 5 av 35 er nok for inntak når elementet er sjeldent i Wikipedia.
2. Emnene i KI-tekstene kommer fra avisavsnitt, mens Wikipedia dekker andre emner. Emneord (`fotball`, `kommune`, `klubb`, `fylke`, `skule`) er derfor med. De er ikke stiltrekk, og skillen behandler dem bare som del av en opphopning.
3. Lista sier at et ord er vanligere i KI-faktatekst enn i Wikipedia-prosa. Den sier ikke at ordet er feil.

## Bokmål

**Samsvar (begge modeller), lemma:** `påvirke_VERB`, `spørsmål_NOUN`, `resultat_NOUN`, `mulighet_NOUN`, `utvikling_NOUN`, `lære_VERB`, `oppgave_NOUN`, `hendelse_NOUN`, `organisasjon_NOUN`, `spiller_NOUN`, `noen_PRON`, `bidra_VERB`, `bane_NOUN`, `tjeneste_NOUN`, `viktig_ADJ`, `selskap_NOUN`, `rett_NOUN`, `innsats_NOUN`, `miljø_NOUN`, `trenge_VERB`, `samfunn_NOUN`, `hvis_SCONJ`, `ansvar_NOUN`, `eksempel_NOUN`, `måte_NOUN`, `interesse_NOUN`, `hjelpe_VERB`, `nå_VERB`, `forskjell_NOUN`, `avhengig_ADJ`, `oppleve_VERB`, `rolle_NOUN`, `økonomisk_ADJ`, `samling_NOUN`, `øke_ADJ`, `lokal_ADJ`, `på_ADV`, `møte_VERB`, `søke_VERB`, `politikk_NOUN`, `markere_VERB`, `lag_NOUN`, `fysisk_ADJ`, `fly_NOUN`, `endring_NOUN`, `person_NOUN`, `direkte_ADJ`, `oppstå_VERB`, `hard_ADJ`, `kilde_NOUN`, `måned_NOUN`, `beskrive_VERB`, `formell_ADJ`, `ren_ADJ`

**Samsvar, bigram:** «være viktig», «kunne bli», «bidra til», «den viktig», «de kunne», «og mange», «en viktig», «person som», «til slutt», «gjøre den», «være ofte», «eksempel på», «den kunne», «for mange», «og gi», «for eksempel», «kunne være», «avhengig av», «ansvar for», «og få», «å ta», «bo i», «i stor», «sin egen», «når den», «å gi», «som gjøre», «som ikke», «side av», «at hun», «der den», «som vise»

**Topp 30 lemmaer, Claude** (c = antall tekster av 35 KI / av referansen):

| # | lemma | c_KI | c_M | LPR | Δ-prevalens | samsvar |
|---|---|---|---|---|---|---|
| 1 | frivillig_ADJ | 6 | 16 | 2.328 | 0.1543 |  |
| 2 | alvorlig_ADJ | 5 | 15 | 2.223 | 0.1268 |  |
| 3 | fotball_NOUN | 5 | 15 | 2.223 | 0.1268 |  |
| 4 | spørsmål_NOUN | 5 | 18 | 2.046 | 0.1236 | ✓ |
| 5 | måle_VERB | 5 | 18 | 2.046 | 0.1236 |  |
| 6 | burde_AUX | 5 | 18 | 2.046 | 0.1236 |  |
| 7 | hvilken_DET | 7 | 25 | 2.035 | 0.1733 |  |
| 8 | vanskelig_ADJ | 10 | 36 | 2.013 | 0.2473 |  |
| 9 | klubb_NOUN | 6 | 25 | 1.892 | 0.1447 |  |
| 10 | likevel_ADV | 8 | 33 | 1.888 | 0.1933 |  |
| 11 | gjelde_VERB | 8 | 34 | 1.858 | 0.1922 |  |
| 12 | lære_VERB | 5 | 22 | 1.85 | 0.1194 | ✓ |
| 13 | oppgave_NOUN | 4 | 18 | 1.845 | 0.0951 | ✓ |
| 14 | bety_VERB | 13 | 55 | 1.845 | 0.3127 |  |
| 15 | nivå_NOUN | 4 | 18 | 1.845 | 0.0951 |  |
| 16 | organisasjon_NOUN | 5 | 24 | 1.765 | 0.1172 | ✓ |
| 17 | spiller_NOUN | 5 | 24 | 1.765 | 0.1172 | ✓ |
| 18 | noen_PRON | 7 | 33 | 1.763 | 0.1647 | ✓ |
| 19 | bane_NOUN | 4 | 20 | 1.743 | 0.0929 | ✓ |
| 20 | kommune_NOUN | 14 | 66 | 1.736 | 0.3295 |  |
| 21 | hvordan_ADV | 7 | 35 | 1.705 | 0.1626 |  |
| 22 | aktivitet_NOUN | 4 | 21 | 1.695 | 0.0918 |  |
| 23 | tjeneste_NOUN | 6 | 31 | 1.681 | 0.1383 | ✓ |
| 24 | svak_ADJ | 3 | 17 | 1.65 | 0.0676 |  |
| 25 | full_ADJ | 3 | 17 | 1.65 | 0.0676 |  |
| 26 | gjerne_ADV | 11 | 57 | 1.65 | 0.2534 |  |
| 27 | tilbake_ADV | 5 | 28 | 1.614 | 0.1129 |  |
| 28 | dessuten_ADV | 4 | 23 | 1.606 | 0.0897 |  |
| 29 | avstand_NOUN | 4 | 23 | 1.606 | 0.0897 |  |
| 30 | derfor_ADV | 19 | 102 | 1.6 | 0.4339 |  |

**Topp 30 lemmaer, NorMistral:**

| # | lemma | c_KI | c_M | LPR | samsvar |
|---|---|---|---|---|---|
| 1 | merke_VERB | 15 | 10 | 3.649 |  |
| 2 | situasjon_NOUN | 7 | 13 | 2.671 |  |
| 3 | suksess_NOUN | 6 | 15 | 2.39 |  |
| 4 | påvirke_VERB | 6 | 18 | 2.213 | ✓ |
| 5 | inkludere_VERB | 9 | 32 | 2.029 |  |
| 6 | anerkjenne_VERB | 4 | 16 | 1.96 |  |
| 7 | resultat_NOUN | 6 | 24 | 1.932 | ✓ |
| 8 | personlig_ADJ | 4 | 17 | 1.901 |  |
| 9 | årsak_NOUN | 5 | 21 | 1.896 |  |
| 10 | mulighet_NOUN | 8 | 33 | 1.888 | ✓ |
| 11 | utvikling_NOUN | 7 | 30 | 1.856 | ✓ |
| 12 | spørsmål_NOUN | 4 | 18 | 1.845 | ✓ |
| 13 | hendelse_NOUN | 5 | 23 | 1.807 | ✓ |
| 14 | bidra_VERB | 8 | 38 | 1.749 | ✓ |
| 15 | viktig_ADJ | 22 | 111 | 1.659 | ✓ |
| 16 | du_PRON | 4 | 22 | 1.65 |  |
| 17 | tillate_VERB | 3 | 17 | 1.65 |  |
| 18 | betydelig_ADJ | 8 | 44 | 1.604 |  |
| 19 | referere_VERB | 3 | 18 | 1.594 |  |
| 20 | informasjon_NOUN | 3 | 18 | 1.594 |  |
| 21 | imidlertid_ADV | 13 | 72 | 1.578 |  |
| 22 | innsats_NOUN | 3 | 19 | 1.542 | ✓ |
| 23 | dyp_ADJ | 3 | 19 | 1.542 |  |
| 24 | oppnå_VERB | 5 | 31 | 1.514 |  |
| 25 | miljø_NOUN | 3 | 20 | 1.492 | ✓ |
| 26 | unngå_VERB | 3 | 20 | 1.492 |  |
| 27 | generell_ADJ | 3 | 20 | 1.492 |  |
| 28 | samfunn_NOUN | 5 | 32 | 1.483 | ✓ |
| 29 | alltid_ADV | 4 | 28 | 1.413 |  |
| 30 | måte_NOUN | 8 | 54 | 1.401 | ✓ |

**Topp 20 bigram, Claude:** «vanskelig å» 8/15 (2.658); «og for» 7/22 (2.161); «vise at» 5/17 (2.102); «kunne bli» 5/18 (2.046); «i norsk» 8/30 (1.982); «den gå» 4/17 (1.901); «de kunne» 5/21 (1.896); «og mange» 7/29 (1.89); «en viktig» 7/29 (1.89); «fra annen» 4/20 (1.743); «med annen» 4/20 (1.743); «fordi den» 4/21 (1.695); «være god» 4/21 (1.695); «til slutt» 5/26 (1.687); «gjøre den» 6/31 (1.681); «være ofte» 4/22 (1.65); «kommune i» 5/27 (1.65); «å legge» 3/17 (1.65); «en egen» 4/22 (1.65); «sette i» 4/23 (1.606)

**Fraser (Antislop, Claude, f_KI/f_M):** «det vanlig» 5/3; «gjør det» 6/4; «kan det» 5/4; «derfor er» 5/5; «betyr at» 7/9; «i finnmark» 6/11; «vanskelig å» 8/15; «hvert år» 5/10; «er det vanlig» 5/2

## Nynorsk

**Samsvar (begge modeller), lemma:** `likevel_ADV`, `fylke_NOUN`, `skule_NOUN`, `setje_VERB`, `når_SCONJ`, `følgje_VERB`, `viktig_ADJ`, `fram_ADV`, `vanskeleg_ADJ`, `mål_NOUN`, `historie_NOUN`, `dårleg_ADJ`, `sjå_VERB`, `innbyggjar_NOUN`, `velje_VERB`

**Samsvar, bigram:** «ved å», «som kunne», «slik at», «på å», «ein viktig», «kunne vere», «for ein», «vere ikkje», «vere med», «i dei», «og annan», «dei mykje», «for dei», «som ikkje»

**Topp 30 lemmaer, Claude** (c = antall tekster av 35 KI / av referansen):

| # | lemma | c_KI | c_M | LPR | Δ-prevalens | samsvar |
|---|---|---|---|---|---|---|
| 1 | korleis_ADV | 9 | 15 | 2.103 | 0.2259 |  |
| 2 | likevel_ADV | 15 | 26 | 2.056 | 0.3744 | ✓ |
| 3 | slik_DET | 12 | 21 | 2.05 | 0.2991 |  |
| 4 | gjerne_ADV | 9 | 17 | 1.981 | 0.2217 |  |
| 5 | samstundes_ADV | 7 | 14 | 1.933 | 0.1708 |  |
| 6 | difor_ADV | 11 | 24 | 1.836 | 0.2643 |  |
| 7 | regel_NOUN | 8 | 18 | 1.815 | 0.1911 |  |
| 8 | ofte_ADJ | 29 | 68 | 1.75 | 0.6869 |  |
| 9 | fylke_NOUN | 7 | 17 | 1.745 | 0.1646 | ✓ |
| 10 | skule_NOUN | 7 | 17 | 1.745 | 0.1646 | ✓ |
| 11 | gjelde_VERB | 6 | 15 | 1.723 | 0.1402 |  |
| 12 | lenge_ADJ | 12 | 30 | 1.7 | 0.2804 |  |
| 13 | setje_VERB | 8 | 22 | 1.619 | 0.1827 | ✓ |
| 14 | når_SCONJ | 20 | 55 | 1.596 | 0.4568 | ✓ |
| 15 | leggje_VERB | 11 | 31 | 1.585 | 0.2497 |  |
| 16 | klar_ADJ | 5 | 15 | 1.556 | 0.1116 |  |
| 17 | nok_ADV | 6 | 18 | 1.546 | 0.1339 |  |
| 18 | følgje_VERB | 7 | 22 | 1.494 | 0.1542 | ✓ |
| 19 | då_ADV | 13 | 40 | 1.494 | 0.2881 |  |
| 20 | ned_ADV | 8 | 25 | 1.494 | 0.1765 |  |
| 21 | person_NOUN | 8 | 27 | 1.418 | 0.1723 |  |
| 22 | att_ADV | 7 | 24 | 1.409 | 0.15 |  |
| 23 | få_ADJ | 5 | 18 | 1.379 | 0.1054 |  |
| 24 | fram_ADV | 12 | 42 | 1.369 | 0.2554 | ✓ |
| 25 | lett_ADJ | 7 | 26 | 1.33 | 0.1458 |  |
| 26 | opne_VERB | 5 | 19 | 1.327 | 0.1033 |  |
| 27 | menneske_NOUN | 6 | 23 | 1.307 | 0.1235 |  |
| 28 | den_PRON | 6 | 23 | 1.307 | 0.1235 |  |
| 29 | vise_VERB | 12 | 45 | 1.3 | 0.2491 |  |
| 30 | døme_NOUN | 13 | 49 | 1.293 | 0.2693 |  |

**Topp 30 lemmaer, NorMistral:**

| # | lemma | c_KI | c_M | LPR | samsvar |
|---|---|---|---|---|---|
| 1 | skape_VERB | 8 | 15 | 1.992 |  |
| 2 | rolle_NOUN | 7 | 18 | 1.689 |  |
| 3 | likevel_ADV | 9 | 26 | 1.566 | ✓ |
| 4 | utvikling_NOUN | 5 | 16 | 1.494 |  |
| 5 | offentleg_ADJ | 5 | 16 | 1.494 |  |
| 6 | samfunn_NOUN | 5 | 17 | 1.435 |  |
| 7 | viktig_ADJ | 19 | 65 | 1.381 | ✓ |
| 8 | noko_PRON | 13 | 51 | 1.253 |  |
| 9 | fylke_NOUN | 4 | 17 | 1.234 | ✓ |
| 10 | tillegg_NOUN | 12 | 50 | 1.196 |  |
| 11 | historie_NOUN | 6 | 27 | 1.15 | ✓ |
| 12 | dårleg_ADJ | 4 | 19 | 1.126 | ✓ |
| 13 | tal_NOUN | 4 | 19 | 1.126 |  |
| 14 | deira_PRON | 9 | 43 | 1.071 |  |
| 15 | slutt_NOUN | 8 | 39 | 1.056 |  |
| 16 | brei_ADJ | 5 | 26 | 1.02 |  |
| 17 | skule_NOUN | 3 | 17 | 0.983 | ✓ |
| 18 | vanskeleg_ADJ | 3 | 17 | 0.983 | ✓ |
| 19 | mål_NOUN | 3 | 17 | 0.983 | ✓ |
| 20 | kamp_NOUN | 3 | 17 | 0.983 |  |
| 21 | arbeide_VERB | 6 | 34 | 0.923 |  |
| 22 | føre_VERB | 9 | 52 | 0.883 |  |
| 23 | delta_VERB | 3 | 19 | 0.875 |  |
| 24 | lov_NOUN | 3 | 19 | 0.875 |  |
| 25 | direkte_ADJ | 3 | 20 | 0.825 |  |
| 26 | sjå_VERB | 8 | 50 | 0.81 | ✓ |
| 27 | desse_DET | 6 | 39 | 0.788 |  |
| 28 | tradisjonell_ADJ | 3 | 21 | 0.777 |  |
| 29 | innbyggjar_NOUN | 6 | 41 | 0.738 | ✓ |
| 30 | setje_VERB | 3 | 22 | 0.732 | ✓ |

**Topp 20 bigram, Claude:** «i noreg» 23/44 (1.954); «i mange» 9/22 (1.73); «slik at» 8/20 (1.712); «som kunne» 6/17 (1.602); «ein viktig» 7/25 (1.369); «til døme» 10/36 (1.346); «at ein» 6/24 (1.265); «kunne vere» 6/25 (1.225); «for ein» 6/26 (1.187); «mykje av» 6/26 (1.187); «og mange» 5/22 (1.184); «vere med» 4/18 (1.179); «vere at» 4/18 (1.179); «kunne ein» 4/19 (1.126); «og som» 4/19 (1.126); «i dei» 6/28 (1.114); «i land» 5/25 (1.058); «og annan» 6/30 (1.046); «dei mykje» 4/21 (1.028); «på dei» 3/17 (0.983)

**Fraser (Antislop, Claude, f_KI/f_M):** «i florø» 5/0; «noreg har» 7/1; «ansvaret for» 6/2; «og fjordane» 5/3; «kven som» 5/3; «vart skipa» 5/3; «kan få» 5/4; «som skal» 5/4; «vart skipa i» 5/3

## Språkrådets markører og strukturmarkører

Uendret fra markorer_v0.json. Kilde for gruppe a: Språkrådet (2025), rapporten om KI-generert norsk tekst (sidetall i markorer_v0.json). Gruppe b er strukturmarkører fra fase A.

- `komplekst_og_viktig` (stående frase): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 14
- `viktig_komponent` (stående frase): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 15
- `innebærer` (stående frase): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 15
- `dette_kan_inkludere` (stående frase): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 15
- `dynamisk_felt` (stående frase): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 15
- `kontinuerlig_tilpasning` (stående frase): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 15
- `fleksibel_tilpasningsdyktig` (stående frase): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 15
- `aspekt` (stående frase): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 15
- `kompleksitet` (stående frase): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 15
- `komplekst_felt` (stående frase): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 15
- `balansert` (stående frase): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 14
- `balansegang` (stående frase): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 15
- `skjæringspunkt` (stående frase): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 14
- `dypt_forankret` (stående frase): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 15
- `ikke_bare_ogsaa` (stående frase): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 15
- `alt_i_alt` (avslutningsformel): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 15
- `samlet_sett` (avslutningsformel): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 15
- `i_sammendrag` (avslutningsformel): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 15
- `gjore_en_forskjell` (kalk): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 10
- `fanget_oyet` (kalk): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 10
- `dypt_pust` (kalk): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 10
- `tilfreds_med_aa` (kalk): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 10
- `som_sine_egne_lommer` (kalk): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 10
- `med_en_x_stemme` (kalk): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 10
- `aktorene_involvert` (kalk): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 10
- `ut_av_kontroll` (kalk): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 10
- `ny_start` (kalk): Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f, s. 10
- `tankestrek_uten_mellomrom` (struktur): oppgavespesifikasjon (strukturmarkør)
- `title_case_overskrift` (struktur): oppgavespesifikasjon (strukturmarkør)
- `ikke_x_men_y` (struktur): oppgavespesifikasjon (strukturmarkør)
- `tredelt_oppramsing` (struktur): oppgavespesifikasjon (strukturmarkør)
- `punktliste_fet_tittel` (struktur): oppgavespesifikasjon (strukturmarkør)
