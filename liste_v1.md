# liste_v1 – målt KI-overbruk i norsk (bokmål og nynorsk)

Versjon v1, 27.11.2026. Bygd etter PREREG.md §5 (sha256 f3e13a9c…). Status: **foreløpig, målt på avisfortsettelser.** Lista gjelder én sjanger (NB-aviser), to modeller (Claude Opus 5.5 og NorMistral-7B) og små utvalg (240 og 185 par). Den er ikke en generell liste over norsk KI-stil.

## Slik er lista laget

- Oppgave: T1, fortsettelse av en avisavsnitt-halvdel. Menneskereferansen er den ekte andre halvdelen.
- Mål: LPR = ln(p_KI/p_M), der p er andelen tekster der elementet forekommer, med Jeffreys-glatting (c+0,5)/(n+1).
- Inntak: LPR ≥ ln 2 (minst dobbelt så vanlig hos KI) og c_KI + c_M ≥ 20. Egennavn og tall er utelatt.
- «Samsvar» betyr at elementet passerer for både Claude og NorMistral. Det er de sikreste elementene.

## Forbehold

1. Lista blander sjangertrekk med KI-trekk. Avisfortsettelser fra KI har mer sitatramme («sier han», «fortelle at») og mer generelt ordforråd enn OCR-avisene, som er mer stedsbundne og har flere tall og navn.
2. Nynorskreferansen er mest fra 1990–1994 (AVVIK B8). Elementer som `òg`, `bli` og `att` speiler trolig normskifte (moderne nynorsk mot eldre `og`/`verte`/`atter`), ikke KI-preg.
3. Lista sier at et ord brukes oftere av KI enn i referansen. Den sier ikke at ordet er feil eller dårlig norsk.

## Bokmål

Inntatt: 76 lemmaer, 52 bigram og 7 trigram. Samsvar i begge modeller: 5 lemmaer og 2 bigram.

**Samsvar (begge modeller):** `holde_VERB`, `sted_NOUN`, `ung_ADJ`, `tidlig_ADJ`, `lag_NOUN`, `å ta`, `å bli`

**Topp 30 lemmaer, Claude (c_KI/c_M, LPR):**

| # | lemma | c_KI | c_M | LPR | Δ-prevalens | samsvar |
|---|---|---|---|---|---|---|
| 1 | før_SCONJ | 29 | 2 | 2.468 | 0.1125 |  |
| 2 | plan_NOUN | 18 | 2 | 2.001 | 0.0667 |  |
| 3 | selv_ADV | 18 | 2 | 2.001 | 0.0667 |  |
| 4 | handle_VERB | 21 | 4 | 1.564 | 0.0708 |  |
| 5 | holde_VERB | 21 | 4 | 1.564 | 0.0708 | ✓ |
| 6 | allerede_ADV | 32 | 7 | 1.466 | 0.1042 |  |
| 7 | trener_NOUN | 18 | 4 | 1.414 | 0.0583 |  |
| 8 | neste_DET | 38 | 9 | 1.399 | 0.1208 |  |
| 9 | tur_NOUN | 17 | 4 | 1.358 | 0.0542 |  |
| 10 | ung_ADJ | 23 | 6 | 1.285 | 0.0708 | ✓ |
| 11 | be_VERB | 17 | 5 | 1.157 | 0.05 |  |
| 12 | politi_NOUN | 20 | 6 | 1.149 | 0.0583 |  |
| 13 | hver_DET | 27 | 9 | 1.063 | 0.075 |  |
| 14 | arbeid_NOUN | 15 | 5 | 1.036 | 0.0417 |  |
| 15 | likevel_ADV | 26 | 9 | 1.026 | 0.0708 |  |
| 16 | skole_NOUN | 23 | 8 | 1.017 | 0.0625 |  |
| 17 | mene_VERB | 53 | 19 | 1.009 | 0.1417 |  |
| 18 | egen_DET | 20 | 7 | 1.006 | 0.0542 |  |
| 19 | lag_NOUN | 17 | 6 | 0.99 | 0.0458 | ✓ |
| 20 | kommune_NOUN | 41 | 15 | 0.985 | 0.1083 |  |
| 21 | gjennom_ADP | 32 | 12 | 0.956 | 0.0833 |  |
| 22 | fortelle_VERB | 37 | 14 | 0.95 | 0.0958 |  |
| 23 | barn_NOUN | 21 | 8 | 0.928 | 0.0542 |  |
| 24 | før_ADP | 25 | 10 | 0.887 | 0.0625 |  |
| 25 | penge_NOUN | 20 | 8 | 0.88 | 0.05 |  |
| 26 | mange_ADJ | 120 | 50 | 0.87 | 0.2917 |  |
| 27 | plass_NOUN | 15 | 6 | 0.869 | 0.0375 |  |
| 28 | sted_NOUN | 15 | 6 | 0.869 | 0.0375 | ✓ |
| 29 | mål_NOUN | 15 | 6 | 0.869 | 0.0375 |  |
| 30 | derfor_ADV | 28 | 12 | 0.824 | 0.0667 |  |

