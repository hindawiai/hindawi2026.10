# HLS bn 2026.10

**Bengali bindings for programming languages: lexical mapping and lowering to the host standards**

Edition 2026.10, working draft, 2026-10-18. © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

## Foreword

This document was prepared by AyeAI, Hindawi project (Project ILM). It is generated from the Bengali cell of Hindawi 2026.10 by lang/hindawi/tools/standards.py, so that the published standard and the reference implementation cannot drift apart. Its stage is a working draft: the words marked proposed in Annex A await review by the Bengali language community, through the review pages of the Hindawi project.

## Introduction

This document lets programs be written in Bengali, in the Bengali script, in each of the programming languages listed in Clause 1. Each binding is a programming language in its own right, Bengali C for example, whose programs are lowered by the function defined in Clause 6 to programs of the host language, and are then processed by any conforming implementation of the host standard. The host standards are incorporated by reference and are not restated. Names keep a defined form down to object code (Clause 7), so programs written in Bengali remain debuggable at the level of firmware, kernels and libraries.

## 1 Scope

This document specifies, for the Bengali language written in the Bengali script, bindings to the following host programming languages: C, C preprocessor, C++, Java, Python, BASIC, LOGO. For each binding it specifies the native keywords and directives, the lowering of native programs to host programs, the treatment of names, and the requirements for conformance.

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

- binding: programming language defined by this document whose programs are written in Bengali and lowered to one host language

- native keyword: word of this document that stands for one keyword, directive or standard library name of a host language

- lowering: function from native programs to host programs defined in Clause 6

- raising: inverse of lowering applied to a host program with a dictionary of names, giving back the native program exactly

- name transformation: function from native names to host identifiers defined in Clause 7

- C-level form: result of the name transformation; the form a native name takes in host source and in object code

## 4 Conformance

A conforming Bengali program of a binding shall be a text that meets Clause 5 and whose lowering is a conforming program of the host language.

A conforming implementation of a binding shall accept every conforming program of that binding and shall behave as the lowering of the program, processed by a conforming implementation of the host language, behaves.

An implementation that raises host programs into a binding shall produce native programs whose lowering, with the same dictionary of names, is identical to the host program it raised.

## 5 Character set and encoding

A native program shall be encoded in UTF-8 and shall be in Normalization Form C. Native keywords and names are written in the Bengali script, whose direction is left to right. Numeric literals are written with the digits 0 to 9 (U+0030 to U+0039). A native keyword written as several words is one token, its words joined by LOW LINE (U+005F).

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

| Host | Bengali | Source |
|---|---|---|
| auto | auto | host form (no native word yet) |
| break | বিরতি | lexicon |
| case | ক্ষেত্র | lexicon |
| char | অক্ষর | lexicon |
| const | ধ্রুবক | lexicon |
| continue | চালু | lexicon |
| default | পূর্বনির্ধারিত | lexicon |
| do | করো | lexicon |
| double | দ্বিগুণ | lexicon |
| else | অন্যথা | lexicon |
| enum | গণনা | lexicon |
| extern | বাহ্যিক | lexicon |
| float | দশমিক | lexicon |
| for | জন্য | lexicon |
| goto | যাও | lexicon |
| if | যদি | lexicon |
| inline | অন্তঃরেখ | lexicon |
| int | পূর্ণসংখ্যা | lexicon |
| long | long | host form (no native word yet) |
| register | নিবন্ধ | lexicon |
| restrict | restrict | host form (no native word yet) |
| return | ফেরত | lexicon |
| short | short | host form (no native word yet) |
| signed | signed | host form (no native word yet) |
| sizeof | আকার | lexicon |
| static | স্থির | lexicon |
| struct | কাঠামো | lexicon |
| switch | নির্বাচন | lexicon |
| typedef | প্রকারলেখ | lexicon |
| union | সংঘ | lexicon |
| unsigned | unsigned | host form (no native word yet) |
| void | শূন্য | lexicon |
| volatile | অস্থির | lexicon |
| while | যখন | lexicon |
| main | প্রধান | lexicon |

Standard library and runtime names of the C binding:

| Host | Bengali | Source |
|---|---|---|
| NULL | ফাঁকা | lexicon |
| assert | প্রতিজ্ঞা | lexicon |
| free | মুক্ত | lexicon |
| private | ব্যক্তিগত | lexicon |
| protected | সুরক্ষিত | lexicon |
| public | সর্বজনীন | lexicon |
| raise | তোলো | lexicon |
| read | পঠ | lexicon |
| signal | সংকেত | lexicon |
| virtual | আভাসী | lexicon |
| write | লিখ | lexicon |

### A.2 C preprocessor

