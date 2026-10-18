# HLS kn 2026.10

**Information technology, Programming languages, Kannada keyword bindings for C, C++, Java, Python, BASIC and LOGO, and their lowering to the host language standards**

Edition 2026.10, draft proposal, 2026-10-18. © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

## Foreword

This draft is proposed by Abhishek Choudhary, AyeAI, for consideration by the Data Management System Sectional Committee, LITD 15, of the Bureau of Indian Standards, whose scope includes programming languages, their environments and system software interfaces. It is an indigenous draft: it adopts no International Standard, binds the language it names to the host programming language standards listed in Clause 2 by reference, and reproduces no text from them.

The method it standardizes was first published as the Hindawi Programming System on 15 August 2004, and has been developed since through the Hindawi releases. This draft is generated from the Kannada cell of Hindawi 2026.10 by lang/hindawi/tools/standards.py, so that the document and its reference implementation cannot diverge; a revision of either is a revision of both.

Annexes A, B and C are normative. Annexes D, E and F are informative.

Every binding in Annex A records its provenance. A binding recorded as proposed has not yet been reviewed by the Kannada language community; its review is part of the work towards an Indian Standard.

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. Hindawi™ and Romenagri™ are trademarks of Abhishek Choudhary. This document is an original work. It defines new programming languages by reference to the host language standards listed in Clause 2 and reproduces no text from them. Permission to adopt, translate or publish it as a standard is given by the copyright holder to a standards body on request.

## Introduction

A program has three properties that this draft keeps apart: the script it is written in, the human language its words come from, and the programming language standard that defines its meaning. The script is handled by transliteration, the language by the keyword bindings of Annex A, and the meaning by the host standard, which this draft does not alter.

A source text in the language is lowered to a source text of the host language and compiled by any conforming host translator. Native names reach the compiled program, and the debugger, in one fixed transliterated form, so that a program written in the language remains readable in that language at every level down to the machine.

## 1 Scope

This draft specifies, for programs written in Kannada in the Kannada script:

- the encoding and character repertoire of source text (Clause 6);
- the lexical structure of source text, where it differs from the host language (Clause 7);
- the keyword bindings of the language for C, the C preprocessor, C++, Java, Python, BASIC and LOGO (Annex A);
- the lowering of a source text to a source text of the host language (Clause 8);
- the transformation of native names to identifiers of the host language (Clause 9, Annexes B and C);
- the requirements for conformance of programs and of translators (Clause 5).

This draft does not specify the semantics of any host language, which remain those of its standard; the names of host libraries, which are informative (Annex D); or any execution environment.

## 2 Normative references

The following documents are referred to in the text in such a way that some or all of their content constitutes requirements of this draft. For dated references, only the edition cited applies. For undated references, the latest edition of the referenced document, including any amendments, applies.

- ISO/IEC 9899, Information technology, Programming languages, C
- ISO/IEC 9899, Information technology, Programming languages, C (preprocessing directives)
- ISO/IEC 14882, Programming languages, C++
- The Java Language Specification, Oracle, current edition
- The Python Language Reference, Python Software Foundation, current version
- ISO/IEC 10279, Information technology, Programming languages, Full BASIC
- ISO/IEC 10646, Information technology, Universal coded character set (UCS)
- Unicode Standard Annex #15, Unicode normalization forms
- Unicode Standard Annex #31, Unicode identifiers and syntax
- ISO/IEC 14977, Information technology, Syntactic metalanguage, Extended BNF
- IS 13194 : 1991, Indian Script Code for Information Interchange, ISCII

## 3 Terms and definitions

3.1 host language: a programming language defined by a standard listed in Clause 2, into which a source text is lowered.

3.2 host keyword: a reserved word or directive name of a host language.

3.3 native keyword: a word of Kannada, written in the Kannada script, bound by Annex A to a host keyword.

3.4 binding: the pairing of one host keyword with one native keyword, for one host language.

3.5 construct: the programming construct a keyword denotes, which is the same across host languages, so that one native keyword serves it in every binding.

