"""Skill v1: skriver references/lag1-overbruk-{nb,nn}.md fra liste_v2.json.
Med i skillen: alle lemmaer som ikke er substantiv, substantiv bare ved samsvar (andre substantiv er trolig emneord), alle bigram/trigram, Antislop-fraser."""
import json
L = json.load(open("liste_v2.json")); OK = {"ADV": "adverb", "SCONJ": "subjunksjon", "CCONJ": "konjunksjon", "ADP": "preposisjon", "AUX": "hjelpeverb", "VERB": "verb", "ADJ": "adjektiv", "DET": "determinativ", "PRON": "pronomen", "NOUN": "substantiv"}
for v, navn in (("nb", "bokmål"), ("nn", "nynorsk")):
    o = L["varianter"][v]; lpr = lambda r: max(r.get("claude_lpr", -9), r.get("lokal_lpr", -9))
    lem = [r for r in o["lemma"] if r["e"].rsplit("_", 1)[1] in OK and (r["e"].endswith("_NOUN") is False or r["samsvar"])]
    lem.sort(key=lambda r: (-r["samsvar"], -lpr(r)))
    g = lambda r: f"{r['e'].rsplit('_', 1)[0]} ({OK[r['e'].rsplit('_', 1)[1]]})"
    ut = [f"# Lag 1 – målte overbruksmønstre, {navn} (liste_v2)", "",
          "Fra liste_v2 (norsk-ki-preg, 27.11.2026): KI-faktatekster (Claude Opus 5.5 og NorMistral-7B) målt mot innledende prosaavsnitt i norsk Wikipedia. Elementene er **overbrukt** i KI-faktatekst, men ikke feil. Hvert ord er vanlig norsk.", "",
          "Bruk dem slik:",
          "- **Bare opphopning teller.** Ett eller to av ordene i en tekst er normalt. Først når flere av dem står tett, i samme avsnitt eller som faste koblinger mellom setninger, er det et KI-preg.",
          "- Rett opphopningen ved å stryke ord som ikke bærer innhold («likevel», «derfor», «samtidig», «gjerne» brukt som lim) eller ved å skrive setningen enklere. Bytt aldri et ord mot et nytt ord som tilfører innhold.",
          "- Substantiv er bare med når begge modellene overbruker dem. Andre substantiv i målingen var trolig emneord og er utelatt.", "",
          "## Ord (lemma), sterkest først; ✓ = overbrukt av begge modellene", ""]
    ut.append(", ".join(("✓ " if r["samsvar"] else "") + g(r) for r in lem[:90]))
    big = sorted(o["bigram"], key=lambda r: (-r["samsvar"], -lpr(r)))[:50]; tri = o["trigram"]
    ut += ["", "## Ordpar og ordtripler (lemmaform), sterkest først", "", ", ".join(("✓ " if r["samsvar"] else "") + f"«{r['e']}»" for r in big)]
    if tri: ut += ["", ", ".join(("✓ " if r["samsvar"] else "") + f"«{r['e']}»" for r in tri)]
    fr = [x for n in ("4", "3", "2") for x in o["antislop_claude_T2"][n] if x["f_KI"] >= 5][:25]
    ut += ["", "## Faste fraser i Claude-faktatekst (overflateform, antall i KI / i referansen)", "", "; ".join(f"«{x['e']}» {x['f_KI']}/{x['f_M']}" for x in fr), ""]
    open(f"skills/norsk-ki-preg/references/lag1-overbruk-{v}.md", "w").write("\n".join(ut))
    print(v, len(lem), "lemma i skill av", len(o["lemma"]), "bigram", len(big), "trigram", len(tri), "fraser", len(fr))
