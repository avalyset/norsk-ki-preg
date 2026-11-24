import json, collections, sys, requests
from huggingface_hub import hf_hub_url
url=hf_hub_url("NbAiLab/NCC","data/validation-shard-0001-of-0001.jsonl",repo_type="dataset")
c=collections.Counter(); n=0; keys=None
with requests.get(url,stream=True,timeout=60) as r:
    for line in r.iter_lines():
        if not line: continue
        d=json.loads(line); n+=1
        if keys is None: keys=list(d.keys()); print(keys, {k:(str(v)[:80]) for k,v in d.items()})
        c[(d.get('doc_type'),d.get('lang'), d.get('publish_year',0)<=2020)]+=1
print("n",n)
for k,v in sorted(c.items(), key=lambda x:-x[1]): print(k,v)
