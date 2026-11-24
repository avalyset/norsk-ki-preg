"""Henter siste SubagentHandback-melding fra en subagent-transkriptfil (JSONL) uten å lese den inn i hovedøkta."""
import json, sys
def hent(fil):
    siste = None
    for l in open(fil):
        if not l.strip(): continue
        d = json.loads(l)
        if d.get("type") != "assistant": continue
        for x in d["message"].get("content", []):
            if x.get("type") == "tool_use" and x.get("name") == "SubagentHandback": siste = x["input"]["message"]
            elif x.get("type") == "text" and x.get("text", "").strip(): siste = siste if "===SVAR" in (siste or "") else x["text"]
    return siste
if __name__ == "__main__": print(hent(sys.argv[1]))
