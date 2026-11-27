"""v1 steg 2: liste_v2 = fase B-faktatekster (T2; fritekst_emne + val_emne; Claude og NorMistral) mot Wikipedia-byggesettet.
Metode som PREREG v1 §5: Stanza-lemma (UPOS), lemma-bi/trigram innen setning, prevalens over tekster, Jeffreys, LPR = ln(p_KI/p_M),
inntak LPR >= ln2 og c_KI + c_M >= TERSKEL (20; senkes til 10 hvis < 50 lemma+bigram+trigram per variant), PROPN/tall utelatt; samsvar = begge modeller.
Byggesettet lengdetilpasses: bare avsnitt >= 150 ord (KI-tekstene er 150–250 ord), AVVIK V4. Antislop-fraser som i v1 (bare Claude)."""
import json, re, sys, math, collections, hashlib
sys.path.insert(0, "skript")
from lpr import prevalens, lpr_tabell
from lemmatiser import analyser
import types
LL = types.SimpleNamespace(); _src = open("skript/lag_liste.py").read().split("ut = {}")[0].split("UT = sys.argv[1]")[0] + "\nW = re.compile(r'\\w+', re.U)\n" + open("skript/lag_liste.py").read().split('MODELLER = sys.argv[2].split(",")')[1].split("ut = {}")[0]
_ns = {}; exec(_src, _ns); LL.elementer = _ns["elementer"]; LL.antislop = _ns["antislop"]  # elementer() og antislop() uendret fra lag_liste.py (v1)
W = re.compile(r"\w+", re.U); MK = json.load(open("markorer_v0.json"))
def bygg(terskel):
    raa, liste, info = {}, {}, {}
    for v in ("nb", "nn"):
        men = [json.loads(l)["tekst"] for l in open(f"data/v1/wiki_{v}.jsonl") if json.loads(l)["rolle"] == "bygg" and json.loads(l)["ord"] >= 150]
        U = {json.loads(l)["nr"]: json.loads(l) for l in open(f"data/b_utvalg_{v}.jsonl")}
        eM = [LL.elementer(t, v) for t in men]
        cnt = collections.Counter(l for t in men for s in analyser(t, v) for (f, l, u) in s if u not in ("PUNCT", "SYM")); stopp = {l for l, _ in cnt.most_common(100)}
        per = {t: {} for t in ("lemma", "bigram", "trigram")}
        for m in ("claude", "lokal"):
            G = [json.loads(l) for l in open(f"data/b_{m}_{v}.jsonl")]
            ki = [d["tekst"] for d in G if d["oppgave"].startswith("T2") and U[d["nr"]]["rolle"] in ("fritekst_emne", "val_emne")]
            eK = [LL.elementer(t, v) for t in ki]; blokk = {"n_KI": len(ki), "n_M": len(men), "ord_KI_median": sorted(len(W.findall(t)) for t in ki)[len(ki)//2], "ord_M_median": sorted(len(W.findall(t)) for t in men)[len(men)//2]}
            for i, navn in enumerate(("lemma", "bigram", "trigram")):
                cK, nK = prevalens([e[i] for e in eK]); cM, nM = prevalens([e[i] for e in eM])
                rad = lpr_tabell(cK, nK, cM, nM, minimum=terskel)
                blokk[navn] = [dict(e=e, c_KI=a, c_M=h, lpr=round(x, 3), delta=round(a / nK - h / nM, 4)) for e, a, h, x in rad]
                blokk[navn + "_over_terskel"] = len(rad)
                for x in blokk[navn]:
                    if x["lpr"] >= math.log(2): per[navn].setdefault(x["e"], {})[m] = x
            if m == "claude": blokk["antislop"] = {str(k): [dict(e=g, f_KI=a, f_M=h, logratio=r) for g, a, h, r in vv] for k, vv in LL.antislop(ki, men, stopp).items()}
            raa[f"{v}|{m}|T2"] = blokk
        out = {}
        for typ, d in per.items():
            rader = [dict(e=e, modeller=sorted(x), samsvar=len(x) == 2, **{f"{m}_{k}": x[m][k] for m in x for k in ("c_KI", "c_M", "lpr", "delta")}) for e, x in d.items()]
            rader.sort(key=lambda r: (-r["samsvar"], -max(r.get("claude_lpr", -9), r.get("lokal_lpr", -9)))); out[typ] = rader
        out["antislop_claude_T2"] = {n: raa[f"{v}|claude|T2"]["antislop"][n][:30] for n in ("2", "3", "4")}
        liste[v] = out; info[v] = {t: len(out[t]) for t in ("lemma", "bigram", "trigram")}
    return raa, liste, info
terskel = 20; raa, liste, info = bygg(terskel)
senket = any(sum(i.values()) < 50 for i in info.values())
if senket: info20 = info; terskel = 10; raa, liste, info = bygg(terskel)
L = {"versjon": "v2", "dato": "2026-11-27", "regel": f"T2 faktatekst (Claude+NorMistral, fase B) mot NCC Wikipedia-byggesett (>=150 ord); LPR>=ln2, c_KI+c_M>={terskel}", "terskel": terskel,
     "terskel_senket": senket, "inntak_ved_20": info20 if senket else info, "varianter": liste, "sprakradet_markorer": MK["markorer"]}
json.dump(raa, open("resultat/liste_v2_raa.json", "w"), ensure_ascii=False, indent=1)
json.dump(L, open("liste_v2.json", "w"), ensure_ascii=False, indent=1)
oppsum = {v: {"inntak": info[v], "samsvar": {t: sum(r["samsvar"] for r in liste[v][t]) for t in ("lemma", "bigram", "trigram")},
              "over_terskel_per_modell": {m: {t: raa[f"{v}|{m}|T2"][t + "_over_terskel"] for t in ("lemma", "bigram", "trigram")} for m in ("claude", "lokal")},
              "n": {m: (raa[f"{v}|{m}|T2"]["n_KI"], raa[f"{v}|{m}|T2"]["n_M"], raa[f"{v}|{m}|T2"]["ord_KI_median"], raa[f"{v}|{m}|T2"]["ord_M_median"]) for m in ("claude", "lokal")}} for v in ("nb", "nn")}
oppsum["terskel"] = terskel; oppsum["senket"] = senket; oppsum["inntak_ved_20"] = L["inntak_ved_20"]; oppsum["sha256"] = hashlib.sha256(open("liste_v2.json", "rb").read()).hexdigest()
json.dump(oppsum, open("resultat/liste_v2_oppsummering.json", "w"), ensure_ascii=False, indent=1); print(json.dumps(oppsum, ensure_ascii=False))