3.6 source text: a program, or part of one, written using native keywords, native names, or both.

3.7 native name: an identifier of a source text written wholly or partly in the Kannada script.

3.8 lowering: the transformation of a source text into a source text of the host language.

3.9 C-level form: the identifier of the host language that a native name becomes by name transformation, and under which it appears in compiled programs and to debuggers.

3.10 name transformation: the mapping of native names to C-level forms specified in Clause 9.

3.11 script filter: the mapping of the Kannada script to Devanagari that precedes transliteration, specified in Annex C.

3.12 translator: a program that performs lowering and name transformation.

3.13 reversal: the transformation of a host-language source text into a source text of the language, through a dictionary of names kept with the program.

3.14 provenance: the record of where a binding came from: the 2004 Hindawi transducers, a language lexicon, or a proposal awaiting review.

## 4 Abbreviated terms

- ACII, the eight-bit form of Indic text used by the Romenagri tools, derived from ISCII
- BURP, Bidirectional Universal Resource Parser, the reference implementation of reversal
- EBNF, Extended Backus-Naur Form as specified in ISO/IEC 14977
- ISCII, Indian Script Code for Information Interchange, IS 13194
- NFC, Normalization Form C of Unicode Standard Annex #15
- UCS, the Universal Coded Character Set of ISO/IEC 10646

## 5 Conformance

5.1 A conforming program shall be a source text whose lowering according to Clause 8 is a program that conforms to the standard of its host language.

5.2 A conforming translator shall accept every conforming program, shall lower it as Clause 8 requires, using the bindings of Annex A, and shall transform its native names as Clause 9 requires, giving for every name in Annex B the C-level form that annex gives.

5.3 A claim of conformance shall name the bindings of Annex A it covers. A translator conforming for C covers the bindings of A.1 and A.2.

5.4 A translator that provides reversal shall reproduce the original host-language source text byte for byte from its lowering and the dictionary of names kept with it.

## 6 Source text

6.1 Source text shall be encoded in UTF-8, as specified in ISO/IEC 10646, and shall be in Normalization Form C.

6.2 Native letters are the characters of the Kannada block of ISO/IEC 10646 whose general category is a letter or a mark. Text written right to left is stored in logical order.

6.3 The Kannada script is written left to right.

6.4 The native digits below are equivalent, in numerals, to the decimal digits of the host language with the same value. A translator shall accept either.

| Code point | Digit | Value |
|---|---|---|
| U+0CE6 | ೦ | 0 |
| U+0CE7 | ೧ | 1 |
| U+0CE8 | ೨ | 2 |
| U+0CE9 | ೩ | 3 |
| U+0CEA | ೪ | 4 |
| U+0CEB | ೫ | 5 |
| U+0CEC | ೬ | 6 |
| U+0CED | ೭ | 7 |
| U+0CEE | ೮ | 8 |
| U+0CEF | ೯ | 9 |

## 7 Lexical structure

7.1 The lexical structure of a source text is that of its host language, with the additions given below in the notation of ISO/IEC 14977.

```
native letter    = ? a character of 6.2 ? ;
latin letter     = ? A to Z or a to z ? ;
digit            = ? 0 to 9, or a native digit of 6.4 ? ;
name start       = native letter | latin letter | "_" ;
identifier       = name start , { name start | digit } ;
native keyword   = ? an entry of the native column of Annex A ? ;
directive        = "#" , ( native keyword | host keyword ) ;
word             = native keyword | identifier ;
```

7.2 A native keyword is recognized only as a whole word. A word of which a native keyword is a proper part is an identifier.

7.3 Character literals, string literals and comments are those of the host language; their content may be written in any script and is not altered by lowering.

7.4 A host keyword written in its host form is accepted unchanged, so that a source text may mix native and host keywords.

## 8 Lowering

8.1 Lowering shall replace each native keyword by the host keyword Annex A binds it to, for the host language of the source text; shall leave literals and comments unaltered; shall replace each native digit by the host digit of the same value; and shall transform each native name as Clause 9 requires.

