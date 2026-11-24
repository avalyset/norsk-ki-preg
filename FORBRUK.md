# FORBRUK – overslag (skrevet før kjøring, 2026-11-24)

Alt innenfor Max-abonnementet (Claude Code-subagenter). Ingen betalte API-kall, ingen nøkler lest.

## Overslag tokens
| Ledd | Kall | Inn per kall | Ut per kall | Sum |
|---|---|---|---|---|
| Generering (100 avsnitt / 5) | 20 | ~15k (systemprompt + oppgave) | ~1,5k | ~0,33M |
| Vask (60 tekster / 5) | 12 | ~50k (≈30k skill + systemprompt + tekster) | ~4k | ~0,65M |
| Hovedøkt | 1 | – | – | ~0,3–0,5M |
| **Sum** | ~32 | | | **~1,3–1,5M tokens** (mest cache-lesing) |

## Lokale modeller (`ollama list`, 2026-11-24)
borealis-open-4b, borealis-open-12b, borealis-4b (NbAiLab, Q4_K_M), nb-llama-3.1-8b(-instruct-cardtmpl), normistral-7b-warm-instruct (ltg, Q4_K_M + cardtmpl), gemma2:9b, llama3.1:8b(-instruct-q8_0), qwen2.5:7b, mistral, smollm2:135m, clef-flash, bge-m3 og nomic-embed-text (innbygging).

Valgt for generering: `hf.co/ltg/normistral-7b-warm-instruct:Q4_K_M` (trent på nb+nn, 4,4 GB, serielt; maskinen har 16 GB).
