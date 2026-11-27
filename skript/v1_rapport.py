"""Skriver NKP-V1-RAPPORT_norsk-ki-preg_v1_2026-11-27.md fra resultatfilene."""
import json, hashlib
J = lambda f: json.load(open(f))
V = J("resultat/v1_validering.json"); M2 = J("resultat/v1_validering_m2.json"); B = J("resultat/v1_tilfoyelser_klassifisert.json"); T = J("resultat/v1_tokenregnskap.json")
L = J("liste_v2.json"); O = J("resultat/liste_v2_oppsummering.json"); KS = J("data/v1/ki_val_status.json")
sha = lambda f: hashlib.sha256(open(f, "rb").read()).hexdigest()
f = lambda x, d=3: f"{x:.{d}f}".replace(".", ",")
ki = lambda k: f"[{f(k[0])}; {f(k[1])}]"
r = []; A = r.append
A("# NKP v1 – rapport (norsk-ki-preg v1, 27.11.2026)\n")
b = V["beslutning"]
A(f"**Beslutning etter PREREG v2-regelen: den norske skillen er {'bedre' if b['norsk_skill_bedre'] else 'ikke bedre'}.** R-vilkåret holder i {'minst én' if b['R_minst_en'] else 'ingen'} variant, M3-vilkåret holder i {'begge' if b['M3_begge'] else 'ikke begge'}. Skill v1 endrer menneskeskrevet tekst svært lite (median M3 0,002–0,003 mot 0,27–0,34 for anti-ai-writing) og legger ikke til noe innhold (0 av 80 tekster mot 4 av 80), men senker ikke markørraten i KI-tekst mer enn anti-ai-writing.\n")
A("## 1. Hovedresultat etter PREREG v2 (20 KI + 20 menneske per variant, Wikipedia-titler som emner)\n")
A(f"KI-tekstene er 40 Claude-faktatekster, ett kall per tekst, median {sorted(KS['ord'].values())[20]} ord. Vask: 16 partier à 5, de samme for begge skills, 32 av 32 kall svarte.\n")
A("| | nb | nn |"); A("|---|---|---|")
g = lambda v, k: V[v]["v0+liste_v2"][k]
A(f"| M1 menneske (per 1000 ord) | {f(g('nb','rate_menneske'),2)} | {f(g('nn','rate_menneske'),2)} |")
A(f"| M1 KI før vask (R) | {f(g('nb','rate_KI_for_vask'),2)} ({f(g('nb','rate_KI_for_vask')/g('nb','rate_menneske'),2)}) | {f(g('nn','rate_KI_for_vask'),2)} ({f(g('nn','rate_KI_for_vask')/g('nn','rate_menneske'),2)}) |")
A(f"| M1 KI etter skill v1 (R_no) | {f(g('nb','rate_KI_etter_no'),2)} ({f(g('nb','R_no'))}) | {f(g('nn','rate_KI_etter_no'),2)} ({f(g('nn','R_no'))}) |")
A(f"| M1 KI etter anti-ai-writing (R_en) | {f(g('nb','rate_KI_etter_en'),2)} ({f(g('nb','R_en'))}) | {f(g('nn','rate_KI_etter_en'),2)} ({f(g('nn','R_en'))}) |")
A(f"| **R_en − R_no, 95 % KI** | **{f(V['nb']['R_en_minus_R_no']['est'])} {ki(V['nb']['R_en_minus_R_no']['KI'])}** | **{f(V['nn']['R_en_minus_R_no']['est'])} {ki(V['nn']['R_en_minus_R_no']['KI'])}** |")
A(f"| R-vilkår (nedre > 0) | {'ja' if V['nb']['R_vilkar'] else 'nei'} | {'ja' if V['nn']['R_vilkar'] else 'nei'} |")
A(f"| M3 menneske, median: v1 / anti-ai-writing | {f(V['nb']['M3_menneske_no']['median'],4)} / {f(V['nb']['M3_menneske_en']['median'],4)} | {f(V['nn']['M3_menneske_no']['median'],4)} / {f(V['nn']['M3_menneske_en']['median'],4)} |")
A(f"| **M3_no − M3_en, 95 % KI** | **{f(V['nb']['M3_no_minus_M3_en']['est'],4)} {ki([round(x,4) for x in V['nb']['M3_no_minus_M3_en']['KI']])}** | **{f(V['nn']['M3_no_minus_M3_en']['est'],4)} {ki(V['nn']['M3_no_minus_M3_en']['KI'])}** |")
A(f"| M3-vilkår (nedre ≤ 0) | {'ja' if V['nb']['M3_vilkar'] else 'nei'} | {'ja' if V['nn']['M3_vilkar'] else 'nei'} |")
A(f"| M2 KI: v1 / anti-ai-writing | {f(M2['nb|no|ki']['snitt'],4)} / {f(M2['nb|en|ki']['snitt'],4)} | {f(M2['nn|no|ki']['snitt'],4)} / {f(M2['nn|en|ki']['snitt'],4)} |")
A(f"| M2 menneske: v1 / anti-ai-writing | {f(M2['nb|no|menneske']['snitt'],4)} / {f(M2['nb|en|menneske']['snitt'],4)} | {f(M2['nn|no|menneske']['snitt'],4)} / {f(M2['nn|en|menneske']['snitt'],4)} |")
A(f"| Uendret av v1: KI / menneske | {V['nb']['M3_KI_no']['uendret']} / {V['nb']['M3_menneske_no']['uendret']} av 20 | {V['nn']['M3_KI_no']['uendret']} / {V['nn']['M3_menneske_no']['uendret']} av 20 |")
A(f"| Bare markorer_v0: R_no / R_en (beskrivende) | {f(V['nb']['bare_v0']['R_no'])} / {f(V['nb']['bare_v0']['R_en'])} | {f(V['nn']['bare_v0']['R_no'])} / {f(V['nn']['bare_v0']['R_en'])} |")
A("\nParret bootstrap 10 000 trekk, `default_rng(2027)`, nb før nn, R-trekk før M3-trekk. Alle R-trekk var endelige.\n")
A(f"**Regelen anvendt mekanisk:** R-vilkåret holder i ingen variant. I nb ligger KI for R_en − R_no helt under 0, altså i favør av anti-ai-writing. I nn dekker KI 0. M3-vilkåret holder i begge. **Resultat: ikke bedre.**\n")
A("Målestokken skiller nå KI fra menneske, med R før vask 1,37 (nb) og 1,11 (nn) mot 1,01 og 1,68 i fase B. Feilen ligger i skillen: grunnregelen lot 15 av 20 nb-KI og 10 av 20 nn-KI stå urørt (AVVIK V7). Når den først endrer noe, er det små stryk. anti-ai-writing skriver om alle tekstene og stryker mer, også av ord som teller i M1.\n")
A("## 2. M3: hvor mye skillen endrer menneskeskrevet tekst\n")
A(f"Median normalisert Levenshtein på de menneskelige tekstene: skill v1 {f(V['nb']['M3_menneske_no']['median'],4)} (nb) og {f(V['nn']['M3_menneske_no']['median'],4)} (nn), anti-ai-writing {f(V['nb']['M3_menneske_en']['median'],4)} og {f(V['nn']['M3_menneske_en']['median'],4)}. Differansen M3_no − M3_en er {f(V['nb']['M3_no_minus_M3_en']['est'],4)} {ki([round(x,4) for x in V['nb']['M3_no_minus_M3_en']['KI']])} (nb) og {f(V['nn']['M3_no_minus_M3_en']['est'],4)} {ki(V['nn']['M3_no_minus_M3_en']['KI'])} (nn). Skill v1 lot {V['nb']['M3_menneske_no']['uendret']} (nb) og {V['nn']['M3_menneske_no']['uendret']} (nn) av 20 menneskelige tekster stå helt uendret, anti-ai-writing ingen. Meningsbevaring (M2, e5-small): skill v1 ≥ {f(min(M2['nb|no|menneske']['snitt'],M2['nn|no|menneske']['snitt'],M2['nb|no|ki']['snitt'],M2['nn|no|ki']['snitt']),4)}, anti-ai-writing ≥ {f(min(M2['nb|en|menneske']['snitt'],M2['nn|en|menneske']['snitt'],M2['nb|en|ki']['snitt'],M2['nn|en|ki']['snitt']),4)} i snitt.\n")
A("## 3. B14: tilføyelser\n")
A("Skill v1 la til noe i **0 av 80** tekster. anti-ai-writing tilføyde navngitte kilder eller fakta som ikke står i kildeteksten i **4 av 80** tekster. Om tilskrivingen er korrekt, er ikke sjekket. Tilføyelsene er funnet maskinelt (diff mot kilden, egennavn, tall, datoer og kildeord) og deretter klassifisert ved lesing fra disk.\n")
A("| Skill | Variant | Tekster | Maskintreff | Omformulering/retting | **Tilføyd** (KI / menneske) |"); A("|---|---|---|---|---|---|")
for s, sn in (("en", "anti-ai-writing"), ("no", "norsk v1")):
    for v in ("nb", "nn"):
        t = B["tabell"].get(f"{s}|{v}", {})
        A(f"| {sn} | {v} | {t.get('n', 40)} | {t.get('maskintreff', 0)} | {t.get('OMFORMULERING', 0) + t.get('RETTING', 0)} | **{t.get('TILFØYD', 0)}** ({t.get('tilføyd_ki', 0)} / {t.get('tilføyd_menneske', 0)}) |")
