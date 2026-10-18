# HLS kn 2026.10

**Kannada bindings for programming languages: lexical mapping and lowering to the host standards**

Edition 2026.10, working draft, 2026-10-18. © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

## Foreword

This document was prepared by AyeAI, Hindawi project (Project ILM). It is generated from the Kannada cell of Hindawi 2026.10 by lang/hindawi/tools/standards.py, so that the published standard and the reference implementation cannot drift apart. Its stage is a working draft: the words marked proposed in Annex A await review by the Kannada language community, through the review pages of the Hindawi project.

## Introduction

This document lets programs be written in Kannada, in the Kannada script, in each of the programming languages listed in Clause 1. Each binding is a programming language in its own right, Kannada C for example, whose programs are lowered by the function defined in Clause 6 to programs of the host language, and are then processed by any conforming implementation of the host standard. The host standards are incorporated by reference and are not restated. Names keep a defined form down to object code (Clause 7), so programs written in Kannada remain debuggable at the level of firmware, kernels and libraries.

## 1 Scope

This document specifies, for the Kannada language written in the Kannada script, bindings to the following host programming languages: C, C preprocessor, C++, Java, Python, BASIC, LOGO. For each binding it specifies the native keywords and directives, the lowering of native programs to host programs, the treatment of names, and the requirements for conformance.

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

- binding: programming language defined by this document whose programs are written in Kannada and lowered to one host language

- native keyword: word of this document that stands for one keyword, directive or standard library name of a host language

- lowering: function from native programs to host programs defined in Clause 6

- raising: inverse of lowering applied to a host program with a dictionary of names, giving back the native program exactly

- name transformation: function from native names to host identifiers defined in Clause 7

- C-level form: result of the name transformation; the form a native name takes in host source and in object code

## 4 Conformance

A conforming Kannada program of a binding shall be a text that meets Clause 5 and whose lowering is a conforming program of the host language.

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

| Host | Kannada | Source |
|---|---|---|
| auto | ಸ್ವಯಂಚಾಲಿತ | proposed |
| break | ನಿಲ್ಲಿಸು | lexicon |
| case | ಸ್ಥಿತಿ | lexicon |
| char | ಅಕ್ಷರ | lexicon |
| const | ಸ್ಥಿರಾಂಕ | lexicon |
| continue | ಮುಂದುವರಿ | lexicon |
| default | ಪೂರ್ವನಿಯೋಜಿತ | lexicon |
| do | ಮಾಡು | lexicon |
| double | ದ್ವಿಗುಣ | lexicon |
| else | ಇಲ್ಲದಿದ್ದರೆ | lexicon |
| enum | ಎಣಿಕೆ | lexicon |
| extern | ಬಾಹ್ಯ | lexicon |
| float | ದಶಮಾಂಶ | lexicon |
| for | ಗಾಗಿ | lexicon |
| goto | ಹೋಗು | lexicon |
| if | ಆದರೆ | lexicon |
| inline | ಸಾಲೊಳಗೆ | lexicon |
| int | ಪೂರ್ಣಾಂಕ | lexicon |
| long | ದೀರ್ಘ | proposed |
| register | ನೋಂದಣಿ | lexicon |
| restrict | ಸೀಮಿತ | proposed |
| return | ಹಿಂತಿರುಗಿ | lexicon |
| short | ಗಿಡ್ಡ | proposed |
| signed | ಚಿಹ್ನೆಯುಳ್ಳ | proposed |
| sizeof | ಗಾತ್ರ | lexicon |
| static | ಸ್ಥಿರ | lexicon |
| struct | ರಚನೆ | lexicon |
| switch | ಆಯ್ಕೆ | lexicon |
| typedef | ಪ್ರಕಾರವ್ಯಾಖ್ಯೆ | lexicon |
| union | ಒಕ್ಕೂಟ | lexicon |
| unsigned | ಚಿಹ್ನೆರಹಿತ | proposed |
| void | ಶೂನ್ಯ | lexicon |
| volatile | ಅಸ್ಥಿರ | lexicon |
| while | ಆಗ | lexicon |
| main | ಮುಖ್ಯ | lexicon |

