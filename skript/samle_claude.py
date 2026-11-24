"""Samler svar_*.txt fra subagentene til data/fortsettelser_claude.jsonl."""
import json, re, sys, os, datetime, glob
G = sys.argv[1]
ut = []
for f in sorted(glob.glob(f"{G}/svar_n?_??.txt")):
    nr = json.load(open(f.replace("svar_", "oppg_").replace(".txt", ".nr.json")))
    deler = re.split(r"^===SVAR (\d)===\s*$", open(f).read(), flags=re.M)
    svar = {int(deler[i]): deler[i + 1].strip() for i in range(1, len(deler), 2)}
    assert sorted(svar) == [1, 2, 3, 4, 5], (f, sorted(svar))
    ts = datetime.datetime.fromtimestamp(os.path.getmtime(f)).astimezone().isoformat(timespec="seconds")
    for i, n in enumerate(nr, 1):
        ut.append({"nr": n, "variant": n[:2], "modell": "claude-opus-5-5 (CC-subagent)", "tidspunkt": ts, "batch": os.path.basename(f), "tekst": svar[i]})
with open("data/fortsettelser_claude.jsonl", "w") as o:
    for d in ut: o.write(json.dumps(d, ensure_ascii=False) + "\n")
print(len(ut))
