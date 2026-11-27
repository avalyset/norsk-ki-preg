"""v1 (PREREG v2 §6, B14-målet): maskinell telling av tilføyde egennavn, tall, datoer og nye påstander (proxy) i vaskede tekster, mot kildeteksten.
Ingen modellkall: bruker Stanza-cachen (skript/lemmatiser.py) og regex.
- egennavn: token med UPOS PROPN og stor forbokstav der verken form eller lemma finnes i kilden
  (kilden sammenlignes også uten mellomrom, så OCR-delte ord som «ung dommane» ikke gir falske treff).
  Setningsinitiale PROPN som finnes som vanlig ord (ikke-PROPN-lemma) i korpuscachen, telles ikke.
- tall: sifferstreng (tusenskille fjernet) som ikke finnes i kildens sifferstrenger.
- dato: tilføyd måneds- eller ukedagsnavn, eller tilføyd årstall 1000–2099.
- ny påstand (proxy): setning med ≥ 3 innholdslemmaer (NOUN/PROPN/NUM/ADJ/VERB) der ≥ 50 % ikke finnes i kilden.
"""
import json, re, sys, collections, unicodedata
sys.path.insert(0, "skript")
from lemmatiser import analyser, _cache
nfc = lambda t: unicodedata.normalize("NFC", t)
U, C = {}, {}
for v in ("nb", "nn"):
    for l in open(f"data/v1/wiki_{v}.jsonl"):
        d = json.loads(l)
        if d["rolle"] == "val": U[d["nr"]] = d
    for l in open(f"data/v1/ki_val_{v}.jsonl"): d = json.loads(l); C[d["nr"]] = d
V = [json.loads(l) for l in open("data/v1/vasket.jsonl")]
for d in V: d["tekst"] = d["tekst"] if d["tekst"] is not None else (U.get(d["nr"]) or C[d["nr"]])["tekst"]
VANLIG = {}
for v in ("nb", "nn"):
    VANLIG[v] = {lem for s in _cache(v).values() for sen in s for (f, lem, up) in sen if up not in ("PROPN", "X")}
MND = r"januar|februar|mars|april|mai|juni|juli|august|september|oktober|november|desember|mandag|tirsdag|onsdag|torsdag|fredag|lørdag|søndag|måndag|tysdag|laurdag|sundag"
def tall(t):
    t = re.sub(r"(?<=\d)[ .  ](?=\d{3}\b)", "", t)
    return re.findall(r"\d+(?:,\d+)?", t)
INNH = {"NOUN", "PROPN", "NUM", "ADJ", "VERB"}
ut = []
for d in V:
    v = d["variant"]; kilde = (C[d["nr"]] if d["kilde"] == "ki" else U[d["nr"]])["tekst"]
    k, r = nfc(kilde), nfc(d["tekst"])
    kl = k.lower(); kns = re.sub(r"[\s\-­]", "", kl)
    ka = analyser(kilde, v); ra = analyser(d["tekst"], v)
    klem = {lem for sen in ka for (f, lem, up) in sen}
    finnes = lambda f, lem: f.lower() in kl or re.sub(r"[\s\-]", "", f.lower()) in kns or lem in klem or (len(lem) > 2 and lem in kns)
    navn = []
    for sen in ra:
        for i, (f, lem, up) in enumerate(sen):
            if up != "PROPN" or not f[:1].isupper(): continue
            if i == 0 and lem in VANLIG[v]: continue
            if not finnes(f, lem): navn.append(f)
    kt = set(tall(k)); nye_tall = [x for x in tall(r) if x not in kt]
    dato = [m for m in re.findall(rf"\b({MND})\b", r, re.I) if m.lower() not in kl]
    dato += [x for x in nye_tall if re.fullmatch(r"1\d{3}|20\d{2}", x)]
    KILDE = r"\bifølge\b|\bi følgje\b|\bviser tal+ fr[åa]\b|\bkilde:|\brapport(?:en)? fr[åa]\b|\bstudie\w*|\bundersøk(?:ing|else)\w*"
    kilder = [m.group(0) for m in re.finditer(KILDE, r, re.I) if m.group(0).lower() not in kl]
    påst = []
    for sen in ra:
        inn = [(f, lem) for (f, lem, up) in sen if up in INNH]
        if len(inn) >= 3:
            nye = [f for f, lem in inn if not finnes(f, lem)]
            if len(nye) / len(inn) >= 0.5: påst.append(" ".join(f for f, _, _ in sen))
    ut.append(dict(skill=d["skill"], variant=v, kilde=d["kilde"], nr=d["nr"], egennavn=sorted(set(navn)), tall=sorted(set(nye_tall)), kilde_ord=sorted(set(x.lower() for x in kilder)),
                   dato=sorted(set(x.lower() for x in dato)), nye_setninger=påst))
json.dump(ut, open("resultat/v1_tilfoyelser.json", "w"), ensure_ascii=False, indent=1)
tab = collections.defaultdict(lambda: collections.Counter())
for x in ut:
    for g in ((x["skill"], x["variant"], x["kilde"]), (x["skill"], x["variant"], "alle"), (x["skill"], "alle", "alle")):
        c = tab[g]; c["n"] += 1
        for f in ("egennavn", "tall", "dato", "kilde_ord", "nye_setninger"): c[f] += bool(x[f])
        c["navn_tall_dato_kilde"] += bool(x["egennavn"] or x["tall"] or x["dato"] or x["kilde_ord"]); c["noe"] += bool(x["egennavn"] or x["tall"] or x["dato"] or x["kilde_ord"] or x["nye_setninger"])
for g in sorted(tab): print(g, dict(tab[g]))
json.dump({"|".join(g): dict(c) for g, c in tab.items()}, open("resultat/v1_tilfoyelser_tabell.json", "w"), indent=1)
