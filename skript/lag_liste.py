"""LPR-lister (lemma, bi-, trigram) + Antislop-fraser per variant × modell × oppgave (PREREG §5).
Bruk: lag_liste.py UTFIL MODELL[,MODELL]   (modell: lokal|claude)"""
import json, re, sys, math, collections
sys.path.insert(0, "skript")
from lpr import prevalens, lpr_tabell, ngram
from lemmatiser import analyser
UT = sys.argv[1]; MODELLER = sys.argv[2].split(",")
W = re.compile(r"\w+", re.U)
def les(f):
    try: return [json.loads(l) for l in open(f)]
    except FileNotFoundError: return []
def elementer(tekst, v):
    S = analyser(tekst, v)
    lem = [[l for (f, l, u) in s if u not in ("PUNCT", "SYM")] for s in S]
    uni = {f"{l}_{u}" for s in S for (f, l, u) in s if u not in ("PUNCT", "SYM", "NUM", "PROPN") and not any(ch.isdigit() for ch in l)}
    return uni, set(ngram(lem, 2)), set(ngram(lem, 3))
def ord_ngram(tekst, n):
    o = [w.lower() for w in W.findall(tekst)]
    return [" ".join(o[i:i + n]) for i in range(len(o) - n + 1)]
def antislop(ki, men, stopp):
    res = {}
    for n in (2, 3, 4):
        fK = collections.Counter(); dK = collections.Counter(); fM = collections.Counter()
        for t in ki:
            g = ord_ngram(t, n); fK.update(g); dK.update(set(g))
        for t in men: fM.update(ord_ngram(t, n))
        NK, NM = sum(fK.values()) or 1, sum(fM.values()) or 1
        rad = []
        for g, f in fK.items():
            if f < 5 or dK[g] < 3 or all(w in stopp for w in g.split()): continue
            rad.append((g, f, fM[g], round(math.log(((f + 1) / NK) / ((fM[g] + 1) / NM)), 3)))
        rad.sort(key=lambda x: -x[3]); res[n] = rad[:100]
    return res
ut = {}
for v in ("nb", "nn"):
    U = {d["nr"]: d for d in les(f"data/b_utvalg_{v}.jsonl")}
    men_T1 = [d["andre"] for d in U.values() if d["rolle"] == "fortsettelse"]
    men_T23 = [d["tekst"] for d in U.values() if d["rolle"] == "fritekst_emne"]
    # stoppord: 100 hyppigste lemmaer i menneskekorpuset (T1 + fritekst-kilder)
    cnt = collections.Counter(l for t in men_T1 + men_T23 for s in analyser(t, v) for (f, l, u) in s if u not in ("PUNCT", "SYM"))
    stopp = {l for l, _ in cnt.most_common(100)}
    for m in MODELLER:
        G = {d["nr"]: d for d in les(f"data/b_{m}_{v}.jsonl")}
        for opp, rolle, menn in (("T1", "fortsettelse", men_T1), ("T2+T3", "fritekst_emne", men_T23)):
            ki = [G[n]["tekst"] for n, d in U.items() if d["rolle"] == rolle and n in G]
            if not ki: continue
            eK = [elementer(t, v) for t in ki]; eM = [elementer(t, v) for t in menn]
            blokk = {"n_KI": len(ki), "n_M": len(menn)}
            for i, navn in enumerate(("lemma", "bigram", "trigram")):
                cK, nK = prevalens([e[i] for e in eK]); cM, nM = prevalens([e[i] for e in eM])
                rad = lpr_tabell(cK, nK, cM, nM, minimum=20)
                blokk[navn] = [dict(e=e, c_KI=a, c_M=h, lpr=round(x, 3), delta=round(a / nK - h / nM, 4)) for e, a, h, x in rad]
            blokk["antislop"] = {str(k): [dict(e=g, f_KI=a, f_M=h, logratio=r) for g, a, h, r in vv] for k, vv in antislop(ki, menn, stopp).items()}
            ut[f"{v}|{m}|{opp}"] = blokk
            print(v, m, opp, len(ki), "lemma over terskel:", len(blokk["lemma"]), "LPR>=ln2:", sum(1 for x in blokk["lemma"] if x["lpr"] >= math.log(2)), flush=True)
json.dump(ut, open(UT, "w"), ensure_ascii=False, indent=1)
