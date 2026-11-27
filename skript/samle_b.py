"""Samler Explore-subagentenes svar fra transkriptene (tasks/*.output) for partier i data/b_partier.json.
Tokens: 'harness' = siste meldings kontekst (= subagent_tokens), 'sum' = summen over alle forespørsler i subagenten."""
import json, re, sys, glob, os, datetime
ARGS = [a for a in sys.argv[1:] if a != "-v"]; TASKS = ARGS[0]; MØNSTER = ARGS[1] if len(ARGS) > 1 else "oppg_"
kart = json.load(open("data/b_partier.json")); per_fil = {os.path.basename(x["fil"]): x for x in kart}
funnet = {}
for f in glob.glob(f"{TASKS}/*.output"):
    try: L = [json.loads(l) for l in open(f) if l.strip()]
    except Exception: continue
    første = next((d for d in L if d.get("type") == "user"), None)
    if not første: continue
    c = første["message"]["content"]; tekst = c if isinstance(c, str) else " ".join(x.get("text", "") for x in c if isinstance(x, dict))
    m = re.search(rf"({MØNSTER}\d{{3}}\.txt)", tekst)
    if not m or m.group(1) not in per_fil: continue
    svar, sumt, siste = None, 0, 0
    for d in L:
        if d.get("type") != "assistant": continue
        u = d["message"].get("usage") or {}
        t = sum(u.get(k, 0) or 0 for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens"))
        sumt += t; siste = t
        for x in d["message"].get("content", []):
            if x.get("type") == "tool_use" and x.get("name") == "SubagentHandback": svar = x["input"]["message"]
    funnet[m.group(1)] = dict(svar=svar, harness=siste, sum=sumt, ts=datetime.datetime.fromtimestamp(os.path.getmtime(f)).astimezone().isoformat(timespec="seconds"), agent=os.path.basename(f))
print(json.dumps({k: dict(harness=v["harness"], sum=v["sum"], har_svar=v["svar"] is not None) for k, v in sorted(funnet.items())}) if "-v" in sys.argv else f"{len(funnet)} transkripter funnet")
json.dump(funnet, open(f"data/b_raa_{MØNSTER.strip('_')}.json", "w"), ensure_ascii=False)
