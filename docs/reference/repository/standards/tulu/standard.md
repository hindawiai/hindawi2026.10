# HLS tulu 2026.10

**Tulu bindings for programming languages: lexical mapping and lowering to the host standards**

Edition 2026.10, working draft, 2026-10-18. © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

## Foreword

This document was prepared by AyeAI, Hindawi project (Project ILM). It is generated from the Tulu cell of Hindawi 2026.10 by lang/hindawi/tools/standards.py, so that the published standard and the reference implementation cannot drift apart. Its stage is a working draft: the words marked proposed in Annex A await review by the Tulu language community, through the review pages of the Hindawi project.

## Introduction

This document lets programs be written in Tulu, in the Kannada script, in each of the programming languages listed in Clause 1. Each binding is a programming language in its own right, Tulu C for example, whose programs are lowered by the function defined in Clause 6 to programs of the host language, and are then processed by any conforming implementation of the host standard. The host standards are incorporated by reference and are not restated. Names keep a defined form down to object code (Clause 7), so programs written in Tulu remain debuggable at the level of firmware, kernels and libraries.

## 1 Scope

This document specifies, for the Tulu language written in the Kannada script, bindings to the following host programming languages: C, C preprocessor, C++, Java, Python, BASIC, LOGO. For each binding it specifies the native keywords and directives, the lowering of native programs to host programs, the treatment of names, and the requirements for conformance.

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

- binding: programming language defined by this document whose programs are written in Tulu and lowered to one host language

- native keyword: word of this document that stands for one keyword, directive or standard library name of a host language

- lowering: function from native programs to host programs defined in Clause 6

- raising: inverse of lowering applied to a host program with a dictionary of names, giving back the native program exactly

- name transformation: function from native names to host identifiers defined in Clause 7

- C-level form: result of the name transformation; the form a native name takes in host source and in object code

## 4 Conformance

A conforming Tulu program of a binding shall be a text that meets Clause 5 and whose lowering is a conforming program of the host language.

A conforming implementation of a binding shall accept every conforming program of that binding and shall behave as the lowering of the program, processed by a conforming implementation of the host language, behaves.

An implementation that raises host programs into a binding shall produce native programs whose lowering, with the same dictionary of names, is identical to the host program it raised.

## 5 Character set and encoding

A native program shall be encoded in UTF-8 and shall be in Normalization Form C. Native keywords and names are written in the Kannada script, whose direction is left to right. Numeric literals are written with the digits 0 to 9 (U+0030 to U+0039). A native keyword written as several words is one token, its words joined by LOW LINE (U+005F).

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

| Host | Tulu | Source |
|---|---|---|
| auto | auto | host form (no native word yet) |
| break | ಭಙ್ಗ | lexicon |
| case | ಪಕ್ಷ | lexicon |
| char | ವರ್ಣ | lexicon |
| const | ಧ್ರುವ | lexicon |
| continue | ಅನುವರ್ತ | lexicon |
| default | ಸ್ವಭಾವ | lexicon |
| do | ಕುರು | lexicon |
| double | ದ್ವಿಗುಣ | lexicon |
| else | ಅನ್ಯಥಾ | lexicon |
| enum | ಗಣನಾ | lexicon |
| extern | ಬಾಹ್ಯ | lexicon |
| float | ಭಿನ್ನ | lexicon |
| for | ಪ್ರತಿ | lexicon |
| goto | ಗಚ್ಛ | lexicon |
| if | ಯದಿ | lexicon |
| inline | ಅನ್ತಃಸ್ಥ | lexicon |
| int | ಪೂರ್ಣಾಙ್ಕ | lexicon |
| long | long | host form (no native word yet) |
| register | ಪಞ್ಜಿಕಾ | lexicon |
| restrict | restrict | host form (no native word yet) |
| return | ಪ್ರತ್ಯಾಗಮ | lexicon |
| short | short | host form (no native word yet) |
| signed | signed | host form (no native word yet) |
| sizeof | ಪರಿಮಾಣ | lexicon |
| static | ಸ್ಥಿರ | lexicon |
| struct | ಸಂರಚನಾ | lexicon |
| switch | ವಿಕಲ್ಪ | lexicon |
| typedef | ಪ್ರಕಾರನಿರ್ದೇಶ | lexicon |
| union | ಸಙ್ಘ | lexicon |
| unsigned | unsigned | host form (no native word yet) |
| void | ಶೂನ್ಯ | lexicon |
| volatile | ಚಞ್ಚಲ | lexicon |
| while | ಯಾವತ್ | lexicon |
| main | main | host form (no native word yet) |

