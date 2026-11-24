"""Steg 5b: samme fortsettelsesoppgave på lokal modell via ollama, serielt."""
import json, re, time, datetime, requests, sys
MODELL = "hf.co/ltg/normistral-7b-warm-instruct:Q4_K_M"
W = re.compile(r"\w+", re.U)
ut_fil = "data/fortsettelser_lokal.jsonl"
ferdig = set()
try: ferdig = {json.loads(l)["nr"] for l in open(ut_fil)}
except FileNotFoundError: pass
with open(ut_fil, "a") as ut:
    for l in open("data/avsnitt.jsonl"):
        d = json.loads(l)
        if d["nr"] in ferdig: continue
        sp = "bokmål" if d["variant"] == "nb" else "nynorsk"
        p = f"Fortsett denne teksten på {sp} med omtrent like mange ord som det som står: {d['forste']}"
        n = len(W.findall(d["forste"]))
        t0 = time.time()
        r = requests.post("http://localhost:11434/api/chat", json={"model": MODELL, "messages": [{"role": "user", "content": p}], "stream": False,
            "options": {"seed": 2026, "num_predict": int(n * 2.5) + 40, "num_thread": 4}}, timeout=600).json()
        tekst = r["message"]["content"].strip()
        ut.write(json.dumps({"nr": d["nr"], "variant": d["variant"], "modell": MODELL, "tidspunkt": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
            "prompt": p, "tekst": tekst, "sekunder": round(time.time() - t0, 1), "eval_count": r.get("eval_count")}, ensure_ascii=False) + "\n"); ut.flush()
        print(d["nr"], round(time.time() - t0, 1), len(W.findall(tekst)), file=sys.stderr)