**Bigram, Claude:** `mange av` 22/2; `og mange` 18/2; `fortelle at` 25/4; `gjøre den` 16/4; `å ta` 16/4; `si hun` 28/8; `være å` 16/5; `å bli` 16/5; `i mange` 15/5; `om å` 24/10; `og at` 39/17; `og en` 15/7

**Fraser (Antislop, overflate, Claude T1):** «han forteller at» 9/0; «mener det er» 8/0; «hun forteller at» 7/0; «ta vare på» 7/0; «han understreker at» 6/0; «målet er å» 6/0; «regner med at» 5/0; «på alvor og» 5/0; «sier en av» 5/0; «mange av dem» 5/0; «har allerede fått» 5/0; «det handler om» 7/1

## Nynorsk

Inntatt: 44 lemmaer, 19 bigram og 0 trigram. Samsvar i begge modeller: 5 lemmaer og 0 bigram.

**Samsvar (begge modeller):** `òg_ADV`, `bli_VERB`, `stad_NOUN`, `gje_VERB`, `kommune_NOUN`

**Topp 30 lemmaer, Claude (c_KI/c_M, LPR):**

| # | lemma | c_KI | c_M | LPR | Δ-prevalens | samsvar |
|---|---|---|---|---|---|---|
| 1 | òg_ADV | 32 | 0 | 4.174 | 0.173 | ✓ |
| 2 | neste_DET | 24 | 2 | 2.282 | 0.1189 |  |
| 3 | håpe_VERB | 20 | 2 | 2.104 | 0.0973 |  |
| 4 | bli_VERB | 37 | 7 | 1.609 | 0.1622 | ✓ |
| 5 | att_ADV | 41 | 9 | 1.474 | 0.173 |  |
| 6 | ung_ADJ | 21 | 5 | 1.363 | 0.0865 |  |
| 7 | eigen_DET | 17 | 4 | 1.358 | 0.0703 |  |
| 8 | sitje_VERB | 16 | 4 | 1.299 | 0.0649 |  |
| 9 | stad_NOUN | 26 | 8 | 1.137 | 0.0973 | ✓ |
| 10 | halde_VERB | 43 | 14 | 1.099 | 0.1568 |  |
| 11 | vente_VERB | 22 | 7 | 1.099 | 0.0811 |  |
| 12 | fortelje_VERB | 33 | 11 | 1.069 | 0.1189 |  |
| 13 | vite_VERB | 24 | 8 | 1.059 | 0.0865 |  |
| 14 | kva_PRON | 32 | 12 | 0.956 | 0.1081 |  |
| 15 | mange_ADJ | 111 | 43 | 0.941 | 0.3676 |  |
| 16 | meine_VERB | 51 | 20 | 0.921 | 0.1676 |  |
| 17 | stå_VERB | 48 | 19 | 0.911 | 0.1568 |  |
| 18 | sak_NOUN | 33 | 13 | 0.909 | 0.1081 |  |
| 19 | lite_ADJ | 15 | 6 | 0.869 | 0.0486 |  |
| 20 | før_ADP | 17 | 7 | 0.847 | 0.0541 |  |
| 21 | kommune_NOUN | 31 | 13 | 0.847 | 0.0973 | ✓ |
| 22 | veg_NOUN | 26 | 11 | 0.835 | 0.0811 |  |
| 23 | framleis_ADV | 19 | 8 | 0.83 | 0.0595 |  |
| 24 | skrive_VERB | 14 | 6 | 0.802 | 0.0432 |  |
| 25 | politi_NOUN | 14 | 6 | 0.802 | 0.0432 |  |
| 26 | bu_VERB | 14 | 6 | 0.802 | 0.0432 |  |
| 27 | god_ADJ | 74 | 33 | 0.799 | 0.2216 |  |
| 28 | folk_NOUN | 38 | 17 | 0.788 | 0.1135 |  |
| 29 | gje_VERB | 26 | 12 | 0.751 | 0.0757 | ✓ |
| 30 | både_CCONJ | 30 | 14 | 0.744 | 0.0865 |  |

**Bigram, Claude:** `seie han` 30/3; `mange av` 27/4; `og at` 27/4; `og det` 27/8; `han meine` 15/5; `om å` 25/10; `og ein` 15/7; `slik at` 16/9; `med ein` 14/8; `vere ikkje` 20/12; `av dei` 24/15; `på at` 16/10

