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
Flyttet til `~/data/kilder/sprakradet_2025.pdf` (sha256 73b84a52…a4702f), fjernet fra indeksen med `git rm --cached` og lagt i .gitignore. Den lå i historikken til 27.11.2026, da den ble fjernet med `git filter-repo` (se V13). Teksten (`kilder/sprakradet_2025.txt`) er også et uttrekk av hele rapporten og er flyttet ut av git på samme måte.

## B3 – NLOD-kildene utelatt
NCC-kortet (kilder/ncc/NCC_README.md, lastet ned 2026-11-24) sier bare «Build date original corpus: 21012022» og «Build data revised corpus: 10032025». Det sier også «When year is undetermined it is set to 2021». Ingenting sier ordrett at en enkelt NLOD-kilde ble samlet inn før 30.11.2022. Den reviderte bygget fra 2025 gjør at innsamlingen kan være nyere. Kortet viser bare til «our papers» om innsamlingen. Artikkelen (arXiv 2104.09617) er ikke lest ordrett, så regelens krav er ikke oppfylt. Alle NLOD-kilder er utelatt.

## B4 – Engelsk anker: bare lister, ingen fortsettelser
Juzek-repoet (github.com/tjuzek/ai-34-languages, commit 0cf18ff2, klonet til ~/data/ekstern/) inneholder bare 10 menneskelige engelske halvdeler som eksempel (`examples/en_pregenhalves_2020-2021_example.jsonl`). Det er ingen KI-fortsettelser. De publiserte listene (`lexa-index/csv_files.7z`, 38 CSV-filer) har tellinger per lemma: `c_H`, `c_M` (antall par der lemmaet forekommer), `n_pairs` og `rank_LAS`. Rangeringen deres er etter **LAS = Δ-prevalens (ell_M − ell_H)**, ikke etter forholdet. Ankeret kjører derfor vår LPR-kode (`skript/lpr.py`) på deres tellinger og sammenligner rangeringen med `rank_LAS`. Det tester formelen og telleregelen, ikke genererings- og lemmatiseringsløypa. Ingen ny generering.

## B5 – Nynorsk: 0 tekster 2000–2020 i validering
Validering ga 473 bokmål og 0 nynorsk for 2000–2020 etter filteret. Nynorsk er utvidet til 1990–2020 og strømmer treningsshards 0001–0024 (PREREG §2), uten tak på antall shards. Oppgaven nevnte ingen grense her. Fase A hadde en grense på 2.

## B6 – Emne = første «setning» etter OCR-splitting
Mange NCC-avsnitt begynner midt i en setning. Emnet blir da et fragment, for eksempel «radarstasjonen i Kautokeino.». Regelen er låst i PREREG og brukes uendret.

## B7 – Nynorskfilteret justert etter låsing (avvik fra PREREG §2)
Diagnose på train-shard-0025 (`skript/diag_nn.py`): av 179 rå nn-avsnitt 1990–2020 (CC0) falt 172 på kriteriet «≥ 90 % kjente ord». simplemmas nynorskordliste kjenner median 79 % av ordene, kvartiler 0,73–0,84. I tillegg var 93 over 200 ord. Med det opprinnelige filteret ga shard 0001 0 treff og shard 0013 3, mens det trengs 275. Kriteriet måler altså ordlistedekning mer enn OCR-kvalitet for nynorsk. **Bare for nn:**
- terskelen for kjente ord er 0,80
- avsnitt over 200 ord kuttes ved siste setningsgrense før 200 ord (deretter gjelder kravene om ≥ 80 ord og ≥ 4 setninger)

Strømmingen er satt til shards 0001–0008, ikke 0001–0024, fordi utbyttet nå er høyere. Kandidatsettet er alle treff i disse 8 shardene. Bokmål er uendret (0,90, ingen kutt, trukket før endringen). Følgen er at nynorsk-utvalget har mer OCR-støy og ordlistefremmede former enn bokmål.

