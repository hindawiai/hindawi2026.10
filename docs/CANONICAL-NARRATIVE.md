# Pushkalavati / Hindawi / ILM — full thread narrative

## 1. Starting point and original handoff

The work began from `HANDOFF.md` and `sanskrit-parser.zip`. The question was whether a simple one-to-one mapping of sutras, cycled in a rule engine, produces all operational rules, and if not, what the benefit of Panini’s system is. The framing was a T-diagram for self-hosting: meta-rules expand into operational rules, then those operational rules run. Translations were to be done by hand because the parser could not yet translate. Claims were to be sourced. Attested forms were to be tested. Shallow implementations were to be avoided.

Later attachments added `pushkalavati-spine.zip`, an architecture document, and the same parser archive, with the instruction to build toward the automated path in the handoff rather than reinvent.

## 2. What the handoff actually required

The Paninian machinery named in the handoff was samjna, paribhasha, adhikara, anuvrtti, atidesha, vipratishedha, para, pratyahara, utsarga, and apavada. The engine side was `Rule.hetu` / `Rule.nigamana`, `Engine.step` / `Engine.run`, specificity plus registration-order tiebreak, and 1.4.2 `vipratiṣedhe paraṃ kāryam`. Structural conversion covered padaccheda, vibhakti role assignment via 1.1.49 / 1.1.66 / 1.1.67, adhikara locative scoping, and a verification gate. The use case that was corrected into place later was not “Sanskrit text generation.” It was building programming languages in Sanskrit across paradigms: a self-hosting meta-grammar, with object, functional, and imperative mappings, and lowering to a backend. A parser that can build an AST can also generate from that syntax.

## 3. First mechanism and what it showed

A flat 1:1 mapping was incomplete: no adhikara inheritance, no guna expansion. The response was an Engine-based meta-cycle. Stage one expands. Stage two runs operational rules. A narrow morph slice was built and tested: a-stem accusative singular via 4.1.2 and 6.1.107. That satisfied a partial REQ-1.1 while respecting the coverage ethic. Coverage classes were COVERED / CANNOT_CHECK. A padaccheda split bug on `आत्-ऐच्` was fixed by hyphen parsing. A provenance bug (`source_has_term` always true) was fixed with a guard. Import paths were fixed by running from repo root with `PYTHONPATH=python`. The main print was corrected so it did not claim a stub where one was not. Karaka remained a stub and was not overclaimed.

## 4. Repo, license, and Nirgundi

A complete GPLv3 repository was requested, Copyright © 2026 Abhishek Choudhary. Attached instructions were to be curated into the zip, and the 3800+ rules were to be completed structurally, not by pretending every sutra was executable.

The Nirgundi experiment was specified exactly: literal longest-first search-and-replace, no stemming, no sandhi reversal, no normalization, execute on a corpus, preserve residual. Lexemes were to be sorted reverse by length, then replaced on first match, longest string first. A substring bug (`evam` inside `devam`) was fixed by whole-token exact match after that sort. A `seen` set that skipped identical tokens was removed. A test method placed outside its class was moved inside. An `agnibhiḥ` expectation was updated to gated consumption. Marker escaping in residual spans was fixed. An overclaim in `__main__.py` was replaced with a truthful print.

Source discovery and IKS licensing were part of this thread. An MW download was attempted; only headwords were extracted, and the script mismatch was reported rather than normalized away. 286k records were extracted at one point. 3983 sutras were converted structurally: roles, anuvrtti copy, locative scoping, expanded JSONL, without claiming full derivation. About 63% matched in one reported run. The verification gate stayed: gloss null means `executable: false`.

The Nirgundi method was then updated to use converted records rather than reinvented. After the first match run, the instruction was to apply parser rules, sandhi vichheda, measure remaining non-consumed corpus, measure rule coverage, and rerun until all rules are built or the corpus is exhausted. That loop was the optimization path, not a claim that it had finished.

## 5. Inverse reduction, two-way grammar, and organization

An inverse-reduction slice was added: Devanagari tokenization, longest prefix, inverse 6.1.87 / 6.1.88 candidate generation, suffix left UNRESOLVED per the architecture. JavaScript was treated as primary; Python was left as placeholders where that was enough. Two zips were compared and the best of both was used to build a two-way grammar: forward generation and inverse analysis from the same production, with 6.1.94 as the example. A later curated version merged romenagri material.

## 6. What others have, and how it compares

Licensed open-source Panini implementations were reviewed from GitHub, not the local tree. Vidyut-prakriya has 2000+ forward rules in Rust, MIT. `sanskrit_parser` has sandhi and YAML, MIT. `vyakarana` had no usable license. Their use case is morphological generation or analysis of Sanskrit text. The local use case is a Sanskrit programming-language front end across paradigms, with lowering and raising. The handoff’s REQ-1.1 / REQ-2.1 were the comparison frame. Benchmark scripts were to be built into the repo against those systems. The observation was that most of them are not building a programming language; one does real reverse analysis.

## 7. Sanchalan Suktam, lowering, and raising