**Fraser (Antislop, overflate, Claude T1):** «for å finne» 5/0; «kanskje er det» 5/0; «det viktigaste er» 5/0; «då er det» 7/1; «peikar på at» 5/1; «og det er» 6/2; «i løpet av» 8/3; «dei som har» 5/2; «det er ikkje» 9/5; «at det er» 10/6; «men det er» 8/5; «i alle fall» 5/4

## Språkrådets markører (beholdt fra markorer_v0, med kilde)

Kilde: Språkrådet (2025), *Rapport fra test av språkroboter*, s. 10 og 14–15. Røyktesten fant 0 treff for disse i avisfortsettelser, men de beholdes fordi de er dokumentert i sakprosa.

- `komplekst_og_viktig` (stående frase, s. 14): «Komplekst og viktig» og lignende er standardfraser som går igjen i de fleste tekstene.
- `viktig_komponent` (stående frase, s. 15): «Viktig komponent», «innebærer» og «dette kan inkludere» er standardformuleringer
- `innebærer` (stående frase, s. 15): «Viktig komponent», «innebærer» og «dette kan inkludere» er standardformuleringer
- `dette_kan_inkludere` (stående frase, s. 15): «dette kan inkludere» er standardformuleringer
- `dynamisk_felt` (stående frase, s. 15): «Fiskeripolitikk er et dynamisk felt som krever kontinuerlig tilpasning og innovasjon.» … ordgyting
- `kontinuerlig_tilpasning` (stående frase, s. 15): «…krever kontinuerlig tilpasning og innovasjon.»
- `fleksibel_tilpasningsdyktig` (stående frase, s. 15): standardformuleringen «fleksibel og tilpasningsdyktig tilnærming» notert som et ordgytingsproblem
- `aspekt` (stående frase, s. 15): «aspektene» og «kompleksiteten» i siste setning, som går igjen i mange tekster
- `kompleksitet` (stående frase, s. 15): «aspektene» og «kompleksiteten» … går igjen i mange tekster
- `komplekst_felt` (stående frase, s. 15): «I sammendrag er landbrukspolitikk et komplekst felt som krever et balansert syn …»
- `balansert` (stående frase, s. 14): «Norge inntok en forsiktig og balansert linje» (s. 14); «et balansert syn» (s. 15)
- `balansegang` (stående frase, s. 15): «Samlet sett er fiskeripolitikk en balansegang mellom ulike hensyn og interesser.»
- `skjæringspunkt` (stående frase, s. 14): «Det er nettopp i skjæringspunktet mellom disse ulike målene at …»
- `dypt_forankret` (stående frase, s. 15): «Alt i alt er Norges forhold til NATO dypt forankret i landets historie …»
- `ikke_bare_ogsaa` (stående frase, s. 15): «Fiskerinæringen er ikke bare en økonomisk aktivitet; den er også en kulturell bærebjelke …»
- `alt_i_alt` (avslutningsformel, s. 15): Oppsummeringsformuleringen «alt i alt … forankret» er registrert som feil.
- `samlet_sett` (avslutningsformel, s. 15): Oppsummeringsformuleringen «samlet sett … balansegang» er notert som en tekstfeil
- `i_sammendrag` (avslutningsformel, s. 15): oppsummeringsformuleringen «[er] i sammendrag et komplekst felt» notert som feil
- `gjore_en_forskjell` (kalk, s. 10): gjøre en forskjell (av engelsk make a difference)
- `fanget_oyet` (kalk, s. 10): plutselig fanget øyet hans noe (ChatGPT)
- `dypt_pust` (kalk, s. 10): ho tok eit djupt pust (Copilot)
- `tilfreds_med_aa` (kalk, s. 10): for no var han tilfreds med å vere i byen (Copilot)
- `som_sine_egne_lommer` (kalk, s. 10): begge kjente den [skogen] som sine egne lommer (Le Chat)
- `med_en_x_stemme` (kalk, s. 10): sa hun med en stolt stemme (Le Chat)
- `aktorene_involvert` (kalk, s. 10): de ulike aktørene involvert (Le Chat)
- `ut_av_kontroll` (kalk, s. 10): en kveld som hadde gått fullstendig ut av kontroll (NorMistral)
- `ny_start` (kalk, s. 10): en kopp [kaffe] som kunne tilby henne en ny start (ChatGPT)

## Strukturmarkører

- `tankestrek_uten_mellomrom`: tankestrek uten mellomrom (—) (Norsk tankestrek med mellomrom ( – / — ) telles ikke)
- `title_case_overskrift`: store forbokstaver i overskrifter etter engelsk mønster (flagg uten i: egen linje, ≥3 ord med stor forbokstav, ingen sluttpunktum)
- `ikke_x_men_y`: «ikke X, men Y»
- `tredelt_oppramsing`: tredelte oppramsinger («A, B og C» med 1–3 ord per ledd)
- `punktliste_fet_tittel`: punktlister med fete titler
