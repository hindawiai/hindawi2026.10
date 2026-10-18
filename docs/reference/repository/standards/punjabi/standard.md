# HLS pa 2026.10

**Punjabi bindings for programming languages: lexical mapping and lowering to the host standards**

Edition 2026.10, working draft, 2026-10-18. © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

## Foreword

This document was prepared by AyeAI, Hindawi project (Project ILM). It is generated from the Punjabi cell of Hindawi 2026.10 by lang/hindawi/tools/standards.py, so that the published standard and the reference implementation cannot drift apart. Its stage is a working draft: the words marked proposed in Annex A await review by the Punjabi language community, through the review pages of the Hindawi project.

## Introduction

This document lets programs be written in Punjabi, in the Gurmukhi script, in each of the programming languages listed in Clause 1. Each binding is a programming language in its own right, Punjabi C for example, whose programs are lowered by the function defined in Clause 6 to programs of the host language, and are then processed by any conforming implementation of the host standard. The host standards are incorporated by reference and are not restated. Names keep a defined form down to object code (Clause 7), so programs written in Punjabi remain debuggable at the level of firmware, kernels and libraries.

## 1 Scope

This document specifies, for the Punjabi language written in the Gurmukhi script, bindings to the following host programming languages: C, C preprocessor, C++, Java, Python, BASIC, LOGO. For each binding it specifies the native keywords and directives, the lowering of native programs to host programs, the treatment of names, and the requirements for conformance.

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

- binding: programming language defined by this document whose programs are written in Punjabi and lowered to one host language

- native keyword: word of this document that stands for one keyword, directive or standard library name of a host language

- lowering: function from native programs to host programs defined in Clause 6

- raising: inverse of lowering applied to a host program with a dictionary of names, giving back the native program exactly

- name transformation: function from native names to host identifiers defined in Clause 7

- C-level form: result of the name transformation; the form a native name takes in host source and in object code

## 4 Conformance

A conforming Punjabi program of a binding shall be a text that meets Clause 5 and whose lowering is a conforming program of the host language.

A conforming implementation of a binding shall accept every conforming program of that binding and shall behave as the lowering of the program, processed by a conforming implementation of the host language, behaves.

An implementation that raises host programs into a binding shall produce native programs whose lowering, with the same dictionary of names, is identical to the host program it raised.

## 5 Character set and encoding

A native program shall be encoded in UTF-8 and shall be in Normalization Form C. Native keywords and names are written in the Gurmukhi script, whose direction is left to right. Numeric literals are written with the digits 0 to 9 (U+0030 to U+0039). A native keyword written as several words is one token, its words joined by LOW LINE (U+005F).

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

| Host | Punjabi | Source |
|---|---|---|
| auto | ਸਵੈਚਾਲਿਤ | proposed |
| break | ਰੋਕੋ | lexicon |
| case | ਹਾਲਤ | lexicon |
| char | ਅੱਖਰ | lexicon |
| const | ਅਚਲ | lexicon |
| continue | ਜਾਰੀ | lexicon |
| default | ਮੂਲ | lexicon |
| do | ਕਰੋ | lexicon |
| double | ਦੁੱਗਣਾ | lexicon |
| else | ਨਹੀਂਤਾਂ | lexicon |
| enum | ਗਿਣਤੀ | lexicon |
| extern | ਬਾਹਰੀ | lexicon |
| float | ਦਸ਼ਮਲਵ | lexicon |
| for | ਲਈ | lexicon |
| goto | ਜਾਓ | lexicon |
| if | ਜੇ | lexicon |
| inline | ਸਤਰਅੰਦਰ | lexicon |
| int | ਪੂਰਨ | lexicon |
| long | ਲੰਮਾ | proposed |
| register | ਰਜਿਸਟਰ | lexicon |
| restrict | ਸੀਮਿਤ | proposed |
| return | ਵਾਪਸ | lexicon |
| short | ਛੋਟਾ | proposed |
| signed | ਨਿਸ਼ਾਨੀਵਾਲਾ | proposed |
| sizeof | ਆਕਾਰ | lexicon |
| static | ਸਥਿਰ | lexicon |
| struct | ਬਣਤਰ | lexicon |
| switch | ਚੋਣ | lexicon |
| typedef | ਕਿਸਮਪਰਿਭਾਸ਼ਾ | lexicon |
| union | ਸੰਘ | lexicon |
| unsigned | ਬਿਨਾਨਿਸ਼ਾਨੀ | proposed |
| void | ਖਾਲੀ | lexicon |
| volatile | ਅਸਥਿਰ | lexicon |
| while | ਜਦੋਂ | lexicon |
| main | ਮੁੱਖ | lexicon |

