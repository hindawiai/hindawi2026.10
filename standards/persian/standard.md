# HLS fa 2026.10

**Persian bindings for programming languages: lexical mapping and lowering to the host standards**

Edition 2026.10, working draft, 2026-10-18. © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

## Foreword

This document was prepared by AyeAI, Hindawi project (Project ILM). It is generated from the Persian cell of Hindawi 2026.10 by lang/hindawi/tools/standards.py, so that the published standard and the reference implementation cannot drift apart. Its stage is a working draft: the words marked proposed in Annex A await review by the Persian language community, through the review pages of the Hindawi project.

## Introduction

This document lets programs be written in Persian, in the Arabic script, in each of the programming languages listed in Clause 1. Each binding is a programming language in its own right, Persian C for example, whose programs are lowered by the function defined in Clause 6 to programs of the host language, and are then processed by any conforming implementation of the host standard. The host standards are incorporated by reference and are not restated. Names keep a defined form down to object code (Clause 7), so programs written in Persian remain debuggable at the level of firmware, kernels and libraries.

## 1 Scope

This document specifies, for the Persian language written in the Arabic script, bindings to the following host programming languages: C, C preprocessor, C++, Java, Python, BASIC, LOGO. For each binding it specifies the native keywords and directives, the lowering of native programs to host programs, the treatment of names, and the requirements for conformance.

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

- binding: programming language defined by this document whose programs are written in Persian and lowered to one host language

- native keyword: word of this document that stands for one keyword, directive or standard library name of a host language

- lowering: function from native programs to host programs defined in Clause 6

- raising: inverse of lowering applied to a host program with a dictionary of names, giving back the native program exactly

- name transformation: function from native names to host identifiers defined in Clause 7

- C-level form: result of the name transformation; the form a native name takes in host source and in object code

## 4 Conformance

A conforming Persian program of a binding shall be a text that meets Clause 5 and whose lowering is a conforming program of the host language.

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

| Host | Persian | Source |
|---|---|---|
| auto | auto | host form (no native word yet) |
| break | بشکن | lexicon |
| case | حالت | lexicon |
| char | نویسه | lexicon |
| const | ثابت | lexicon |
| continue | ادامه | lexicon |
| default | پیشفرض | lexicon |
| do | انجامبده | lexicon |
| double | دوگانه | lexicon |
| else | وگرنه | lexicon |
| enum | شمارش | lexicon |
| extern | بیرونی | lexicon |
| float | اعشاری | lexicon |
| for | برای | lexicon |
| goto | برو | lexicon |
| if | اگر | lexicon |
| inline | درونخطی | lexicon |
| int | صحیح | lexicon |
| long | long | host form (no native word yet) |
| register | ثبات | lexicon |
| restrict | restrict | host form (no native word yet) |
| return | بازگشت | lexicon |
| short | short | host form (no native word yet) |
| signed | signed | host form (no native word yet) |
| sizeof | اندازه | lexicon |
| static | ایستا | lexicon |
| struct | ساختار | lexicon |
| switch | انتخاب | lexicon |
| typedef | تعریفنوع | lexicon |
| union | اجتماع | lexicon |
| unsigned | unsigned | host form (no native word yet) |
| void | تهی | lexicon |
| volatile | فرار | lexicon |
| while | وقتی | lexicon |
| main | اصلی | lexicon |

Standard library and runtime names of the C binding:

| Host | Persian | Source |
|---|---|---|
| NULL | پوچ | lexicon |
| assert | أكد | lexicon |
| free | آزاد | lexicon |
| private | خصوصی | lexicon |
| protected | محافظتشده | lexicon |
| public | عمومی | lexicon |
| raise | بالاببر | lexicon |
| read | اقرأ | lexicon |
| signal | سیگنال | lexicon |
| virtual | مجازی | lexicon |
| write | اكتب | lexicon |

### A.2 C preprocessor

