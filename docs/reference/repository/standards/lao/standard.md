# HLS lo 2026.10

**Lao bindings for programming languages: lexical mapping and lowering to the host standards**

Edition 2026.10, working draft, 2026-10-18. © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

## Foreword

This document was prepared by AyeAI, Hindawi project (Project ILM). It is generated from the Lao cell of Hindawi 2026.10 by lang/hindawi/tools/standards.py, so that the published standard and the reference implementation cannot drift apart. Its stage is a working draft: the words marked proposed in Annex A await review by the Lao language community, through the review pages of the Hindawi project.

## Introduction

This document lets programs be written in Lao, in the Lao script, in each of the programming languages listed in Clause 1. Each binding is a programming language in its own right, Lao C for example, whose programs are lowered by the function defined in Clause 6 to programs of the host language, and are then processed by any conforming implementation of the host standard. The host standards are incorporated by reference and are not restated. Names keep a defined form down to object code (Clause 7), so programs written in Lao remain debuggable at the level of firmware, kernels and libraries.

## 1 Scope

This document specifies, for the Lao language written in the Lao script, bindings to the following host programming languages: C, C preprocessor, C++, Java, Python, BASIC, LOGO. For each binding it specifies the native keywords and directives, the lowering of native programs to host programs, the treatment of names, and the requirements for conformance.

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

- binding: programming language defined by this document whose programs are written in Lao and lowered to one host language

- native keyword: word of this document that stands for one keyword, directive or standard library name of a host language

- lowering: function from native programs to host programs defined in Clause 6

- raising: inverse of lowering applied to a host program with a dictionary of names, giving back the native program exactly

- name transformation: function from native names to host identifiers defined in Clause 7

- C-level form: result of the name transformation; the form a native name takes in host source and in object code

## 4 Conformance

A conforming Lao program of a binding shall be a text that meets Clause 5 and whose lowering is a conforming program of the host language.

A conforming implementation of a binding shall accept every conforming program of that binding and shall behave as the lowering of the program, processed by a conforming implementation of the host language, behaves.

An implementation that raises host programs into a binding shall produce native programs whose lowering, with the same dictionary of names, is identical to the host program it raised.

## 5 Character set and encoding

A native program shall be encoded in UTF-8 and shall be in Normalization Form C. Native keywords and names are written in the Lao script, whose direction is left to right. Numeric literals are written with the digits 0 to 9 (U+0030 to U+0039). A native keyword written as several words is one token, its words joined by LOW LINE (U+005F).

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

| Host | Lao | Source |
|---|---|---|
| auto | auto | host form (no native word yet) |
| break | bha_nga | lexicon |
| case | pak_sa | lexicon |
| char | var_na | lexicon |
| const | const | host form (no native word yet) |
| continue | continue | host form (no native word yet) |
| default | default | host form (no native word yet) |
| do | do | host form (no native word yet) |
| double | dviguu_na | lexicon |
| else | ບໍ່ດັ່ງນັ້ນ | lexicon |
| enum | ga_nanaa | lexicon |
| extern | extern | host form (no native word yet) |
| float | float | host form (no native word yet) |
| for | ສຳລັບ | lexicon |
| goto | goto | host form (no native word yet) |
| if | ຖ້າ | lexicon |
| inline | anta_hstha | lexicon |
| int | ຈຳນວນເຕັມ | lexicon |
| long | long | host form (no native word yet) |
| register | pa_njikaa | lexicon |
| restrict | restrict | host form (no native word yet) |
| return | ສົ່ງຄືນ | lexicon |
| short | short | host form (no native word yet) |
| signed | signed | host form (no native word yet) |
| sizeof | parimaa_na | lexicon |
| static | static | host form (no native word yet) |
| struct | sa_nracanaa | lexicon |
| switch | switch | host form (no native word yet) |
| typedef | typedef | host form (no native word yet) |
| union | sa_ngha | lexicon |
| unsigned | unsigned | host form (no native word yet) |
| void | void | host form (no native word yet) |
| volatile | ca_ncala | lexicon |
| while | ໃນຂະນະທີ່ | lexicon |
| main | main | host form (no native word yet) |