Standard library and runtime names of the C binding:

| Host | Punjabi | Source |
|---|---|---|
| INT_MAX | ਵੱਧ_ਤੋਂ_ਵੱਧ_ਅੰਕ | proposed |
| NULL | ਨਿਰਾ | lexicon |
| abs | ਨਿਰਪੇਖ | proposed |
| assert | ਪ੍ਰਤਿਜ੍ਞਾ | lexicon |
| calloc | ਸਿਫਰ_ਸਮ੍ਰਿਤੀ_ਦਿਓ | proposed |
| cos | ਕੋਜੀਵਾ | proposed |
| exit | ਬਾਹਰ_ਨਿਕਲੋ | proposed |
| exp | ਘਾਤਾਂਕ | proposed |
| free | ਮੁਕਤ | lexicon |
| friend | ਮਿੱਤਰ | proposed |
| isalnum | ਅੱਖਰ_ਜਾਂ_ਅੰਕ | proposed |
| isalpha | ਅੱਖਰ_ਹੈ | proposed |
| isdigit | ਅੰਕ_ਹੈ | proposed |
| isspace | ਖਾਲੀ_ਥਾਂ_ਹੈ | proposed |
| log | ਲਘੂਗਣਕ | proposed |
| malloc | ਸਮ੍ਰਿਤੀ_ਦਿਓ | proposed |
| memcpy | ਸਮ੍ਰਿਤੀ_ਨਕਲ | proposed |
| operator | ਸੰਚਾਲਕ | proposed |
| pow | ਘਾਤ | proposed |
| printf | ਲਿਖੋ | proposed |
| private | ਨਿਜੀ | lexicon |
| protected | ਸੁਰੱਖਿਅਤ | lexicon |
| public | ਜਨਤਕ | lexicon |
| putchar | ਅੱਖਰ_ਲਿਖੋ | proposed |
| raise | ਉਠਾਓ | lexicon |
| read | ਪਠ | lexicon |
| signal | ਸੰਕੇਤ | lexicon |
| sin | ਜੀਵਾ | proposed |
| sqrt | ਵਰਗਮੂਲ | proposed |
| sscanf | ਲੜੀ_ਤੋਂ_ਪੜ੍ਹੋ | proposed |
| strlen | ਲੜੀ_ਲੰਬਾਈ | proposed |
| strncmp | ਲੜੀ_ਤੁਲਨਾ | proposed |
| strstr | ਲੜੀ_ਖੋਜ | proposed |
| template | ਸਾਂਚਾ | proposed |
| toupper | ਵੱਡਾ_ਅੱਖਰ | proposed |
| virtual | ਆਭਾਸੀ | lexicon |
| write | ਲਿਖ | lexicon |

### A.2 C preprocessor

Host: ISO/IEC 9899, Information technology, Programming languages, C (preprocessing directives). Names: name transformation.

| Host | Punjabi | Source |
|---|---|---|
| #define | #ਪਰਿਭਾਸ਼ਿਤ_ਕਰੋ | proposed |
| #include | #ਅਨ੍ਤਰ੍ਭਾਵ | lexicon |
| #if | #ਜੇ | lexicon |
| #ifdef | #ਜੇ_ਪਰਿਭਾਸ਼ਿਤ | proposed |
| #ifndef | #ਜੇ_ਅਪਰਿਭਾਸ਼ਿਤ | proposed |
| #else | #ਨਹੀਂਤਾਂ | lexicon |
| #elif | #ਜਾਂਜੇ | lexicon |
| #endif | #ਜੇ_ਅੰਤ | proposed |
| #undef | #ਪਰਿਭਾਸ਼ਾ_ਰੱਦ | proposed |
| #pragma | #ਹਦਾਇਤ | proposed |
| #error | #ਗਲਤੀ | proposed |
| #line | #ਸਤਰ | proposed |

### A.3 C++

Host: ISO/IEC 14882, Programming languages, C++. Names: name transformation.

