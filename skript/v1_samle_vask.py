"""v1: hent vaskesvar (v1no_/v1en_tekster_NNN.txt) fra transkriptene; omskrivingsblokken som i fase B (samle_vask_b.py). Skriver data/v1/vasket.jsonl.
Bruk: v1_samle_vask.py TASKS [VENT_SEK] – venter blokkerende (én gang, med tidsgrense) til alle partier har svar."""
import json, re, sys, glob, time
TASKS = sys.argv[1]; VENT = int(sys.argv[2]) if len(sys.argv) > 2 else 0
plan = {p["fil"]: p for p in json.load(open("data/v1/vaskeplan.json"))}
HODE = re.compile(r"^\s*(?:#{1,4}\s*)?\**\s*(?:rewrite|omskriving)\s*\**\s*:?\s*$", re.I | re.M)
NESTE = re.compile(r"^\s*(?:#{1,4}\s*)?\**\s*(?:changes|notes|endringer|endringar|merknader|merknad|notater|diagnose|diagnosis)\s*\**\s*:?\s*$", re.I | re.M)
def samle():
    svar_per = {}
    for f in glob.glob(f"{TASKS}/*.output"):
        try: L = [json.loads(l) for l in open(f) if l.strip()]
        except Exception: continue
        u = next((d for d in L if d.get("type") == "user"), None)
        if not u: continue
        c = u["message"]["content"]; t = c if isinstance(c, str) else " ".join(x.get("text", "") for x in c if isinstance(x, dict))
        m = re.search(r"/v1(no|en)_(tekster_\d{3}\.txt)", t)
        if not m or m.group(2) not in plan: continue
        for d in L:
            if d.get("type") == "assistant":
                for y in d["message"].get("content", []):
                    if y.get("type") == "tool_use" and y.get("name") == "SubagentHandback": svar_per[(m.group(1), m.group(2))] = y["input"]["message"]
    return svar_per
slutt = time.time() + VENT
while True:
    S = samle()
    if len(S) >= 2 * len(plan) or time.time() >= slutt: break
    time.sleep(30)
ut, feil = [], []
for (skill, fil), svar in sorted(S.items()):
    deler = re.split(r"^===SVAR (\d)===\s*$", svar, flags=re.M); D = {int(deler[i]): deler[i + 1] for i in range(1, len(deler), 2)}
    for i, (kilde, nr) in enumerate(plan[fil]["innhold"], 1):
        r = D.get(i)
        if r is None: feil.append((skill, fil, i)); continue
        h = HODE.search(r)
        if h:
            rest = r[h.end():]; n = NESTE.search(rest); tekst = (rest[:n.start()] if n else rest).strip()
        elif re.search(r"Ingen endring", r): tekst = None  # uendret: fylles med kilden ved måling
        else: tekst = r.strip(); feil.append((skill, fil, i, "uten overskrift"))
        ut.append(dict(skill="no" if skill == "no" else "en", parti=fil, nr=nr, kilde=kilde, variant=plan[fil]["variant"], tekst=tekst, ingen_endringer=bool(re.search(r"Ingen endring", r)), raasvar=r))
with open("data/v1/vasket.jsonl", "w") as o:
    for x in ut: o.write(json.dumps(x, ensure_ascii=False) + "\n")
json.dump(dict(partier=len(plan), svar=len(S), mangler=[f"v1{s}_{f}" for f in plan for s in ("no", "en") if (s, f) not in S], tekster=len(ut), feil=feil), open("data/v1/vask_status.json", "w"), ensure_ascii=False, indent=1)
print("partier", len(plan), "svar", len(S), "tekster", len(ut), "feil", feil[:8])
