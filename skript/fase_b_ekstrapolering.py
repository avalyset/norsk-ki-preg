"""Ekstrapolerer antall avsnittspar (KI-fortsettelse + ekte fortsettelse) som trengs for >= 200 lemmaer med samlet frekvens >= 20."""
import json, re, random, collections, math, unicodedata, simplemma, numpy as np
W = re.compile(r"\w+", re.U)
av = {json.loads(l)["nr"]: json.loads(l) for l in open("data/avsnitt.jsonl")}
cl = {json.loads(l)["nr"]: json.loads(l) for l in open("data/fortsettelser_claude.jsonl")}
rng = random.Random(2026); out = {}
for v in ("nb", "nn"):
    lem = lambda t: [simplemma.lemmatize(w.lower(), lang=v) for w in W.findall(unicodedata.normalize("NFC", t)) if w.isalpha()]
    par = [collections.Counter(lem(av[n]["andre"]) + lem(cl[n]["tekst"])) for n in sorted(cl) if n.startswith(v)]
    xs, ys = [], []
    for k in (10, 20, 30, 40, 50):
        vals = []
        for _ in range(200):
            c = collections.Counter()
            for p in rng.sample(par, k): c.update(p)
            vals.append(sum(1 for x in c.values() if x >= 20))
        xs.append(k); ys.append(float(np.mean(vals)))
    b, a = np.polyfit(np.log(xs[1:]), np.log(ys[1:]), 1)
    trengs = math.exp((math.log(200) - a) / b)
    tok_per_par = sum(sum(p.values()) for p in par) / len(par)
    out[v] = dict(kurve=dict(zip(xs, [round(y, 1) for y in ys])), eksponent=round(b, 3), par_for_200=int(math.ceil(trengs)), tokens_per_par=round(tok_per_par, 1))
json.dump(out, open("resultat/fase_b_ekstrapolering.json", "w"), indent=1)
print(json.dumps(out, indent=1))
