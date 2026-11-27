# norsk-ki-preg

Spørsmål: fjerner anti-ai-writing v2.1.0 (avectats7, MIT) KI-preg i norsk tekst (bokmål og nynorsk), eller trengs en målt norsk markørliste?

Status:
- Fase A fullført 2026-11-24. Beslutning: fase B trengs (utløst av nynorsk). Se NKP-ROYK-RAPPORT_norsk-ki-preg_v1_2026-11-24.md.
- Fase B fullført 2026-11-27: målt liste (`liste_v1.json`, `liste_v1.md`) og norsk skill v0 (`skills/norsk-ki-preg/`). Valideringsregelen i PREREG.md ga **ikke bedre**: den norske skillen endret menneskeskrevet tekst mindre, men senket ikke markørraten mer enn anti-ai-writing. Se NKP-FASEB-RAPPORT_norsk-ki-preg_v1_2026-11-27.md.

Forhåndsregistrering: `PREREG.md` (sha256 f3e13a9c…dd521df9, OpenTimestamps i `PREREG.md.ots`). Ikke publisert.

Struktur:
- `BESLUTNING.md` – låst beslutningsregel for fase A (sha256 i `logg/kjorelogg.md`)
- `PREREG.md` – låst plan for fase B
- `liste_v1.json`, `liste_v1.md` – målt liste (fase B)
- `skills/norsk-ki-preg/` – norsk skill v0 (Markdown)
- `markorer_v0.json` – frosset markørliste (Språkrådet 2025 + strukturmarkører)
- `data/` – NCC-utvalg, genererte tekster, vaskede tekster (JSONL)
- `skript/` – uttrekk, generering, måling
- `resultat/` – M1–M4
- `AVVIK.md` – alle avvik fra planen
- `FORBRUK.md` – forbruksoverslag og faktisk forbruk

Ingen KI-detektorer brukes. Lisens: Apache-2.0 (kode). Data fra NCC beholder kildelisensen (CC0; fase B bruker bare CC0, AVVIK B3). Lag 2 i skillen er MIT (anti-ai-writing, se `skills/norsk-ki-preg/references/KREDITERING.md`).
