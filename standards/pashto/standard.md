# HLS pashto 2026.10

**Pashto bindings for programming languages: lexical mapping and lowering to the host standards**

Edition 2026.10, working draft, 2026-10-18. © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

## Foreword

This document was prepared by AyeAI, Hindawi project (Project ILM). It is generated from the Pashto cell of Hindawi 2026.10 by lang/hindawi/tools/standards.py, so that the published standard and the reference implementation cannot drift apart. Its stage is a working draft: the words marked proposed in Annex A await review by the Pashto language community, through the review pages of the Hindawi project.

## Introduction

This document lets programs be written in Pashto, in the Arabic script, in each of the programming languages listed in Clause 1. Each binding is a programming language in its own right, Pashto C for example, whose programs are lowered by the function defined in Clause 6 to programs of the host language, and are then processed by any conforming implementation of the host standard. The host standards are incorporated by reference and are not restated. Names keep a defined form down to object code (Clause 7), so programs written in Pashto remain debuggable at the level of firmware, kernels and libraries.

## 1 Scope

This document specifies, for the Pashto language written in the Arabic script, bindings to the following host programming languages: C, C preprocessor, C++, Java, Python, BASIC, LOGO. For each binding it specifies the native keywords and directives, the lowering of native programs to host programs, the treatment of names, and the requirements for conformance.

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

- binding: programming language defined by this document whose programs are written in Pashto and lowered to one host language

- native keyword: word of this document that stands for one keyword, directive or standard library name of a host language

- lowering: function from native programs to host programs defined in Clause 6

- raising: inverse of lowering applied to a host program with a dictionary of names, giving back the native program exactly

- name transformation: function from native names to host identifiers defined in Clause 7

- C-level form: result of the name transformation; the form a native name takes in host source and in object code

## 4 Conformance

A conforming Pashto program of a binding shall be a text that meets Clause 5 and whose lowering is a conforming program of the host language.

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

| Host | Pashto | Source |
|---|---|---|
| auto | خپلکاری | proposed |
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
| long | اوږد | proposed |
| register | سجل | lexicon |
| restrict | محدود | proposed |
| return | أرجع | lexicon |
| short | لنډ | proposed |
| signed | نښهدار | proposed |
| sizeof | حجم | lexicon |
| static | ساكن | lexicon |
| struct | بنية | lexicon |
| switch | بدل | lexicon |
| typedef | تعريفنوع | lexicon |
| union | اتحاد | lexicon |
| unsigned | بینښه | proposed |
| void | فراغ | lexicon |
| volatile | متطاير | lexicon |
| while | طالما | lexicon |
| main | اصلي | proposed |

Standard library and runtime names of the C binding:

| Host | Pashto | Source |
|---|---|---|
| INT_MAX | لوی_عدد | proposed |
| NULL | عدم | lexicon |
| abs | مطلق_قیمت | proposed |
| assert | أكد | lexicon |
| calloc | حافظه_صفر_ورکړه | proposed |
| cos | کوساین | proposed |
| exit | وتل | proposed |
| exp | توانیز_تابع | proposed |
| free | حرر | lexicon |
| friend | ملګری | proposed |
| isalnum | که_توری_یا_عدد | proposed |
| isalpha | که_توری | proposed |
| isdigit | که_عدد | proposed |
| isspace | که_تشه | proposed |
| log | لوګاریتم | proposed |
| malloc | حافظه_ورکړه | proposed |
| memcpy | حافظه_نقل | proposed |
| operator | چلوونکی | proposed |
| pow | توان | proposed |
| printf | چاپ_کړه | proposed |
| private | خاص | lexicon |
| protected | محمي | lexicon |
| public | عام | lexicon |
| putchar | توری_چاپ_کړه | proposed |
| raise | ارفع | lexicon |
| read | اقرأ | lexicon |
| signal | إشارة | lexicon |
| sin | ساین | proposed |
| sqrt | جذر | proposed |
| sscanf | له_مزي_ولوله | proposed |
| strlen | مزي_اوږدوالی | proposed |
| strncmp | مزي_پرتله | proposed |
| strstr | مزي_پلټنه | proposed |
| template | کينډۍ | proposed |
| toupper | لوی_توری | proposed |
| virtual | مجازي | proposed |
| write | اكتب | lexicon |