Host: ISO/IEC 9899, Information technology, Programming languages, C (preprocessing directives). Names: name transformation.

| Host | Bengali | Source |
|---|---|---|
| #define | #define | host form (no native word yet) |
| #include | #অন্তর্ভা঵ | lexicon |
| #if | #যদি | lexicon |
| #ifdef | #ifdef | host form (no native word yet) |
| #ifndef | #ifndef | host form (no native word yet) |
| #else | #অন্যথা | lexicon |
| #elif | #নতুবা_যদি | lexicon |
| #endif | #endif | host form (no native word yet) |
| #undef | #undef | host form (no native word yet) |
| #pragma | #pragma | host form (no native word yet) |
| #error | #error | host form (no native word yet) |
| #line | #line | host form (no native word yet) |

### A.3 C++

Host: ISO/IEC 14882, Programming languages, C++. Names: name transformation.

| Host | Bengali | Source |
|---|---|---|
| auto | auto | host form (no native word yet) |
| break | বিরতি | lexicon |
| case | ক্ষেত্র | lexicon |
| char | অক্ষর | lexicon |
| const | ধ্রুবক | lexicon |
| continue | চালু | lexicon |
| default | পূর্বনির্ধারিত | lexicon |
| do | করো | lexicon |
| double | দ্বিগুণ | lexicon |
| else | অন্যথা | lexicon |
| enum | গণনা | lexicon |
| extern | বাহ্যিক | lexicon |
| float | দশমিক | lexicon |
| for | জন্য | lexicon |
| goto | যাও | lexicon |
| if | যদি | lexicon |
| inline | অন্তঃরেখ | lexicon |
| int | পূর্ণসংখ্যা | lexicon |
| long | long | host form (no native word yet) |
| register | নিবন্ধ | lexicon |
| restrict | restrict | host form (no native word yet) |
| return | ফেরত | lexicon |
| short | short | host form (no native word yet) |
| signed | signed | host form (no native word yet) |
| sizeof | আকার | lexicon |
| static | স্থির | lexicon |
| struct | কাঠামো | lexicon |
| switch | নির্বাচন | lexicon |
| typedef | প্রকারলেখ | lexicon |
| union | সংঘ | lexicon |
| unsigned | unsigned | host form (no native word yet) |
| void | শূন্য | lexicon |
| volatile | অস্থির | lexicon |
| while | যখন | lexicon |
| main | প্রধান | lexicon |
| bool | যৌক্তিক | lexicon |
| catch | ধরো | lexicon |
| class | শ্রেণী | lexicon |
| delete | delete | host form (no native word yet) |
| explicit | explicit | host form (no native word yet) |
| false | মিথ্যা | lexicon |
| friend | friend | host form (no native word yet) |
| mutable | mutable | host form (no native word yet) |
| namespace | নামাকাশ | lexicon |
| new | নতুন | lexicon |
| nullptr | nullptr | host form (no native word yet) |
| operator | operator | host form (no native word yet) |
| private | ব্যক্তিগত | lexicon |
| protected | সুরক্ষিত | lexicon |
| public | সর্বজনীন | lexicon |
| template | template | host form (no native word yet) |
| this | এই | lexicon |
| throw | ছোড়ো | lexicon |
| true | সত্য | lexicon |
| try | চেষ্টা | lexicon |
| typename | typename | host form (no native word yet) |
| using | using | host form (no native word yet) |
| virtual | আভাসী | lexicon |
| cout | cout | host form (no native word yet) |
| cin | cin | host form (no native word yet) |
| endl | endl | host form (no native word yet) |

Standard library and runtime names of the C++ binding:

| Host | Bengali | Source |
|---|---|---|
| NULL | ফাঁকা | lexicon |
| assert | প্রতিজ্ঞা | lexicon |
| free | মুক্ত | lexicon |
| pipe | প্রণাল | lexicon |
| raise | তোলো | lexicon |
| read | পঠ | lexicon |
| signal | সংকেত | lexicon |
| sleep | সুষুপ্তি | lexicon |
| sync | সমলয় | lexicon |
| write | লিখ | lexicon |

### A.4 Java

Host: The Java Language Specification, Oracle, current edition. Names: unchanged.

