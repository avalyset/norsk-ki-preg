# PREREG – norsk-ki-preg fase B (låst 2026-11-24, før all fase B-generering)

Bygger på fase A (NKP-ROYK-RAPPORT_norsk-ki-preg_v1_2026-11-24.md), BESLUTNING.md (fase A) og markorer_v0.json (sha256 6ddb4448…31b399c, uendret).

## 1. Formål
(a) En målt liste over ord og fraser som Claude (Opus 5.5) og NorMistral-7B overbruker i bokmål og nynorsk sammenlignet med menneskeskrevet tekst (liste_v1).
(b) En norsk språkvasker-skill (v0) bygd på lista, validert mot anti-ai-writing v2.1.0 på et holdt-ut sett. Ingen KI-detektorer brukes. Skillen måles på KI-preg (markørrate), meningsbevaring og hvor lite den endrer menneskeskrevet tekst.

## 2. Data
- NCC (NbAiLab/NCC), `lang_fasttext` ∈ {no→nb, nn}, `doc_type` ∈ {newspaper_ocr, books} (CC0). NLOD-kildene er utelatt (AVVIK B3). newspapers_online_*, opensubtitles og Wikipedia er ikke med.
- År: nb 2000–2020 (validering). nn 2000–2020 ga 0 tekster i validering, så nn utvides til 1990–2020 og treningsshards 0001–0024 strømmes. Kommer det under 275 nn-kandidater, strømmes shards 0025–0046.
- Kvalitetsfilter som i fase A (AVVIK A3): 80–200 ord, ≥ 4 setninger, ≥ 90 % kjente ord (simplemma), ingen orddelingsrester, sluttpunktum. Avsnitt brukt i fase A er utelatt.
- Trekk per variant: kandidatene sorteres på id og stokkes med `random.Random(2026)`. Deretter tildeles de i denne rekkefølgen (også prioritet ved mangel):
  1. 20 holdt-ut menneskelige avsnitt (validering, M-hum)
  2. 20 holdt-ut emner (validering, KI-tekster)
  3. fortsettelsespar: nb 240, nn 185
  4. 50 emner for fritekst
  Ved mangel kuttes bakfra (fritekst-emner først, deretter fortsettelsespar under minimum). Dette rapporteres. Holdt-ut-avsnitt og -emner brukes aldri til å bygge lista.
- Fortsettelse: delt ved setningsgrensen nærmest ordmidten, som i fase A. Andre halvdel er menneskereferansen.
- Emne = første setning i et trukket avsnitt. Menneskereferansen for fritekst er hele kildeavsnittet. Det er en registerforskjell (avis mot faktatekst/fortelling), så fritekst-LPR er beskrivende.

## 3. Oppgaver og prompter (ordrett)
- T1 fortsettelse: «Fortsett denne teksten på {bokmål|nynorsk} med omtrent like mange ord som det som står: {første halvdel}»
- T2 faktatekst (emneindeks 0–24 etter stokking; validering 0–9): «Skriv en faktatekst på {bokmål|nynorsk} på 150–250 ord om temaet i denne setningen: «{emne}»»
- T3 kort fortelling (emneindeks 25–49; validering 10–19): «Skriv en kort fortelling på {bokmål|nynorsk} på 150–250 ord med utgangspunkt i denne setningen: «{emne}»»
- Valideringsemner gir T2/T3-tekster (KI-tekster for validering).

## 4. Modeller og mekanisme
- Claude: claude-opus-5-5 via Claude Code-subagent av typen Explore, 5 oppgaver per kall med rammen «Les fila … Løs hver oppgave for seg, uavhengig av de andre. Svar bare med … ===SVAR N===». Svaret hentes fra transkriptet med skript/hent_handback.py. `claude -p` kunne ikke brukes (AVVIK B1).
- NorMistral: `hf.co/ltg/normistral-7b-warm-instruct:Q4_K_M` (ollama), serielt, seed 2026, `num_predict` = 2,5 × forventede ord + 40 (T1) eller 400 (T2/T3), samme prompter.
- Lemmatisering: Stanza 1.15.1, nb/nn, `tokenize,pos,lemma`. Setningsmodell (M2): intfloat/multilingual-e5-small rev. 614241f6 (MIT).

