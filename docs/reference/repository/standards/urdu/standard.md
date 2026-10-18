# HLS ur 2026.10

**Information technology, Programming languages, Urdu keyword bindings for C, C++, Java, Python, BASIC and LOGO, and their lowering to the host language standards**

Edition 2026.10, draft proposal, 2026-10-18. © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

## Foreword

This draft is proposed by Abhishek Choudhary, AyeAI, for consideration by the Data Management System Sectional Committee, LITD 15, of the Bureau of Indian Standards, whose scope includes programming languages, their environments and system software interfaces. It is an indigenous draft: it adopts no International Standard, binds the language it names to the host programming language standards listed in Clause 2 by reference, and reproduces no text from them.

The method it standardizes was first published as the Hindawi Programming System on 15 August 2004, and has been developed since through the Hindawi releases. This draft is generated from the Urdu cell of Hindawi 2026.10 by lang/hindawi/tools/standards.py, so that the document and its reference implementation cannot diverge; a revision of either is a revision of both.

Annexes A, B and C are normative. Annexes D, E and F are informative.

Every binding in Annex A records its provenance. A binding recorded as proposed has not yet been reviewed by the Urdu language community; its review is part of the work towards an Indian Standard.

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. Hindawi™ and Romenagri™ are trademarks of Abhishek Choudhary. This document is an original work. It defines new programming languages by reference to the host language standards listed in Clause 2 and reproduces no text from them. Permission to adopt, translate or publish it as a standard is given by the copyright holder to a standards body on request.

## Introduction

A program has three properties that this draft keeps apart: the script it is written in, the human language its words come from, and the programming language standard that defines its meaning. The script is handled by transliteration, the language by the keyword bindings of Annex A, and the meaning by the host standard, which this draft does not alter.

A source text in the language is lowered to a source text of the host language and compiled by any conforming host translator. Native names reach the compiled program, and the debugger, in one fixed transliterated form, so that a program written in the language remains readable in that language at every level down to the machine.

## 1 Scope

This draft specifies, for programs written in Urdu in the Arabic script:

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

3.3 native keyword: a word of Urdu, written in the Arabic script, bound by Annex A to a host keyword.

3.4 binding: the pairing of one host keyword with one native keyword, for one host language.

3.5 construct: the programming construct a keyword denotes, which is the same across host languages, so that one native keyword serves it in every binding.

3.6 source text: a program, or part of one, written using native keywords, native names, or both.

3.7 native name: an identifier of a source text written wholly or partly in the Arabic script.

3.8 lowering: the transformation of a source text into a source text of the host language.

3.9 C-level form: the identifier of the host language that a native name becomes by name transformation, and under which it appears in compiled programs and to debuggers.

3.10 name transformation: the mapping of native names to C-level forms specified in Clause 9.

3.11 script filter: the mapping of the Arabic script to Devanagari that precedes transliteration, specified in Annex C.

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

6.2 Native letters are the characters of the Arabic block of ISO/IEC 10646 whose general category is a letter or a mark. Text written right to left is stored in logical order.

6.3 The Arabic script is written right to left.

6.4 The native digits below are equivalent, in numerals, to the decimal digits of the host language with the same value. A translator shall accept either.

| Code point | Digit | Value |
|---|---|---|
| U+0660 | ٠ | 0 |
| U+0661 | ١ | 1 |
| U+0662 | ٢ | 2 |
| U+0663 | ٣ | 3 |
| U+0664 | ٤ | 4 |
| U+0665 | ٥ | 5 |
| U+0666 | ٦ | 6 |
| U+0667 | ٧ | 7 |
| U+0668 | ٨ | 8 |
| U+0669 | ٩ | 9 |
| U+06F0 | ۰ | 0 |
| U+06F1 | ۱ | 1 |
| U+06F2 | ۲ | 2 |
| U+06F3 | ۳ | 3 |
| U+06F4 | ۴ | 4 |
| U+06F5 | ۵ | 5 |
| U+06F6 | ۶ | 6 |
| U+06F7 | ۷ | 7 |
| U+06F8 | ۸ | 8 |
| U+06F9 | ۹ | 9 |

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

