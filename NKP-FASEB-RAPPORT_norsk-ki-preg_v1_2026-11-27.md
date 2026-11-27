# NKP fase B – rapport (v1, 27.11.2026)

**Beslutning etter PREREG-regelen: den norske skillen er ikke bedre.** R-vilkåret holder ikke i noen variant. I bokmål senker anti-ai-writing markørraten signifikant mer enn den norske skillen. M3-vilkåret holder i begge varianter: den norske skillen endrer menneskeskrevet tekst langt mindre.

## 1. Forbruk og kutt
Fra `message.usage` i transkriptene (AVVIK B12, FORBRUK.md). A = `subagent_tokens` (siste forespørsel per kall, harnessens tall). B = sum per forespørsel, deduplisert på `message.id`. C = B uten cache-lesing.

| Ledd | Kall | A | B | C |
|---|---|---|---|---|
| Claude-generering | 113 | 6 245 229 | 11 126 620 | 3 810 340 |
| Vask, norsk skill | 16 | 1 392 109 | 3 076 451 | 1 404 154 |
| Vask, anti-ai-writing | 16 | 1 965 141 | 5 231 406 | 1 710 476 |
| **Subagenter** | 145 | **9 602 479** | **19 434 477** | **6 924 970** |
| Hovedøkt (DEL 2) | – | – | 46 626 886 | 1 710 398 |
| **Alt** | | | **66 061 363** | **8 635 368** |

Det tidligere tallet 39,5M var dobbelttelt (én transkriptlinje per innholdsblokk med gjentatt `usage`). Overslaget for hovedøkta (0,8M) var for lavt med en faktor på rundt 58, nesten bare på grunn av cache-lesing. Hvilket mål som tilsvarer forbruk mot Max, kan ikke avgjøres fra loggene.

Taket på 12M gjaldt etter det låste PREREG-målet (A + overslag), som gir ≈ 10,4M. **Ingen kutt.** Etter B er taket overskredet, etter C ikke. Kontrollpunktet ble ikke utløst: snittet for de 10 første genereringskallene var 54,0k mot grensen 62k. Lokalt: NorMistral 564 tekster (81,7 min), e5-small på CPU. Ingen betalte API-er, ingen nøkler, ingen push.

Generering, opptalt fra disk etter at overvåkingen var stoppet (AVVIK B11): før 113 ferdige, 0 manglende, 0 feilet; etter det samme. Ingenting ble kjørt på nytt. Vask: 32 av 32 kall svarte (160 tekster), ingen nye kjøringer (B13).

## 2. PREREG
`PREREG.md` sha256 `f3e13a9cc266c2970ee9c3f4cf694e71c192c8fd38d7dacb1ab47398dd521df9`, låst 24.11 (commit 0e29caf) før all fase B-generering. OpenTimestamps: `PREREG.md.ots` (commit ce2df09), oppgradert 27.11 (commit d676d77) med Bitcoin-attestasjoner (blokk 977348 og 977351). Lokal `ots verify` krever egen Bitcoin-node.

`liste_v1.json` frosset før valideringsvasken: sha256 `336068c35ca1cfa967cd390e43a451d41f49b21a94743c48760c1ace4c4a298f` (commit 9b125ef). Uendret etter valideringen.

## 3. Datautvalg
| Variant | Kilde | År | Kandidater | Utvalg |
|---|---|---|---|---|
| nb | NCC, NB-aviser (CC0), validering | 2000–2018 | 473 | 20 val-menneske, 20 val-emner, 240 fortsettelsespar, 50 fritekst-emner |
| nn | NCC, NB-aviser 260 + bøker 15 (CC0), train-shard 0001–0008 | 1990–2019 (181 fra 1990–94) | 362 | 20 / 20 / 185 / 50 |

NLOD-kildene er utelatt (B3). Nynorskfilteret ble justert etter låsing (B7, avvik). nn-utvalget er skjevt i tid (B8). Claude: 565 tekster (nb 310, nn 255). NorMistral: 564 (nb-fortsettelse-112 mangler, B9).

## 4. Engelsk anker (bare formelen, B4)
Juzek-repoet har ingen KI-fortsettelser. Vår LPR-kode er kjørt på deres publiserte tellinger og sammenlignet med deres rangering (LAS = Δ-prevalens): Spearman over alle elementer ≥ 20 er 0,889–0,912 for tre lister. Toppene overlapper lite (Jaccard topp 100: 0,015–0,064), fordi LPR løfter sjeldne ord og LAS hyppige funksjonsord. Ankeret tester formel og telleregel, ikke genererings- og lemmatiseringsløypa.