## B8 – Nynorsk-utvalget er skjevt i tid
nn: 181 av 275 avsnitt er fra 1990–1994, og 15 er bøker. nb er fra 2000–2018 og bare aviser. Variantforskjeller i lista kan derfor blandes med tidsforskjeller (eldre nynorskformer i menneskereferansen).

## B9 – NorMistral: én tekst mangler, én krasj
- `nb-fortsettelse-112`: Ollama avbrøt tre ganger med «prediction aborted, token repeat limit reached». Det er en gjentakelsessløyfe, og med fast seed blir utfallet det samme hver gang. Teksten er utelatt, så nb T1 har 239 NorMistral-tekster.
- Første kjøring stoppet på en ubehandlet feilrespons (samme type). Skriptet har nå tre forsøk og fortsetter så.
- `nn-fortsettelse-125` lyktes på andre forsøk.

## B10 – Tolkningsforbehold for liste_v1-nm
- nn-referansen er mest fra 1990–1994 (B8). Lemmaer som `òg` (27/0) og `verte` (lavere hos KI) gjenspeiler trolig normskifte og ikke bare KI-preg.
- Antislop-frasene er overflate-n-gram og filtrerer ikke egennavn. Derfor kommer «sogn og fjordane» med. Lemmalistene utelater PROPN og tall, slik PREREG sier.
- NorMistral skriver noen ganger metakommentarer («den opphavlege teksten»). Slike treff er modellatferd, ikke norsk KI-stil.

## B11 – Innsamlingsfeil i overvåkingen (ingen datatap)
`samle_b.py -v` tolket `-v` som filmønster, så overvåkingen fant 0 partier og ble aldri ferdig. Feilen er rettet. En opptelling fra disk viste at alle 113 partiene hadde 5 svar hver, og ingen kall ble kjørt på nytt.

## B12 – To tokenmål (lukket 27.11 fra disk, `skript/tokenregnskap.py` → `resultat/tokenregnskap.json`)
Kilde: transkriptene til de 145 subagentkallene (`tasks/*.output` → `subagents/agent-*.jsonl`), feltet `message.usage` på hver `assistant`-linje: `input_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens` og `output_tokens`. Alle kall har `message.model` = `claude-opus-5-5`.

- **9 602 479 = `subagent_tokens`** = summen av de fire feltene i **siste** forespørsel i hvert kall: input 290 + cache-skriving 1 792 965 + cache-lesing 7 042 246 + output 766 978. Det er kontekststørrelsen ved slutten av kallet, ikke forbruket. Tidligere forespørsler i samme kall er ikke med. Tallet stemmer med `usage.subagent_tokens` i harnessvarslene (for eksempel en_tekster_011: 129 049 i begge).
- **39 510 121 = summen over alle `assistant`-linjer**: input 1 334 + cache-skriving 10 736 512 + cache-lesing 26 852 704 + output 1 919 571. Tallet er **dobbelttelt**. Transkriptet skriver én linje per innholdsblokk, og alle linjene i en forespørsel gjentar samme `usage`. 223 forespørsler har flere linjer, alle med identisk `usage`.
- **Riktig sum per forespørsel** (deduplisert på `message.id`, 341 forespørsler): input 682 + cache-skriving 6 005 748 + cache-lesing 12 509 507 + output 918 540 = **19 434 477**.
- **Hovedøkta i DEL 2** (`45403c01….jsonl`, ikke-sidekjede, fra «kjør del 2» 09:18:31Z til commit 73e966f 09:52:52Z, 83 forespørsler, `resultat/tokenregnskap_hovedokt.json`): input 238 + cache-skriving 1 611 809 + cache-lesing 44 916 488 + output 98 351 = **46 626 886**. Overslaget i PREREG §7 (≈ 0,8M) var altså for lavt med en faktor på rundt 58. Det er cache-lesing av en lang kontekst.

**Hva som samsvarer med forbruk mot Max kan ikke avgjøres fra loggene.** Loggene inneholder ingen Max-kvote eller -vekting. Hvordan cache-lesing, cache-skriving og output vektes mot Max-grensen, er ikke dokumentert i noe på disk. Det nærmeste målet på faktisk behandlede tokens er summen per forespørsel: 19,4M for subagentene og 66,1M med hovedøkta. Uten cache-lesing er tallene 6,9M og 8,6M. 9,6M er ikke et forbruksmål.

