import json, re, requests, simplemma, collections, sys
from huggingface_hub import hf_hub_url
W = re.compile(r"\w+", re.U); SENT = re.compile(r"(?<=[.!?])\s+(?=[A-ZÆØÅ«\"–-])")
c = collections.Counter(); ord_ = []; kj = []; eks = []
with requests.get(hf_hub_url("NbAiLab/NCC", sys.argv[1], repo_type="dataset"), stream=True, timeout=120) as r:
    for line in r.iter_lines():
        if not line: continue
        d = json.loads(line); y = int(d["publish_year"] or 2021)
        if d["lang_fasttext"] != "nn" or not 1990 <= y <= 2020 or d["doc_type"] not in ("newspaper_ocr", "books"): continue
        t = d["text"].strip(); o = W.findall(t); ord_.append(len(o))
        a = [w for w in o if w.isalpha() and len(w) > 2]
        k = sum(simplemma.is_known(w.lower(), lang="nn") for w in a) / max(len(a), 1); kj.append(k)
        c["ord<80"] += len(o) < 80; c["ord>200"] += len(o) > 200; c["ikke punktum"] += not t.rstrip().endswith((".", "!", "?", "»", "\""))
        c["<4 setn"] += len(SENT.split(t)) < 4; c["kjent<0.9"] += k < 0.9; c["orddeling"] += bool(re.search(r"\b\w+ ?- \w", t)); c["n"] += 1
        if 80 <= len(o) <= 200 and len(eks) < 3: eks.append((round(k, 2), t[:250]))
import statistics as st
print(dict(c)); print("ord median", st.median(ord_), "kvartiler", st.quantiles(ord_, n=4)); print("kjent median", round(st.median(kj), 3), st.quantiles(kj, n=4))
for e in eks: print(e)
