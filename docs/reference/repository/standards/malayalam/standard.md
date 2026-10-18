# HLS ml 2026.10

**Malayalam bindings for programming languages: lexical mapping and lowering to the host standards**

Edition 2026.10, working draft, 2026-10-18. © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

## Foreword

This document was prepared by AyeAI, Hindawi project (Project ILM). It is generated from the Malayalam cell of Hindawi 2026.10 by lang/hindawi/tools/standards.py, so that the published standard and the reference implementation cannot drift apart. Its stage is a working draft: the words marked proposed in Annex A await review by the Malayalam language community, through the review pages of the Hindawi project.

## Introduction

This document lets programs be written in Malayalam, in the Malayalam script, in each of the programming languages listed in Clause 1. Each binding is a programming language in its own right, Malayalam C for example, whose programs are lowered by the function defined in Clause 6 to programs of the host language, and are then processed by any conforming implementation of the host standard. The host standards are incorporated by reference and are not restated. Names keep a defined form down to object code (Clause 7), so programs written in Malayalam remain debuggable at the level of firmware, kernels and libraries.

## 1 Scope

This document specifies, for the Malayalam language written in the Malayalam script, bindings to the following host programming languages: C, C preprocessor, C++, Java, Python, BASIC, LOGO. For each binding it specifies the native keywords and directives, the lowering of native programs to host programs, the treatment of names, and the requirements for conformance.

It does not specify the syntax or semantics of any host language beyond what is needed to define the lowering, and it does not specify translations of comments, string literals or documentation.

## 2 Normative references

The following documents are referred to in the text in such a way that some or all of their content constitutes requirements of this document. For undated references, the latest edition of the referenced document (including any amendments) applies.

- ISO/IEC 9899, Information technology, Programming languages, C
- ISO/IEC 14882, Programming languages, C++
- The Java Language Specification, Oracle, current edition
- The Python Language Reference, Python Software Foundation, current version
- ISO/IEC 10279, Information technology, Programming languages, Full BASIC
- ISO/IEC 10646, Information technology, Universal coded character set (UCS)
- Unicode Standard Annex #15, Unicode normalization forms
- Unicode Standard Annex #31, Unicode identifiers and syntax

## 3 Terms and definitions

- host language: programming language defined by a normative reference, to which a native program is lowered

- binding: programming language defined by this document whose programs are written in Malayalam and lowered to one host language

- native keyword: word of this document that stands for one keyword, directive or standard library name of a host language

- lowering: function from native programs to host programs defined in Clause 6

- raising: inverse of lowering applied to a host program with a dictionary of names, giving back the native program exactly

- name transformation: function from native names to host identifiers defined in Clause 7

- C-level form: result of the name transformation; the form a native name takes in host source and in object code

## 4 Conformance

A conforming Malayalam program of a binding shall be a text that meets Clause 5 and whose lowering is a conforming program of the host language.

A conforming implementation of a binding shall accept every conforming program of that binding and shall behave as the lowering of the program, processed by a conforming implementation of the host language, behaves.

An implementation that raises host programs into a binding shall produce native programs whose lowering, with the same dictionary of names, is identical to the host program it raised.

## 5 Character set and encoding

A native program shall be encoded in UTF-8 and shall be in Normalization Form C. Native keywords and names are written in the Malayalam script, whose direction is left to right. Numeric literals are written with the digits 0 to 9 (U+0030 to U+0039). A native keyword written as several words is one token, its words joined by LOW LINE (U+005F).

## 6 Lowering

A native program is lowered by the following steps, applied in order to the tokens the host language's lexical rules yield when the letters and marks of the script are treated as identifier characters.

- Each native keyword of the binding's table in Annex A is replaced by the host keyword, directive or name it stands for.
- A host keyword for which Annex A gives no native word is written in its host form.
- Every other name is lowered as the binding requires: by the name transformation of Clause 7 for C, the C preprocessor, C++, BASIC and LOGO; unchanged for Java and Python, whose host standards accept such names.
- String literals, character constants, header names in include directives, and comments are not changed.
- Every other character is not changed.

## 7 Name transformation

The C-level form of a native name is obtained by passing the name, alone, through the script filter of the script (Annex C), then through the Romenagri transliteration (uni2acii followed by acii2cf), and writing each circumflex accent (U+005E) that results as LOW LINE (U+005F). Names already written in the digits, Latin letters and LOW LINE of the Basic Latin block are not transformed.

Two names declared in the same scope shall not have the same C-level form.

## 8 Reference implementation

