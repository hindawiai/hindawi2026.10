# BURP, the Bidirectional Universal Resource Parser

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

BURP is Hindawi's ingestion pipeline. It takes an existing project, in any of the paradigms (shailis), into any
number of languages at once, and back again exactly.

## Two paths, kept apart

**The ingestion path** is for people. It localises a project so that a speaker reads and writes it in their own
language. It needs no transliteration, only the right words in the language's own script:
- **Keywords** become the language's own keywords, from that language's reverse transducers (`*2h.uhin`). For
  Hindi these are Chintamani's originals.
- **Identifiers** are translated once per project and language, and recorded in the project's dictionary.
- **Comments** are translated, and also recorded in the dictionary, so the reverse restores them exactly.
- **Externals** stay as they are: names the project does not define (whatever the system headers declare, found
  by running the preprocessor), the host language's keywords, and anything matched by `--keep`.
- **`-D` and `-U` names in build files** go through the same dictionary.
- **File names** are localised only with `--rename-files`: the files are renamed, and the `#include` lines and
  build files that name them follow.

**The compilation path** is for the machine. Native source goes through the script filter and Romenagri to
the language's h2c, then to gcc. Transliteration is essential here: it is what lets names survive to the symbol
table, the debugger and the firmware.

## Commands

    python3 lang/hindawi/burp/burp.py ingest  SRC --langs all|hindi,urdu,... --out OUT [--scripts brahmi|bengali,...]
                                              [--rename-files] [--translators glossary,argos,cmd] [--keep REGEX]
    python3 lang/hindawi/burp/burp.py reverse OUT/<language> --out BACK
    python3 lang/hindawi/burp/burp.py check   SRC --langs all --scripts brahmi      ingest, reverse, compare
    python3 lang/hindawi/tools/build_project.py OUT/<language> --lang <language> -- <make target>

- **`OUT/<language>/`** holds the native tree, and its dictionary is `OUT/<language>/.hindawi/dictionary.json`.
- **`--scripts`** also renders a Brahmi-script language in the other Brahmi scripts, by Unicode name projection.
  Each rendering goes to `OUT/<language>@<script>/`.
- **`build_project.py`** builds the native tree with the project's own Makefile, using `CC=hindawicc`, which
  maps every `-D` and `-U` name through Romenagri.

## Translators

They are tried in order, for every word or phrase not yet in the dictionary:
- **`glossary`:** `lang/hindawi/tools/tables/identifiers.csv`, then `lang/hindawi/burp/glossary/<language>.tsv`.
- **`argos`:** Argos Translate, offline.
- **`cmd`:** any program named in `HINDAWI_TRANSLATE_CMD` (with `{lang}`), reading lines and writing lines. A
  local LLM fits here.

A word no translator knows stays as it is. The dictionary is built during each ingestion, never fixed in
advance. `docs/hindawi/TRANSLATION-TOOLS.md` compares the tools available.

## Measured, 16 October 2026

The sample project in `tests/burp/sample` has a Makefile with `-D` names, three C files across two folders,
C++, Java, Python, BASIC, yacc, lex, assembly and LOGO. `burp.py check --langs all --scripts brahmi`:
- **Ingestions:** 355 in all, 76 languages plus 279 renderings into other Brahmi scripts, and every one of them
  reverses to the original byte for byte.
- **Languages whose own keywords appear, by paradigm:** C 66, C++ 55, Java 58, Python 55, lex 63, yacc 7,
  BASIC 4, LOGO 5, assembly 0.
- **Nothing localised in 10 languages,** because their cells carry Latin keywords or none: Balinese, Batak,
  Buginese, Lepcha, Limbu, Pashto, Santali, Shan, Sundanese and Tagalog.
- **Compilation path:** the sample, ingested and built with its own Makefile through `hindawicc`, prints 42 in 30
  of the 76 languages, 20 of them with their own keywords and 10 (the ones above where nothing is localised)
  only because their source is unchanged. `docs/hindawi/burp-status.tsv` names them. In the rest, the cell's two directions disagree
  or its script has no route to Devanagari yet (`docs/hindawi/DEVIATIONS.md`).
