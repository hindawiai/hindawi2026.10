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
