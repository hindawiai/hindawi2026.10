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

## C2. Pages workflow restored from BUILD-0024

**Why.** `tests/test_static_pages.sh` requires `.github/workflows/pages.yml`; BUILD-0102 does not carry it, so its own test script failed (exit 1) at the Pages step.

- added `.github/workflows/pages.yml`, byte for byte from BUILD-0024 (sha256 `e54dbada5fced646f4a488cc2ae692ab4d4788a47c552f0dab6d8c1377ea6cf6`)

**Verified.** `tests/test_static_pages.sh` passes.

## C3. Generated language cells moved out of the Chintamani copy

**Why.** `lang/hindawi/upstream/chintamani/` must hold Chintamani as it is. Its seven original folders are byte-identical to hindawiai/chintamani; the other 76 folders were generated for this build and were mixed in beside them. They now live in `lang/hindawi/languages/`, beside its `registry.csv`.

- moved `lang/hindawi/upstream/chintamani/arabic/` to `lang/hindawi/languages/arabic/`
- moved `lang/hindawi/upstream/chintamani/aramaic/` to `lang/hindawi/languages/aramaic/`
- moved `lang/hindawi/upstream/chintamani/assamese/` to `lang/hindawi/languages/assamese/`
- moved `lang/hindawi/upstream/chintamani/awadhi/` to `lang/hindawi/languages/awadhi/`
- moved `lang/hindawi/upstream/chintamani/balinese/` to `lang/hindawi/languages/balinese/`
- moved `lang/hindawi/upstream/chintamani/balochi/` to `lang/hindawi/languages/balochi/`
- moved `lang/hindawi/upstream/chintamani/batak/` to `lang/hindawi/languages/batak/`
- moved `lang/hindawi/upstream/chintamani/bengali/` to `lang/hindawi/languages/bengali/`
- moved `lang/hindawi/upstream/chintamani/bhojpuri/` to `lang/hindawi/languages/bhojpuri/`
- moved `lang/hindawi/upstream/chintamani/bodo/` to `lang/hindawi/languages/bodo/`
- moved `lang/hindawi/upstream/chintamani/buginese/` to `lang/hindawi/languages/buginese/`
- moved `lang/hindawi/upstream/chintamani/bulgarian/` to `lang/hindawi/languages/bulgarian/`
- moved `lang/hindawi/upstream/chintamani/burmese/` to `lang/hindawi/languages/burmese/`
- moved `lang/hindawi/upstream/chintamani/chhattisgarhi/` to `lang/hindawi/languages/chhattisgarhi/`
- moved `lang/hindawi/upstream/chintamani/chinese/` to `lang/hindawi/languages/chinese/`
- moved `lang/hindawi/upstream/chintamani/dari/` to `lang/hindawi/languages/dari/`
- moved `lang/hindawi/upstream/chintamani/dogri/` to `lang/hindawi/languages/dogri/`
- moved `lang/hindawi/upstream/chintamani/dzongkha/` to `lang/hindawi/languages/dzongkha/`
- moved `lang/hindawi/upstream/chintamani/gujarati/` to `lang/hindawi/languages/gujarati/`
- moved `lang/hindawi/upstream/chintamani/hausa_ajami/` to `lang/hindawi/languages/hausa_ajami/`
- moved `lang/hindawi/upstream/chintamani/hebrew/` to `lang/hindawi/languages/hebrew/`
- moved `lang/hindawi/upstream/chintamani/hindi/` to `lang/hindawi/languages/hindi/`
- moved `lang/hindawi/upstream/chintamani/japanese/` to `lang/hindawi/languages/japanese/`
- moved `lang/hindawi/upstream/chintamani/javanese/` to `lang/hindawi/languages/javanese/`
- moved `lang/hindawi/upstream/chintamani/kannada/` to `lang/hindawi/languages/kannada/`
- moved `lang/hindawi/upstream/chintamani/kashmiri/` to `lang/hindawi/languages/kashmiri/`
- moved `lang/hindawi/upstream/chintamani/kashmiri_dev/` to `lang/hindawi/languages/kashmiri_dev/`
- moved `lang/hindawi/upstream/chintamani/khmer/` to `lang/hindawi/languages/khmer/`
- moved `lang/hindawi/upstream/chintamani/konkani/` to `lang/hindawi/languages/konkani/`
- moved `lang/hindawi/upstream/chintamani/korean/` to `lang/hindawi/languages/korean/`
- moved `lang/hindawi/upstream/chintamani/kurdish_sorani/` to `lang/hindawi/languages/kurdish_sorani/`
- moved `lang/hindawi/upstream/chintamani/lao/` to `lang/hindawi/languages/lao/`
- moved `lang/hindawi/upstream/chintamani/lepcha/` to `lang/hindawi/languages/lepcha/`
- moved `lang/hindawi/upstream/chintamani/limbu/` to `lang/hindawi/languages/limbu/`
- moved `lang/hindawi/upstream/chintamani/magahi/` to `lang/hindawi/languages/magahi/`
- moved `lang/hindawi/upstream/chintamani/maithili/` to `lang/hindawi/languages/maithili/`
- moved `lang/hindawi/upstream/chintamani/malay_jawi/` to `lang/hindawi/languages/malay_jawi/`
- moved `lang/hindawi/upstream/chintamani/malayalam/` to `lang/hindawi/languages/malayalam/`
- moved `lang/hindawi/upstream/chintamani/mandaic/` to `lang/hindawi/languages/mandaic/`
- moved `lang/hindawi/upstream/chintamani/manipuri_beng/` to `lang/hindawi/languages/manipuri_beng/`
- moved `lang/hindawi/upstream/chintamani/marathi/` to `lang/hindawi/languages/marathi/`
- moved `lang/hindawi/upstream/chintamani/marwari/` to `lang/hindawi/languages/marwari/`
- moved `lang/hindawi/upstream/chintamani/nabataean/` to `lang/hindawi/languages/nabataean/`
- moved `lang/hindawi/upstream/chintamani/nepali/` to `lang/hindawi/languages/nepali/`
- moved `lang/hindawi/upstream/chintamani/newari/` to `lang/hindawi/languages/newari/`
- moved `lang/hindawi/upstream/chintamani/odia/` to `lang/hindawi/languages/odia/`
- moved `lang/hindawi/upstream/chintamani/pali/` to `lang/hindawi/languages/pali/`
- moved `lang/hindawi/upstream/chintamani/pashto/` to `lang/hindawi/languages/pashto/`
- moved `lang/hindawi/upstream/chintamani/persian/` to `lang/hindawi/languages/persian/`
- moved `lang/hindawi/upstream/chintamani/phoenician/` to `lang/hindawi/languages/phoenician/`
- moved `lang/hindawi/upstream/chintamani/prakrit/` to `lang/hindawi/languages/prakrit/`
- moved `lang/hindawi/upstream/chintamani/punjabi/` to `lang/hindawi/languages/punjabi/`
- moved `lang/hindawi/upstream/chintamani/punjabi_shahmukhi/` to `lang/hindawi/languages/punjabi_shahmukhi/`
- moved `lang/hindawi/upstream/chintamani/rajasthani/` to `lang/hindawi/languages/rajasthani/`
- moved `lang/hindawi/upstream/chintamani/russian/` to `lang/hindawi/languages/russian/`
- moved `lang/hindawi/upstream/chintamani/samaritan/` to `lang/hindawi/languages/samaritan/`
- moved `lang/hindawi/upstream/chintamani/sanskrit/` to `lang/hindawi/languages/sanskrit/`
- moved `lang/hindawi/upstream/chintamani/santali/` to `lang/hindawi/languages/santali/`
- moved `lang/hindawi/upstream/chintamani/saraiki/` to `lang/hindawi/languages/saraiki/`
- moved `lang/hindawi/upstream/chintamani/serbian/` to `lang/hindawi/languages/serbian/`
- moved `lang/hindawi/upstream/chintamani/shan/` to `lang/hindawi/languages/shan/`
- moved `lang/hindawi/upstream/chintamani/sindhi/` to `lang/hindawi/languages/sindhi/`
- moved `lang/hindawi/upstream/chintamani/sindhi_dev/` to `lang/hindawi/languages/sindhi_dev/`
- moved `lang/hindawi/upstream/chintamani/sinhala/` to `lang/hindawi/languages/sinhala/`
- moved `lang/hindawi/upstream/chintamani/sundanese/` to `lang/hindawi/languages/sundanese/`
- moved `lang/hindawi/upstream/chintamani/syriac/` to `lang/hindawi/languages/syriac/`
- moved `lang/hindawi/upstream/chintamani/tagalog/` to `lang/hindawi/languages/tagalog/`
- moved `lang/hindawi/upstream/chintamani/tamil/` to `lang/hindawi/languages/tamil/`
- moved `lang/hindawi/upstream/chintamani/telugu/` to `lang/hindawi/languages/telugu/`
- moved `lang/hindawi/upstream/chintamani/thai/` to `lang/hindawi/languages/thai/`
- moved `lang/hindawi/upstream/chintamani/tibetan/` to `lang/hindawi/languages/tibetan/`
- moved `lang/hindawi/upstream/chintamani/tulu/` to `lang/hindawi/languages/tulu/`
- moved `lang/hindawi/upstream/chintamani/ukrainian/` to `lang/hindawi/languages/ukrainian/`
- moved `lang/hindawi/upstream/chintamani/urdu/` to `lang/hindawi/languages/urdu/`
- moved `lang/hindawi/upstream/chintamani/uyghur/` to `lang/hindawi/languages/uyghur/`
- moved `lang/hindawi/upstream/chintamani/vietnamese/` to `lang/hindawi/languages/vietnamese/`
- `lang/hindawi/tests/comprehensive/test_all.py`: language folders read from `LANGS` (sha256 `e2c1565fb8db` to `60dbd42a595f`)
- `lang/hindawi/tests/suite/run_tests.py`: language folders read from `LANGS` (sha256 `b20154a81613` to `10191d29ae48`)
- `lang/hindawi/tools/to_upstream.py`: language folders read from `LANGS` (sha256 `32a767a9cd9e` to `06d1414acf96`)

