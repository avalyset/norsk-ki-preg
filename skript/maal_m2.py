"""M2: meningsbevaring, cosinus før/etter vask med intfloat/multilingual-e5-small (MIT, rev 614241f6)."""
import json, numpy as np
from sentence_transformers import SentenceTransformer
m = SentenceTransformer("intfloat/multilingual-e5-small", revision="614241f622f53c4eeff9890bdc4f31cfecc418b3", device="cpu")
av = {json.loads(l)["nr"]: json.loads(l) for l in open("data/avsnitt.jsonl")}
cl = {json.loads(l)["nr"]: json.loads(l) for l in open("data/fortsettelser_claude.jsonl")}
lo = {json.loads(l)["nr"]: json.loads(l) for l in open("data/fortsettelser_lokal.jsonl")}
vask = [json.loads(l) for l in open("data/vasket.jsonl")]
def emb(T): return m.encode(["query: " + t for t in T], normalize_embeddings=True, batch_size=8)
før = [av[d["nr"]]["andre"] if d["kilde"] == "menneske" else cl[d["nr"]]["tekst"] for d in vask]
E1, E2 = emb(før), emb([d["tekst"] for d in vask])
cos = (E1 * E2).sum(1)
res = {"modell": "intfloat/multilingual-e5-small@614241f6 (MIT)", "prefiks": "query: ", "per_tekst": [], "sammendrag": {}}
for d, c in zip(vask, cos): res["per_tekst"].append({"nr": d["nr"], "kilde": d["kilde"], "variant": d["variant"], "cos": round(float(c), 4)})
# referanse: cosinus mellom ekte andre halvdel og Claude-fortsettelse (to ulike tekster om samme sak)
nrs = sorted(cl); Ea, Ec = emb([av[n]["andre"] for n in nrs]), emb([cl[n]["tekst"] for n in nrs])
ref = (Ea * Ec).sum(1)
for v in ("nb", "nn"):
    for k in ("claude", "menneske"):
        x = [r["cos"] for r in res["per_tekst"] if r["variant"] == v and r["kilde"] == k]
        res["sammendrag"][f"{v}|{k} før→etter vask"] = dict(n=len(x), snitt=round(float(np.mean(x)), 4), min=round(float(np.min(x)), 4))
    x = [float(c) for n, c in zip(nrs, ref) if n.startswith(v)]
    res["sammendrag"][f"{v}|referanse: fasit vs Claude-fortsettelse"] = dict(n=len(x), snitt=round(float(np.mean(x)), 4), min=round(float(np.min(x)), 4))
json.dump(res, open("resultat/m2.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps(res["sammendrag"], ensure_ascii=False, indent=1))
