"""PREREG §5: liste_v1 = T1-elementer (lemma/bigram/trigram) med LPR >= ln2 og c_KI+c_M >= 20, per variant og modell; samsvar-flagg; + markorer_v0."""
import json, math, hashlib
R = json.load(open("resultat/liste_v1_raa.json")); MK = json.load(open("markorer_v0.json"))
L = {"versjon": "v1", "dato": "2026-11-27", "regel": "T1, LPR>=ln2, c_KI+c_M>=20 (prevalens over tekster, Jeffreys)", "varianter": {}}
for v in ("nb", "nn"):
    out = {}
    for typ in ("lemma", "bigram", "trigram"):
        per = {}
        for m in ("claude", "lokal"):
            for x in R[f"{v}|{m}|T1"][typ]:
                if x["lpr"] >= math.log(2): per.setdefault(x["e"], {})[m] = x
        rader = []
        for e, d in per.items():
            rader.append(dict(e=e, modeller=sorted(d), samsvar=len(d) == 2, **{f"{m}_{k}": d[m][k] for m in d for k in ("c_KI", "c_M", "lpr", "delta")}))
        rader.sort(key=lambda r: (-r["samsvar"], -max(r.get("claude_lpr", -9), r.get("lokal_lpr", -9))))
        out[typ] = rader
    out["antislop_claude_T1"] = {n: R[f"{v}|claude|T1"]["antislop"][n][:30] for n in ("2", "3", "4")}
    L["varianter"][v] = out
L["sprakradet_markorer"] = [m for m in MK["markorer"]]
json.dump(L, open("liste_v1.json", "w"), ensure_ascii=False, indent=1)
for v in ("nb", "nn"):
    o = L["varianter"][v]
    print(v, {t: (len(o[t]), sum(r["samsvar"] for r in o[t]), sum("claude" in r["modeller"] for r in o[t])) for t in ("lemma", "bigram", "trigram")})
print(hashlib.sha256(open("liste_v1.json", "rb").read()).hexdigest())