Standard library and runtime names of the C binding:

| Host | Lao | Source |
|---|---|---|
| protected | rak_sita | lexicon |
| signal | sa_nkeeta | lexicon |

### A.2 C preprocessor

Host: ISO/IEC 9899, Information technology, Programming languages, C (preprocessing directives). Names: name transformation.

| Host | Lao | Source |
|---|---|---|
| #define | #define | host form (no native word yet) |
| #include | #include | host form (no native word yet) |
| #if | #ຖ້າ | lexicon |
| #ifdef | #ifdef | host form (no native word yet) |
| #ifndef | #ifndef | host form (no native word yet) |
| #else | #ບໍ່ດັ່ງນັ້ນ | lexicon |
| #elif | #elif | host form (no native word yet) |
| #endif | #endif | host form (no native word yet) |
| #undef | #undef | host form (no native word yet) |
| #pragma | #pragma | host form (no native word yet) |
| #error | #error | host form (no native word yet) |
| #line | #line | host form (no native word yet) |

### A.3 C++

Host: ISO/IEC 14882, Programming languages, C++. Names: name transformation.

| Host | Lao | Source |
|---|---|---|
| auto | auto | host form (no native word yet) |
| break | bha_nga | lexicon |
| case | pak_sa | lexicon |
| char | var_na | lexicon |
| const | const | host form (no native word yet) |
| continue | continue | host form (no native word yet) |
| default | default | host form (no native word yet) |
| do | do | host form (no native word yet) |
| double | dviguu_na | lexicon |
| else | ບໍ່ດັ່ງນັ້ນ | lexicon |
| enum | ga_nanaa | lexicon |
| extern | extern | host form (no native word yet) |
| float | float | host form (no native word yet) |
| for | ສຳລັບ | lexicon |
| goto | goto | host form (no native word yet) |
| if | ຖ້າ | lexicon |
| inline | anta_hstha | lexicon |
| int | ຈຳນວນເຕັມ | lexicon |
| long | long | host form (no native word yet) |
| register | pa_njikaa | lexicon |
| restrict | restrict | host form (no native word yet) |
| return | ສົ່ງຄືນ | lexicon |
| short | short | host form (no native word yet) |
| signed | signed | host form (no native word yet) |
| sizeof | parimaa_na | lexicon |
| static | static | host form (no native word yet) |
| struct | sa_nracanaa | lexicon |
| switch | switch | host form (no native word yet) |
| typedef | typedef | host form (no native word yet) |
| union | sa_ngha | lexicon |
| unsigned | unsigned | host form (no native word yet) |
| void | void | host form (no native word yet) |
| volatile | ca_ncala | lexicon |
| while | ໃນຂະນະທີ່ | lexicon |
| main | main | host form (no native word yet) |
| bool | bool | host form (no native word yet) |
| catch | gr_haa_na | lexicon |
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
| protected | rak_sita | lexicon |
| public | public | host form (no native word yet) |
| template | template | host form (no native word yet) |
| this | this | host form (no native word yet) |
| throw | k_sipa | lexicon |
| true | true | host form (no native word yet) |
| try | try | host form (no native word yet) |
| typename | typename | host form (no native word yet) |
| using | using | host form (no native word yet) |
| virtual | virtual | host form (no native word yet) |
| cout | cout | host form (no native word yet) |
| cin | cin | host form (no native word yet) |
| endl | endl | host form (no native word yet) |

Standard library and runtime names of the C++ binding:

| Host | Lao | Source |
|---|---|---|
| pipe | pra_naala | lexicon |
| signal | sa_nkeeta | lexicon |
| sleep | su_supti | lexicon |

### A.4 Java

Host: The Java Language Specification, Oracle, current edition. Names: unchanged.

