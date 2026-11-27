"""v1 B14 trinn 2 (PREREG v2 §6): klassifisering, lest fra disk 27.11 uten modellkall, av hvert maskintreff i resultat/v1_tilfoyelser.json.
TILFØYD = navn/tall/dato/kilde/påstand som ikke finnes i kilden i noen form (også endret faktapåstand fra egen kunnskap);
OMFORMULERING = samme innhold med andre ord; RETTING = rettet skrivefeil/stavemåte i kilden."""
import json, collections, re
K = {
 ("en", "nb-ki-0003"): ("TILFØYD", "«Ifølge en kjent fortelling» → «Ifølge Giorgio Vasari»"),
 ("en", "nb-wiki-0003"): ("TILFØYD", "«som representerte Michelangelo i Roma» → «som var den franske kongens utsending i Roma» (endret påstand)"),
 ("en", "nn-wiki-0003"): ("TILFØYD", "«differensiell form av fysisk integrering» → «ein variasjonsmetode», «kvantekostnadene» → «ladningskvantet» o.a. (påstander byttet ut fra egen kunnskap)"),
 ("en", "nb-wiki-0016"): ("OMFORMULERING", "«siste halvdel av 1800-tallet» → «mellom 1850 og 1900»"),
 ("en", "nb-wiki-0019"): ("OMFORMULERING", "«De forteller at» → «Ifølge gruppen selv»"),
 ("en", "nb-wiki-0002"): ("OMFORMULERING", "«Fra 1.1. 2020» → «1. januar 2020»; prostata-eksempelet omformet"),
 ("en", "nb-wiki-0010"): ("OMFORMULERING", "«datteren … som Sara har sammen med sin eksmann» → «Faren er Saras eksmann»"),
 ("en", "nb-wiki-0006"): ("OMFORMULERING", "«PR-katastrofe» → «skandale i pressen»; «Alex'» genitiv"),
 ("en", "nb-wiki-0015"): ("OMFORMULERING", "«det er trolig at … kommer fra klassisismen» → «stammer trolig fra klassisismen»"),
 ("en", "nb-wiki-0014"): ("OMFORMULERING", "«sju større chakraer» → «sju hovedchakraer»"),
 ("en", "nb-wiki-0000"): ("RETTING", "«Bagdat» → «Bağdat»; «midt på 1300-tallet» → «rundt 1350» (omformulering)"),
 ("en", "nb-ki-0000"): ("OMFORMULERING", "«600-tallet» → «det 7. århundre»"),
 ("en", "nn-wiki-0012"): ("OMFORMULERING", "«ca. 140 km2» → «om lag 140 km²»"),
 ("en", "nn-wiki-0014"): ("OMFORMULERING", "omskriving av setningen om bussane"),
}
EKSTRA = [("en", "nb-wiki-0007", "TILFØYD", "«grensa mot Meldal» → «grensa mot Orkland» (endret påstand fra egen kunnskap, ikke fanget maskinelt)", "grensa mot Orkland")]
T = json.load(open("resultat/v1_tilfoyelser.json"))
treff = [x for x in T if x["egennavn"] or x["tall"] or x["dato"] or x["kilde_ord"] or x["nye_setninger"]]
mangler = [(x["skill"], x["nr"]) for x in treff if (x["skill"], x["nr"]) not in K]; assert not mangler, mangler
W = {(d["skill"], d["nr"]): d["tekst"] for d in map(json.loads, open("data/v1/vasket.jsonl"))}
def setning(t, o):
    for s in re.split(r"(?<=[.!?»])\s+(?=[A-ZÆØÅ«])", t or ""):
        if o in s: return s.strip()
ut = [dict(skill=s, nr=n, klasse=K[(s, n)][0], beskrivelse=K[(s, n)][1], kilde="ki" if "-ki-" in n else "menneske", variant=n[:2]) for (s, n) in [(x["skill"], x["nr"]) for x in treff]]
for s, n, kl, b, o in EKSTRA: ut.append(dict(skill=s, nr=n, klasse=kl, beskrivelse=b, kilde="menneske", variant=n[:2], setning=setning(W[(s, n)], o), maskinelt=False))
for x in ut:
    x.setdefault("maskinelt", True)
    if x["klasse"] == "TILFØYD" and "setning" not in x:
        o = {"nb-ki-0003": "Vasari", "nb-wiki-0003": "utsending", "nn-wiki-0003": "variasjonsmetode"}[x["nr"]]; x["setning"] = setning(W[(x["skill"], x["nr"])], o)
tab = collections.defaultdict(collections.Counter)
for x in T: tab[(x["skill"], x["variant"])]["n"] += 1
for x in treff: tab[(x["skill"], x["variant"])]["maskintreff"] += 1
for x in ut:
    tab[(x["skill"], x["variant"])][x["klasse"]] += 1
    if x["klasse"] == "TILFØYD": tab[(x["skill"], x["variant"])]["tilføyd_" + x["kilde"]] += 1
json.dump(dict(klassifisert=ut, tabell={"|".join(k): dict(v) for k, v in sorted(tab.items())}), open("resultat/v1_tilfoyelser_klassifisert.json", "w"), ensure_ascii=False, indent=1)
for k, v in sorted(tab.items()): print(k, dict(v))
for x in ut:
    if x["klasse"] == "TILFØYD": print(x["nr"], "|", x["setning"])
