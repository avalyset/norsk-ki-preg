"""Fase B: trekk per variant etter PREREG §2. Bruk: trekk_b.py VARIANT KANDIDATFIL..."""
import json, re, random, sys
V = sys.argv[1]; FILER = sys.argv[2:]
W = re.compile(r"\w+", re.U); SENT = re.compile(r"(?<=[.!?])\s+(?=[A-ZÆØÅ«\"–-])")
lang = "no" if V == "nb" else "nn"; sett = {}
for f in FILER:
    for l in open(f):
        d = json.loads(l)
        if d["lang_fasttext"] == lang: sett[d["id"]] = d
K = sorted(sett.values(), key=lambda d: d["id"]); random.Random(2026).shuffle(K)
NPAR = 240 if V == "nb" else 185
plan = [("val_menneske", 20), ("val_emne", 20), ("fortsettelse", NPAR), ("fritekst_emne", 50)]
ut, i = [], 0
for rolle, n in plan:
    tatt = K[i:i + n]; i += len(tatt)
    for j, d in enumerate(tatt):
        d = dict(d, variant=V, rolle=rolle, nr=f"{V}-{rolle}-{j:03d}")
        if rolle == "fortsettelse":
            s = SENT.split(d["tekst"]); m = len(W.findall(d["tekst"])) / 2
            k = min(range(1, len(s)), key=lambda k: abs(len(W.findall(" ".join(s[:k]))) - m))
            d.update(forste=" ".join(s[:k]), andre=" ".join(s[k:]))
        if rolle in ("val_emne", "fritekst_emne"):
            d["emne"] = SENT.split(d["tekst"])[0]
            grense = 10 if rolle == "val_emne" else 25
            d["oppgave"] = "T2 faktatekst" if j < grense else "T3 fortelling"
        ut.append(d)
    print(V, rolle, f"{len(tatt)}/{n}")
print(V, "kandidater i alt", len(K))
with open(f"data/b_utvalg_{V}.jsonl", "w") as o:
    for d in ut: o.write(json.dumps(d, ensure_ascii=False) + "\n")