Host: ISO/IEC 9899, Information technology, Programming languages, C (preprocessing directives). Names: name transformation.

| Host | Persian | Source |
|---|---|---|
| #define | #define | host form (no native word yet) |
| #include | #شامل | lexicon |
| #if | #اگر | lexicon |
| #ifdef | #ifdef | host form (no native word yet) |
| #ifndef | #ifndef | host form (no native word yet) |
| #else | #وگرنه | lexicon |
| #elif | #وگرنهاگر | lexicon |
| #endif | #endif | host form (no native word yet) |
| #undef | #undef | host form (no native word yet) |
| #pragma | #pragma | host form (no native word yet) |
| #error | #error | host form (no native word yet) |
| #line | #line | host form (no native word yet) |

### A.3 C++

Host: ISO/IEC 14882, Programming languages, C++. Names: name transformation.

| Host | Persian | Source |
|---|---|---|
| auto | auto | host form (no native word yet) |
| break | بشکن | lexicon |
| case | حالت | lexicon |
| char | نویسه | lexicon |
| const | ثابت | lexicon |
| continue | ادامه | lexicon |
| default | پیشفرض | lexicon |
| do | انجامبده | lexicon |
| double | دوگانه | lexicon |
| else | وگرنه | lexicon |
| enum | شمارش | lexicon |
| extern | بیرونی | lexicon |
| float | اعشاری | lexicon |
| for | برای | lexicon |
| goto | برو | lexicon |
| if | اگر | lexicon |
| inline | درونخطی | lexicon |
| int | صحیح | lexicon |
| long | long | host form (no native word yet) |
| register | ثبات | lexicon |
| restrict | restrict | host form (no native word yet) |
| return | بازگشت | lexicon |
| short | short | host form (no native word yet) |
| signed | signed | host form (no native word yet) |
| sizeof | اندازه | lexicon |
| static | ایستا | lexicon |
| struct | ساختار | lexicon |
| switch | انتخاب | lexicon |
| typedef | تعریفنوع | lexicon |
| union | اجتماع | lexicon |
| unsigned | unsigned | host form (no native word yet) |
| void | تهی | lexicon |
| volatile | فرار | lexicon |
| while | وقتی | lexicon |
| main | اصلی | lexicon |
| bool | منطقی | lexicon |
| catch | بگیر | lexicon |
| class | رده | lexicon |
| delete | delete | host form (no native word yet) |
| explicit | explicit | host form (no native word yet) |
| false | نادرست | lexicon |
| friend | friend | host form (no native word yet) |
| mutable | mutable | host form (no native word yet) |
| namespace | فضاینام | lexicon |
| new | جدید | lexicon |
| nullptr | nullptr | host form (no native word yet) |
| operator | operator | host form (no native word yet) |
| private | خصوصی | lexicon |
| protected | محافظتشده | lexicon |
| public | عمومی | lexicon |
| template | template | host form (no native word yet) |
| this | این | lexicon |
| throw | پرتابکن | lexicon |
| true | درست | lexicon |
| try | تلاش | lexicon |
| typename | typename | host form (no native word yet) |
| using | using | host form (no native word yet) |
| virtual | مجازی | lexicon |
| cout | cout | host form (no native word yet) |
| cin | cin | host form (no native word yet) |
| endl | endl | host form (no native word yet) |

Standard library and runtime names of the C++ binding:

| Host | Persian | Source |
|---|---|---|
| NULL | پوچ | lexicon |
| assert | أكد | lexicon |
| free | آزاد | lexicon |
| pipe | أنبوب | lexicon |
| raise | بالاببر | lexicon |
| read | اقرأ | lexicon |
| signal | سیگنال | lexicon |
| sleep | نوم | lexicon |
| sync | همگام | lexicon |
| write | اكتب | lexicon |

### A.4 Java

Host: The Java Language Specification, Oracle, current edition. Names: unchanged.

