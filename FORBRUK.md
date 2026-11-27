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

# FORBRUK – faktisk (2026-11-24)
| Ledd | Kall | Tokens (harness `subagent_tokens`) | Per kall |
|---|---|---|---|
| Generering (Opus 5.5) | 20 | 1 654 795 | 82 740 |
| Vask (Opus 5.5 + skill) | 12 | 1 610 496 | 134 208 |
| **Subagenter i alt** | 32 | **3 265 291** | |
| Hovedøkt | 1 | ikke målt | |

Overslaget (~1,3–1,5M) var for lavt med en faktor på rundt 2,3. Hvert subagentkall har en fast grunnkostnad på ~75–80k tokens (systemprompt og verktøy), uavhengig av oppgaven. Det meste er cache-lesing.

Lokal modell: `hf.co/ltg/normistral-7b-warm-instruct:Q4_K_M`, 100 fortsettelser, 582 s maskintid i alt (median 5,3 s). Ingen andre lokale modeller ble brukt. M2 kjørte `intfloat/multilingual-e5-small` på CPU i under ett minutt. Ingen modell ble lastet ned, og ingen betalte API-er ble brukt.

# FASE B – kallmekanisme (steg 1, 2026-11-24)
| Mekanisme | Tekster per kall | Tokens per kall | Per tekst | Status |
|---|---|---|---|---|
| `claude -p --model claude-opus-5-5 --output-format json`, minimal systemprompt, `--tools ""` | 1 | – | – | **ikke målbar**: CLI-en er ikke innlogget (`claude auth status` → `loggedIn: false`, «OAuth session expired»). `--bare` godtar bare API-nøkkel, som er forbudt. 3 forsøk, 0 tokens. |
| Subagent general-purpose (røyktest, 20 kall) | 5 | 82 740 | 16 548 | målt |
| Subagent **Explore** (read-only), svar i handback | 5 | 53 557 | **10 711** | målt (1 kall) |

**Valg: Explore-subagent, 5 tekster per kall.** Utdata hentes fra `SubagentHandback` i transkriptfila med et skript (`skript/hent_handback.py`) og går ikke gjennom hovedøktas kontekst. Ett uavhengig kall per tekst ville gitt rundt 53k per tekst, 5 ganger så mye. Det oppfyller ikke 1,5×-kriteriet.

## Anslag DEL 2 (før kutt)
| Ledd | Tekster | Kall (5/kall) | Tokens |
|---|---|---|---|
| Fortsettelser (240 nb + 185 nn) | 425 | 85 | 4,55M |
| Fritekst (50 + 50) | 100 | 20 | 1,07M |
| Valideringsemner (20 + 20) | 40 | 8 | 0,43M |
| Vask, validering: (40 KI + 40 menneske) × 2 skills | 160 | 32 | ≈ 3,4M (Explore + skill ≈ 105k per kall, røyktest-tallet 134k minus Explore-rabatten 29k) |
| Hovedøkt | – | – | ≈ 0,8M |
| **Sum** | | **145** | **≈ 10,3M** < tak 12M → ingen kutt |

Margin ≈ 1,7M (14 %). Hvis de første 10 genereringskallene i snitt bruker over 62k per kall, kuttes fritekst til 25 per variant før resten startes. Regelen er låst i PREREG.md.

# DEL 2 – steg 7 budsjettsjekk (2026-11-27)
Anslag 10,3M < tak 12M → **ingen kutt**. Fritekst 50/50, validering 20/20, fortsettelser 240/185. Kontrollpunkt: snittet av `subagent_tokens` for de 10 første genereringskallene sammenlignes med 62k.
