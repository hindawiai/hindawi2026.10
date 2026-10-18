# HLS sindhi 2026.10

**Sindhi bindings for programming languages: lexical mapping and lowering to the host standards**

Edition 2026.10, working draft, 2026-10-18. © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

## Foreword

This document was prepared by AyeAI, Hindawi project (Project ILM). It is generated from the Sindhi cell of Hindawi 2026.10 by lang/hindawi/tools/standards.py, so that the published standard and the reference implementation cannot drift apart. Its stage is a working draft: the words marked proposed in Annex A await review by the Sindhi language community, through the review pages of the Hindawi project.

## Introduction

This document lets programs be written in Sindhi, in the Arabic script, in each of the programming languages listed in Clause 1. Each binding is a programming language in its own right, Sindhi C for example, whose programs are lowered by the function defined in Clause 6 to programs of the host language, and are then processed by any conforming implementation of the host standard. The host standards are incorporated by reference and are not restated. Names keep a defined form down to object code (Clause 7), so programs written in Sindhi remain debuggable at the level of firmware, kernels and libraries.

## 1 Scope

This document specifies, for the Sindhi language written in the Arabic script, bindings to the following host programming languages: C, C preprocessor, C++, Java, Python, BASIC, LOGO. For each binding it specifies the native keywords and directives, the lowering of native programs to host programs, the treatment of names, and the requirements for conformance.

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

- binding: programming language defined by this document whose programs are written in Sindhi and lowered to one host language

- native keyword: word of this document that stands for one keyword, directive or standard library name of a host language

- lowering: function from native programs to host programs defined in Clause 6

- raising: inverse of lowering applied to a host program with a dictionary of names, giving back the native program exactly

- name transformation: function from native names to host identifiers defined in Clause 7

- C-level form: result of the name transformation; the form a native name takes in host source and in object code

## 4 Conformance

A conforming Sindhi program of a binding shall be a text that meets Clause 5 and whose lowering is a conforming program of the host language.

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

| Host | Sindhi | Source |
|---|---|---|
| auto | خودڪار | proposed |
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
| long | ڊگهو | proposed |
| register | سجل | lexicon |
| restrict | محدود | proposed |
| return | أرجع | lexicon |
| short | ننڍو | proposed |
| signed | نشانوارو | proposed |
| sizeof | حجم | lexicon |
| static | ساكن | lexicon |
| struct | بنية | lexicon |
| switch | بدل | lexicon |
| typedef | تعريفنوع | lexicon |
| union | اتحاد | lexicon |
| unsigned | بنانشان | proposed |
| void | فراغ | lexicon |
| volatile | متطاير | lexicon |
| while | طالما | lexicon |
| main | مکيه | proposed |

Standard library and runtime names of the C binding:

| Host | Sindhi | Source |
|---|---|---|
| INT_MAX | وڌ_کان_وڌ_عدد | proposed |
| NULL | عدم | lexicon |
| abs | مطلق_قدر | proposed |
| assert | أكد | lexicon |
| calloc | صفر_يادگيري_ڏيو | proposed |
| cos | جيب_تمام | proposed |
| exit | ٻاهر_نڪرو | proposed |
| exp | قوت_نما | proposed |
| free | حرر | lexicon |
| friend | دوست | proposed |
| isalnum | اکر_يا_انگ | proposed |
| isalpha | اکر_آهي | proposed |
| isdigit | انگ_آهي | proposed |
| isspace | خال_آهي | proposed |
| log | لاگرٿم | proposed |
| malloc | يادگيري_ڏيو | proposed |
| memcpy | يادگيري_نقل | proposed |
| operator | عامل | proposed |
| pow | قوت | proposed |
| printf | لکو | proposed |
| private | خاص | lexicon |
| protected | محمي | lexicon |
| public | عام | lexicon |
| putchar | اکر_لکو | proposed |
| raise | ارفع | lexicon |
| read | اقرأ | lexicon |
| signal | إشارة | lexicon |
| sin | جيب | proposed |
| sqrt | جذر | proposed |
| sscanf | لڙي_مان_پڙهو | proposed |
| strlen | لڙي_ڊيگهه | proposed |
| strncmp | لڙي_ڀيٽ | proposed |
| strstr | لڙي_ڳولا | proposed |
| template | سانچو | proposed |
| toupper | وڏو_اکر | proposed |
| virtual | مجازي | proposed |
| write | اكتب | lexicon |

### A.2 C preprocessor

