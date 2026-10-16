# How hindawi2026.10 was put together

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

**Inputs**, kept byte for byte in `releases/originals/` and pinned in its `SHA256SUMS`:
- `BUILD-0102__pushkalavati-hindawi-ilm-2026-10-16.zip`, the base;
- `HINDAWI2026_10-best.zip` (Grok): BUILD-0102 plus four files;
- `HINDAWI2026_10-regression.zip` (Grok): the same plus one ingestion's dictionary;
- `HINDAWI2026_10-ingest.zip` (Grok): the file-name fix and `ingest_dir.py`;
- `CHECKLIST-FOR-CLAUDE.md` (Grok).

**History.** One commit per change, C0 to C15, each recorded in `CHANGE-LOG.md` with its paths and hashes:
- **C0 to C9:** BUILD-0102 restructured without changing what it does (BUILD-0103). The generated compiler output is
  left out, and the language cells live in `lang/hindawi/languages/` so Chintamani's copy stays Chintamani.
- **C10:** Grok's ingestion tools, exactly as delivered.
- **C11:** those tools and the multi-file driver put on the original chain, and the fundamental regression.
- **C12 and C13:** the upstream checks, the documents, the localisation page and the regenerated index.
- **C14:** Grok's fix keeping file names out of the ingestion dictionary, merged into the original-chain ingester.
- **C15:** the fundamental regression made safe on any machine (bounded steps, unjudged when it cannot judge).

Tags: `build-0102` at C0, `hindawi2026.10` at C15.

**Taken from Grok and kept:** `ingest.py` (a dictionary per ingestion, names in the language),
`import_project.py`, `identifier_map.py`, `tests/regression.sh`, and the 76 language cells as BUILD-0102 has them.

**Not taken:** BUILD-0117's regenerated cells and `normalize.py`, which Grok itself withdrew. The audit bundle
from ChatGPT was read, not included.

**What the gate proves (`ops/verify.sh`):**
- S01: the inputs match their pins.
- S02: BUILD-0102 is in the history exactly as received.
- S03: the build's own suite passes.
- S04 and S05: no secrets, no file over 95 MB.
- S06: the metadata agree.
- tests/fundamental.py is not part of the gate; run it by hand: bash scripts/fetch.sh && bash scripts/build.sh && python3 tests/fundamental.py

**Known limits, measured and written down in `docs/hindawi/ADDING-LANGUAGES.md`:**
- Romenagri's `acii2cf` doubles underscores in ASCII identifiers, so SeaBIOS builds as is but not through the Hindi
  pair.
- Chintamani's own assembly pair is not round-trip stable on its sample.
- Only Devanagari, and Brahmi scripts through it, are reversible to the lowest layer today.
