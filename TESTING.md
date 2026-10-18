# Testing Hindawi 2026.10

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

After seeding, one command tests the repository: `hindawi test`, or `hindawi test --full` to add the GATE programs.
Each suite prints its own result and the harness ends with a summary, PASS or FAIL per suite.

| Suite | What it protects | Command |
|---|---|---|
| Originals byte for byte | the original Hindawi files, the BUILD-0102 sources and the recorded source stages are exactly as received, and nothing is added among them | `bash tests/check_originals.sh` |
| The build's own suite | the JavaScript and Sūtram tests, the ports, the Romenagri integration, the static pages, and everything below that is wired into it | `bash scripts/test_all.sh` |
| Standards, review data, trademarks, register, stages | each draft standard is complete where it exists and absent where bindings are incomplete; Hindi is on the review page; the trademark pointer and credits are present; every open task has a package with the originator's credit; the compilation stages are shown and compiled as shown | `python3 tests/check_standards_register.py` |
| Fundamental regression | the original Hindawi files unchanged, its samples compiled, Wave 0, every shaili both ways, a two-file project through BURP and hindawicc, a native name surviving to the ELF symbol | `python3 tests/fundamental.py` |
| Notebooks | every language's notebook has Chintamani's structure (installation, practice area, and per shaili the program, input, compilation flow, execution and Std2Hin cells), and its demos build through the original pipeline and print what English prints | `python3 tests/check_notebooks.py` |
| GATE programs (`--full`) | every C program compiled from each complete language through the original pipeline, the Python program run through each language's own transducer, both compared with English; every file reversed byte for byte | `python3 tests/gate/run.py --langs …` |
| Manual verification | the same, step by step, with the result each step should give | `VERIFY.md`, `hindawi verify` |

The GATE results are recorded, dated, in `docs/hindawi/data/gate-results.json`; the standards cite that record.
A suite that cannot run (for example, the stages check before `hindawi setup` has built the Romenagri tools) says
UNJUDGED and why; it never passes silently.
