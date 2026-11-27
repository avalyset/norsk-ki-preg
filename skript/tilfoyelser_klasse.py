"""B14 trinn 2: manuell klassifisering (lest fra disk 27.11, ingen modellkall) av hvert maskintreff i resultat/tilfoyelser.json.
Klasser: TILFØYD (finnes ikke i kilden i noen form), OCR (rekonstruksjon av skadet ord/tall i kilden), OMFORMULERING (samme innhold, nye ord)."""
import json, re, collections
K = {  # (skill, nr): (klasse, kildeform)
 ("en", "nb-val_emne-004"): ("TILFØYD", "Forskere har pekt på at"),
 ("en", "nb-val_emne-007"): ("TILFØYD", "Språkforskere har vist at"),
 ("en", "nb-val_emne-006"): ("TILFØYD", "Forskning på såkalt tilskuereffekt viser"),
 ("en", "nb-val_emne-005"): ("OMFORMULERING", "Mange unge flytter ut for å ta utdanning eller finne arbeid, mens de eldre b[lir]"),
 ("en", "nb-val_emne-008"): ("OMFORMULERING", "kan selv små forskjeller, som en enkelt bokstav, vekke sterke følelser"),
 ("en", "nb-val_emne-014"): ("OMFORMULERING", "Riksteater-forestilling / Riksteateret"),
 ("en", "nb-val_menneske-009"): ("OCR", "garn kan det … / pålBoo-1900-tallet / ikke-vestlige land"),
 ("no", "nb-val_menneske-009"): ("OCR", "pålBoo-1900-tallet"),
 ("en", "nb-val_menneske-015"): ("OCR", "Tbrgersen"), ("no", "nb-val_menneske-015"): ("OCR", "Tbrgersen"),
 ("en", "nb-val_menneske-008"): ("OCR", "I3.mars"), ("no", "nb-val_menneske-008"): ("OCR", "I3.mars"),
 ("en", "nn-val_menneske-005"): ("OCR", "i. juli"), ("no", "nn-val_menneske-005"): ("OCR", "i. juli"),
 ("en", "nn-val_menneske-004"): ("OCR", "Stats lause:2ol"), ("no", "nn-val_menneske-004"): ("OCR", "Stats lause:2ol"),
 ("en", "nn-val_menneske-007"): ("OCR", "Faksmile"), ("no", "nn-val_menneske-007"): ("OCR", "Faksmile"),
 ("en", "nn-val_menneske-012"): ("OCR", "Øog Fjordane"), ("no", "nn-val_menneske-012"): ("OCR", "Øog Fjordane"),
 ("no", "nn-val_menneske-014"): ("OCR", "1850-19 60-talet"),
}
# Funnet utenom maskinen (tallord fanges ikke av sifferregexen): endret faktapåstand
EKSTRA = [("en", "nn-val_emne-000", "TILFØYD", "nesten tre hundre år", "over tre hundre år")]
T = json.load(open("resultat/tilfoyelser.json"))
treff = [x for x in T if x["egennavn"] or x["tall"] or x["dato"] or x["nye_setninger"]]
manglar = [(x["skill"], x["nr"]) for x in treff if (x["skill"], x["nr"]) not in K]
assert not manglar, manglar
W = {(d["skill"], d["nr"]): d["tekst"] for d in map(json.loads, open("data/b_vasket.jsonl"))}
def setning(t, ord_):
    for s in re.split(r"(?<=[.!?»])\s+", t):
        if ord_ in s: return s.strip()
ut = []
for x in treff:
    kl, kf = K[(x["skill"], x["nr"])]; nøkkel = (x["egennavn"] or x["tall"] or [None])[0]
    ut.append(dict(skill=x["skill"], nr=x["nr"], variant=x["variant"], kilde=x["kilde"], klasse=kl, kildeform=kf,
                   treff=dict(egennavn=x["egennavn"], tall=x["tall"], dato=x["dato"], nye_setninger=len(x["nye_setninger"])),
                   setning=setning(W[(x["skill"], x["nr"])], nøkkel) if nøkkel else x["nye_setninger"][0]))
for s, nr, kl, kf, ny in EKSTRA:
    ut.append(dict(skill=s, nr=nr, variant=nr[:2], kilde="ki", klasse=kl, kildeform=kf, treff="utenom maskinen (tallord)", setning=setning(W[(s, nr)], ny)))
tab = collections.defaultdict(collections.Counter)
for x in T: tab[(x["skill"], x["variant"])]["n"] += 1
for x in treff: tab[(x["skill"], x["variant"])]["maskintreff"] += 1
for x in ut:
    if x["klasse"] == "TILFØYD": tab[(x["skill"], x["variant"])]["tilføyd"] += 1
    tab[(x["skill"], x["variant"])][x["klasse"]] += 1
json.dump(dict(klassifisert=ut, tabell={"|".join(k): dict(v) for k, v in sorted(tab.items())}), open("resultat/tilfoyelser_klassifisert.json", "w"), ensure_ascii=False, indent=1)
for k, v in sorted(tab.items()): print(k, dict(v))
for x in ut: print(x["skill"], x["nr"], x["klasse"], "|", x["setning"], "| kilde:", x["kildeform"])