Konsekvens for taket: PREREG §7 definerte taket som `subagent_tokens` + overslag for hovedøkta. Etter den definisjonen er forbruket ≈ 10,4M < 12M. Etter summen per forespørsel er taket overskredet (19,4M bare for subagentene). Utenom cache-lesing er forbruket under taket (8,6M i alt). Ingen kutt ble gjort, fordi regelen ble anvendt etter det låste målet.

## B13 – Vask i validering: mekanisme og uttrekk
32 Explore-kall (16 per skill), 5 tekster per kall. Skillen ble lest fra disk: den norske fra `skills/norsk-ki-preg/`, den engelske fra pluginkatalogen til anti-ai-writing v2.1.0. Omskrivingsblokken hentes med `skript/samle_vask_b.py`. Overskriften varierer mellom «### Omskriving», «**Omskriving**» og «Rewrite», og skriptet godtar alle tre. Alle 32 kall svarte, med 5 svar hvert (160 tekster). Ingen kall ble kjørt på nytt, og ingen ble drept. Fire engelske kall brukte 5–6 minutter. De ble sjekket fra disk innenfor 10-minuttersgrensen.

## B14 – Tilføyelser i vasken (lukket 27.11 fra disk, `skript/tilfoyelser.py` + `skript/tilfoyelser_klasse.py`)
Den engelske skillen forbyr alle streker, og derfor gjør den replikkstrek om til «» i norske tekster. Det gjør M3 høyere på menneskelig tekst.

Tilføyelser er telt maskinelt i alle 160 vaskede tekster mot kildeteksten, uten modellkall:
- Egennavn: Stanza PROPN der form og lemma mangler i kilden. Kilden sjekkes også uten mellomrom.
- Tall: sifferstrenger.
- Datoer: måneds- og ukedagsnavn og årstall.
- Nye påstander (proxy): setninger med ≥ 3 innholdslemmaer der minst halvparten mangler i kilden.

Hvert maskintreff er deretter klassifisert ved lesing fra disk som TILFØYD, OCR (rekonstruksjon av et skadet ord eller tall i kilden) eller OMFORMULERING.

| Skill | Variant | Tekster | Maskintreff | Av dem OCR | Av dem omformulering | **Ekte tilføyelse** |
|---|---|---|---|---|---|---|
| anti-ai-writing | nb | 40 | 9 | 3 | 3 | **3** (alle KI) |
| anti-ai-writing | nn | 40 | 4 | 4 | 0 | **1** (KI, tallord, funnet utenom maskinen) |
| norsk v0 | nb | 40 | 3 | 3 | 0 | **0** |
| norsk v0 | nn | 40 | 5 | 5 | 0 | **0** |

De ekte tilføyelsene er navngitte forskere og årstall som erstatter «forskere har …» (nb-val_emne-004, -006, -007), og «nesten tre hundre år» → «over tre hundre år» (nn-val_emne-000). Begge skills rekonstruerer de samme OCR-skadene i menneskelig tekst (for eksempel «I3.mars» → «13. mars»). Det er rettinger, ikke tilføyelser.

Begrensning: tallord og endrede påstander uten nye navn eller tall fanges ikke av maskinen. nn-val_emne-000 er funnet fordi den engelske skillen selv nevnte endringen i svaret.

## B15 – Den norske skillen lar halvparten av KI-tekstene stå urørt
Grunnregelen «la tekst uten markører stå urørt» ga «Ingen endringer» for 11 av 20 nb-KI og 9 av 20 nn-KI. Ingen av de 40 menneskelige tekstene ble returnert uendret. De har OCR-feil som skillen retter (orddeling, «Øog» osv.), og derfor er M3 > 0 også for dem. Dette forklarer det meste av resultatet: lag 1-elementene er vanlige ord som bare teller ved opphopning, og Claudes fritekst (T2/T3) utløser dem sjelden.

