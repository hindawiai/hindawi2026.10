# Hindawi 2026.10: how to work on it

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

Hindawi lets a program be written in a human language and its own script, and built by the ordinary toolchain. It has
two paths, and one command, `hindawi`, reaches everything in the repository.

- **Ingestion (BURP).** Any file or project goes into any number of languages at once, and comes back byte for byte.
  Keywords come from each language's cell; names and comments are translated through glossaries into a dictionary
  kept with the project. This is what application work needs.
- **Compilation.** Source written in a language goes through the script filter and Romenagri, and the language's
  transducer turns it into the host language, which gcc compiles. Compilation always runs on the transliterated
  (Romenagri) form, so native names survive into the binary and the debugger. This is what firmware, kernels and
  the sovereign stack need.

## Install

    bash install.sh                  # for this user, into ~/.local
    bash install.sh --prefix /usr/local
    bash install.sh --uninstall

It checks for python3, gcc, flex, make, iconv and git, builds the Hindawi toolchain from the pinned source (the first
run fetches it from GitHub), links `hindawi` and `hindawicc` into the prefix's `bin`, installs `man hindawi`, and proves
the installation by compiling quick sort from Urdu and from Telugu. `hindawi doctor` repeats the checks at any time.

## The command

| Command | What it does | Behind it |
|---|---|---|
| `hindawi doctor` | checks prerequisites and the built toolchain | `bin/hindawi` |
| `hindawi setup` | builds the Hindawi toolchain, the original way | `scripts/build.sh`, `scripts/fetch.sh` |
| `hindawi languages [--refresh]` | each language's script, and whether it compiles | `tests/burp/compile_status.py` |
| `hindawi coverage --langs L [--missing]` | how complete a language is, paradigm by paradigm | `lang/hindawi/tools/coverage.py` |
| `hindawi ingest SRC --langs L --out D` | puts a file or project into languages | `lang/hindawi/burp/burp.py` |
| `hindawi reverse D/L --out B` | brings an ingested project back | `lang/hindawi/burp/burp.py` |
| `hindawi check SRC --langs L` | ingests, reverses and compares | `lang/hindawi/burp/burp.py` |
| `hindawi cc --lang L [gcc options]` | gcc for sources written in L | `lang/hindawi/hindawicc` |
| `hindawi build TREE --lang L` | builds a project with its own Makefile through hindawicc | `lang/hindawi/tools/build_project.py` |
| `hindawi gate [--langs L] [--only TEXT] [--gallery]` | the GATE programs in languages, compiled, run and compared | `tests/gate/run.py` |
| `hindawi standard [generate\|import]` | each language's standard in Markdown, JSON and Word; a filled work package back into the language | `lang/hindawi/tools/standards.py`, `standards_docx.js`, `standard_import.py` |
| `hindawi wp [list\|show ID\|generate]` | the work packages anyone can take: languages, JavaScript | `lang/hindawi/tools/work_packages.py` |
| `hindawi notebooks` | the Colab notebooks, in English and in each language | `lang/hindawi/tools/notebooks.py`, `lang/hindawi/colab.py` |
| `hindawi cells [--langs L]` | regenerates the language cells from the lexicons | `lang/hindawi/tools/complete_cells.py` |
| `hindawi stack [--stage Lnn]` | the sovereign-stack test, one stage at a time | `scripts/sovereign/stack.sh` |
| `hindawi arduino install` | the Arduino IDE drop-in | `ide/arduino/` |
| `hindawi lab` | the linguistics lab in Docker | `lab/` |
| `hindawi test` | the build's own suite and the fundamental regression | `scripts/test_all.sh`, `tests/fundamental.py` |
| `hindawi verify [--langs L]` | the verification steps of `VERIFY.md`, with PASS or FAIL | `bin/hindawi` |

`L` is a comma-separated list of language names (`urdu,sindhi,telugu`) or `all`.

## Everyday work

**See a project in a language, and bring it back.**

    hindawi ingest myproject --langs urdu,telugu --out /tmp/n
    hindawi reverse /tmp/n/urdu --out /tmp/back        # identical to myproject

The dictionary is in `/tmp/n/urdu/.hindawi/dictionary.json`; keep it with the project.

**Write or edit in a language, and compile.** A file BURP produced keeps its extension (`.c`), so tell `hindawicc`
it is native, and give it the project's dictionary:

    HINDAWI_LANG=urdu HINDAWI_NATIVE_SOURCE=1 HINDAWI_DICT=/tmp/n/urdu/.hindawi/dictionary.json \
      hindawicc -O2 -o prog /tmp/n/urdu/main.c /tmp/n/urdu/lib.c