Host: ISO/IEC 9899, Information technology, Programming languages, C (preprocessing directives). Names: name transformation.

| Host | Sindhi | Source |
|---|---|---|
| #define | #وصف_ڪريو | proposed |
| #include | #ضمن | lexicon |
| #if | #إذا | lexicon |
| #ifdef | #جيڪڏهن_وصف_ٿيل | proposed |
| #ifndef | #جيڪڏهن_وصف_نه_ٿيل | proposed |
| #else | #وإلا | lexicon |
| #elif | #وإلاإذا | lexicon |
| #endif | #جيڪڏهن_پورو | proposed |
| #undef | #وصف_رد | proposed |
| #pragma | #هدايت | proposed |
| #error | #غلطي | proposed |
| #line | #سٽ | proposed |

### A.3 C++

Host: ISO/IEC 14882, Programming languages, C++. Names: name transformation.

| Host | Sindhi | Source |
|---|---|---|
| auto | خودڪار | proposed |
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
| long | ڊگهو | proposed |
| register | سجل | lexicon |
| restrict | محدود | proposed |
| return | أرجع | lexicon |
| short | ننڍو | proposed |
| signed | نشانوارو | proposed |
| sizeof | حجم | lexicon |
| static | ساكن | lexicon |
| struct | بنية | lexicon |
| switch | بدل | lexicon |
| typedef | تعريفنوع | lexicon |
| union | اتحاد | lexicon |
| unsigned | بنانشان | proposed |
| void | فراغ | lexicon |
| volatile | متطاير | lexicon |
| while | طالما | lexicon |
| main | مکيه | proposed |
| bool | منطقي | lexicon |
| catch | امسك | lexicon |
| class | صنف | lexicon |
| delete | ميٽيو | proposed |
| explicit | واضح | proposed |
| false | خطأ | lexicon |
| friend | دوست | proposed |
| mutable | بدلجندڙ | proposed |
| namespace | نطاق | lexicon |
| new | جديد | lexicon |
| nullptr | خالي_اشارو | proposed |
| operator | عامل | proposed |
| private | خاص | lexicon |
| protected | محمي | lexicon |
| public | عام | lexicon |
| template | سانچو | proposed |
| this | هذا | lexicon |
| throw | ارم | lexicon |
| true | سچ | proposed |
| try | حاول | lexicon |
| typename | قسم_نالو | proposed |
| using | استعمال | proposed |
| virtual | مجازي | proposed |
| cout | ٻاهر | proposed |
| cin | اندر | proposed |
| endl | سٽ_پڄاڻي | proposed |

Standard library and runtime names of the C++ binding:

| Host | Sindhi | Source |
|---|---|---|
| INT_MAX | وڌ_کان_وڌ_عدد | proposed |
| NULL | عدم | lexicon |
| abs | مطلق_قدر | proposed |
| assert | أكد | lexicon |
| calloc | صفر_يادگيري_ڏيو | proposed |
| cos | جيب_تمام | proposed |
| exit | ٻاهر_نڪرو | proposed |
| exp | قوت_نما | proposed |
| free | حرر | lexicon |
| isalnum | اکر_يا_انگ | proposed |
| isalpha | اکر_آهي | proposed |
| isdigit | انگ_آهي | proposed |
| isspace | خال_آهي | proposed |
| left | کاٻي | proposed |
| log | لاگرٿم | proposed |
| malloc | يادگيري_ڏيو | proposed |
| memcpy | يادگيري_نقل | proposed |
| pipe | أنبوب | lexicon |
| pow | قوت | proposed |
| printf | لکو | proposed |
| putchar | اکر_لکو | proposed |
| raise | ارفع | lexicon |
| read | اقرأ | lexicon |
| right | ساڄي | proposed |
| signal | إشارة | lexicon |
| sin | جيب | proposed |
| sleep | نوم | lexicon |
| sqrt | جذر | proposed |
| sscanf | لڙي_مان_پڙهو | proposed |
| strlen | لڙي_ڊيگهه | proposed |
| strncmp | لڙي_ڀيٽ | proposed |
| strstr | لڙي_ڳولا | proposed |
| sync | متزامن | lexicon |
| toupper | وڏو_اکر | proposed |
| write | اكتب | lexicon |

### A.4 Java

Host: The Java Language Specification, Oracle, current edition. Names: unchanged.