The bindings of Annex A are maintained as a living register. A proposed binding becomes reviewed when the Urdu language community accepts it; a change to a reviewed binding is a revision of this draft. The construct, not the host keyword, is primary: one native keyword serves one construct in every binding where that construct occurs.

## Annex A (normative) Keyword bindings

### A.1 C

Host standard: ISO/IEC 9899, Information technology, Programming languages, C. Names are lowered by name transformation.

| Host keyword | Urdu | Provenance |
|---|---|---|
| auto | خودکار | proposed |
| break | توڑو | lexicon |
| case | حالت | lexicon |
| char | حرف | lexicon |
| const | ثابت | lexicon |
| continue | جاری | lexicon |
| default | طےشدہ | lexicon |
| do | کرو | lexicon |
| double | دوہرا | lexicon |
| else | ورنہ | lexicon |
| enum | شمار | lexicon |
| extern | خارجی | lexicon |
| float | اعشاری | lexicon |
| for | برائے | lexicon |
| goto | جاؤ | lexicon |
| if | اگر | lexicon |
| inline | اندرونی | lexicon |
| int | صحیح | lexicon |
| long | طویل | proposed |
| register | اندراج | lexicon |
| restrict | محدود | proposed |
| return | واپس | lexicon |
| short | مختصر | proposed |
| signed | علامتی | proposed |
| sizeof | حجم | lexicon |
| static | ساکن | lexicon |
| struct | ساخت | lexicon |
| switch | انتخاب | lexicon |
| typedef | قسمتعریف | lexicon |
| union | اتحاد | lexicon |
| unsigned | غیرعلامتی | proposed |
| void | خالی | lexicon |
| volatile | متلون | lexicon |
| while | جب | lexicon |
| main | مین | lexicon |

### A.2 C preprocessor

Host standard: ISO/IEC 9899, Information technology, Programming languages, C (preprocessing directives). Names are lowered by name transformation.

| Host keyword | Urdu | Provenance |
|---|---|---|
| #define | #تعریف_کرو | proposed |
| #include | #شامل | lexicon |
| #if | #اگر | lexicon |
| #ifdef | #اگر_تعریف_شدہ | proposed |
| #ifndef | #اگر_غیر_تعریف_شدہ | proposed |
| #else | #ورنہ | lexicon |
| #elif | #وگرنہ_اگر | lexicon |
| #endif | #اگر_ختم | proposed |
| #undef | #تعریف_منسوخ | proposed |
| #pragma | #ہدایت | proposed |
| #error | #غلطی | proposed |
| #line | #سطر | proposed |

### A.3 C++

Host standard: ISO/IEC 14882, Programming languages, C++. Names are lowered by name transformation.

| Host keyword | Urdu | Provenance |
|---|---|---|
| auto | خودکار | proposed |
| break | توڑو | lexicon |
| case | حالت | lexicon |
| char | حرف | lexicon |
| const | ثابت | lexicon |
| continue | جاری | lexicon |
| default | طےشدہ | lexicon |
| do | کرو | lexicon |
| double | دوہرا | lexicon |
| else | ورنہ | lexicon |
| enum | شمار | lexicon |
| extern | خارجی | lexicon |
| float | اعشاری | lexicon |
| for | برائے | lexicon |
| goto | جاؤ | lexicon |
| if | اگر | lexicon |
| inline | اندرونی | lexicon |
| int | صحیح | lexicon |
| long | طویل | proposed |
| register | اندراج | lexicon |
| restrict | محدود | proposed |
| return | واپس | lexicon |
| short | مختصر | proposed |
| signed | علامتی | proposed |
| sizeof | حجم | lexicon |
| static | ساکن | lexicon |
| struct | ساخت | lexicon |
| switch | انتخاب | lexicon |
| typedef | قسمتعریف | lexicon |
| union | اتحاد | lexicon |
| unsigned | غیرعلامتی | proposed |
| void | خالی | lexicon |
| volatile | متلون | lexicon |
| while | جب | lexicon |
| main | مین | lexicon |
| bool | منطقی | lexicon |
| catch | پکڑو | lexicon |
| class | جماعت | lexicon |
| delete | حذف | proposed |
| explicit | صریح | proposed |
| false | جھوٹ | lexicon |
| friend | دوست | proposed |
| mutable | تغیرپذیر | proposed |
| namespace | نامخلا | lexicon |
| new | نیا | lexicon |
| nullptr | خالی_اشاریہ | proposed |
| operator | عامل | proposed |
| private | نجی | lexicon |
| protected | محفوظ | lexicon |
| public | عوامی | lexicon |
| template | سانچہ | proposed |
| this | یہ | lexicon |
| throw | پھینکو | lexicon |
| true | سچ | lexicon |
| try | کوشش | lexicon |
| typename | قسم_نام | proposed |
| using | استعمال | proposed |
| virtual | مجازی | lexicon |
| cout | خارج | proposed |
| cin | داخل | proposed |
| endl | سطر_ختم | proposed |

