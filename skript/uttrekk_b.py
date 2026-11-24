"""Fase B steg 2: strøm NCC, samle kandidater (CC0 aviser/bøker, år FRA–TIL), kvalitetsfilter som AVVIK A3. Lagrer alle kandidater."""
import json, re, sys, unicodedata, requests, simplemma
from huggingface_hub import hf_hub_url
FRA, TIL = int(sys.argv[1]), int(sys.argv[2]); FILER = sys.argv[3:]
LISENS = {"newspaper_ocr": "CC0 (NB aviser)", "books": "CC0 (NB bøker)"}
W = re.compile(r"\w+", re.U); SENT = re.compile(r"(?<=[.!?])\s+(?=[A-ZÆØÅ«\"–-])")
brukt = {json.loads(l)["id"] for l in open("data/avsnitt.jsonl")}
def god(t, lang):
    o = W.findall(t)
    if not 80 <= len(o) <= 200 or not t.rstrip().endswith((".", "!", "?", "»", "\"")) or len(SENT.split(t)) < 4: return False
    a = [w for w in o if w.isalpha() and len(w) > 2]
    if not a: return False
    k = sum(simplemma.is_known(w.lower(), lang="nb" if lang == "no" else "nn") for w in a) / len(a)
    return k >= 0.90 and not re.search(r"\b\w+ ?- \w", t)
SPRAAK = set((__import__("os").environ.get("SPRAAK") or "no,nn").split(","))
ut = open(f"data/kandidater_{FRA}_{TIL}{__import__('os').environ.get('SUFFIKS','')}.jsonl", "a"); feil = 0; n = {"no": 0, "nn": 0}; raa = {"no": 0, "nn": 0}
for fil in FILER:
    with requests.get(hf_hub_url("NbAiLab/NCC", fil, repo_type="dataset"), stream=True, timeout=120) as r:
        r.raise_for_status()
        for line in r.iter_lines():
            if not line: continue
            try: d = json.loads(line)
            except json.JSONDecodeError: feil += 1; continue
            y = int(d["publish_year"] or 2021); lang = d["lang_fasttext"]
            if lang in SPRAAK and FRA <= y <= TIL and d["doc_type"] in LISENS and d["id"] not in brukt:
                raa[lang] += 1
                t = unicodedata.normalize("NFC", d["text"].strip())
                if god(t, lang):
                    n[lang] += 1
                    ut.write(json.dumps({"id": d["id"], "doc_type": d["doc_type"], "aar": y, "lisens": LISENS[d["doc_type"]], "lang_fasttext": lang, "lang_conf": d["lang_fasttext_conf"], "split": fil, "tekst": t}, ensure_ascii=False) + "\n"); ut.flush()
    print(fil, "passert", n, "rå", raa, "json-feil", feil, flush=True)