**Verified.** Both Hindawi suites give the same counts as before the move (C8).

## C4. Committed flex output removed

**Why.** A `.c` file that flex generates from a transducer is a build product: it drifts from its `.uhin` the moment the `.uhin` changes.

- removed `lang/hindawi/languages/bengali/h2c.c` (sha256 `fb66636f2845eb89bc2cac7c58f2dda4f0bf7f1d1099fbd12f3b15014fba6580`), generated by flex from the `h2c.uhin` beside it

**Verified.** The cell's Makefile regenerates it.

## C5. Hard-coded /tmp tool locations made overridable

**Why.** Every cell's Makefile and driver, the multi-file driver and the suites named /tmp/flexroot and /tmp/chintamani, which exist only on the machine that generated them. The old locations remain the defaults; FLEX, FLIB, FLEX_PATH and ROMENAGRI now override them, and a flex on the PATH is preferred.

- `lang/hindawi/languages/arabic/Makefile` (sha256 `cf72336ef777` to `4844b1221b43`)
- `lang/hindawi/languages/aramaic/Makefile` (sha256 `69cf2bba1849` to `7a979fa7fba5`)
- `lang/hindawi/languages/assamese/Makefile` (sha256 `64f301f05447` to `88b79de80a3b`)
- `lang/hindawi/languages/awadhi/Makefile` (sha256 `99f4b730ec12` to `f585c6bc221a`)
- `lang/hindawi/languages/bengali/Makefile` (sha256 `8678c8c69750` to `4aa1dc4b9995`)
- `lang/hindawi/languages/bhojpuri/Makefile` (sha256 `bc1e080ac92d` to `b45c095c61fc`)
- `lang/hindawi/languages/gujarati/Makefile` (sha256 `09fdccd1ed81` to `681d1b538391`)
- `lang/hindawi/languages/hebrew/Makefile` (sha256 `52a57926328f` to `a96db737d252`)
- `lang/hindawi/languages/kannada/Makefile` (sha256 `9d9d6b6f885a` to `36855925fee5`)
- `lang/hindawi/languages/malayalam/Makefile` (sha256 `07bcbf4c053f` to `647d711e1579`)
- `lang/hindawi/languages/marathi/Makefile` (sha256 `111cdfff58dd` to `419aec904a8c`)
- `lang/hindawi/languages/nepali/Makefile` (sha256 `1b20d4d78626` to `cbf1433a7c7d`)
- `lang/hindawi/languages/odia/Makefile` (sha256 `0a37a18bb4cb` to `e443f901bf05`)
- `lang/hindawi/languages/pali/Makefile` (sha256 `a40f1e9c321b` to `e3952939caed`)
- `lang/hindawi/languages/persian/Makefile` (sha256 `3a92e53df090` to `3b9cf67dcfae`)
- `lang/hindawi/languages/phoenician/Makefile` (sha256 `68aadc1f2d71` to `dc7eeb1e5853`)
- `lang/hindawi/languages/prakrit/Makefile` (sha256 `0b4c491ebc48` to `4de9eef7b4be`)
- `lang/hindawi/languages/punjabi/Makefile` (sha256 `f75441fda4a7` to `64b35b8758e7`)
- `lang/hindawi/languages/sanskrit/Makefile` (sha256 `1b299e58c37e` to `1804ce61f18b`)
- `lang/hindawi/languages/syriac/Makefile` (sha256 `62c47f0268b8` to `b097f398584b`)
- `lang/hindawi/languages/tamil/Makefile` (sha256 `701679f9269c` to `4c45a0a6ea12`)
- `lang/hindawi/languages/telugu/Makefile` (sha256 `5b38ab558833` to `89fdc5c40071`)
- `lang/hindawi/languages/urdu/Makefile` (sha256 `88a1e21de7f6` to `d4bd090eafc8`)
- `lang/hindawi/languages/arabic/arabiccc` (sha256 `d11db5a0e79b` to `398da32a8f45`)
- `lang/hindawi/languages/aramaic/aramaiccc` (sha256 `cf31fe2a2821` to `d08396ed5049`)
- `lang/hindawi/languages/assamese/assamesecc` (sha256 `8c26104b4d21` to `a9402ccc26df`)
- `lang/hindawi/languages/awadhi/awadhicc` (sha256 `a5066f3f898d` to `479e73ccefc8`)
- `lang/hindawi/languages/bengali/bengalicc` (sha256 `5e3aa749d452` to `c2e1fd32fe91`)
- `lang/hindawi/languages/bhojpuri/bhojpuricc` (sha256 `235e801cfcfa` to `063ca2e5d57b`)
- `lang/hindawi/languages/gujarati/gujaraticc` (sha256 `8fa4bc6a04d2` to `13ccc0d2d22a`)
- `lang/hindawi/languages/hebrew/hebrewcc` (sha256 `c312267bf684` to `c8b64549e655`)
- `lang/hindawi/languages/kannada/kannadacc` (sha256 `364d2a343a69` to `c3823aee948f`)
- `lang/hindawi/languages/malayalam/malayalamcc` (sha256 `ecc699761e96` to `a1af9db4fd53`)
- `lang/hindawi/languages/marathi/marathicc` (sha256 `2d8cafa100bd` to `71e0e81f77f8`)
- `lang/hindawi/languages/nepali/nepalicc` (sha256 `5108a7c84a70` to `043f7aba2753`)
- `lang/hindawi/languages/odia/odiacc` (sha256 `311cea09d80c` to `69b0d388b439`)
- `lang/hindawi/languages/pali/palicc` (sha256 `7bfaab6b92e9` to `62c9cf5565eb`)
- `lang/hindawi/languages/persian/persiancc` (sha256 `a4ac22268053` to `bccce7e383f3`)
- `lang/hindawi/languages/phoenician/phoeniciancc` (sha256 `2126852fa630` to `0d413cc8702a`)
- `lang/hindawi/languages/prakrit/prakritcc` (sha256 `9f778ed15fcf` to `31ab6151f00d`)
- `lang/hindawi/languages/punjabi/punjabicc` (sha256 `72966c11ea27` to `971f7091df12`)
- `lang/hindawi/languages/sanskrit/sanskritcc` (sha256 `abb6e0797d53` to `4bd31e60e421`)
- `lang/hindawi/languages/syriac/syriaccc` (sha256 `6f88329b7569` to `97da03b1a36c`)
- `lang/hindawi/languages/tamil/tamilcc` (sha256 `366081dcc5b0` to `9240f4c4ecba`)
- `lang/hindawi/languages/telugu/telugucc` (sha256 `ec14bb90d255` to `810f481c0ed2`)
- `lang/hindawi/languages/urdu/urducc` (sha256 `90deb93c7c68` to `1f6380b975c7`)
- `lang/hindawi/hindawicc` (sha256 `485bc48bd512` to `6ac353bac0de`)
- `lang/hindawi/tests/suite/run_tests.py` (sha256 `10191d29ae48` to `e9ae3d0ffc99`)
- `lang/hindawi/tests/comprehensive/test_all.py` (sha256 `60dbd42a595f` to `ded960080519`)

**Verified.** Both suites and `scripts/test_all.sh` give the same results (C8).

## C6. Per-build reports moved from the root to docs/history/

**Why.** Sixteen reports of single builds crowded the root beside the README. They are history, not orientation. The documentation catalog is regenerated by the build's own `scripts/build_docs_catalog.py`, so its links follow the move.

