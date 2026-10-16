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
