# Terminology book

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

One place for the terms used across the estate. Each entry gives the term, then what it means here.

## Hindawi and Project ILM

**Hindawi.** The programming system first released on 15 August 2004 (GPL): programming in one's own language,
carried by transducers to existing toolchains.

**Chintamani** (`hindawiai/chintamani`). Legacy Hindawi and Romenagri as they stand; the reference everything is
checked against.

**Shaili.** A Hindawi style: the pair of transducers, driver and Makefile that carry one host language. The nine:
- guru (C), shraeni (C++), yantra (assembly);
- kritrima (Java), praatha (BASIC), soochee (Python);
- wyaaka (yacc), shabda (lex), robot (LOGO).

**Transducer (`.uhin`).** A lexer written in the language's own script that maps its words to a host language
(`h2c`) or back (`c2h`). The lexers are the mapping.

**Composition.** One shaili piping into another, because the host's embedded code is C. `shabda` runs `h2l | h2c`.

**Romenagri.** The script layer: Unicode to ACII and back, and the C-friendly form names take in host code.

**ACII.** Romenagri's internal encoding, through which every script passes.

**Name ABI.** The rule that turns a native identifier into its host symbol, and back: Romenagri's C-friendly
form, so `योगफल` becomes `yoagaphala`.

**Cell.** One language's set of transducers for the shailis, in `lang/hindawi/languages/<language>/`.

**Construct.** One unit of the standard, such as `if`, translated once per human language and never once per
host language.

**Decorator.** What a host needs that no construct carries, such as `stdio.h` for C.

**Ingestion path.** Turning an existing project into a language, for people: keywords, identifiers and comments.
No transliteration.

**Compilation path.** Turning native source into host code, for the machine, always through Romenagri.

**BURP.** The Bidirectional Universal Resource Parser, Hindawi's ingestion pipeline.

**Dictionary.** BURP's record, for one project in one language, of every identifier, comment and renamed file.
It is built during ingestion and makes the reverse exact.

**Script filter.** The step that carries a script to Devanagari, the pivot for Brahmi-derived scripts.

**Project ILM.** Integrative Linguistic Multiscript, the successor programme to Hindawi. It keeps three axes
apart: script, language and the computational standard.

## The estate's repositories and tools

**tajziya** (`zistgah/tajziya`). The parser system for the classical languages and their language packages.

**Pushkalāvatī / Nirgundi** (`hindawiai/sanskrit`). Computational Paninian grammar for Sanskrit. It is separate
from Hindawi.

**Sūtram.** Pushkalāvatī's rule-rewrite language. **Sanchalan / Sūktam:** the kernel work written in it.

**PANINI.** The language for prompt cycles; the cyclers are written in it.

**zops.** The operations library: seal, push, mint and record back, each behind a typed gate.

**Typed gate.** An irreversible step proceeds only when its word is typed, such as PUSH or MINT.

**misty** (`misty-doi`). The tool that mints Zenodo DOIs and versions beneath a concept DOI.

**Seed.** Creating a repository and pushing its first sealed history. **Mint:** giving it a DOI.

**Concept DOI.** The DOI that names every version of a work. **Version DOI:** the one that names one release.

**Candor.** The protocol for frank, verifiable intent: an in-toto statement, stamped with OpenTimestamps.

**Seal.** `MANIFEST.sha256` over every file, stamped with OpenTimestamps.

**Packet.** A unit of work handed to someone else, with one mechanical acceptance command.