8.2 Lowering shall not reorder, insert or remove any other token. The lowered text shall have the same line structure as the source text.

NOTE: The reference implementation lowers in three steps: the script filter of Annex C, transliteration by the Romenagri tools, and the language's transducer for the host language, a lexical analyser built from the bindings of Annex A. Lowering is performed on the transliterated form; Unicode text is never compiled directly.

## 9 Name transformation

9.1 Name transformation shall be deterministic, and shall give one native name the same C-level form wherever the name stands in a program.

9.2 Every C-level form shall be an identifier of the host language.

9.3 Two different native names of one program shall not be given the same C-level form; a translator shall report such a collision as an error.

9.4 A name written wholly in Latin letters, digits and underscores is not transformed.

9.5 The C-level forms of the names in Annex B are normative. They are those of the Romenagri transliteration applied, word by word, to the output of the script filter of Annex C.

## 10 Reversal

Reversal is optional. A translator that provides it shall keep with each program a dictionary of its native names, and shall satisfy 5.4.

## 11 Maintenance of the bindings

The bindings of Annex A are maintained as a living register. A proposed binding becomes reviewed when the Kannada language community accepts it; a change to a reviewed binding is a revision of this draft. The construct, not the host keyword, is primary: one native keyword serves one construct in every binding where that construct occurs.

## Annex A (normative) Keyword bindings

### A.1 C

Host standard: ISO/IEC 9899, Information technology, Programming languages, C. Names are lowered by name transformation.

| Host keyword | Kannada | Provenance |
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

### A.2 C preprocessor

Host standard: ISO/IEC 9899, Information technology, Programming languages, C (preprocessing directives). Names are lowered by name transformation.

| Host keyword | Kannada | Provenance |
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

Host standard: ISO/IEC 14882, Programming languages, C++. Names are lowered by name transformation.

| Host keyword | Kannada | Provenance |
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

### A.4 Java

Host standard: The Java Language Specification, Oracle, current edition. Names are lowered by unchanged.

| Host keyword | Kannada | Provenance |
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

### A.5 Python

Host standard: The Python Language Reference, Python Software Foundation, current version. Names are lowered by unchanged.

| Host keyword | Kannada | Provenance |
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

### A.6 BASIC

Host standard: ISO/IEC 10279, Information technology, Programming languages, Full BASIC. Names are lowered by name transformation.

| Host keyword | Kannada | Provenance |
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

### A.7 LOGO

Host standard: No international standard; the host is the Berkeley Logo dialect (bibliography). Names are lowered by name transformation.

| Host keyword | Kannada | Provenance |
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

## Annex B (normative) Name transformation test vectors

Each native name shall be given the C-level form shown. The vectors are computed by the reference implementation when this draft is generated.

| Native name | C-level form |
|---|---|
| ಅಂಚು | _a_mchu |
| ಅಂಚುಗಳು | _a_mchugalvru |
| ಅಂಶ | _a_msha |
| ಅಂಶಗಳು | _a_mshagalvru |
| ಅಕ್ಷರಸರಣಿಗಳು | _akxarasara_nnigalvru |
| ಅಗಲ | _agala |
| ಅಚ್ಚು | _achchu |
| ಅಟ್ಟಿ | _atti |
| ಅಟ್ಟಿ_2 | _atti_2 |
| ಅಡಚಣೆ_ಚಕ್ರಗಳು | _adacha_nnae_chakragalvru |
| ಅಡ್ಡಸಾಲು | _addasaalu |
| ಅಡ್ಡಸಾಲುಗಳು | _addasaalugalvru |
| ಅತಿಕಡಿಮೆ | _a_tikadimae |
| ಅತಿಚಿಕ್ಕ | _a_tichikka |
| ಅತಿದೊಡ್ಡ | _a_ti_dowdda |
| ಅತಿಪ್ರವಾಹ | _a_tiprawaa_ha |
| ಅತಿಹ್ರಸ್ವ | _a_ti_hraswa |
| ಅತ್ಯಂತಆಳ | _a_tya_m_ta_aalvra |
| ಅದಲುಬದಲು | _a_daluba_dalu |
| ಅಧೋ | _a_dhoa |
| ಅನುಪಾತ | _anupaa_ta |
| ಅಪವರ್ತ್ಯ | _apawar_tya |
| ಅಪವರ್ತ್ಯಲಬ್ಧ | _apawar_tyalab_dha |
| ಅಭಿವ್ಯಕ್ತಿ | _abhiwyak_ti |
| ಅವಧಿ | _awa_dhi |
| ಅವಧಿ_ಚಕ್ರಗಳು | _awa_dhi_chakragalvru |
| ಅವಧಿ_ಸಿದ್ಧತೆ | _awa_dhi_si_d_dha_tae |
| ಆಂತರಿಕ | _aa_m_tarika |
| ಆಗಮನ | _aagamana |
| ಆದ್ಯತೆ | _aa_dya_tae |

