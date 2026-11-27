"""v1 steg 6: vaskepartier (PREREG v2 §5). KI uten gyldig tekst utelates sammen med paret. random.Random(2027), nb før nn, partier à 5.
Skriver data/v1/vaskeplan.json og SCRATCH/v1w/{v1no,v1en}_tekster_NNN.txt (samme innhold for begge skills)."""
import json, random, os, sys
SCR = sys.argv[1]; os.makedirs(f"{SCR}/v1w", exist_ok=True)
rng = random.Random(2027); plan = []; nr_parti = 0
for v in ("nb", "nn"):
    ki = {json.loads(l)["kilde_nr"]: json.loads(l) for l in open(f"data/v1/ki_val_{v}.jsonl")}
    hum = [json.loads(l) for l in open(f"data/v1/wiki_{v}.jsonl") if json.loads(l)["rolle"] == "val"]
    par = [h for h in hum if h["nr"] in ki]
    items = sorted([("ki", ki[h["nr"]]["nr"]) for h in par] + [("menneske", h["nr"]) for h in par]); rng.shuffle(items)
    tekst = {("ki", ki[h["nr"]]["nr"]): ki[h["nr"]]["tekst"] for h in par} | {("menneske", h["nr"]): h["tekst"] for h in par}
    for i in range(0, len(items), 5):
        nr_parti += 1; del_ = items[i:i + 5]
        innhold = "\n\n".join(f"===TEKST {k}===\n{tekst[x]}" for k, x in enumerate(del_, 1)) + "\n"
        for s in ("v1no", "v1en"): open(f"{SCR}/v1w/{s}_tekster_{nr_parti:03d}.txt", "w").write(innhold)
        plan.append(dict(parti=nr_parti, fil=f"tekster_{nr_parti:03d}.txt", variant=v, innhold=del_))
json.dump(plan, open("data/v1/vaskeplan.json", "w"), ensure_ascii=False, indent=1)
print(len(plan), "partier", {v: sum(len(p["innhold"]) for p in plan if p["variant"] == v) for v in ("nb", "nn")}, [len(p["innhold"]) for p in plan])