### A.4 Java

Host standard: The Java Language Specification, Oracle, current edition. Names are lowered by unchanged.

| Host keyword | Urdu | Provenance |
|---|---|---|
| abstract | تجریدی | lexicon |
| assert | أكد | lexicon |
| boolean | منطقی | proposed |
| break | توڑو | lexicon |
| byte | بائٹ | proposed |
| case | حالت | lexicon |
| catch | پکڑو | lexicon |
| char | حرف | lexicon |
| class | جماعت | lexicon |
| continue | جاری | lexicon |
| default | طےشدہ | lexicon |
| do | کرو | lexicon |
| double | دوہرا | lexicon |
| else | ورنہ | lexicon |
| enum | شمار | lexicon |
| extends | توسیع | lexicon |
| final | حتمی | proposed |
| finally | آخرکار | lexicon |
| float | اعشاری | lexicon |
| for | برائے | lexicon |
| if | اگر | lexicon |
| implements | نافذ | lexicon |
| import | درآمد | lexicon |
| instanceof | نمونہ_ہے | proposed |
| int | صحیح | lexicon |
| interface | سطحرابطہ | lexicon |
| long | طویل | proposed |
| native | مقامی | proposed |
| new | نیا | lexicon |
| package | بستہ | lexicon |
| private | نجی | lexicon |
| protected | محفوظ | lexicon |
| public | عوامی | lexicon |
| return | واپس | lexicon |
| short | مختصر | proposed |
| static | ساکن | lexicon |
| super | بالا | proposed |
| switch | انتخاب | lexicon |
| synchronized | ہمزمان | proposed |
| this | یہ | lexicon |
| throw | پھینکو | lexicon |
| throws | پھینکتا | proposed |
| try | کوشش | lexicon |
| void | خالی | lexicon |
| volatile | متلون | lexicon |
| while | جب | lexicon |
| true | سچ | lexicon |
| false | جھوٹ | lexicon |
| null | تہی | lexicon |
| String | جملہ | lexicon |
| System | نظام | proposed |

### A.5 Python

Host standard: The Python Language Reference, Python Software Foundation, current version. Names are lowered by unchanged.

| Host keyword | Urdu | Provenance |
|---|---|---|
| False | جھوٹ | lexicon |
| None | کچھ_نہیں | proposed |
| True | سچ | lexicon |
| and | اور | lexicon |
| as | بطور | lexicon |
| assert | أكد | lexicon |
| break | توڑو | lexicon |
| class | جماعت | lexicon |
| continue | جاری | lexicon |
| def | تعریف | proposed |
| del | مٹاؤ | proposed |
| elif | وگرنہ_اگر | lexicon |
| else | ورنہ | lexicon |
| except | استثنا | lexicon |
| finally | آخرکار | lexicon |
| for | برائے | lexicon |
| from | سے | lexicon |
| global | عام | lexicon |
| if | اگر | lexicon |
| import | درآمد | lexicon |
| in | میں | lexicon |
| is | ہے | proposed |
| lambda | بےنام | lexicon |
| nonlocal | غیرمقامی | proposed |
| not | نہیں | lexicon |
| or | یا | lexicon |
| pass | گزرو | proposed |
| raise | اٹھاؤ | lexicon |
| return | واپس | lexicon |
| try | کوشش | lexicon |
| while | جب | lexicon |
| with | ساتھ | proposed |
| yield | دو | lexicon |
| print | چھاپو | proposed |
| range | سلسلہ | proposed |
| len | لمبائی | proposed |

### A.6 BASIC

Host standard: ISO/IEC 10279, Information technology, Programming languages, Full BASIC. Names are lowered by name transformation.

