# NOTICE – norsk-ki-preg (katalogplugin / directory plugin)

Denne pluginen er lisensiert under Apache-2.0 (`LICENSE`), med unntak av to filer: `skills/norsk-ki-preg/references/lag2-discourse-tells.md` og `skills/norsk-ki-preg/references/lag2-discourse-rewrites.md`. De bygger på **anti-ai-writing v2.1.0** av Tato Polanco (github.com/avectats7/anti-ai-writing) og er lisensiert under MIT, © 2026 Tato Polanco. Den fullstendige MIT-lisensteksten står i `skills/norsk-ki-preg/references/KREDITERING.md`.

This plugin is licensed under Apache-2.0 (`LICENSE`), except the two files above, which build on anti-ai-writing v2.1.0 by Tato Polanco and are licensed under MIT, © 2026 Tato Polanco. The full MIT licence text is in `skills/norsk-ki-preg/references/KREDITERING.md`.

Endringene fra originalen står nedenfor (samme tekst som `skills/norsk-ki-preg/NOTICE.md`). / The changes from the original are listed below.

---


Denne skillen inneholder materiale fra **anti-ai-writing v2.1.0** av Tato Polanco (github.com/avectats7/anti-ai-writing), MIT-lisens. Lisensteksten står i `references/KREDITERING.md`.

## Hva som er hentet
`references/lag2-discourse-tells.md` og `references/lag2-discourse-rewrites.md` (lag 2, diskurs), på engelsk.

## Hva som er endret (norsk-ki-preg v1, 27.11.2026)
Alt i lag 2 som ber om å legge til innhold, er fjernet eller endret. Det gjelder særlig **signalet om å gjeninnføre navngitte detaljer** («Named specifics»).

I `lag2-discourse-tells.md`:
- Seksjonen «Six signals to restore, and the budget that limits them» er fjernet i sin helhet, med alle seks signalene, blant dem «3. Named specifics».
- Under vane 6 («The vague allusion») er regelen «every paragraph that makes a claim names something real …» erstattet med: gjør påstanden svakere eller stryk den, og legg aldri til navn, tall, datoer eller kilder.
- Tabellen over lengdebånd tillater ingen tilføyelser i noe bånd.
- Sjekklisten spør om noe er lagt til i stedet for om tilføyelsene er innenfor budsjettet.
- Henvisninger til de fjernede signalene er tatt ut.

I `lag2-discourse-rewrites.md`:
- «Fix 6: name something real» er erstattet med «Fix 6: weaken or cut the vague claim».
- «Fix 7: assume shared history», «Additions: address, jumps, ambivalence» og «The three tests every addition has to pass» er fjernet.
- Guardrail 2 og 3 sier nå at ingenting skal legges til.
- Rådet om å styrke belegget og punktet «The named specific is wrong» er fjernet.

## Hvorfor
I valideringen av v0 la anti-ai-writing inn forskernavn og årstall som ikke sto i teksten, i 4 av 80 tekster (norsk-ki-preg AVVIK B14). Den norske skillen skal aldri legge til innhold.

## Resten
Lag 1 (`references/lag1-overbruk-*.md`) er målt i norsk-ki-preg (liste_v2). `references/sprakradet.md` bygger på Språkrådet (2025), rapporten om test av språkroboter, med sidetall. `references/struktur.md` er norsk-ki-preg.