| Host | Persian | Source |
|---|---|---|
| abstract | انتزاعی | lexicon |
| assert | أكد | lexicon |
| boolean | boolean | host form (no native word yet) |
| break | بشکن | lexicon |
| byte | byte | host form (no native word yet) |
| case | حالت | lexicon |
| catch | بگیر | lexicon |
| char | نویسه | lexicon |
| class | رده | lexicon |
| continue | ادامه | lexicon |
| default | پیشفرض | lexicon |
| do | انجامبده | lexicon |
| double | دوگانه | lexicon |
| else | وگرنه | lexicon |
| enum | شمارش | lexicon |
| extends | گسترش | lexicon |
| final | final | host form (no native word yet) |
| finally | سرانجام | lexicon |
| float | اعشاری | lexicon |
| for | برای | lexicon |
| if | اگر | lexicon |
| implements | پیادهسازی | lexicon |
| import | واردکن | lexicon |
| instanceof | instanceof | host form (no native word yet) |
| int | صحیح | lexicon |
| interface | واسط | lexicon |
| long | long | host form (no native word yet) |
| native | native | host form (no native word yet) |
| new | جدید | lexicon |
| package | بسته | lexicon |
| private | خصوصی | lexicon |
| protected | محافظتشده | lexicon |
| public | عمومی | lexicon |
| return | بازگشت | lexicon |
| short | short | host form (no native word yet) |
| static | ایستا | lexicon |
| super | ابر | lexicon |
| switch | انتخاب | lexicon |
| synchronized | synchronized | host form (no native word yet) |
| this | این | lexicon |
| throw | پرتابکن | lexicon |
| throws | throws | host form (no native word yet) |
| try | تلاش | lexicon |
| void | تهی | lexicon |
| volatile | فرار | lexicon |
| while | وقتی | lexicon |
| true | درست | lexicon |
| false | نادرست | lexicon |
| null | پوچ | lexicon |
| String | رشته | lexicon |
| System | System | host form (no native word yet) |

Standard library and runtime names of the Java binding:

| Host | Persian | Source |
|---|---|---|
| Object | شیء | lexicon |
| Thread | نخ | lexicon |
| const | ثابت | lexicon |
| extern | بیرونی | lexicon |
| free | آزاد | lexicon |
| goto | برو | lexicon |
| inline | درونخطی | lexicon |
| main | اصلی | lexicon |
| raise | بالاببر | lexicon |
| read | اقرأ | lexicon |
| register | ثبات | lexicon |
| signal | سیگنال | lexicon |
| sizeof | اندازه | lexicon |
| sleep | نوم | lexicon |
| struct | ساختار | lexicon |
| typedef | تعریفنوع | lexicon |
| union | اجتماع | lexicon |
| virtual | مجازی | lexicon |
| write | اكتب | lexicon |

### A.5 Python

Host: The Python Language Reference, Python Software Foundation, current version. Names: unchanged.

| Host | Persian | Source |
|---|---|---|
| False | نادرست | lexicon |
| None | None | host form (no native word yet) |
| True | درست | lexicon |
| and | و | lexicon |
| as | بهعنوان | lexicon |
| assert | أكد | lexicon |
| break | بشکن | lexicon |
| class | رده | lexicon |
| continue | ادامه | lexicon |
| def | def | host form (no native word yet) |
| del | del | host form (no native word yet) |
| elif | وگرنهاگر | lexicon |
| else | وگرنه | lexicon |
| except | استثنا | lexicon |
| finally | سرانجام | lexicon |
| for | برای | lexicon |
| from | از | lexicon |
| global | عام | lexicon |
| if | اگر | lexicon |
| import | واردکن | lexicon |
| in | در | lexicon |
| is | is | host form (no native word yet) |
| lambda | بینام | lexicon |
| nonlocal | nonlocal | host form (no native word yet) |
| not | نه | lexicon |
| or | یا | lexicon |
| pass | pass | host form (no native word yet) |
| raise | بالاببر | lexicon |
| return | بازگشت | lexicon |
| try | تلاش | lexicon |
| while | وقتی | lexicon |
| with | with | host form (no native word yet) |
| yield | بده | lexicon |
| print | print | host form (no native word yet) |
| range | range | host form (no native word yet) |
| len | len | host form (no native word yet) |