| Host | Punjabi | Source |
|---|---|---|
| auto | ਸਵੈਚਾਲਿਤ | proposed |
| break | ਰੋਕੋ | lexicon |
| case | ਹਾਲਤ | lexicon |
| char | ਅੱਖਰ | lexicon |
| const | ਅਚਲ | lexicon |
| continue | ਜਾਰੀ | lexicon |
| default | ਮੂਲ | lexicon |
| do | ਕਰੋ | lexicon |
| double | ਦੁੱਗਣਾ | lexicon |
| else | ਨਹੀਂਤਾਂ | lexicon |
| enum | ਗਿਣਤੀ | lexicon |
| extern | ਬਾਹਰੀ | lexicon |
| float | ਦਸ਼ਮਲਵ | lexicon |
| for | ਲਈ | lexicon |
| goto | ਜਾਓ | lexicon |
| if | ਜੇ | lexicon |
| inline | ਸਤਰਅੰਦਰ | lexicon |
| int | ਪੂਰਨ | lexicon |
| long | ਲੰਮਾ | proposed |
| register | ਰਜਿਸਟਰ | lexicon |
| restrict | ਸੀਮਿਤ | proposed |
| return | ਵਾਪਸ | lexicon |
| short | ਛੋਟਾ | proposed |
| signed | ਨਿਸ਼ਾਨੀਵਾਲਾ | proposed |
| sizeof | ਆਕਾਰ | lexicon |
| static | ਸਥਿਰ | lexicon |
| struct | ਬਣਤਰ | lexicon |
| switch | ਚੋਣ | lexicon |
| typedef | ਕਿਸਮਪਰਿਭਾਸ਼ਾ | lexicon |
| union | ਸੰਘ | lexicon |
| unsigned | ਬਿਨਾਨਿਸ਼ਾਨੀ | proposed |
| void | ਖਾਲੀ | lexicon |
| volatile | ਅਸਥਿਰ | lexicon |
| while | ਜਦੋਂ | lexicon |
| main | ਮੁੱਖ | lexicon |
| bool | ਤਾਰਕਿਕ | lexicon |
| catch | ਫੜੋ | lexicon |
| class | ਵਰਗ | lexicon |
| delete | ਮਿਟਾਓ | proposed |
| explicit | ਸਪਸ਼ਟ | proposed |
| false | ਝੂਠ | lexicon |
| friend | ਮਿੱਤਰ | proposed |
| mutable | ਬਦਲਣਯੋਗ | proposed |
| namespace | ਨਾਮਾਕਾਸ਼ | lexicon |
| new | ਨਵਾਂ | lexicon |
| nullptr | ਖਾਲੀ_ਸੂਚਕ | proposed |
| operator | ਸੰਚਾਲਕ | proposed |
| private | ਨਿਜੀ | lexicon |
| protected | ਸੁਰੱਖਿਅਤ | lexicon |
| public | ਜਨਤਕ | lexicon |
| template | ਸਾਂਚਾ | proposed |
| this | ਇਹ | lexicon |
| throw | ਸੁੱਟੋ | lexicon |
| true | ਸੱਚ | lexicon |
| try | ਕੋਸ਼ਿਸ਼ | lexicon |
| typename | ਕਿਸਮ_ਨਾਂ | proposed |
| using | ਵਰਤੋਂ | proposed |
| virtual | ਆਭਾਸੀ | lexicon |
| cout | ਬਾਹਰ | proposed |
| cin | ਅੰਦਰ | proposed |
| endl | ਸਤਰ_ਅੰਤ | proposed |

Standard library and runtime names of the C++ binding:

