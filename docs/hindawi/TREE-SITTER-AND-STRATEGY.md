# Tree-sitter, and where BURP stands

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

## What tree-sitter is

Tree-sitter is a parser generator and incremental parsing library, open source under MIT, begun at GitHub. A grammar
per programming language yields a concrete syntax tree that updates as the user types and survives syntax errors.
Editors use it for highlighting, folding and structural selection (Neovim, Helix, Zed, Emacs 29 and others), and
GitHub uses it for code navigation. It parses programming languages; it has no notion of the human language a program
is written in. Its keywords stay English, it translates nothing, and it has no compilation path.

## How BURP differs, and where they meet

| | Tree-sitter | BURP and Hindawi |
|---|---|---|
| Purpose | parse code for tools | let people write, read and build code in their own language |
| Unit | programming language grammar | human language × script × paradigm |
| Output | syntax tree | the same program in another human language, and back byte for byte |
| Names | untouched | translated per project through a dictionary; survive to the ELF symbol through Romenagri |
| Build | none | hindawicc, a drop-in gcc |

They complement each other. Tree-sitter's grammars could replace BURP's regular-expression scanners for exact,
error-tolerant tokenisation across the many programming languages beyond the nine shailis, while the transducers stay
the source of every keyword's native form and Romenagri the compilation path. Tree-sitter's query files
(`highlights.scm`) could carry each language's native keywords, giving every tree-sitter editor highlighting in
every human language at once.

## Strategy

Tree-sitter spread because it is permissively licensed, solves a problem every editor has, and lets communities
contribute grammars that every editor then shares. The same shape suits Hindawi:

1. **Plug into the editors people already use** rather than ask them to move: a language server that serves any
   file as a view in the reader's language, and tree-sitter query files for native highlighting.
2. **Let communities own their languages.** Each language's keywords and glossary are contributed and reviewed by
   its speakers, with provenance, as tree-sitter's grammars are by theirs.
3. **Lead with what nobody else does:** the round trip that loses nothing, names that survive to firmware, and one
   codebase worked on in many human languages at once.
4. **Enter through education and sovereign stacks:** courses taught in the student's language, and public
   infrastructure that must be maintainable by people who do not read English.

Earlier non-English programming languages, from Hindawi itself in 2004 to Hedy's multilingual keywords for teaching,
changed keywords for one language at a time. Localising identifiers and comments reversibly, across many languages at
once, inside existing toolchains, is the opening.
