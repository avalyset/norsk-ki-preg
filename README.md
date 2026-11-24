# norsk-ki-preg – røyktest

Spørsmål: fjerner anti-ai-writing v2.1.0 (avectats7, MIT) KI-preg i norsk tekst (bokmål og nynorsk), eller trengs en målt norsk markørliste?

Status: røyktest (fase A). Beslutningsregelen er låst i `BESLUTNING.md` før datauttrekk.

Struktur:
- `BESLUTNING.md` – låst beslutningsregel (sha256 i `logg/kjorelogg.md`)
- `markorer_v0.json` – frosset markørliste (Språkrådet 2025 + strukturmarkører)
- `data/` – NCC-utvalg, fortsettelser, vaskede tekster (JSONL)
- `skript/` – uttrekk, generering, måling
- `resultat/` – M1–M4
- `AVVIK.md` – alle avvik fra planen
- `FORBRUK.md` – forbruksoverslag og faktisk forbruk

Ingen KI-detektorer brukes. Lisens: Apache-2.0 (kode). Data fra NCC beholder kildelisensen (CC0 / NLOD 2.0).