| Host | Punjabi | Source |
|---|---|---|
| INT_MAX | ਵੱਧ_ਤੋਂ_ਵੱਧ_ਅੰਕ | proposed |
| NULL | ਨਿਰਾ | lexicon |
| abs | ਨਿਰਪੇਖ | proposed |
| assert | ਪ੍ਰਤਿਜ੍ਞਾ | lexicon |
| calloc | ਸਿਫਰ_ਸਮ੍ਰਿਤੀ_ਦਿਓ | proposed |
| cos | ਕੋਜੀਵਾ | proposed |
| exit | ਬਾਹਰ_ਨਿਕਲੋ | proposed |
| exp | ਘਾਤਾਂਕ | proposed |
| free | ਮੁਕਤ | lexicon |
| isalnum | ਅੱਖਰ_ਜਾਂ_ਅੰਕ | proposed |
| isalpha | ਅੱਖਰ_ਹੈ | proposed |
| isdigit | ਅੰਕ_ਹੈ | proposed |
| isspace | ਖਾਲੀ_ਥਾਂ_ਹੈ | proposed |
| left | ਖੱਬੇ | proposed |
| log | ਲਘੂਗਣਕ | proposed |
| malloc | ਸਮ੍ਰਿਤੀ_ਦਿਓ | proposed |
| memcpy | ਸਮ੍ਰਿਤੀ_ਨਕਲ | proposed |
| pipe | ਪ੍ਰਣਾਲ | lexicon |
| pow | ਘਾਤ | proposed |
| printf | ਲਿਖੋ | proposed |
| putchar | ਅੱਖਰ_ਲਿਖੋ | proposed |
| raise | ਉਠਾਓ | lexicon |
| read | ਪਠ | lexicon |
| right | ਸੱਜੇ | proposed |
| signal | ਸੰਕੇਤ | lexicon |
| sin | ਜੀਵਾ | proposed |
| sleep | ਸੁ਷ੁਪ੍ਤਿ | lexicon |
| sqrt | ਵਰਗਮੂਲ | proposed |
| sscanf | ਲੜੀ_ਤੋਂ_ਪੜ੍ਹੋ | proposed |
| strlen | ਲੜੀ_ਲੰਬਾਈ | proposed |
| strncmp | ਲੜੀ_ਤੁਲਨਾ | proposed |
| strstr | ਲੜੀ_ਖੋਜ | proposed |
| sync | ਸਮਕਾਲੀ | lexicon |
| toupper | ਵੱਡਾ_ਅੱਖਰ | proposed |
| write | ਲਿਖ | lexicon |

### A.4 Java

Host: The Java Language Specification, Oracle, current edition. Names: unchanged.

| Host | Punjabi | Source |
|---|---|---|
| abstract | ਅਮੂਰਤ | lexicon |
| assert | ਪ੍ਰਤਿਜ੍ਞਾ | lexicon |
| boolean | ਤਰਕੀ | proposed |
| break | ਰੋਕੋ | lexicon |
| byte | ਬਾਈਟ | proposed |
| case | ਹਾਲਤ | lexicon |
| catch | ਫੜੋ | lexicon |
| char | ਅੱਖਰ | lexicon |
| class | ਵਰਗ | lexicon |
| continue | ਜਾਰੀ | lexicon |
| default | ਮੂਲ | lexicon |
| do | ਕਰੋ | lexicon |
| double | ਦੁੱਗਣਾ | lexicon |
| else | ਨਹੀਂਤਾਂ | lexicon |
| enum | ਗਿਣਤੀ | lexicon |
| extends | ਵਧਾਓ | lexicon |
| final | ਅੰਤਿਮ | proposed |
| finally | ਅਖੀਰ | lexicon |
| float | ਦਸ਼ਮਲਵ | lexicon |
| for | ਲਈ | lexicon |
| if | ਜੇ | lexicon |
| implements | ਲਾਗੂ | lexicon |
| import | ਆਯਾਤ | lexicon |
| instanceof | ਨਮੂਨਾ_ਹੈ | proposed |
| int | ਪੂਰਨ | lexicon |
| interface | ਅੰਤਰਮੁਖ | lexicon |
| long | ਲੰਮਾ | proposed |
| native | ਦੇਸੀ | proposed |
| new | ਨਵਾਂ | lexicon |
| package | ਪੈਕੇਜ | lexicon |
| private | ਨਿਜੀ | lexicon |
| protected | ਸੁਰੱਖਿਅਤ | lexicon |
| public | ਜਨਤਕ | lexicon |
| return | ਵਾਪਸ | lexicon |
| short | ਛੋਟਾ | proposed |
| static | ਸਥਿਰ | lexicon |
| super | ਪਰਮ | lexicon |
| switch | ਚੋਣ | lexicon |
| synchronized | ਸਮਕਾਲੀ | proposed |
| this | ਇਹ | lexicon |
| throw | ਸੁੱਟੋ | lexicon |
| throws | ਸੁੱਟਦਾ | proposed |
| try | ਕੋਸ਼ਿਸ਼ | lexicon |
| void | ਖਾਲੀ | lexicon |
| volatile | ਅਸਥਿਰ | lexicon |
| while | ਜਦੋਂ | lexicon |
| true | ਸੱਚ | lexicon |
| false | ਝੂਠ | lexicon |
| null | ਨਿਰਾ | lexicon |
| String | ਸ਼ਬਦਮਾਲਾ | lexicon |
| System | ਪ੍ਰਣਾਲੀ | proposed |

