# HLS kashmiri 2026.10

**Kashmiri bindings for programming languages: lexical mapping and lowering to the host standards**

Edition 2026.10, working draft, 2026-10-18. © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

## Foreword

This document was prepared by AyeAI, Hindawi project (Project ILM). It is generated from the Kashmiri cell of Hindawi 2026.10 by lang/hindawi/tools/standards.py, so that the published standard and the reference implementation cannot drift apart. Its stage is a working draft: the words marked proposed in Annex A await review by the Kashmiri language community, through the review pages of the Hindawi project.

## Introduction

This document lets programs be written in Kashmiri, in the Arabic script, in each of the programming languages listed in Clause 1. Each binding is a programming language in its own right, Kashmiri C for example, whose programs are lowered by the function defined in Clause 6 to programs of the host language, and are then processed by any conforming implementation of the host standard. The host standards are incorporated by reference and are not restated. Names keep a defined form down to object code (Clause 7), so programs written in Kashmiri remain debuggable at the level of firmware, kernels and libraries.

## 1 Scope

This document specifies, for the Kashmiri language written in the Arabic script, bindings to the following host programming languages: C, C preprocessor, C++, Java, Python, BASIC, LOGO. For each binding it specifies the native keywords and directives, the lowering of native programs to host programs, the treatment of names, and the requirements for conformance.

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

- binding: programming language defined by this document whose programs are written in Kashmiri and lowered to one host language

- native keyword: word of this document that stands for one keyword, directive or standard library name of a host language

- lowering: function from native programs to host programs defined in Clause 6

- raising: inverse of lowering applied to a host program with a dictionary of names, giving back the native program exactly

- name transformation: function from native names to host identifiers defined in Clause 7

- C-level form: result of the name transformation; the form a native name takes in host source and in object code

## 4 Conformance

A conforming Kashmiri program of a binding shall be a text that meets Clause 5 and whose lowering is a conforming program of the host language.

A conforming implementation of a binding shall accept every conforming program of that binding and shall behave as the lowering of the program, processed by a conforming implementation of the host language, behaves.

An implementation that raises host programs into a binding shall produce native programs whose lowering, with the same dictionary of names, is identical to the host program it raised.

## 5 Character set and encoding

A native program shall be encoded in UTF-8 and shall be in Normalization Form C. Native keywords and names are written in the Arabic script, whose direction is right to left. Numeric literals are written with the digits 0 to 9 (U+0030 to U+0039). A native keyword written as several words is one token, its words joined by LOW LINE (U+005F).

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

| Host | Kashmiri | Source |
|---|---|---|
| auto | auto | host form (no native word yet) |
| break | اكسر | lexicon |
| case | حالة | lexicon |
| char | حرف | lexicon |
| const | ثابت | lexicon |
| continue | استمر | lexicon |
| default | افتراضي | lexicon |
| do | افعل | lexicon |
| double | مزدوج | lexicon |
| else | وإلا | lexicon |
| enum | تعداد | lexicon |
| extern | خارجي | lexicon |
| float | عائم | lexicon |
| for | لكل | lexicon |
| goto | اذهب | lexicon |
| if | إذا | lexicon |
| inline | مضمن | lexicon |
| int | صحيح | lexicon |
| long | long | host form (no native word yet) |
| register | سجل | lexicon |
| restrict | restrict | host form (no native word yet) |
| return | أرجع | lexicon |
| short | short | host form (no native word yet) |
| signed | signed | host form (no native word yet) |
| sizeof | حجم | lexicon |
| static | ساكن | lexicon |
| struct | بنية | lexicon |
| switch | بدل | lexicon |
| typedef | تعريفنوع | lexicon |
| union | اتحاد | lexicon |
| unsigned | unsigned | host form (no native word yet) |
| void | فراغ | lexicon |
| volatile | متطاير | lexicon |
| while | طالما | lexicon |
| main | main | host form (no native word yet) |

Standard library and runtime names of the C binding:

| Host | Kashmiri | Source |
|---|---|---|
| NULL | عدم | lexicon |
| assert | أكد | lexicon |
| free | حرر | lexicon |
| private | خاص | lexicon |
| protected | محمي | lexicon |
| public | عام | lexicon |
| raise | ارفع | lexicon |
| read | اقرأ | lexicon |
| signal | إشارة | lexicon |
| write | اكتب | lexicon |

### A.2 C preprocessor

Host: ISO/IEC 9899, Information technology, Programming languages, C (preprocessing directives). Names: name transformation.

