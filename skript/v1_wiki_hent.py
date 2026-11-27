"""v1 steg 1: lagre alle Wikipedia-dokumenter fra NCC validation til data/v1/wiki_val.jsonl (CC BY-SA 3.0)."""
import json, sys, requests
from huggingface_hub import hf_hub_url
fil = sys.argv[1]; n = 0
with requests.get(hf_hub_url("NbAiLab/NCC", fil, repo_type="dataset"), stream=True, timeout=120) as r, open("data/v1/wiki_val.jsonl", "w") as ut:
    r.raise_for_status()
    for line in r.iter_lines():
        if not line: continue
        try: d = json.loads(line)
        except json.JSONDecodeError: continue
        if d["doc_type"] in ("wikipedia_download_nbo", "wikipedia_download_nno"):
            ut.write(json.dumps(d, ensure_ascii=False) + "\n"); n += 1
print(n)