Standard library and runtime names of the Java binding:

| Host | Punjabi | Source |
|---|---|---|
| INT_MAX | ਵੱਧ_ਤੋਂ_ਵੱਧ_ਅੰਕ | proposed |
| Object | ਵਸਤੂ | lexicon |
| Thread | ਧਾਗਾ | lexicon |
| abs | ਨਿਰਪੇਖ | proposed |
| auto | ਸਵੈਚਾਲਿਤ | proposed |
| calloc | ਸਿਫਰ_ਸਮ੍ਰਿਤੀ_ਦਿਓ | proposed |
| const | ਅਚਲ | lexicon |
| cos | ਕੋਜੀਵਾ | proposed |
| exit | ਬਾਹਰ_ਨਿਕਲੋ | proposed |
| exp | ਘਾਤਾਂਕ | proposed |
| extern | ਬਾਹਰੀ | lexicon |
| free | ਮੁਕਤ | lexicon |
| friend | ਮਿੱਤਰ | proposed |
| goto | ਜਾਓ | lexicon |
| inline | ਸਤਰਅੰਦਰ | lexicon |
| isalnum | ਅੱਖਰ_ਜਾਂ_ਅੰਕ | proposed |
| isalpha | ਅੱਖਰ_ਹੈ | proposed |
| isdigit | ਅੰਕ_ਹੈ | proposed |
| isspace | ਖਾਲੀ_ਥਾਂ_ਹੈ | proposed |
| log | ਲਘੂਗਣਕ | proposed |
| main | ਮੁੱਖ | lexicon |
| malloc | ਸਮ੍ਰਿਤੀ_ਦਿਓ | proposed |
| memcpy | ਸਮ੍ਰਿਤੀ_ਨਕਲ | proposed |
| operator | ਸੰਚਾਲਕ | proposed |
| pow | ਘਾਤ | proposed |
| printf | ਲਿਖੋ | proposed |
| println | ਸਤਰ_ਛਾਪੋ | proposed |
| putchar | ਅੱਖਰ_ਲਿਖੋ | proposed |
| raise | ਉਠਾਓ | lexicon |
| read | ਪਠ | lexicon |
| register | ਰਜਿਸਟਰ | lexicon |
| restrict | ਸੀਮਿਤ | proposed |
| signal | ਸੰਕੇਤ | lexicon |
| signed | ਨਿਸ਼ਾਨੀਵਾਲਾ | proposed |
| sin | ਜੀਵਾ | proposed |
| sizeof | ਆਕਾਰ | lexicon |
| sleep | ਸੁ਷ੁਪ੍ਤਿ | lexicon |
| sqrt | ਵਰਗਮੂਲ | proposed |
| sscanf | ਲੜੀ_ਤੋਂ_ਪੜ੍ਹੋ | proposed |
| strlen | ਲੜੀ_ਲੰਬਾਈ | proposed |
| strncmp | ਲੜੀ_ਤੁਲਨਾ | proposed |
| strstr | ਲੜੀ_ਖੋਜ | proposed |
| struct | ਬਣਤਰ | lexicon |
| template | ਸਾਂਚਾ | proposed |
| toupper | ਵੱਡਾ_ਅੱਖਰ | proposed |
| typedef | ਕਿਸਮਪਰਿਭਾਸ਼ਾ | lexicon |
| union | ਸੰਘ | lexicon |
| unsigned | ਬਿਨਾਨਿਸ਼ਾਨੀ | proposed |
| virtual | ਆਭਾਸੀ | lexicon |
| write | ਲਿਖ | lexicon |

### A.5 Python

Host: The Python Language Reference, Python Software Foundation, current version. Names: unchanged.