| Host | Kashmiri | Source |
|---|---|---|
| #define | #define | host form (no native word yet) |
| #include | #ضمن | lexicon |
| #if | #إذا | lexicon |
| #ifdef | #ifdef | host form (no native word yet) |
| #ifndef | #ifndef | host form (no native word yet) |
| #else | #وإلا | lexicon |
| #elif | #وإلاإذا | lexicon |
| #endif | #endif | host form (no native word yet) |
| #undef | #undef | host form (no native word yet) |
| #pragma | #pragma | host form (no native word yet) |
| #error | #error | host form (no native word yet) |
| #line | #line | host form (no native word yet) |

### A.3 C++

Host: ISO/IEC 14882, Programming languages, C++. Names: name transformation.

| Host | Kashmiri | Source |
|---|---|---|
| auto | auto | host form (no native word yet) |
| break | اكسر | lexicon |
| case | حالة | lexicon |
| char | حرف | lexicon |
| const | ثابت | lexicon |
| continue | استمر | lexicon |
| default | افتراضي | lexicon |
| do | افعل | lexicon |
| double | مزدوج | lexicon |
| else | وإلا | lexicon |
| enum | تعداد | lexicon |
| extern | خارجي | lexicon |
| float | عائم | lexicon |
| for | لكل | lexicon |
| goto | اذهب | lexicon |
| if | إذا | lexicon |
| inline | مضمن | lexicon |
| int | صحيح | lexicon |
| long | long | host form (no native word yet) |
| register | سجل | lexicon |
| restrict | restrict | host form (no native word yet) |
| return | أرجع | lexicon |
| short | short | host form (no native word yet) |
| signed | signed | host form (no native word yet) |
| sizeof | حجم | lexicon |
| static | ساكن | lexicon |
| struct | بنية | lexicon |
| switch | بدل | lexicon |
| typedef | تعريفنوع | lexicon |
| union | اتحاد | lexicon |
| unsigned | unsigned | host form (no native word yet) |
| void | فراغ | lexicon |
| volatile | متطاير | lexicon |
| while | طالما | lexicon |
| main | main | host form (no native word yet) |
| bool | منطقي | lexicon |
| catch | امسك | lexicon |
| class | صنف | lexicon |
| delete | delete | host form (no native word yet) |
| explicit | explicit | host form (no native word yet) |
| false | خطأ | lexicon |
| friend | friend | host form (no native word yet) |
| mutable | mutable | host form (no native word yet) |
| namespace | نطاق | lexicon |
| new | جديد | lexicon |
| nullptr | nullptr | host form (no native word yet) |
| operator | operator | host form (no native word yet) |
| private | خاص | lexicon |
| protected | محمي | lexicon |
| public | عام | lexicon |
| template | template | host form (no native word yet) |
| this | هذا | lexicon |
| throw | ارم | lexicon |
| true | true | host form (no native word yet) |
| try | حاول | lexicon |
| typename | typename | host form (no native word yet) |
| using | using | host form (no native word yet) |
| virtual | virtual | host form (no native word yet) |
| cout | cout | host form (no native word yet) |
| cin | cin | host form (no native word yet) |
| endl | endl | host form (no native word yet) |

Standard library and runtime names of the C++ binding:

| Host | Kashmiri | Source |
|---|---|---|
| NULL | عدم | lexicon |
| assert | أكد | lexicon |
| free | حرر | lexicon |
| pipe | أنبوب | lexicon |
| raise | ارفع | lexicon |
| read | اقرأ | lexicon |
| signal | إشارة | lexicon |
| sleep | نوم | lexicon |
| sync | متزامن | lexicon |
| write | اكتب | lexicon |

### A.4 Java

Host: The Java Language Specification, Oracle, current edition. Names: unchanged.