- moved `AUDIT-0056.md` to `docs/history/AUDIT-0056.md`
- moved `AUDIT-0057.md` to `docs/history/AUDIT-0057.md`
- moved `AUDIT-0070.md` to `docs/history/AUDIT-0070.md`
- moved `AUDIT-0076.md` to `docs/history/AUDIT-0076.md`
- moved `AUDIT-0089.md` to `docs/history/AUDIT-0089.md`
- moved `AUDIT-0093.md` to `docs/history/AUDIT-0093.md`
- moved `AUDIT-QUESTIONS.md` to `docs/history/AUDIT-QUESTIONS.md`
- moved `BUILD-0051-FILTER-REPORT.md` to `docs/history/BUILD-0051-FILTER-REPORT.md`
- moved `CONVERSION-TEST-0068.md` to `docs/history/CONVERSION-TEST-0068.md`
- moved `KEYWORD-AUDIT.md` to `docs/history/KEYWORD-AUDIT.md`
- moved `PIPELINE-TEST-0061.md` to `docs/history/PIPELINE-TEST-0061.md`
- moved `TEST-0094.md` to `docs/history/TEST-0094.md`
- moved `UPSTREAM-AUDIT.md` to `docs/history/UPSTREAM-AUDIT.md`
- moved `HINDAWI-ARCHITECTURE-CORRECTION-TEST-REPORT.md` to `docs/history/HINDAWI-ARCHITECTURE-CORRECTION-TEST-REPORT.md`
- moved `ARCHITECTURE-RESTORED.md` to `docs/history/ARCHITECTURE-RESTORED.md`
- moved `GROK-HINDAWI-MULTILINGUAL-HANDOFF.md` to `docs/history/GROK-HINDAWI-MULTILINGUAL-HANDOFF.md`
- `docs/documentation-catalog.html` regenerated (sha256 `89361c1f1799` to `1fa8dc4d99af`)

**Verified.** `tests/test_static_pages.sh` passes.

## C7. Unreferenced Romenagri text dump removed

**Why.** A 2.9 MB concatenation of Romenagri's sources prepared for a language model. Nothing reads it, and Romenagri's source of record is hindawiai/chintamani.

- removed `tools/pushkalavati-compiler/vendor/romenagri/upstream/romenagri_llm_dump.txt` (2,927,972 bytes, sha256 `acc19cba9a4531a04c94922bb7df791760d8b00a38ad821c49958b4e78b35b8d`)

**Verified.** No file in the tree refers to it.

## C8. An end-to-end check of the pipeline, by execution

**Why.** The build's own suites test its Python and JavaScript tools; none runs a program through the original
Hindawi chain, and none checks that a language's keywords survive Romenagri. This check reports both. It never
gates: it prints status, because coverage is published as status.

- added `lang/hindawi/tests/e2e/check_pipeline.py` (sha256 `7aee7fc8c3f483945987f69a9c9e75c4d1f03f3eca7488105c85fe8ed95e207d`). It needs a built Romenagri and a
  Chintamani checkout (`ROMENAGRI`, `CHINTAMANI_HINDAWI`), flex, gcc and gawk; `--wave0` runs only Wave 0.

**Verified, 16 October 2026.**

- Wave 0: every Chintamani shaili builds with its own Makefile (guru, shraeni, yantra, kritrima, praatha,
  soochee, wyaaka, shabda, and hindrv). All eight Chintamani samples are transduced to their host source
  (.c, .cpp, .asm, .bas twice, .java, .lex, .yacc). The C, C++ and lex samples compile and run; the others need
  a host toolchain this machine lacks (fasm, a BASIC compiler, javac, yacc) and were not run.
- Script axis: of 11,483 native keywords across the 76 language folders, 3,746 survive
  `uni2acii | acii2cf` and back unchanged. The Devanagari-script languages pass (203 of 204 each); every
  other script fails (0 to 2 of 204), because the cells' Makefiles feed non-Devanagari text straight to
  `uni2acii`, which reads Devanagari only, without first passing it through a script filter.
- Guru cells: 2,108 of 2,512 declared Guru keywords are recognised by their own lexer, built the original way;
  Hindi, Sanskrit, Nepali, Awadhi and Bhojpuri 278 of 321 each, Bengali 12 of 34, Tamil 12 of 30, and 0 for
  Arabic, Persian, Urdu, Punjabi, Telugu, Malayalam and Odia.

## C9. Build number, and what the multi-file driver leaves behind

**Why.** This tree is BUILD-0103. `lang/hindawi/hindawicc` compiles the Guru transducer into the Chintamani copy
(`lang/hindawi/upstream/chintamani/guru/h2c`) and writes `<name>_deva.uhin` beside each source; neither may
ever be committed, and the first would make the Chintamani copy differ from Chintamani.

- `BUILD-NUMBER.txt`: BUILD-0102 to BUILD-0103 (sha256 `805397fc75ee` to `1cfc9ef6a155`)
- `.gitignore`: those two outputs ignored (sha256 `c83998c70246` to `ec1f72f584ce`)