Standard library and runtime names of the C binding:

| Host | Tulu | Source |
|---|---|---|
| NULL | ರಿಕ್ತ | lexicon |
| assert | ಪ್ರತಿಜ್ಞಾ | lexicon |
| free | ಮುಕ್ತ | lexicon |
| private | ಗುಪ್ತ | lexicon |
| protected | ರಕ್ಷಿತ | lexicon |
| public | ಸಾರ್ವಜನಿಕ | lexicon |
| raise | ಉತ್ಥಾಪಯ | lexicon |
| read | ಪಠ | lexicon |
| signal | ಸಙ್ಕೇತ | lexicon |
| virtual | ಆಭಾಸ | lexicon |
| write | ಲಿಖ | lexicon |

### A.2 C preprocessor

Host: ISO/IEC 9899, Information technology, Programming languages, C (preprocessing directives). Names: name transformation.

| Host | Tulu | Source |
|---|---|---|
| #define | #define | host form (no native word yet) |
| #include | #ಅನ್ತರ್ಭಾವ | lexicon |
| #if | #ಯದಿ | lexicon |
| #ifdef | #ifdef | host form (no native word yet) |
| #ifndef | #ifndef | host form (no native word yet) |
| #else | #ಅನ್ಯಥಾ | lexicon |
| #elif | #ನೋಚೇದ್ಯದಿ | lexicon |
| #endif | #endif | host form (no native word yet) |
| #undef | #undef | host form (no native word yet) |
| #pragma | #pragma | host form (no native word yet) |
| #error | #error | host form (no native word yet) |
| #line | #line | host form (no native word yet) |

### A.3 C++

Host: ISO/IEC 14882, Programming languages, C++. Names: name transformation.

| Host | Tulu | Source |
|---|---|---|
| auto | auto | host form (no native word yet) |
| break | ಭಙ್ಗ | lexicon |
| case | ಪಕ್ಷ | lexicon |
| char | ವರ್ಣ | lexicon |
| const | ಧ್ರುವ | lexicon |
| continue | ಅನುವರ್ತ | lexicon |
| default | ಸ್ವಭಾವ | lexicon |
| do | ಕುರು | lexicon |
| double | ದ್ವಿಗುಣ | lexicon |
| else | ಅನ್ಯಥಾ | lexicon |
| enum | ಗಣನಾ | lexicon |
| extern | ಬಾಹ್ಯ | lexicon |
| float | ಭಿನ್ನ | lexicon |
| for | ಪ್ರತಿ | lexicon |
| goto | ಗಚ್ಛ | lexicon |
| if | ಯದಿ | lexicon |
| inline | ಅನ್ತಃಸ್ಥ | lexicon |
| int | ಪೂರ್ಣಾಙ್ಕ | lexicon |
| long | long | host form (no native word yet) |
| register | ಪಞ್ಜಿಕಾ | lexicon |
| restrict | restrict | host form (no native word yet) |
| return | ಪ್ರತ್ಯಾಗಮ | lexicon |
| short | short | host form (no native word yet) |
| signed | signed | host form (no native word yet) |
| sizeof | ಪರಿಮಾಣ | lexicon |
| static | ಸ್ಥಿರ | lexicon |
| struct | ಸಂರಚನಾ | lexicon |
| switch | ವಿಕಲ್ಪ | lexicon |
| typedef | ಪ್ರಕಾರನಿರ್ದೇಶ | lexicon |
| union | ಸಙ್ಘ | lexicon |
| unsigned | unsigned | host form (no native word yet) |
| void | ಶೂನ್ಯ | lexicon |
| volatile | ಚಞ್ಚಲ | lexicon |
| while | ಯಾವತ್ | lexicon |
| main | main | host form (no native word yet) |
| bool | ತಾರ್ಕಿಕ | lexicon |
| catch | ಗೃಹಾಣ | lexicon |
| class | ವರ್ಗ | lexicon |
| delete | delete | host form (no native word yet) |
| explicit | explicit | host form (no native word yet) |
| false | ಅಸತ್ಯ | lexicon |
| friend | friend | host form (no native word yet) |
| mutable | mutable | host form (no native word yet) |
| namespace | ನಾಮಾಕಾಶ | lexicon |
| new | ನೂತನ | lexicon |
| nullptr | nullptr | host form (no native word yet) |
| operator | operator | host form (no native word yet) |
| private | ಗುಪ್ತ | lexicon |
| protected | ರಕ್ಷಿತ | lexicon |
| public | ಸಾರ್ವಜನಿಕ | lexicon |
| template | template | host form (no native word yet) |
| this | ಏತತ್ | lexicon |
| throw | ಕ್ಷಿಪ | lexicon |
| true | ಸತ್ಯ | lexicon |
| try | ಯತ್ನ | lexicon |
| typename | typename | host form (no native word yet) |
| using | using | host form (no native word yet) |
| virtual | ಆಭಾಸ | lexicon |
| cout | cout | host form (no native word yet) |
| cin | cin | host form (no native word yet) |
| endl | endl | host form (no native word yet) |

