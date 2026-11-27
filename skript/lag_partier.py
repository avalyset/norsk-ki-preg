"""DEL 2 steg 8: lager partier à 5 oppgaver (samme prompter som PREREG §3) for Explore-subagenter."""
import json, sys
sys.path.insert(0, "skript")
B = sys.argv[1]; kart = []; k = 0
def prompt(d):
    sp = "bokmål" if d["variant"] == "nb" else "nynorsk"
    if d["rolle"] == "fortsettelse": return f"Fortsett denne teksten på {sp} med omtrent like mange ord som det som står: {d['forste']}"
    if d["oppgave"].startswith("T2"): return f"Skriv en faktatekst på {sp} på 150–250 ord om temaet i denne setningen: «{d['emne']}»"
    return f"Skriv en kort fortelling på {sp} på 150–250 ord med utgangspunkt i denne setningen: «{d['emne']}»"
for v in ("nb", "nn"):
    U = [json.loads(l) for l in open(f"data/b_utvalg_{v}.jsonl")]
    for rolle in ("fortsettelse", "fritekst_emne", "val_emne"):
        X = [d for d in U if d["rolle"] == rolle]
        for i in range(0, len(X), 5):
            b = X[i:i + 5]; k += 1; fn = f"{B}/oppg_{k:03d}.txt"
            with open(fn, "w") as f:
                for j, d in enumerate(b, 1): f.write(f"===OPPGAVE {j}===\n{prompt(d)}\n\n")
            kart.append({"parti": k, "fil": fn, "nr": [d["nr"] for d in b], "prompter": [prompt(d) for d in b]})
json.dump(kart, open("data/b_partier.json", "w"), ensure_ascii=False, indent=1)
print(len(kart), sum(len(x["nr"]) for x in kart))