## Annex C (normative) Script filter

The Kannada script is mapped to Devanagari letter by letter, by Unicode character name: each letter of the Kannada block maps to the Devanagari letter of the same name.

## Annex D (informative) Library names

### D C

| Host name | Kannada | Provenance |
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

### D C++

| Host name | Kannada | Provenance |
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

### D Java

| Host name | Kannada | Provenance |
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

### D Python

| Host name | Kannada | Provenance |
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

### D BASIC

| Host name | Kannada | Provenance |
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

### D LOGO

| Host name | Kannada | Provenance |
|---|---|---|
| print | ಮುದ್ರಿಸು | proposed |

## Annex E (informative) Conformance tests

The reference implementation is tested with the programs of samples/gate in the Hindawi repository, which cover the programming content of the GATE Computer Science paper. Recorded on 2026-10-18: 113 of 113 C programs, written in Kannada, were lowered, compiled and run, and printed exactly what their English originals print; 1 of 1 Python programs did the same; 117 of 117 files were reversed byte for byte.

The program below, as written in the language, its transliterated form, and the C that the transducer gives:

### E source

```
#ಅನ್ತರ್ಭಾವ <stdio.h>
/* binary search in a sorted array */
ಪೂರ್ಣಾಂಕ ದ್ವಿಮಾನ_ಹುಡುಕು(ಪೂರ್ಣಾಂಕ ಮೌಲ್ಯಗಳು[], ಪೂರ್ಣಾಂಕ ಎಣಿಕೆ_2, ಪೂರ್ಣಾಂಕ ಕೀಲಿ) {
  ಪೂರ್ಣಾಂಕ ಕೆಳಗಿನ = 0, ಮೇಲಿನ = ಎಣಿಕೆ_2 - 1;
  ಆಗ (ಕೆಳಗಿನ <= ಮೇಲಿನ) {
    ಪೂರ್ಣಾಂಕ ಮಧ್ಯ = ಕೆಳಗಿನ + (ಮೇಲಿನ - ಕೆಳಗಿನ) / 2;
    ಆದರೆ (ಮೌಲ್ಯಗಳು[ಮಧ್ಯ] == ಕೀಲಿ) ಹಿಂತಿರುಗಿ ಮಧ್ಯ;
    ಆದರೆ (ಮೌಲ್ಯಗಳು[ಮಧ್ಯ] < ಕೀಲಿ) ಕೆಳಗಿನ = ಮಧ್ಯ + 1; ಇಲ್ಲದಿದ್ದರೆ ಮೇಲಿನ = ಮಧ್ಯ - 1;
  }
  ಹಿಂತಿರುಗಿ -1;
}
ಪೂರ್ಣಾಂಕ ಮುಖ್ಯ(ಶೂನ್ಯ) {
  ಪೂರ್ಣಾಂಕ ಮೌಲ್ಯಗಳು[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  ಬರೆ("%d %d\n", ದ್ವಿಮಾನ_ಹುಡುಕು(ಮೌಲ್ಯಗಳು, 10, 23), ದ್ವಿಮಾನ_ಹುಡುಕು(ಮೌಲ್ಯಗಳು, 10, 7));
  ಹಿಂತಿರುಗಿ 0;
}
```

