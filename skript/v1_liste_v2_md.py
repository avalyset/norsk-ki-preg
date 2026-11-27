"""Skriver liste_v2.md fra liste_v2.json og resultat/liste_v2_oppsummering.json."""
import json, hashlib
L = json.load(open("liste_v2.json")); O = json.load(open("resultat/liste_v2_oppsummering.json"))
sha = hashlib.sha256(open("liste_v2.json", "rb").read()).hexdigest()
ut = [f"# liste_v2 – målt KI-overbruk i norsk faktatekst (bokmål og nynorsk)\n",
      f"Versjon v2, 27.11.2026. `liste_v2.json` sha256 `{sha}`.\n",
      "## Slik er lista laget\n",
      "- KI-tekster: faktatekstene (T2) fra fase B, 35 per modell og variant (25 fritekst-emner + 10 tidligere valideringsemner), fra Claude Opus 5.5 og NorMistral-7B. Ingen ny generering.",
      "- Menneskereferanse: innledende prosaavsnitt fra NCC `wikipedia_download_nbo`/`_nno` (CC BY-SA 3.0), byggesettet, bare avsnitt på minst 150 ord for å matche KI-lengden (nb 936, nn 480). De 20 valideringsavsnittene per variant er ikke brukt.",
      f"- Mål som i PREREG v1 §5: Stanza-lemma med UPOS, lemma-bi- og trigram innen setning, prevalens over tekster med Jeffreys-glatting, LPR = ln(p_KI/p_M). Inntak: LPR ≥ ln 2 og c_KI + c_M ≥ {L['terskel']} for minst én modell. Egennavn og tall er utelatt. «Samsvar» = passerer for begge modeller.",
      f"- Telleterskelen ble {'senket til 10' if L['terskel_senket'] else 'ikke senket (≥ 50 elementer per variant ved 20)'}.\n",
      "## Antall elementer\n", "| Variant | Lemma | Bigram | Trigram | Samsvar (lemma/bigram/trigram) | Over terskelen før LPR-krav (Claude / NorMistral, lemma) |", "|---|---|---|---|---|---|"]
for v in ("nb", "nn"):
    i, s, p = O[v]["inntak"], O[v]["samsvar"], O[v]["over_terskel_per_modell"]
    ut.append(f"| {v} | {i['lemma']} | {i['bigram']} | {i['trigram']} | {s['lemma']}/{s['bigram']}/{s['trigram']} | {p['claude']['lemma']} / {p['lokal']['lemma']} |")
ut += ["", "## Forbehold\n",
       "1. Små KI-utvalg (35 per modell). En prevalens på 5 av 35 er nok for inntak når elementet er sjeldent i Wikipedia.",
       "2. Emnene i KI-tekstene kommer fra avisavsnitt, mens Wikipedia dekker andre emner. Emneord (`fotball`, `kommune`, `klubb`, `fylke`, `skule`) er derfor med. De er ikke stiltrekk, og skillen behandler dem bare som del av en opphopning.",
       "3. Lista sier at et ord er vanligere i KI-faktatekst enn i Wikipedia-prosa. Den sier ikke at ordet er feil.", ""]
for v, navn in (("nb", "Bokmål"), ("nn", "Nynorsk")):
    o = L["varianter"][v]
    ut += [f"## {navn}\n", "**Samsvar (begge modeller), lemma:** " + ", ".join(f"`{r['e']}`" for r in o["lemma"] if r["samsvar"]), "",
           "**Samsvar, bigram:** " + ", ".join(f"«{r['e']}»" for r in o["bigram"] if r["samsvar"]), "",
           "**Topp 30 lemmaer, Claude** (c = antall tekster av 35 KI / av referansen):\n", "| # | lemma | c_KI | c_M | LPR | Δ-prevalens | samsvar |", "|---|---|---|---|---|---|---|"]
    top = sorted([r for r in o["lemma"] if "claude" in r["modeller"]], key=lambda r: -r["claude_lpr"])[:30]
    for k, r in enumerate(top, 1): ut.append(f"| {k} | {r['e']} | {r['claude_c_KI']} | {r['claude_c_M']} | {r['claude_lpr']} | {r['claude_delta']} | {'✓' if r['samsvar'] else ''} |")
    ut += ["", "**Topp 30 lemmaer, NorMistral:**\n", "| # | lemma | c_KI | c_M | LPR | samsvar |", "|---|---|---|---|---|---|"]
    top = sorted([r for r in o["lemma"] if "lokal" in r["modeller"]], key=lambda r: -r["lokal_lpr"])[:30]
    for k, r in enumerate(top, 1): ut.append(f"| {k} | {r['e']} | {r['lokal_c_KI']} | {r['lokal_c_M']} | {r['lokal_lpr']} | {'✓' if r['samsvar'] else ''} |")
    big = sorted([r for r in o["bigram"] if "claude" in r["modeller"]], key=lambda r: -r["claude_lpr"])[:20]
    ut += ["", "**Topp 20 bigram, Claude:** " + "; ".join(f"«{r['e']}» {r['claude_c_KI']}/{r['claude_c_M']} ({r['claude_lpr']})" for r in big), ""]
    ut += ["**Fraser (Antislop, Claude, f_KI/f_M):** " + "; ".join(f"«{x['e']}» {x['f_KI']}/{x['f_M']}" for n in ("2", "3", "4") for x in o["antislop_claude_T2"][n][:8]), ""]
ut += ["## Språkrådets markører og strukturmarkører\n", "Uendret fra markorer_v0.json. Kilde for gruppe a: Språkrådet (2025), rapporten om KI-generert norsk tekst (sidetall i markorer_v0.json). Gruppe b er strukturmarkører fra fase A.\n"]
for m in L["sprakradet_markorer"]: ut.append(f"- `{m['id']}` ({m.get('gruppe', '')}): {m.get('kilde', '')}" + (f", s. {m['side']}" if m.get('side') else ""))
open("liste_v2.md", "w").write("\n".join(ut) + "\n"); print(len(ut), "linjer")