Hindawi 2026.10 is the reference implementation: hindawicc lowers and compiles, BURP raises and lowers projects, and the Romenagri tools of Chintamani at commit 3ad87785a75dc2b18438a8b068807103cb920c81 give the name transformation. Where this document and the reference implementation differ, this document governs.

## Annex A (normative) Native keywords

### A.1 C

Host: ISO/IEC 9899, Information technology, Programming languages, C. Names: name transformation.

| Host | Malayalam | Source |
|---|---|---|
| auto | auto | host form (no native word yet) |
| break | നിർത്തുക | lexicon |
| case | അവസ്ഥ | lexicon |
| char | അക്ഷരം | lexicon |
| const | സ്ഥിരം | lexicon |
| continue | തുടരുക | lexicon |
| default | സ്ഥിരസ്ഥിതി | lexicon |
| do | ചെയ്യുക | lexicon |
| double | ഇരട്ട | lexicon |
| else | അല്ലെങ്കിൽ | lexicon |
| enum | എണ്ണൽ | lexicon |
| extern | ബാഹ്യ | lexicon |
| float | ദശാംശം | lexicon |
| for | വേണ്ടി | lexicon |
| goto | പോകുക | lexicon |
| if | എങ്കിൽ | lexicon |
| inline | വരിയിൽ | lexicon |
| int | പൂർണ്ണസംഖ്യ | lexicon |
| long | long | host form (no native word yet) |
| register | രജിസ്റ്റർ | lexicon |
| restrict | restrict | host form (no native word yet) |
| return | തിരികെ | lexicon |
| short | short | host form (no native word yet) |
| signed | signed | host form (no native word yet) |
| sizeof | വലുപ്പം | lexicon |
| static | സ്ഥിതം | lexicon |
| struct | ഘടന | lexicon |
| switch | തിരഞ്ഞെടുപ്പ് | lexicon |
| typedef | തരനിർവചനം | lexicon |
| union | സംഘം | lexicon |
| unsigned | unsigned | host form (no native word yet) |
| void | ശൂന്യം | lexicon |
| volatile | അസ്ഥിര | lexicon |
| while | ആകുമ്പോൾ | lexicon |
| main | പ്രധാന | lexicon |

Standard library and runtime names of the C binding:

| Host | Malayalam | Source |
|---|---|---|
| NULL | ശൂന്യ | lexicon |
| assert | പ്രതിജ്ഞാ | lexicon |
| free | സ്വതന്ത്രം | lexicon |
| private | സ്വകാര്യ | lexicon |
| protected | സംരക്ഷിത | lexicon |
| public | പൊതു | lexicon |
| raise | ഉയർത്തുക | lexicon |
| read | പഠ | lexicon |
| signal | സൂചന | lexicon |
| virtual | മായാ | lexicon |
| write | ലിഖ | lexicon |

### A.2 C preprocessor

Host: ISO/IEC 9899, Information technology, Programming languages, C (preprocessing directives). Names: name transformation.

| Host | Malayalam | Source |
|---|---|---|
| #define | #define | host form (no native word yet) |
| #include | #അന്തര്ഭാവ | lexicon |
| #if | #എങ്കിൽ | lexicon |
| #ifdef | #ifdef | host form (no native word yet) |
| #ifndef | #ifndef | host form (no native word yet) |
| #else | #അല്ലെങ്കിൽ | lexicon |
| #elif | #അല്ലെങ്കിലെങ്കിൽ | lexicon |
| #endif | #endif | host form (no native word yet) |
| #undef | #undef | host form (no native word yet) |
| #pragma | #pragma | host form (no native word yet) |
| #error | #error | host form (no native word yet) |
| #line | #line | host form (no native word yet) |

### A.3 C++

Host: ISO/IEC 14882, Programming languages, C++. Names: name transformation.