| Host | Lao | Source |
|---|---|---|
| abstract | abstract | host form (no native word yet) |
| assert | assert | host form (no native word yet) |
| boolean | boolean | host form (no native word yet) |
| break | bha_nga | lexicon |
| byte | byte | host form (no native word yet) |
| case | pak_sa | lexicon |
| catch | gr_haa_na | lexicon |
| char | var_na | lexicon |
| class | class | host form (no native word yet) |
| continue | continue | host form (no native word yet) |
| default | default | host form (no native word yet) |
| do | do | host form (no native word yet) |
| double | dviguu_na | lexicon |
| else | ບໍ່ດັ່ງນັ້ນ | lexicon |
| enum | ga_nanaa | lexicon |
| extends | vistr_ta | lexicon |
| final | final | host form (no native word yet) |
| finally | antata_h | lexicon |
| float | float | host form (no native word yet) |
| for | ສຳລັບ | lexicon |
| if | ຖ້າ | lexicon |
| implements | ni_spaadita | lexicon |
| import | import | host form (no native word yet) |
| instanceof | instanceof | host form (no native word yet) |
| int | ຈຳນວນເຕັມ | lexicon |
| interface | interface | host form (no native word yet) |
| long | long | host form (no native word yet) |
| native | native | host form (no native word yet) |
| new | new | host form (no native word yet) |
| package | package | host form (no native word yet) |
| private | private | host form (no native word yet) |
| protected | rak_sita | lexicon |
| public | public | host form (no native word yet) |
| return | ສົ່ງຄືນ | lexicon |
| short | short | host form (no native word yet) |
| static | static | host form (no native word yet) |
| super | super | host form (no native word yet) |
| switch | switch | host form (no native word yet) |
| synchronized | synchronized | host form (no native word yet) |
| this | this | host form (no native word yet) |
| throw | k_sipa | lexicon |
| throws | throws | host form (no native word yet) |
| try | try | host form (no native word yet) |
| void | void | host form (no native word yet) |
| volatile | ca_ncala | lexicon |
| while | ໃນຂະນະທີ່ | lexicon |
| true | true | host form (no native word yet) |
| false | false | host form (no native word yet) |
| null | null | host form (no native word yet) |
| String | String | host form (no native word yet) |
| System | System | host form (no native word yet) |

Standard library and runtime names of the Java binding:

| Host | Lao | Source |
|---|---|---|
| inline | anta_hstha | lexicon |
| register | pa_njikaa | lexicon |
| signal | sa_nkeeta | lexicon |
| sizeof | parimaa_na | lexicon |
| sleep | su_supti | lexicon |
| struct | sa_nracanaa | lexicon |
| union | sa_ngha | lexicon |

### A.5 Python

Host: The Python Language Reference, Python Software Foundation, current version. Names: unchanged.

| Host | Lao | Source |
|---|---|---|
| False | False | host form (no native word yet) |
| None | None | host form (no native word yet) |
| True | True | host form (no native word yet) |
| and | ca | lexicon |
| as | as | host form (no native word yet) |
| assert | assert | host form (no native word yet) |
| break | bha_nga | lexicon |
| class | class | host form (no native word yet) |
| continue | continue | host form (no native word yet) |
| def | def | host form (no native word yet) |
| del | del | host form (no native word yet) |
| elif | elif | host form (no native word yet) |
| else | ບໍ່ດັ່ງນັ້ນ | lexicon |
| except | except | host form (no native word yet) |
| finally | antata_h | lexicon |
| for | ສຳລັບ | lexicon |
| from | ta_h | lexicon |
| global | global | host form (no native word yet) |
| if | ຖ້າ | lexicon |
| import | import | host form (no native word yet) |
| in | anta_h | lexicon |
| is | is | host form (no native word yet) |
| lambda | lambda | host form (no native word yet) |
| nonlocal | nonlocal | host form (no native word yet) |
| not | na | lexicon |
| or | or | host form (no native word yet) |
| pass | pass | host form (no native word yet) |
| raise | raise | host form (no native word yet) |
| return | ສົ່ງຄືນ | lexicon |
| try | try | host form (no native word yet) |
| while | ໃນຂະນະທີ່ | lexicon |
| with | with | host form (no native word yet) |
| yield | yield | host form (no native word yet) |
| print | print | host form (no native word yet) |
| range | range | host form (no native word yet) |
| len | len | host form (no native word yet) |