| Host | Kashmiri | Source |
|---|---|---|
| abstract | مجرد | lexicon |
| assert | أكد | lexicon |
| boolean | boolean | host form (no native word yet) |
| break | اكسر | lexicon |
| byte | byte | host form (no native word yet) |
| case | حالة | lexicon |
| catch | امسك | lexicon |
| char | حرف | lexicon |
| class | صنف | lexicon |
| continue | استمر | lexicon |
| default | افتراضي | lexicon |
| do | افعل | lexicon |
| double | مزدوج | lexicon |
| else | وإلا | lexicon |
| enum | تعداد | lexicon |
| extends | يمتد | lexicon |
| final | final | host form (no native word yet) |
| finally | أخيرا | lexicon |
| float | عائم | lexicon |
| for | لكل | lexicon |
| if | إذا | lexicon |
| implements | ينفذ | lexicon |
| import | استورد | lexicon |
| instanceof | instanceof | host form (no native word yet) |
| int | صحيح | lexicon |
| interface | واجهة | lexicon |
| long | long | host form (no native word yet) |
| native | native | host form (no native word yet) |
| new | جديد | lexicon |
| package | حزمة | lexicon |
| private | خاص | lexicon |
| protected | محمي | lexicon |
| public | عام | lexicon |
| return | أرجع | lexicon |
| short | short | host form (no native word yet) |
| static | ساكن | lexicon |
| super | أعلى | lexicon |
| switch | بدل | lexicon |
| synchronized | synchronized | host form (no native word yet) |
| this | هذا | lexicon |
| throw | ارم | lexicon |
| throws | throws | host form (no native word yet) |
| try | حاول | lexicon |
| void | فراغ | lexicon |
| volatile | متطاير | lexicon |
| while | طالما | lexicon |
| true | true | host form (no native word yet) |
| false | خطأ | lexicon |
| null | عدم | lexicon |
| String | نص | lexicon |
| System | System | host form (no native word yet) |

Standard library and runtime names of the Java binding:

| Host | Kashmiri | Source |
|---|---|---|
| Object | كائن | lexicon |
| Thread | خيط | lexicon |
| const | ثابت | lexicon |
| extern | خارجي | lexicon |
| free | حرر | lexicon |
| goto | اذهب | lexicon |
| inline | مضمن | lexicon |
| raise | ارفع | lexicon |
| read | اقرأ | lexicon |
| register | سجل | lexicon |
| signal | إشارة | lexicon |
| sizeof | حجم | lexicon |
| sleep | نوم | lexicon |
| struct | بنية | lexicon |
| typedef | تعريفنوع | lexicon |
| union | اتحاد | lexicon |
| write | اكتب | lexicon |

### A.5 Python

Host: The Python Language Reference, Python Software Foundation, current version. Names: unchanged.

| Host | Kashmiri | Source |
|---|---|---|
| False | خطأ | lexicon |
| None | None | host form (no native word yet) |
| True | صحيح | lexicon |
| and | و | lexicon |
| as | كـ | lexicon |
| assert | أكد | lexicon |
| break | اكسر | lexicon |
| class | صنف | lexicon |
| continue | استمر | lexicon |
| def | def | host form (no native word yet) |
| del | del | host form (no native word yet) |
| elif | وإلاإذا | lexicon |
| else | وإلا | lexicon |
| except | استثناء | lexicon |
| finally | أخيرا | lexicon |
| for | لكل | lexicon |
| from | من | lexicon |
| global | عام | lexicon |
| if | إذا | lexicon |
| import | استورد | lexicon |
| in | في | lexicon |
| is | is | host form (no native word yet) |
| lambda | مجهول | lexicon |
| nonlocal | nonlocal | host form (no native word yet) |
| not | ليس | lexicon |
| or | أو | lexicon |
| pass | pass | host form (no native word yet) |
| raise | ارفع | lexicon |
| return | أرجع | lexicon |
| try | حاول | lexicon |
| while | طالما | lexicon |
| with | with | host form (no native word yet) |
| yield | أنتج | lexicon |
| print | print | host form (no native word yet) |
| range | range | host form (no native word yet) |
| len | len | host form (no native word yet) |

Standard library and runtime names of the Python binding:

| Host | Kashmiri | Source |
|---|---|---|
| Object | كائن | lexicon |
| String | نص | lexicon |
| Thread | خيط | lexicon |
| abstract | مجرد | lexicon |
| case | حالة | lexicon |
| catch | امسك | lexicon |
| char | حرف | lexicon |
| const | ثابت | lexicon |
| default | افتراضي | lexicon |
| do | افعل | lexicon |
| double | مزدوج | lexicon |
| extends | يمتد | lexicon |
| float | عائم | lexicon |
| goto | اذهب | lexicon |
| implements | ينفذ | lexicon |
| interface | واجهة | lexicon |
| new | جديد | lexicon |
| package | حزمة | lexicon |
| private | خاص | lexicon |
| protected | محمي | lexicon |
| read | اقرأ | lexicon |
| sleep | نوم | lexicon |
| static | ساكن | lexicon |
| super | أعلى | lexicon |
| switch | بدل | lexicon |
| this | هذا | lexicon |
| throw | ارم | lexicon |
| void | فراغ | lexicon |
| volatile | متطاير | lexicon |
| write | اكتب | lexicon |

### A.6 BASIC

Host: ISO/IEC 10279, Information technology, Programming languages, Full BASIC. Names: name transformation.

