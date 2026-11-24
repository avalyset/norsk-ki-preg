"""Samler vaskesvar, tar bare ut Rewrite-blokken. Lagrer råsvar også."""
import json, re, sys, os, datetime
V = sys.argv[1]
plan = json.load(open("data/vaskeplan.json"))
# Rewrite-blokken: overskriftslinje «Rewrite»/«Omskriving» (med eller uten ###/**), til neste kjente seksjonsoverskrift
HODE = re.compile(r"^\s*(?:#{1,4}\s*)?\**\s*(?:rewrite|omskriving)\s*\**\s*:?\s*$", re.I | re.M)
NESTE = re.compile(r"^\s*(?:#{1,4}\s*)?\**\s*(?:changes|notes|endringer|endringar|merknader|merknad|notater)\s*\**\s*:?\s*$", re.I | re.M)
ut, raa, feil = [], [], []
for p in plan:
    f = f"{V}/{p['fil'].replace('tekster_', 'svar_')}"
    deler = re.split(r"^===SVAR (\d)===\s*$", open(f).read(), flags=re.M)
    svar = {int(deler[i]): deler[i + 1].strip() for i in range(1, len(deler), 2)}
    ts = datetime.datetime.fromtimestamp(os.path.getmtime(f)).astimezone().isoformat(timespec="seconds")
    for i, (kilde, nr) in enumerate(p["innhold"], 1):
        s = svar.get(i, ""); m = HODE.search(s)
        if not m: feil.append((p["fil"], i)); tekst = None
        else:
            rest = s[m.end():]; n = NESTE.search(rest)
            tekst = (rest[:n.start()] if n else rest).strip()
            tekst = re.sub(r"^```\w*\n|\n```$", "", tekst).strip()
        raa.append({"nr": nr, "kilde": kilde, "variant": p["variant"], "fil": p["fil"], "pos": i, "raasvar": s})
        if tekst: ut.append({"nr": nr, "kilde": kilde, "variant": p["variant"], "modell": "claude-opus-5-5 + anti-ai-writing v2.1.0", "tidspunkt": ts, "tekst": tekst})
with open("data/vasket.jsonl", "w") as o:
    for d in ut: o.write(json.dumps(d, ensure_ascii=False) + "\n")
with open("data/vasket_raasvar.jsonl", "w") as o:
    for d in raa: o.write(json.dumps(d, ensure_ascii=False) + "\n")
print(len(ut), "feil:", feil)