### E script filter

```
#अन्तर्भाव <stdio.h>
/* binary search in a sorted array */
पूर्णांक द्विमान_हुडुकु(पूर्णांक मौल्यगळु[], पूर्णांक ऎणिकॆ_2, पूर्णांक कीलि) {
  पूर्णांक कॆळगिन = 0, मेलिन = ऎणिकॆ_2 - 1;
  आग (कॆळगिन <= मेलिन) {
    पूर्णांक मध्य = कॆळगिन + (मेलिन - कॆळगिन) / 2;
    आदरॆ (मौल्यगळु[मध्य] == कीलि) हिंतिरुगि मध्य;
    आदरॆ (मौल्यगळु[मध्य] < कीलि) कॆळगिन = मध्य + 1; इल्लदिद्दरॆ मेलिन = मध्य - 1;
  }
  हिंतिरुगि -1;
}
पूर्णांक मुख्य(शून्य) {
  पूर्णांक मौल्यगळु[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  बरॆ("%d %d\n", द्विमान_हुडुकु(मौल्यगळु, 10, 23), द्विमान_हुडुकु(मौल्यगळु, 10, 7));
  हिंतिरुगि 0;
}
```

### E Romenagri

```
#_an_tarbhaawa <stdio.h>
/* binary search in a sorted array */
poor_nnaa_mka _dwimaana__huduku(poor_nnaa_mka moulyagalvru[], poor_nnaa_mka _ae_nnikae_2, poor_nnaa_mka keeli) {
  poor_nnaa_mka kaelvragina = 0, maeelina = _ae_nnikae_2 - 1;
  _aaga (kaelvragina <= maeelina) {
    poor_nnaa_mka ma_dhya = kaelvragina + (maeelina - kaelvragina) / 2;
    _aa_darae (moulyagalvru[ma_dhya] == keeli) _hi_m_tirugi ma_dhya;
    _aa_darae (moulyagalvru[ma_dhya] < keeli) kaelvragina = ma_dhya + 1; _illa_di_d_darae maeelina = ma_dhya - 1;
  }
  _hi_m_tirugi -1;
}
poor_nnaa_mka mukhya(shoonya) {
  poor_nnaa_mka moulyagalvru[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  barae("%d %d\n", _dwimaana__huduku(moulyagalvru, 10, 23), _dwimaana__huduku(moulyagalvru, 10, 7));
  _hi_m_tirugi 0;
}
```

### E C

```
#include <stdio.h>
/* binary search in a sorted array */
int _dwimaana__huduku(int moulyagalvru[], int _ae_nnikae_2, int keeli) {
  int kaelvragina = 0, maeelina = _ae_nnikae_2 - 1;
  while (kaelvragina <= maeelina) {
    int ma_dhya = kaelvragina + (maeelina - kaelvragina) / 2;
    if (moulyagalvru[ma_dhya] == keeli) return ma_dhya;
    if (moulyagalvru[ma_dhya] < keeli) kaelvragina = ma_dhya + 1; else maeelina = ma_dhya - 1;
  }
  return -1;
}
int main(void) {
  int moulyagalvru[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  printf("%d %d\n", _dwimaana__huduku(moulyagalvru, 10, 23), _dwimaana__huduku(moulyagalvru, 10, 7));
  return 0;
}
```

## Annex F (informative) Provenance of the bindings

| Provenance | Bindings |
|---|---|
| lexicon | 156 |
| proposed | 74 |

## Bibliography

- Hindawi Programming System, first public release 15 August 2004, savannah.nongnu.org/projects/hindawi
- Chintamani, hindawiai/chintamani: the Hindawi transducers and the Romenagri tools
- Hindawi 2026.10, hindawiai/hindawi2026.10, concept DOI 10.5281/zenodo.23424410
- IS 12 : 2005, Guide for drafting and presentation of Indian Standards
- ISO/IEC 10279, Information technology, Programming languages, Full BASIC
- Berkeley Logo reference manual, Brian Harvey