Standard library and runtime names of the C binding:

| Host | Kannada | Source |
|---|---|---|
| INT_MAX | ಗರಿಷ್ಠ_ಪೂರ್ಣಾಂಕ | proposed |
| NULL | ಖಾಲಿ | lexicon |
| abs | ನಿರಪೇಕ್ಷ | proposed |
| assert | ಪ್ರತಿಜ್ಞಾ | lexicon |
| calloc | ಸೊನ್ನೆ_ಸ್ಮರಣೆ_ಕೊಡು | proposed |
| cos | ಕೋಜ್ಯಾ | proposed |
| exit | ನಿರ್ಗಮಿಸು | proposed |
| exp | ಘಾತಾಂಕ | proposed |
| free | ಬಿಡುಗಡೆ | lexicon |
| friend | ಮಿತ್ರ | proposed |
| isalnum | ಅಕ್ಷರವೇ_ಅಂಕಿಯೇ | proposed |
| isalpha | ಅಕ್ಷರವೇ | proposed |
| isdigit | ಅಂಕಿಯೇ | proposed |
| isspace | ಖಾಲಿಯೇ | proposed |
| log | ಲಘುಗಣಕ | proposed |
| malloc | ಸ್ಮರಣೆ_ಕೊಡು | proposed |
| memcpy | ಸ್ಮರಣೆ_ನಕಲು | proposed |
| operator | ಕ್ರಿಯಾಕಾರಕ | proposed |
| pow | ಘಾತ | proposed |
| printf | ಬರೆ | proposed |
| private | ಖಾಸಗಿ | lexicon |
| protected | ಸಂರಕ್ಷಿತ | lexicon |
| public | ಸಾರ್ವಜನಿಕ | lexicon |
| putchar | ಅಕ್ಷರ_ಬರೆ | proposed |
| raise | ಎತ್ತು | lexicon |
| read | ಪಠ | lexicon |
| signal | ಸಂಕೇತ | lexicon |
| sin | ಜ್ಯಾ | proposed |
| sqrt | ವರ್ಗಮೂಲ | proposed |
| sscanf | ಅಕ್ಷರಸರಣಿ_ಓದು | proposed |
| strlen | ಅಕ್ಷರಸರಣಿ_ಉದ್ದ | proposed |
| strncmp | ಅಕ್ಷರಸರಣಿ_ಹೋಲಿಕೆ | proposed |
| strstr | ಅಕ್ಷರಸರಣಿ_ಹುಡುಕು | proposed |
| template | ಮಾದರಿ | proposed |
| toupper | ದೊಡ್ಡ_ಅಕ್ಷರ | proposed |
| virtual | ವಾಸ್ತವಿಕ | lexicon |
| write | ಲಿಖ | lexicon |

### A.2 C preprocessor

Host: ISO/IEC 9899, Information technology, Programming languages, C (preprocessing directives). Names: name transformation.

| Host | Kannada | Source |
|---|---|---|
| #define | #ವ್ಯಾಖ್ಯಾನಿಸು | proposed |
| #include | #ಅನ್ತರ್ಭಾವ | lexicon |
| #if | #ಆದರೆ | lexicon |
| #ifdef | #ವ್ಯಾಖ್ಯಾನಿತವಾದರೆ | proposed |
| #ifndef | #ವ್ಯಾಖ್ಯಾನಿತವಾಗದಿದ್ದರೆ | proposed |
| #else | #ಇಲ್ಲದಿದ್ದರೆ | lexicon |
| #elif | #ಅಥವಾಆದರೆ | lexicon |
| #endif | #ಆದರೆ_ಅಂತ್ಯ | proposed |
| #undef | #ವ್ಯಾಖ್ಯಾನ_ರದ್ದು | proposed |
| #pragma | #ಸೂಚನೆ | proposed |
| #error | #ದೋಷ | proposed |
| #line | #ಸಾಲು | proposed |