Standard library and runtime names of the C++ binding:

| Host | Tulu | Source |
|---|---|---|
| NULL | ರಿಕ್ತ | lexicon |
| assert | ಪ್ರತಿಜ್ಞಾ | lexicon |
| free | ಮುಕ್ತ | lexicon |
| pipe | ಪ್ರಣಾಲ | lexicon |
| raise | ಉತ್ಥಾಪಯ | lexicon |
| read | ಪಠ | lexicon |
| signal | ಸಙ್ಕೇತ | lexicon |
| sleep | ಸುಷುಪ್ತಿ | lexicon |
| sync | ಸಮಕಾಲ | lexicon |
| write | ಲಿಖ | lexicon |

### A.4 Java

Host: The Java Language Specification, Oracle, current edition. Names: unchanged.

| Host | Tulu | Source |
|---|---|---|
| abstract | ಅಮೂರ್ತ | lexicon |
| assert | ಪ್ರತಿಜ್ಞಾ | lexicon |
| boolean | boolean | host form (no native word yet) |
| break | ಭಙ್ಗ | lexicon |
| byte | byte | host form (no native word yet) |
| case | ಪಕ್ಷ | lexicon |
| catch | ಗೃಹಾಣ | lexicon |
| char | ವರ್ಣ | lexicon |
| class | ವರ್ಗ | lexicon |
| continue | ಅನುವರ್ತ | lexicon |
| default | ಸ್ವಭಾವ | lexicon |
| do | ಕುರು | lexicon |
| double | ದ್ವಿಗುಣ | lexicon |
| else | ಅನ್ಯಥಾ | lexicon |
| enum | ಗಣನಾ | lexicon |
| extends | ವಿಸ್ತೃತ | lexicon |
| final | final | host form (no native word yet) |
| finally | ಅನ್ತತಃ | lexicon |
| float | ಭಿನ್ನ | lexicon |
| for | ಪ್ರತಿ | lexicon |
| if | ಯದಿ | lexicon |
| implements | ನಿಷ್ಪಾದಿತ | lexicon |
| import | ಆನಯನ | lexicon |
| instanceof | instanceof | host form (no native word yet) |
| int | ಪೂರ್ಣಾಙ್ಕ | lexicon |
| interface | ಸನ್ಧಿ | lexicon |
| long | long | host form (no native word yet) |
| native | native | host form (no native word yet) |
| new | ನೂತನ | lexicon |
| package | ಪುಟಕ | lexicon |
| private | ಗುಪ್ತ | lexicon |
| protected | ರಕ್ಷಿತ | lexicon |
| public | ಸಾರ್ವಜನಿಕ | lexicon |
| return | ಪ್ರತ್ಯಾಗಮ | lexicon |
| short | short | host form (no native word yet) |
| static | ಸ್ಥಿರ | lexicon |
| super | ಪರ | lexicon |
| switch | ವಿಕಲ್ಪ | lexicon |
| synchronized | synchronized | host form (no native word yet) |
| this | ಏತತ್ | lexicon |
| throw | ಕ್ಷಿಪ | lexicon |
| throws | throws | host form (no native word yet) |
| try | ಯತ್ನ | lexicon |
| void | ಶೂನ್ಯ | lexicon |
| volatile | ಚಞ್ಚಲ | lexicon |
| while | ಯಾವತ್ | lexicon |
| true | ಸತ್ಯ | lexicon |
| false | ಅಸತ್ಯ | lexicon |
| null | ರಿಕ್ತ | lexicon |
| String | ಪದಾವಲೀ | lexicon |
| System | System | host form (no native word yet) |

Standard library and runtime names of the Java binding:

