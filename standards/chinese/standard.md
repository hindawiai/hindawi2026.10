# HLS zh 2026.10

**Chinese bindings for programming languages: lexical mapping and lowering to the host standards**

Edition 2026.10, working draft, 2026-10-18. © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

## Foreword

This document was prepared by AyeAI, Hindawi project (Project ILM). It is generated from the Chinese cell of Hindawi 2026.10 by lang/hindawi/tools/standards.py, so that the published standard and the reference implementation cannot drift apart. Its stage is a working draft: the words marked proposed in Annex A await review by the Chinese language community, through the review pages of the Hindawi project.

## Introduction

This document lets programs be written in Chinese, in the Cjk script, in each of the programming languages listed in Clause 1. Each binding is a programming language in its own right, Chinese C for example, whose programs are lowered by the function defined in Clause 6 to programs of the host language, and are then processed by any conforming implementation of the host standard. The host standards are incorporated by reference and are not restated. Names keep a defined form down to object code (Clause 7), so programs written in Chinese remain debuggable at the level of firmware, kernels and libraries.

## 1 Scope

This document specifies, for the Chinese language written in the Cjk script, bindings to the following host programming languages: C, C preprocessor, C++, Java, Python, BASIC, LOGO. For each binding it specifies the native keywords and directives, the lowering of native programs to host programs, the treatment of names, and the requirements for conformance.

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

- binding: programming language defined by this document whose programs are written in Chinese and lowered to one host language

- native keyword: word of this document that stands for one keyword, directive or standard library name of a host language

- lowering: function from native programs to host programs defined in Clause 6

- raising: inverse of lowering applied to a host program with a dictionary of names, giving back the native program exactly

- name transformation: function from native names to host identifiers defined in Clause 7

- C-level form: result of the name transformation; the form a native name takes in host source and in object code

## 4 Conformance

A conforming Chinese program of a binding shall be a text that meets Clause 5 and whose lowering is a conforming program of the host language.

A conforming implementation of a binding shall accept every conforming program of that binding and shall behave as the lowering of the program, processed by a conforming implementation of the host language, behaves.

An implementation that raises host programs into a binding shall produce native programs whose lowering, with the same dictionary of names, is identical to the host program it raised.

## 5 Character set and encoding

A native program shall be encoded in UTF-8 and shall be in Normalization Form C. Native keywords and names are written in the Cjk script, whose direction is left to right. Numeric literals are written with the digits 0 to 9 (U+0030 to U+0039). A native keyword written as several words is one token, its words joined by LOW LINE (U+005F).

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

| Host | Chinese | Source |
|---|---|---|
| auto | auto | host form (no native word yet) |
| break | break | host form (no native word yet) |
| case | case | host form (no native word yet) |
| char | char | host form (no native word yet) |
| const | const | host form (no native word yet) |
| continue | continue | host form (no native word yet) |
| default | default | host form (no native word yet) |
| do | do | host form (no native word yet) |
| double | double | host form (no native word yet) |
| else | 否则 | lexicon |
| enum | enum | host form (no native word yet) |
| extern | extern | host form (no native word yet) |
| float | float | host form (no native word yet) |
| for | 为 | lexicon |
| goto | goto | host form (no native word yet) |
| if | 如果 | lexicon |
| inline | inline | host form (no native word yet) |
| int | 整数 | lexicon |
| long | long | host form (no native word yet) |
| register | register | host form (no native word yet) |
| restrict | restrict | host form (no native word yet) |
| return | 返回 | lexicon |
| short | short | host form (no native word yet) |
| signed | signed | host form (no native word yet) |
| sizeof | sizeof | host form (no native word yet) |
| static | static | host form (no native word yet) |
| struct | struct | host form (no native word yet) |
| switch | switch | host form (no native word yet) |
| typedef | typedef | host form (no native word yet) |
| union | union | host form (no native word yet) |
| unsigned | unsigned | host form (no native word yet) |
| void | void | host form (no native word yet) |
| volatile | volatile | host form (no native word yet) |
| while | 当 | lexicon |
| main | 主要 | lexicon |