## 5. Metrikker for lista
- **LPR (Juzek-stil):** prevalens = andelen tekster (par) der elementet forekommer minst én gang. Jeffreys: p = (c + 0,5)/(n + 1). LPR = ln(p_KI / p_M). Telleterskel: c_KI + c_M ≥ 20. Elementer: Stanza-lemma (med UPOS), lemma-bigram og lemma-trigram innenfor setninger (tegnsetting fjernet).
- Sekundært for sammenligning med Juzeks publiserte tall: Δ-prevalens = p_KI − p_M (tilsvarer «LAS/Delta_MH»).
- **Fraser, Antislop-metoden:** overflate-n-gram (n = 2–4, små bokstaver), frekvensforhold (f_KI + 1)/(f_M + 1) normalisert for korpusstørrelse. Krav: f_KI ≥ 5 og ≥ 3 ulike KI-tekster. N-gram som bare består av stoppord (de 100 hyppigste lemmaene i menneskekorpuset for varianten) fjernes.
- Beregnes per variant × modell (Claude, NorMistral) × oppgave (T1, T2+T3).
- **Inntak i liste_v1 (lag 1):** fra T1, per variant og modell, LPR ≥ ln 2 og c_KI + c_M ≥ 20. Elementet merkes «samsvar» når det passerer for både Claude og NorMistral. Egennavn (UPOS PROPN) og tall utelates. Språkrådets markører (markorer_v0, gruppe a) tas med uendret med kildehenvisning. Strukturmarkørene (gruppe b) tas med.
- liste_v1.json fryses (sha256 i loggen) før valideringsvasken.

## 6. Validering (holdt-ut sett)
- Tekster per variant: 20 KI (Claude T2/T3 fra valideringsemner) + 20 menneskelige avsnitt. De blandes og stokkes (seed 2026) i partier på 5. Samme partier vaskes med begge skills.
- Vask: Explore-subagent leser skillens SKILL.md og alle referansefiler. Instruks: «Fjern KI-preg fra denne teksten» + «Du kan ikke stille spørsmål tilbake, så gjør jobben fullt ut». Uttrekk: bare omskrivingsblokken.
- **M1:** markørrate per 1000 ord = (treff fra markorer_v0-regex + forekomster av liste_v1-elementer i lag 1 for varianten, talt på Stanza-lemmaer) / ord × 1000. R_skill = rate(KI etter vask med skill) / rate(menneske, uvasket).
- **M2:** cosinus før/etter (e5-small, prefiks «query: »).
- **M3:** normalisert Levenshtein på tegnnivå, før/etter, på de menneskelige tekstene.
- **Valideringsregel (ordrett):** «Den norske skillen er bedre hvis 95 % parret bootstrap-KI (10 000 trekk, seed 2026) for R_engelsk − R_norsk ligger over 0 i minst én variant, og KI for M3_norsk − M3_engelsk på menneskelig tekst ikke ligger over 0»
- Operasjonalisering:
  - Parret bootstrap per variant: KI-indekser og menneskeindekser trekkes med tilbakelegging. Samme indekser brukes for begge skills.
  - `numpy.random.default_rng(2026)`, nb før nn, R-trekk før M3-trekk.
  - M3-differansen er snittet av per-tekst-differanser.
  - «Ikke over 0» betyr nedre KI-grense ≤ 0. M3-vilkåret må holde i **begge** varianter, R-vilkåret i minst én.
  - Er menneskeraten 0 i et trekk, regnes R som +∞ hvis KI-raten > 0 og som 1 hvis begge er 0.
- Kjent sirkularitet: liste_v1 er grunnlaget for både den norske skillen og en del av M1. Derfor rapporteres R også med bare markorer_v0, beskrivende.
- Regelen anvendes mekanisk.

## 7. Forbrukstak (DEL 2)
- Tak: 12M tokens mot Max (sum av `subagent_tokens` + overslag for hovedøkta).
- Anslag ≈ 10,3M, så ingen kutt planlegges.
- Kuttrekkefølge hvis anslaget eller faktisk takt overstiger taket: fritekst 50 → 25 per variant, deretter validering 20 → 10 menneskelige tekster per variant. Fortsettelser går aldri under 240/185. Overstiger fortsettelsene alene taket, stoppes alt før generering.
- Kontrollpunkt: overstiger snittet etter de 10 første genereringskallene 62k tokens per kall, anvendes første kutt før resten kjøres.

## 8. Avvik
Alle avvik føres i AVVIK.md (seksjon «Fase B») med begrunnelse.