| Host | Sindhi | Source |
|---|---|---|
| abstract | مجرد | lexicon |
| assert | أكد | lexicon |
| boolean | منطقي | proposed |
| break | اكسر | lexicon |
| byte | بائيٽ | proposed |
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
| final | حتمي | proposed |
| finally | أخيرا | lexicon |
| float | عائم | lexicon |
| for | لكل | lexicon |
| if | إذا | lexicon |
| implements | ينفذ | lexicon |
| import | استورد | lexicon |
| instanceof | نمونو_آهي | proposed |
| int | صحيح | lexicon |
| interface | واجهة | lexicon |
| long | ڊگهو | proposed |
| native | مقامي | proposed |
| new | جديد | lexicon |
| package | حزمة | lexicon |
| private | خاص | lexicon |
| protected | محمي | lexicon |
| public | عام | lexicon |
| return | أرجع | lexicon |
| short | ننڍو | proposed |
| static | ساكن | lexicon |
| super | أعلى | lexicon |
| switch | بدل | lexicon |
| synchronized | هم_وقت | proposed |
| this | هذا | lexicon |
| throw | ارم | lexicon |
| throws | اڇلائي | proposed |
| try | حاول | lexicon |
| void | فراغ | lexicon |
| volatile | متطاير | lexicon |
| while | طالما | lexicon |
| true | سچ | proposed |
| false | خطأ | lexicon |
| null | عدم | lexicon |
| String | نص | lexicon |
| System | سرشتو | proposed |

Standard library and runtime names of the Java binding:

| Host | Sindhi | Source |
|---|---|---|
| INT_MAX | وڌ_کان_وڌ_عدد | proposed |
| Object | كائن | lexicon |
| Thread | خيط | lexicon |
| abs | مطلق_قدر | proposed |
| auto | خودڪار | proposed |
| calloc | صفر_يادگيري_ڏيو | proposed |
| const | ثابت | lexicon |
| cos | جيب_تمام | proposed |
| exit | ٻاهر_نڪرو | proposed |
| exp | قوت_نما | proposed |
| extern | خارجي | lexicon |
| free | حرر | lexicon |
| friend | دوست | proposed |
| goto | اذهب | lexicon |
| inline | مضمن | lexicon |
| isalnum | اکر_يا_انگ | proposed |
| isalpha | اکر_آهي | proposed |
| isdigit | انگ_آهي | proposed |
| isspace | خال_آهي | proposed |
| log | لاگرٿم | proposed |
| main | مکيه | proposed |
| malloc | يادگيري_ڏيو | proposed |
| memcpy | يادگيري_نقل | proposed |
| operator | عامل | proposed |
| pow | قوت | proposed |
| printf | لکو | proposed |
| println | سٽ_ڇاپيو | proposed |
| putchar | اکر_لکو | proposed |
| raise | ارفع | lexicon |
| read | اقرأ | lexicon |
| register | سجل | lexicon |
| restrict | محدود | proposed |
| signal | إشارة | lexicon |
| signed | نشانوارو | proposed |
| sin | جيب | proposed |
| sizeof | حجم | lexicon |
| sleep | نوم | lexicon |
| sqrt | جذر | proposed |
| sscanf | لڙي_مان_پڙهو | proposed |
| strlen | لڙي_ڊيگهه | proposed |
| strncmp | لڙي_ڀيٽ | proposed |
| strstr | لڙي_ڳولا | proposed |
| struct | بنية | lexicon |
| template | سانچو | proposed |
| toupper | وڏو_اکر | proposed |
| typedef | تعريفنوع | lexicon |
| union | اتحاد | lexicon |
| unsigned | بنانشان | proposed |
| virtual | مجازي | proposed |
| write | اكتب | lexicon |

### A.5 Python

Host: The Python Language Reference, Python Software Foundation, current version. Names: unchanged.

| Host | Sindhi | Source |
|---|---|---|
| False | خطأ | lexicon |
| None | ڪجهه_نه | proposed |
| True | سچ | proposed |
| and | و | lexicon |
| as | كـ | lexicon |
| assert | أكد | lexicon |
| break | اكسر | lexicon |
| class | صنف | lexicon |
| continue | استمر | lexicon |
| def | وصف | proposed |
| del | هٽايو | proposed |
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
| is | آهي | proposed |
| lambda | مجهول | lexicon |
| nonlocal | غيرمقامي | proposed |
| not | ليس | lexicon |
| or | أو | lexicon |
| pass | لنگهه | proposed |
| raise | ارفع | lexicon |
| return | أرجع | lexicon |
| try | حاول | lexicon |
| while | طالما | lexicon |
| with | سان | proposed |
| yield | أنتج | lexicon |
| print | ڇاپيو | proposed |
| range | سلسلو | proposed |
| len | ڊيگهه | proposed |