### A.2 C preprocessor

Host: ISO/IEC 9899, Information technology, Programming languages, C (preprocessing directives). Names: name transformation.

| Host | Chinese | Source |
|---|---|---|
| #define | #define | host form (no native word yet) |
| #include | #include | host form (no native word yet) |
| #if | #如果 | lexicon |
| #ifdef | #ifdef | host form (no native word yet) |
| #ifndef | #ifndef | host form (no native word yet) |
| #else | #否则 | lexicon |
| #elif | #elif | host form (no native word yet) |
| #endif | #endif | host form (no native word yet) |
| #undef | #undef | host form (no native word yet) |
| #pragma | #pragma | host form (no native word yet) |
| #error | #error | host form (no native word yet) |
| #line | #line | host form (no native word yet) |

### A.3 C++

Host: ISO/IEC 14882, Programming languages, C++. Names: name transformation.

| Host | Chinese | Source |
|---|---|---|
| auto | auto | host form (no native word yet) |
| break | break | host form (no native word yet) |
| case | case | host form (no native word yet) |
| char | char | host form (no native word yet) |
| const | const | host form (no native word yet) |
| continue | continue | host form (no native word yet) |
| default | default | host form (no native word yet) |
| do | do | host form (no native word yet) |
| double | double | host form (no native word yet) |
| else | 否则 | lexicon |
| enum | enum | host form (no native word yet) |
| extern | extern | host form (no native word yet) |
| float | float | host form (no native word yet) |
| for | 为 | lexicon |
| goto | goto | host form (no native word yet) |
| if | 如果 | lexicon |
| inline | inline | host form (no native word yet) |
| int | 整数 | lexicon |
| long | long | host form (no native word yet) |
| register | register | host form (no native word yet) |
| restrict | restrict | host form (no native word yet) |
| return | 返回 | lexicon |
| short | short | host form (no native word yet) |
| signed | signed | host form (no native word yet) |
| sizeof | sizeof | host form (no native word yet) |
| static | static | host form (no native word yet) |
| struct | struct | host form (no native word yet) |
| switch | switch | host form (no native word yet) |
| typedef | typedef | host form (no native word yet) |
| union | union | host form (no native word yet) |
| unsigned | unsigned | host form (no native word yet) |
| void | void | host form (no native word yet) |
| volatile | volatile | host form (no native word yet) |
| while | 当 | lexicon |
| main | 主要 | lexicon |
| bool | bool | host form (no native word yet) |
| catch | catch | host form (no native word yet) |
| class | class | host form (no native word yet) |
| delete | delete | host form (no native word yet) |
| explicit | explicit | host form (no native word yet) |
| false | false | host form (no native word yet) |
| friend | friend | host form (no native word yet) |
| mutable | mutable | host form (no native word yet) |
| namespace | namespace | host form (no native word yet) |
| new | new | host form (no native word yet) |
| nullptr | nullptr | host form (no native word yet) |
| operator | operator | host form (no native word yet) |
| private | private | host form (no native word yet) |
| protected | protected | host form (no native word yet) |
| public | public | host form (no native word yet) |
| template | template | host form (no native word yet) |
| this | this | host form (no native word yet) |
| throw | throw | host form (no native word yet) |
| true | true | host form (no native word yet) |
| try | try | host form (no native word yet) |
| typename | typename | host form (no native word yet) |
| using | using | host form (no native word yet) |
| virtual | virtual | host form (no native word yet) |
| cout | cout | host form (no native word yet) |
| cin | cin | host form (no native word yet) |
| endl | endl | host form (no native word yet) |

### A.4 Java

Host: The Java Language Specification, Oracle, current edition. Names: unchanged.

