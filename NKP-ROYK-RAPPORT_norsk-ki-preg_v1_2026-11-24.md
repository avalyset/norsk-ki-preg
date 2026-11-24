# NKP-RØYK-RAPPORT – norsk-ki-preg v1 (2026-11-24)

**Spørsmål:** Fjerner anti-ai-writing v2.1.0 KI-preg i norsk tekst, eller trengs en målt norsk liste?

**Svar (mekanisk etter BESLUTNING.md):** Ja, fase B trengs. Nynorsk: R = 3,70, 95 % KI [1,47; 8,52]. Nedre grense er over 1. Bokmål: R = 1,43 [0,69; 2,90], ikke signifikant. Fase B er ikke startet.

Låste filer: BESLUTNING.md sha256 `bf251ffb…75d671a1` (commit 1e0588e, før datauttrekk). markorer_v0.json sha256 `6ddb4448…31b399c` (commit c6010e6, før generering).

## 1. Forbruk og lokale modeller

- Subagenter (Opus 5.5): 32 kall, **3 265 291 tokens** i alt. Generering: 20 kall, 1 654 795 tokens (82,7k per kall). Vask: 12 kall, 1 610 496 tokens (134,2k per kall). Hovedøkta er ikke målt. Overslaget var ~1,4M, og avviket skyldes en fast grunnkostnad på ~80k per subagent.
- Ingen betalte API-kall, ingen nøkler lest og ingen modell lastet ned. multilingual-e5-small lå allerede i cachen.
- Lokalt: `hf.co/ltg/normistral-7b-warm-instruct:Q4_K_M`, 100 fortsettelser, 582 s i alt. `ollama list` viste 16 modeller (FORBRUK.md). Bare denne ble brukt.

## 2. Datautvalg

NCC (NbAiLab/NCC), filter `lang_fasttext` ∈ {no, nn}, CC0/NLOD-kilder, `publish_year` ≤ 2020, 80–200 ord og et OCR-kvalitetsfilter (AVVIK A3). Trukket med seed 2026.

| Variant | n | doc_type | Lisens | År | Split |
|---|---|---|---|---|---|
| nb | 50 | newspaper_ocr | CC0 (NB aviser) | 1946–2018 | validering |
| nn | 50 | newspaper_ocr | CC0 (NB aviser) | 1942–2013 | 25 validering + 25 train-shard-0001 |

Alle NLOD-kilder (maalfrid_*) har år 2021 = ukjent og falt ut (AVVIK A2). Bøker passerte ikke kvalitetsfilteret. Logg per avsnitt (id, doc_type, år, lisens, språkkonfidens) står i `data/avsnitt.jsonl`.

## 3. markorer_v0 (32 markører)

Kilde (a): Språkrådet (2025), *Rapport fra test av språkroboter*, PDF sha256 73b84a52…. Sidetall er PDF-sider. Gruppe (b) er strukturmarkører fra oppgaven.