## B16 – M1 skiller dårlig mellom KI og menneske i bokmål
Før vask er raten 100,61 (KI) mot 99,62 (menneske) per 1000 ord i nb, altså R ≈ 1,01. Lag 1-elementene er målt på T1 (fortsettelser), mens validerings-KI er T2/T3 (fritekst) og menneskereferansen er OCR-avis. Mesteparten av M1 er vanlige lemmaer (`mange`, `mene`, `før`) som forekommer i all tekst. I nn er R før vask 1,68, men det kan delvis være normskiftet (B8). Med bare markorer_v0 er R før vask 1,64 (nb) og 3,14 (nn). Regelen anvendes uendret.

## B17 – Etter-validering: bare status og presiseringer endret
Etter at regelen var anvendt, fikk `SKILL.md` en statuslinje, og i `liste_v1.md` ble sjangerforbeholdet presisert (nn har 15 bokavsnitt) og en setning rettet. `README.md` fikk oppdatert status. Ingen regel i skillen og ingen element i `liste_v1.json` er endret (sha256 336068c3…4c4a298f, uendret).

# v1 (2026-11-27)

## V1 – Datoen for Wikipedia-dumpen (godtatt av Eirik 27.11.2026)
**Dokumentert øvre grense:** NCC-kortet (`kilder/ncc/NCC_README.md`, lastet ned 2026-11-24) sier ordrett «Build date original corpus: 21012022». Wikipedia-delen (`wikipedia_download_nbo`/`_nno`) var med i det opprinnelige korpuset, så dumpen er senest fra 21.01.2022, altså før 30.11.2022. Kortet nevner også «Build data revised corpus: 10032025». At Wikipedia-delen ikke ble lastet ned på nytt i den reviderte bygget, støttes av innholdsdateringen nedenfor. Lisensen står ordrett i kortet: «| Wikipedia | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) |». Alle 15 115 Wikipedia-dokumenter i validation har `publish_year` = 2021, som kortet bruker når året er ukjent («When year is undetermined it is set to 2021»).

**Bekreftelse fra innholdet** (`skript/v1_wiki_datering.py` → `data/v1/wiki_datering.json`):
- Dokumenter som nevner årstallet (nb): 2019 → 436, 2020 → 338, 2021 → 135, 2022 → 14. Omtalene av 2022 ligger på nivå med fremtidige år (2023 → 16, 2028 → 6), og stikkprøver viser planlagte hendelser («planlagt åpning er i 2022»).
- Daterte omtaler av 2021 per måned (begge varianter): januar 14, februar 23, mars 25, april 20, mai 16, juni 9, juli 2, august 7.
- 0 treff på «Regjeringen/Regjeringa Støre» (tiltrådt 14.10.2021), på invasjonen av Ukraina i 2022, på Elizabeth IIs død (08.09.2022) og på ChatGPT.

Samlet: dumpen er fra rundt sommeren 2021. Den dokumenterte øvre grensen er 21.01.2022.