Standard library and runtime names of the Python binding:

| Host | Sindhi | Source |
|---|---|---|
| Object | كائن | lexicon |
| String | نص | lexicon |
| System | سرشتو | proposed |
| Thread | خيط | lexicon |
| abstract | مجرد | lexicon |
| boolean | منطقي | proposed |
| byte | بائيٽ | proposed |
| case | حالة | lexicon |
| catch | امسك | lexicon |
| char | حرف | lexicon |
| const | ثابت | lexicon |
| default | افتراضي | lexicon |
| do | افعل | lexicon |
| double | مزدوج | lexicon |
| extends | يمتد | lexicon |
| final | حتمي | proposed |
| float | عائم | lexicon |
| goto | اذهب | lexicon |
| implements | ينفذ | lexicon |
| instanceof | نمونو_آهي | proposed |
| int | صحيح | lexicon |
| interface | واجهة | lexicon |
| long | ڊگهو | proposed |
| main | مکيه | proposed |
| native | مقامي | proposed |
| new | جديد | lexicon |
| package | حزمة | lexicon |
| println | سٽ_ڇاپيو | proposed |
| private | خاص | lexicon |
| protected | محمي | lexicon |
| read | اقرأ | lexicon |
| short | ننڍو | proposed |
| sleep | نوم | lexicon |
| sqrt | جذر | proposed |
| static | ساكن | lexicon |
| super | أعلى | lexicon |
| switch | بدل | lexicon |
| this | هذا | lexicon |
| throw | ارم | lexicon |
| throws | اڇلائي | proposed |
| void | فراغ | lexicon |
| volatile | متطاير | lexicon |
| write | اكتب | lexicon |

### A.6 BASIC

Host: ISO/IEC 10279, Information technology, Programming languages, Full BASIC. Names: name transformation.

| Host | Sindhi | Source |
|---|---|---|
| dim | ماپ | proposed |
| end | انته | lexicon |
| for | لكل | lexicon |
| gosub | ذيلي_وڃو | proposed |
| goto | اذهب | lexicon |
| if | إذا | lexicon |
| input | وٺو | proposed |
| let | ليكن | lexicon |
| next | ايندڙ_ڦيرو | proposed |
| print | ڇاپيو | proposed |
| rem | تبصرو | proposed |
| return | أرجع | lexicon |
| step | قدم_سان | proposed |
| then | ته | proposed |
| to | تائين | proposed |
| wend | جيستائين_پورو | proposed |
| while | طالما | lexicon |
| and | و | lexicon |
| or | أو | lexicon |
| not | ليس | lexicon |
| mod | باقي | proposed |

Standard library and runtime names of the BASIC binding:

| Host | Sindhi | Source |
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

| Host | Sindhi | Source |
|---|---|---|
| forward | أمامي | lexicon |
| back | پوئتي | proposed |
| left | کاٻي | proposed |
| right | ساڄي | proposed |
| penup | قلم_مٿي | proposed |
| pendown | قلم_هيٺ | proposed |
| repeat | ورجايو | proposed |
| to | تائين | proposed |
| end | انته | lexicon |
| make | ٺاهيو | proposed |
| if | إذا | lexicon |
| ifelse | جيڪڏهن_ٻي_صورت | proposed |
| home | گهر | proposed |
| clearscreen | پردو_صاف | proposed |

Standard library and runtime names of the LOGO binding:

| Host | Sindhi | Source |
|---|---|---|
| print | ڇاپيو | proposed |

## Annex B (informative) Coverage and review

| Binding | Host keywords with a native word | Library names |
|---|---|---|
| C | 35 of 35 | 37 |
| C preprocessor | 12 of 12 | 0 |
| C++ | 61 of 61 | 35 |
| Java | 51 of 51 | 50 |
| Python | 36 of 36 | 43 |
| BASIC | 21 of 21 | 10 |
| LOGO | 14 of 14 | 1 |

The lowering of Sindhi programs to C is verified by the reference implementation: runs, same output. Source Chintamani means a word of the original Hindawi transducers; lexicon, a word of the language's lexicon; proposed, a word proposed by the project and not yet reviewed by the language community.

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