| Host | Tulu | Source |
|---|---|---|
| Object | ವಸ್ತು | lexicon |
| Thread | ತನ್ತು | lexicon |
| const | ಧ್ರುವ | lexicon |
| extern | ಬಾಹ್ಯ | lexicon |
| free | ಮುಕ್ತ | lexicon |
| goto | ಗಚ್ಛ | lexicon |
| inline | ಅನ್ತಃಸ್ಥ | lexicon |
| raise | ಉತ್ಥಾಪಯ | lexicon |
| read | ಪಠ | lexicon |
| register | ಪಞ್ಜಿಕಾ | lexicon |
| signal | ಸಙ್ಕೇತ | lexicon |
| sizeof | ಪರಿಮಾಣ | lexicon |
| sleep | ಸುಷುಪ್ತಿ | lexicon |
| struct | ಸಂರಚನಾ | lexicon |
| typedef | ಪ್ರಕಾರನಿರ್ದೇಶ | lexicon |
| union | ಸಙ್ಘ | lexicon |
| virtual | ಆಭಾಸ | lexicon |
| write | ಲಿಖ | lexicon |

### A.5 Python

Host: The Python Language Reference, Python Software Foundation, current version. Names: unchanged.

| Host | Tulu | Source |
|---|---|---|
| False | ಅಸತ್ಯ | lexicon |
| None | None | host form (no native word yet) |
| True | ಸತ್ಯ | lexicon |
| and | ಚ | lexicon |
| as | ಇವ | lexicon |
| assert | ಪ್ರತಿಜ್ಞಾ | lexicon |
| break | ಭಙ್ಗ | lexicon |
| class | ವರ್ಗ | lexicon |
| continue | ಅನುವರ್ತ | lexicon |
| def | def | host form (no native word yet) |
| del | del | host form (no native word yet) |
| elif | ನೋಚೇದ್ಯದಿ | lexicon |
| else | ಅನ್ಯಥಾ | lexicon |
| except | ಅಪವಾದ | lexicon |
| finally | ಅನ್ತತಃ | lexicon |
| for | ಪ್ರತಿ | lexicon |
| from | ತಃ | lexicon |
| global | ವೈಶ್ವಿಕ | lexicon |
| if | ಯದಿ | lexicon |
| import | ಆನಯನ | lexicon |
| in | ಅನ್ತಃ | lexicon |
| is | is | host form (no native word yet) |
| lambda | ಅನಾಮನ್ | lexicon |
| nonlocal | nonlocal | host form (no native word yet) |
| not | ನ | lexicon |
| or | ವಾ | lexicon |
| pass | pass | host form (no native word yet) |
| raise | ಉತ್ಥಾಪಯ | lexicon |
| return | ಪ್ರತ್ಯಾಗಮ | lexicon |
| try | ಯತ್ನ | lexicon |
| while | ಯಾವತ್ | lexicon |
| with | with | host form (no native word yet) |
| yield | ದಾ | lexicon |
| print | print | host form (no native word yet) |
| range | range | host form (no native word yet) |
| len | len | host form (no native word yet) |

Standard library and runtime names of the Python binding:

| Host | Tulu | Source |
|---|---|---|
| Object | ವಸ್ತು | lexicon |
| String | ಪದಾವಲೀ | lexicon |
| Thread | ತನ್ತು | lexicon |
| abstract | ಅಮೂರ್ತ | lexicon |
| case | ಪಕ್ಷ | lexicon |
| catch | ಗೃಹಾಣ | lexicon |
| char | ವರ್ಣ | lexicon |
| const | ಧ್ರುವ | lexicon |
| default | ಸ್ವಭಾವ | lexicon |
| do | ಕುರು | lexicon |
| double | ದ್ವಿಗುಣ | lexicon |
| extends | ವಿಸ್ತೃತ | lexicon |
| float | ಭಿನ್ನ | lexicon |
| goto | ಗಚ್ಛ | lexicon |
| implements | ನಿಷ್ಪಾದಿತ | lexicon |
| int | ಪೂರ್ಣಾಙ್ಕ | lexicon |
| interface | ಸನ್ಧಿ | lexicon |
| new | ನೂತನ | lexicon |
| package | ಪುಟಕ | lexicon |
| private | ಗುಪ್ತ | lexicon |
| protected | ರಕ್ಷಿತ | lexicon |
| public | ಸಾರ್ವಜನಿಕ | lexicon |
| read | ಪಠ | lexicon |
| sleep | ಸುಷುಪ್ತಿ | lexicon |
| static | ಸ್ಥಿರ | lexicon |
| super | ಪರ | lexicon |
| switch | ವಿಕಲ್ಪ | lexicon |
| this | ಏತತ್ | lexicon |
| throw | ಕ್ಷಿಪ | lexicon |
| void | ಶೂನ್ಯ | lexicon |
| volatile | ಚಞ್ಚಲ | lexicon |
| write | ಲಿಖ | lexicon |

