# norsk-ki-preg

En skill for Claude som retter KI-preg i norsk tekst (bokmål og nynorsk). / A skill for Claude that removes AI tells from Norwegian text.

DOI: [10.5281/zenodo.24586253](https://doi.org/10.5281/zenodo.24586253) · Repo: https://github.com/avalyset/norsk-ki-preg

## Norsk

norsk-ki-preg er en Markdown-skill for Claude som retter KI-preg i bokmål og nynorsk. Den har en fast regel om aldri å legge til navn, tall, datoer eller kilder som ikke står i teksten. Grunnlaget er liste_v2: ord og fraser som Claude Opus 5.5 og NorMistral-7B overbruker i faktatekst sammenlignet med norsk Wikipedia, 475 på bokmål og 175 på nynorsk. Skillen ble sammenlignet med anti-ai-writing v2.1.0 på et urørt sett med 20 KI-tekster og 20 Wikipedia-avsnitt per målform, etter forhåndsregistreringen PREREG v2 (sha256 1e810888865cbdd66761dce6db88178f9374a1c5ee8dda3e1f0f694e4633000c). Målet R er forekomsten av markørene fra lista i KI-tekst etter vask, delt på forekomsten i menneskeskrevet tekst. Etter beslutningsregelen er skillen ikke bedre: R_engelsk − R_norsk var −0,107 [−0,185; −0,039] på bokmål og −0,055 [−0,122; 0,010] på nynorsk. Den endret menneskeskrevet tekst langt mindre: median normalisert redigeringsavstand (M3) var 0,002 og 0,003, mot 0,339 og 0,272. Den la ikke til innhold i noen av 80 tekster. anti-ai-writing la til navngitte kilder eller fakta fra utenfor kildeteksten i 4 av 80. Det er ikke sjekket om tilskrivingene er riktige. Kjent begrensning: grunnregelen lot 25 av 40 KI-tekster stå urørt. Lisenser: Apache-2.0 for kode og skill, MIT for delen fra anti-ai-writing, CC BY-SA 3.0 for data og liste_v2.

## English

norsk-ki-preg is a Markdown skill for Claude removing AI tells from Bokmål and Nynorsk text. A fixed rule bars it from adding names, numbers, dates or sources not in the text. It builds on liste_v2: 475 Bokmål and 175 Nynorsk words and phrases Claude Opus 5.5 and NorMistral-7B overuse in expository text versus Norwegian Wikipedia. The skill was compared with anti-ai-writing v2.1.0 on untouched sets of 20 AI texts and 20 Wikipedia paragraphs per variety, as preregistered in PREREG v2 (sha256 1e810888865cbdd66761dce6db88178f9374a1c5ee8dda3e1f0f694e4633000c). The measure R is the listed markers' rate in AI text after editing, divided by their rate in human-written text. Under the decision rule, the skill is not better: R_English − R_Norwegian was −0.107 [−0.185; −0.039] for Bokmål and −0.055 [−0.122; 0.010] for Nynorsk. It changed human-written text far less: median normalised edit distance (M3) 0.002 and 0.003, against 0.339 and 0.272. It added content to none of 80 texts. anti-ai-writing added named sources or facts absent from the source to 4 of 80. Their accuracy was not checked. Known limitation: the basic rule left 25 of 40 AI texts untouched. Licences: Apache-2.0 for code and skill, MIT for the anti-ai-writing part, CC BY-SA 3.0 for data and liste_v2.

## Innhold / Contents

- `skills/norsk-ki-preg/`: skillen (`SKILL.md` og `references/`)
- `LICENSE`: Apache-2.0 (skillen)
- `NOTICE.md`: kreditering av anti-ai-writing (MIT) / credit for anti-ai-writing (MIT)

Måledata, skript, forhåndsregistrering og rapporter ligger i hovedrepoet og i Zenodo-depositumet. / Data, scripts, preregistration and reports are in the main repository and the Zenodo deposit.
