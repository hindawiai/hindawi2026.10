# HLS pa 2026.10

**Information technology, Programming languages, Punjabi keyword bindings for C, C++, Java, Python, BASIC and LOGO, and their lowering to the host language standards**

Edition 2026.10, draft proposal, 2026-10-18. © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

## Foreword

This draft is proposed by Abhishek Choudhary, AyeAI, for consideration by the Data Management System Sectional Committee, LITD 15, of the Bureau of Indian Standards, whose scope includes programming languages, their environments and system software interfaces. It is an indigenous draft: it adopts no International Standard, binds the language it names to the host programming language standards listed in Clause 2 by reference, and reproduces no text from them.

The method it standardizes was first published as the Hindawi Programming System on 15 August 2004, and has been developed since through the Hindawi releases. This draft is generated from the Punjabi cell of Hindawi 2026.10 by lang/hindawi/tools/standards.py, so that the document and its reference implementation cannot diverge; a revision of either is a revision of both.

Annexes A, B and C are normative. Annexes D, E and F are informative.

Every binding in Annex A records its provenance. A binding recorded as proposed has not yet been reviewed by the Punjabi language community; its review is part of the work towards an Indian Standard.

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. Hindawi™ and Romenagri™ are trademarks of Abhishek Choudhary. This document is an original work. It defines new programming languages by reference to the host language standards listed in Clause 2 and reproduces no text from them. Permission to adopt, translate or publish it as a standard is given by the copyright holder to a standards body on request.

## Introduction

A program has three properties that this draft keeps apart: the script it is written in, the human language its words come from, and the programming language standard that defines its meaning. The script is handled by transliteration, the language by the keyword bindings of Annex A, and the meaning by the host standard, which this draft does not alter.

A source text in the language is lowered to a source text of the host language and compiled by any conforming host translator. Native names reach the compiled program, and the debugger, in one fixed transliterated form, so that a program written in the language remains readable in that language at every level down to the machine.

## 1 Scope

This draft specifies, for programs written in Punjabi in the Gurmukhi script:

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

3.3 native keyword: a word of Punjabi, written in the Gurmukhi script, bound by Annex A to a host keyword.

3.4 binding: the pairing of one host keyword with one native keyword, for one host language.

3.5 construct: the programming construct a keyword denotes, which is the same across host languages, so that one native keyword serves it in every binding.

3.6 source text: a program, or part of one, written using native keywords, native names, or both.

3.7 native name: an identifier of a source text written wholly or partly in the Gurmukhi script.

3.8 lowering: the transformation of a source text into a source text of the host language.

3.9 C-level form: the identifier of the host language that a native name becomes by name transformation, and under which it appears in compiled programs and to debuggers.

3.10 name transformation: the mapping of native names to C-level forms specified in Clause 9.

3.11 script filter: the mapping of the Gurmukhi script to Devanagari that precedes transliteration, specified in Annex C.

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

6.2 Native letters are the characters of the Gurmukhi block of ISO/IEC 10646 whose general category is a letter or a mark. Text written right to left is stored in logical order.

6.3 The Gurmukhi script is written left to right.

6.4 The native digits below are equivalent, in numerals, to the decimal digits of the host language with the same value. A translator shall accept either.

| Code point | Digit | Value |
|---|---|---|
| U+0A66 | ੦ | 0 |
| U+0A67 | ੧ | 1 |
| U+0A68 | ੨ | 2 |
| U+0A69 | ੩ | 3 |
| U+0A6A | ੪ | 4 |
| U+0A6B | ੫ | 5 |
| U+0A6C | ੬ | 6 |
| U+0A6D | ੭ | 7 |
| U+0A6E | ੮ | 8 |
| U+0A6F | ੯ | 9 |

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

The bindings of Annex A are maintained as a living register. A proposed binding becomes reviewed when the Punjabi language community accepts it; a change to a reviewed binding is a revision of this draft. The construct, not the host keyword, is primary: one native keyword serves one construct in every binding where that construct occurs.

## Annex A (normative) Keyword bindings

### A.1 C

Host standard: ISO/IEC 9899, Information technology, Programming languages, C. Names are lowered by name transformation.

| Host keyword | Punjabi | Provenance |
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

### A.2 C preprocessor

Host standard: ISO/IEC 9899, Information technology, Programming languages, C (preprocessing directives). Names are lowered by name transformation.

| Host keyword | Punjabi | Provenance |
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