| Host | Punjabi | Source |
|---|---|---|
| False | ਝੂਠ | lexicon |
| None | ਕੁਝ_ਨਹੀਂ | proposed |
| True | ਸੱਚ | lexicon |
| and | ਅਤੇ | lexicon |
| as | ਇਵ | lexicon |
| assert | ਪ੍ਰਤਿਜ੍ਞਾ | lexicon |
| break | ਰੋਕੋ | lexicon |
| class | ਵਰਗ | lexicon |
| continue | ਜਾਰੀ | lexicon |
| def | ਪਰਿਭਾਸ਼ਾ | proposed |
| del | ਹਟਾਓ | proposed |
| elif | ਜਾਂਜੇ | lexicon |
| else | ਨਹੀਂਤਾਂ | lexicon |
| except | ਅਪਵਾਦ | lexicon |
| finally | ਅਖੀਰ | lexicon |
| for | ਲਈ | lexicon |
| from | ਤਃ | lexicon |
| global | ਵੈਸ਼੍ਵਿਕ | lexicon |
| if | ਜੇ | lexicon |
| import | ਆਯਾਤ | lexicon |
| in | ਵਿੱਚ | lexicon |
| is | ਹੈ | proposed |
| lambda | ਅਨਾਮ | lexicon |
| nonlocal | ਗੈਰਸਥਾਨਕ | proposed |
| not | ਨਹੀਂ | lexicon |
| or | ਜਾਂ | lexicon |
| pass | ਲੰਘੋ | proposed |
| raise | ਉਠਾਓ | lexicon |
| return | ਵਾਪਸ | lexicon |
| try | ਕੋਸ਼ਿਸ਼ | lexicon |
| while | ਜਦੋਂ | lexicon |
| with | ਨਾਲ | proposed |
| yield | ਦਿਓ | lexicon |
| print | ਛਾਪੋ | proposed |
| range | ਸੀਮਾ | proposed |
| len | ਲੰਬਾਈ | proposed |

Standard library and runtime names of the Python binding:

| Host | Punjabi | Source |
|---|---|---|
| Object | ਵਸਤੂ | lexicon |
| String | ਸ਼ਬਦਮਾਲਾ | lexicon |
| System | ਪ੍ਰਣਾਲੀ | proposed |
| Thread | ਧਾਗਾ | lexicon |
| abstract | ਅਮੂਰਤ | lexicon |
| boolean | ਤਰਕੀ | proposed |
| byte | ਬਾਈਟ | proposed |
| case | ਹਾਲਤ | lexicon |
| catch | ਫੜੋ | lexicon |
| char | ਅੱਖਰ | lexicon |
| const | ਅਚਲ | lexicon |
| default | ਮੂਲ | lexicon |
| do | ਕਰੋ | lexicon |
| double | ਦੁੱਗਣਾ | lexicon |
| extends | ਵਧਾਓ | lexicon |
| final | ਅੰਤਿਮ | proposed |
| float | ਦਸ਼ਮਲਵ | lexicon |
| goto | ਜਾਓ | lexicon |
| implements | ਲਾਗੂ | lexicon |
| instanceof | ਨਮੂਨਾ_ਹੈ | proposed |
| int | ਪੂਰਨ | lexicon |
| interface | ਅੰਤਰਮੁਖ | lexicon |
| long | ਲੰਮਾ | proposed |
| main | ਮੁੱਖ | lexicon |
| native | ਦੇਸੀ | proposed |
| new | ਨਵਾਂ | lexicon |
| package | ਪੈਕੇਜ | lexicon |
| println | ਸਤਰ_ਛਾਪੋ | proposed |
| private | ਨਿਜੀ | lexicon |
| protected | ਸੁਰੱਖਿਅਤ | lexicon |
| public | ਜਨਤਕ | lexicon |
| read | ਪਠ | lexicon |
| short | ਛੋਟਾ | proposed |
| sleep | ਸੁ਷ੁਪ੍ਤਿ | lexicon |
| sqrt | ਵਰਗਮੂਲ | proposed |
| static | ਸਥਿਰ | lexicon |
| super | ਪਰਮ | lexicon |
| switch | ਚੋਣ | lexicon |
| this | ਇਹ | lexicon |
| throw | ਸੁੱਟੋ | lexicon |
| throws | ਸੁੱਟਦਾ | proposed |
| void | ਖਾਲੀ | lexicon |
| volatile | ਅਸਥਿਰ | lexicon |
| write | ਲਿਖ | lexicon |

### A.6 BASIC

