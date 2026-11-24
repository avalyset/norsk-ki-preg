"""LPR, Juzek-stil: prevalens = andel par der elementet forekommer (minst én gang i teksten).
Jeffreys-glatting: p = (c + 0.5) / (n + 1). LPR = ln(p_KI / p_M). Telleterskel: c_KI + c_M >= MIN."""
import math, collections
def prevalens(tekster_som_elementmengder):
    c = collections.Counter()
    for s in tekster_som_elementmengder: c.update(set(s))
    return c, len(tekster_som_elementmengder)
def lpr_tabell(c_ki, n_ki, c_m, n_m, minimum=20):
    rad = []
    for e in set(c_ki) | set(c_m):
        a, h = c_ki.get(e, 0), c_m.get(e, 0)
        if a + h < minimum: continue
        rad.append((e, a, h, math.log(((a + .5) / (n_ki + 1)) / ((h + .5) / (n_m + 1)))))
    rad.sort(key=lambda x: -x[3]); return rad
def ngram(lemmaer_per_setning, n):
    return [" ".join(s[i:i + n]) for s in lemmaer_per_setning for i in range(len(s) - n + 1)]
