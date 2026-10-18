# PANIR, the Paninian Intermediate Representation: a proposal

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. PANIR™ is a trademark of Abhishek Choudhary.

Status: **proposal**. Nothing in this document is implemented in Hindawi 2026.10 except what section 5 names as existing.
The specification was drafted with ChatGPT and Gemini on 18 October 2026 and given to this project to integrate. This
record says what it proposes, what was checked, and what was found wrong, so that the proposal can be judged on its
merits and nothing in it is mistaken for a result.

## 1 What it proposes

A canonical semantic representation between source languages and their renderings. Each source language keeps its own
parser; its syntax tree is normalised into PANIR, which records meaning (types, symbols, scopes, expressions, control
flow, calls, memory, aggregates, modules, exceptions, provenance and diagnostics) and none of the source's punctuation.
Renderers then express PANIR in a target: Hindawi in any language, C, Python, or documentation. The C/C++, Fortran,
COBOL and Python frontends are described, with the normalisations each needs (array slices, verb-driven arithmetic,
indentation scoping, comprehensions).

Its strongest point is one the Hindawi transducers cannot make: the same source character can mean different things
(`*` as multiplication, dereference or a pointer declarator; `[]` as indexing or as array size), and a representation
built from the syntax tree keeps those meanings apart before any word is chosen for them.

## 2 How it relates to Hindawi

- **BURP** ingests by tokens and a dictionary: keywords are replaced, names translated, punctuation kept. It is exact
  and reversible, and needs no parser. PANIR needs a parser per source language; it does not replace BURP.
- **The compilation path** lowers a native source text, through the script filter and Romenagri, with the language's
  transducer, to the host language, which gcc compiles. This is the covenant: everything survives to the silicon
  layers. PANIR must therefore lower **into** this path, never around it.
- A **de-punctuated rendering** (words for operators, no brackets or semicolons) is a new surface for reading and
  teaching. It is not compilable by the transducers. For it to survive to silicon it needs a parser back to PANIR, and
  PANIR needs a renderer to a host-language text that enters the existing pipeline.

## 3 What was checked and found wrong in the inputs

1. The poster "Hindawi Programming System, a multi-language semantic normalization and target-rendering framework"
   shows evaluation results (success rates near 90 per cent by language) and a performance-overhead chart. No such
   evaluation has been run. Those panels are illustrations produced by an image generator and are not results.
2. Several Devanagari renderings on the same poster are garbled by the image generator; they are not specified text.
3. The Fortran `IF (...) THEN` row keeps parentheses in its target, against the specification's own rule that grouping
   parentheses are eliminated.
4. The Fortran `DO i = 1, 10` rendering adds a declaration of `i` that the Fortran loop does not contain, which changes
   the program.
5. COBOL `ADD ... GIVING` is normalised to a plain addition. COBOL arithmetic carries decimal sizing, rounding and size
   error semantics; the specification's own equivalence rule (its section 41) forbids dropping them.
6. The Python comprehension example uses an address-of operation. Python has none.
7. "No global regex substitution" is stated as non-negotiable. Taken literally it would rule out the Hindawi
   transducers, which are lexical substitution and are the compiled path. The rule is adopted for PANIR's own renderers
   only.

## 4 What is adopted, as proposal

The separation of frontend, PANIR and renderer; semantic neutrality (PANIR carries `MULTIPLY`, never a Hindawi word);
distinctions kept until rendering (dereference versus multiplication, indexing versus array type, `.` versus `->`);
ordered arguments and evaluation order; provenance on every node; diagnostics instead of silent change; versioned
serialisation; no machine-level lowering inside PANIR (that belongs downstream, as GCC's GENERIC precedes GIMPLE).

## 5 What exists today that PANIR would use

- `lang/hindawi/tools/hindawi_chain.py`: the compilation path, with every stage visible (`stages()`), which a PANIR
  renderer to C would feed.
- `lang/hindawi/burp/burp.py`: exact, reversible ingestion with a per-project dictionary of names.
- The standards in `standards/`: the keyword bindings a Hindawi renderer would use.

## 6 What would make it real

A machine-checkable PANIR schema and its validator; a C frontend built on an existing C parser; a renderer to C whose
output passes through the existing pipeline and runs the GATE programs with unchanged results in every complete
language; then a de-punctuated renderer with a parser back, tested by round trip. Each is a work package in TASKS.md
(T-14); none is claimed done.