Standard library and runtime names of the Python binding:

| Host | Lao | Source |
|---|---|---|
| case | pak_sa | lexicon |
| catch | gr_haa_na | lexicon |
| char | var_na | lexicon |
| double | dviguu_na | lexicon |
| extends | vistr_ta | lexicon |
| implements | ni_spaadita | lexicon |
| int | ຈຳນວນເຕັມ | lexicon |
| protected | rak_sita | lexicon |
| sleep | su_supti | lexicon |
| throw | k_sipa | lexicon |
| volatile | ca_ncala | lexicon |

### A.6 BASIC

Host: ISO/IEC 10279, Information technology, Programming languages, Full BASIC. Names: name transformation.

| Host | Lao | Source |
|---|---|---|
| dim | dim | host form (no native word yet) |
| end | end | host form (no native word yet) |
| for | ສຳລັບ | lexicon |
| gosub | gosub | host form (no native word yet) |
| goto | goto | host form (no native word yet) |
| if | ຖ້າ | lexicon |
| input | input | host form (no native word yet) |
| let | let | host form (no native word yet) |
| next | next | host form (no native word yet) |
| print | print | host form (no native word yet) |
| rem | rem | host form (no native word yet) |
| return | ສົ່ງຄືນ | lexicon |
| step | step | host form (no native word yet) |
| then | then | host form (no native word yet) |
| to | to | host form (no native word yet) |
| wend | wend | host form (no native word yet) |
| while | ໃນຂະນະທີ່ | lexicon |
| and | ca | lexicon |
| or | or | host form (no native word yet) |
| not | na | lexicon |
| mod | mod | host form (no native word yet) |

Standard library and runtime names of the BASIC binding:

| Host | Lao | Source |
|---|---|---|
| ELSE | ບໍ່ດັ່ງນັ້ນ | lexicon |
| INT | ຈຳນວນເຕັມ | lexicon |

### A.7 LOGO

Host: No international standard; the host is the Berkeley Logo dialect (bibliography). Names: name transformation.

| Host | Lao | Source |
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
| if | ຖ້າ | lexicon |
| ifelse | ifelse | host form (no native word yet) |
| home | home | host form (no native word yet) |
| clearscreen | clearscreen | host form (no native word yet) |

## Annex B (informative) Coverage and review

| Binding | Host keywords with a native word | Library names |
|---|---|---|
| C | 17 of 35 | 2 |
| C preprocessor | 2 of 12 | 0 |
| C++ | 20 of 61 | 3 |
| Java | 18 of 51 | 7 |
| Python | 11 of 36 | 11 |
| BASIC | 6 of 21 | 2 |
| LOGO | 1 of 14 | 0 |

The lowering of Lao programs to C is verified by the reference implementation: no filter yet. Source Chintamani means a word of the original Hindawi transducers; lexicon, a word of the language's lexicon; proposed, a word proposed by the project and not yet reviewed by the language community.

## Annex C (normative) Script filter

The script filter maps each letter and sign of the script to the Devanagari letter or sign of the same Unicode name, as generated by lang/hindawi/tools/script_filters.py.

## Annex D (informative) Rights and provenance

This document is an original work. It defines new programming languages by reference to the host language standards listed in Clause 2 and reproduces no text from them. Permission to adopt, translate or publish it as a standard is given by the copyright holder to a standards body on request.

Single words and the keywords of the host languages are not reproduced from any copyrighted text; the native words of Annex A were chosen by the Hindawi project, taken from the language's lexicon in the Hindawi repository, or, for Hindi, taken from the Chintamani transducers of the original Hindawi, whose author holds their copyright.

## Bibliography

- Hindawi 2026.10, hindawiai/hindawi2026.10, the reference implementation
- Chintamani, hindawiai/chintamani, the Hindawi transducers and the Romenagri tools
- Berkeley Logo reference manual, Brian Harvey

