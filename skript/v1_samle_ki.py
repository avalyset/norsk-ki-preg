"""v1 steg 5: hent KI-faktatekstene (ett Explore-kall per tekst) fra transkriptene. Skriver data/v1/ki_val_{nb,nn}.jsonl og data/v1/ki_val_status.json.
Bruk: v1_samle_ki.py TASKS [VENT_SEK]  – med VENT_SEK venter skriptet blokkerende (én gang, med tidsgrense) til alle 40 har svar."""
import json, re, sys, glob, time, os
TASKS = sys.argv[1]; VENT = int(sys.argv[2]) if len(sys.argv) > 2 else 0
PROMPT = re.compile(r"^Skriv en faktatekst på (bokmål|nynorsk) på 150–250 ord om temaet «(.*)»\. Svar bare med teksten\. Ikke bruk verktøy\.$", re.S)
VAL = {v: [json.loads(l) for l in open(f"data/v1/wiki_{v}.jsonl") if json.loads(l)["rolle"] == "val"] for v in ("nb", "nn")}
nøkkel = {(("bokmål" if v == "nb" else "nynorsk"), x["tittel"]): (v, x["nr"]) for v in VAL for x in VAL[v]}
AVSLAG = re.compile(r"kan ikkje skrive|kan ikke skrive|har ingen påliteleg kunnskap|har ingen pålitelig kunnskap", re.I)
def rens(t):
    """PREREG v2 §4, AVVIK V5: del på linjer som bare er «---», dropp deler som begynner med «Merknad», behold den lengste resten;
    fjern så en innledende overskriftslinje (<= 8 ord, uten sluttpunktum)."""
    d = [x.strip() for x in re.split(r"(?m)^\s*---\s*$", t) if x.strip() and not re.match(r"\W*merknad", x.strip(), re.I)]
    t = max(d, key=len) if d else t.strip()
    l = t.split("\n", 1)
    if len(l) == 2 and len(l[0].split()) <= 8 and not l[0].rstrip().endswith((".", "!", "?", ":")): t = l[1].strip()
    return t
def samle():
    funnet = {}
    for f in glob.glob(f"{TASKS}/*.output"):
        try: L = [json.loads(l) for l in open(f) if l.strip()]
        except Exception: continue
        u = next((d for d in L if d.get("type") == "user"), None)
        if not u or not isinstance(u["message"]["content"], str): continue
        m = PROMPT.match(u["message"]["content"].strip())
        if not m or (m.group(1), m.group(2)) not in nøkkel: continue
        svar = None; modell = set()
        for d in L:
            if d.get("type") != "assistant": continue
            modell.add(d["message"].get("model"))
            for y in d["message"].get("content", []):
                if y.get("type") == "tool_use" and y.get("name") == "SubagentHandback": svar = y["input"]["message"].strip()
        v, nr = nøkkel[(m.group(1), m.group(2))]
        if svar:
            rå = svar; svar = rens(svar); avslag = bool(AVSLAG.search(svar))
            tid = L[-1].get("timestamp", "")
            if nr in funnet and (funnet[nr]["avslag"] < avslag or (funnet[nr]["avslag"] == avslag and funnet[nr]["tid"] > tid)):
                funnet[nr]["forsok"] += 1; continue
            forsok = funnet[nr]["forsok"] + 1 if nr in funnet else 1
            funnet[nr] = dict(avslag=avslag, tid=tid, forsok=forsok, raa=rå, nr=nr.replace("wiki", "ki"), kilde_nr=nr, variant=v, tittel=m.group(2), prompt=u["message"]["content"].strip(), modell=sorted(map(str, modell)), agent=os.path.basename(f), tekst=svar)
    return funnet
slutt = time.time() + VENT
while True:
    F = samle()
    if (len(F) >= 40 and all(x["forsok"] >= 2 or not x["avslag"] for x in F.values())) or time.time() >= slutt: break
    time.sleep(20)
for v in ("nb", "nn"):
    with open(f"data/v1/ki_val_{v}.jsonl", "w") as o:
        for x in VAL[v]:
            if x["nr"] in F and not F[x["nr"]]["avslag"]: o.write(json.dumps(F[x["nr"]], ensure_ascii=False) + "\n")
mangler = [x["nr"] for v in VAL for x in VAL[v] if x["nr"] not in F or F[x["nr"]]["avslag"]]
W = re.compile(r"\w+")
st = dict(ferdige=len(F), avslag={nr: x["forsok"] for nr, x in F.items() if x["avslag"]}, rensa={nr: True for nr, x in F.items() if x["raa"].strip() != x["tekst"]}, mangler=mangler, ord={nr: len(W.findall(x["tekst"])) for nr, x in F.items()}, modeller=sorted({m for x in F.values() for m in x["modell"]}))
json.dump(st, open("data/v1/ki_val_status.json", "w"), ensure_ascii=False, indent=1)
o = sorted(st["ord"].values()); print("ferdige", len(F), "mangler", mangler, "modeller", st["modeller"], "ord min/median/max", (o[0], o[len(o)//2], o[-1]) if o else None)
