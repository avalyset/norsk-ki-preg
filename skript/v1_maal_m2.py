"""M2 validering: cosinus før/etter vask (e5-small, 'query: '), per variant × skill × kilde."""
import json, numpy as np
from sentence_transformers import SentenceTransformer
m = SentenceTransformer("intfloat/multilingual-e5-small", revision="614241f622f53c4eeff9890bdc4f31cfecc418b3", device="cpu")
U, C = {}, {}
for v in ("nb", "nn"):
    for l in open(f"data/v1/wiki_{v}.jsonl"):
        d = json.loads(l)
        if d["rolle"] == "val": U[d["nr"]] = d
    for l in open(f"data/v1/ki_val_{v}.jsonl"): d = json.loads(l); C[d["nr"]] = d
V = [json.loads(l) for l in open("data/v1/vasket.jsonl")]
for d in V: d["tekst"] = d["tekst"] if d["tekst"] is not None else (U.get(d["nr"]) or C[d["nr"]])["tekst"]
før = [U[d["nr"]]["tekst"] if d["kilde"] == "menneske" else C[d["nr"]]["tekst"] for d in V]
E1 = m.encode(["query: " + t for t in før], normalize_embeddings=True, batch_size=8); E2 = m.encode(["query: " + d["tekst"] for d in V], normalize_embeddings=True, batch_size=8)
cos = (E1 * E2).sum(1); res = {}
for d, c in zip(V, cos): res.setdefault(f"{d['variant']}|{d['skill']}|{d['kilde']}", []).append(float(c))
out = {k: dict(n=len(x), snitt=round(float(np.mean(x)), 4), min=round(float(np.min(x)), 4)) for k, x in sorted(res.items())}
json.dump(out, open("resultat/v1_validering_m2.json", "w"), indent=1); print(json.dumps(out, indent=1))
