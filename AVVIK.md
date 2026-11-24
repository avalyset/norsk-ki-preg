# AVVIK

Avvik fra oppgavebeskrivelsen og kjente begrensninger, i den rekkefølgen de oppsto.

## A1 – NCC-feltnavn
Oppgaven sier `lang`; NCC har `lang_fasttext` (+ `lang_fasttext_conf`). `no` tolkes som bokmål, `nn` som nynorsk. `publish_year` er en streng.

## A2 – NLOD-kildene faller ut av årsfilteret
Alle `maalfrid_*`-dokumenter i validering har `publish_year = 2021` (ukjent år) og faller ut av filteret ≤ 2020. Utvalget består dermed bare av CC0-kildene `newspaper_ocr` og `books` (NB). Wikipedia (CC BY-SA) er ikke på lista over tillatte kilder og er utelatt.

## A3 – Kvalitetsfilter for OCR-tekst (lagt til, ikke i oppgaven)
NB-avisene er OCR. Filteret ble skrevet før noe utvalg ble sett: 80–200 ord, slutter på sluttpunktum, ≥ 4 setninger, ≥ 90 % av alfabetiske ord over 2 tegn kjent i simplemma-ordlista for varianten, ingen orddeling av typen «ord- videre». Filteret skjevvrider mot rent språk og kan underrepresentere eldre rettskrivning (særlig nynorsk før 1938/1959).

## A4 – Nynorsk utvidet til treningssplitten
Validering ga 26 nynorsk-avsnitt som passerte filteret. Uttrekket strømmet videre i `train-shard-0001` og ved behov `-0002` (grense 2 shards), som planen sier. Bokmål kommer bare fra validering.

## A5 – Stanza ikke installert
Stanza og nb/nn-modellene finnes ikke på maskinen. Å laste dem ned ville vært en ekstra modellnedlasting. Lemmatisering i M4 og ordkontroll i A3 bruker derfor `simplemma` (MIT, ordlistebasert, ingen nevral modell). Simplemma er svakere enn Stanza på flertydige former.

## A6 – Setningsmodell allerede lokalt
`intfloat/multilingual-e5-small` (MIT, rev. 614241f6, 471 MB) lå allerede i HF-cachen. Ingen modell ble lastet ned. M2 kjøres i `~/dev/mteb-5657/.venv` (torch + sentence-transformers) for å slippe å installere torch på nytt.

## A7 – Markører: nynorskformer lagt til
Språkrådets eksempler er nesten bare bokmål (vedlegg 1 er «hentet fra tre sakprosatekster på bokmål»). Der det er åpenbart, er nynorskformer lagt inn i samme regex (inneber, samla sett, i samandrag, kontinuerleg, djupt, ikkje berre, gjere ein skilnad). Hver tilpasning står i `merknad` i markorer_v0.json. Bøyingsformer (komplekst/kompleks/komplekse) er tillatt.

## A8 – Språkrådet-PDF i repoet
`kilder/sprakradet_2025.pdf` er lagt i det lokale repoet som revisjonsspor (sha256 73b84a52…). Fjern før eventuell publisering hvis gjenbruksvilkårene er uklare.

## A9 – Delt kontekst i generering (kjent begrensning)
Hver Claude-subagent fikk fem fortsettelsesoppgaver i én fil og skrev alle fem i samme kontekst. Fortsettelsene er dermed ikke helt uavhengige. Subagentene hadde også Claude Code sin systemprompt og verktøy, ikke en ren modellkontekst. Oppgaveteksten var ordrett lik planen. Rammen rundt (filsti og svarformat `===SVAR N===`) var nøytral og nevnte ikke studien.

## A10 – Vask: ingen spørsmål tilbake, overskrifter på norsk
SKILL.md ber Claude spørre skribenten om språket når teksten ikke er på engelsk eller spansk. Subagenten kan ikke spørre, så instruksen fikk tillegget «Du kan ikke stille spørsmål tilbake, så gjør jobben fullt ut». Ellers var instruksen den vanlige: «Fjern KI-preg fra denne teksten». Subagentene skrev seksjonsoverskriftene på norsk og uten `###` (Diagnose / Omskriving / Endringer|Endringar / Merknader|Notater). Uttrekket tar teksten mellom «Omskriving» (eller «Rewrite») og neste kjente overskrift. Alle 60 ble hentet ut. Råsvarene ligger i `data/vask_raa/`.

## A11 – Hvilke KI-tekster som ble vasket
Bare Claude-fortsettelser ble vasket: 20 per variant, trukket med seed 2026. De 10 menneskelige tekstene per variant ble trukket fra de 30 avsnittene som ikke var med i KI-utvalget. KI- og menneskelige tekster ble blandet i partier på 5, så vaskeren ikke visste hvilke som var hvilke. NorMistral-fortsettelsene er bare med i M1 og M4 («før vask»).

## A12 – Lokal modell
`hf.co/ltg/normistral-7b-warm-instruct:Q4_K_M`, serielt, `nice 19`, 4 tråder, seed 2026 og `num_predict` = 2,5 × ordtallet i første halvdel + 40. Ingen andre tunge prosesser kjørte. Lengden på fortsettelsene varierer mer enn hos Claude.

## A13 – Tokentall
Tokentallene er det CC-harnessen rapporterte per subagent (`subagent_tokens`). Hovedøkta er ikke målt.

## A14 – OCR-støy i fasit
Det er orddelingsfeil i den menneskelige teksten (for eksempel «spylevog nen», «Vi nes»). Det gir litt flere ord og påvirker trolig markørraten lite. M3 og M4 påvirkes mer. Vaskeren rettet slike feil i noen menneskelige tekster, og det blåser opp M3.

## A15 – Fase B-terskel
«≥ 20» i ekstrapoleringen er tolket som samlet frekvens (KI + menneske) per lemma, i samsvar med telleterskelen i M4.

# Fase B

## B1 – claude -p kunne ikke måles
CLI-en er ikke innlogget (OAuth utløpt), og `--bare` krever API-nøkkel. Mekanismen ble valgt mellom to subagenttyper: Explore (10,7k per tekst) mot general-purpose (16,5k per tekst). Explore har en systemprompt for kodesøk og bare lese-verktøy. Det er en annen kontekst enn i røyktesten (general-purpose), så fase A- og fase B-tekster er ikke helt sammenlignbare.

## B2 – Språkrådet-PDF ut av git
Flyttet til `~/data/kilder/sprakradet_2025.pdf` (sha256 73b84a52…a4702f), fjernet fra indeksen med `git rm --cached` og lagt i .gitignore. **Den ligger fortsatt i historikken (commit c6010e6 og eldre). Historikken må renskes (git filter-repo) før en eventuell push.** Teksten (`kilder/sprakradet_2025.txt`) er også et uttrekk av hele rapporten og er flyttet ut av git på samme måte.

## B3 – NLOD-kildene utelatt
NCC-kortet (kilder/ncc/NCC_README.md, lastet ned 2026-11-24) sier bare «Build date original corpus: 21012022» og «Build data revised corpus: 10032025». Det sier også «When year is undetermined it is set to 2021». Ingenting sier ordrett at en enkelt NLOD-kilde ble samlet inn før 30.11.2022. Den reviderte bygget fra 2025 gjør at innsamlingen kan være nyere. Kortet viser bare til «our papers» om innsamlingen. Artikkelen (arXiv 2104.09617) er ikke lest ordrett, så regelens krav er ikke oppfylt. Alle NLOD-kilder er utelatt.