| Host keyword | Urdu | Provenance |
|---|---|---|
| dim | ابعاد | proposed |
| end | اختتام | lexicon |
| for | برائے | lexicon |
| gosub | ذیلی_جاؤ | proposed |
| goto | جاؤ | lexicon |
| if | اگر | lexicon |
| input | حاصل_کرو | proposed |
| let | مانو | lexicon |
| next | اگلا_چکر | proposed |
| print | چھاپو | proposed |
| rem | تبصرہ | proposed |
| return | واپس | lexicon |
| step | قدم_سے | proposed |
| then | تو | proposed |
| to | تک | proposed |
| wend | جب_تک_ختم | proposed |
| while | جب | lexicon |
| and | اور | lexicon |
| or | یا | lexicon |
| not | نہیں | lexicon |
| mod | باقی | proposed |

### A.7 LOGO

Host standard: No international standard; the host is the Berkeley Logo dialect (bibliography). Names are lowered by name transformation.

| Host keyword | Urdu | Provenance |
|---|---|---|
| forward | أمامي | lexicon |
| back | پیچھے | proposed |
| left | بائیں | proposed |
| right | دائیں | proposed |
| penup | قلم_اٹھاؤ | proposed |
| pendown | قلم_رکھو | proposed |
| repeat | دہراؤ | proposed |
| to | تک | proposed |
| end | اختتام | lexicon |
| make | بناؤ | proposed |
| if | اگر | lexicon |
| ifelse | اگر_ورنہ | proposed |
| home | گھر | proposed |
| clearscreen | سکرین_صاف | proposed |

## Annex B (normative) Name transformation test vectors

Each native name shall be given the C-level form shown. The vectors are computed by the reference implementation when this draft is generated.

| Native name | C-level form |
|---|---|
| آخری | _aakhzaree |
| آغاز | _aagzaajza |
| آمد | _aama_da |
| آنے_والا | _aanaee_waalaa |
| احاطہ | _i_hzaa_tza_ha |
| اختتام | _ikhza_ta_taama |
| ادوار_فی_لفظ | _i_dawaara_phzee_laphza_jzza |
| ادوار_فی_مداخلت | _i_dawaara_phzee_ma_daakhzala_ta |
| استعداد | _isa_ta_aee_daa_da |
| استعمال_کرتا | _isa_ta_aeemaala_kara_taa |
| استعمال_کرتا_پچھلا | _isa_ta_aeemaala_kara_taa_pachhalaa |
| اشارات | _ishaaraa_ta |
| اشارہ_گر | _ishaara_ha_gara |
| اشاریہ_دار | _ishaaree_ha__daara |
| اشاریہ_رجسٹر | _ishaaree_ha_rajasatara |
| اشارے | _ishaaraee |
| اشاعت | _ishaa_aee_ta |
| اشیاء | _ishayaa_ha |
| اقدار | _ikza_daara |
| اقدام | _ikza_daama |
| اقل | _ikzala |
| اقل_اجزا | _ikzala__aajajzaa |
| الفاظ | _ilaphzaa_jzza |
| الٹ | _ilata |
| انبار | _inabaara |
| انبار_2 | _inabaara_2 |
| انتخاب_2 | _ina_takhzaaba_2 |
| انتظار | _ina_ta_jzzaara |
| انتہا | _ina_ta_haa |
| انحراف | _ina_hzaraaphza |

## Annex C (normative) Script filter

The Arabic script is mapped to Devanagari by the filter of the Hindawi tools for this script (fltr_ur_hi), unchanged since its publication in Chintamani.

Letters of the Perso-Arabic orthographies that the filter does not distinguish are first folded to the nearest Urdu letter: ٻ to ب, ټ to ٹ, ٽ to ٹ, ٿ to تھ, ڀ to بھ, ځ to ز, ڄ to ج, څ to س, ڇ to چھ, ډ to ڈ, ڊ to ڈ, ڌ to دھ, ڍ to ڈھ, ڏ to د, ړ to ڑ, ږ to ژ, ڙ to ڑ, ښ to ش, ڦ to پھ, ڪ to ک, ګ to گ, ڱ to نگ, ڳ to گ, ڻ to ن, ڼ to ن, ۀ to ہ, ۍ to ی, ې to ی.