A("\nTilføyelsene fra anti-ai-writing, ordrett:")
for x in B["klassifisert"]:
    if x["klasse"] == "TILFØYD": A(f"- {x['nr']}: «{x['setning'].rstrip('.')}.» Endring: {x['beskrivelse']}.")
A("\nSkill v1 hadde 0 maskintreff i alle 80 tekstene, og ingen tilføyelse ble funnet ved lesing. Én av de fire anti-ai-writing-tilføyelsene ble funnet utenom maskinen (AVVIK V9).\n")
A("## 4. Kjent begrensning: grunnregelen (AVVIK V7)\n")
A(f"Skill v1 skal la tekst uten markører stå urørt. Regelen slo til for {V['nb']['M3_KI_no']['uendret']} av 20 KI-tekster på bokmål og {V['nn']['M3_KI_no']['uendret']} av 20 på nynorsk, og det er hovedgrunnen til at R-vilkåret feiler. Terskelen i regelen er kalibrert på byggesettet (AVVIK V6). Skillen er dermed forsiktig: den bevarer menneskeskrevet tekst og legger ikke til noe, men fjerner mindre KI-preg enn anti-ai-writing. Det er ikke laget noen v2.\n")
A("## 5. Forløpere\n")
A("- **Fase A, røyktest (24.11.2026):** anti-ai-writing på norsk avistekst. Resultatet var at fase B trengtes, utløst av nynorsk. Se `NKP-ROYK-RAPPORT_norsk-ki-preg_v1_2026-11-24.md` og `BESLUTNING.md`.")
A("- **Fase B og skill v0 (24.–27.11.2026):** liste_v1 målt på avisfortsettelser, skill v0 og validering etter `PREREG.md`. Resultatet var «ikke bedre», fordi målestokken ikke skilte KI fra menneske på bokmål (R før vask 1,01; AVVIK B16). Se `NKP-FASEB-RAPPORT_norsk-ki-preg_v1_2026-11-27.md`, `liste_v1.md` og skill v0 i commit 43c1d9a. v1 retter målestokken: lista er målt på faktatekst mot Wikipedia, og valideringen bruker et nytt, urørt sett.\n")
A("## 6. PREREG og tidsstempler\n")
A(f"`PREREG_v2.md` sha256 `{sha('PREREG_v2.md')}`, låst 27.11 i commit 59c4e64 før skill v1, KI-generering og validering. OpenTimestamps: `PREREG_v2.md.ots` (commit 91da284). `ots upgrade` 27.11: v2 venter fortsatt på Bitcoin-attestasjon (AVVIK V11). PREREG v1 (`PREREG.md`, sha256 f3e13a9c…dd521df9) er fullstendig attestert i blokk 977348 og 977351. Skill v1 ble committet før første vaskekall (aab3438). `liste_v2.json` sha256 `{sha('liste_v2.json')}`.\n")
A("## 7. Menneskelig referanse: dato og lisens\n")
A("Kilde: NCC (NbAiLab/NCC), validation-shard-0001, `wikipedia_download_nbo` og `wikipedia_download_nno`. Lisensen står i NCC-kortet (`kilder/ncc/NCC_README.md`, ikke med i deponeringstarballen, AVVIK V12), ordrett: «| Wikipedia | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) |».\n")
A("Dato (AVVIK V1, godtatt): kortet sier ordrett «Build date original corpus: 21012022». Det er den dokumenterte øvre grensen for dumpen, før 30.11.2022. Innholdet bekrefter det: daterte omtaler av 2021 stopper i juli og august 2021, omtaler av 2022 gjelder planlagte hendelser, og det er 0 treff på regjeringen Støre (14.10.2021), invasjonen av Ukraina, Elizabeth IIs død og ChatGPT.\n")
A("Utvalg (seed 2027, ett avsnitt per artikkel, 80–250 ord, prosafilter, AVVIK V2–V3): nb 1435 kandidater (20 til validering, 1415 til bygging), nn 773 (20 / 753).\n")
A("## 8. liste_v2\n")
A(f"KI: T2-faktatekster fra fase B, 35 per modell og variant (Claude Opus 5.5 og NorMistral-7B). Menneske: byggesettet ≥ 150 ord (nb 936, nn 480), AVVIK V4. Telleterskel c ≥ {L['terskel']}, {'senket' if L['terskel_senket'] else 'ikke senket'}.\n")
A("| Variant | Lemma | Bigram | Trigram | Samsvar (L/B/T) | Over terskelen før LPR-krav, lemma (Claude / NorMistral) |"); A("|---|---|---|---|---|---|")
for v in ("nb", "nn"):
    i, s, p = O[v]["inntak"], O[v]["samsvar"], O[v]["over_terskel_per_modell"]
    A(f"| {v} | {i['lemma']} | {i['bigram']} | {i['trigram']} | {s['lemma']}/{s['bigram']}/{s['trigram']} | {p['claude']['lemma']} / {p['lokal']['lemma']} |")