### A.2 C preprocessor

Host: ISO/IEC 9899, Information technology, Programming languages, C (preprocessing directives). Names: name transformation.

| Host | Pashto | Source |
|---|---|---|
| #define | #تعریف_کړه | proposed |
| #include | #ضمن | lexicon |
| #if | #إذا | lexicon |
| #ifdef | #که_تعریف_شوی | proposed |
| #ifndef | #که_نه_تعریف_شوی | proposed |
| #else | #وإلا | lexicon |
| #elif | #وإلاإذا | lexicon |
| #endif | #د_که_پای | proposed |
| #undef | #تعریف_لغوه | proposed |
| #pragma | #لارښوونه | proposed |
| #error | #تېروتنه | proposed |
| #line | #کرښه | proposed |

### A.3 C++

Host: ISO/IEC 14882, Programming languages, C++. Names: name transformation.

| Host | Pashto | Source |
|---|---|---|
| auto | خپلکاری | proposed |
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
| long | اوږد | proposed |
| register | سجل | lexicon |
| restrict | محدود | proposed |
| return | أرجع | lexicon |
| short | لنډ | proposed |
| signed | نښهدار | proposed |
| sizeof | حجم | lexicon |
| static | ساكن | lexicon |
| struct | بنية | lexicon |
| switch | بدل | lexicon |
| typedef | تعريفنوع | lexicon |
| union | اتحاد | lexicon |
| unsigned | بینښه | proposed |
| void | فراغ | lexicon |
| volatile | متطاير | lexicon |
| while | طالما | lexicon |
| main | اصلي | proposed |
| bool | منطقي | lexicon |
| catch | امسك | lexicon |
| class | صنف | lexicon |
| delete | ړنګول | proposed |
| explicit | څرګند | proposed |
| false | خطأ | lexicon |
| friend | ملګری | proposed |
| mutable | بدلیدونکی | proposed |
| namespace | نطاق | lexicon |
| new | جديد | lexicon |
| nullptr | تش_اشاره | proposed |
| operator | چلوونکی | proposed |
| private | خاص | lexicon |
| protected | محمي | lexicon |
| public | عام | lexicon |
| template | کينډۍ | proposed |
| this | هذا | lexicon |
| throw | ارم | lexicon |
| true | ریښتیا | proposed |
| try | حاول | lexicon |
| typename | ډول_نوم | proposed |
| using | کارول | proposed |
| virtual | مجازي | proposed |
| cout | وتنه | proposed |
| cin | ننوتنه | proposed |
| endl | کرښه_پای | proposed |

Standard library and runtime names of the C++ binding:

| Host | Pashto | Source |
|---|---|---|
| INT_MAX | لوی_عدد | proposed |
| NULL | عدم | lexicon |
| abs | مطلق_قیمت | proposed |
| assert | أكد | lexicon |
| calloc | حافظه_صفر_ورکړه | proposed |
| cos | کوساین | proposed |
| exit | وتل | proposed |
| exp | توانیز_تابع | proposed |
| free | حرر | lexicon |
| isalnum | که_توری_یا_عدد | proposed |
| isalpha | که_توری | proposed |
| isdigit | که_عدد | proposed |
| isspace | که_تشه | proposed |
| left | کیڼ | proposed |
| log | لوګاریتم | proposed |
| malloc | حافظه_ورکړه | proposed |
| memcpy | حافظه_نقل | proposed |
| pipe | أنبوب | lexicon |
| pow | توان | proposed |
| printf | چاپ_کړه | proposed |
| putchar | توری_چاپ_کړه | proposed |
| raise | ارفع | lexicon |
| read | اقرأ | lexicon |
| right | ښی | proposed |
| signal | إشارة | lexicon |
| sin | ساین | proposed |
| sleep | نوم | lexicon |
| sqrt | جذر | proposed |
| sscanf | له_مزي_ولوله | proposed |
| strlen | مزي_اوږدوالی | proposed |
| strncmp | مزي_پرتله | proposed |
| strstr | مزي_پلټنه | proposed |
| sync | متزامن | lexicon |
| toupper | لوی_توری | proposed |
| write | اكتب | lexicon |

