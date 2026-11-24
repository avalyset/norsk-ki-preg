"""Fase B steg 4: NorMistral via ollama, serielt, på fortsettelser, fritekst og valideringsemner. Gjenopptakbar."""
import json, re, time, datetime, requests, sys
MODELL = "hf.co/ltg/normistral-7b-warm-instruct:Q4_K_M"
W = re.compile(r"\w+", re.U); V = sys.argv[1]
def prompt(d):
    sp = "bokmål" if d["variant"] == "nb" else "nynorsk"
    if d["rolle"] == "fortsettelse": return f"Fortsett denne teksten på {sp} med omtrent like mange ord som det som står: {d['forste']}", int(len(W.findall(d['forste'])) * 2.5) + 40
    if d["oppgave"].startswith("T2"): return f"Skriv en faktatekst på {sp} på 150–250 ord om temaet i denne setningen: «{d['emne']}»", 400
    return f"Skriv en kort fortelling på {sp} på 150–250 ord med utgangspunkt i denne setningen: «{d['emne']}»", 400
ut_fil = f"data/b_lokal_{V}.jsonl"
try: ferdig = {json.loads(l)["nr"] for l in open(ut_fil)}
except FileNotFoundError: ferdig = set()
with open(ut_fil, "a") as ut:
    for l in open(f"data/b_utvalg_{V}.jsonl"):
        d = json.loads(l)
        if d["rolle"] == "val_menneske" or d["nr"] in ferdig: continue
        p, npred = prompt(d); t0 = time.time()
        r = requests.post("http://localhost:11434/api/chat", json={"model": MODELL, "messages": [{"role": "user", "content": p}], "stream": False,
            "options": {"seed": 2026, "num_predict": npred, "num_thread": 4}}, timeout=900).json()
        ut.write(json.dumps({"nr": d["nr"], "variant": V, "rolle": d["rolle"], "oppgave": d.get("oppgave", "T1 fortsettelse"), "modell": MODELL,
            "tidspunkt": datetime.datetime.now().astimezone().isoformat(timespec="seconds"), "prompt": p, "tekst": r["message"]["content"].strip(),
            "tokens_inn": r.get("prompt_eval_count"), "tokens_ut": r.get("eval_count"), "sekunder": round(time.time() - t0, 1)}, ensure_ascii=False) + "\n"); ut.flush()
