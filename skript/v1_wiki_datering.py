"""v1 steg 1: datering av Wikipedia-dumpen fra innholdet (årstall nevnt, kjente hendelser 2021–2023)."""
import json, re, collections
å = collections.Counter(); hend = collections.defaultdict(list)
H = {"ChatGPT": r"ChatGPT", "invasjon_ukraina_2022": r"(invasjon|invaderte|angrep)\w*[^.]{0,80}Ukraina[^.]{0,40}2022|24\. februar 2022",
     "elizabeth_dod": r"Elizabeth II[^.]{0,200}(døde|døydde|død)[^.]{0,40}2022|8\. september 2022",
     "charles_iii_konge": r"Charles III", "store_regjering": r"Regjeringa Støre|Regjeringen Støre|Støre-regjeringen", "vm_qatar_2022_vinner": r"(vant|vann)[^.]{0,60}(VM|verdsmeisterskapet|verdensmesterskapet)[^.]{0,40}2022"}
N = 0
for l in open("data/v1/wiki_val.jsonl"):
    d = json.loads(l); t = d["text"]; N += 1
    for y in set(re.findall(r"\b(20[12]\d)\b", t)): å[(d["doc_type"][-3:], int(y))] += 1
    for k, p in H.items():
        if re.search(p, t) and len(hend[k]) < 5: m = re.search(p, t); hend[k].append((d["id"], t[max(0, m.start()-80): m.end()+60]))
ut = dict(n=N, dokumenter_med_aar={f"{a}|{y}": c for (a, y), c in sorted(å.items()) if y >= 2015}, hendelser={k: v for k, v in hend.items()}, hendelser_antall={k: len(v) for k, v in hend.items()})
json.dump(ut, open("data/v1/wiki_datering.json", "w"), ensure_ascii=False, indent=1)
print({k: v for k, v in ut["dokumenter_med_aar"].items()}); print(ut["hendelser_antall"])
for k, v in hend.items(): print(k, v[:2])