Host standard: ISO/IEC 14882, Programming languages, C++. Names are lowered by name transformation.

| Host keyword | Punjabi | Provenance |
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

### A.4 Java

Host standard: The Java Language Specification, Oracle, current edition. Names are lowered by unchanged.

| Host keyword | Punjabi | Provenance |
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

### A.5 Python

Host standard: The Python Language Reference, Python Software Foundation, current version. Names are lowered by unchanged.

| Host keyword | Punjabi | Provenance |
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

### A.6 BASIC

Host standard: ISO/IEC 10279, Information technology, Programming languages, Full BASIC. Names are lowered by name transformation.

| Host keyword | Punjabi | Provenance |
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

### A.7 LOGO

Host standard: No international standard; the host is the Berkeley Logo dialect (bibliography). Names are lowered by name transformation.

| Host keyword | Punjabi | Provenance |
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

## Annex B (normative) Name transformation test vectors

Each native name shall be given the C-level form shown. The vectors are computed by the reference implementation when this draft is generated.

| Native name | C-level form |
|---|---|
| ਅਗਲਾ | _agalaa |
| ਅਗੇਤਰ | _agaee_tara |
| ਅਣਵਰਤਿਆ | _a_nnawara_ti_aa |
| ਅਦਲਾ_ਬਦਲੀ | _a_dalaa_ba_dalee |
| ਅਧਾਰ | _a_dhaara |
| ਅਨੁਪਾਤ | _anupaa_ta |
| ਅਸਿੱਧਾ | _asi_dhaa |
| ਅੰਕੜੇ | _a_mka_rraee |
| ਅੰਤ | _a_m_ta |
| ਅੰਦਰਲੀ_ਡਿਗਰੀ | _a_m_daralee_digaree |
| ਅੰਦਰੂਨੀ | _a_m_daroonee |
| ਆਉਣ_ਵਾਲਾ | _aa_u_nna_waalaa |
| ਆਖਰੀ | _aakharee |
| ਆਮਦ | _aama_da |
| ਆਰਜ਼ੀ | _aarajzee |
| ਇਕਸਾਰ | _ikasaara |
| ਇੰਦਰਾਜ | _i_m_daraaja |
| ਇੱਕੋ_ਵੇਲੇ | _ikoa_waeelaee |
| ਉਚਾਈ | _uchaa_ee |
| ਉਛਾਲ | _uchhaala |
| ਉਡੀਕ | _udeeka |
| ਉਤਪਾਦਕ | _u_tapaa_daka |
| ਉਪਲਬਧ | _upalaba_dha |
| ਉਲਟ | _ulata |
| ਉੱਚਾ | _uchaa |
| ਉੱਤਮ | _u_tama |
| ਉੱਤਮ_ਖਾਨਾਬੱਧ | _u_tama_khaanaaba_dha |
| ਉੱਤਮ_ਸ਼ੁੱਧ | _u_tama_szu_dha |
| ਉੱਤਰਾਧਿਕਾਰੀ | _u_taraa_dhikaaree |
| ਉੱਤਲਾ | _u_talaa |

## Annex C (normative) Script filter

The Gurmukhi script is mapped to Devanagari letter by letter, by Unicode character name: each letter of the Gurmukhi block maps to the Devanagari letter of the same name.

Gurmukhi signs named differently from Devanagari are mapped by alias: bindi and tippi to anusvara, the vowel signs EE and OO to E and O. Addak has no Devanagari sign and is dropped.

## Annex D (informative) Library names

### D C

| Host name | Punjabi | Provenance |
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

### D C++

| Host name | Punjabi | Provenance |
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

### D Java

| Host name | Punjabi | Provenance |
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

### D Python

| Host name | Punjabi | Provenance |
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

### D BASIC

| Host name | Punjabi | Provenance |
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

### D LOGO

| Host name | Punjabi | Provenance |
|---|---|---|
| print | ਛਾਪੋ | proposed |

## Annex E (informative) Conformance tests

The reference implementation is tested with the programs of samples/gate in the Hindawi repository, which cover the programming content of the GATE Computer Science paper. Recorded on 2026-10-18: 113 of 113 C programs, written in Punjabi, were lowered, compiled and run, and printed exactly what their English originals print; 1 of 1 Python programs did the same; 117 of 117 files were reversed byte for byte.

The program below, as written in the language, its transliterated form, and the C that the transducer gives:

### E source

