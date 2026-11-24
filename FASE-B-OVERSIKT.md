# FASE-B-OVERSIKT (ikke startet)

Utløst av BESLUTNING.md: nynorsk R = 3,70, 95 % KI [1,47; 8,52]. Nedre grense er over 1.

## 1. Utvalgsstørrelse
Mål: minst 200 lemmaer med samlet frekvens ≥ 20 (KI-fortsettelse + ekte fortsettelse). Grunnlaget er delutvalg av de 50 parene per variant (200 trekk per størrelse) med en log-log-tilpasning (`resultat/fase_b_ekstrapolering.json`):

| Variant | Lemmaer ≥ 20 ved 50 par | Eksponent | Par som trengs | Tokens per par |
|---|---|---|---|---|
| nb | 48,0 | 0,93 | **≈ 239** | 130 |
| nn | 56,0 | 1,00 | **≈ 183** | 129 |

Avrundet trengs rundt 250 par per variant, altså 500 i alt (400 nye). Juzeks metode og en stabil LPR-rangering trenger trolig langt mer, ≥ 2 000 par per variant. Tallene over er gulvet for at telleterskelen skal gi mening, ikke et mål for statistisk styrke.

## 2. Forbruk mot Max og maskintid
- Generering kostet 82,7k tokens per subagent med 5 par. Grunnkostnaden dominerer.
  - 400 nye par med 5 per kall: 80 kall ≈ 6,6M tokens.
  - Med 10 per kall: 40 kall ≈ 3,4M (lavere uavhengighet, se AVVIK A9).
  - For 2 000 par per variant: 400 kall ≈ 33M tokens med 10 per kall. Det bør spres over flere dager.
- Vask trengs ikke for å bygge lista, bare til validering etterpå (≈ 134k per 5 tekster).
- Lokal modell (NorMistral-7B Q4): 5,8 s per fortsettelse i snitt. 500 par ≈ 50 min, og 4 000 par ≈ 6,5 t serielt.

## 3. Engelsk anker
Kjør samme løype (deling ved setningsgrense, fortsettelse, LPR med Jeffreys-glatting) på et engelsk utvalg av samme størrelse. Sammenlign topplista med Juzeks publiserte engelske liste (github.com/tjuzek/ai-34-languages, MIT-0/CC0), for eksempel med overlapp@50 og Spearman på felles lemmaer. Det viser om pipelinen gjenskaper et kjent resultat før den norske lista tas i bruk. Ikke hentet eller kjørt i fase A.

## 4. Lisenssjekk for en avledet liste
- NCC-kildene i utvalget: NB-aviser og -bøker er CC0, uten krav.
- maalfrid_*/government/parliament er NLOD 2.0, med krav om kildeangivelse. Disse falt ut i fase A (AVVIK A2) og bør tas med i fase B. Årsfilteret må da revurderes, fordi publish_year = 2021 betyr «ukjent».
- Claude-utdata: brukeren eier dem etter Anthropics vilkår, og det er ingen hindring for å publisere en avledet frekvensliste.
- NorMistral (ltg): Apache-2.0.
- anti-ai-writing: MIT. Sitater fra Språkrådet-rapporten er korte og med kildeangivelse, innenfor sitatretten (åndsverkloven § 29).
- Ikke bruk: newspapers_online_* (CC BY-NC) og opensubtitles.
- Anbefalt lisens for lista: CC0 (data) + Apache-2.0 (kode).

## 5. Preregistrering
Prereg på Zenodo før noen generering: hypoteser, BESLUTNING/terskler, markørdefinisjoner, utvalg (seed), modeller og versjoner, og telle- og glattingsregler. Stemple prereg-PDF og sha256 for skriptene med OpenTimestamps. Start generering først når OTS-beviset er bekreftet (Bitcoin-blokk).

## 6. Funn fra fase A som bør styre fase B
- Hele R-utslaget for nynorsk kommer fra strukturmarkørene «A, B og C» og «ikke X, men Y». Språkrådets frase- og kalkmarkører hadde 0 treff i vasket Claude-tekst i begge varianter (`resultat/folsomhet.json`). Fase B bør måle kandidater fra data (M4) og ikke bare bruke Språkrådets eksempelliste.
- Vasken endret nesten ikke markørraten. For nn på samme 20 tekster: R før vask 3,82, etter vask 3,70. 8 av 20 nn-tekster ble returnert uendret. Skillens engelske regel om «rule of three» ble ikke brukt på norsk.