The Sanchalan Suktam is a 22-verse OS-like process model: pid, memory boards, pipes, traps, user mode. Rules needed to parse it were to be built in. The repo was to lower the sutram to compilable C and Rust, and raise C and Rust back toward the Sanskrit language. A Suktam parser, a C/Rust lab, and a Sanchalan parser were added. Visarga sandhi reduced residual: 8.3.15 khar-avasana, and the 8.3.34 + 8.4.40 path for `agniḥ + ca`.

QEMU was then required. A static freestanding-style C runtime was generated and run under `qemu-x86_64-static`. Apt install failed; the deb was downloaded and extracted. A trailing comma in JSON and a C function-order bug were fixed. The first QEMU path was user-mode execution of a static Linux executable, not a system-emulator boot of an OS image.

## 8. ChatGPT feedback on the visarga pair and the fake runtime

ChatGPT’s audit accepted the increment but rejected two things. 8.4.40 was collapsing 8.3.34 and 8.4.40 into one handler for `agniḥ + ca`. The derivation is 8.3.34 (`ḥ` to `s` before khar) then 8.4.40 (`s` to `ś` before palatal `c`). 8.3.15 is a different rule and does not produce the `ś` in `agniśca`. The generated C had a 22-entry table and `run_op` that only bumped three integers. Unknown operations were silently ignored. The emulator path was hard-coded under `/tmp`. QEMU was not independently reproducible from the archive alone.

The acceptance list was R1 through R6: separate 8.3.34 and 8.4.40, positive and negative vectors, fail closed on unknown ops, configurable emulator path, a reproducible QEMU test, and a document separating lexical recognition, grammatical derivation, and runtime execution.

## 9. Library instead of counters; x86 and Shakti-class RISC-V

The fake counters were removed. A small C library, `lang/suktam/lib/sanchalan.c`, became the runtime. The generated program calls `sanchalan_call`. Unknown names print a diagnostic and return nonzero. Recognized names with no runtime yet are counted as deferred. The user said the library would be converted to Sanskrit later, and that it should load on different architectures under QEMU. x86 was already addressed. RISC-V was to match Shakti.

Shakti C-class is RV64GC / RV64IMAFDC, 64-bit, in-order, Linux-capable, from IIT Madras. The run is QEMU user-mode on that ISA, not a Shakti SoC boot. A musl RISC-V toolchain was downloaded; it was a 32-bit host binary, so `cc1`, `as`, and `ld` were wrapped under `qemu-i386-static`. Both x86_64 and RV64GC verse traces matched. The emulator path checks `PATH`, then `QEMU_X86_64` / `QEMU_RISCV64`, and fails closed if neither is found. `docs/LAYERS.md` separates the three layers. Executable tested operations reached 15 after the split.

## 10. Hindawi upstream, and the path that actually works

ChatGPT could not finish Hindawi end-to-end: `flex`, `c2h`, `h2c`, `uni2acii`, `acii2uni` were missing, and apt timed out. A reverse-path bug was corrected in review: do not feed `acii2pcf` straight to `h2c`. The next gate was to build the real upstream, not invent substitutes.

`hindawiai/chintamani` was cloned at `3ad87785a75dc2b18438a8b068807103cb920c81`. Romenagri’s Makefile failed first on missing `flex`, then on missing `m4`. Those were downloaded as debs, not apt-installed. Romenagri then built `uni2acii`, `acii2uni`, `acii2cf`, and the other filters. Guru’s Makefile then built `h2c` and `c2h`.

The tested contract is `C → c2h → ACII → acii2cf → h2c → C`. The built `h2c` matches romanized tokens (`mukhya` becomes `main`) because the Guru Makefile runs `h2c.uhin` through `uni2acii | acii2cf` before flex. `gurucc` does `acii2uni | iconv | h2c`, which yields Devanagari. A minimal Hindi program stayed Hindi and did not compile on that path. That path was rejected. A tiny `int main(void){return 0;}` round-tripped. The Sanchalan library went through the same path, compiled, linked, and ran. Unknown operation returned nonzero. `build.sh` gained stages: `check-deps`, `translate`, `compile`, `test`, `clean`. Generated files stay in `lang/suktam/hindawi/build/`. The regression suite passed after a test script’s execute bit was restored. QEMU was excluded from that pass. Equivalence of every generated Sanchalan line with the original C was not claimed.

## 11. Localized C ports and vendored Hindawi files

ChatGPT could not open the upstream language files. They were vendored under `lang/hindawi/upstream/`: `project-ilm/romenagri` at `ef57fa4cdc7be00dac877498da9b2204577965cd` (`langs/*_c.tsv`, `langspec/data`, `tables`), and Chintamani shailis and samples (Guru, Shabda, Praatha, Wyaaka, Soochee, Shraeni). The expansion plan’s three axes were recorded: script projection to a Devanagari hub, language vocabulary, construct semantics. Perso-Arabic is lowered to Devanagari first, then follows the common path. Urdu is not Hindi. Persian is not Arabic. Gurmukhi is not Shahmukhi.