| id | gruppe | s. | kildesitat (forkortet) |
|---|---|---|---|
| komplekst_og_viktig | stående frase | 14 | «Komplekst og viktig» og lignende er standardfraser som går igjen i de fleste tekstene. |
| viktig_komponent | stående frase | 15 | «Viktig komponent», «innebærer» og «dette kan inkludere» er standardformuleringer |
| innebærer | stående frase | 15 | «Viktig komponent», «innebærer» og «dette kan inkludere» er standardformuleringer |
| dette_kan_inkludere | stående frase | 15 | «dette kan inkludere» er standardformuleringer |
| dynamisk_felt | stående frase | 15 | «Fiskeripolitikk er et dynamisk felt som krever kontinuerlig tilpasning og innovasjon.» …  |
| kontinuerlig_tilpasning | stående frase | 15 | «…krever kontinuerlig tilpasning og innovasjon.» |
| fleksibel_tilpasningsdyktig | stående frase | 15 | standardformuleringen «fleksibel og tilpasningsdyktig tilnærming» notert som et ordgytings |
| aspekt | stående frase | 15 | «aspektene» og «kompleksiteten» i siste setning, som går igjen i mange tekster |
| kompleksitet | stående frase | 15 | «aspektene» og «kompleksiteten» … går igjen i mange tekster |
| komplekst_felt | stående frase | 15 | «I sammendrag er landbrukspolitikk et komplekst felt som krever et balansert syn …» |
| balansert | stående frase | 14 | «Norge inntok en forsiktig og balansert linje» (s. 14); «et balansert syn» (s. 15) |
| balansegang | stående frase | 15 | «Samlet sett er fiskeripolitikk en balansegang mellom ulike hensyn og interesser.» |
| skjæringspunkt | stående frase | 14 | «Det er nettopp i skjæringspunktet mellom disse ulike målene at …» |
| dypt_forankret | stående frase | 15 | «Alt i alt er Norges forhold til NATO dypt forankret i landets historie …» |
| ikke_bare_ogsaa | stående frase | 15 | «Fiskerinæringen er ikke bare en økonomisk aktivitet; den er også en kulturell bærebjelke  |
| alt_i_alt | avslutningsformel | 15 | Oppsummeringsformuleringen «alt i alt … forankret» er registrert som feil. |
| samlet_sett | avslutningsformel | 15 | Oppsummeringsformuleringen «samlet sett … balansegang» er notert som en tekstfeil |
| i_sammendrag | avslutningsformel | 15 | oppsummeringsformuleringen «[er] i sammendrag et komplekst felt» notert som feil |
| gjore_en_forskjell | kalk | 10 | gjøre en forskjell (av engelsk make a difference) |
| fanget_oyet | kalk | 10 | plutselig fanget øyet hans noe (ChatGPT) |
| dypt_pust | kalk | 10 | ho tok eit djupt pust (Copilot) |
| tilfreds_med_aa | kalk | 10 | for no var han tilfreds med å vere i byen (Copilot) |
| som_sine_egne_lommer | kalk | 10 | begge kjente den [skogen] som sine egne lommer (Le Chat) |
| med_en_x_stemme | kalk | 10 | sa hun med en stolt stemme (Le Chat) |
| aktorene_involvert | kalk | 10 | de ulike aktørene involvert (Le Chat) |
| ut_av_kontroll | kalk | 10 | en kveld som hadde gått fullstendig ut av kontroll (NorMistral) |
| ny_start | kalk | 10 | en kopp [kaffe] som kunne tilby henne en ny start (ChatGPT) |
| tankestrek_uten_mellomrom | struktur | – | tankestrek uten mellomrom (—) |
| title_case_overskrift | struktur | – | store forbokstaver i overskrifter etter engelsk mønster |
| ikke_x_men_y | struktur | – | «ikke X, men Y» |
| tredelt_oppramsing | struktur | – | tredelte oppramsinger |
| punktliste_fet_tittel | struktur | – | punktlister med fete titler |

Regex og nynorsktilpasninger står i markorer_v0.json (AVVIK A7). Norsk tankestrek med mellomrom telles ikke.

## 4. Resultater
### M1 – markørrate per 1000 ord

| Variant | Gruppe | n | treff | ord | rate |
|---|---|---|---|---|---|
| nb | Claude etter vask | 20 | 9 | 1173 | 7.67 |
| nb | Claude før vask | 50 | 30 | 3175 | 9.45 |
| nb | Claude før vask (vaskeutvalget) | 20 | 10 | 1236 | 8.09 |
| nb | NorMistral før vask | 50 | 27 | 4487 | 6.02 |
| nb | menneske (fasit) | 50 | 18 | 3347 | 5.38 |
| nb | menneske etter vask | 10 | 4 | 609 | 6.57 |
| nn | Claude etter vask | 20 | 13 | 1159 | 11.22 |
| nn | Claude før vask | 50 | 30 | 3219 | 9.32 |
| nn | Claude før vask (vaskeutvalget) | 20 | 15 | 1293 | 11.6 |
| nn | NorMistral før vask | 50 | 16 | 4168 | 3.84 |
| nn | menneske (fasit) | 50 | 10 | 3297 | 3.03 |
| nn | menneske etter vask | 10 | 1 | 657 | 1.52 |

