---
name: norsk-ki-preg
description: Retter KI-preg og språkfeil i norsk tekst på bokmål og nynorsk. Skillen fjerner målte overbruksmønstre (sitatrammer, faste fraser og ordpar som KI-tekst bruker oftere enn menneskeskrevet norsk), Språkrådets dokumenterte stående fraser, avslutningsformler og kalker, opphopning av tredelte oppramsinger og «ikke X, men Y», engelsk tankestrek uten mellomrom og engelsk stor forbokstav i overskrifter. Den retter klare skrive- og rettskrivingsfeil. Tekst uten slike mønstre returneres uendret. Bruk den når noen ber om å fjerne KI-preg, vaske en norsk tekst, gjøre den mer naturlig eller rette den. Versjon v0, bygd på liste_v1 (norsk-ki-preg). Lag 2 (diskurs) er gjenbrukt fra anti-ai-writing og er ikke målt for norsk.
---

# norsk-ki-preg (v0)

Du retter norsk tekst. Målet er at teksten skal lese som god norsk prosa av et menneske, med samme innhold. Endre så lite som mulig.

## Grunnregel: la tekst uten markører stå urørt
Finner du ingen markører fra lag 1, ingen strukturmarkører og ingen klare språkfeil, **returner teksten ordrett uendret**. Skriv «Ingen endringer» under Endringer. Ikke forbedre stil, ordvalg, rytme eller tegnsetting som er korrekt etter rettskrivingen. Menneskeskrevet tekst skal som regel stå nesten urørt.

## Arbeidsgang
1. **Les hele teksten.** Avgjør om den er bokmål eller nynorsk, og bruk samme målform hele veien. Bytt aldri målform. Endre ikke valgfrie former (for eksempel a-/en-endinger, «òg»/«også», «vart»/«blei»), med mindre teksten blander dem inkonsekvent.
2. **Lag 1, målte mønstre.** Les `references/lag1-overbruk-nb.md` eller `references/lag1-overbruk-nn.md`, og `references/sprakradet.md`.
   - Fraser og Språkrådets markører vurderes hver for seg i sammenhengen.
   - Lemmaene teller bare ved opphopning. Bytt aldri ut et vanlig ord bare fordi det står på lista.
3. **Strukturregler.** Les `references/struktur.md`. Tredelte oppramsinger og «ikke X, men Y» rettes bare når de hoper seg opp eller er tomme. **Tankestrek med mellomrom og replikkstrek er korrekt norsk og røres ikke.**
4. **Språkfeil.** Rett klare feil: feilstaving, feil bøying, orddeling midt i et ord (for eksempel OCR-rester som «spylevog nen» → «spylevognen»), feil kongruens og manglende ord. Er du i tvil om noe er feil, la det stå.
5. **Lag 2, diskurs (ikke målt for norsk).** Les `references/lag2-discourse-tells.md` bare når teksten har tydelige mønstre som lag 1 ikke dekker, for eksempel en oppsummerende sluttsetning som bare gjentar teksten eller en stemningsåpning uten innhold. Ved tvil, la det stå. Disse reglene er laget for engelsk og er ikke testet på norsk.
6. **Les omskrivingen.** Innholdet skal være det samme: ingen nye fakta, navn, tall eller sitater. Stryk heller enn å finne opp.

## Utdata
Svar i dette formatet:

### Omskriving
Hele teksten, ferdig til bruk, uten kommentarer inni.

### Endringer
En kort liste med det du endret og hvorfor, eller «Ingen endringer».

## Kreditering
Lag 2 (`references/lag2-*.md`) er kopiert uendret fra anti-ai-writing v2.1.0 (MIT, se `references/KREDITERING.md`). Lag 1 og strukturreglene er målt i norsk-ki-preg (liste_v1) eller hentet fra Språkrådet (2025).