| Host | Chinese | Source |
|---|---|---|
| abstract | abstract | host form (no native word yet) |
| assert | assert | host form (no native word yet) |
| boolean | boolean | host form (no native word yet) |
| break | break | host form (no native word yet) |
| byte | byte | host form (no native word yet) |
| case | case | host form (no native word yet) |
| catch | catch | host form (no native word yet) |
| char | char | host form (no native word yet) |
| class | class | host form (no native word yet) |
| continue | continue | host form (no native word yet) |
| default | default | host form (no native word yet) |
| do | do | host form (no native word yet) |
| double | double | host form (no native word yet) |
| else | 否则 | lexicon |
| enum | enum | host form (no native word yet) |
| extends | extends | host form (no native word yet) |
| final | final | host form (no native word yet) |
| finally | finally | host form (no native word yet) |
| float | float | host form (no native word yet) |
| for | 为 | lexicon |
| if | 如果 | lexicon |
| implements | implements | host form (no native word yet) |
| import | import | host form (no native word yet) |
| instanceof | instanceof | host form (no native word yet) |
| int | 整数 | lexicon |
| interface | interface | host form (no native word yet) |
| long | long | host form (no native word yet) |
| native | native | host form (no native word yet) |
| new | new | host form (no native word yet) |
| package | package | host form (no native word yet) |
| private | private | host form (no native word yet) |
| protected | protected | host form (no native word yet) |
| public | public | host form (no native word yet) |
| return | 返回 | lexicon |
| short | short | host form (no native word yet) |
| static | static | host form (no native word yet) |
| super | super | host form (no native word yet) |
| switch | switch | host form (no native word yet) |
| synchronized | synchronized | host form (no native word yet) |
| this | this | host form (no native word yet) |
| throw | throw | host form (no native word yet) |
| throws | throws | host form (no native word yet) |
| try | try | host form (no native word yet) |
| void | void | host form (no native word yet) |
| volatile | volatile | host form (no native word yet) |
| while | 当 | lexicon |
| true | true | host form (no native word yet) |
| false | false | host form (no native word yet) |
| null | null | host form (no native word yet) |
| String | String | host form (no native word yet) |
| System | System | host form (no native word yet) |

Standard library and runtime names of the Java binding:

| Host | Chinese | Source |
|---|---|---|
| main | 主要 | lexicon |

### A.5 Python

Host: The Python Language Reference, Python Software Foundation, current version. Names: unchanged.

| Host | Chinese | Source |
|---|---|---|
| False | False | host form (no native word yet) |
| None | None | host form (no native word yet) |
| True | True | host form (no native word yet) |
| and | and | host form (no native word yet) |
| as | as | host form (no native word yet) |
| assert | assert | host form (no native word yet) |
| break | break | host form (no native word yet) |
| class | class | host form (no native word yet) |
| continue | continue | host form (no native word yet) |
| def | def | host form (no native word yet) |
| del | del | host form (no native word yet) |
| elif | elif | host form (no native word yet) |
| else | 否则 | lexicon |
| except | except | host form (no native word yet) |
| finally | finally | host form (no native word yet) |
| for | 为 | lexicon |
| from | from | host form (no native word yet) |
| global | global | host form (no native word yet) |
| if | 如果 | lexicon |
| import | import | host form (no native word yet) |
| in | in | host form (no native word yet) |
| is | is | host form (no native word yet) |
| lambda | lambda | host form (no native word yet) |
| nonlocal | nonlocal | host form (no native word yet) |
| not | not | host form (no native word yet) |
| or | or | host form (no native word yet) |
| pass | pass | host form (no native word yet) |
| raise | raise | host form (no native word yet) |
| return | 返回 | lexicon |
| try | try | host form (no native word yet) |
| while | 当 | lexicon |
| with | with | host form (no native word yet) |
| yield | yield | host form (no native word yet) |
| print | print | host form (no native word yet) |
| range | range | host form (no native word yet) |
| len | len | host form (no native word yet) |