## Annex D (informative) Library names

### D C

| Host name | Urdu | Provenance |
|---|---|---|
| INT_MAX | زیادہ_سے_زیادہ_عدد | proposed |
| NULL | تہی | lexicon |
| abs | مطلق_قدر | proposed |
| assert | أكد | lexicon |
| calloc | صفر_حافظہ_دو | proposed |
| cos | جیب_تمام | proposed |
| exit | باہر_نکلو | proposed |
| exp | قوت_نما | proposed |
| free | آزاد | lexicon |
| friend | دوست | proposed |
| isalnum | حرف_یا_ہندسہ | proposed |
| isalpha | حرف_ہے | proposed |
| isdigit | ہندسہ_ہے | proposed |
| isspace | خلا_ہے | proposed |
| log | لوگارتھم | proposed |
| malloc | حافظہ_دو | proposed |
| memcpy | حافظہ_نقل | proposed |
| operator | عامل | proposed |
| pow | قوت | proposed |
| printf | لکھو | proposed |
| private | نجی | lexicon |
| protected | محفوظ | lexicon |
| public | عوامی | lexicon |
| putchar | حرف_لکھو | proposed |
| raise | اٹھاؤ | lexicon |
| read | اقرأ | lexicon |
| signal | اشارہ | lexicon |
| sin | جیب | proposed |
| sqrt | جذر | proposed |
| sscanf | لڑی_سے_پڑھو | proposed |
| strlen | لڑی_لمبائی | proposed |
| strncmp | لڑی_موازنہ | proposed |
| strstr | لڑی_تلاش | proposed |
| template | سانچہ | proposed |
| toupper | بڑا_حرف | proposed |
| virtual | مجازی | lexicon |
| write | اكتب | lexicon |

### D C++

| Host name | Urdu | Provenance |
|---|---|---|
| INT_MAX | زیادہ_سے_زیادہ_عدد | proposed |
| NULL | تہی | lexicon |
| abs | مطلق_قدر | proposed |
| assert | أكد | lexicon |
| calloc | صفر_حافظہ_دو | proposed |
| cos | جیب_تمام | proposed |
| exit | باہر_نکلو | proposed |
| exp | قوت_نما | proposed |
| free | آزاد | lexicon |
| isalnum | حرف_یا_ہندسہ | proposed |
| isalpha | حرف_ہے | proposed |
| isdigit | ہندسہ_ہے | proposed |
| isspace | خلا_ہے | proposed |
| left | بائیں | proposed |
| log | لوگارتھم | proposed |
| malloc | حافظہ_دو | proposed |
| memcpy | حافظہ_نقل | proposed |
| pipe | أنبوب | lexicon |
| pow | قوت | proposed |
| printf | لکھو | proposed |
| putchar | حرف_لکھو | proposed |
| raise | اٹھاؤ | lexicon |
| read | اقرأ | lexicon |
| right | دائیں | proposed |
| signal | اشارہ | lexicon |
| sin | جیب | proposed |
| sleep | نوم | lexicon |
| sqrt | جذر | proposed |
| sscanf | لڑی_سے_پڑھو | proposed |
| strlen | لڑی_لمبائی | proposed |
| strncmp | لڑی_موازنہ | proposed |
| strstr | لڑی_تلاش | proposed |
| sync | ہمآہنگ | lexicon |
| toupper | بڑا_حرف | proposed |
| write | اكتب | lexicon |

### D Java

