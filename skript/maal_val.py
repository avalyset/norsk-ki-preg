"""PREREG §6: M1 (markørrate, R per skill), M3 (Levenshtein på menneskelig tekst), parret bootstrap, regel."""
import json, re, math, unicodedata, sys, collections, numpy as np
sys.path.insert(0, "skript"); from lemmatiser import analyser
from lpr import ngram
W = re.compile(r"\w+", re.U)
MK = json.load(open("markorer_v0.json"))["markorer"]; RX = [re.compile(m["regex"], re.I if m["flagg"] else 0) for m in MK]
L1 = json.load(open("liste_v1.json"))["varianter"]
def nfc(t): return unicodedata.normalize("NFC", t)
def ord_(t): return len(W.findall(nfc(t)))
def treff(t, v, bare_v0=False):
    t = nfc(t); h = sum(len(r.findall(t)) for r in RX)
    if bare_v0: return h
    S = analyser(t, v); lem = [[l for (f, l, u) in s if u not in ("PUNCT", "SYM")] for s in S]
    uni = collections.Counter(f"{l}_{u}" for s in S for (f, l, u) in s)
    bi = collections.Counter(ngram(lem, 2)); tri = collections.Counter(ngram(lem, 3))
    for typ, C in (("lemma", uni), ("bigram", bi), ("trigram", tri)):
        h += sum(C[r["e"]] for r in L1[v][typ])
    return h
def lev(a, b):
    if len(a) < len(b): a, b = b, a
    p = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        c = [i]
        for j, y in enumerate(b, 1): c.append(min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (x != y)))
        p = c
    return p[-1]
def m3(a, b): a, b = nfc(a).strip(), nfc(b).strip(); return lev(a, b) / max(len(a), len(b), 1)
U = {}; C = {}
for v in ("nb", "nn"):
    for l in open(f"data/b_utvalg_{v}.jsonl"): d = json.loads(l); U[d["nr"]] = d
    for l in open(f"data/b_claude_{v}.jsonl"): d = json.loads(l); C[d["nr"]] = d
V = [json.loads(l) for l in open("data/b_vasket.jsonl")]
vask = {(d["skill"], d["nr"]): d["tekst"] for d in V}
rng = np.random.default_rng(2026); res = {}
for v in ("nb", "nn"):
    H = sorted(n for n, d in U.items() if d["variant"] == v and d["rolle"] == "val_menneske")
    K = sorted(n for n, d in U.items() if d["variant"] == v and d["rolle"] == "val_emne")
    K = [n for n in K if ("no", n) in vask and ("en", n) in vask]; H2 = [n for n in H if ("no", n) in vask and ("en", n) in vask]
    out = {"n_KI": len(K), "n_menneske": len(H), "n_menneske_vasket": len(H2)}
    for bare in (False, True):
        tag = "v0+liste_v1" if not bare else "bare_v0"
        hh = np.array([treff(U[n]["tekst"], v, bare) for n in H]); hw = np.array([ord_(U[n]["tekst"]) for n in H])
        A = {s: (np.array([treff(vask[(s, n)], v, bare) for n in K]), np.array([ord_(vask[(s, n)]) for n in K])) for s in ("no", "en")}
        F = (np.array([treff(C[n]["tekst"], v, bare) for n in K]), np.array([ord_(C[n]["tekst"]) for n in K]))
        rate = lambda h, w: 1000 * h.sum() / w.sum()
        out[tag] = {"rate_menneske": round(rate(hh, hw), 2), "rate_KI_for_vask": round(rate(*F), 2),
                    "rate_KI_etter_no": round(rate(*A["no"]), 2), "rate_KI_etter_en": round(rate(*A["en"]), 2)}
        out[tag]["R_no"] = round(out[tag]["rate_KI_etter_no"] / out[tag]["rate_menneske"], 3) if hh.sum() else None
        out[tag]["R_en"] = round(out[tag]["rate_KI_etter_en"] / out[tag]["rate_menneske"], 3) if hh.sum() else None
        if not bare:  # beslutningsbootstrap (PREREG §6)
            D = np.empty(10000)
            for b in range(10000):
                ia = rng.integers(0, len(K), len(K)); ih = rng.integers(0, len(H), len(H)); rh = hh[ih].sum() / hw[ih].sum()
                def R(s):
                    ra = A[s][0][ia].sum() / A[s][1][ia].sum()
                    return (math.inf if ra > 0 else 1.0) if rh == 0 else ra / rh
                D[b] = R("en") - R("no")
            D = D[np.isfinite(D)]
            out["R_en_minus_R_no"] = dict(est=round(out[tag]["R_en"] - out[tag]["R_no"], 3), KI=[round(float(x), 3) for x in np.percentile(D, [2.5, 97.5])], n_endelige=int(len(D)))
            d3 = np.array([m3(U[n]["tekst"], vask[("no", n)]) - m3(U[n]["tekst"], vask[("en", n)]) for n in H2])
            B = np.array([d3[rng.integers(0, len(d3), len(d3))].mean() for _ in range(10000)])
            out["M3_no_minus_M3_en"] = dict(est=round(float(d3.mean()), 4), KI=[round(float(x), 4) for x in np.percentile(B, [2.5, 97.5])])
    for s in ("no", "en"):
        out[f"M3_menneske_{s}"] = dict(median=round(float(np.median([m3(U[n]["tekst"], vask[(s, n)]) for n in H2])), 4), snitt=round(float(np.mean([m3(U[n]["tekst"], vask[(s, n)]) for n in H2])), 4), uendret=sum(nfc(U[n]["tekst"]).strip() == nfc(vask[(s, n)]).strip() for n in H2))
        out[f"M3_KI_{s}"] = dict(median=round(float(np.median([m3(C[n]["tekst"], vask[(s, n)]) for n in K])), 4), uendret=sum(nfc(C[n]["tekst"]).strip() == nfc(vask[(s, n)]).strip() for n in K))
    out["R_vilkar"] = out["R_en_minus_R_no"]["KI"][0] > 0; out["M3_vilkar"] = out["M3_no_minus_M3_en"]["KI"][0] <= 0
    res[v] = out
res["beslutning"] = dict(R_minst_en=any(res[v]["R_vilkar"] for v in ("nb", "nn")), M3_begge=all(res[v]["M3_vilkar"] for v in ("nb", "nn")))
res["beslutning"]["norsk_skill_bedre"] = res["beslutning"]["R_minst_en"] and res["beslutning"]["M3_begge"]
json.dump(res, open("resultat/validering.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps(res, ensure_ascii=False, indent=1))
