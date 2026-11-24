"""Steg 7: M1 (markørrate + R med bootstrap), M3 (endringsgrad), M4 (LPR per lemma). M2 i maal_m2.py."""
import json, re, math, unicodedata, collections
import numpy as np, simplemma
W = re.compile(r"\w+", re.U)
MK = json.load(open("markorer_v0.json"))["markorer"]
RX = [(m["id"], m["gruppe"], re.compile(m["regex"], re.I if m["flagg"] else 0)) for m in MK]
def nfc(t): return unicodedata.normalize("NFC", t)
def ord_(t): return len(W.findall(nfc(t)))
def treff(t):
    t = nfc(t); return {i: len(r.findall(t)) for i, _, r in RX}
def les(f):
    try: return [json.loads(l) for l in open(f)]
    except FileNotFoundError: return []
av = {d["nr"]: d for d in les("data/avsnitt.jsonl")}
claude = {d["nr"]: d for d in les("data/fortsettelser_claude.jsonl")}
lokal = {d["nr"]: d for d in les("data/fortsettelser_lokal.jsonl")}
vask = les("data/vasket.jsonl")  # felter: nr, kilde ('claude'|'menneske'), variant, tekst
grupper = collections.defaultdict(list)  # (variant, gruppe) -> list of texts
for nr, d in av.items(): grupper[(d["variant"], "menneske (fasit)")].append(d["andre"])
for nr, d in claude.items(): grupper[(d["variant"], "Claude før vask")].append(d["tekst"])
for nr, d in lokal.items(): grupper[(d["variant"], "NorMistral før vask")].append(d["tekst"])
for d in vask:
    navn = {"claude": "Claude etter vask", "menneske": "menneske etter vask"}[d["kilde"]]
    grupper[(d["variant"], navn)].append(d["tekst"])
# Claude før vask, begrenset til de 20 som ble vasket (samme tekster)
vnr = {d["nr"] for d in vask if d["kilde"] == "claude"}
for nr, d in claude.items():
    if nr in vnr: grupper[(d["variant"], "Claude før vask (vaskeutvalget)")].append(d["tekst"])
def rate(tekster):
    h = sum(sum(treff(t).values()) for t in tekster); w = sum(ord_(t) for t in tekster)
    return h, w, 1000 * h / w if w else float("nan")
res = {"M1": {}, "R": {}, "M1_per_markor": {}}
for (v, g), T in sorted(grupper.items()):
    h, w, r = rate(T); res["M1"][f"{v}|{g}"] = dict(n=len(T), treff=h, ord=w, rate=round(r, 2))
    c = collections.Counter()
    for t in T: c.update({k: n for k, n in treff(t).items() if n})
    res["M1_per_markor"][f"{v}|{g}"] = dict(c.most_common())
rng = np.random.default_rng(2026)
for v in ("nb", "nn"):
    A = grupper[(v, "Claude etter vask")]; H = grupper[(v, "menneske (fasit)")]
    if not A: continue
    ah = np.array([sum(treff(t).values()) for t in A]); aw = np.array([ord_(t) for t in A])
    hh = np.array([sum(treff(t).values()) for t in H]); hw = np.array([ord_(t) for t in H])
    R0 = (ah.sum() / aw.sum()) / (hh.sum() / hw.sum())
    B = np.empty(10000)
    for b in range(10000):
        ia = rng.integers(0, len(A), len(A)); ih = rng.integers(0, len(H), len(H))
        ra = ah[ia].sum() / aw[ia].sum(); rh = hh[ih].sum() / hw[ih].sum()
        B[b] = (math.inf if ra > 0 else 1.0) if rh == 0 else ra / rh
    lo, hi = np.percentile(B, [2.5, 97.5])
    res["R"][v] = dict(R=round(float(R0), 3), KI_nedre=round(float(lo), 3), KI_ovre=round(float(hi), 3), n_KI=len(A), n_menneske=len(H), fase_B=bool(lo > 1))
# M3: normalisert redigeringsavstand (tegnnivå, Levenshtein / max(len)) på menneskelig tekst før/etter vask, og Claude før/etter
def lev(a, b):
    if len(a) < len(b): a, b = b, a
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1): cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]
def lev_ord(a, b): return lev(W.findall(nfc(a).lower()), W.findall(nfc(b).lower())) / max(ord_(a), ord_(b), 1)
res["M3"] = {}
for d in vask:
    før = av[d["nr"]]["andre"] if d["kilde"] == "menneske" else claude[d["nr"]]["tekst"]
    k = f"{d['variant']}|{d['kilde']}"
    res["M3"].setdefault(k, []).append(dict(nr=d["nr"], tegn=round(lev(nfc(før), nfc(d["tekst"])) / max(len(før), len(d["tekst"])), 3), ord=round(lev_ord(før, d["tekst"]), 3), uendret=nfc(før).strip() == nfc(d["tekst"]).strip()))
res["M3_sammendrag"] = {k: dict(n=len(L), tegn_median=float(np.median([x["tegn"] for x in L])), tegn_snitt=round(float(np.mean([x["tegn"] for x in L])), 3),
    ord_median=float(np.median([x["ord"] for x in L])), uendret=sum(x["uendret"] for x in L)) for k, L in res["M3"].items()}
# M4: log prevalence ratio per lemma (simplemma), Claude-fortsettelse mot ekte fortsettelse, Jeffreys-glatting, terskel >= 5
res["M4"] = {}
for v in ("nb", "nn"):
    lg = "nb" if v == "nb" else "nn"
    def lem(T):
        c = collections.Counter()
        for t in T: c.update(simplemma.lemmatize(w.lower(), lang=lg) for w in W.findall(nfc(t)) if w.isalpha())
        return c
    cA = lem([d["tekst"] for d in claude.values() if d["variant"] == v]); cH = lem(grupper[(v, "menneske (fasit)")])
    NA, NH = sum(cA.values()), sum(cH.values()); V = len(set(cA) | set(cH))
    rows = []
    for w in set(cA) | set(cH):
        a, h = cA[w], cH[w]
        if a + h < 5: continue
        lpr = math.log(((a + .5) / (NA + .5 * V)) / ((h + .5) / (NH + .5 * V)))
        rows.append((w, a, h, round(lpr, 3)))
    rows.sort(key=lambda x: -x[3])
    res["M4"][v] = dict(N_KI=NA, N_menneske=NH, V=V, lemma_over_terskel=len(rows), topp50=rows[:50], bunn10=rows[-10:],
                        lemma_over_20=sum(1 for w in set(cA) | set(cH) if cA[w] + cH[w] >= 20))
json.dump(res, open("resultat/m1_m3_m4.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps({k: res[k] for k in ("M1", "R", "M3_sammendrag")}, ensure_ascii=False, indent=1))