A("")
for v, n in (("nb", "Bokmål"), ("nn", "Nynorsk")):
    o = L["varianter"][v]; top = sorted([x for x in o["lemma"] if "claude" in x["modeller"]], key=lambda x: -x["claude_lpr"])[:30]
    A(f"**{n}, topp 30 lemmaer (Claude; c_KI av 35 / c_M av {O[v]['n']['claude'][1]}; LPR; ✓ = samsvar):** " + " · ".join(f"{x['e']} {x['claude_c_KI']}/{x['claude_c_M']} {f(x['claude_lpr'],2)}{' ✓' if x['samsvar'] else ''}" for x in top) + "\n")
A("Lista domineres av lim- og registerord (`likevel`, `derfor`/`difor`, `samtidig`/`samstundes`, `gjerne`, `hvordan`/`korleis`, `viktig`, `bidra til`, `for eksempel`) og en del emneord. Full liste med NorMistral-tall og bigram står i `liste_v2.md`.\n")
A("## 9. Forbruk (sum per forespørsel, deduplisert på message.id)\n")
A("| Ledd | Kall | Forespørsler | Input | Cache-skriving | Cache-lesing | Output | Sum | Uten cache-lesing |"); A("|---|---|---|---|---|---|---|---|---|")
for k, n in (("generering", "KI-generering (41 kall, ett per tekst + ett nytt forsøk)"), ("vask_no", "Vask, skill v1"), ("vask_en", "Vask, anti-ai-writing"), ("hovedøkt", "Hovedøkt (10:03–10:41Z)")):
    x = T[k]; A(f"| {n} | {x['kall']} | {x['forespørsler']} | {x['input_tokens']:,} | {x['cache_creation_input_tokens']:,} | {x['cache_read_input_tokens']:,} | {x['output_tokens']:,} | {x['sum']:,} | {x['uten_cache_lesing']:,} |".replace(",", " "))
