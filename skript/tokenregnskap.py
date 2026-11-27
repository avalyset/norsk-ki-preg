"""B12: bryter tokentallene for fase B DEL 2 ned per tokentype, fra transkriptene (tasks/*.output -> subagents/agent-*.jsonl).
Felt: message.usage.{input_tokens, cache_creation_input_tokens, cache_read_input_tokens, output_tokens} på hver assistant-linje.
'per linje' = slik samle_b.py/samle_vask_b.py summerte (én JSONL-linje per innholdsblokk; samme usage kan gjentas).
'per forespørsel' = dedupliseret på message.id (én API-forespørsel)."""
import json, re, sys, glob, os, collections
TASKS = sys.argv[1]
partier = {os.path.basename(x["fil"]) for x in json.load(open("data/b_partier.json"))}
TYPER = ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens")
res = {}
for f in sorted(glob.glob(f"{TASKS}/*.output")):
    try: L = [json.loads(l) for l in open(f) if l.strip()]
    except Exception: continue
    u = next((d for d in L if d.get("type") == "user"), None)
    if not u: continue
    c = u["message"]["content"]; t = c if isinstance(c, str) else " ".join(x.get("text", "") for x in c if isinstance(x, dict))
    m = re.search(r"/(no|en)_(tekster_\d{3}\.txt)", t); g = re.search(r"(oppg_\d{3}\.txt)", t)
    if m: ledd = "vask_" + m.group(1); nøkkel = m.group(0)
    elif g and g.group(1) in partier: ledd = "generering"; nøkkel = g.group(1)
    else: continue
    linje = collections.Counter(); forsp = {}; siste = None; modeller = set()
    for d in L:
        if d.get("type") != "assistant": continue
        us = d["message"].get("usage") or {}
        for k in TYPER: linje[k] += us.get(k, 0) or 0
        mid = d["message"].get("id") or d.get("requestId") or id(d)
        forsp[mid] = {k: us.get(k, 0) or 0 for k in TYPER}  # siste linje per forespørsel vinner (endelig output_tokens)
        siste = mid; modeller.add(d["message"].get("model"))
    res[nøkkel] = dict(ledd=ledd, linjer=dict(linje), forespørsler=len(forsp),
                       per_forsp={k: sum(v[k] for v in forsp.values()) for k in TYPER},
                       siste={k: forsp[siste][k] for k in TYPER} if siste else {}, modeller=sorted(map(str, modeller)))
agg = collections.defaultdict(lambda: collections.defaultdict(int))
for v in res.values():
    a = agg[v["ledd"]]; a["kall"] += 1; a["forespørsler"] += v["forespørsler"]
    for k in TYPER:
        a["linje_" + k] += v["linjer"].get(k, 0); a["forsp_" + k] += v["per_forsp"][k]; a["siste_" + k] += v["siste"].get(k, 0)
tot = collections.defaultdict(int)
for a in agg.values():
    for k, x in a.items(): tot[k] += x
agg["ALLE"] = tot
ut = {l: dict(a) for l, a in agg.items()}
ut["modeller"] = sorted({m for v in res.values() for m in v["modeller"]})
json.dump(dict(oppsummert=ut, per_kall=res), open("resultat/tokenregnskap.json", "w"), indent=1, ensure_ascii=False)
for l, a in ut.items(): print(l, a)