### A.3 C++

Host: ISO/IEC 14882, Programming languages, C++. Names: name transformation.

| Host | Kannada | Source |
|---|---|---|
| auto | ಸ್ವಯಂಚಾಲಿತ | proposed |
| break | ನಿಲ್ಲಿಸು | lexicon |
| case | ಸ್ಥಿತಿ | lexicon |
| char | ಅಕ್ಷರ | lexicon |
| const | ಸ್ಥಿರಾಂಕ | lexicon |
| continue | ಮುಂದುವರಿ | lexicon |
| default | ಪೂರ್ವನಿಯೋಜಿತ | lexicon |
| do | ಮಾಡು | lexicon |
| double | ದ್ವಿಗುಣ | lexicon |
| else | ಇಲ್ಲದಿದ್ದರೆ | lexicon |
| enum | ಎಣಿಕೆ | lexicon |
| extern | ಬಾಹ್ಯ | lexicon |
| float | ದಶಮಾಂಶ | lexicon |
| for | ಗಾಗಿ | lexicon |
| goto | ಹೋಗು | lexicon |
| if | ಆದರೆ | lexicon |
| inline | ಸಾಲೊಳಗೆ | lexicon |
| int | ಪೂರ್ಣಾಂಕ | lexicon |
| long | ದೀರ್ಘ | proposed |
| register | ನೋಂದಣಿ | lexicon |
| restrict | ಸೀಮಿತ | proposed |
| return | ಹಿಂತಿರುಗಿ | lexicon |
| short | ಗಿಡ್ಡ | proposed |
| signed | ಚಿಹ್ನೆಯುಳ್ಳ | proposed |
| sizeof | ಗಾತ್ರ | lexicon |
| static | ಸ್ಥಿರ | lexicon |
| struct | ರಚನೆ | lexicon |
| switch | ಆಯ್ಕೆ | lexicon |
| typedef | ಪ್ರಕಾರವ್ಯಾಖ್ಯೆ | lexicon |
| union | ಒಕ್ಕೂಟ | lexicon |
| unsigned | ಚಿಹ್ನೆರಹಿತ | proposed |
| void | ಶೂನ್ಯ | lexicon |
| volatile | ಅಸ್ಥಿರ | lexicon |
| while | ಆಗ | lexicon |
| main | ಮುಖ್ಯ | lexicon |
| bool | ತಾರ್ಕಿಕ | lexicon |
| catch | ಹಿಡಿ | lexicon |
| class | ವರ್ಗ | lexicon |
| delete | ಅಳಿಸು | proposed |
| explicit | ಸ್ಪಷ್ಟ | proposed |
| false | ಸುಳ್ಳು | lexicon |
| friend | ಮಿತ್ರ | proposed |
| mutable | ಬದಲಾಯಿಸಬಹುದಾದ | proposed |
| namespace | ನಾಮಾಕಾಶ | lexicon |
| new | ಹೊಸ | lexicon |
| nullptr | ಶೂನ್ಯಸೂಚಕ | proposed |
| operator | ಕ್ರಿಯಾಕಾರಕ | proposed |
| private | ಖಾಸಗಿ | lexicon |
| protected | ಸಂರಕ್ಷಿತ | lexicon |
| public | ಸಾರ್ವಜನಿಕ | lexicon |
| template | ಮಾದರಿ | proposed |
| this | ಇದು | lexicon |
| throw | ಎಸೆ | lexicon |
| true | ನಿಜ | lexicon |
| try | ಪ್ರಯತ್ನಿಸು | lexicon |
| typename | ಬಗೆ_ಹೆಸರು | proposed |
| using | ಬಳಸಿ | proposed |
| virtual | ವಾಸ್ತವಿಕ | lexicon |
| cout | ಹೊರಗೆ | proposed |
| cin | ಒಳಗೆ | proposed |
| endl | ಸಾಲು_ಅಂತ್ಯ | proposed |