Standard library and runtime names of the Python binding:

| Host | Persian | Source |
|---|---|---|
| Object | شیء | lexicon |
| String | رشته | lexicon |
| Thread | نخ | lexicon |
| abstract | انتزاعی | lexicon |
| case | حالت | lexicon |
| catch | بگیر | lexicon |
| char | نویسه | lexicon |
| const | ثابت | lexicon |
| default | پیشفرض | lexicon |
| do | انجامبده | lexicon |
| double | دوگانه | lexicon |
| extends | گسترش | lexicon |
| float | اعشاری | lexicon |
| goto | برو | lexicon |
| implements | پیادهسازی | lexicon |
| int | صحیح | lexicon |
| interface | واسط | lexicon |
| main | اصلی | lexicon |
| new | جدید | lexicon |
| package | بسته | lexicon |
| private | خصوصی | lexicon |
| protected | محافظتشده | lexicon |
| public | عمومی | lexicon |
| read | اقرأ | lexicon |
| sleep | نوم | lexicon |
| static | ایستا | lexicon |
| super | ابر | lexicon |
| switch | انتخاب | lexicon |
| this | این | lexicon |
| throw | پرتابکن | lexicon |
| void | تهی | lexicon |
| volatile | فرار | lexicon |
| write | اكتب | lexicon |

### A.6 BASIC

Host: ISO/IEC 10279, Information technology, Programming languages, Full BASIC. Names: name transformation.

| Host | Persian | Source |
|---|---|---|
| dim | dim | host form (no native word yet) |
| end | پایان | lexicon |
| for | برای | lexicon |
| gosub | gosub | host form (no native word yet) |
| goto | برو | lexicon |
| if | اگر | lexicon |
| input | input | host form (no native word yet) |
| let | بگذار | lexicon |
| next | next | host form (no native word yet) |
| print | print | host form (no native word yet) |
| rem | rem | host form (no native word yet) |
| return | بازگشت | lexicon |
| step | step | host form (no native word yet) |
| then | then | host form (no native word yet) |
| to | to | host form (no native word yet) |
| wend | wend | host form (no native word yet) |
| while | وقتی | lexicon |
| and | و | lexicon |
| or | یا | lexicon |
| not | نه | lexicon |
| mod | mod | host form (no native word yet) |

Standard library and runtime names of the BASIC binding:

| Host | Persian | Source |
|---|---|---|
| AS | بهعنوان | lexicon |
| CALL | فراخوان | lexicon |
| CONST | ثابت | lexicon |
| DO | انجامبده | lexicon |
| ELSE | وگرنه | lexicon |
| INT | صحیح | lexicon |
| SHARED | مشترك | lexicon |
| STATIC | ایستا | lexicon |
| STRING | رشته | lexicon |
| TIMER | مؤقت | lexicon |

### A.7 LOGO

Host: No international standard; the host is the Berkeley Logo dialect (bibliography). Names: name transformation.

| Host | Persian | Source |
|---|---|---|
| forward | أمامي | lexicon |
| back | back | host form (no native word yet) |
| left | left | host form (no native word yet) |
| right | right | host form (no native word yet) |
| penup | penup | host form (no native word yet) |
| pendown | pendown | host form (no native word yet) |
| repeat | repeat | host form (no native word yet) |
| to | to | host form (no native word yet) |
| end | پایان | lexicon |
| make | make | host form (no native word yet) |
| if | اگر | lexicon |
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

The lowering of Persian programs to C is verified by the reference implementation: runs, same output. Source Chintamani means a word of the original Hindawi transducers; lexicon, a word of the language's lexicon; proposed, a word proposed by the project and not yet reviewed by the language community.

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