**Verified.** `scripts/test_all.sh` passes on the tree at this commit (see the record below C9's commit).

## C10. Grok's ingestion tools, as delivered in HINDAWI2026_10-best

**Why.** HINDAWI2026_10-best is BUILD-0102 plus these four files and nothing else; HINDAWI2026_10-regression adds only the dictionary one ingestion run wrote. They are taken exactly as delivered, so C11 shows every change made to them.

- added `lang/hindawi/tools/ingest.py` (sha256 `853b88c200a241ee`)
- added `lang/hindawi/tools/import_project.py` (sha256 `845f22d1dd8f207a`)
- added `lang/hindawi/tools/identifier_map.py` (sha256 `89c9881ba0141b9e`)
- added `tests/regression.sh` (sha256 `ae1182e27b3dd8e7`)

**Verified.** Byte-identical to the files in HINDAWI2026_10-best.zip.

## C11. Ingestion, the multi-file driver and the fundamental regression, on the original chain

**Why.** hindawicc compiled with Hindi's transducer for every language, bypassed Romenagri, skipped the original driver's escape repairs and, when a source did not transduce, quietly compiled the raw source. ingest.py fed the lexers raw UTF-8 although they read Romenagri's encoding, translated identifiers inside string literals (so %d became %द) and could give two identifiers one native name. Both now run the chain Chintamani's own drivers run: fixuninum, iconv, uni2acii, acii2cf, acii2uni, iconv, h2c, and, for C to the language, Romenagri's encoding in before c2h. hindawicc passes every other argument to gcc, takes the language's cell from HINDAWI_CELL, and stops on any failure. ingest.py keeps one dictionary per ingestion (HINDAWI_DICT), one native name per identifier, touches only code, and reverses through each identifier's C-level Romenagri name, which is the name ABI. scripts/fetch.sh and scripts/build.sh fetch Chintamani at its pinned commit and build Romenagri and every shaili with their own Makefiles; tests/fundamental.py is the regression that must hold.

- changed `lang/hindawi/hindawicc` (sha256 `e201dbc6522923a3`)
- changed `lang/hindawi/tools/ingest.py` (sha256 `fbb5e9b28f49e598`)
- added `tests/fundamental.py` (sha256 `4f0bbdc1fc38ae49`)
- added `scripts/fetch.sh` (sha256 `8d49aabe76a174ba`)
- added `scripts/build.sh` (sha256 `081b60b412661b76`)
- changed `.gitignore` (sha256 `d77bfbcc63bc34ca`)

**Verified.** tests/fundamental.py: the Chintamani copy unchanged; Wave 0 eight of eight; guru, shraeni, kritrima, praatha, wyaaka and shabda stable to host and back (yantra recorded as Chintamani's own behaviour); a two-file project ingested with one dictionary, compiled by hindawicc with -DVALUE=40 -O2 -Wall -g into a program printing 42, and reversed to its original C; योगफल becomes the ELF symbol yoagaphala and returns through Romenagri. 12 passed, 0 failed.

## C12. The upstream checks, the cell harness, the two documents and the localisation page

**Why.** He asked for firmware, a Shakti-class bootstrap and the kernel to be brought in, pass or fail; for instructions on adding a human language, a script or a programming language without breaking the pipeline; for the sovereign stack; and for a web page where speakers localise the keywords. scripts/upstream/seabios.sh builds SeaBIOS as is and through a language's Guru pair and boots both under qemu-system-x86_64; scripts/upstream/riscv.sh runs a Hindi program on RV64IMAC under qemu-system-riscv64; scripts/upstream/linux.sh does the same for the Linux kernel's tinyconfig and is never part of the gate. lang/hindawi/tests/cells/cells.py measures every language cell by execution. docs/hindawi/localize.html reads docs/hindawi/data/keywords.json, generated from the language parameters without their romanised column. BUILD-NUMBER.txt names the release.

- added `scripts/upstream/seabios.sh` (sha256 `3213e222dcd8ad59`)
- added `scripts/upstream/riscv.sh` (sha256 `48c71961c3c77589`)
- added `scripts/upstream/linux.sh` (sha256 `690d60bc87587cfe`)
- added `lang/hindawi/tests/cells/cells.py` (sha256 `e1e89c24fcd5a516`)
- added `docs/hindawi/ADDING-LANGUAGES.md` (sha256 `ee58b12220b61994`)
- added `docs/hindawi/SOVEREIGN-STACK.md` (sha256 `b1e6cf8dcb8a7d81`)
- added `docs/hindawi/localize.html` (sha256 `b32a8bd06852e1e1`)
- added `docs/hindawi/data/keywords.json` (sha256 `af9182807ca2516d`)
- changed `docs/index.html` (sha256 `567ee2618ab7a18e`)
- changed `BUILD-NUMBER.txt` (sha256 `40417b9239623158`)

**Verified.** scripts/test_all.sh passes (ALL AVAILABLE TESTS PASSED); tests/fundamental.py 12 passed, 0 failed; scripts/upstream/riscv.sh PASS; scripts/upstream/seabios.sh: SeaBIOS rel-1.16.3 builds and boots as is, and fails to build through the Hindi pair because acii2cf doubles underscores in identifiers, recorded in docs/hindawi/ADDING-LANGUAGES.md.

## C13. The documentation index, regenerated by the build's own suite

**Why.** scripts/test_all.sh rebuilds the documentation catalogue and its mirror of every Markdown file under docs/; after C12 added docs/hindawi, both changed. They are generated, and committed because the Pages test reads them.

- changed `docs/documentation-catalog.html` (sha256 `8c991c1151699096`)
- added `docs/reference/repository/docs/hindawi/ADDING-LANGUAGES.md` (sha256 `ee58b12220b61994`)
- added `docs/reference/repository/docs/hindawi/SOVEREIGN-STACK.md` (sha256 `b1e6cf8dcb8a7d81`)

**Verified.** scripts/test_all.sh passes on the tree with them.

## C14. File names kept out of the ingestion dictionary (HINDAWI2026_10-ingest)

**Why.** Ingesting an upstream project put #include file names into the dictionary. Grok's fix in HINDAWI2026_10-ingest is merged into the original-chain ingest.py of C11 rather than replacing it: #include <file> names are skipped like string literals and comments, and preprocessor words and printf, scanf, malloc, free, NULL, true and false are reserved, as Grok's version reserves them. Grok's lang/hindawi/tools/ingest_dir.py is added as delivered.

- changed `lang/hindawi/tools/ingest.py` (sha256 `28e1cdfb2e05eeef`)
- added `lang/hindawi/tools/ingest_dir.py` (sha256 `aba4eea8d849941c`)

**Verified.** #include <sys/io_port.h> and #include "my_lib.h" give no dictionary entries; tests/fundamental.py 12 passed, 0 failed.

## C15. The fundamental regression made safe on any machine

**Why.** On his machine the seed's gate stopped with TypeError in tests/fundamental.py: Wave 0 returned no rows, and the check counted an empty list. Wave 0 now builds only the nine original Chintamani folders (not every folder with a Makefile), reads nothing from the terminal, and bounds every step, so a step that hangs or fails is reported, not a crash. When the checker cannot judge on a machine, fundamental.py says why and exits 3 (unjudged); when Wave 0 yields nothing, the failure shows the checker's own output.

- changed `tests/fundamental.py` (sha256 `8c09bbcd0e1b9b6f`)
- changed `lang/hindawi/tests/e2e/check_pipeline.py` (sha256 `b4bc7bd6058b4dd5`)

**Verified.** tests/fundamental.py 12 passed, 0 failed.

## C16. The compilation-path tools for ingested projects

**Why.** An earlier run, interrupted before it could commit, built the compilation path for whole projects on the regression-fixed drop's design: tools/hindawi_chain.py holds both paths in one place (ingestion: C to the language; compilation: the language to C through the script filter, Romenagri and the language's h2c, with ASCII names held aside so CONFIG_X and memcpy keep their identity); tools/ingest_project.py ingests a tree into several languages with one dictionary per language; tools/build_project.py builds a native tree with its own Makefile and CC=hindawicc; hindawicc maps every -D and -U name through the dictionary to its C-level form; tools/ingest.py uses the shared chain.

- changed `lang/hindawi/hindawicc` (sha256 `d2ced1a1bae5dee8`)
- added `lang/hindawi/tools/hindawi_chain.py` (sha256 `34e6ede10a35ea22`)
- added `lang/hindawi/tools/ingest_project.py` (sha256 `f1f8c0bf4f202ea9`)
- added `lang/hindawi/tools/build_project.py` (sha256 `918ac57787fb7e9d`)
- changed `lang/hindawi/tools/ingest.py` (sha256 `ef51de309782ac10`)

**Verified.** tests/fundamental.py 12 passed, 0 failed; scripts/test_all.sh passes.

## C17. BURP, the Bidirectional Universal Resource Parser

**Why.** His ingestion pipeline, named by him: any project, in every paradigm by file type, into any number of languages at once and back exactly. Keywords come from each language's own reverse transducers (Chintamani's for Hindi), applied per token outside literals, comments and #include names; identifiers and comments go through a dictionary built during ingestion by pluggable translators (glossary, Argos, any command); externals found by the preprocessor stay; -D and -U names in build files follow the dictionary; files are renamed only on request; Brahmi-script languages can be rendered in the other Brahmi scripts. Its dictionary sits where build_project.py and hindawicc read it. transliterate.py finds its tables inside the repository, and, where a table is only a header, projects by Unicode name as the tables' headers say. docs/hindawi/BURP.md, DEVIATIONS.md (every deviation from legacy Hindawi, changing nothing), TRANSLATION-TOOLS.md and docs/TERMINOLOGY.md, the terminology book, begin here.

- added `lang/hindawi/burp/burp.py` (sha256 `fc6d7d5f019079b6`)
- changed `lang/hindawi/pipeline/transliterate.py` (sha256 `ea92d310f6442b49`)
- added `tests/burp/sample/Makefile` (sha256 `1a67f16ec278b92e`)
- added `tests/burp/sample/src/main.c` (sha256 `7106a1b3fcc15629`)
- added `docs/hindawi/BURP.md` (sha256 `89f0033391a6e148`)
- added `docs/hindawi/DEVIATIONS.md` (sha256 `d1f69de3dc560ba3`)
- added `docs/hindawi/TRANSLATION-TOOLS.md` (sha256 `c3cdb10665bbecc5`)
- added `docs/hindawi/burp-status.tsv` (sha256 `7bb2cd610a2d0bdc`)
- added `docs/TERMINOLOGY.md` (sha256 `0efc9ef8cb44c8e8`)

**Verified.** burp.py check over the sample project: 355 ingestions (76 languages and 279 renderings) reverse byte for byte; the sample built through hindawicc prints 42 in 30 of 76 languages (docs/hindawi/burp-status.tsv); scripts/test_all.sh passes; tests/fundamental.py 12 passed.

## C18. The sovereign-stack test, VHDL in BURP, the IDE working mechanism, and the strategy note

**Why.** He asked for a script to run on his own machine that takes the open-source stack layer by layer, from a processor in VHDL through firmware, kernel, C library, binutils and the compiler to libraries, ingests each into every language, measures how much becomes localised (target 100%), reverses it, builds it, and tests TinyCC rebuilding itself (the T-diagram); for a basic VHDL keyword list; for a lightweight, locally installable IDE where each person works in their own language through the dictionary, with highlighting and debugging; for a comparison with tree-sitter from a market-strategy view; and for the deviations to be noted against the true baseline. scripts/sovereign/stack.sh and measure.py do the first and are not run here; BURP gains a VHDL paradigm (IEEE 1076-2008 reserved words, kept untranslated until a language has vhdl2h tables); ide/burp_ide.py gives views per language with saves back to the canonical tree and Geany filetypes, and ide/burp_gdb.py native names in gdb; DEVIATIONS.md now says its baseline is Chintamani, a Telugu-era iteration, not the 2004 Hindawi.

- changed `lang/hindawi/burp/burp.py` (sha256 `032bb5ca45a675dd`)
- added `lang/hindawi/burp/paradigms/vhdl_keywords.txt` (sha256 `67c13b9808f4060c`)
- added `scripts/sovereign/stack.sh` (sha256 `4d1291c4d83a8db7`)
- added `scripts/sovereign/measure.py` (sha256 `1b67789e122b16ec`)
- added `ide/burp_ide.py` (sha256 `6b73da74101312df`)
- added `ide/burp_gdb.py` (sha256 `fec5f03ba7413fb4`)
- added `docs/hindawi/IDE.md` (sha256 `a5ab0e9c4fa51f06`)
- added `docs/hindawi/TREE-SITTER-AND-STRATEGY.md` (sha256 `94108d6e207b2aa7`)
- changed `docs/hindawi/DEVIATIONS.md` (sha256 `ec2d119b5fa3c46a`)

**Verified.** A VHDL file ingests into Hindi and reverses byte for byte. A Tamil view's edit reaches the canonical tree and the Gujarati view. measure.py on the sample: keywords localised 65.9% Hindi, 70.7% Urdu, 70.7% Punjabi (Gurmukhi), 58.5% Punjabi (Shahmukhi); identifiers 18.2% and comments 0% with only the glossary as translator. stack.sh not run, as asked.

## C19. Ingestion completed further, the whole stack list, real IDE integrations, the contribution page, and a Hindawi README

