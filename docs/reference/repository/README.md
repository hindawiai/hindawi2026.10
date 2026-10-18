# Hindawi 2026.10

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

Hindawi lets people program in their own language and script, from application code down to firmware. This release
carries Hindawi's shaili toolchains for 76 languages, and BURP, the Bidirectional Universal Resource Parser, which
ingests any existing project into any number of languages at once and reverses it byte for byte.

**Start here.** `bash install.sh` checks what Hindawi needs, builds Chintamani's toolchain from the pinned source,
puts `hindawi` and `hindawicc` on your PATH, and proves the installation by compiling a program from Urdu and from
Telugu. Then `hindawi --help`, `man hindawi`, and `docs/hindawi/MANUAL.md`, which says how to work on this and where
every tool lives. `VERIFY.md` is the manual verification, step by step, with the result each step should give.

- **Ingestion (BURP).** `hindawi ingest SRC --langs all --out OUT`. Keywords come from each
  language's own transducers; names and comments are translated into a dictionary kept with the project, using
  whichever translators are installed (glossary, Argos Translate, a local language model, any command). Application
  work needs nothing more. See `docs/hindawi/BURP.md`.
- **Compilation, down to firmware.** `lang/hindawi/hindawicc` is a drop-in gcc. It compiles on the transliterated
  (Romenagri) form, so native names survive to the symbol table and the debugger. This is needed only at the lowest
  layers.
- **Editors.** The Arduino IDE (`ide/arduino/install.sh`: students program their boards in their own language),
  Eclipse (`ide/eclipse/`), Geany, and gdb with native names (`ide/gdbinit`). See `docs/hindawi/IDE.md`.
- **Samples.** `samples/gate/`: programs for every programming domain GATE covers, in C with Python, Java, C++ and
  BASIC beside them. `hindawi gate --langs sanskrit` ingests them into a language, compiles each C program
  from that language through the original pipeline and checks it prints what the English one prints. What each
  program teaches, against the GATE syllabus, is in `docs/hindawi/GATE-PROGRAMS.md`. The sets are on the site beside the English one: `docs/hindawi/samples/index.html`.
- **Your language's standard.** Review it construct by construct and paradigm by paradigm, from hardware description
  to robots and AI, on `docs/hindawi/review.html`; each proposal is an issue here. Each language's gaps are in its
  cell's `STATUS.tsv`.
- **The linguistics lab.** `docker compose -f lab/docker-compose.yml up --build`: JupyterLab, the review pages, Praat
  and Argos Translate, with Hindawi built inside. See `lab/README.md`.
- **The sovereign stack.** `scripts/sovereign/stack.sh --list`, then one stage at a time.
- **What changed, and where this departs from earlier Hindawi.** `CHANGE-LOG.md`, `docs/hindawi/DEVIATIONS.md`.

The Sanskrit parser (Pushkalāvatī, Sūtram) that shares this tree has its own home in hindawiai/sanskrit; this
tree's earlier README is kept at `docs/history/README-BUILD-0102.md`.