| Host | Malayalam | Source |
|---|---|---|
| auto | auto | host form (no native word yet) |
| break | നിർത്തുക | lexicon |
| case | അവസ്ഥ | lexicon |
| char | അക്ഷരം | lexicon |
| const | സ്ഥിരം | lexicon |
| continue | തുടരുക | lexicon |
| default | സ്ഥിരസ്ഥിതി | lexicon |
| do | ചെയ്യുക | lexicon |
| double | ഇരട്ട | lexicon |
| else | അല്ലെങ്കിൽ | lexicon |
| enum | എണ്ണൽ | lexicon |
| extern | ബാഹ്യ | lexicon |
| float | ദശാംശം | lexicon |
| for | വേണ്ടി | lexicon |
| goto | പോകുക | lexicon |
| if | എങ്കിൽ | lexicon |
| inline | വരിയിൽ | lexicon |
| int | പൂർണ്ണസംഖ്യ | lexicon |
| long | long | host form (no native word yet) |
| register | രജിസ്റ്റർ | lexicon |
| restrict | restrict | host form (no native word yet) |
| return | തിരികെ | lexicon |
| short | short | host form (no native word yet) |
| signed | signed | host form (no native word yet) |
| sizeof | വലുപ്പം | lexicon |
| static | സ്ഥിതം | lexicon |
| struct | ഘടന | lexicon |
| switch | തിരഞ്ഞെടുപ്പ് | lexicon |
| typedef | തരനിർവചനം | lexicon |
| union | സംഘം | lexicon |
| unsigned | unsigned | host form (no native word yet) |
| void | ശൂന്യം | lexicon |
| volatile | അസ്ഥിര | lexicon |
| while | ആകുമ്പോൾ | lexicon |
| main | പ്രധാന | lexicon |
| bool | തർക്കം | lexicon |
| catch | പിടിക്കുക | lexicon |
| class | വർഗ്ഗം | lexicon |
| delete | delete | host form (no native word yet) |
| explicit | explicit | host form (no native word yet) |
| false | അസത്യം | lexicon |
| friend | friend | host form (no native word yet) |
| mutable | mutable | host form (no native word yet) |
| namespace | നാമാകാശ | lexicon |
| new | പുതിയ | lexicon |
| nullptr | nullptr | host form (no native word yet) |
| operator | operator | host form (no native word yet) |
| private | സ്വകാര്യ | lexicon |
| protected | സംരക്ഷിത | lexicon |
| public | പൊതു | lexicon |
| template | template | host form (no native word yet) |
| this | ഇത് | lexicon |
| throw | എറിയുക | lexicon |
| true | സത്യം | lexicon |
| try | ശ്രമിക്കുക | lexicon |
| typename | typename | host form (no native word yet) |
| using | using | host form (no native word yet) |
| virtual | മായാ | lexicon |
| cout | cout | host form (no native word yet) |
| cin | cin | host form (no native word yet) |
| endl | endl | host form (no native word yet) |

Standard library and runtime names of the C++ binding:

| Host | Malayalam | Source |
|---|---|---|
| NULL | ശൂന്യ | lexicon |
| assert | പ്രതിജ്ഞാ | lexicon |
| free | സ്വതന്ത്രം | lexicon |
| pipe | പ്രണാല | lexicon |
| raise | ഉയർത്തുക | lexicon |
| read | പഠ | lexicon |
| signal | സൂചന | lexicon |
| sleep | സുഷുപ്തി | lexicon |
| sync | സമന്വയം | lexicon |
| write | ലിഖ | lexicon |

### A.4 Java

Host: The Java Language Specification, Oracle, current edition. Names: unchanged.

| Host | Malayalam | Source |
|---|---|---|
| abstract | അമൂർത്ത | lexicon |
| assert | പ്രതിജ്ഞാ | lexicon |
| boolean | boolean | host form (no native word yet) |
| break | നിർത്തുക | lexicon |
| byte | byte | host form (no native word yet) |
| case | അവസ്ഥ | lexicon |
| catch | പിടിക്കുക | lexicon |
| char | അക്ഷരം | lexicon |
| class | വർഗ്ഗം | lexicon |
| continue | തുടരുക | lexicon |
| default | സ്ഥിരസ്ഥിതി | lexicon |
| do | ചെയ്യുക | lexicon |
| double | ഇരട്ട | lexicon |
| else | അല്ലെങ്കിൽ | lexicon |
| enum | എണ്ണൽ | lexicon |
| extends | വിപുലീകരിക്കുക | lexicon |
| final | final | host form (no native word yet) |
| finally | അവസാനമായി | lexicon |
| float | ദശാംശം | lexicon |
| for | വേണ്ടി | lexicon |
| if | എങ്കിൽ | lexicon |
| implements | നടപ്പാക്കുക | lexicon |
| import | ഇറക്കുമതി | lexicon |
| instanceof | instanceof | host form (no native word yet) |
| int | പൂർണ്ണസംഖ്യ | lexicon |
| interface | സമ്പർക്കമുഖം | lexicon |
| long | long | host form (no native word yet) |
| native | native | host form (no native word yet) |
| new | പുതിയ | lexicon |
| package | പൊതി | lexicon |
| private | സ്വകാര്യ | lexicon |
| protected | സംരക്ഷിത | lexicon |
| public | പൊതു | lexicon |
| return | തിരികെ | lexicon |
| short | short | host form (no native word yet) |
| static | സ്ഥിതം | lexicon |
| super | പരം | lexicon |
| switch | തിരഞ്ഞെടുപ്പ് | lexicon |
| synchronized | synchronized | host form (no native word yet) |
| this | ഇത് | lexicon |
| throw | എറിയുക | lexicon |
| throws | throws | host form (no native word yet) |
| try | ശ്രമിക്കുക | lexicon |
| void | ശൂന്യം | lexicon |
| volatile | അസ്ഥിര | lexicon |
| while | ആകുമ്പോൾ | lexicon |
| true | സത്യം | lexicon |
| false | അസത്യം | lexicon |
| null | ശൂന്യ | lexicon |
| String | വാക്യം | lexicon |
| System | System | host form (no native word yet) |

