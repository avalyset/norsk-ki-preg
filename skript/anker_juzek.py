"""Steg 5: engelsk anker. Repoet har ingen fortsettelser, bare publiserte LAS-lister med tellinger (c_H, c_M, n_pairs).
Vår LPR-kode (skript/lpr.py) kjøres på deres tellinger og sammenlignes med deres publiserte rangering (rank_LAS)."""
import csv, json, sys, math
sys.path.insert(0, "skript"); from lpr import lpr_tabell
from scipy.stats import spearmanr
ROT = sys.argv[1]
FILER = {"news/gpt-4.1-mini": "news/las-gpt4.1-mini/policy=quantile_trim=no_M=1_K=12_jitter=no/en/las_word_en.csv",
         "science/claude-3-haiku": "science/las-claude-3-haiku/policy=quantile_trim=no_M=1_K=40_jitter=no/en/las_word_en.csv",
         "science/gpt-5.2": "science/las-gpt-5.2/policy=quantile_trim=no_M=1_K=40_jitter=no/en/las_word_en.csv"}
ut = {}
for navn, f in FILER.items():
    R = list(csv.DictReader(open(f"{ROT}/{f}")))
    n = int(R[0]["n_pairs"]); cM = {}; cH = {}; las = {}
    for r in R:
        k = r["key"]; cM[k] = float(r["c_M"]); cH[k] = float(r["c_H"]); las[k] = int(r["rank_LAS"])
    vår = lpr_tabell(cM, n, cH, n, minimum=20)
    v100 = [e for e, *_ in vår[:100]]
    pub = sorted([k for k in las if cM[k] + cH[k] >= 20], key=lambda k: las[k])
    p100 = pub[:100]
    felles = sorted(set(v100) & set(p100))
    jac = len(felles) / len(set(v100) | set(p100))
    vr = {e: i for i, (e, *_) in enumerate(vår)}
    rho = spearmanr([vr[k] for k in felles], [las[k] for k in felles]).statistic if len(felles) > 2 else float("nan")
    # Rangkorrelasjon over alle elementer over terskel (vår LPR mot publisert LAS)
    alle = [k for k in vr if k in las]
    rho_alle = spearmanr([vr[k] for k in alle], [las[k] for k in alle]).statistic
    ut[navn] = dict(n_pairs=n, elementer_over_terskel=len(vår), topp100_felles=len(felles), jaccard_topp100=round(jac, 3),
                    spearman_felles_topp100=round(float(rho), 3), spearman_alle=round(float(rho_alle), 3),
                    vår_topp15=[e for e, *_ in vår[:15]], publisert_topp15=p100[:15])
json.dump(ut, open("resultat/anker_juzek.json", "w"), indent=1)
print(json.dumps(ut, indent=1))