```
#ਅਨ੍ਤਰ੍ਭਾਵ <stdio.h>
/* binary search in a sorted array */
ਪੂਰਨ ਦੁਆਧਾਰੀ_ਖੋਜ(ਪੂਰਨ ਮੁੱਲ[], ਪੂਰਨ ਗਿਣਤੀ_2, ਪੂਰਨ ਕੁੰਜੀ) {
  ਪੂਰਨ ਨੀਵਾਂ = 0, ਉੱਚਾ = ਗਿਣਤੀ_2 - 1;
  ਜਦੋਂ (ਨੀਵਾਂ <= ਉੱਚਾ) {
    ਪੂਰਨ ਵਿਚਕਾਰ = ਨੀਵਾਂ + (ਉੱਚਾ - ਨੀਵਾਂ) / 2;
    ਜੇ (ਮੁੱਲ[ਵਿਚਕਾਰ] == ਕੁੰਜੀ) ਵਾਪਸ ਵਿਚਕਾਰ;
    ਜੇ (ਮੁੱਲ[ਵਿਚਕਾਰ] < ਕੁੰਜੀ) ਨੀਵਾਂ = ਵਿਚਕਾਰ + 1; ਨਹੀਂਤਾਂ ਉੱਚਾ = ਵਿਚਕਾਰ - 1;
  }
  ਵਾਪਸ -1;
}
ਪੂਰਨ ਮੁੱਖ(ਖਾਲੀ) {
  ਪੂਰਨ ਮੁੱਲ[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  ਲਿਖੋ("%d %d\n", ਦੁਆਧਾਰੀ_ਖੋਜ(ਮੁੱਲ, 10, 23), ਦੁਆਧਾਰੀ_ਖੋਜ(ਮੁੱਲ, 10, 7));
  ਵਾਪਸ 0;
}
```

### E script filter

```
#अन्तर्भाव <stdio.h>
/* binary search in a sorted array */
पूरन दुआधारी_खोज(पूरन मुल[], पूरन गिणती_2, पूरन कुंजी) {
  पूरन नीवां = 0, उचा = गिणती_2 - 1;
  जदों (नीवां <= उचा) {
    पूरन विचकार = नीवां + (उचा - नीवां) / 2;
    जे (मुल[विचकार] == कुंजी) वापस विचकार;
    जे (मुल[विचकार] < कुंजी) नीवां = विचकार + 1; नहींतां उचा = विचकार - 1;
  }
  वापस -1;
}
पूरन मुख(खाली) {
  पूरन मुल[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  लिखो("%d %d\n", दुआधारी_खोज(मुल, 10, 23), दुआधारी_खोज(मुल, 10, 7));
  वापस 0;
}
```

### E Romenagri

```
#_an_tarbhaawa <stdio.h>
/* binary search in a sorted array */
poorana _du_aa_dhaaree_khoaja(poorana mula[], poorana gi_nna_tee_2, poorana ku_mjee) {
  poorana neewaa_m = 0, _uchaa = gi_nna_tee_2 - 1;
  ja_doa_m (neewaa_m <= _uchaa) {
    poorana wichakaara = neewaa_m + (_uchaa - neewaa_m) / 2;
    jaee (mula[wichakaara] == ku_mjee) waapasa wichakaara;
    jaee (mula[wichakaara] < ku_mjee) neewaa_m = wichakaara + 1; na_hee_m_taa_m _uchaa = wichakaara - 1;
  }
  waapasa -1;
}
poorana mukha(khaalee) {
  poorana mula[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  likhoa("%d %d\n", _du_aa_dhaaree_khoaja(mula, 10, 23), _du_aa_dhaaree_khoaja(mula, 10, 7));
  waapasa 0;
}
```

### E C

```
#include <stdio.h>
/* binary search in a sorted array */
int _du_aa_dhaaree_khoaja(int mula[], int gi_nna_tee_2, int ku_mjee) {
  int neewaa_m = 0, _uchaa = gi_nna_tee_2 - 1;
  while (neewaa_m <= _uchaa) {
    int wichakaara = neewaa_m + (_uchaa - neewaa_m) / 2;
    if (mula[wichakaara] == ku_mjee) return wichakaara;
    if (mula[wichakaara] < ku_mjee) neewaa_m = wichakaara + 1; else _uchaa = wichakaara - 1;
  }
  return -1;
}
int main(void) {
  int mula[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  printf("%d %d\n", _du_aa_dhaaree_khoaja(mula, 10, 23), _du_aa_dhaaree_khoaja(mula, 10, 7));
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