Treff per markør:

- nb|Claude etter vask: {'tredelt_oppramsing': 8, 'ikke_x_men_y': 1}
- nb|Claude før vask: {'tredelt_oppramsing': 26, 'ikke_x_men_y': 4}
- nb|Claude før vask (vaskeutvalget): {'tredelt_oppramsing': 9, 'ikke_x_men_y': 1}
- nb|NorMistral før vask: {'tredelt_oppramsing': 19, 'ikke_x_men_y': 4, 'gjore_en_forskjell': 2, 'ny_start': 1, 'aspekt': 1}
- nb|menneske (fasit): {'tredelt_oppramsing': 16, 'ikke_x_men_y': 1, 'tankestrek_uten_mellomrom': 1}
- nb|menneske etter vask: {'tredelt_oppramsing': 4}
- nn|Claude etter vask: {'tredelt_oppramsing': 9, 'ikke_x_men_y': 3, 'title_case_overskrift': 1}
- nn|Claude før vask: {'tredelt_oppramsing': 27, 'ikke_x_men_y': 3}
- nn|Claude før vask (vaskeutvalget): {'tredelt_oppramsing': 12, 'ikke_x_men_y': 3}
- nn|NorMistral før vask: {'tredelt_oppramsing': 9, 'ikke_x_men_y': 5, 'tankestrek_uten_mellomrom': 1, 'samlet_sett': 1}
- nn|menneske (fasit): {'tredelt_oppramsing': 6, 'ikke_x_men_y': 3, 'innebærer': 1}
- nn|menneske etter vask: {'tredelt_oppramsing': 1}

**R (beslutning, 10 000 bootstrap-trekk, seed 2026):**

| Variant | R | 95 % KI | Fase B? |
|---|---|---|---|
| nb | 1.427 | [0.689; 2.899] | nei |
| nn | 3.698 | [1.468; 8.518] | JA |

Følsomhet (beskrivende, påvirker ikke beslutningen, egne trekk; `resultat/folsomhet.json`):

| Variant | Variasjon | R | 95 % KI |
|---|---|---|---|
| nb | etter vask, alle | 1.43 | [0.69; 2.9] |
| nb | før vask, samme 20 | 1.5 | [0.77; 3.01] |
| nb | etter vask, uten tredelt_oppramsing | 1.43 | for få treff |
| nb | etter vask, uten ikke_x_men_y | 1.34 | [0.59; 2.87] |
| nb | etter vask, bare Språkrådet-markører (a) | udefinert (0 treff i begge) | for få treff |
| nn | etter vask, alle | 3.7 | [1.47; 8.56] |
| nn | før vask, samme 20 | 3.82 | [1.56; 8.75] |
| nn | etter vask, uten tredelt_oppramsing | 2.84 | [0.58; 15.53] |
| nn | etter vask, uten ikke_x_men_y | 4.06 | [1.09; 12.24] |
| nn | etter vask, bare Språkrådet-markører (a) | 0.0 | [0.0; 1.0] |

### M2 – meningsbevaring (cosinus før/etter vask)

Modell: `intfloat/multilingual-e5-small` rev. 614241f6, lisens MIT, prefiks «query: ».

| Gruppe | n | snitt | min |
|---|---|---|---|
| nb|claude før→etter vask | 20 | 0.9946 | 0.9671 |
| nb|menneske før→etter vask | 10 | 0.9839 | 0.9781 |
| nb|referanse: fasit vs Claude-fortsettelse | 50 | 0.8778 | 0.7793 |
| nn|claude før→etter vask | 20 | 0.9884 | 0.8407 |
| nn|menneske før→etter vask | 10 | 0.9944 | 0.9846 |
| nn|referanse: fasit vs Claude-fortsettelse | 50 | 0.8885 | 0.8271 |

Til sammenligning: to ulike tekster om samme sak (fasit mot Claude-fortsettelse) ligger på ~0,88. Vasken bevarer meningen nesten fullt ut. Laveste verdi er 0,84 (én nn-tekst).