### A.6 BASIC

Host: ISO/IEC 10279, Information technology, Programming languages, Full BASIC. Names: name transformation.

| Host | Tulu | Source |
|---|---|---|
| dim | dim | host form (no native word yet) |
| end | ಅನ್ತ | lexicon |
| for | ಪ್ರತಿ | lexicon |
| gosub | gosub | host form (no native word yet) |
| goto | ಗಚ್ಛ | lexicon |
| if | ಯದಿ | lexicon |
| input | input | host form (no native word yet) |
| let | ಅಸ್ತು | lexicon |
| next | next | host form (no native word yet) |
| print | print | host form (no native word yet) |
| rem | rem | host form (no native word yet) |
| return | ಪ್ರತ್ಯಾಗಮ | lexicon |
| step | step | host form (no native word yet) |
| then | then | host form (no native word yet) |
| to | to | host form (no native word yet) |
| wend | wend | host form (no native word yet) |
| while | ಯಾವತ್ | lexicon |
| and | ಚ | lexicon |
| or | ವಾ | lexicon |
| not | ನ | lexicon |
| mod | mod | host form (no native word yet) |

Standard library and runtime names of the BASIC binding:

| Host | Tulu | Source |
|---|---|---|
| AS | ಇವ | lexicon |
| CALL | ಆಹ್ವಾನ | lexicon |
| CONST | ಧ್ರುವ | lexicon |
| DO | ಕುರು | lexicon |
| ELSE | ಅನ್ಯಥಾ | lexicon |
| INT | ಪೂರ್ಣಾಙ್ಕ | lexicon |
| SHARED | ಸಹಭಾಜಿತ | lexicon |
| STATIC | ಸ್ಥಿರ | lexicon |
| STRING | ಪದಾವಲೀ | lexicon |
| TIMER | ಕಾಲಯನ್ತ್ರ | lexicon |

### A.7 LOGO

Host: No international standard; the host is the Berkeley Logo dialect (bibliography). Names: name transformation.

| Host | Tulu | Source |
|---|---|---|
| forward | ಅಗ್ರಪ್ರಸಾರ | lexicon |
| back | back | host form (no native word yet) |
| left | left | host form (no native word yet) |
| right | right | host form (no native word yet) |
| penup | penup | host form (no native word yet) |
| pendown | pendown | host form (no native word yet) |
| repeat | repeat | host form (no native word yet) |
| to | to | host form (no native word yet) |
| end | ಅನ್ತ | lexicon |
| make | make | host form (no native word yet) |
| if | ಯದಿ | lexicon |
| ifelse | ifelse | host form (no native word yet) |
| home | home | host form (no native word yet) |
| clearscreen | clearscreen | host form (no native word yet) |

## Annex B (informative) Coverage and review

| Binding | Host keywords with a native word | Library names |
|---|---|---|
| C | 28 of 35 | 11 |
| C preprocessor | 4 of 12 | 0 |
| C++ | 42 of 61 | 10 |
| Java | 41 of 51 | 18 |
| Python | 26 of 36 | 32 |
| BASIC | 10 of 21 | 10 |
| LOGO | 3 of 14 | 0 |

The lowering of Tulu programs to C is verified by the reference implementation: runs, same output. Source Chintamani means a word of the original Hindawi transducers; lexicon, a word of the language's lexicon; proposed, a word proposed by the project and not yet reviewed by the language community.

## Annex C (normative) Script filter

The script filter maps each letter and sign of the script to the Devanagari letter or sign of the same Unicode name, as generated by lang/hindawi/tools/script_filters.py.

## Annex D (informative) Rights and provenance

This document is an original work. It defines new programming languages by reference to the host language standards listed in Clause 2 and reproduces no text from them. Permission to adopt, translate or publish it as a standard is given by the copyright holder to a standards body on request.

Single words and the keywords of the host languages are not reproduced from any copyrighted text; the native words of Annex A were chosen by the Hindawi project, taken from the language's lexicon in the Hindawi repository, or, for Hindi, taken from the Chintamani transducers of the original Hindawi, whose author holds their copyright.

## Bibliography

- Hindawi 2026.10, hindawiai/hindawi2026.10, the reference implementation
- Chintamani, hindawiai/chintamani, the Hindawi transducers and the Romenagri tools
- Berkeley Logo reference manual, Brian Harvey