**Why.** He asked that the ingestion pipeline be completed first, since application work needs no transliteration; that the sovereign-stack test cover his whole list, generic across architectures, one stage at a time, with the GATE programming domains; configuration for existing IDEs rather than a home-made one, the Arduino IDE first so students program their boards in their own language, with a professional IDE besides; a page where speakers contribute to each language's standard through issues; and a README about Hindawi, not the Sūtram tree it inherited. BURP now takes Hindi's assembly and Java keywords from the pinned Chintamani, matches BASIC and VHDL keywords in any case with the original spelling kept for the reverse, and can use a local language model (any OpenAI-compatible endpoint) to translate names and comments. stack.sh now runs 53 projects in 15 stages plus the GATE domains from Rosetta Code, checks the reversed RTL with GHDL, Yosys and Verilator where installed, and reads the self-hosting table from its report. ide/arduino hooks every installed Arduino core's build; ide/eclipse holds External Tools launches and ide/gdbinit native names in gdb.

- added `.github/ISSUE_TEMPLATE/keyword.yml` (sha256 `5572ceab27b78746`)
- added `.github/ISSUE_TEMPLATE/config.yml` (sha256 `13064e7bea658e01`)
- changed `README.md` (sha256 `d89ae1ebd2dc86b4`)
- added `docs/history/README-BUILD-0102.md` (sha256 `7f3ed52e986a2df3`)
- added `docs/hindawi/contribute.html` (sha256 `8bfbb0a96f031d6c`)
- changed `docs/hindawi/IDE.md` (sha256 `5bf9c5caf3355fd2`)
- added `ide/arduino/install.sh` (sha256 `e9a4b630c59c812b`)
- added `ide/arduino/transduce.sh` (sha256 `98b603f612902490`)
- added `ide/gdbinit` (sha256 `0f952630ced6d2cf`)
- added `ide/eclipse/Hindawi_make.launch` (sha256 `8f9cc974a5280a4b`)
- changed `lang/hindawi/burp/burp.py` (sha256 `adb4f29be1fddfa0`)
- changed `scripts/sovereign/stack.sh` (sha256 `c3177beb3a125f9a`)
- added `ide/eclipse/Hindawi_view.launch` (sha256 `c813c66087dbc972`)
- added `ide/eclipse/Hindawi_save.launch` (sha256 `6b2fc52931f48e25`)

**Verified.** All 355 ingestions of the sample still reverse byte for byte; Hindi keywords localised rise from 65.9% to 82.9%. A Hindi blink sketch passed through the Arduino hook becomes C++ that compiles (देरी becomes _daeeree). scripts/test_all.sh passes. stack.sh is not run here.

## C20. The compilation path on the original pipeline, every cell completed from its lexicon, review templates per paradigm, and the linguistics lab

**Why.** He asked for the compilation path to go back to the original pipeline rather than move acii2uni; for the
languages' transducers to be complete, since the delivered cells carried the same 28 rules in all eighteen files of
every language while each language's lexicon holds a word for about 204 constructs; for review templates through which
each language's community reviews its standard paradigm by paradigm, from hardware description to IoT, robotics and AI,
as the Aṣṭādhyāyī's sūtras are reviewed in tajziya; and for the Dockerised linguistics lab for collaborators.

- **Pipeline.** `lang/hindawi/tools/script_filters.py` (Chintamani's own fltr_te_hi and fltr_ur_hi; generated filters of
  the same flex form for the other Brahmi scripts; each lexer keyword filtered in both contexts); `hindawi_chain.py` no
  longer calls `pipeline/transliterate.py`.
