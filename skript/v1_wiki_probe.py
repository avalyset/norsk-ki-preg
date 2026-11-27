"""v1 steg 1: undersøk Wikipedia-dokumentene i NCC validation (id, doc_type, publish_year) for å dokumentere dumpdato."""
import json, sys, collections, requests
from huggingface_hub import hf_hub_url
fil = sys.argv[1]; N = collections.Counter(); Å = collections.Counter(); eks = collections.defaultdict(list); felt = None
with requests.get(hf_hub_url("NbAiLab/NCC", fil, repo_type="dataset"), stream=True, timeout=120) as r:
    r.raise_for_status()
    for line in r.iter_lines():
        if not line: continue
        try: d = json.loads(line)
        except json.JSONDecodeError: continue
        if "wiki" not in d["doc_type"]: continue
        felt = felt or sorted(d.keys())
        N[d["doc_type"]] += 1; Å[(d["doc_type"], d["publish_year"])] += 1
        if len(eks[d["doc_type"]]) < 8: eks[d["doc_type"]].append({k: (v[:120] if isinstance(v, str) else v) for k, v in d.items()})
json.dump(dict(fil=fil, felt=felt, antall=N, aar={f"{a}|{b}": c for (a, b), c in Å.items()}, eksempler=eks), open("data/v1/wiki_probe.json", "w"), ensure_ascii=False, indent=1)
print(dict(N)); print(sorted(Å.items())[:20]); print(felt)
for k, v in eks.items(): print(k, [x["id"] for x in v])