## 5. liste_v1 – topp 30 per variant (Claude, T1, Stanza-lemma)
c_KI/c_M = antall tekster av 240 (nb) eller 185 (nn) der lemmaet forekommer. LPR = ln(p_KI/p_M) med Jeffreys-glatting.

**Bokmål** (inntatt: 76 lemmaer, 52 bigram, 7 trigram; samsvar med NorMistral: `holde`, `sted`, `ung`, `tidlig`, `lag`, «å ta», «å bli»):
før_SCONJ 29/2 2,47 · plan_NOUN 18/2 2,00 · selv_ADV 18/2 2,00 · handle_VERB 21/4 1,56 · holde_VERB 21/4 1,56 · allerede_ADV 32/7 1,47 · trener_NOUN 18/4 1,41 · neste_DET 38/9 1,40 · tur_NOUN 17/4 1,36 · ung_ADJ 23/6 1,29 · be_VERB 17/5 1,16 · politi_NOUN 20/6 1,15 · hver_DET 27/9 1,06 · arbeid_NOUN 15/5 1,04 · likevel_ADV 26/9 1,03 · skole_NOUN 23/8 1,02 · mene_VERB 53/19 1,01 · egen_DET 20/7 1,01 · lag_NOUN 17/6 0,99 · kommune_NOUN 41/15 0,99 · gjennom_ADP 32/12 0,96 · fortelle_VERB 37/14 0,95 · barn_NOUN 21/8 0,93 · før_ADP 25/10 0,89 · penge_NOUN 20/8 0,88 · mange_ADJ 120/50 0,87 · plass_NOUN 15/6 0,87 · sted_NOUN 15/6 0,87 · mål_NOUN 15/6 0,87 · derfor_ADV 28/12 0,82

Fraser (Antislop, f_KI/f_M): «han forteller at» 9/0, «mener det er» 8/0, «hun forteller at» 7/0, «ta vare på» 7/0, «han understreker at» 6/0, «målet er å» 6/0. Bigram: «mange av» 22/2, «og mange» 18/2, «fortelle at» 25/4.

**Nynorsk** (inntatt: 44 lemmaer, 19 bigram, 0 trigram; 5 lemmaer i samsvar):
òg_ADV 32/0 4,17 · neste_DET 24/2 2,28 · håpe_VERB 20/2 2,10 · bli_VERB 37/7 1,61 · att_ADV 41/9 1,47 · ung_ADJ 21/5 1,36 · eigen_DET 17/4 1,36 · sitje_VERB 16/4 1,30 · stad_NOUN 26/8 1,14 · halde_VERB 43/14 1,10 · vente_VERB 22/7 1,10 · fortelje_VERB 33/11 1,07 · vite_VERB 24/8 1,06 · kva_PRON 32/12 0,96 · mange_ADJ 111/43 0,94 · meine_VERB 51/20 0,92 · stå_VERB 48/19 0,91 · sak_NOUN 33/13 0,91 · lite_ADJ 15/6 0,87 · før_ADP 17/7 0,85 · kommune_NOUN 31/13 0,85 · veg_NOUN 26/11 0,84 · framleis_ADV 19/8 0,83 · skrive_VERB 14/6 0,80 · politi_NOUN 14/6 0,80 · bu_VERB 14/6 0,80 · god_ADJ 74/33 0,80 · folk_NOUN 38/17 0,79 · gje_VERB 26/12 0,75 · både_CCONJ 30/14 0,74

Fraser: «for å finne» 5/0, «kanskje er det» 5/0, «det viktigaste er» 5/0. Bigram: «seie han» 30/3, «mange av» 27/4, «og at» 27/4.

Tolkning: lista domineres av sitatrammer («fortelle at», «mene», «seie han») og generelt ordforråd, ikke av typiske «KI-ord». I nynorsk speiler `òg`, `bli` og `att` trolig normskiftet mot en referanse fra 1990–94 (B8). NorMistral-lista (`resultat/liste_v1-nm.json`) har tydeligere registermarkører (`uttrykke`, `imidlertid`, «å merke seg»). Full liste med Δ-prevalens og Språkrådets markører står i `liste_v1.md`.