| Host name | Urdu | Provenance |
|---|---|---|
| INT_MAX | زیادہ_سے_زیادہ_عدد | proposed |
| Object | شے | lexicon |
| Thread | دھاگہ | lexicon |
| abs | مطلق_قدر | proposed |
| auto | خودکار | proposed |
| calloc | صفر_حافظہ_دو | proposed |
| const | ثابت | lexicon |
| cos | جیب_تمام | proposed |
| exit | باہر_نکلو | proposed |
| exp | قوت_نما | proposed |
| extern | خارجی | lexicon |
| free | آزاد | lexicon |
| friend | دوست | proposed |
| goto | جاؤ | lexicon |
| inline | اندرونی | lexicon |
| isalnum | حرف_یا_ہندسہ | proposed |
| isalpha | حرف_ہے | proposed |
| isdigit | ہندسہ_ہے | proposed |
| isspace | خلا_ہے | proposed |
| log | لوگارتھم | proposed |
| main | مین | lexicon |
| malloc | حافظہ_دو | proposed |
| memcpy | حافظہ_نقل | proposed |
| operator | عامل | proposed |
| pow | قوت | proposed |
| printf | لکھو | proposed |
| println | سطر_چھاپو | proposed |
| putchar | حرف_لکھو | proposed |
| raise | اٹھاؤ | lexicon |
| read | اقرأ | lexicon |
| register | اندراج | lexicon |
| restrict | محدود | proposed |
| signal | اشارہ | lexicon |
| signed | علامتی | proposed |
| sin | جیب | proposed |
| sizeof | حجم | lexicon |
| sleep | نوم | lexicon |
| sqrt | جذر | proposed |
| sscanf | لڑی_سے_پڑھو | proposed |
| strlen | لڑی_لمبائی | proposed |
| strncmp | لڑی_موازنہ | proposed |
| strstr | لڑی_تلاش | proposed |
| struct | ساخت | lexicon |
| template | سانچہ | proposed |
| toupper | بڑا_حرف | proposed |
| typedef | قسمتعریف | lexicon |
| union | اتحاد | lexicon |
| unsigned | غیرعلامتی | proposed |
| virtual | مجازی | lexicon |
| write | اكتب | lexicon |

### D Python

| Host name | Urdu | Provenance |
|---|---|---|
| Object | شے | lexicon |
| String | جملہ | lexicon |
| System | نظام | proposed |
| Thread | دھاگہ | lexicon |
| abstract | تجریدی | lexicon |
| boolean | منطقی | proposed |
| byte | بائٹ | proposed |
| case | حالت | lexicon |
| catch | پکڑو | lexicon |
| char | حرف | lexicon |
| const | ثابت | lexicon |
| default | طےشدہ | lexicon |
| do | کرو | lexicon |
| double | دوہرا | lexicon |
| extends | توسیع | lexicon |
| final | حتمی | proposed |
| float | اعشاری | lexicon |
| goto | جاؤ | lexicon |
| implements | نافذ | lexicon |
| instanceof | نمونہ_ہے | proposed |
| int | صحیح | lexicon |
| interface | سطحرابطہ | lexicon |
| long | طویل | proposed |
| main | مین | lexicon |
| native | مقامی | proposed |
| new | نیا | lexicon |
| package | بستہ | lexicon |
| println | سطر_چھاپو | proposed |
| private | نجی | lexicon |
| protected | محفوظ | lexicon |
| public | عوامی | lexicon |
| read | اقرأ | lexicon |
| short | مختصر | proposed |
| sleep | نوم | lexicon |
| sqrt | جذر | proposed |
| static | ساکن | lexicon |
| super | بالا | proposed |
| switch | انتخاب | lexicon |
| this | یہ | lexicon |
| throw | پھینکو | lexicon |
| throws | پھینکتا | proposed |
| void | خالی | lexicon |
| volatile | متلون | lexicon |
| write | اكتب | lexicon |

### D BASIC

| Host name | Urdu | Provenance |
|---|---|---|
| AS | بطور | lexicon |
| CALL | بلاؤ | lexicon |
| CONST | ثابت | lexicon |
| DO | کرو | lexicon |
| ELSE | ورنہ | lexicon |
| INT | صحیح | lexicon |
| SHARED | مشترك | lexicon |
| STATIC | ساکن | lexicon |
| STRING | جملہ | lexicon |
| TIMER | مؤقت | lexicon |

### D LOGO

| Host name | Urdu | Provenance |
|---|---|---|
| print | چھاپو | proposed |

## Annex E (informative) Conformance tests

The reference implementation is tested with the programs of samples/gate in the Hindawi repository, which cover the programming content of the GATE Computer Science paper. Recorded on 2026-10-18: 113 of 113 C programs, written in Urdu, were lowered, compiled and run, and printed exactly what their English originals print; 1 of 1 Python programs did the same; 117 of 117 files were reversed byte for byte.

The program below, as written in the language, its transliterated form, and the C that the transducer gives:

### E source