| Host | Bengali | Source |
|---|---|---|
| abstract | বিমূর্ত | lexicon |
| assert | প্রতিজ্ঞা | lexicon |
| boolean | boolean | host form (no native word yet) |
| break | বিরতি | lexicon |
| byte | byte | host form (no native word yet) |
| case | ক্ষেত্র | lexicon |
| catch | ধরো | lexicon |
| char | অক্ষর | lexicon |
| class | শ্রেণী | lexicon |
| continue | চালু | lexicon |
| default | পূর্বনির্ধারিত | lexicon |
| do | করো | lexicon |
| double | দ্বিগুণ | lexicon |
| else | অন্যথা | lexicon |
| enum | গণনা | lexicon |
| extends | সম্প্রসারিত | lexicon |
| final | final | host form (no native word yet) |
| finally | অবশেষে | lexicon |
| float | দশমিক | lexicon |
| for | জন্য | lexicon |
| if | যদি | lexicon |
| implements | বাস্তবায়িত | lexicon |
| import | আমদানি | lexicon |
| instanceof | instanceof | host form (no native word yet) |
| int | পূর্ণসংখ্যা | lexicon |
| interface | সংযোগস্থল | lexicon |
| long | long | host form (no native word yet) |
| native | native | host form (no native word yet) |
| new | নতুন | lexicon |
| package | মোড়ক | lexicon |
| private | ব্যক্তিগত | lexicon |
| protected | সুরক্ষিত | lexicon |
| public | সর্বজনীন | lexicon |
| return | ফেরত | lexicon |
| short | short | host form (no native word yet) |
| static | স্থির | lexicon |
| super | পরম | lexicon |
| switch | নির্বাচন | lexicon |
| synchronized | synchronized | host form (no native word yet) |
| this | এই | lexicon |
| throw | ছোড়ো | lexicon |
| throws | throws | host form (no native word yet) |
| try | চেষ্টা | lexicon |
| void | শূন্য | lexicon |
| volatile | অস্থির | lexicon |
| while | যখন | lexicon |
| true | সত্য | lexicon |
| false | মিথ্যা | lexicon |
| null | ফাঁকা | lexicon |
| String | বাক্য | lexicon |
| System | System | host form (no native word yet) |

Standard library and runtime names of the Java binding:

| Host | Bengali | Source |
|---|---|---|
| Object | বস্তু | lexicon |
| Thread | সুতা | lexicon |
| const | ধ্রুবক | lexicon |
| extern | বাহ্যিক | lexicon |
| free | মুক্ত | lexicon |
| goto | যাও | lexicon |
| inline | অন্তঃরেখ | lexicon |
| main | প্রধান | lexicon |
| raise | তোলো | lexicon |
| read | পঠ | lexicon |
| register | নিবন্ধ | lexicon |
| signal | সংকেত | lexicon |
| sizeof | আকার | lexicon |
| sleep | সুষুপ্তি | lexicon |
| struct | কাঠামো | lexicon |
| typedef | প্রকারলেখ | lexicon |
| union | সংঘ | lexicon |
| virtual | আভাসী | lexicon |
| write | লিখ | lexicon |

### A.5 Python

Host: The Python Language Reference, Python Software Foundation, current version. Names: unchanged.

| Host | Bengali | Source |
|---|---|---|
| False | মিথ্যা | lexicon |
| None | None | host form (no native word yet) |
| True | সত্য | lexicon |
| and | এবং | lexicon |
| as | ই঵ | lexicon |
| assert | প্রতিজ্ঞা | lexicon |
| break | বিরতি | lexicon |
| class | শ্রেণী | lexicon |
| continue | চালু | lexicon |
| def | def | host form (no native word yet) |
| del | del | host form (no native word yet) |
| elif | নতুবা_যদি | lexicon |
| else | অন্যথা | lexicon |
| except | ব্যতিক্রম | lexicon |
| finally | অবশেষে | lexicon |
| for | জন্য | lexicon |
| from | তঃ | lexicon |
| global | global | host form (no native word yet) |
| if | যদি | lexicon |
| import | আমদানি | lexicon |
| in | মধ্যে | lexicon |
| is | is | host form (no native word yet) |
| lambda | অনামা | lexicon |
| nonlocal | nonlocal | host form (no native word yet) |
| not | নয় | lexicon |
| or | অথবা | lexicon |
| pass | pass | host form (no native word yet) |
| raise | তোলো | lexicon |
| return | ফেরত | lexicon |
| try | চেষ্টা | lexicon |
| while | যখন | lexicon |
| with | with | host form (no native word yet) |
| yield | দাও | lexicon |
| print | print | host form (no native word yet) |
| range | range | host form (no native word yet) |
| len | len | host form (no native word yet) |

Standard library and runtime names of the Python binding:

| Host | Bengali | Source |
|---|---|---|
| Object | বস্তু | lexicon |
| String | বাক্য | lexicon |
| Thread | সুতা | lexicon |
| abstract | বিমূর্ত | lexicon |
| case | ক্ষেত্র | lexicon |
| catch | ধরো | lexicon |
| char | অক্ষর | lexicon |
| const | ধ্রুবক | lexicon |
| default | পূর্বনির্ধারিত | lexicon |
| do | করো | lexicon |
| double | দ্বিগুণ | lexicon |
| extends | সম্প্রসারিত | lexicon |
| float | দশমিক | lexicon |
| goto | যাও | lexicon |
| implements | বাস্তবায়িত | lexicon |
| int | পূর্ণসংখ্যা | lexicon |
| interface | সংযোগস্থল | lexicon |
| main | প্রধান | lexicon |
| new | নতুন | lexicon |
| package | মোড়ক | lexicon |
| private | ব্যক্তিগত | lexicon |
| protected | সুরক্ষিত | lexicon |
| public | সর্বজনীন | lexicon |
| read | পঠ | lexicon |
| sleep | সুষুপ্তি | lexicon |
| static | স্থির | lexicon |
| super | পরম | lexicon |
| switch | নির্বাচন | lexicon |
| this | এই | lexicon |
| throw | ছোড়ো | lexicon |
| void | শূন্য | lexicon |
| volatile | অস্থির | lexicon |
| write | লিখ | lexicon |

### A.6 BASIC

Host: ISO/IEC 10279, Information technology, Programming languages, Full BASIC. Names: name transformation.

| Host | Bengali | Source |
|---|---|---|
| dim | dim | host form (no native word yet) |
| end | শেষ | lexicon |
| for | জন্য | lexicon |
| gosub | gosub | host form (no native word yet) |
| goto | যাও | lexicon |
| if | যদি | lexicon |
| input | input | host form (no native word yet) |
| let | ধরি | lexicon |
| next | next | host form (no native word yet) |
| print | print | host form (no native word yet) |
| rem | rem | host form (no native word yet) |
| return | ফেরত | lexicon |
| step | step | host form (no native word yet) |
| then | then | host form (no native word yet) |
| to | to | host form (no native word yet) |
| wend | wend | host form (no native word yet) |
| while | যখন | lexicon |
| and | এবং | lexicon |
| or | অথবা | lexicon |
| not | নয় | lexicon |
| mod | mod | host form (no native word yet) |

Standard library and runtime names of the BASIC binding:

| Host | Bengali | Source |
|---|---|---|
| AS | ই঵ | lexicon |
| CALL | ডাকো | lexicon |
| CONST | ধ্রুবক | lexicon |
| DO | করো | lexicon |
| ELSE | অন্যথা | lexicon |
| INT | পূর্ণসংখ্যা | lexicon |
| SHARED | সহভাজিত | lexicon |
| STATIC | স্থির | lexicon |
| STRING | বাক্য | lexicon |
| TIMER | কালযন্ত্র | lexicon |

### A.7 LOGO

Host: No international standard; the host is the Berkeley Logo dialect (bibliography). Names: name transformation.

| Host | Bengali | Source |
|---|---|---|
| forward | অগ্রপ্রসার | lexicon |
| back | back | host form (no native word yet) |
| left | left | host form (no native word yet) |
| right | right | host form (no native word yet) |
| penup | penup | host form (no native word yet) |
| pendown | pendown | host form (no native word yet) |
| repeat | repeat | host form (no native word yet) |
| to | to | host form (no native word yet) |
| end | শেষ | lexicon |
| make | make | host form (no native word yet) |
| if | যদি | lexicon |
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
| Python | 25 of 36 | 33 |
| BASIC | 10 of 21 | 10 |
| LOGO | 3 of 14 | 0 |

The lowering of Bengali programs to C is verified by the reference implementation: runs, same output. Source Chintamani means a word of the original Hindawi transducers; lexicon, a word of the language's lexicon; proposed, a word proposed by the project and not yet reviewed by the language community.

## Annex C (normative) Script filter

The script filter maps each letter and sign of the script to the Devanagari letter or sign of the same Unicode name, as generated by lang/hindawi/tools/script_filters.py.

## Annex D (informative) Rights and provenance

This document is an original work. It defines new programming languages by reference to the host language standards listed in Clause 2 and reproduces no text from them. Permission to adopt, translate or publish it as a standard is given by the copyright holder to a standards body on request.

Single words and the keywords of the host languages are not reproduced from any copyrighted text; the native words of Annex A were chosen by the Hindawi project, taken from the language's lexicon in the Hindawi repository, or, for Hindi, taken from the Chintamani transducers of the original Hindawi, whose author holds their copyright.

## Bibliography

- Hindawi 2026.10, hindawiai/hindawi2026.10, the reference implementation
- Chintamani, hindawiai/chintamani, the Hindawi transducers and the Romenagri tools
- Berkeley Logo reference manual, Brian Harvey