## V2 – «Avsnitt» i Wikipedia-teksten
NCC-teksten har ingen linjeskift, og hele artikkelen ligger på én linje med rester av markup («'''»). Et avsnitt er derfor definert som den innledende prosablokken før første liste (« * », « # ») eller overskrift («==»), kuttet ved siste setningsgrense ≤ 250 ord. «'''» og «''» fjernes. Ett avsnitt per artikkel.

## V3 – Kjentordfilteret for nynorsk
simplemma kjenner median 74 % av ordene i nynorsk Wikipedia. Med terskelen 0,85 ga nn bare 112 avsnitt. Terskelen er 0,70 for nn og 0,85 for nb. Wikipedia er ikke OCR, så filteret skal bare stoppe fremmedspråklig tekst. Utbytte: nb 1435, nn 773.

## V4 – liste_v2: utvalg og lengde
- KI-tekstene er alle T2-faktatekster fra fase B: 25 fritekst-emner og 10 tidligere valideringsemner per modell og variant, til sammen 35. De tidligere valideringsemnene ble brukt i v0-valideringen, men ikke til å bygge en liste.
- Byggesettet er begrenset til avsnitt på minst 150 ord (nb 936, nn 480), fordi prevalens øker med tekstlengden og KI-tekstene er 150–250 ord. Median antall ord: KI 209/193 (nb Claude/NorMistral) og 214/172 (nn), Wikipedia 236/234.
- Terskelen c ≥ 20 ga 475 elementer (nb) og 175 (nn), så den ble ikke senket.

## V5 – Rensing av KI-tekstene og avslaget på Holsdagen
`skript/v1_samle_ki.py` fjerner en innledende overskriftslinje (≤ 8 ord, uten sluttpunktum) i 29 av 40 tekster. Teksten deles også på linjer som bare er «---», deler som begynner med «Merknad» droppes, og den lengste resten beholdes (to tekster: Norheimsund kyrkje og Holsdagen, forsøk 2). Regelen er mekanisk, men ble formulert etter at svarene var lest. Den står ikke i PREREG v2 §4.

nn-wiki-0009 (Holsdagen): første svar var et avslag («Eg kan ikkje skrive denne faktateksten utan å finne på fakta»). Etter PREREG v2 §4 ble kallet kjørt én gang til. Andre svar er en generell tekst om bygdedager i Hallingdal med en merknad om at detaljene mangler. Det regnes som svar, og paret er med.

## V6 – Terskelen i grunnregelen er kalibrert på byggesettet
Grunnregelen i SKILL.md (omtrent 1 av 7 ord i nb, 1 av 9 i nn) er satt ut fra tettheten av lag 1-ord i byggesettet (Wikipedia ≥ 150 ord, 300 per variant) mot fase B-faktatekstene fra Claude:
- nb: menneske p90 13,3, KI p10 15,9 per 100 ord
- nn: menneske p90 10,2, KI p10 11,5 per 100 ord

Kalibreringen er gjort på de samme dataene som lista er bygd fra, så skillet er optimistisk. Valideringssettet er ikke brukt.

## V7 – Skill v1 lar de fleste KI-tekstene stå urørt
«Ingen endringer» (M3 = 0) ble gitt for 15 av 20 nb-KI og 10 av 20 nn-KI. Grunnregelen slår altså til oftere enn i v0. Det er hovedgrunnen til at R-vilkåret feiler. Skillen ser opphopningen dårligere enn M1 teller den, og M1 teller også substantiv og alle bigram.

## V8 – Valideringsavsnittene fra Wikipedia har rester av markup
Prosafilteret slapp gjennom bildetekster («Polititenestemenn i Australia 2006.», «Plasseringa av Yanbian (gul)»), tomme parenteser («Arid Uka ()»), listefragmenter («*1996: A. T.») og lisenslinjer («*Denne artikkelen bygger på … frå, den …»). anti-ai-writing stryker mange av disse, og det gir høyere M3 for den skillen. Den norske skillen lar dem stort sett stå. Begge skills fikk de samme tekstene, så regelen er anvendt uendret.

## V9 – B14 i v1: anti-ai-writing endrer fakta fra egen kunnskap
Utenom maskintreffene: Rindal (nb-wiki-0007) «grensa mot Meldal» → «grensa mot Orkland». Det ble funnet fordi skillen nevnte endringen i svaret sitt. Sammen med Pietà («som representerte Michelangelo» → «den franske kongens utsending») og Schwinger (fagtermer byttet ut) er dette endrede påstander, ikke nye navn. Maskinen fanger dem bare delvis. Tallord og omformulerte påstander kan fortsatt mangle i tellingen.

## V10 – Forbruket i hovedøkta er målt til kjøretidspunktet
`resultat/v1_tokenregnskap.json` dekker hovedøkta fra v1-oppgaven (10:03:53Z) til 10:41:14Z. Skriving av rapport og commit etter dette er ikke med.

## V11 – OpenTimestamps (status 27.11.2026)
- `PREREG.md.ots` er fullstendig, med Bitcoin-attestasjoner i blokk 977348 og 977351 (`ots upgrade`: «Timestamp complete»).
- `PREREG_v2.md.ots` har ikke fått attestasjon ennå. `ots upgrade` svarte «Pending confirmation in Bitcoin blockchain» fra alle fire kalenderne. Stemplet er gyldig som innsendt, og `ots upgrade` må kjøres på nytt før eller etter publisering. Ny kjøring 27.11 (før Brevet): bob.btc.calendar.opentimestamps.org melder «Timestamped by transaction fd5c49c96a40281df1cc2d97178a1a1117e13f9faa07c41c1e166e324fc683a8; waiting for 6 confirmations». Stemplet er fortsatt ikke komplett.

## V12 – Lisensvalg for pakken
- **Kode og skill (Apache-2.0, `LISENS`):** `skript/` og `skills/norsk-ki-preg/` unntatt lag 2. Apache-2.0 var allerede repoets lisens, og den har en eksplisitt patentklausul og NOTICE-mekanisme.
- **Lag 2 (MIT):** `skills/norsk-ki-preg/references/lag2-*.md` er endrede kopier fra anti-ai-writing v2.1.0. MIT krever at opphavsmerknaden og lisensteksten følger med. Den står i `references/KREDITERING.md`, og endringene står i `NOTICE.md`.
- **Data, lister, resultater og rapporter (CC BY-SA 3.0):** `data/v1/wiki_{nb,nn}.jsonl` inneholder utdrag av norsk Wikipedia under CC BY-SA 3.0, ifølge NCC-kortet. CC BY-SA krever at avledede verk deles under samme vilkår. `liste_v2` og `data/v1/vasket.jsonl` (vaskede Wikipedia-avsnitt) bygger direkte på utdragene. Jeg valgte samme versjon, 3.0, og ikke 4.0. 3.0 tillater riktignok senere versjoner (§ 4(b)), men samme versjon som kilden krever ingen tolkning. Resten av dataene (NCC-aviser og -bøker under CC0, tekster fra Claude og NorMistral, målinger) har ingen strengere vilkår. Det er lagt under samme lisens, så pakken bare har én datalisens.
- **Unntak:** korte sitater fra Språkrådet (2025) i `markorer_v0.json` og `references/sprakradet.md` står med kildehenvisning etter sitatretten (åndsverkloven § 29) og er ikke underlisensiert. Kopien av NCC-kortet (`kilder/ncc/NCC_README.md`) er tatt ut av deponeringstarballen, fordi kortets egen lisens ikke er oppgitt. sha256 for kopien (lastet ned 2026-11-24 fra huggingface.co/datasets/NbAiLab/NCC): `da62b2659b71f858accd6c571f4692014c7283716fee4acbf8e5baaa2db1b9aa`.
- **Zenodo-metadata:** `.zenodo.json` oppgir `cc-by-sa-3.0` som postens lisens, fordi det er den strengeste komponenten. Komponentlisensene står i beskrivelsen og i `LISENSER.md`. Lisens-ID-en er sjekket 27.11.2026 mot https://zenodo.org/api/vocabularies/licenses/cc-by-sa-3.0 (HTTP 200, `"id": "cc-by-sa-3.0"`, «Creative Commons Attribution Share Alike 3.0 Unported», scheme spdx) og er gyldig.

## V13 – Historikken renset for Språkrådet-filene
`kilder/sprakradet_2025.pdf` og `kilder/sprakradet_2025.txt` er fjernet fra alle commits med `git filter-repo --invert-paths` (27.11.2026). Backup før rensingen: `~/dev/norsk-ki-preg-backup_2026-11-27_pre-filter-repo.bundle` (sha256 `ffb1b35f513c7b6b6bf0d958ff4d5c5aaf9965b3ad5a11be9ad8021b6757198a`, `git bundle verify`: «is okay»).

Verifisering etter rensingen: ingen av stiene finnes i `git log --all`, og blob-ene `8603cc77…` (PDF) og `51605f2b…` (tekst) finnes ikke (`git cat-file -e`). Alle 26 commits fikk nye hashverdier. Tabellen fra gammel til ny hash står i `logg/filter-repo-commit-map.txt`, og hashene i de gjeldende dokumentene er oppdatert. Eldre commits inneholder fortsatt de gamle hashene i teksten sin.
