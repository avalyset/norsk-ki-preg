"""Steg 3: strøm NCC validering, filtrer, trekk 50 avsnitt per variant (seed 2026)."""
import json, re, random, unicodedata, requests, simplemma
from huggingface_hub import hf_hub_url
LISENS = {"newspaper_ocr": "CC0 (NB aviser)", "books": "CC0 (NB bøker)"}
# maalfrid_*/government/parliament er NLOD 2.0, men har publish_year=2021 (ukjent) i NCC og faller ut av år <= 2020.
TILLATT = lambda dt: dt in LISENS or dt.startswith("maalfrid_") or dt in ("government", "parliament")
W = re.compile(r"\w+", re.U)
SENT = re.compile(r"(?<=[.!?])\s+(?=[A-ZÆØÅ«\"–-])")
def god(t, lang):
    ord_ = W.findall(t)
    if not 80 <= len(ord_) <= 200: return False
    if not t.rstrip().endswith((".", "!", "?", "»", "\"")): return False
    if len(SENT.split(t)) < 4: return False
    alfa = [w for w in ord_ if w.isalpha() and len(w) > 2]
    if not alfa: return False
    kjent = sum(simplemma.is_known(w.lower(), lang="nb" if lang == "no" else "nn") for w in alfa) / len(alfa)
    return kjent >= 0.90 and not re.search(r"\b\w+ ?- \w", t)
def strøm(fil):
    url = hf_hub_url("NbAiLab/NCC", fil, repo_type="dataset")
    with requests.get(url, stream=True, timeout=60) as r:
        for line in r.iter_lines():
            if line: yield json.loads(line)
kand = {"no": [], "nn": []}
for d in strøm("data/validation-shard-0001-of-0001.jsonl"):
    y = int(d["publish_year"] or 2021); lang = d["lang_fasttext"]
    if lang in kand and y <= 2020 and TILLATT(d["doc_type"]):
        t = unicodedata.normalize("NFC", d["text"].strip())
        if god(t, lang): kand[lang].append({"id": d["id"], "doc_type": d["doc_type"], "aar": y, "lisens": LISENS.get(d["doc_type"], "NLOD 2.0"), "lang_fasttext": lang, "lang_conf": d["lang_fasttext_conf"], "tekst": t})
print("validering", {k: len(v) for k, v in kand.items()})
BRUKT_TRENING = []
for fil in ("data/train-shard-0001-of-0046.jsonl", "data/train-shard-0002-of-0046.jsonl"):
    if len(kand["nn"]) >= 50: break
    BRUKT_TRENING.append(fil)
    for d in strøm(fil):
        y = int(d["publish_year"] or 2021)
        if d["lang_fasttext"] == "nn" and y <= 2020 and TILLATT(d["doc_type"]):
            t = unicodedata.normalize("NFC", d["text"].strip())
            if god(t, "nn"): kand["nn"].append({"id": d["id"], "doc_type": d["doc_type"], "aar": y, "lisens": LISENS.get(d["doc_type"], "NLOD 2.0"), "lang_fasttext": "nn", "lang_conf": d["lang_fasttext_conf"], "tekst": t, "split": fil})
    print(fil, {k: len(v) for k, v in kand.items()})
print("treningsshards brukt:", BRUKT_TRENING)
rng = random.Random(2026)
ut = []
for lang, var in (("no", "nb"), ("nn", "nn")):
    for i, d in enumerate(rng.sample(sorted(kand[lang], key=lambda x: x["id"]), 50)):
        s = SENT.split(d["tekst"]); n = len(W.findall(d["tekst"]))
        # del ved setningsgrensen nærmest ordmidten
        best, acc = None, 0
        for j in range(1, len(s)):
            acc = len(W.findall(" ".join(s[:j])))
            if best is None or abs(acc - n / 2) < abs(best[1] - n / 2): best = (j, acc)
        d.update(variant=var, nr=f"{var}{i+1:02d}", forste=" ".join(s[:best[0]]), andre=" ".join(s[best[0]:]))
        ut.append(d)
with open("data/avsnitt.jsonl", "w") as f:
    for d in ut: f.write(json.dumps(d, ensure_ascii=False) + "\n")