Standard library and runtime names of the Java binding:

| Host | Malayalam | Source |
|---|---|---|
| Object | വസ്തു | lexicon |
| Thread | നൂൽ | lexicon |
| const | സ്ഥിരം | lexicon |
| extern | ബാഹ്യ | lexicon |
| free | സ്വതന്ത്രം | lexicon |
| goto | പോകുക | lexicon |
| inline | വരിയിൽ | lexicon |
| main | പ്രധാന | lexicon |
| raise | ഉയർത്തുക | lexicon |
| read | പഠ | lexicon |
| register | രജിസ്റ്റർ | lexicon |
| signal | സൂചന | lexicon |
| sizeof | വലുപ്പം | lexicon |
| sleep | സുഷുപ്തി | lexicon |
| struct | ഘടന | lexicon |
| typedef | തരനിർവചനം | lexicon |
| union | സംഘം | lexicon |
| virtual | മായാ | lexicon |
| write | ലിഖ | lexicon |

### A.5 Python

Host: The Python Language Reference, Python Software Foundation, current version. Names: unchanged.

| Host | Malayalam | Source |
|---|---|---|
| False | അസത്യം | lexicon |
| None | None | host form (no native word yet) |
| True | സത്യം | lexicon |
| and | ഒപ്പം | lexicon |
| as | ഇവ | lexicon |
| assert | പ്രതിജ്ഞാ | lexicon |
| break | നിർത്തുക | lexicon |
| class | വർഗ്ഗം | lexicon |
| continue | തുടരുക | lexicon |
| def | def | host form (no native word yet) |
| del | del | host form (no native word yet) |
| elif | അല്ലെങ്കിലെങ്കിൽ | lexicon |
| else | അല്ലെങ്കിൽ | lexicon |
| except | അപവാദം | lexicon |
| finally | അവസാനമായി | lexicon |
| for | വേണ്ടി | lexicon |
| from | തഃ | lexicon |
| global | വൈശ്വിക | lexicon |
| if | എങ്കിൽ | lexicon |
| import | ഇറക്കുമതി | lexicon |
| in | ഇൽ | lexicon |
| is | is | host form (no native word yet) |
| lambda | അജ്ഞാത | lexicon |
| nonlocal | nonlocal | host form (no native word yet) |
| not | അല്ല | lexicon |
| or | അഥവാ | lexicon |
| pass | pass | host form (no native word yet) |
| raise | ഉയർത്തുക | lexicon |
| return | തിരികെ | lexicon |
| try | ശ്രമിക്കുക | lexicon |
| while | ആകുമ്പോൾ | lexicon |
| with | with | host form (no native word yet) |
| yield | നൽകുക | lexicon |
| print | print | host form (no native word yet) |
| range | range | host form (no native word yet) |
| len | len | host form (no native word yet) |

Standard library and runtime names of the Python binding:

| Host | Malayalam | Source |
|---|---|---|
| Object | വസ്തു | lexicon |
| String | വാക്യം | lexicon |
| Thread | നൂൽ | lexicon |
| abstract | അമൂർത്ത | lexicon |
| case | അവസ്ഥ | lexicon |
| catch | പിടിക്കുക | lexicon |
| char | അക്ഷരം | lexicon |
| const | സ്ഥിരം | lexicon |
| default | സ്ഥിരസ്ഥിതി | lexicon |
| do | ചെയ്യുക | lexicon |
| double | ഇരട്ട | lexicon |
| extends | വിപുലീകരിക്കുക | lexicon |
| float | ദശാംശം | lexicon |
| goto | പോകുക | lexicon |
| implements | നടപ്പാക്കുക | lexicon |
| int | പൂർണ്ണസംഖ്യ | lexicon |
| interface | സമ്പർക്കമുഖം | lexicon |
| main | പ്രധാന | lexicon |
| new | പുതിയ | lexicon |
| package | പൊതി | lexicon |
| private | സ്വകാര്യ | lexicon |
| protected | സംരക്ഷിത | lexicon |
| public | പൊതു | lexicon |
| read | പഠ | lexicon |
| sleep | സുഷുപ്തി | lexicon |
| static | സ്ഥിതം | lexicon |
| super | പരം | lexicon |
| switch | തിരഞ്ഞെടുപ്പ് | lexicon |
| this | ഇത് | lexicon |
| throw | എറിയുക | lexicon |
| void | ശൂന്യം | lexicon |
| volatile | അസ്ഥിര | lexicon |
| write | ലിഖ | lexicon |