Every gcc option passes through; `-D` and `-U` names go through the dictionary. `hindawi build /tmp/n/urdu --lang urdu`
does the same with the project's own Makefile.

**Complete a language.** `hindawi coverage --langs L --missing` lists every host keyword without a word, and every
word of the GATE programs' names without a translation. Words go in:

- `lang/hindawi/lexicons/L.tsv` or the language's column of `lang/hindawi/lexicons/multi.tsv`, for keywords and
  library calls (`token`, tab, `word`);
- `lang/hindawi/burp/glossary/L.tsv` or the column of `lang/hindawi/burp/glossary/multi.tsv`, for names.

Then `hindawi cells --langs L`, `hindawi coverage --langs L`, and `hindawi gate --langs L`. A language's own file wins
over the shared table, and the lexicon in `lang/hindawi/pipeline/language_params.json` wins over both. Every word added
this way is marked proposed until its community reviews it.

**Review a language's standard.** `docs/hindawi/review.html` shows each language construct by construct and paradigm
by paradigm; `docs/hindawi/contribute.html` turns a proposal into an issue on the repository.

**Teach with the GATE programs.** `hindawi gate --langs L --gallery` checks every program in L and copies the
ingested set into the site, where `docs/hindawi/samples/index.html` shows each beside its English original. What the
programs cover, what is still to write, and how another AI can write more: `docs/hindawi/GATE-PROGRAMS.md`.

**Publish a language's standard.** `hindawi standard --langs L` writes `standards/L/standard.md`, `standard.json` and
`standard.docx`: the language's bindings for C, C++, Java, Python, BASIC, LOGO and the preprocessor, laid out as standards
bodies take drafts, citing the host standards by reference only and recording where each word came from.

**Hand out the work.** `hindawi wp list` shows the open packages: for each language not yet complete, the keywords and
names it still needs (`work-packages/languages/L/`), and the move of the tools to JavaScript. Anyone claims one as a
GitHub issue from `docs/hindawi/work-packages.html`; a filled language package comes back with
`hindawi standard import L keywords.tsv names.tsv --by "name"`, which checks every word before it goes in.

**Teach in a notebook.** `notebooks/<language>/` holds seven Colab notebooks per language, from getting started to the
sovereign stack; `docs/hindawi/notebooks.html` opens them in Colab. In a notebook, `%%hindawi_c urdu` compiles a cell
written in Urdu through the original pipeline and runs it (`lang/hindawi/colab.py`).

**Editors and debuggers.** The Arduino IDE, Eclipse, Geany and gdb with native names: `docs/hindawi/IDE.md`.

## Where everything lives

| Path | What it holds |
|---|---|
| `bin/hindawi` | the command |
| `install.sh` | the installer |
| `lang/hindawi/hindawicc` | the drop-in gcc |
| `lang/hindawi/burp/` | BURP: ingestion and reversal; `glossary/` for names; `paradigms/` for VHDL |
| `lang/hindawi/languages/<lang>/` | each language's cell: eighteen transducers and `STATUS.tsv` |
| `lang/hindawi/lexicons/` | words proposed for keywords and library calls |
| `lang/hindawi/pipeline/language_params.json` | the languages' lexicons |
| `lang/hindawi/tools/` | the compilation path (`hindawi_chain.py`, `script_filters.py`), the cell generator, coverage, the project builder |
| `lang/hindawi/upstream/chintamani/` | Chintamani, unchanged: the reference every cell is measured against |
| `samples/gate/` | the GATE programs |
| `standards/` | each language's standard (Markdown, JSON, Word) and the standards' metadata |
| `work-packages/` | the open work, for students and AI, indexed for the site |
| `notebooks/` | the Colab notebooks, per language |
| `tests/` | `fundamental.py`, `gate/`, `burp/` and the build's earlier tests |
| `scripts/` | `build.sh` and `fetch.sh` (the toolchain), `sovereign/` (the stack test), `upstream/` |
| `ide/`, `lab/` | editor integrations; the linguistics lab |
| `docs/hindawi/` | this manual, BURP, IDEs, deviations, review and contribution pages, the samples site |
| `attic/` | retired tools, with what replaces each |
| `.build/` | everything built or fetched; safe to delete, `hindawi setup` rebuilds it |

## Rules that hold everywhere

- Compilation runs on the transliterated (Romenagri) form only. ACII and Unicode are never compiled; `acii2uni` comes
  after compilation.
- Ingestion is keyword replacement and dictionary-based naming; it needs no transliteration.
- Script, language and standard are kept apart.
- Coverage is published as status, never used as a gate.
- Every departure from the original pipeline is written down in `docs/hindawi/DEVIATIONS.md`, never made quietly.