Standard library and runtime names of the C++ binding:

| Host | Kannada | Source |
|---|---|---|
| INT_MAX | ಗರಿಷ್ಠ_ಪೂರ್ಣಾಂಕ | proposed |
| NULL | ಖಾಲಿ | lexicon |
| abs | ನಿರಪೇಕ್ಷ | proposed |
| assert | ಪ್ರತಿಜ್ಞಾ | lexicon |
| calloc | ಸೊನ್ನೆ_ಸ್ಮರಣೆ_ಕೊಡು | proposed |
| cos | ಕೋಜ್ಯಾ | proposed |
| exit | ನಿರ್ಗಮಿಸು | proposed |
| exp | ಘಾತಾಂಕ | proposed |
| free | ಬಿಡುಗಡೆ | lexicon |
| isalnum | ಅಕ್ಷರವೇ_ಅಂಕಿಯೇ | proposed |
| isalpha | ಅಕ್ಷರವೇ | proposed |
| isdigit | ಅಂಕಿಯೇ | proposed |
| isspace | ಖಾಲಿಯೇ | proposed |
| left | ಎಡ | proposed |
| log | ಲಘುಗಣಕ | proposed |
| malloc | ಸ್ಮರಣೆ_ಕೊಡು | proposed |
| memcpy | ಸ್ಮರಣೆ_ನಕಲು | proposed |
| pipe | ಪ್ರಣಾಲ | lexicon |
| pow | ಘಾತ | proposed |
| printf | ಬರೆ | proposed |
| putchar | ಅಕ್ಷರ_ಬರೆ | proposed |
| raise | ಎತ್ತು | lexicon |
| read | ಪಠ | lexicon |
| right | ಬಲ | proposed |
| signal | ಸಂಕೇತ | lexicon |
| sin | ಜ್ಯಾ | proposed |
| sleep | ಸುಷುಪ್ತಿ | lexicon |
| sqrt | ವರ್ಗಮೂಲ | proposed |
| sscanf | ಅಕ್ಷರಸರಣಿ_ಓದು | proposed |
| strlen | ಅಕ್ಷರಸರಣಿ_ಉದ್ದ | proposed |
| strncmp | ಅಕ್ಷರಸರಣಿ_ಹೋಲಿಕೆ | proposed |
| strstr | ಅಕ್ಷರಸರಣಿ_ಹುಡುಕು | proposed |
| sync | ಸಮಕಾಲೀಕರಣ | lexicon |
| toupper | ದೊಡ್ಡ_ಅಕ್ಷರ | proposed |
| write | ಲಿಖ | lexicon |

### A.4 Java

Host: The Java Language Specification, Oracle, current edition. Names: unchanged.

