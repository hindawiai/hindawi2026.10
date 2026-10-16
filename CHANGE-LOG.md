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

## C1. Executable bits restored

**Why.** The archive stored no permissions, so `scripts/test_all.sh` stopped at its first script with "Permission denied" (exit 126). Contents are unchanged.

- `benchmarks/local_inverse.js`: mode 755
- `docs/source-stages/BUILD_PIPELINE.sh`: mode 755
- `docs/vendor-packs/nirgundi-source-attribution-pack/scripts/download_csl_mw.py`: mode 755
- `lang/hindawi/filters/fltr_hi_he.py`: mode 755
- `lang/hindawi/pipeline/transliterate.py`: mode 755
- `lang/hindawi/test_ports.py`: mode 755
- `lang/hindawi/test_sanchalan_ports.py`: mode 755
- `lang/hindawi/upstream/chintamani/guru/gurucc`: mode 755
- `lang/hindawi/upstream/chintamani/praatha/praathacc`: mode 755
- `lang/hindawi/upstream/chintamani/shabda/shabdacc`: mode 755
- `lang/hindawi/upstream/chintamani/shraeni/shraenicc`: mode 755
- `lang/hindawi/upstream/chintamani/soochee/fixpy.awk`: mode 755
- `lang/hindawi/upstream/chintamani/soochee/soocheecc`: mode 755
- `lang/hindawi/upstream/chintamani/wyaaka/wyaakacc`: mode 755
- `lang/js/backend.js`: mode 755
- `lang/js/raise.js`: mode 755
- `lang/js/run.js`: mode 755
- `lang/js/run_bootstrap.js`: mode 755
- `lang/js/test_backend.js`: mode 755
- `lang/suktam/hindawi/build.sh`: mode 755
- `lang/suktam/kernel/run-first-login.sh`: mode 755
- `lang/suktam/run-qemu.sh`: mode 755
- `lang/suktam/test/suktam.test.js`: mode 755
- `scripts/build_docs_catalog.py`: mode 755
- `scripts/build_romenagri.sh`: mode 755
- `scripts/generate_hindawi_ports.py`: mode 755
- `scripts/hindawi_language_port_audit.py`: mode 755
- `scripts/nirgundi/expand_all_sutras.py`: mode 755
- `scripts/nirgundi/extract_mw_k1.py`: mode 755
- `scripts/nirgundi/observed_form_bootstrap.py`: mode 755
- `scripts/nirgundi/run_experiment.py`: mode 755
- `scripts/romenagri_perso_arabic_filter.sh`: mode 755
- `scripts/test_all.sh`: mode 755
- `scripts/vendor_romenagri.sh`: mode 755
- `tests/test_browser_labs.js`: mode 755
- `tests/test_pages_http.py`: mode 755
- `tests/test_romenagri_integration.sh`: mode 755
- `tests/test_static_pages.sh`: mode 755
- `tools/pushkalavati-compiler/src/cli.js`: mode 755
- `tools/pushkalavati-compiler/src/inverse-cli.js`: mode 755
- `tools/pushkalavati-compiler/vendor/romenagri/upstream/filters/perso2deva_heur.py`: mode 755
- `tools/pushkalavati-compiler/vendor/romenagri/upstream/filters/rom2deva_heur.py`: mode 755
- `tools/pushkalavati-compiler/vendor/romenagri/upstream/ilm-living-standards/src/living_standards_generator.py`: mode 755
- `tools/pushkalavati-compiler/vendor/romenagri/upstream/ilm-living-standards/src/review_tool.py`: mode 755
- `tools/pushkalavati-compiler/vendor/romenagri/upstream/langspec/generator/autoseed_from_registry.py`: mode 755
- `tools/pushkalavati-compiler/vendor/romenagri/upstream/langspec/generator/derive_keywords.py`: mode 755
- `tools/pushkalavati-compiler/vendor/romenagri/upstream/langspec/generator/langspec_generator.py`: mode 755
- `tools/pushkalavati-compiler/vendor/romenagri/upstream/langspec/tools/langspec_gen.py`: mode 755

**Verified.** `scripts/test_all.sh` gets past the step that failed.
