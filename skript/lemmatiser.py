"""Stanza-lemmatisering med disk-cache (data/stanza_cache_{v}.jsonl): tekst-sha1 -> [[ (form, lemma, upos), ...] per setning]."""
import json, hashlib, os, stanza
_P = {}; _C = {}
def _cache(v):
    if v not in _C:
        _C[v] = {}
        f = f"data/stanza_cache_{v}.jsonl"
        if os.path.exists(f):
            for l in open(f): d = json.loads(l); _C[v][d["k"]] = d["s"]
    return _C[v]
def analyser(tekst, v):
    k = hashlib.sha1(tekst.encode()).hexdigest(); c = _cache(v)
    if k in c: return c[k]
    if v not in _P: _P[v] = stanza.Pipeline(v, processors="tokenize,pos,lemma", verbose=False)
    s = [[(w.text, (w.lemma or w.text).lower(), w.upos) for w in sen.words] for sen in _P[v](tekst).sentences]
    c[k] = s
    with open(f"data/stanza_cache_{v}.jsonl", "a") as o: o.write(json.dumps({"k": k, "s": s}, ensure_ascii=False) + "\n")
    return s
