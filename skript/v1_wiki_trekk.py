"""v1 steg 1: trekk Wikipedia-avsnitt (80–250 ord, løpende prosa), ett per artikkel, seed 2027.
NCC-teksten har ingen linjeskift: «avsnitt» = innledende prosablokk før første liste/overskrift, kuttet ved siste setningsgrense <= 250 ord (AVVIK V2).
Markup ''' og '' fjernes før filteret.
Prosafilter: >= 3 setninger, slutter med punktum/!/?, ingen wikimarkup (''  [[ {{ | = Fil: Kategori: *), ingen linje som starter med : * # ;,
<= 8 % sifre blant tokenene, >= 85 % kjente ord (simplemma). Deler i val (20 per variant, urørt) og bygg (resten)."""
import json, re, random, unicodedata, collections, simplemma
W = re.compile(r"\w+", re.U); SENT = re.compile(r"(?<=[.!?])\s+(?=[A-ZÆØÅ«\"])")
MARK = re.compile(r"''|\[\[|\]\]|\{\{|\}\}|\||==|Fil:|File:|Kategori:|Bilde:|thumb|px\b|<|>|http|www\.")
def prosa(p, v):
    o = W.findall(p)
    if not 80 <= len(o) <= 250 or not p.rstrip().endswith((".", "!", "?")) or MARK.search(p): return False
    if re.match(r"^\s*[:*#;•\-–]", p) or len(SENT.split(p)) < 3: return False
    if sum(w.isdigit() for w in o) / len(o) > 0.08: return False
    a = [w for w in o if w.isalpha() and len(w) > 2]
    return bool(a) and sum(simplemma.is_known(w.lower(), lang=v) for w in a) / len(a) >= (0.85 if v == "nb" else 0.70)  # nn: simplemma kjenner median 74 % av nn-Wikipedia (AVVIK V3)
kand = collections.defaultdict(list)
for l in open("data/v1/wiki_val.jsonl"):
    d = json.loads(l); v = "nb" if d["doc_type"].endswith("nbo") else "nn"
    m = re.match(r"wikipedia_download_n[bn]o_(.*)_(\d+)$", d["id"]); tittel = m.group(1) if m else d["id"]
    t = unicodedata.normalize("NFC", d["text"]).replace("'''", "").replace("''", "")
    t = re.split(r"\s\*\s|\s#\s|==|\s:\s?\*|\s;\s", t)[0]  # bare innledende prosablokk, før første liste/overskrift (NCC-teksten har ingen linjeskift)
    t = re.sub(r"\s+", " ", t).strip(); t = re.sub(r"\s+([.,;:!?])", r"\1", t)
    acc = []
    for x in SENT.split(t):
        if len(W.findall(" ".join(acc + [x]))) > 250: break
        acc.append(x)
    p = " ".join(acc)
    if prosa(p, v): kand[v].append(dict(id=d["id"], tittel=tittel, variant=v, ord=len(W.findall(p)), tekst=p))
ut = {}
for v in ("nb", "nn"):
    k = sorted(kand[v], key=lambda x: x["id"]); random.Random(2027).shuffle(k)
    for i, x in enumerate(k): x["rolle"] = "val" if i < 20 else "bygg"; x["nr"] = f"{v}-wiki-{i:04d}"; x["lisens"] = "CC BY-SA 3.0 (NCC wikipedia_download_n%so)" % ("b" if v == "nb" else "n")
    ut[v] = k
    with open(f"data/v1/wiki_{v}.jsonl", "w") as f:
        for x in k: f.write(json.dumps(x, ensure_ascii=False) + "\n")
    o = sorted(x["ord"] for x in k); b = [x["ord"] for x in k if x["rolle"] == "bygg"]
    print(v, "kandidater", len(k), "median ord", o[len(o)//2], "bygg", len(b), "bygg>=150", sum(x >= 150 for x in b))
