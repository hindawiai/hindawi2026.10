# Adding a human language, a script or a programming language without breaking the pipeline

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

## The pipeline that must not change

Chintamani's own drivers define it, and every addition plugs into it rather than around it:

    source in its own script
      → script filter to Devanagari (Brahmi-derived scripts; tables in tools/pushkalavati-compiler/vendor/romenagri/upstream/tables)
      → fixuninum | iconv | uni2acii | acii2cf | acii2uni | iconv          (Romenagri: the encoding names travel in)
      → the language's h2<shaili> transducer, composed with h2c where the shaili's action blocks are C (lex, yacc)
      → the host toolchain (gcc, flex, bison, javac, an assembler ...)

The reverse runs Romenagri's encoding in before <shaili>2h and acii2uni after it. `lang/hindawi/upstream/chintamani`
stays byte for byte Chintamani; `tests/fundamental.py` F1 fails the moment it does not.

## A new human language

1. Write its keywords in its own script only, construct by construct, starting from Chintamani's Hindi transducers
   (they are the reference for every construct). Mark each keyword's provenance: retrieved, reviewed by a speaker,
   inherited from a related language, or projected through the script table.
2. Make its cell: `lang/hindawi/languages/<language>/`, with a forward and reverse transducer for each shaili, a
   Makefile using the original commands, and a driver copied from Chintamani's with the language's cell.
3. Build it with Romenagri on the PATH, then measure it: `python3 lang/hindawi/tests/cells/cells.py roundtrip
   --cells lang/hindawi/languages --corpus <C sources> --langs <language>`. Coverage is published as status.
4. Identifiers: `hindawi ingest <project> --langs <code>` names them in the language through its dictionary (`lang/hindawi/burp/glossary/`)
   (one per ingestion, `HINDAWI_DICT`), and reverses through each name's Romenagri form.

## A new script

Add a table `<script>_to_deva.tsv` beside the existing 150 and a filter built from it, in flex and C as Chintamani's
`fltr_te_hi` is, with its inverse. Reversibility to the lowest layer exists today for Devanagari and, through
Devanagari, for Brahmi-derived scripts. Perso-Arabic, Hebrew, Cyrillic and CJK scripts are front ends: compilation
happens on the transliterated form, and where a script leaves sounds unwritten the table must say so.

## A new programming language (shaili)

Write its pair in Hindi first, `h2<x>.uhin` and `<x>2h.uhin`, in the layout of Chintamani's shailis (pass-through
rules for strings and comments, then one rule per keyword), with a Makefile and a driver like `gurucc`. If its
action or embedded code is C, compose with h2c as `shabdacc` and `wyaakacc` do. Add a sample, add the pair to
`PAIRS` in `tests/fundamental.py`, and only then generate it for other languages.

## Known limits, measured

- `acii2cf` doubles every underscore in ASCII identifiers (`debug_putc` becomes `debug__putc`). Inside one
  ingested project the dictionary reverses it; against existing libraries and macros it breaks names
  (`scripts/upstream/seabios.sh` builds SeaBIOS as is, and fails through the Hindi pair for this reason).
- Chintamani's own assembly pair (`yantra`) is not round-trip stable on its own sample.
- Comments are carried as text; their translation needs an offline translation model and must be stored in
  the ingestion's dictionary so the reverse can restore them exactly.
