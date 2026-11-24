import json, collections, requests, sys
from huggingface_hub import hf_hub_url
f=sys.argv[1]
url=hf_hub_url("NbAiLab/NCC",f,repo_type="dataset")
c=collections.Counter(); ex={}
with requests.get(url,stream=True,timeout=60) as r:
    for line in r.iter_lines():
        if not line: continue
        d=json.loads(line)
        y=int(d['publish_year'] or 2021)
        if y<=2020:
            k=(d['doc_type'],d['lang_fasttext']); c[k]+=1
            if k not in ex: ex[k]=(y,d['text'][:300])
for k,v in sorted(c.items(), key=lambda x:-x[1])[:30]: print(k,v, ex[k][0], repr(ex[k][1][:200]))
