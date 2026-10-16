# Change log, absolute

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

Every change from BUILD-0102 (as received on 16 October 2026) to BUILD-0103 is recorded here: one entry
per change, and one git commit per entry, in the same order. Paths are relative to the repository root;
hashes are SHA-256. Nothing changed that is not listed.

The previous builds carried no git history. This repository's history starts at C0.

## C0. BUILD-0102 as received, without its generated compiler outputs

**Why.** The 88 MB tree was mostly the compiler's own regenerated output. `scripts/test_all.sh` rebuilds it (`npm run compile:rules`) before anything reads it, so it does not belong in history. The files remain in the BUILD-0102 archive.

- left out: `tools/pushkalavati-compiler/out/functional-classification.json` (1,993,001 bytes, sha256 `48d361989ab6c966796dc39f7f40d8cf5787a81a0f641f70bdbfa2d14ba1fb6b`)
- left out: `tools/pushkalavati-compiler/out/generated-rules.json` (1,919,252 bytes, sha256 `b01faeac48684890c5bc10539248061a291d25e67c9d39a9c4b466c83662c157`)
- left out: `tools/pushkalavati-compiler/out/meta-compiler-catalog.json` (272,981 bytes, sha256 `74632fcc7336ab76b728d16dd3d4681c037d91332b185ac2578e41de3f5055ce`)
- left out: `tools/pushkalavati-compiler/out/meta-expansion.json` (27,732,972 bytes, sha256 `f6fc35f8bb87f97ef063df83c181a62486710983472137e0ba230777156b3b14`)
- left out: `tools/pushkalavati-compiler/out/progress.json` (1,506 bytes, sha256 `5d1ebb404f1b62d33ff971d625c98e5eb9cfd8e7e2e1c6d3bb33007645ce0c4c`)
- left out: `tools/pushkalavati-compiler/out/rules-ir.json` (21,074,285 bytes, sha256 `9edd1688827a2e06c50ed2e79ef2274d94044df5e92766da1a531b12fcc3d866`)
- `.gitignore`: those outputs and the flex build products of the language cells are ignored

**Verified.** `scripts/test_all.sh` regenerates the outputs; see C8 for the full run.