### A.4 Java

Host: The Java Language Specification, Oracle, current edition. Names: unchanged.

| Host | Pashto | Source |
|---|---|---|
| abstract | مجرد | lexicon |
| assert | أكد | lexicon |
| boolean | منطقي | proposed |
| break | اكسر | lexicon |
| byte | بایټ | proposed |
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
| final | نهایي | proposed |
| finally | أخيرا | lexicon |
| float | عائم | lexicon |
| for | لكل | lexicon |
| if | إذا | lexicon |
| implements | ينفذ | lexicon |
| import | استورد | lexicon |
| instanceof | بېلګه_د | proposed |
| int | صحيح | lexicon |
| interface | واجهة | lexicon |
| long | اوږد | proposed |
| native | ځایی | proposed |
| new | جديد | lexicon |
| package | حزمة | lexicon |
| private | خاص | lexicon |
| protected | محمي | lexicon |
| public | عام | lexicon |
| return | أرجع | lexicon |
| short | لنډ | proposed |
| static | ساكن | lexicon |
| super | أعلى | lexicon |
| switch | بدل | lexicon |
| synchronized | همغږی | proposed |
| this | هذا | lexicon |
| throw | ارم | lexicon |
| throws | غورځوي | proposed |
| try | حاول | lexicon |
| void | فراغ | lexicon |
| volatile | متطاير | lexicon |
| while | طالما | lexicon |
| true | ریښتیا | proposed |
| false | خطأ | lexicon |
| null | عدم | lexicon |
| String | نص | lexicon |
| System | سیستم | proposed |

Standard library and runtime names of the Java binding:

| Host | Pashto | Source |
|---|---|---|
| INT_MAX | لوی_عدد | proposed |
| Object | كائن | lexicon |
| Thread | خيط | lexicon |
| abs | مطلق_قیمت | proposed |
| auto | خپلکاری | proposed |
| calloc | حافظه_صفر_ورکړه | proposed |
| const | ثابت | lexicon |
| cos | کوساین | proposed |
| exit | وتل | proposed |
| exp | توانیز_تابع | proposed |
| extern | خارجي | lexicon |
| free | حرر | lexicon |
| friend | ملګری | proposed |
| goto | اذهب | lexicon |
| inline | مضمن | lexicon |
| isalnum | که_توری_یا_عدد | proposed |
| isalpha | که_توری | proposed |
| isdigit | که_عدد | proposed |
| isspace | که_تشه | proposed |
| log | لوګاریتم | proposed |
| main | اصلي | proposed |
| malloc | حافظه_ورکړه | proposed |
| memcpy | حافظه_نقل | proposed |
| operator | چلوونکی | proposed |
| pow | توان | proposed |
| printf | چاپ_کړه | proposed |
| println | چاپ_کرښه | proposed |
| putchar | توری_چاپ_کړه | proposed |
| raise | ارفع | lexicon |
| read | اقرأ | lexicon |
| register | سجل | lexicon |
| restrict | محدود | proposed |
| signal | إشارة | lexicon |
| signed | نښهدار | proposed |
| sin | ساین | proposed |
| sizeof | حجم | lexicon |
| sleep | نوم | lexicon |
| sqrt | جذر | proposed |
| sscanf | له_مزي_ولوله | proposed |
| strlen | مزي_اوږدوالی | proposed |
| strncmp | مزي_پرتله | proposed |
| strstr | مزي_پلټنه | proposed |
| struct | بنية | lexicon |
| template | کينډۍ | proposed |
| toupper | لوی_توری | proposed |
| typedef | تعريفنوع | lexicon |
| union | اتحاد | lexicon |
| unsigned | بینښه | proposed |
| virtual | مجازي | proposed |
| write | اكتب | lexicon |

### A.5 Python

Host: The Python Language Reference, Python Software Foundation, current version. Names: unchanged.