| Host | Kannada | Source |
|---|---|---|
| abstract | ಅಮೂರ್ತ | lexicon |
| assert | ಪ್ರತಿಜ್ಞಾ | lexicon |
| boolean | ತಾರ್ಕಿಕ | proposed |
| break | ನಿಲ್ಲಿಸು | lexicon |
| byte | ಬೈಟ್ | proposed |
| case | ಸ್ಥಿತಿ | lexicon |
| catch | ಹಿಡಿ | lexicon |
| char | ಅಕ್ಷರ | lexicon |
| class | ವರ್ಗ | lexicon |
| continue | ಮುಂದುವರಿ | lexicon |
| default | ಪೂರ್ವನಿಯೋಜಿತ | lexicon |
| do | ಮಾಡು | lexicon |
| double | ದ್ವಿಗುಣ | lexicon |
| else | ಇಲ್ಲದಿದ್ದರೆ | lexicon |
| enum | ಎಣಿಕೆ | lexicon |
| extends | ವಿಸ್ತರಿಸು | lexicon |
| final | ಅಂತಿಮ | proposed |
| finally | ಕೊನೆಗೆ | lexicon |
| float | ದಶಮಾಂಶ | lexicon |
| for | ಗಾಗಿ | lexicon |
| if | ಆದರೆ | lexicon |
| implements | ಅನುಷ್ಠಾನ | lexicon |
| import | ಆಮದು | lexicon |
| instanceof | ನಮೂನೆ_ಆಗಿದೆ | proposed |
| int | ಪೂರ್ಣಾಂಕ | lexicon |
| interface | ಸಂಪರ್ಕಮುಖ | lexicon |
| long | ದೀರ್ಘ | proposed |
| native | ಸ್ಥಳೀಯ | proposed |
| new | ಹೊಸ | lexicon |
| package | ಪೊಟ್ಟಣ | lexicon |
| private | ಖಾಸಗಿ | lexicon |
| protected | ಸಂರಕ್ಷಿತ | lexicon |
| public | ಸಾರ್ವಜನಿಕ | lexicon |
| return | ಹಿಂತಿರುಗಿ | lexicon |
| short | ಗಿಡ್ಡ | proposed |
| static | ಸ್ಥಿರ | lexicon |
| super | ಪರ | lexicon |
| switch | ಆಯ್ಕೆ | lexicon |
| synchronized | ಸಮಕಾಲಿಕ | proposed |
| this | ಇದು | lexicon |
| throw | ಎಸೆ | lexicon |
| throws | ಎಸೆಯುತ್ತದೆ | proposed |
| try | ಪ್ರಯತ್ನಿಸು | lexicon |
| void | ಶೂನ್ಯ | lexicon |
| volatile | ಅಸ್ಥಿರ | lexicon |
| while | ಆಗ | lexicon |
| true | ನಿಜ | lexicon |
| false | ಸುಳ್ಳು | lexicon |
| null | ಖಾಲಿ | lexicon |
| String | ಪದಪುಂಜ | lexicon |
| System | ವ್ಯವಸ್ಥೆ | proposed |

Standard library and runtime names of the Java binding:

| Host | Kannada | Source |
|---|---|---|
| INT_MAX | ಗರಿಷ್ಠ_ಪೂರ್ಣಾಂಕ | proposed |
| Object | ವಸ್ತು | lexicon |
| Thread | ಎಳೆ | lexicon |
| abs | ನಿರಪೇಕ್ಷ | proposed |
| auto | ಸ್ವಯಂಚಾಲಿತ | proposed |
| calloc | ಸೊನ್ನೆ_ಸ್ಮರಣೆ_ಕೊಡು | proposed |
| const | ಸ್ಥಿರಾಂಕ | lexicon |
| cos | ಕೋಜ್ಯಾ | proposed |
| exit | ನಿರ್ಗಮಿಸು | proposed |
| exp | ಘಾತಾಂಕ | proposed |
| extern | ಬಾಹ್ಯ | lexicon |
| free | ಬಿಡುಗಡೆ | lexicon |
| friend | ಮಿತ್ರ | proposed |
| goto | ಹೋಗು | lexicon |
| inline | ಸಾಲೊಳಗೆ | lexicon |
| isalnum | ಅಕ್ಷರವೇ_ಅಂಕಿಯೇ | proposed |
| isalpha | ಅಕ್ಷರವೇ | proposed |
| isdigit | ಅಂಕಿಯೇ | proposed |
| isspace | ಖಾಲಿಯೇ | proposed |
| log | ಲಘುಗಣಕ | proposed |
| main | ಮುಖ್ಯ | lexicon |
| malloc | ಸ್ಮರಣೆ_ಕೊಡು | proposed |
| memcpy | ಸ್ಮರಣೆ_ನಕಲು | proposed |
| operator | ಕ್ರಿಯಾಕಾರಕ | proposed |
| pow | ಘಾತ | proposed |
| printf | ಬರೆ | proposed |
| println | ಸಾಲು_ಮುದ್ರಿಸು | proposed |
| putchar | ಅಕ್ಷರ_ಬರೆ | proposed |
| raise | ಎತ್ತು | lexicon |
| read | ಪಠ | lexicon |
| register | ನೋಂದಣಿ | lexicon |
| restrict | ಸೀಮಿತ | proposed |
| signal | ಸಂಕೇತ | lexicon |
| signed | ಚಿಹ್ನೆಯುಳ್ಳ | proposed |
| sin | ಜ್ಯಾ | proposed |
| sizeof | ಗಾತ್ರ | lexicon |
| sleep | ಸುಷುಪ್ತಿ | lexicon |
| sqrt | ವರ್ಗಮೂಲ | proposed |
| sscanf | ಅಕ್ಷರಸರಣಿ_ಓದು | proposed |
| strlen | ಅಕ್ಷರಸರಣಿ_ಉದ್ದ | proposed |
| strncmp | ಅಕ್ಷರಸರಣಿ_ಹೋಲಿಕೆ | proposed |
| strstr | ಅಕ್ಷರಸರಣಿ_ಹುಡುಕು | proposed |
| struct | ರಚನೆ | lexicon |
| template | ಮಾದರಿ | proposed |
| toupper | ದೊಡ್ಡ_ಅಕ್ಷರ | proposed |
| typedef | ಪ್ರಕಾರವ್ಯಾಖ್ಯೆ | lexicon |
| union | ಒಕ್ಕೂಟ | lexicon |
| unsigned | ಚಿಹ್ನೆರಹಿತ | proposed |
| virtual | ವಾಸ್ತವಿಕ | lexicon |
| write | ಲಿಖ | lexicon |

### A.5 Python

Host: The Python Language Reference, Python Software Foundation, current version. Names: unchanged.

| Host | Kannada | Source |
|---|---|---|
| False | ಸುಳ್ಳು | lexicon |
| None | ಏನೂಇಲ್ಲ | proposed |
| True | ನಿಜ | lexicon |
| and | ಮತ್ತು | lexicon |
| as | ಇವ | lexicon |
| assert | ಪ್ರತಿಜ್ಞಾ | lexicon |
| break | ನಿಲ್ಲಿಸು | lexicon |
| class | ವರ್ಗ | lexicon |
| continue | ಮುಂದುವರಿ | lexicon |
| def | ವ್ಯಾಖ್ಯಾನ | proposed |
| del | ತೆಗೆ | proposed |
| elif | ಅಥವಾಆದರೆ | lexicon |
| else | ಇಲ್ಲದಿದ್ದರೆ | lexicon |
| except | ಅಪವಾದ | lexicon |
| finally | ಕೊನೆಗೆ | lexicon |
| for | ಗಾಗಿ | lexicon |
| from | ತಃ | lexicon |
| global | ವೈಶ್ವಿಕ | lexicon |
| if | ಆದರೆ | lexicon |
| import | ಆಮದು | lexicon |
| in | ಒಳಗೆ | lexicon |
| is | ಆಗಿರುವ | proposed |
| lambda | ಅನಾಮಿಕ | lexicon |
| nonlocal | ಸ್ಥಳೀಯೇತರ | proposed |
| not | ಅಲ್ಲ | lexicon |
| or | ಅಥವಾ | lexicon |
| pass | ದಾಟು | proposed |
| raise | ಎತ್ತು | lexicon |
| return | ಹಿಂತಿರುಗಿ | lexicon |
| try | ಪ್ರಯತ್ನಿಸು | lexicon |
| while | ಆಗ | lexicon |
| with | ಜೊತೆ | proposed |
| yield | ನೀಡು | lexicon |
| print | ಮುದ್ರಿಸು | proposed |
| range | ಶ್ರೇಣಿ | proposed |
| len | ಉದ್ದ | proposed |