### M3 – endringsgrad (normalisert Levenshtein)

| Gruppe | n | tegn median | tegn snitt | ord median | uendret |
|---|---|---|---|---|---|
| nb|menneske | 10 | 0.109 | 0.136 | 0.19 | 0 |
| nb|claude | 20 | 0.046 | 0.118 | 0.046 | 6 |
| nn|claude | 20 | 0.017 | 0.094 | 0.0 | 8 |
| nn|menneske | 10 | 0.022 | 0.041 | 0.092 | 1 |

For bokmål endret skillen den menneskelige teksten mer (median 11 % av tegnene, 0/10 uendret) enn KI-teksten (median 5 %, 6/20 uendret). Noe av dette er OCR-retting (AVVIK A14). Vaskeren gjorde også om replikkstrek til «» i flere tekster.

### M4 – log prevalence ratio per lemma (beskrivende)

LPR = ln[(c_KI+0,5)/(N_KI+0,5V) / (c_M+0,5)/(N_M+0,5V)], simplemma-lemmaer (AVVIK A5), Claude-fortsettelse mot ekte fortsettelse, terskel c_KI+c_M ≥ 5. **Dette er kandidater, ikke funn.** n = 50 par per variant gir svært usikre estimater.

**nb** (N_KI=3168, N_M=3314, 199 lemmaer over terskel). Topp 50 (lemma KI/menneske LPR):

allerede 6/0 2.6, sette 5/0 2.433, kommune 9/1 1.881, neste 9/1 1.881, bruke 6/1 1.502, hver 10/2 1.471, se 9/2 1.37, trenge 5/1 1.335, enkelt 5/1 1.335, første 5/1 1.335, sitte 5/1 1.335, folk 8/2 1.259, klasse 4/1 1.134, vurdere 4/1 1.134, plass 4/1 1.134, penge 7/2 1.134, lenge 4/1 1.134, særlig 4/1 1.134, enn 4/1 1.134, kort 4/1 1.134, politiker 4/1 1.134, igjen 7/2 1.134, fast 4/1 1.134, kvinne 4/1 1.134, gå 12/4 1.057, holde 6/2 0.991, bare 6/2 0.991, likevel 8/3 0.923, der 15/6 0.905, ved 12/5 0.856, håpe 5/2 0.824, skole 5/2 0.824, lærer 5/2 0.824, ta 18/8 0.813, egen 7/3 0.798, fortelle 7/3 0.798, både 11/5 0.773, mange 36/17 0.771, de 56/29 0.685, uten 8/4 0.671, derfor 8/4 0.671, elev 8/4 0.671, mene 8/4 0.671, komme 17/9 0.646, etter 15/8 0.636, kveld 4/2 0.623, lite 4/2 0.623, selv 4/2 0.623, vente 4/2 0.623, god 16/9 0.588

**nn** (N_KI=3215, N_M=3225, 195 lemmaer over terskel). Topp 50 (lemma KI/menneske LPR):

difor 10/0 3.047, bygd 8/0 2.836, natt 8/0 2.836, syngja 5/0 2.4, aldri 5/0 2.4, halde 12/1 2.123, finne 9/1 1.848, arbeid 8/1 1.737, medan 7/1 1.612, likevel 6/1 1.469, sein 6/1 1.469, mange 22/5 1.411, kyrkje 5/1 1.302, liggja 5/1 1.302, be 5/1 1.302, haust 4/1 1.101, melde 7/2 1.101, stad 10/3 1.101, plass 4/1 1.101, vind 4/1 1.101, før 13/4 1.101, bilete 4/1 1.101, viktig 4/1 1.101, vår 4/1 1.101, ung 4/1 1.101, tru 4/1 1.101, lang 10/3 1.101, kvar 12/4 1.024, over 14/5 0.972, liggje 6/2 0.958, kor 6/2 0.958, lensmann 5/2 0.791, vise 5/2 0.791, lag 5/2 0.791, vilje 18/8 0.78, etter 20/9 0.772, og 163/77 0.749, gå 22/11 0.674, stor 14/7 0.662, mot 8/4 0.638, både 6/3 0.622, få 31/17 0.59, to 4/2 0.59, fyrste 4/2 0.59, parti 4/2 0.59, skrive 4/2 0.59, korleis 4/2 0.59, familie 4/2 0.59, time 4/2 0.59, hans 4/2 0.59

