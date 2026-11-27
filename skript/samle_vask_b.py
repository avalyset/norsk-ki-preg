"""Henter vaskesvar (no_/en_tekster_NNN.txt) fra transkriptene og tar ut omskrivingsblokken."""
import json, re, sys, glob, os
TASKS = sys.argv[1]
plan = {f"tekster_{p['parti']:03d}.txt": p for p in json.load(open("data/b_vaskeplan.json"))}
HODE = re.compile(r"^\s*(?:#{1,4}\s*)?\**\s*(?:rewrite|omskriving)\s*\**\s*:?\s*$", re.I | re.M)
NESTE = re.compile(r"^\s*(?:#{1,4}\s*)?\**\s*(?:changes|notes|endringer|endringar|merknader|merknad|notater|diagnose|diagnosis)\s*\**\s*:?\s*$", re.I | re.M)
ut, feil, tok = [], [], {}
for f in glob.glob(f"{TASKS}/*.output"):
    try: L = [json.loads(l) for l in open(f) if l.strip()]
    except Exception: continue
    u = next((d for d in L if d.get("type") == "user"), None)
    if not u: continue
    c = u["message"]["content"]; t = c if isinstance(c, str) else " ".join(x.get("text", "") for x in c if isinstance(x, dict))
    m = re.search(r"/(no|en)_(tekster_\d{3}\.txt)", t)
    if not m: continue
    skill, fil = m.group(1), m.group(2); svar = None; siste = sumt = 0
    for d in L:
        if d.get("type") != "assistant": continue
        us = d["message"].get("usage") or {}; x = sum(us.get(k, 0) or 0 for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens")); sumt += x; siste = x
        for y in d["message"].get("content", []):
            if y.get("type") == "tool_use" and y.get("name") == "SubagentHandback": svar = y["input"]["message"]
    tok[f"{skill}_{fil}"] = dict(harness=siste, sum=sumt, har_svar=svar is not None)
    if not svar: continue
    deler = re.split(r"^===SVAR (\d)===\s*$", svar, flags=re.M); S = {int(deler[i]): deler[i + 1] for i in range(1, len(deler), 2)}
    for i, (kilde, nr) in enumerate(plan[fil]["innhold"], 1):
        s = S.get(i, ""); h = HODE.search(s)
        if not h: feil.append((skill, fil, i)); continue
        rest = s[h.end():]; n = NESTE.search(rest); tekst = (rest[:n.start()] if n else rest).strip()
        ut.append(dict(skill=skill, parti=fil, nr=nr, kilde=kilde, variant=plan[fil]["variant"], tekst=tekst, raasvar=s))
with open("data/b_vasket.jsonl", "w") as o:
    for d in ut: o.write(json.dumps(d, ensure_ascii=False) + "\n")
json.dump(tok, open("data/b_vask_tokens.json", "w"), indent=1)
print("transkripter", len(tok), "med svar", sum(v["har_svar"] for v in tok.values()), "tekster", len(ut), "feil", feil[:10], len(feil))
