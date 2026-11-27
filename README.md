# norsk-ki-preg

En skill for Claude som retter KI-preg i norsk tekst (bokmål og nynorsk), med en målt overbruksliste og forhåndsregistrert validering.

## Sammendrag

norsk-ki-preg er en Markdown-skill for Claude som retter KI-preg i bokmål og nynorsk. Den har en fast regel om aldri å legge til navn, tall, datoer eller kilder som ikke står i teksten. Grunnlaget er liste_v2: ord og fraser som Claude Opus 5.5 og NorMistral-7B overbruker i faktatekst sammenlignet med norsk Wikipedia, 475 på bokmål og 175 på nynorsk. Skillen ble sammenlignet med anti-ai-writing v2.1.0 på et urørt sett med 20 KI-tekster og 20 Wikipedia-avsnitt per målform, etter forhåndsregistreringen PREREG v2 (sha256 1e810888865cbdd66761dce6db88178f9374a1c5ee8dda3e1f0f694e4633000c). Målet R er forekomsten av markørene fra lista i KI-tekst etter vask, delt på forekomsten i menneskeskrevet tekst. Etter beslutningsregelen er skillen ikke bedre: R_engelsk − R_norsk var −0,107 [−0,185; −0,039] på bokmål og −0,055 [−0,122; 0,010] på nynorsk. Den endret menneskeskrevet tekst langt mindre: median normalisert redigeringsavstand (M3) var 0,002 og 0,003, mot 0,339 og 0,272. Den la ikke til innhold i noen av 80 tekster. anti-ai-writing la til navngitte kilder eller fakta fra utenfor kildeteksten i 4 av 80. Det er ikke sjekket om tilskrivingene er riktige. Kjent begrensning: grunnregelen lot 25 av 40 KI-tekster stå urørt. Lisenser: Apache-2.0 for kode og skill, MIT for delen fra anti-ai-writing, CC BY-SA 3.0 for data og liste_v2.

## Summary (English)

norsk-ki-preg is a Markdown skill for Claude removing AI tells from Bokmål and Nynorsk text. A fixed rule bars it from adding names, numbers, dates or sources not in the text. It builds on liste_v2: 475 Bokmål and 175 Nynorsk words and phrases Claude Opus 5.5 and NorMistral-7B overuse in expository text versus Norwegian Wikipedia. The skill was compared with anti-ai-writing v2.1.0 on untouched sets of 20 AI texts and 20 Wikipedia paragraphs per variety, as preregistered in PREREG v2 (sha256 1e810888865cbdd66761dce6db88178f9374a1c5ee8dda3e1f0f694e4633000c). The measure R is the listed markers' rate in AI text after editing, divided by their rate in human-written text. Under the decision rule, the skill is not better: R_English − R_Norwegian was −0.107 [−0.185; −0.039] for Bokmål and −0.055 [−0.122; 0.010] for Nynorsk. It changed human-written text far less: median normalised edit distance (M3) 0.002 and 0.003, against 0.339 and 0.272. It added content to none of 80 texts. anti-ai-writing added named sources or facts absent from the source to 4 of 80. Their accuracy was not checked. Known limitation: the basic rule left 25 of 40 AI texts untouched. Licences: Apache-2.0 for code and skill, MIT for the anti-ai-writing part, CC BY-SA 3.0 for data and liste_v2.

A skill for Claude that removes AI tells from Norwegian text.

## Bruk

Kopier mappa `skills/norsk-ki-preg/` til skill-mappa i Claude (for eksempel `~/.claude/skills/norsk-ki-preg/`). Skillen er bare Markdown: `SKILL.md`, `references/` og `NOTICE.md`. Den svarer med en omskriving og en liste over endringer, eller med «Ingen endringer».

## Innhold

- `skills/norsk-ki-preg/`: skill v1 (`NOTICE.md` viser hva som er hentet fra anti-ai-writing og endret). Skill v0 ligger i commit c947a62.
- `liste_v2.json`, `liste_v2.md`: målt liste (v1). `liste_v1.*` er fase B.
- `PREREG_v2.md` og `PREREG_v2.md.ots`: forhåndsregistrering for v1. `PREREG.md` og `PREREG.md.ots` gjelder fase B.
- `NKP-V1-RAPPORT_norsk-ki-preg_v1_2026-11-27.md`: hovedrapporten.
- Forløpere: `NKP-ROYK-RAPPORT_norsk-ki-preg_v1_2026-11-24.md` (fase A), `NKP-FASEB-DEL1_norsk-ki-preg_2026-11-24.md` og `NKP-FASEB-RAPPORT_norsk-ki-preg_v1_2026-11-27.md` (fase B og skill v0).
- `AVVIK.md`: alle avvik. `FORBRUK.md`: tokenforbruk. `logg/`: kjørelogg og commit-kart etter historikkrensingen.
- `data/`, `resultat/`, `skript/`: data, resultater og koden som produserte dem.

## Status

- Fase A (24.11.2026): røyktest. Resultat: fase B trengs.
- Fase B (27.11.2026): liste_v1 og skill v0. Etter `PREREG.md`: ikke bedre.
- v1 (27.11.2026): Wikipedia-referanse, liste_v2 og skill v1. Etter `PREREG_v2.md`: ikke bedre (R-vilkåret feiler). Skill v1 endrer menneskeskrevet tekst nesten ikke og legger ikke til innhold.

## Lisenser

Se `LISENSER.md` og AVVIK V12.
- Apache-2.0 (`LISENS`): kode (`skript/`) og skill (`skills/norsk-ki-preg/`).
- MIT: lag 2 (`skills/norsk-ki-preg/references/lag2-*.md`), fra anti-ai-writing v2.1.0 av Tato Polanco. Kreditert i `NOTICE.md` og `references/KREDITERING.md`.
- CC BY-SA 3.0: data, `liste_v1`, `liste_v2`, resultater og rapporter. Wikipedia-utdragene er © bidragsytere til norsk Wikipedia (bokmål og nynorsk), via NbAiLab/NCC.

## Sitering

Botten Nicolaysen, E. (2026). *norsk-ki-preg: en skill som retter KI-preg i norsk tekst* (versjon 1.0.0) [programvare og data]. Se `CITATION.cff`.

## KI-erklæring

Språkmodeller ble brukt i to roller. Som forskningsinstrument genererte Claude Opus 5.5 og NorMistral-7B tekstene som ble målt, og Claude Opus 5.5 utførte vaskene under låste instrukser. Rollene står i metoden (PREREG og rapportene). Som verktøy ble Claude Code brukt til kode og tekstarbeid under forfatterens styring. Forfatteren bestemte opplegget og beslutningsreglene og tar ansvar for innholdet. Avvikene er ført i AVVIK.md.

KI-erklæring: implementert med Claude Code.
