"""Beskrivende (ikke beslutning): R uten enkeltmarkører, og R før vask på samme 20 tekster."""
import json, re, math, unicodedata, numpy as np
W = re.compile(r"\w+", re.U)
MK = json.load(open("markorer_v0.json"))["markorer"]
av = {json.loads(l)["nr"]: json.loads(l) for l in open("data/avsnitt.jsonl")}
cl = {json.loads(l)["nr"]: json.loads(l) for l in open("data/fortsettelser_claude.jsonl")}
vask = [json.loads(l) for l in open("data/vasket.jsonl")]
def n(t, ut): t = unicodedata.normalize("NFC", t); return sum(len(re.findall(m["regex"], t, re.I if m["flagg"] else 0)) for m in MK if m["id"] not in ut)
def R(A, H, ut, rng):
    ah = np.array([n(t, ut) for t in A]); aw = np.array([len(W.findall(t)) for t in A]); hh = np.array([n(t, ut) for t in H]); hw = np.array([len(W.findall(t)) for t in H])
    B = []
    for _ in range(10000):
        ia = rng.integers(0, len(A), len(A)); ih = rng.integers(0, len(H), len(H)); ra = ah[ia].sum() / aw[ia].sum(); rh = hh[ih].sum() / hw[ih].sum()
        B.append((math.inf if ra > 0 else 1.0) if rh == 0 else ra / rh)
    r0 = (ah.sum() / aw.sum()) / (hh.sum() / hw.sum()) if hh.sum() else math.inf
    return [round(r0, 2)] + [round(float(x), 2) for x in np.percentile(B, [2.5, 97.5])]
out = {}
for v in ("nb", "nn"):
    rng = np.random.default_rng(2026)
    H = [d["andre"] for d in av.values() if d["variant"] == v]
    A = [d["tekst"] for d in vask if d["kilde"] == "claude" and d["variant"] == v]
    F = [cl[d["nr"]]["tekst"] for d in vask if d["kilde"] == "claude" and d["variant"] == v]
    out[v] = {"etter vask, alle": R(A, H, set(), rng), "før vask, samme 20": R(F, H, set(), rng),
              "etter vask, uten tredelt_oppramsing": R(A, H, {"tredelt_oppramsing"}, rng),
              "etter vask, uten ikke_x_men_y": R(A, H, {"ikke_x_men_y"}, rng),
              "etter vask, bare Språkrådet-markører (a)": R(A, H, {m["id"] for m in MK if m["gruppe"] == "struktur"}, rng)}
json.dump(out, open("resultat/folsomhet.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1))
