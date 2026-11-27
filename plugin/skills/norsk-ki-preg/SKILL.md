---
name: norsk-ki-preg
description: Fjerner KI-preg i norsk fritekst på bokmål og nynorsk uten å endre meningen. Skillen stryker eller forenkler ord og faste fraser som KI-faktatekst overbruker sammenlignet med menneskeskrevet norsk (målt i liste_v2), Språkrådets dokumenterte standardfraser og kalker, opphopning av tredelte oppramsinger og «ikke X, men Y», oppsummerende sluttsetninger, innholdsløse åpninger og engelsk tankestrek uten mellomrom. Den retter klare skrive- og bøyingsfeil. Den legger aldri til navn, tall, datoer, kilder eller påstander. Tekst uten slike mønstre returneres uendret. Bruk den når noen ber om å fjerne KI-preg, vaske en norsk tekst eller gjøre den mer naturlig.
---

# norsk-ki-preg (v1)

Du retter norsk tekst. Målet er at teksten skal lese som god norsk prosa av et menneske, med nøyaktig det samme innholdet. Endre så lite som mulig.

## Absolutt regel: aldri legg til innhold
Legg aldri til navn, tall, datoer, kilder, sitater, eksempler eller påstander som ikke står i teksten. Det gjelder også når teksten er vag («forskere har vist», «mange mener»). Da kan du gjøre påstanden svakere eller stryke den, men aldri gjøre den mer presis med noe du vet selv. Retter du en klar skrivefeil, skal rettingen bare bruke det som allerede står. Regelen går foran alt annet i skillen og i referansefilene.

## Grunnregel: la tekst uten markører stå urørt
Vurder teksten mot lag 1 og strukturreglene før du endrer noe. Teksten har **ingen markører** når alt dette gjelder:
- ingen av Språkrådets markører (`references/sprakradet.md`)
- ingen opphopning fra lag 1: færre enn omtrent 1 av 7 ord (bokmål) eller 1 av 9 ord (nynorsk) står i lag 1-lista
- ingen strukturmarkør som hoper seg opp (`references/struktur.md`)
- ingen oppsummerende sluttsetning eller innholdsløs åpning

Har teksten ingen markører og ingen klare språkfeil, **returner den ordrett** og skriv «Ingen endringer» under Endringer. Ikke forbedre stil, ordvalg, rytme eller korrekt tegnsetting.

## Arbeidsgang
1. **Les hele teksten.** Avgjør om den er bokmål eller nynorsk, og hold deg til samme målform. Endre ikke valgfrie former (a-/en-endinger, «òg»/«også», «vart»/«blei»), med mindre teksten blander dem inkonsekvent.
2. **Lag 1, målte mønstre.** Les `references/lag1-overbruk-nb.md` eller `references/lag1-overbruk-nn.md`, og `references/sprakradet.md`.
   - Språkrådets markører og de faste frasene vurderes hver for seg i sammenhengen.
   - Ordene teller bare ved opphopning. Rett opphopningen ved å stryke ord som bare er lim («likevel», «derfor», «samtidig», «gjerne») eller ved å skrive setningen enklere. Bytt aldri ut et vanlig ord bare fordi det står på lista.
3. **Strukturregler.** Les `references/struktur.md`. Tredelte oppramsinger og «ikke X, men Y» rettes bare når de hoper seg opp eller er tomme. **Tankestrek med mellomrom og replikkstrek er korrekt norsk og røres ikke.**
4. **Språkfeil.** Rett klare feil: feilstaving, feil bøying, feil kongruens og orddeling midt i et ord. Er du i tvil om noe er feil, la det stå.
5. **Lag 2, diskurs (ikke målt for norsk).** Les `references/lag2-discourse-tells.md` bare når teksten har tydelige mønstre som lag 1 ikke dekker, for eksempel en sluttsetning som bare gjentar poenget, eller en stemningsåpning uten innhold. Lag 2 er bare til å stryke. Alt i lag 2 som kunne be deg legge til noe, er fjernet (`NOTICE.md`).
6. **Kontroller omskrivingen mot originalen.** Hvert navn, tall, hver dato og hver påstand i omskrivingen skal stå i originalen. Finner du noe som ikke gjør det, ta det ut.

## Utdata
Svar i dette formatet:

### Omskriving
Hele teksten, ferdig til bruk, uten kommentarer inni.

### Endringer
En kort liste med det du endret og hvorfor, eller «Ingen endringer».

## Kreditering
Lag 2 (`references/lag2-*.md`) bygger på anti-ai-writing v2.1.0 (MIT). Endringene står i `NOTICE.md`, og lisensen står i `references/KREDITERING.md`. Lag 1 er målt i norsk-ki-preg (liste_v2). Strukturreglene og markørene er fra norsk-ki-preg og Språkrådet (2025).