### A.6 BASIC

Host: ISO/IEC 10279, Information technology, Programming languages, Full BASIC. Names: name transformation.

| Host | Malayalam | Source |
|---|---|---|
| dim | dim | host form (no native word yet) |
| end | അവസാനം | lexicon |
| for | വേണ്ടി | lexicon |
| gosub | gosub | host form (no native word yet) |
| goto | പോകുക | lexicon |
| if | എങ്കിൽ | lexicon |
| input | input | host form (no native word yet) |
| let | ആകട്ടെ | lexicon |
| next | next | host form (no native word yet) |
| print | print | host form (no native word yet) |
| rem | rem | host form (no native word yet) |
| return | തിരികെ | lexicon |
| step | step | host form (no native word yet) |
| then | then | host form (no native word yet) |
| to | to | host form (no native word yet) |
| wend | wend | host form (no native word yet) |
| while | ആകുമ്പോൾ | lexicon |
| and | ഒപ്പം | lexicon |
| or | അഥവാ | lexicon |
| not | അല്ല | lexicon |
| mod | mod | host form (no native word yet) |

Standard library and runtime names of the BASIC binding:

| Host | Malayalam | Source |
|---|---|---|
| AS | ഇവ | lexicon |
| CALL | വിളിക്കുക | lexicon |
| CONST | സ്ഥിരം | lexicon |
| DO | ചെയ്യുക | lexicon |
| ELSE | അല്ലെങ്കിൽ | lexicon |
| INT | പൂർണ്ണസംഖ്യ | lexicon |
| SHARED | സഹഭാജിത | lexicon |
| STATIC | സ്ഥിതം | lexicon |
| STRING | വാക്യം | lexicon |
| TIMER | കാലയന്ത്ര | lexicon |

### A.7 LOGO

Host: No international standard; the host is the Berkeley Logo dialect (bibliography). Names: name transformation.

| Host | Malayalam | Source |
|---|---|---|
| forward | അഗ്രപ്രസാര | lexicon |
| back | back | host form (no native word yet) |
| left | left | host form (no native word yet) |
| right | right | host form (no native word yet) |
| penup | penup | host form (no native word yet) |
| pendown | pendown | host form (no native word yet) |
| repeat | repeat | host form (no native word yet) |
| to | to | host form (no native word yet) |
| end | അവസാനം | lexicon |
| make | make | host form (no native word yet) |
| if | എങ്കിൽ | lexicon |
| ifelse | ifelse | host form (no native word yet) |
| home | home | host form (no native word yet) |
| clearscreen | clearscreen | host form (no native word yet) |

## Annex B (informative) Coverage and review

| Binding | Host keywords with a native word | Library names |
|---|---|---|
| C | 29 of 35 | 11 |
| C preprocessor | 4 of 12 | 0 |
| C++ | 43 of 61 | 10 |
| Java | 41 of 51 | 19 |
| Python | 26 of 36 | 33 |
| BASIC | 10 of 21 | 10 |
| LOGO | 3 of 14 | 0 |

The lowering of Malayalam programs to C is verified by the reference implementation: does not compile. Source Chintamani means a word of the original Hindawi transducers; lexicon, a word of the language's lexicon; proposed, a word proposed by the project and not yet reviewed by the language community.

## Annex C (normative) Script filter

The script filter maps each letter and sign of the script to the Devanagari letter or sign of the same Unicode name, as generated by lang/hindawi/tools/script_filters.py.

## Annex D (informative) Rights and provenance

This document is an original work. It defines new programming languages by reference to the host language standards listed in Clause 2 and reproduces no text from them. Permission to adopt, translate or publish it as a standard is given by the copyright holder to a standards body on request.

Single words and the keywords of the host languages are not reproduced from any copyrighted text; the native words of Annex A were chosen by the Hindawi project, taken from the language's lexicon in the Hindawi repository, or, for Hindi, taken from the Chintamani transducers of the original Hindawi, whose author holds their copyright.

## Bibliography

- Hindawi 2026.10, hindawiai/hindawi2026.10, the reference implementation
- Chintamani, hindawiai/chintamani, the Hindawi transducers and the Romenagri tools
- Berkeley Logo reference manual, Brian Harvey