| Host | Pashto | Source |
|---|---|---|
| False | خطأ | lexicon |
| None | هیڅ | proposed |
| True | ریښتیا | proposed |
| and | و | lexicon |
| as | كـ | lexicon |
| assert | أكد | lexicon |
| break | اكسر | lexicon |
| class | صنف | lexicon |
| continue | استمر | lexicon |
| def | تعریف | proposed |
| del | لرېکړه | proposed |
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
| is | دی | proposed |
| lambda | مجهول | lexicon |
| nonlocal | غیرځایی | proposed |
| not | ليس | lexicon |
| or | أو | lexicon |
| pass | تیرشه | proposed |
| raise | ارفع | lexicon |
| return | أرجع | lexicon |
| try | حاول | lexicon |
| while | طالما | lexicon |
| with | سره | proposed |
| yield | أنتج | lexicon |
| print | چاپ | proposed |
| range | لړ | proposed |
| len | اوږدوالی | proposed |

Standard library and runtime names of the Python binding:

| Host | Pashto | Source |
|---|---|---|
| Object | كائن | lexicon |
| String | نص | lexicon |
| System | سیستم | proposed |
| Thread | خيط | lexicon |
| abstract | مجرد | lexicon |
| boolean | منطقي | proposed |
| byte | بایټ | proposed |
| case | حالة | lexicon |
| catch | امسك | lexicon |
| char | حرف | lexicon |
| const | ثابت | lexicon |
| default | افتراضي | lexicon |
| do | افعل | lexicon |
| double | مزدوج | lexicon |
| extends | يمتد | lexicon |
| final | نهایي | proposed |
| float | عائم | lexicon |
| goto | اذهب | lexicon |
| implements | ينفذ | lexicon |
| instanceof | بېلګه_د | proposed |
| int | صحيح | lexicon |
| interface | واجهة | lexicon |
| long | اوږد | proposed |
| main | اصلي | proposed |
| native | ځایی | proposed |
| new | جديد | lexicon |
| package | حزمة | lexicon |
| println | چاپ_کرښه | proposed |
| private | خاص | lexicon |
| protected | محمي | lexicon |
| read | اقرأ | lexicon |
| short | لنډ | proposed |
| sleep | نوم | lexicon |
| sqrt | جذر | proposed |
| static | ساكن | lexicon |
| super | أعلى | lexicon |
| switch | بدل | lexicon |
| this | هذا | lexicon |
| throw | ارم | lexicon |
| throws | غورځوي | proposed |
| void | فراغ | lexicon |
| volatile | متطاير | lexicon |
| write | اكتب | lexicon |

### A.6 BASIC

Host: ISO/IEC 10279, Information technology, Programming languages, Full BASIC. Names: name transformation.

| Host | Pashto | Source |
|---|---|---|
| dim | بعد | proposed |
| end | انته | lexicon |
| for | لكل | lexicon |
| gosub | ځه_فرعي | proposed |
| goto | اذهب | lexicon |
| if | إذا | lexicon |
| input | واخله | proposed |
| let | ليكن | lexicon |
| next | بل_ځل | proposed |
| print | چاپ | proposed |
| rem | تبصره | proposed |
| return | أرجع | lexicon |
| step | ګام_په | proposed |
| then | نو | proposed |
| to | تر | proposed |
| wend | پای_ترهغه | proposed |
| while | طالما | lexicon |
| and | و | lexicon |
| or | أو | lexicon |
| not | ليس | lexicon |
| mod | پاتی | proposed |

Standard library and runtime names of the BASIC binding:

| Host | Pashto | Source |
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

| Host | Pashto | Source |
|---|---|---|
| forward | أمامي | lexicon |
| back | شاته | proposed |
| left | کیڼ | proposed |
| right | ښی | proposed |
| penup | قلم_پورته | proposed |
| pendown | قلم_ښکته | proposed |
| repeat | تکرار | proposed |
| to | تر | proposed |
| end | انته | lexicon |
| make | جوړ | proposed |
| if | إذا | lexicon |
| ifelse | که_نو | proposed |
| home | کور | proposed |
| clearscreen | پاڼه_پاکه | proposed |

Standard library and runtime names of the LOGO binding:

| Host | Pashto | Source |
|---|---|---|
| print | چاپ | proposed |

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

The lowering of Pashto programs to C is verified by the reference implementation: runs, same output. Source Chintamani means a word of the original Hindawi transducers; lexicon, a word of the language's lexicon; proposed, a word proposed by the project and not yet reviewed by the language community.

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