Standard library and runtime names of the Python binding:

| Host | Chinese | Source |
|---|---|---|
| int | 整数 | lexicon |
| main | 主要 | lexicon |

### A.6 BASIC

Host: ISO/IEC 10279, Information technology, Programming languages, Full BASIC. Names: name transformation.

| Host | Chinese | Source |
|---|---|---|
| dim | dim | host form (no native word yet) |
| end | end | host form (no native word yet) |
| for | 为 | lexicon |
| gosub | gosub | host form (no native word yet) |
| goto | goto | host form (no native word yet) |
| if | 如果 | lexicon |
| input | input | host form (no native word yet) |
| let | let | host form (no native word yet) |
| next | next | host form (no native word yet) |
| print | print | host form (no native word yet) |
| rem | rem | host form (no native word yet) |
| return | 返回 | lexicon |
| step | step | host form (no native word yet) |
| then | then | host form (no native word yet) |
| to | to | host form (no native word yet) |
| wend | wend | host form (no native word yet) |
| while | 当 | lexicon |
| and | and | host form (no native word yet) |
| or | or | host form (no native word yet) |
| not | not | host form (no native word yet) |
| mod | mod | host form (no native word yet) |

Standard library and runtime names of the BASIC binding:

| Host | Chinese | Source |
|---|---|---|
| ELSE | 否则 | lexicon |
| INT | 整数 | lexicon |

### A.7 LOGO

Host: No international standard; the host is the Berkeley Logo dialect (bibliography). Names: name transformation.

| Host | Chinese | Source |
|---|---|---|
| forward | forward | host form (no native word yet) |
| back | back | host form (no native word yet) |
| left | left | host form (no native word yet) |
| right | right | host form (no native word yet) |
| penup | penup | host form (no native word yet) |
| pendown | pendown | host form (no native word yet) |
| repeat | repeat | host form (no native word yet) |
| to | to | host form (no native word yet) |
| end | end | host form (no native word yet) |
| make | make | host form (no native word yet) |
| if | 如果 | lexicon |
| ifelse | ifelse | host form (no native word yet) |
| home | home | host form (no native word yet) |
| clearscreen | clearscreen | host form (no native word yet) |

## Annex B (informative) Coverage and review

| Binding | Host keywords with a native word | Library names |
|---|---|---|
| C | 7 of 35 | 0 |
| C preprocessor | 2 of 12 | 0 |
| C++ | 7 of 61 | 0 |
| Java | 6 of 51 | 1 |
| Python | 5 of 36 | 2 |
| BASIC | 4 of 21 | 2 |
| LOGO | 1 of 14 | 0 |

The lowering of Chinese programs to C is verified by the reference implementation: no filter yet. Source Chintamani means a word of the original Hindawi transducers; lexicon, a word of the language's lexicon; proposed, a word proposed by the project and not yet reviewed by the language community.

## Annex C (normative) Script filter

The script filter maps each letter and sign of the script to the Devanagari letter or sign of the same Unicode name, as generated by lang/hindawi/tools/script_filters.py.

## Annex D (informative) Rights and provenance

This document is an original work. It defines new programming languages by reference to the host language standards listed in Clause 2 and reproduces no text from them. Permission to adopt, translate or publish it as a standard is given by the copyright holder to a standards body on request.

Single words and the keywords of the host languages are not reproduced from any copyrighted text; the native words of Annex A were chosen by the Hindawi project, taken from the language's lexicon in the Hindawi repository, or, for Hindi, taken from the Chintamani transducers of the original Hindawi, whose author holds their copyright.

## Bibliography

- Hindawi 2026.10, hindawiai/hindawi2026.10, the reference implementation
- Chintamani, hindawiai/chintamani, the Hindawi transducers and the Romenagri tools
- Berkeley Logo reference manual, Brian Harvey