## 6. Validering (holdt-ut sett, 20 KI + 20 menneske per variant)
KI-tekster = Claude T2/T3 på valideringsemner. Menneske = holdt-ut NCC-avsnitt. Begge skills vasket de samme 16 partiene. M1 = (markorer_v0-regex + liste_v1 lag 1 på Stanza-lemmaer) per 1000 ord. R = rate(KI etter vask) / rate(menneske, uvasket).

| | nb | nn |
|---|---|---|
| M1 menneske | 99,62 | 71,06 |
| M1 KI før vask (R) | 100,61 (1,01) | 119,41 (1,68) |
| M1 KI etter norsk skill (R_no) | 98,51 (0,989) | 115,93 (1,631) |
| M1 KI etter anti-ai-writing (R_en) | 90,96 (0,913) | 116,89 (1,645) |
| **R_en − R_no, 95 % KI** | **−0,076 [−0,135; −0,023]** | **0,014 [−0,056; 0,079]** |
| R-vilkår (nedre > 0) | nei | nei |
| M3 menneske, median: norsk / engelsk | 0,010 / 0,058 | 0,014 / 0,066 |
| **M3_no − M3_en, 95 % KI** | **−0,079 [−0,111; −0,050]** | **−0,104 [−0,154; −0,059]** |
| M3-vilkår (nedre ≤ 0) | ja | ja |
| M2 cosinus, KI: norsk / engelsk | 0,999 / 0,988 | 0,997 / 0,988 |
| M2 cosinus, menneske: norsk / engelsk | 0,992 / 0,987 | 0,995 / 0,989 |
| M3 KI, median: norsk / engelsk | 0,000 / 0,226 | 0,001 / 0,165 |
| KI returnert uendret, norsk skill | 11 av 20 | 9 av 20 |
| Bare markorer_v0: R_no / R_en (beskrivende) | 1,60 / 1,19 | 3,20 / 2,80 |

Parret bootstrap 10 000 trekk, `default_rng(2026)`, nb før nn, R-trekk før M3-trekk. Alle 10 000 R-trekk var endelige.

**Regelen anvendt mekanisk:** R-vilkåret må holde i minst én variant. Det holder i ingen (nb: KI ligger under 0, altså i favør av anti-ai-writing; nn: KI dekker 0). M3-vilkåret holder i begge. **Resultat: den norske skillen er ikke bedre.**

Hva som skjedde:
- Den norske skillen gjør nesten ingenting med Claude-fritekst. Grunnregelen «la tekst uten markører stå urørt» slo til på halvparten av KI-tekstene (B15). Lag 1-lemmaene er vanlige ord som bare teller ved opphopning.
- Den endret alle 40 menneskelige tekster litt, fordi den retter OCR-feil. M3 er likevel 5–8 ganger lavere enn for anti-ai-writing.
- anti-ai-writing skriver om mye: den kutter avslutninger og bytter replikkstrek til «». Det senker markørraten noe i nb, men endrer menneskelig tekst mye.
- **Tilføyelser (B14, maskinell telling mot kilden og klassifisering fra disk):** anti-ai-writing la inn navn, tall eller påstander som ikke står i kilden i 4 av 80 tekster (nb 3/40, nn 1/40, alle KI-tekster). Den norske skillen gjorde det i 0 av 80. Begge skills rekonstruerer de samme OCR-skadene i menneskelig tekst (nb 3, nn 4–5). De er ikke regnet som tilføyelser.

| Skill | Variant | Maskintreff | OCR | Omformulering | Ekte tilføyelse |
|---|---|---|---|---|---|
| anti-ai-writing | nb | 9 | 3 | 3 | 3 |
| anti-ai-writing | nn | 4 | 4 | 0 | 1 (tallord, funnet utenom maskinen) |
| norsk v0 | nb | 3 | 3 | 0 | 0 |
| norsk v0 | nn | 5 | 5 | 0 | 0 |

Eksempler, ordrett fra `data/b_vasket.jsonl`:

*anti-ai-writing*
1. nb-val_emne-004 (TILFØYD): «Den nederlandske psykologen Peter de Jong og kollegaene hans har i flere forsøk funnet støtte for at rødming kan fungere som et sosialt signal.» Kilden har: «Forskere har pekt på at».
2. nb-val_emne-007 (TILFØYD): «Rafael Núñez og Eve Sweetser viste i en studie fra 2006 at aymara, som snakkes i Andesfjellene, beskriver fortiden som noe som ligger foran». Kilden har: «Språkforskere har vist at».
3. nb-val_emne-006 (TILFØYD): «Forsøkene til de amerikanske sosialpsykologene Bibb Latané og John Darley fra 1968 la grunnlaget for det som kalles tilskuereffekten». Kilden har: «Forskning på såkalt tilskuereffekt viser».
4. nn-val_emne-000 (TILFØYD, endret faktapåstand): «har vore spela i over tre hundre år». Kilden har: «nesten tre hundre år».
5. nb-val_menneske-009 (OCR): «For Ungarn kan det være viktig å kunne vise at den ungarske minoriteten i Romania er sterk og homogen». Kilden har: «garn kan det være viktig».

*norsk v0* (alle treff er OCR-rekonstruksjoner)
1. nn-val_menneske-005: «høve til å røysta frå 1. juli valåret». Kilden har: «frå i. juli valåret».
2. nn-val_menneske-004: «Iran: 244, Statslause: 201, Libanon: 179». Kilden har: «Stats lause:2ol».
3. nb-val_menneske-015: «Nedgangen i belegg ble tatt igjen med en liten prisøkning, sier Torgersen.» Kilden har: «sier Tbrgersen.»
4. nn-val_menneske-012: «I Sogn og Fjordane og Møre og Romsdal vart det i fjor berre meldt 5 saker». Kilden har: «Øog Fjordane Øog Møre Øog Romsdal».
5. nb-val_menneske-008: «Det hele avsluttes i Lakselv den 13. mars». Kilden har: «den I3.mars».
- M1 skiller nesten ikke KI fra menneske i bokmål før vask (R = 1,01, B16). Valideringen har derfor lite å måle en nedgang mot. Lista er målt på fortsettelser (T1), mens validerings-KI er fritekst (T2/T3) mot OCR-avis.
- Sirkularitet: lista er grunnlaget for både skillen og M1. Med bare markorer_v0 er R_no høyere enn R_en i begge varianter, og bildet er det samme.

## 7. Frys-lesing (steg 12)
- `liste_v1.md`: «én sjanger (NB-aviser)» presisert (nn har 15 bokavsnitt). Én setning rettet. Valideringsstatus lagt til.
- `SKILL.md`: statuslinje lagt til (besto ikke valideringen). Ingen regel endret. Påstanden i `struktur.md` om tredelte oppramsinger er kontrollert mot fase A (nn Claude 27 mot menneske 6; uten dem faller R til 2,84 [0,58; 15,53]). Språkrådet-henvisningen (s. 15–16) er kontrollert mot PDF-en.
- `README.md`: stale status (bare fase A) og tittel («røyktest») rettet, struktur og lisens oppdatert.

## 8. AVVIK (fase B, fullstendig i AVVIK.md)
- B1 `claude -p` ikke målbar (CLI ikke innlogget, `--bare` krever nøkkel) → Explore-subagent, 5 tekster per kall.
- B2 Språkrådet-PDF ute av git-indeksen, **men fortsatt i historikken. Må renskes før en eventuell push.**
- B3 NLOD-kildene utelatt. B4 anker bare på formelen. B5 nn 0 tekster 2000–2020 → 1990–2020.
- B6 emne kan være et OCR-fragment. **B7 nn-filteret justert etter låsing.** B8 nn skjevt i tid (normskifte).
- B9 NorMistral: én tekst mangler. B10 tolkningsforbehold for NorMistral-lista.
- B11 overvåkingsfeil (`-v`), ingen datatap og ingen nye kjøringer. **B12 lukket:** 9,6M = siste forespørsel per kall, 39,5M = dobbelttelt linjesum, riktig sum 19,4M (subagenter) + 46,6M (hovedøkt).
- B13 vaskemekanisme, 32/32. **B14 lukket:** tilføyelser i 4/80 (engelsk) mot 0/80 (norsk). B15 norsk skill lar 20 av 40 KI-tekster stå urørt. B16 M1 skiller dårlig i nb. B17 bare status og presiseringer endret etter valideringen.

## 9. Neste steg
Valideringen sier at v0 ikke slår anti-ai-writing på markørrate. Den sier også at v0 er langt skånsommere mot menneskelig tekst. En v1 bør måles på fritekst (T2/T3) i stedet for fortsettelser, fordi det er der skillen faktisk skal brukes. Den bør også ha en referanse som ikke er OCR-avis. Det krever ny PREREG. Ingenting er publisert eller pushet.