`test_ports.py` loads Sanchalan library keywords through every vendored C table. A port passes only if the keywords are present and round-trip to the same C tokens. Passed: Arabic, Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Odia, Persian, Punjabi, Sanskrit, Tamil, Telugu, Urdu. Incomplete and left incomplete: Aramaic, Assamese, Hebrew, Nepali, Pali, Phoenician, Prakrit, Syriac. Missing rows were not invented. QEMU x86 and RV64GC were rerun; verse traces matched.

## 12. Naming, standards, algorithms, privacy

Shaili is a paradigm. Shaili Prathmik is the Hindi BASIC-like language. Shaili Robot is the LOGO-like interface, which can also program robots. It is not Hindi Basic. BUILD-0002 already had the Robot page named correctly. Standards seeds were added as drafts for Hindi C, Hindi C++, Bangla C, and Bangla C++, with a template. They are drafts, not adopted standards. A C quicksort with three-way partitioning, median-of-three, insertion sort for small partitions, and heapsort fallback was added and tested. A privacy audit flagged the historical contact `choudhary@indicybers.net` in vendored `.uhin` headers. It was pointed out and not removed. No “by the author’s admission” language was to be written into the repo.

## 13. Suktam measurement and the rule-converter ceiling

Claude’s analysis, carried into this thread: the real number was 15 of 3983, with about 98% not close. The 15 that worked were pure phonology over the closed Siva-sutra inventory already built. Everything else splits into roots needing the Dhatupatha, verbal/nominal morphology, karaka/samjna machinery, and operations the compiler cannot express because it only knows substitution, not general deletion or insertion. 6.1.66 was noted as phonological and close. `IMPLEMENTATION_STATUS.md` was stale at 11.

Measured Suktam state at BUILD-0002: 22/22 verse boundaries, 141 lexicon nodes, 814 residual code points, 0/22 lexically complete. The parser scans the whole verse with a closed lexicon, longest-known-lexeme intent, and residual preservation. It does not do general sandhi-viccheda, padaccheda, morphology, or chandas. The generated C is a report. It does not execute the intended OS operations. General sandhi-viccheda and padaccheda were explicitly not implemented.

## 14. Builds 0003 through 0007

Build numbers go at the front of the zip name.

BUILD-0003: lexicon increment, 6.1.66 (`v`/`y` lopa before val). Nodes 159, residual 655. Executable tested 16 of 3983.

BUILD-0004: more source technical forms, 8.4.41 (dental `s` to `ṣ` before retroflex `ṭ`). Nodes 186, residual 428. Executable tested 17.

BUILD-0005: more source forms, 8.3.23 (final `m` to anusvara before a consonant). Nodes 212, residual 271. Executable tested 18.

BUILD-0006: remaining forms, 8.4.58 (anusvara to class nasal; class nasal supplied in context). Nodes 215, residual 256. Executable tested 19. What remained was mostly sandhi fragments and inflected endings.

BUILD-0007: the scanner was fixed to actual longest-match. Every remaining span in this Suktam, including the title `||SanchalanSuktam||` and sandhi fragments, was added to the closed lexicon as `residual` / `deferred`. Nodes 286. Residual on this source: 0. Unknown text outside this source is still preserved. Zero residual is recognition, not execution, not chanda-viccheda, not general sandhi-viccheda. The generated C is still lexical IR, not an operating system. Executable tested remains 19 of 3983. The contact address was left in place.

## 15. What is verified, and what is not

Verified: structural conversion of 3983 sutras; a meta-cycle on a small fixture; 19 attested phonological or morph operations; Nirgundi literal longest-first on a corpus with residual preserved; inverse-reduction slice with suffix unresolved; two-way grammar on a narrow production; Suktam framing of all 22 verses; library runtime with fail-closed unknown ops; QEMU user-mode on x86_64 and RV64GC with matching verse traces; Hindawi path `c2h | acii2cf | h2c` against real upstream tools; 14 complete localized C keyword ports; residual zero on this one Suktam by deferred recognition.

Not verified and not claimed: full derivation of 3983 sutras; Dhatupatha; full morphology; karaka parser; general sandhi-viccheda or chanda-viccheda; self-hosting of the whole meta-grammar; Shakti SoC boot; equivalence of every Hindawi-lowered Sanchalan line with the original C; semantic completeness of any Suktam verse; adopted national language standards.

## 16. BUILD-0008

A basic boot was added. The generated program calls `sanchalan_boot_banner`, runs the 22 verses through the library, then `sanchalan_boot_check`. Ready means pid 0 and at least one memory page. This is still a library boot under QEMU user-mode, not a kernel and not a Shakti SoC boot.


## 17. BUILD-0009

A freestanding RISC-V kernel boots under `qemu-system-riscv64 -machine virt -bios none` and reaches `login: `. That is the first prompt. It is not a shell and not a file system. The 22 verses are still lexically scanned, not grammatically derived. See `docs/SUKTAM-PARSE.md`, `docs/FIRST-LOGIN.md`, and `docs/OS-DISTANCE.md`.


## 18. BUILD-0010

8.4.55 was added as a closed pair: final g becomes k before unvoiced k. executable_tested is 20 of 3983. Residual on the Suktam remains 0 by deferred recognition. See `docs/NUMBERS.md` and `docs/WHY-NOT-AUTOMATED.md`.