- **Cells.** `lang/hindawi/tools/complete_cells.py` regenerates all 75 cells (Hindi stays Chintamani's): eighteen
  transducers each in Chintamani's form, from the language's lexicon, keywords never replaced inside longer names,
  directives distinct from words (#if, if), multi-word keywords joined with underscores, invalid words rejected and
  listed; a Makefile and driver on the original pipeline; `STATUS.tsv` listing every construct without a word.
- **Review.** `docs/hindawi/review.html` over `docs/hindawi/data/standards.json`: per language and paradigm (the nine
  shailis; hardware, IoT and Arduino, robotics, AI), every construct, its word and source, and a prefilled issue; the
  issue form gains a paradigm field.
- **Lab.** `lab/Dockerfile`, `lab/docker-compose.yml`, `lab/README.md`: JupyterLab, the review pages, Praat, Argos
  Translate, and Hindawi built inside.
- **BURP.** Words carry zero-width joiners and the Limbu and Hangul ranges; a name spelled like a keyword is recorded
  so the reverse stays exact.
- **Status.** `tests/burp/compile_status.py` and its output `docs/hindawi/burp-status.tsv`.

**Verified.** All 355 ingestions of the sample (76 languages and their Brahmi renderings) reverse byte for byte.
Keywords localised on the sample: 82.9% for Urdu, Sindhi, Punjabi in both scripts, Arabic, Persian, Bengali and Tamil
(Urdu was 70.7%, Sindhi and Shahmukhi 58.5%). The sample builds and runs through the original pipeline in 47 of 76
languages, among them Urdu, Sindhi, Punjabi (Gurmukhi and Shahmukhi), Arabic, Persian, Pashto, Dari, Kashmiri, Bengali,
Tamil, Telugu, Gujarati, Odia and Kannada; 5 do not compile and 24 have no script filter yet. tests/fundamental.py 12
passed; scripts/test_all.sh passes.

## C21. Sanskrit made complete, and the GATE programs in every language

**Why.** He asked for a complete Sanskrit version and for the sample programs that teach every programming domain GATE covers. The Sanskrit lexicon held genuine Sanskrit words for most constructs, but its cell had carried Hindi's transducer; lang/hindawi/lexicons/sanskrit.tsv adds proposed Sanskrit words, unreviewed, for every construct the lexicon lacks across C, C++, Java, Python, BASIC, LOGO, yacc and lex, assembly, VHDL, Arduino, robotics and AI, and the C library calls the programs use, and drops the Hindi words copied into the cell; lang/hindawi/burp/glossary/sanskrit.tsv names the identifiers the programs use. samples/gate holds 43 C programs across algorithms (sorting, searching, greedy, dynamic programming, graphs, divide and conquer, backtracking), data structures, programming, discrete mathematics, theory of computation, compiler design, operating systems, networks, digital logic and databases, plus Python, Java, C++ and BASIC programs; tests/gate/run.py ingests them into any language, compiles each C program from that language through the original pipeline and compares its output with the English one. BURP now reads numeric literals as single tokens, leaves untranslated names exactly as they were, and reads back a native keyword written as several words, as Chintamani's BASIC THEN is. The Sanskrit set is on the site beside the English one.

- added `samples/gate/algorithms/sorting/quick_sort.c` (sha256 `9d91d2b16ad5d7de`)
- added `lang/hindawi/lexicons/sanskrit.tsv` (sha256 `ab7d559398072c78`)
- added `lang/hindawi/burp/glossary/sanskrit.tsv` (sha256 `53d52af85d127866`)
- changed `lang/hindawi/burp/burp.py` (sha256 `eda23b4c35eb31de`)
- changed `lang/hindawi/tools/complete_cells.py` (sha256 `e29d738602a48fc8`)
- added `tests/gate/run.py` (sha256 `cab9f76434054d5b`)
- added `docs/hindawi/samples/index.html` (sha256 `0f5d40e5b3646a71`)
- changed `README.md` (sha256 `94e420450aabc689`)

**Verified.** Sanskrit: 43 of 43 C programs compile from Sanskrit and print exactly what the English originals print; all 47 files reverse byte for byte. The same holds in Hindi, Urdu, Sindhi, Punjabi in Shahmukhi and Gurmukhi, Bengali, Tamil, Telugu, Arabic, Persian, Marathi, Nepali, Gujarati, Odia and Kannada. All 355 ingestions of the BURP sample still reverse byte for byte; scripts/test_all.sh passes.

## C22. Nine languages completed, one standard tool, the GATE syllabus mapped, and native names exact on the compilation path

**Why.** He asked for Dari, Pashto, Urdu, Punjabi in Gurmukhi and in Shahmukhi, Sindhi, Telugu and Kannada to be completed and verified (Sanskrit with them); for the tools scattered across the tree to become one standard tool with an installer and documentation he can verify by hand; and for the GATE syllabus to be read and mapped, with instructions another AI can follow. Words: lang/hindawi/lexicons/multi.tsv (77 host keywords and library calls) and lang/hindawi/burp/glossary/multi.tsv (202 names), one column per language, all proposed and unreviewed; the cell generator and BURP read them, the language's own files winning; every paradigm's token set now carries its host keywords; lang/hindawi/tools/coverage.py measures a language. Compiling translated names at scale exposed five faults, each fixed and recorded in DEVIATIONS.md: each native word is now transliterated on its own (the Urdu filter read a word-initial letter by its neighbour); Pashto and Sindhi letters the Urdu filter lacks are folded to Urdu letters; Romenagri's mid-word ^ is written _ in C-level names; the cells use the standard literal rules instead of Chintamani's greedy one; Gurmukhi signs named differently from Devanagari are mapped. Compiled lexers are rebuilt whenever their cell changes. BURP reads line-numbered BASIC REM lines as comments, and keeps a C++ header's names in English only in C++ files. Seventeen GATE programs added (60 in C); docs/hindawi/GATE-PROGRAMS.md maps the 2027 CS syllabus in our own words, with the program contract and instructions for another AI. The tool: bin/hindawi, install.sh, docs/man/hindawi.1, VERSION 2026.10.4, docs/hindawi/MANUAL.md, VERIFY.md; hindawicc works through a symlink; nine superseded tools retired to attic/ with what replaces each, the fundamental regression's project check moved onto BURP.

- added `bin/hindawi` (sha256 `faa75fde047562f8`)
- added `install.sh` (sha256 `879d0356fa226aa9`)
- added `VERSION` (sha256 `8a168414a72a4872`)
- added `docs/man/hindawi.1` (sha256 `4cf3d6dda1d8a55b`)
- added `docs/hindawi/MANUAL.md` (sha256 `6313c1e2d2a0bc02`)
- added `VERIFY.md` (sha256 `496df4349c1479df`)
- added `docs/hindawi/GATE-PROGRAMS.md` (sha256 `1765a05b7c2e09c2`)
- added `lang/hindawi/lexicons/multi.tsv` (sha256 `74c536e7e2c7523c`)
- added `lang/hindawi/burp/glossary/multi.tsv` (sha256 `f57dba5875c90508`)
- added `lang/hindawi/tools/coverage.py` (sha256 `ccbba2a297c7aa8e`)
- changed `lang/hindawi/tools/complete_cells.py` (sha256 `6773e2b865c45125`)
- changed `lang/hindawi/tools/hindawi_chain.py` (sha256 `198ae27cf61705bc`)
- changed `lang/hindawi/tools/script_filters.py` (sha256 `200d862075f617c3`)
- changed `lang/hindawi/burp/burp.py` (sha256 `1459e4b6878b8b2e`)
- changed `lang/hindawi/hindawicc` (sha256 `155427da03b7ba30`)
- changed `tests/gate/run.py` (sha256 `8af213c0948ffb95`)
- changed `tests/fundamental.py` (sha256 `6b8cd9ddbdfcd8c8`)
- added `attic/README.md` (sha256 `5535f8a27774a9e9`)
- changed `docs/hindawi/DEVIATIONS.md` (sha256 `3ec51569fe6eae77`)
- changed `README.md` (sha256 `94ea8f757af70d4f`)

**Verified.** All nine languages: keywords C 35/35, C++ 61/61, Java 51/51, Python 36/36, BASIC 21/21, LOGO 14/14; every name of the GATE programs in the language (199/199, Sanskrit 198/198); no library call left in English. In each, 60 of 60 C programs compile from the language through the original pipeline and print exactly what the English originals print, and 64 of 64 files reverse byte for byte. All 355 ingestions of the BURP sample reverse byte for byte; tests/fundamental.py 12 passed; scripts/test_all.sh passes; 47 of 76 languages build and run the sample, as before. install.sh installed into a scratch prefix and compiled quick sort from Urdu and Telugu; hindawi verify passed every step.

## C23. Every GATE topic written, each language's standard, work packages, notebooks, and the faults the new names exposed

**Why.** He asked to complete the languages and much more: programs for the whole GATE syllabus, a standard for each language that its community can review, the remaining work written out as packages students and AIs can take, and notebooks to teach with. This records that work, done over two turns (the first turn's report never reached him), and its verification. GATE: 53 programs added, 113 in C; every topic of the 2027 CS map in docs/hindawi/GATE-PROGRAMS.md now has one; tests/gate/run.py links -lpthread, takes --only, and records a program that hangs as a failure. Words: 136 names added to lang/hindawi/burp/glossary/multi.tsv and the preprocessor directives to lang/hindawi/lexicons/multi.tsv for the nine languages; coverage.py measures the preprocessor too. Standards: lang/hindawi/tools/standards.py, standards_docx.js and standard_import.py write standards/<language>/standard.md, standard.json and standard.docx for all 76 languages, in the structure standards bodies use, citing host standards by reference only and recording where each word came from; hindawi standard generates them and imports a filled work package. Work packages: lang/hindawi/tools/work_packages.py writes work-packages/ (67 language packages, 12 JavaScript packages; no GATE topic left open) and docs/hindawi/work-packages.html, where each is claimed as an issue; hindawi wp lists them. Notebooks: lang/hindawi/tools/notebooks.py and lang/hindawi/colab.py make seven Colab notebooks in each of eleven languages, from notebooks/ and docs/hindawi/notebooks.html; hindawi notebooks. Faults fixed and recorded in DEVIATIONS.md: the Dravidian scripts' short and long e and o kept apart in the generated filters; one word for one construct in each cell; licence and copyright notices never translated; BURP reads and writes files byte for byte, line endings included; directive forms keep their #; the flex runtime found as libfl, libl or none; hindawicc follows symlinks without readlink -f; the Arduino installer finds cores on macOS and under WSL.

- added `samples/gate/discrete_mathematics/truth_table.c` (sha256 `5c82e45a2c184f3a`)
- changed `lang/hindawi/burp/glossary/multi.tsv` (sha256 `5bdd0ba85ab1fe95`)
- changed `lang/hindawi/lexicons/multi.tsv` (sha256 `b5d4df9508d44265`)
- added `lang/hindawi/tools/standards.py` (sha256 `35a09b6b0f00253a`)
- added `lang/hindawi/tools/standards_docx.js` (sha256 `ab573bd0df0d8752`)
- added `lang/hindawi/tools/standard_import.py` (sha256 `4d9d7ce769cf338d`)
- added `lang/hindawi/tools/work_packages.py` (sha256 `ad6a0dac5c2dae74`)
- added `lang/hindawi/tools/notebooks.py` (sha256 `6add5fb04add9210`)
- added `lang/hindawi/colab.py` (sha256 `69bb52b15686adf7`)
- added `docs/hindawi/work-packages.html` (sha256 `c986cacc06c32e5b`)
- added `docs/hindawi/notebooks.html` (sha256 `cc7c87b5bcc79e48`)
- added `standards/urdu/standard.docx` (sha256 `b99616710026aa28`)
- added `notebooks/urdu/00_start_here.ipynb` (sha256 `e702fb0a66037d85`)
- changed `tests/gate/run.py` (sha256 `c69b0207a78a4ae2`)
- changed `bin/hindawi` (sha256 `0665fb46416e2036`)
- changed `lang/hindawi/burp/burp.py` (sha256 `9a605bff762a4009`)
- changed `lang/hindawi/tools/script_filters.py` (sha256 `982aa8ed49b9c0c7`)
- changed `lang/hindawi/tools/complete_cells.py` (sha256 `f0b74f7a9e18a111`)
- changed `lang/hindawi/tools/hindawi_chain.py` (sha256 `ff5522c0dbcce2be`)
- changed `lang/hindawi/hindawicc` (sha256 `daa692b799c38f09`)
- changed `docs/hindawi/DEVIATIONS.md` (sha256 `d2ebb75543fe3dd4`)
- changed `docs/hindawi/MANUAL.md` (sha256 `21c3b6614bb03a77`)
- changed `docs/hindawi/GATE-PROGRAMS.md` (sha256 `7a798c476f8bafc3`)

**Verified.** All nine languages: keywords complete in C, C++, Java, Python, BASIC, LOGO and the C preprocessor; 354 of 354 names of the GATE programs in the language; no library call left in English. In each, 113 of 113 C programs compile from the language through the original pipeline and print exactly what the English originals print, and 117 of 117 files reverse byte for byte. All 355 ingestions of the BURP sample reverse byte for byte; tests/fundamental.py 12 passed; scripts/test_all.sh passes; 47 of 76 languages build and run the sample, as before. 76 standards written as Word files that open cleanly; 77 notebooks; 79 open work packages.

## C24. Trademarks asserted, standards drafted for LITD 15, every task registered, and the compilation path shown stage by stage

**Why.** He ruled that code keeps its GPL and MIT licences and that every trademark be asserted, the triad's registered marks first; found the standards to be stubs and asked for drafts a standards body can take; asked that every open task be captured, completed or packaged without losing his credits; and asked for the notebooks to show the whole compilation flow. legal/TRADEMARKS.md asserts AyeAI, AyeCNSe and AyeAM as registered in India and the claimed marks, separates them from code licences, and keeps the originator's credit; CREDITS.md records contributors under the originator. lang/hindawi/tools/standards.py now writes Indian Standard drafts for LITD 15 of BIS (foreword, scope, normative references, terms, conformance, source text with the script's native digits from the Unicode database, lexical structure in ISO/IEC 14977 EBNF, lowering, name transformation, normative keyword annex, test vectors computed by the reference implementation, script filter, dated conformance record, worked example), only for languages whose keyword bindings are complete; the stubs for the other 67 are removed and each has a work package. The review and contribution pages read one source with Hindi included and host keywords first; the old localisation data is retired. work-packages/tasks.json registers every point of his requests (7 covenants, done items with evidence, open items); each open item is a work package carrying the originator's credit, listed in TASKS.md and on the work-packages page with a share link. hindawi_chain.stages() shows source, script filter, Romenagri form and host text, and to_c is its last stage; Python now runs through each language's own h2py built through Romenagri, as Chintamani's Makefile builds it; every generated forward transducer passes whole words, so a keyword is never matched inside a longer name. docs/hindawi/PANIR.md records the ChatGPT and Gemini intermediate representation as a proposal with seven defects found in it; docs/hindawi/TOOLS-PROPOSED.md lists fourteen proposed tools.

- added `legal/TRADEMARKS.md` (sha256 `232415001153c4e3`)
- added `CREDITS.md` (sha256 `41be0f0c579f3c0a`)
- added `TASKS.md` (sha256 `1f83df82d9f3797a`)
- added `work-packages/tasks.json` (sha256 `ae5f14a29b20f83d`)
- changed `lang/hindawi/tools/standards.py` (sha256 `d0edbe4c0f71411e`)
- changed `lang/hindawi/tools/standards_docx.js` (sha256 `ded628012a4e4bf0`)
- changed `lang/hindawi/tools/work_packages.py` (sha256 `f5d82598037c43d2`)
- changed `lang/hindawi/tools/hindawi_chain.py` (sha256 `908fccbf8da28805`)
- changed `lang/hindawi/tools/complete_cells.py` (sha256 `e506d20cc0e656d1`)
- changed `tests/gate/run.py` (sha256 `55140554d631d827`)
- added `tests/check_standards_register.py` (sha256 `40ab50fcf0fc2f95`)
- added `docs/hindawi/PANIR.md` (sha256 `1583a889b606b9a9`)
- added `docs/hindawi/TOOLS-PROPOSED.md` (sha256 `9871cc7389a9f2fc`)
- changed `docs/hindawi/review.html` (sha256 `ab8cad48b17a8bf9`)
- changed `docs/hindawi/contribute.html` (sha256 `673ab9ed6fe7dbd9`)
- changed `docs/hindawi/work-packages.html` (sha256 `07b171dd266fad75`)
- changed `standards/urdu/standard.docx` (sha256 `0183a066d62e3979`)
- changed `README.md` (sha256 `f8b7e836ce86e2b6`)
- changed `docs/hindawi/DEVIATIONS.md` (sha256 `6c1c92fb2e542b62`)

**Verified.** Nine languages (Dari, Pashto, Urdu, Punjabi in Gurmukhi and Shahmukhi, Sindhi, Telugu, Kannada, Sanskrit): 113 of 113 C programs and the Python program compile or run from the language and print what the English originals print; 117 of 117 files reverse byte for byte. Hindi: 111 of 113, the two failures caused by Chintamani's greedy character-literal rule (task T-10). Nine draft standards written as Markdown, JSON and Word, each Word file opening cleanly; tests/check_standards_register.py 149 passed; tests/fundamental.py 12 passed; scripts/test_all.sh passes. The trademark kit was dry-run against three live repositories, staging only legal/TRADEMARKS.md and README.md in each.

## C25. Originals restored and guarded, the lexicon's shifted code points corrected, Parashakti, robot coding, practice notebooks, and the test harness

**Why.** The 2026.10.5 push re-normalised the line endings of ten of the original Hindawi transducer files (carried from hindawiai/chintamani, the Telugu version of Hindawi) and three BUILD-0102 and source-stage files, and C24 had committed seven build outputs into that copy. The originals are now excluded from every line-ending rule (.gitattributes), recorded by hash (ORIGINALS.sha256) and checked first in the test suite (tests/check_originals.sh); the build outputs are removed and Hindi's transducers build in a cache copy, never in place. 177 lexicon words in Tamil, Bengali, Assamese, Manipuri and Punjabi had been made by shifting Devanagari code points into those scripts and held code points Unicode never assigned (the Tamil xv6 failure); each is rewritten as the script writes that sound, the compilation path names any such word instead of emitting stray bytes, and the data is tested. hindawicc takes the compiler underneath from HINDAWI_GCC, for cross builds; build_project.py no longer rewrites path pieces in linker scripts. scripts/parashakti.sh ingests, lowers, cross-compiles and runs the sovereign stack on QEMU (SHAKTI C-class bare metal, xv6 on RISC-V, SeaBIOS, TinyCC), writing the evidence into its report. robot_coding/ holds the Stage 1 (Arduino UNO, L293D, USB) and Stage 3 (ESP32, L298N, WiFi) sketches for the AyeAM control interface's commands, in English and six languages, with a guide. notebooks/practice/ holds a notebook per language in the design of the Hindawi NB UI: every GATE program selectable, C and Python, Build, Run, Stages, To C, From English, New, Upload, Download, and a place per GATE section to teach it in the mother tongue. hindawi test is the local harness (TESTING.md). Terminology corrected: the transducers and toolchain are the original Hindawi ones; Chintamani is the Telugu version that carries them.

- changed `.gitattributes` (sha256 `400670b7d67f7ced`)
- added `ORIGINALS.sha256` (sha256 `bb2bdb521758a958`)
- added `tests/check_originals.sh` (sha256 `7d7b4373058e4f98`)
- changed `lang/hindawi/pipeline/language_params.json` (sha256 `03236948f864ca62`)
- changed `lang/hindawi/tools/hindawi_chain.py` (sha256 `1e4fffd9b0989a5c`)
- changed `lang/hindawi/hindawicc` (sha256 `d3733a9c5f3cc495`)
- changed `lang/hindawi/tools/build_project.py` (sha256 `cc64bcac0e31f364`)
- added `scripts/parashakti.sh` (sha256 `f8d26c6e9578012d`)
- added `scripts/seed_notebooks.sh` (sha256 `d6402361a25eb900`)
- added `robot_coding/README.md` (sha256 `81eb9d89a7d9bc7f`)
- added `notebooks/practice/hindawi_urdu.ipynb` (sha256 `d31e9dd2d4b36534`)
- changed `bin/hindawi` (sha256 `3b40577716866980`)
- added `TESTING.md` (sha256 `58cec2a13911c33f`)
- changed `work-packages/tasks.json` (sha256 `65d5bc4c9f05add2`)
- changed `legal/TRADEMARKS.md` (sha256 `dbcf83a16bc4063b`)

**Verified.** test_all passes with the originals check first; tests/fundamental.py 12 passed; GATE: Urdu and Tamil 113 of 113 C programs and the Python program, 117 of 117 files reversed. Parashakti run here: bare metal in Urdu, Tamil and Hindi printed its result on QEMU's SHAKTI C-class machine; xv6 in Urdu, Tamil, Bengali and Punjabi booted on QEMU's RISC-V machine and its shell ran echo and ls; SeaBIOS and TinyCC stages not run here. The practice notebooks were driven headless in Urdu and Hindi: Build, Run, To C, From English and the Python path each gave the expected result. The robot sketches pass a C++ syntax check against stand-in Arduino headers, also after lowering from Urdu, Tamil and Hindi; they have not been compiled against the real cores or run on a robot.

## C26. The foundation, parametric Parashakti, the explainer site with the posters, and gates only on what a release needs

**Why.** He found the per-language fixes to be structures built without foundations, asked for Parashakti to cover MINIX, Linux, GCC, LLVM and WebAssembly and to be parametric, asked for an explainer site for every script with his posters on the description pages, and ruled that an unverified claim gets a disclaimer, that the intention is his, and that gates guard only what a release needs. The foundation: one normalisation (NFC, then whole-script rules: Arabic tatweel, Malayalam chillus, Assamese ra and wa) applied identically to the cells' rules and the compiled words (script_filters.normalize); one function gives every native word its C-level form (hindawi_chain.forms); lower_many lowers a whole tree with one transliteration and one transducer run per 32 MB, giving file for file what each file gives alone; foundation.py checks every script's characters and every language's words and computes readiness, and records keyword bindings that do not come back through the language's own transducer, which BURP then keeps in host form (lang/hindawi/data/roundtrip.json). Parashakti (scripts/parashakti.sh) is a manifest of projects, each fetched, configured, ingested, lowered as a whole tree with build_project.py --lower-only, built with its own tools, run and checked, languages chosen by readiness, the report giving each run its AyeKnow state. docs/trace/ is the explainer site: one character of any script followed from human language to the physical signal and back, representation versus encoding, the hexdump and mojibake, Qwan-tum quantisation, a 7-bit segment lab with its round trip, Romenagri forms and a program's stages computed by the real pipeline, every layer's evidence state, and the five posters with each claim's evidence state. The originals check and the standards and register audit now report without refusing a release; update_contract.sh adds the two rulings to the master contract.

- added `lang/hindawi/tools/foundation.py` (sha256 `2cec080ae3dead3e`)
- changed `lang/hindawi/tools/hindawi_chain.py` (sha256 `ce0c44df27d4b20c`)
- changed `lang/hindawi/tools/script_filters.py` (sha256 `243b1655017e8ec0`)
- changed `lang/hindawi/tools/build_project.py` (sha256 `a8f8a691d440515d`)
- changed `lang/hindawi/burp/burp.py` (sha256 `8d22a9971544cc2e`)
- added `lang/hindawi/data/roundtrip.json` (sha256 `d84abe4121aad842`)
- changed `scripts/parashakti.sh` (sha256 `c1f320453ef57212`)
- added `docs/trace/index.html` (sha256 `40ea6dc3c1262976`)
- added `lang/hindawi/tools/trace_site.py` (sha256 `ca9dd16d0be13bf0`)
- changed `tests/check_originals.sh` (sha256 `f4f88f7b6cca28ea`)
- changed `scripts/test_all.sh` (sha256 `dc3221bca592602f`)
- changed `README.md` (sha256 `b969fb839b87599b`)
- changed `work-packages/tasks.json` (sha256 `c4592fea187fca57`)

**Verified.** test_all passes (162 audit checks, the audit now reporting only); fundamental 12 passed; originals 96 of 96 byte for byte. lower_many against file by file on xv6: 65 of 65 files identical in Urdu, Tamil and Hindi, Urdu 0.1 s against 5.8 s. Foundation: 48 of 76 languages ready to compile, 8 complete, 113 bindings in 6 languages kept in host form by the round trip. Parashakti here: SHAKTI bare metal and xv6 verified in Urdu, Tamil and Hindi; Hebrew skipped by readiness; wasm3 changed to its own Fibonacci module, not yet rerun; MINIX, Linux, GCC, LLVM, SeaBIOS and TinyCC in the manifest, not run. The site was driven headless with its real data: no script errors, the 7-bit round trip verified in Devanagari, Arabic and Hangul, the trace complete.

## C27. AyeCode reused in the explainer site, the products defined, and phones linked to the practice notebooks

**Why.** He named where AyeCode lives (ayehandsum) and asked for focus on productization. The explainer site now writes the typed text in any AyeCode alphabet (NATO words, Egyptian and Anatolian hieroglyphs, Sa Re Ga notes, emoji, poem connectives), read back with its round trip checked; the alphabets are taken exactly from ayehandsum/ayehandsum at commit f338cba with its copyright. PRODUCTS.md defines six products (Practice on phones, the CLI, the robot kit, Parashakti, the Trace site, the UISA record), each with its audience, how to get it, what is shown to work and its release gap; the README links each practice notebook to Colab.

- added `lang/hindawi/data/ayecode_alphabets.json` (sha256 `9a9147a1fe2b9234`)
- changed `docs/trace/index.html` (sha256 `0ba0d441ec97744e`)
- changed `docs/trace/data.js` (sha256 `ce1911fd15b5be60`)
- added `PRODUCTS.md` (sha256 `44bdbf0f5ebe7e1b`)
- changed `README.md` (sha256 `6e116e5a8025e4d1`)
- changed `work-packages/tasks.json` (sha256 `737c1d1c368eccea`)

**Verified.** The site driven headless: no errors; the AyeCode round trip verified in the Sa Re Ga alphabet. test_all passes.

## C28. Inside the machine: APCISR's algorithm, a text-mode screen, graphics mode, the framebuffer, the display, GPUs, GPGPU and AI

**Why.** He found the explainer site too shallow for the question asked and asked for the whole path end to end: APCISR's algorithm shown on its 9-grid, text mode, graphics mode, the DAC, GPUs, GPGPU, acceleration and AI. docs/trace/machine.html follows a typed Indic text from Unicode to ISCII, then steps APCISR's original acii2cisr() component by component, showing the table entry (Romenagri name, ISCII bytes, purna, the nine grid values), the state before and after (matrik, lipik, purak, purna, varna_purna, prev_hal, prev_ra_hal), the working map with the cells each step changed, and the letter forming through the font substitution; then an 80 by 60 text-mode screen whose cells hold a code and an attribute at B800, with each cell's address and 8 by 16 bitmap; graphics mode with raster against vector at any size; the framebuffer with RGB and HSV per pixel; the VGA DAC and the digital link; one processor against many; a matrix product as CUDA threads; and a neural layer. The engine is the original C (hindawiai/chintamani APCISR/, GPL-2.0-or-later) compiled to WebAssembly with two lines that only record state (docs/trace/apcisr/src).

- added `docs/trace/machine.html` (sha256 `e9516ef877bb2145`)
- added `docs/trace/apcisr.js` (sha256 `7c54636a05aa2e84`)
- added `docs/trace/apcisr-data.js` (sha256 `5c0da53f62a24d1e`)
- added `docs/trace/apcisr/src/acii2csr.c` (sha256 `2610a50603f5734f`)
- changed `docs/trace/index.html` (sha256 `9328dfdc564ada79`)
- changed `README.md` (sha256 `8b1f73fd7cd9da90`)

**Verified.** On 1,497 inputs (every table entry, pairs of the first thirty, triples of the first eight) the WebAssembly engine's output is byte for byte that of the original compiled natively. The page driven headless with the real engine: no errors; कर्म क्षत्रिय gives eight steps and eleven result columns; a tap on the screen gives the cell's address, code and bitmap. test_all passes.

## C29. Robots ready for physical seeding, the machine page made to build concepts, files and AI, Start here, Parashakti's sanity check, and the audit

**Why.** He found the APCISR lab did not yet show how characters combine, and the GPU and CUDA part did not build concepts; asked for the files, formats, OCR and AI discussion to be built in, for a landing that routes people, for the robots to be ready for physical seeding with an instructions page, for Parashakti to check the machine in limited time instead of installing everything, and for an audit of everything done and pending. The APCISR lab now draws, for each step, the working map before, the component's own pieces on its 3 by 3 grid, and the map after, with a sentence saying what the algorithm decided (a full letter, a vowel sign joining, a halant waiting, a ref placed). The GPGPU section builds the idea in seven steps, from one multiplication to a neural layer. A files, formats, OCR and AI section gives his answers, with the reader's text measured. A GATE syllabus map links each part to its subject. The front page has Start here. docs/robots/index.html takes a builder from parts to a recorded run; the ESP32 serves its own phone control page; Stage 1 can be driven from the page over USB. parashakti.sh probes each tool, the SHAKTI machine, the network, sudo and the disk, each in limited time, installs nothing unless asked, and runs each project only where its needs are met. AUDIT.md records what is released, done, pending and related.

- added `docs/robots/index.html` (sha256 `541ede69e51e14c8`)
- changed `docs/trace/machine.html` (sha256 `33c4f2e18e541bfd`)
- changed `docs/index.html` (sha256 `092321af393ff44a`)
- changed `robot_coding/esp32_l298n_wifi/esp32_l298n_wifi.ino` (sha256 `8c251610420c1aea`)
- changed `scripts/parashakti.sh` (sha256 `f4b1086b2806db66`)
- added `AUDIT.md` (sha256 `e3ca555fa5cdf472`)
- changed `work-packages/tasks.json` (sha256 `34ba4ee24cd8614c`)

**Verified.** The machine page driven headless: no errors; the step sentence, the ideas and the sizes shown. The ESP32 sketch, with its page, lowered from six languages and syntax-checked. parashakti.sh --check run here. test_all passes.

## C30. Doubt any section, ask any AI, a modern home page, the process as a product, and Parashakti that publishes

**Why.** He asked for a way for doubtful readers to check each claim (a fingerprint to quote, problems to solve, issues for the best critics, games for the curious), for any text on any page to be put to any AI, for a modern home page linking everything, for zops and this process to be offered to others, and for Parashakti to show progress, ingest the SHAKTI SDK first and every dependency layer by layer, test more strictly than upstream, and publish each result as a fork with one branch per language, synced and minted. docs/assets/aye.js gives every page a Doubt this? panel per section (its SHA-256 fingerprint, a way to check it, a pre-filled GitHub issue, a work package), badges and hidden finds, and an Ask AI menu for selected text (Claude, ChatGPT, Perplexity, Copilot, Grok, Gemini). docs/index.html is rebuilt as a landing with every page, the products and the ecosystem. docs/process/index.html sets out the process and how to install and use zops, misty and the timestamp client. parashakti.sh shows a progress line on every long step, checks readiness only for the languages asked, puts the SHAKTI SDK first with OpenSBI, QEMU and binutils behind it by layer, builds each project once in English as the baseline, verifies a language only when its tree reverses to upstream byte for byte and its output matches the English build, and with --publish forks the upstream (or mirrors it) with one branch per language, a default branch carrying the evidence and a daily sync workflow, under a typed PUSH, with --mint behind a typed MINT. docs/parashakti/PROCESS.md describes it.

- added `docs/assets/aye.js` (sha256 `5c10857b16cca5dc`)
- changed `docs/index.html` (sha256 `464d495e87d4272b`)
- added `docs/process/index.html` (sha256 `06641f45a2c9e27a`)
- changed `scripts/parashakti.sh` (sha256 `4d601a51f9e1dcfa`)
- added `docs/parashakti/PROCESS.md` (sha256 `121baac34ebdb27b`)
- changed `lang/hindawi/tools/foundation.py` (sha256 `97b8ed8c09c65c10`)
- changed `AUDIT.md` (sha256 `6ebf42ea597a79a8`)
- changed `work-packages/tasks.json` (sha256 `b175d2308f17eafd`)

**Verified.** Rehearsed here: SHAKTI and xv6 proved in Urdu with progress shown; xv6 in Urdu reversing to its upstream in 65 of 65 C files and printing the same lines as the English build; published into a local repository with the branches riscv, lang/urdu and parashakti. The home page driven headless with the shared script: no errors, four doubt panels, a fingerprint and a pre-filled issue, badges awarded. test_all passes.