Mønster: Claude bruker mer generelle og tidløse ord (allerede, neste, hver, folk; nn: difor, aldri, medan, likevel) og mer «og» på nynorsk (163 mot 77). Menneskeskrevet avistekst har flere tall- og stedsforankrede ord (prosent, fjor, fisk) og eldre former (so, desse, ho). Den siste skjevheten kommer delvis av årstallene i korpuset.

## 5. Beslutning

Regelen i BESLUTNING.md er anvendt mekanisk:
- **nb:** nedre grense 0,69 ≤ 1, ikke utløst.
- **nn:** nedre grense 1,47 > 1, **utløst**.

→ **En målt norsk liste trengs (fase B).** Se FASE-B-OVERSIKT.md.

Tolkning (ikke en del av regelen): Utslaget skyldes de to strukturmarkørene «A, B og C» og «ikke X, men Y». Uten tredelt oppramsing faller nn-KI-et under 1 ([0,58; 15,5]). Språkrådets frase- og kalkmarkører ga 0 treff i vasket Claude-tekst, fordi genren (avisfortsettelser) knapt fremkaller dem. Vasken flyttet markørraten lite (nn før vask 3,82, etter 3,70, på de samme 20 tekstene). Skillen gjør altså ikke på norsk det den gjør på engelsk med «rule of three». Markørsettet er tynt for denne genren, og det taler for en datadrevet liste i fase B.

## 6. FASE-B-OVERSIKT (sammendrag)

- Par som trengs for ≥ 200 lemmaer med frekvens ≥ 20: **nb ≈ 239, nn ≈ 183** (eksponent 0,93 og 1,00). Rund av til ~250 per variant.
- Forbruk: 400 nye par ≈ 6,6M tokens med 5 par per kall, eller ≈ 3,4M med 10 per kall. Lokal maskintid ≈ 50 min for 500 par.
- Engelsk anker: samme løype på engelsk, sammenlignet med Juzeks liste (overlapp@50, Spearman).
- Lisens: CC0/NLOD-kilder og Claude-utdata kan brukes. Avledet liste under CC0. Ikke bruk BY-NC eller opensubtitles.
- Prereg på Zenodo og OTS-stempel før all generering.

## 7. AVVIK (sammendrag, full tekst i AVVIK.md)

- A1 NCC-feltet heter lang_fasttext, ikke lang
- A2 NLOD-kildene har år 2021 (ukjent) og falt ut; utvalget er bare CC0-aviser
- A3 OCR-kvalitetsfilter lagt til før uttrekk
- A4 nynorsk utvidet til train-shard-0001 (1 av 2 tillatte)
- A5 Stanza ikke installert; simplemma brukt
- A6 setningsmodellen lå i cachen; ingen nedlasting
- A7 nynorskformer lagt til i Språkrådet-markørene
- A8 Språkrådet-PDF i det lokale repoet
- A9 5 fortsettelser per subagentkontekst, med CC-systemprompt
- A10 vaskeinstruksen fikk «ikke still spørsmål»; norske overskrifter i svarene
- A11 bare Claude-tekster vasket; KI og menneske blandet blindt
- A12 innstillinger for den lokale modellen
- A13 tokentall fra harnessen; hovedøkta ikke målt
- A14 OCR-støy i fasit påvirker M3/M4
- A15 fase B-terskelen er tolket som samlet frekvens

## 8. Til Eirik

Ingen avgjørelse trengs for fase A. Før fase B starter: godkjenn tokenbudsjettet (3–7M for gulvet, mer for en robust liste) og avgjør om NLOD-kildene skal inn. Da må årsfilteret ≤ 2020 droppes eller erstattes, fordi NCC koder ukjent år som 2021.
