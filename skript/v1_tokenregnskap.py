"""v1: forbruk som sum per forespørsel (deduplisert på message.id), per tokentype, for subagentene (40+1 genereringskall, 32 vaskekall) og hovedøkta
fra v1-oppgaven til kjøretidspunktet. Kilde: message.usage i transkriptene (AVVIK B12)."""
import json, re, sys, glob, collections, datetime
TASKS, HOVED = sys.argv[1], sys.argv[2]; TY = ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens")
GEN = re.compile(r"^Skriv en faktatekst på (bokmål|nynorsk) på 150–250 ord om temaet «.*»\. Svar bare med teksten\. Ikke bruk verktøy\.$", re.S)
agg = collections.defaultdict(collections.Counter)
for f in glob.glob(f"{TASKS}/*.output"):
    try: L = [json.loads(l) for l in open(f) if l.strip()]
    except Exception: continue
    u = next((d for d in L if d.get("type") == "user"), None)
    if not u: continue
    c = u["message"]["content"]; t = c if isinstance(c, str) else " ".join(x.get("text", "") for x in c if isinstance(x, dict))
    m = re.search(r"/v1(no|en)_tekster_\d{3}\.txt", t)
    ledd = "vask_" + m.group(1) if m else ("generering" if GEN.match(t.strip()) else None)
    if not ledd: continue
    F = {}; siste = None
    for d in L:
        if d.get("type") == "assistant": us = d["message"].get("usage") or {}; F[d["message"].get("id")] = {k: us.get(k, 0) or 0 for k in TY}; siste = F[d["message"].get("id")]
    a = agg[ledd]; a["kall"] += 1; a["forespørsler"] += len(F)
    for k in TY: a[k] += sum(x[k] for x in F.values()); a["siste_" + k] += siste[k] if siste else 0
start = None; F = {}
for l in open(HOVED):
    try: d = json.loads(l)
    except Exception: continue
    if d.get("type") == "user" and not d.get("isSidechain") and isinstance(d["message"].get("content"), str) and "OPPGAVE: norsk-ki-preg v1" in d["message"]["content"]: start = d["timestamp"]
    if start and d.get("type") == "assistant" and not d.get("isSidechain") and d.get("timestamp", "") >= start:
        us = d["message"].get("usage") or {}; F[d["message"].get("id")] = {k: us.get(k, 0) or 0 for k in TY}; slutt = d["timestamp"]
h = agg["hovedøkt"]; h["kall"] = 1; h["forespørsler"] = len(F)
for k in TY: h[k] = sum(x[k] for x in F.values())
ut = {l: dict(a, sum=sum(a[k] for k in TY), uten_cache_lesing=sum(a[k] for k in TY) - a["cache_read_input_tokens"], subagent_tokens=sum(a.get("siste_" + k, 0) for k in TY)) for l, a in agg.items()}
ut["alle"] = {k: sum(x[k] for x in ut.values()) for k in ("sum", "uten_cache_lesing", "forespørsler") } | {k: sum(x.get(k, 0) for x in ut.values()) for k in TY}
ut["hovedøkt_periode"] = [start, slutt]
json.dump(ut, open("resultat/v1_tokenregnskap.json", "w"), ensure_ascii=False, indent=1)
for k, v in ut.items(): print(k, v if not isinstance(v, dict) else {x: v[x] for x in v if not x.startswith("siste_")})