Host: ISO/IEC 10279, Information technology, Programming languages, Full BASIC. Names: name transformation.

| Host | Punjabi | Source |
|---|---|---|
| dim | ਆਕਾਰ | proposed |
| end | ਅੰਤ | lexicon |
| for | ਲਈ | lexicon |
| gosub | ਉਪ_ਜਾਓ | proposed |
| goto | ਜਾਓ | lexicon |
| if | ਜੇ | lexicon |
| input | ਲਵੋ | proposed |
| let | ਮੰਨੋ | lexicon |
| next | ਅਗਲਾ_ਗੇੜ | proposed |
| print | ਛਾਪੋ | proposed |
| rem | ਟਿੱਪਣੀ | proposed |
| return | ਵਾਪਸ | lexicon |
| step | ਕਦਮ_ਨਾਲ | proposed |
| then | ਤਾਂ | proposed |
| to | ਤੱਕ | proposed |
| wend | ਜਦੋਂਤੱਕ_ਅੰਤ | proposed |
| while | ਜਦੋਂ | lexicon |
| and | ਅਤੇ | lexicon |
| or | ਜਾਂ | lexicon |
| not | ਨਹੀਂ | lexicon |
| mod | ਬਾਕੀ | proposed |

Standard library and runtime names of the BASIC binding:

| Host | Punjabi | Source |
|---|---|---|
| AS | ਇਵ | lexicon |
| CALL | ਬੁਲਾਓ | lexicon |
| CONST | ਅਚਲ | lexicon |
| DO | ਕਰੋ | lexicon |
| ELSE | ਨਹੀਂਤਾਂ | lexicon |
| INT | ਪੂਰਨ | lexicon |
| SHARED | ਸਹਭਾਜਿਤ | lexicon |
| STATIC | ਸਥਿਰ | lexicon |
| STRING | ਸ਼ਬਦਮਾਲਾ | lexicon |
| TIMER | ਕਾਲਯਨ੍ਤ੍ਰ | lexicon |

### A.7 LOGO

Host: No international standard; the host is the Berkeley Logo dialect (bibliography). Names: name transformation.

| Host | Punjabi | Source |
|---|---|---|
| forward | ਅਗ੍ਰਪ੍ਰਸਾਰ | lexicon |
| back | ਪਿੱਛੇ | proposed |
| left | ਖੱਬੇ | proposed |
| right | ਸੱਜੇ | proposed |
| penup | ਕਲਮ_ਚੁੱਕੋ | proposed |
| pendown | ਕਲਮ_ਰੱਖੋ | proposed |
| repeat | ਦੁਹਰਾਓ | proposed |
| to | ਤੱਕ | proposed |
| end | ਅੰਤ | lexicon |
| make | ਬਣਾਓ | proposed |
| if | ਜੇ | lexicon |
| ifelse | ਜੇ_ਨਹੀਂਤਾਂ | proposed |
| home | ਘਰ | proposed |
| clearscreen | ਪਰਦਾ_ਸਾਫ | proposed |

Standard library and runtime names of the LOGO binding:

| Host | Punjabi | Source |
|---|---|---|
| print | ਛਾਪੋ | proposed |

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

The lowering of Punjabi programs to C is verified by the reference implementation: runs, same output. Source Chintamani means a word of the original Hindawi transducers; lexicon, a word of the language's lexicon; proposed, a word proposed by the project and not yet reviewed by the language community.

## Annex C (normative) Script filter

The script filter maps each letter and sign of the script to the Devanagari letter or sign of the same Unicode name, as generated by lang/hindawi/tools/script_filters.py.

## Annex D (informative) Rights and provenance

This document is an original work. It defines new programming languages by reference to the host language standards listed in Clause 2 and reproduces no text from them. Permission to adopt, translate or publish it as a standard is given by the copyright holder to a standards body on request.

Single words and the keywords of the host languages are not reproduced from any copyrighted text; the native words of Annex A were chosen by the Hindawi project, taken from the language's lexicon in the Hindawi repository, or, for Hindi, taken from the Chintamani transducers of the original Hindawi, whose author holds their copyright.

## Bibliography

- Hindawi 2026.10, hindawiai/hindawi2026.10, the reference implementation
- Chintamani, hindawiai/chintamani, the Hindawi transducers and the Romenagri tools
- Berkeley Logo reference manual, Brian Harvey