a = T["alle"]; A(f"| **Alt** | | {a['forespørsler']} | {a['input_tokens']:,} | {a['cache_creation_input_tokens']:,} | {a['cache_read_input_tokens']:,} | {a['output_tokens']:,} | **{a['sum']:,}** | **{a['uten_cache_lesing']:,}** |".replace(",", " "))
A("\nHvilket mål som tilsvarer forbruk mot Max, kan ikke avgjøres fra loggene (AVVIK B12). Ingen betalte API-er, ingen nøkler, ingen push. Lokalt: Stanza og e5-small på CPU, NCC-strømming (gratis).\n")
A("## 10. AVVIK (v1, fullstendig i AVVIK.md)\n")
for t in ["V1 Øvre grense for Wikipedia-dumpen: NCC-kortets byggedato 21.01.2022, bekreftet av innholdet (godtatt).",
          "V2 «Avsnitt» = innledende prosablokk, fordi NCC-teksten ikke har linjeskift.", "V3 Kjentordterskel 0,70 for nn (simplemma-dekning 74 %).",
          "V4 liste_v2: 35 KI-tekster per modell (med de tidligere valideringsemnene), byggesettet ≥ 150 ord.", "V5 Rensing av overskriftslinjer og «---»-merknader i KI-tekstene. Holsdagen besvart på andre forsøk.",
          "V6 Terskelen i grunnregelen er kalibrert på byggesettet (optimistisk).", "V7 Skill v1 lot 25 av 40 KI-tekster stå urørt. Det er hovedgrunnen til at R-vilkåret feiler.",
          "V8 Rester av markup i valideringsavsnittene gir høyere M3 for anti-ai-writing.", "V9 anti-ai-writing endrer fakta fra egen kunnskap. Én av fire tilføyelser ble funnet utenom maskinen.", "V10 Forbruket i hovedøkta er målt til kjøretidspunktet.", "V11 OTS for PREREG v2 er ikke attestert ennå.", "V12 Lisensvalg for pakken."]:
    A(f"- {t}")
A("")
open("NKP-V1-RAPPORT_norsk-ki-preg_v1_2026-11-27.md", "w").write("\n".join(r)); print(len(r))
