# Working on one codebase in many human languages

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

A tech lead who reads Gujarati C reviews code a colleague writes in Tamil C. Neither learns the other's language: each
works in a **view** of the same canonical tree, rendered in their own language by BURP, and every save returns through
BURP's reverse to the canonical tree, from which every other view is refreshed. The canonical tree stays what the
project's repository holds, so git, review, CI and upstream contribution are unchanged.

## The editor: Geany

Geany is light, installs from the distribution (`apt install geany geany-plugin-debugger`), and runs offline. It
takes a filetype per language with its own keywords, build commands per filetype, and GDB debugging through its
debugger plugin. Eclipse CDT works the same way, through External Tools; VSCodium, the open-source build of VS Code,
installs offline as a .deb if a heavier editor is wanted.

    python3 ide/burp_ide.py view  ~/src/project --lang tamil    --out ~/views/project-tamil
    python3 ide/burp_ide.py view  ~/src/project --lang gujarati --out ~/views/project-gujarati
    python3 ide/burp_ide.py geany --lang tamil       # keywords highlighted, compile, build, run through hindawicc
    python3 ide/burp_ide.py watch ~/views/project-tamil   # every save reaches the canonical tree and the other views

## Debugging

Build with `-g` through hindawicc (the Geany build commands do). Native names reach the ELF symbol table through
Romenagri. In gdb, with `ROMENAGRI` and `BURP_DICT` (the view's `.hindawi/dictionary.json`) set:

    (gdb) source ide/burp_gdb.py
    (gdb) burp-bt
    (gdb) burp-locals

## What it does not do yet

- A name typed in a view that the dictionary does not know reaches the canonical tree as typed, and other views show
  it as typed until a translator names it.
- Comments are translated only when a translator is installed (docs/hindawi/TRANSLATION-TOOLS.md).
- The compilation path works for the languages `docs/hindawi/burp-status.tsv` marks `runs-42`; a view in any other
  language reads and edits correctly, and builds from the canonical tree.
- Converting one programming language into another (C to Java, say) is not this: it needs the AST and IR work that
  Sūktam carries.