Standard library and runtime names of the Python binding:

| Host | Kannada | Source |
|---|---|---|
| Object | ವಸ್ತು | lexicon |
| String | ಪದಪುಂಜ | lexicon |
| System | ವ್ಯವಸ್ಥೆ | proposed |
| Thread | ಎಳೆ | lexicon |
| abstract | ಅಮೂರ್ತ | lexicon |
| boolean | ತಾರ್ಕಿಕ | proposed |
| byte | ಬೈಟ್ | proposed |
| case | ಸ್ಥಿತಿ | lexicon |
| catch | ಹಿಡಿ | lexicon |
| char | ಅಕ್ಷರ | lexicon |
| const | ಸ್ಥಿರಾಂಕ | lexicon |
| default | ಪೂರ್ವನಿಯೋಜಿತ | lexicon |
| do | ಮಾಡು | lexicon |
| double | ದ್ವಿಗುಣ | lexicon |
| extends | ವಿಸ್ತರಿಸು | lexicon |
| final | ಅಂತಿಮ | proposed |
| float | ದಶಮಾಂಶ | lexicon |
| goto | ಹೋಗು | lexicon |
| implements | ಅನುಷ್ಠಾನ | lexicon |
| instanceof | ನಮೂನೆ_ಆಗಿದೆ | proposed |
| int | ಪೂರ್ಣಾಂಕ | lexicon |
| interface | ಸಂಪರ್ಕಮುಖ | lexicon |
| long | ದೀರ್ಘ | proposed |
| main | ಮುಖ್ಯ | lexicon |
| native | ಸ್ಥಳೀಯ | proposed |
| new | ಹೊಸ | lexicon |
| package | ಪೊಟ್ಟಣ | lexicon |
| println | ಸಾಲು_ಮುದ್ರಿಸು | proposed |
| private | ಖಾಸಗಿ | lexicon |
| protected | ಸಂರಕ್ಷಿತ | lexicon |
| public | ಸಾರ್ವಜನಿಕ | lexicon |
| read | ಪಠ | lexicon |
| short | ಗಿಡ್ಡ | proposed |
| sleep | ಸುಷುಪ್ತಿ | lexicon |
| sqrt | ವರ್ಗಮೂಲ | proposed |
| static | ಸ್ಥಿರ | lexicon |
| super | ಪರ | lexicon |
| switch | ಆಯ್ಕೆ | lexicon |
| this | ಇದು | lexicon |
| throw | ಎಸೆ | lexicon |
| throws | ಎಸೆಯುತ್ತದೆ | proposed |
| void | ಶೂನ್ಯ | lexicon |
| volatile | ಅಸ್ಥಿರ | lexicon |
| write | ಲಿಖ | lexicon |

### A.6 BASIC

Host: ISO/IEC 10279, Information technology, Programming languages, Full BASIC. Names: name transformation.

| Host | Kannada | Source |
|---|---|---|
| dim | ಆಯಾಮ | proposed |
| end | ಅಂತ್ಯ | lexicon |
| for | ಗಾಗಿ | lexicon |
| gosub | ಉಪ_ಹೋಗು | proposed |
| goto | ಹೋಗು | lexicon |
| if | ಆದರೆ | lexicon |
| input | ತೆಗೆದುಕೊ | proposed |
| let | ಇರಲಿ | lexicon |
| next | ಮುಂದಿನ_ಸುತ್ತು | proposed |
| print | ಮುದ್ರಿಸು | proposed |
| rem | ಟಿಪ್ಪಣಿ | proposed |
| return | ಹಿಂತಿರುಗಿ | lexicon |
| step | ಹೆಜ್ಜೆಯಲ್ಲಿ | proposed |
| then | ಹಾಗಾದರೆ | proposed |
| to | ವರೆಗೆ | proposed |
| wend | ತನಕ_ಅಂತ್ಯ | proposed |
| while | ಆಗ | lexicon |
| and | ಮತ್ತು | lexicon |
| or | ಅಥವಾ | lexicon |
| not | ಅಲ್ಲ | lexicon |
| mod | ಶೇಷ | proposed |

