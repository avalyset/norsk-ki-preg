# NKP-FASEB-DEL1 – norsk-ki-preg (2026-11-24)

DEL 1 er ferdig. DEL 2 starter først på «kjør del 2».

## Kallmekanisme
`claude -p` kunne ikke måles, fordi CLI-en ikke er innlogget (`loggedIn: false`) og `--bare` krever API-nøkkel (AVVIK B1). Målt: general-purpose-subagent 82 740 tokens per 5 tekster (16,5k per tekst), **Explore-subagent 53 557 per 5 tekster (10,7k per tekst) → valgt**. Svarene hentes fra transkriptet med skript.

## Anslag DEL 2
≈ 10,3M tokens (145 kall), mot taket på 12M. Ingen kutt planlagt. Kontrollpunkt etter 10 kall (> 62k per kall → fritekst kuttes til 25). Se FORBRUK.md.

## PREREG
`PREREG.md` sha256 `f3e13a9cc266c2970ee9c3f4cf694e71c192c8fd38d7dacb1ab47398dd521df9`, commit 0e29caf. OTS: `PREREG.md.ots` (commit ce2df09), oppgradert 27.11 med Bitcoin-attestasjoner fra 3 kalendere (fullstendig stempel; lokal `ots verify` krever egen Bitcoin-node).

## Datautvalg
| Variant | Kilde | År | Kandidater | Utvalg |
|---|---|---|---|---|
| nb | NB-aviser (CC0), validering | 2000–2018 | 473 | 20 val-menneske, 20 val-emner, 240 par, 50 emner |
| nn | NB-aviser 260 + bøker 15 (CC0), train-shard 0001–0008 | 1990–2019 (181 fra 1990–94) | 362 | 20 / 20 / 185 / 50 |

NLOD utelatt (B3). Nynorsk 2000–2020 ga 0 i validering (B5). Nynorskfilteret er justert etter låsing (B7, avvik). Språkrådet-PDF-en er ute av git-indeksen, men ligger fortsatt i historikken (B2).

## NorMistral-generering
564 tekster (nb 309/310, nn 255/255), 81,7 min serielt, 71 839 tokens inn og 98 191 ut (ollama).

## Engelsk anker (bare formelen, AVVIK B4)
Juzek-repoet har ingen fortsettelser. Vår LPR-kode er kjørt på deres publiserte tellinger (c_H, c_M, n_pairs) og sammenlignet med deres rangering (LAS = Δ-prevalens).

| Liste | n_pairs | Jaccard topp 100 | Spearman (felles topp 100) | Spearman (alle ≥ 20) |
|---|---|---|---|---|
| news/gpt-4.1-mini | 99974 | 0.064 | 0.343 (12 felles) | 0.893 |
| science/claude-3-haiku | 24963 | 0.058 | -0.536 (11 felles) | 0.912 |
| science/gpt-5.2 | 22089 | 0.015 | 1.0 (3 felles) | 0.889 |

Tolkning: rangeringene er samstemte over hele lista (ρ ≈ 0,89–0,91). Toppene er nesten disjunkte. LPR (forhold) løfter sjeldne ord, mens LAS (differanse) løfter hyppige funksjonsord (and, the, this). Topp 100 etter LPR med terskel 20 er støyete i store korpus (for eksempel «p=0.02», «2.41»). I liste_v1 rapporteres derfor Δ-prevalens ved siden av LPR, og funksjonsord vurderes med Δ.

## Topp 20 – liste_v1-nm (NorMistral, T1, lemma; c_KI/c_M = antall tekster; LPR)

**nb** (n = 239/240): uttrykke_VERB 21/0 3.765; ettersom_SCONJ 19/1 2.569; imidlertid_ADV 35/3 2.321; betydelig_ADJ 19/2 2.058; merke_VERB 23/3 1.908; tross_ADP 21/3 1.819; oppleve_VERB 20/3 1.772; sikre_VERB 25/4 1.739; deres_PRON 24/4 1.699; spesiell_ADJ 18/3 1.669; dette_DET 28/5 1.649; disse_DET 33/6 1.644; holde_VERB 22/4 1.614; sted_NOUN 31/6 1.582; mulighet_NOUN 20/4 1.521; bety_VERB 19/4 1.47; denne_DET 80/20 1.372; jobbe_VERB 24/6 1.331; grunn_NOUN 24/6 1.331; tillegg_NOUN 20/5 1.32

**nn** (n = 185/185): òg_ADV 27/0 4.007; ulik_ADJ 20/5 1.316; føre_VERB 21/7 1.053; særleg_ADJ 15/5 1.036; tillegg_NOUN 22/8 0.973; gje_VERB 32/12 0.956; stad_NOUN 21/8 0.928; finne_VERB 28/11 0.908; då_SCONJ 32/13 0.879; døme_NOUN 15/6 0.869; viktig_ADJ 41/18 0.808; denne_DET 79/35 0.806; lag_NOUN 23/10 0.806; bli_VERB 15/7 0.726; gammal_ADJ 21/10 0.717; kommune_NOUN 27/13 0.711; desse_DET 29/14 0.71; den_DET 97/49 0.678; sjølv_DET 14/7 0.659; nokon_DET 31/16 0.647

Fraser (Antislop, nb): «å merke seg» 24/0, «det er imidlertid» 15/0, «for å sikre» 12/0, «dette betyr» 11/0. Fraser (nn): «å merke seg» 11/0, «den opphavlege teksten» 9/0 (metakommentar), «føre til» (bigram 19/2).

Forbehold: nn-referansen er fra 1990-tallet (`òg` 27/0, `verte` underbrukt hos KI = normskifte). Dette er en foreløpig liste for én modell, ikke liste_v1.