| Host | Kashmiri | Source |
|---|---|---|
| dim | dim | host form (no native word yet) |
| end | انته | lexicon |
| for | لكل | lexicon |
| gosub | gosub | host form (no native word yet) |
| goto | اذهب | lexicon |
| if | إذا | lexicon |
| input | input | host form (no native word yet) |
| let | ليكن | lexicon |
| next | next | host form (no native word yet) |
| print | print | host form (no native word yet) |
| rem | rem | host form (no native word yet) |
| return | أرجع | lexicon |
| step | step | host form (no native word yet) |
| then | then | host form (no native word yet) |
| to | to | host form (no native word yet) |
| wend | wend | host form (no native word yet) |
| while | طالما | lexicon |
| and | و | lexicon |
| or | أو | lexicon |
| not | ليس | lexicon |
| mod | mod | host form (no native word yet) |

Standard library and runtime names of the BASIC binding:

| Host | Kashmiri | Source |
|---|---|---|
| AS | كـ | lexicon |
| CALL | نادي | lexicon |
| CONST | ثابت | lexicon |
| DO | افعل | lexicon |
| ELSE | وإلا | lexicon |
| INT | صحيح | lexicon |
| SHARED | مشترك | lexicon |
| STATIC | ساكن | lexicon |
| STRING | نص | lexicon |
| TIMER | مؤقت | lexicon |

### A.7 LOGO

Host: No international standard; the host is the Berkeley Logo dialect (bibliography). Names: name transformation.

| Host | Kashmiri | Source |
|---|---|---|
| forward | أمامي | lexicon |
| back | back | host form (no native word yet) |
| left | left | host form (no native word yet) |
| right | right | host form (no native word yet) |
| penup | penup | host form (no native word yet) |
| pendown | pendown | host form (no native word yet) |
| repeat | repeat | host form (no native word yet) |
| to | to | host form (no native word yet) |
| end | انته | lexicon |
| make | make | host form (no native word yet) |
| if | إذا | lexicon |
| ifelse | ifelse | host form (no native word yet) |
| home | home | host form (no native word yet) |
| clearscreen | clearscreen | host form (no native word yet) |

## Annex B (informative) Coverage and review

| Binding | Host keywords with a native word | Library names |
|---|---|---|
| C | 28 of 35 | 10 |
| C preprocessor | 4 of 12 | 0 |
| C++ | 40 of 61 | 10 |
| Java | 40 of 51 | 17 |
| Python | 26 of 36 | 30 |
| BASIC | 10 of 21 | 10 |
| LOGO | 3 of 14 | 0 |

The lowering of Kashmiri programs to C is verified by the reference implementation: runs, same output. Source Chintamani means a word of the original Hindawi transducers; lexicon, a word of the language's lexicon; proposed, a word proposed by the project and not yet reviewed by the language community.

## Annex C (normative) Script filter

The script filter is Chintamani's own (fltr_ur_hi).

Before the filter, these letters are written as the letters that follow them:

| Letter | Written as |
|---|---|
| ٻ | ب |
| ټ | ٹ |
| ٽ | ٹ |
| ٿ | تھ |
| ڀ | بھ |
| ځ | ز |
| ڄ | ج |
| څ | س |
| ڇ | چھ |
| ډ | ڈ |
| ڊ | ڈ |
| ڌ | دھ |
| ڍ | ڈھ |
| ڏ | د |
| ړ | ڑ |
| ږ | ژ |
| ڙ | ڑ |
| ښ | ش |
| ڦ | پھ |
| ڪ | ک |
| ګ | گ |
| ڱ | نگ |
| ڳ | گ |
| ڻ | ن |
| ڼ | ن |
| ۀ | ہ |
| ۍ | ی |
| ې | ی |

## Annex D (informative) Rights and provenance

This document is an original work. It defines new programming languages by reference to the host language standards listed in Clause 2 and reproduces no text from them. Permission to adopt, translate or publish it as a standard is given by the copyright holder to a standards body on request.

Single words and the keywords of the host languages are not reproduced from any copyrighted text; the native words of Annex A were chosen by the Hindawi project, taken from the language's lexicon in the Hindawi repository, or, for Hindi, taken from the Chintamani transducers of the original Hindawi, whose author holds their copyright.

## Bibliography

- Hindawi 2026.10, hindawiai/hindawi2026.10, the reference implementation
- Chintamani, hindawiai/chintamani, the Hindawi transducers and the Romenagri tools
- Berkeley Logo reference manual, Brian Harvey