Standard library and runtime names of the BASIC binding:

| Host | Kannada | Source |
|---|---|---|
| AS | ಇವ | lexicon |
| CALL | ಕರೆ | lexicon |
| CONST | ಸ್ಥಿರಾಂಕ | lexicon |
| DO | ಮಾಡು | lexicon |
| ELSE | ಇಲ್ಲದಿದ್ದರೆ | lexicon |
| INT | ಪೂರ್ಣಾಂಕ | lexicon |
| SHARED | ಸಹಭಾಜಿತ | lexicon |
| STATIC | ಸ್ಥಿರ | lexicon |
| STRING | ಪದಪುಂಜ | lexicon |
| TIMER | ಕಾಲಯನ್ತ್ರ | lexicon |

### A.7 LOGO

Host: No international standard; the host is the Berkeley Logo dialect (bibliography). Names: name transformation.

| Host | Kannada | Source |
|---|---|---|
| forward | ಅಗ್ರಪ್ರಸಾರ | lexicon |
| back | ಹಿಂದೆ | proposed |
| left | ಎಡ | proposed |
| right | ಬಲ | proposed |
| penup | ಲೇಖನಿ_ಎತ್ತು | proposed |
| pendown | ಲೇಖನಿ_ಇಳಿಸು | proposed |
| repeat | ಪುನರಾವರ್ತಿಸು | proposed |
| to | ವರೆಗೆ | proposed |
| end | ಅಂತ್ಯ | lexicon |
| make | ಮಾಡು | proposed |
| if | ಆದರೆ | lexicon |
| ifelse | ಆದರೆ_ಇಲ್ಲದಿದ್ದರೆ | proposed |
| home | ಮನೆ | proposed |
| clearscreen | ಪರದೆ_ಶುಚಿ | proposed |

Standard library and runtime names of the LOGO binding:

| Host | Kannada | Source |
|---|---|---|
| print | ಮುದ್ರಿಸು | proposed |

## Annex B (informative) Coverage and review

| Binding | Host keywords with a native word | Library names |
|---|---|---|
| C | 35 of 35 | 37 |
| C preprocessor | 12 of 12 | 0 |
| C++ | 61 of 61 | 35 |
| Java | 51 of 51 | 50 |
| Python | 36 of 36 | 44 |
| BASIC | 21 of 21 | 10 |
| LOGO | 14 of 14 | 1 |

The lowering of Kannada programs to C is verified by the reference implementation: runs, same output. Source Chintamani means a word of the original Hindawi transducers; lexicon, a word of the language's lexicon; proposed, a word proposed by the project and not yet reviewed by the language community.

## Annex C (normative) Script filter

The script filter maps each letter and sign of the script to the Devanagari letter or sign of the same Unicode name, as generated by lang/hindawi/tools/script_filters.py.

## Annex D (informative) Rights and provenance

This document is an original work. It defines new programming languages by reference to the host language standards listed in Clause 2 and reproduces no text from them. Permission to adopt, translate or publish it as a standard is given by the copyright holder to a standards body on request.

Single words and the keywords of the host languages are not reproduced from any copyrighted text; the native words of Annex A were chosen by the Hindawi project, taken from the language's lexicon in the Hindawi repository, or, for Hindi, taken from the Chintamani transducers of the original Hindawi, whose author holds their copyright.

## Bibliography

- Hindawi 2026.10, hindawiai/hindawi2026.10, the reference implementation
- Chintamani, hindawiai/chintamani, the Hindawi transducers and the Romenagri tools
- Berkeley Logo reference manual, Brian Harvey

