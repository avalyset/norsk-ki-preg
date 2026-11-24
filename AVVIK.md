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