```
#شامل <stdio.h>
/* binary search in a sorted array */
صحیح ثنائی_تلاش(صحیح اقدار[], صحیح گنتی, صحیح کلید) {
  صحیح کم = 0, بلند = گنتی - 1;
  جب (کم <= بلند) {
    صحیح درمیان = کم + (بلند - کم) / 2;
    اگر (اقدار[درمیان] == کلید) واپس درمیان;
    اگر (اقدار[درمیان] < کلید) کم = درمیان + 1; ورنہ بلند = درمیان - 1;
  }
  واپس -1;
}
صحیح مین(خالی) {
  صحیح اقدار[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  لکھو("%d %d\n", ثنائی_تلاش(اقدار, 10, 23), ثنائی_تلاش(اقدار, 10, 7));
  واپس 0;
}
```

### E script filter

```
#शामल <stdio.h>
/* binary search in a sorted array */
स़ह़ीह़ स़़नायी_तलाश(स़ह़ीह़ इक़दार[], स़ह़ीह़ गनती, स़ह़ीह़ कलीद) {
  स़ह़ीह़ कम = 0, बलनद = गनती - 1;
  जब (कम <= बलनद) {
    स़ह़ीह़ दरमयान = कम + (बलनद - कम) / 2;
    इगर (इक़दार[दरमयान] == कलीद) वापस दरमयान;
    इगर (इक़दार[दरमयान] < कलीद) कम = दरमयान + 1; वरनह बलनद = दरमयान - 1;
  }
  वापस -1;
}
स़ह़ीह़ मीन(ख़ाली) {
  स़ह़ीह़ इक़दार[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  लखॉ("%d %d\n", स़़नायी_तलाश(इक़दार, 10, 23), स़़नायी_तलाश(इक़दार, 10, 7));
  वापस 0;
}
```

### E Romenagri

```
#shaamala <stdio.h>
/* binary search in a sorted array */
sza_hzee_hza szzanaayee__talaasha(sza_hzee_hza _ikza_daara[], sza_hzee_hza gana_tee, sza_hzee_hza kalee_da) {
  sza_hzee_hza kama = 0, balana_da = gana_tee - 1;
  jaba (kama <= balana_da) {
    sza_hzee_hza _daramayaana = kama + (balana_da - kama) / 2;
    _igara (_ikza_daara[_daramayaana] == kalee_da) waapasa _daramayaana;
    _igara (_ikza_daara[_daramayaana] < kalee_da) kama = _daramayaana + 1; warana_ha balana_da = _daramayaana - 1;
  }
  waapasa -1;
}
sza_hzee_hza meena(khzaalee) {
  sza_hzee_hza _ikza_daara[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  lakhau("%d %d\n", szzanaayee__talaasha(_ikza_daara, 10, 23), szzanaayee__talaasha(_ikza_daara, 10, 7));
  waapasa 0;
}
```

### E C

```
#include <stdio.h>
/* binary search in a sorted array */
int szzanaayee__talaasha(int _ikza_daara[], int gana_tee, int kalee_da) {
  int kama = 0, balana_da = gana_tee - 1;
  while (kama <= balana_da) {
    int _daramayaana = kama + (balana_da - kama) / 2;
    if (_ikza_daara[_daramayaana] == kalee_da) return _daramayaana;
    if (_ikza_daara[_daramayaana] < kalee_da) kama = _daramayaana + 1; else balana_da = _daramayaana - 1;
  }
  return -1;
}
int main(void) {
  int _ikza_daara[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  printf("%d %d\n", szzanaayee__talaasha(_ikza_daara, 10, 23), szzanaayee__talaasha(_ikza_daara, 10, 7));
  return 0;
}
```

## Annex F (informative) Provenance of the bindings

| Provenance | Bindings |
|---|---|
| lexicon | 155 |
| proposed | 75 |

## Bibliography

- Hindawi Programming System, first public release 15 August 2004, savannah.nongnu.org/projects/hindawi
- Chintamani, hindawiai/chintamani: the Hindawi transducers and the Romenagri tools
- Hindawi 2026.10, hindawiai/hindawi2026.10, concept DOI 10.5281/zenodo.23424410
- IS 12 : 2005, Guide for drafting and presentation of Indian Standards
- ISO/IEC 10279, Information technology, Programming languages, Full BASIC
- Berkeley Logo reference manual, Brian Harvey

