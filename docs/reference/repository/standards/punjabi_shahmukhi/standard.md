# HLS punjabi_shahmukhi 2026.10

**Information technology, Programming languages, Punjabi Shahmukhi keyword bindings for C, C++, Java, Python, BASIC and LOGO, and their lowering to the host language standards**

Edition 2026.10, draft proposal, 2026-10-18. © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

## Foreword

This draft is proposed by Abhishek Choudhary, AyeAI, for consideration by the Data Management System Sectional Committee, LITD 15, of the Bureau of Indian Standards, whose scope includes programming languages, their environments and system software interfaces. It is an indigenous draft: it adopts no International Standard, binds the language it names to the host programming language standards listed in Clause 2 by reference, and reproduces no text from them.

The method it standardizes was first published as the Hindawi Programming System on 15 August 2004, and has been developed since through the Hindawi releases. This draft is generated from the Punjabi Shahmukhi cell of Hindawi 2026.10 by lang/hindawi/tools/standards.py, so that the document and its reference implementation cannot diverge; a revision of either is a revision of both.

Annexes A, B and C are normative. Annexes D, E and F are informative.

Every binding in Annex A records its provenance. A binding recorded as proposed has not yet been reviewed by the Punjabi Shahmukhi language community; its review is part of the work towards an Indian Standard.

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. Hindawi™ and Romenagri™ are trademarks of Abhishek Choudhary. This document is an original work. It defines new programming languages by reference to the host language standards listed in Clause 2 and reproduces no text from them. Permission to adopt, translate or publish it as a standard is given by the copyright holder to a standards body on request.

## Introduction

A program has three properties that this draft keeps apart: the script it is written in, the human language its words come from, and the programming language standard that defines its meaning. The script is handled by transliteration, the language by the keyword bindings of Annex A, and the meaning by the host standard, which this draft does not alter.

A source text in the language is lowered to a source text of the host language and compiled by any conforming host translator. Native names reach the compiled program, and the debugger, in one fixed transliterated form, so that a program written in the language remains readable in that language at every level down to the machine.

## 1 Scope

This draft specifies, for programs written in Punjabi Shahmukhi in the Arabic script:

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

3.3 native keyword: a word of Punjabi Shahmukhi, written in the Arabic script, bound by Annex A to a host keyword.

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

The bindings of Annex A are maintained as a living register. A proposed binding becomes reviewed when the Punjabi Shahmukhi language community accepts it; a change to a reviewed binding is a revision of this draft. The construct, not the host keyword, is primary: one native keyword serves one construct in every binding where that construct occurs.

## Annex A (normative) Keyword bindings

### A.1 C

Host standard: ISO/IEC 9899, Information technology, Programming languages, C. Names are lowered by name transformation.

| Host keyword | Punjabi Shahmukhi | Provenance |
|---|---|---|
| auto | خودکار | proposed |
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
| long | لما | proposed |
| register | سجل | lexicon |
| restrict | محدود | proposed |
| return | أرجع | lexicon |
| short | چھوٹا | proposed |
| signed | نشانیوالا | proposed |
| sizeof | حجم | lexicon |
| static | ساكن | lexicon |
| struct | بنية | lexicon |
| switch | بدل | lexicon |
| typedef | تعريفنوع | lexicon |
| union | اتحاد | lexicon |
| unsigned | بنانشانی | proposed |
| void | فراغ | lexicon |
| volatile | متطاير | lexicon |
| while | طالما | lexicon |
| main | مکھ | proposed |

### A.2 C preprocessor

Host standard: ISO/IEC 9899, Information technology, Programming languages, C (preprocessing directives). Names are lowered by name transformation.

| Host keyword | Punjabi Shahmukhi | Provenance |
|---|---|---|
| #define | #تعریف_کرو | proposed |
| #include | #ضمن | lexicon |
| #if | #إذا | lexicon |
| #ifdef | #جے_تعریف_شدہ | proposed |
| #ifndef | #جے_بنا_تعریف | proposed |
| #else | #وإلا | lexicon |
| #elif | #وإلاإذا | lexicon |
| #endif | #جے_انت | proposed |
| #undef | #تعریف_رد | proposed |
| #pragma | #ہدایت | proposed |
| #error | #غلطی | proposed |
| #line | #سطر | proposed |

### A.3 C++

Host standard: ISO/IEC 14882, Programming languages, C++. Names are lowered by name transformation.

| Host keyword | Punjabi Shahmukhi | Provenance |
|---|---|---|
| auto | خودکار | proposed |
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
| long | لما | proposed |
| register | سجل | lexicon |
| restrict | محدود | proposed |
| return | أرجع | lexicon |
| short | چھوٹا | proposed |
| signed | نشانیوالا | proposed |
| sizeof | حجم | lexicon |
| static | ساكن | lexicon |
| struct | بنية | lexicon |
| switch | بدل | lexicon |
| typedef | تعريفنوع | lexicon |
| union | اتحاد | lexicon |
| unsigned | بنانشانی | proposed |
| void | فراغ | lexicon |
| volatile | متطاير | lexicon |
| while | طالما | lexicon |
| main | مکھ | proposed |
| bool | منطقي | lexicon |
| catch | امسك | lexicon |
| class | صنف | lexicon |
| delete | مٹاؤ | proposed |
| explicit | واضح | proposed |
| false | خطأ | lexicon |
| friend | یار | proposed |
| mutable | بدلنجوگ | proposed |
| namespace | نطاق | lexicon |
| new | جديد | lexicon |
| nullptr | خالی_سوچک | proposed |
| operator | عامل | proposed |
| private | خاص | lexicon |
| protected | محمي | lexicon |
| public | عام | lexicon |
| template | سانچا | proposed |
| this | هذا | lexicon |
| throw | ارم | lexicon |
| true | سچ | proposed |
| try | حاول | lexicon |
| typename | قسم_ناں | proposed |
| using | ورتوں | proposed |
| virtual | مجازی | proposed |
| cout | باہر | proposed |
| cin | اندر | proposed |
| endl | سطر_انت | proposed |

### A.4 Java

Host standard: The Java Language Specification, Oracle, current edition. Names are lowered by unchanged.

| Host keyword | Punjabi Shahmukhi | Provenance |
|---|---|---|
| abstract | مجرد | lexicon |
| assert | أكد | lexicon |
| boolean | منطقی | proposed |
| break | اكسر | lexicon |
| byte | بائٹ | proposed |
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
| final | حتمی | proposed |
| finally | أخيرا | lexicon |
| float | عائم | lexicon |
| for | لكل | lexicon |
| if | إذا | lexicon |
| implements | ينفذ | lexicon |
| import | استورد | lexicon |
| instanceof | نمونہ_اے | proposed |
| int | صحيح | lexicon |
| interface | واجهة | lexicon |
| long | لما | proposed |
| native | مقامی | proposed |
| new | جديد | lexicon |
| package | حزمة | lexicon |
| private | خاص | lexicon |
| protected | محمي | lexicon |
| public | عام | lexicon |
| return | أرجع | lexicon |
| short | چھوٹا | proposed |
| static | ساكن | lexicon |
| super | أعلى | lexicon |
| switch | بدل | lexicon |
| synchronized | ہمزمان | proposed |
| this | هذا | lexicon |
| throw | ارم | lexicon |
| throws | سٹدا | proposed |
| try | حاول | lexicon |
| void | فراغ | lexicon |
| volatile | متطاير | lexicon |
| while | طالما | lexicon |
| true | سچ | proposed |
| false | خطأ | lexicon |
| null | عدم | lexicon |
| String | نص | lexicon |
| System | نظام | proposed |

### A.5 Python

Host standard: The Python Language Reference, Python Software Foundation, current version. Names are lowered by unchanged.

| Host keyword | Punjabi Shahmukhi | Provenance |
|---|---|---|
| False | خطأ | lexicon |
| None | کجھ_نئیں | proposed |
| True | سچ | proposed |
| and | و | lexicon |
| as | كـ | lexicon |
| assert | أكد | lexicon |
| break | اكسر | lexicon |
| class | صنف | lexicon |
| continue | استمر | lexicon |
| def | تعریف | proposed |
| del | ہٹاؤ | proposed |
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
| is | اے | proposed |
| lambda | مجهول | lexicon |
| nonlocal | غیرمقامی | proposed |
| not | ليس | lexicon |
| or | أو | lexicon |
| pass | لنگھو | proposed |
| raise | ارفع | lexicon |
| return | أرجع | lexicon |
| try | حاول | lexicon |
| while | طالما | lexicon |
| with | نال | proposed |
| yield | أنتج | lexicon |
| print | چھاپو | proposed |
| range | سلسلہ | proposed |
| len | لمبائی | proposed |

### A.6 BASIC

Host standard: ISO/IEC 10279, Information technology, Programming languages, Full BASIC. Names are lowered by name transformation.

| Host keyword | Punjabi Shahmukhi | Provenance |
|---|---|---|
| dim | اکار | proposed |
| end | انته | lexicon |
| for | لكل | lexicon |
| gosub | ذیلی_جاؤ | proposed |
| goto | اذهب | lexicon |
| if | إذا | lexicon |
| input | لوو | proposed |
| let | ليكن | lexicon |
| next | اگلا_گیڑ | proposed |
| print | چھاپو | proposed |
| rem | تبصرہ | proposed |
| return | أرجع | lexicon |
| step | قدم_نال | proposed |
| then | تاں | proposed |
| to | تک | proposed |
| wend | جدوں_تک_انت | proposed |
| while | طالما | lexicon |
| and | و | lexicon |
| or | أو | lexicon |
| not | ليس | lexicon |
| mod | باقی | proposed |

### A.7 LOGO

Host standard: No international standard; the host is the Berkeley Logo dialect (bibliography). Names are lowered by name transformation.

| Host keyword | Punjabi Shahmukhi | Provenance |
|---|---|---|
| forward | أمامي | lexicon |
| back | پچھے | proposed |
| left | کھبے | proposed |
| right | سجے | proposed |
| penup | قلم_چکو | proposed |
| pendown | قلم_رکھو | proposed |
| repeat | دہراؤ | proposed |
| to | تک | proposed |
| end | انته | lexicon |
| make | بناؤ | proposed |
| if | إذا | lexicon |
| ifelse | جے_نئیں_تے | proposed |
| home | گھر | proposed |
| clearscreen | پردہ_صاف | proposed |

## Annex B (normative) Name transformation test vectors

Each native name shall be given the C-level form shown. The vectors are computed by the reference implementation when this draft is generated.

| Native name | C-level form |
|---|---|
| آخری | _aakhzaree |
| آمد | _aama_da |
| آون_والا | _aayauna_waalaa |
| اتلا | _i_talaa |
| ادھار | _i_dhaara |
| اسدھا | _isa_dhaa |
| اشارہ_گر | _ishaara_ha_gara |
| اشاریہ_دار | _ishaaree_ha__daara |
| اشاریہ_رجسٹر | _ishaaree_ha_rajasatara |
| اشارے | _ishaaraee |
| اقل | _ikzala |
| اقل_جز | _ikzala_jajza |
| الٹ | _ilata |
| انت | _ina_ta |
| اندراج | _ina_daraaja |
| اندرلی_ڈگری | _ina_daralee_dagaree |
| اندرونی | _ina_daraunee |
| انعکاسی | _ina_aeekaasee |
| انکڑے | _inaka_rdaee |
| اوسط | _ousa_tza |
| اوسطن | _ousa_tzana |
| اپڑ | _ipa_rda |
| اچا | _ichaa |
| اچائی | _ichaayee |
| اڈیک | _ideeka |
| اکسار | _ikasaara |
| اکو_ویلے | _ikau_weelaee |
| اگلا | _igalaa |
| اگیتر | _igee_tara |
| بائٹاں | baayataa_m |

## Annex C (normative) Script filter

The Arabic script is mapped to Devanagari by the filter of the Hindawi tools for this script (fltr_ur_hi), unchanged since its publication in Chintamani.

Letters of the Perso-Arabic orthographies that the filter does not distinguish are first folded to the nearest Urdu letter: ٻ to ب, ټ to ٹ, ٽ to ٹ, ٿ to تھ, ڀ to بھ, ځ to ز, ڄ to ج, څ to س, ڇ to چھ, ډ to ڈ, ڊ to ڈ, ڌ to دھ, ڍ to ڈھ, ڏ to د, ړ to ڑ, ږ to ژ, ڙ to ڑ, ښ to ش, ڦ to پھ, ڪ to ک, ګ to گ, ڱ to نگ, ڳ to گ, ڻ to ن, ڼ to ن, ۀ to ہ, ۍ to ی, ې to ی.

## Annex D (informative) Library names

### D C

| Host name | Punjabi Shahmukhi | Provenance |
|---|---|---|
| INT_MAX | ودھ_توں_ودھ_عدد | proposed |
| NULL | عدم | lexicon |
| abs | مطلق_قدر | proposed |
| assert | أكد | lexicon |
| calloc | صفر_حافظہ_دیو | proposed |
| cos | جیب_تمام | proposed |
| exit | باہر_نکلو | proposed |
| exp | قوت_نما | proposed |
| free | حرر | lexicon |
| friend | یار | proposed |
| isalnum | حرف_یا_ہندسہ | proposed |
| isalpha | حرف_اے | proposed |
| isdigit | ہندسہ_اے | proposed |
| isspace | خلا_اے | proposed |
| log | لوگارتھم | proposed |
| malloc | حافظہ_دیو | proposed |
| memcpy | حافظہ_نقل | proposed |
| operator | عامل | proposed |
| pow | قوت | proposed |
| printf | لکھو | proposed |
| private | خاص | lexicon |
| protected | محمي | lexicon |
| public | عام | lexicon |
| putchar | حرف_لکھو | proposed |
| raise | ارفع | lexicon |
| read | اقرأ | lexicon |
| signal | إشارة | lexicon |
| sin | جیب | proposed |
| sqrt | جذر | proposed |
| sscanf | لڑی_توں_پڑھو | proposed |
| strlen | لڑی_لمبائی | proposed |
| strncmp | لڑی_مقابلہ | proposed |
| strstr | لڑی_کھوج | proposed |
| template | سانچا | proposed |
| toupper | وڈا_حرف | proposed |
| virtual | مجازی | proposed |
| write | اكتب | lexicon |

### D C++

| Host name | Punjabi Shahmukhi | Provenance |
|---|---|---|
| INT_MAX | ودھ_توں_ودھ_عدد | proposed |
| NULL | عدم | lexicon |
| abs | مطلق_قدر | proposed |
| assert | أكد | lexicon |
| calloc | صفر_حافظہ_دیو | proposed |
| cos | جیب_تمام | proposed |
| exit | باہر_نکلو | proposed |
| exp | قوت_نما | proposed |
| free | حرر | lexicon |
| isalnum | حرف_یا_ہندسہ | proposed |
| isalpha | حرف_اے | proposed |
| isdigit | ہندسہ_اے | proposed |
| isspace | خلا_اے | proposed |
| left | کھبے | proposed |
| log | لوگارتھم | proposed |
| malloc | حافظہ_دیو | proposed |
| memcpy | حافظہ_نقل | proposed |
| pipe | أنبوب | lexicon |
| pow | قوت | proposed |
| printf | لکھو | proposed |
| putchar | حرف_لکھو | proposed |
| raise | ارفع | lexicon |
| read | اقرأ | lexicon |
| right | سجے | proposed |
| signal | إشارة | lexicon |
| sin | جیب | proposed |
| sleep | نوم | lexicon |
| sqrt | جذر | proposed |
| sscanf | لڑی_توں_پڑھو | proposed |
| strlen | لڑی_لمبائی | proposed |
| strncmp | لڑی_مقابلہ | proposed |
| strstr | لڑی_کھوج | proposed |
| sync | متزامن | lexicon |
| toupper | وڈا_حرف | proposed |
| write | اكتب | lexicon |

### D Java

| Host name | Punjabi Shahmukhi | Provenance |
|---|---|---|
| INT_MAX | ودھ_توں_ودھ_عدد | proposed |
| Object | كائن | lexicon |
| Thread | خيط | lexicon |
| abs | مطلق_قدر | proposed |
| auto | خودکار | proposed |
| calloc | صفر_حافظہ_دیو | proposed |
| const | ثابت | lexicon |
| cos | جیب_تمام | proposed |
| exit | باہر_نکلو | proposed |
| exp | قوت_نما | proposed |
| extern | خارجي | lexicon |
| free | حرر | lexicon |
| friend | یار | proposed |
| goto | اذهب | lexicon |
| inline | مضمن | lexicon |
| isalnum | حرف_یا_ہندسہ | proposed |
| isalpha | حرف_اے | proposed |
| isdigit | ہندسہ_اے | proposed |
| isspace | خلا_اے | proposed |
| log | لوگارتھم | proposed |
| main | مکھ | proposed |
| malloc | حافظہ_دیو | proposed |
| memcpy | حافظہ_نقل | proposed |
| operator | عامل | proposed |
| pow | قوت | proposed |
| printf | لکھو | proposed |
| println | سطر_چھاپو | proposed |
| putchar | حرف_لکھو | proposed |
| raise | ارفع | lexicon |
| read | اقرأ | lexicon |
| register | سجل | lexicon |
| restrict | محدود | proposed |
| signal | إشارة | lexicon |
| signed | نشانیوالا | proposed |
| sin | جیب | proposed |
| sizeof | حجم | lexicon |
| sleep | نوم | lexicon |
| sqrt | جذر | proposed |
| sscanf | لڑی_توں_پڑھو | proposed |
| strlen | لڑی_لمبائی | proposed |
| strncmp | لڑی_مقابلہ | proposed |
| strstr | لڑی_کھوج | proposed |
| struct | بنية | lexicon |
| template | سانچا | proposed |
| toupper | وڈا_حرف | proposed |
| typedef | تعريفنوع | lexicon |
| union | اتحاد | lexicon |
| unsigned | بنانشانی | proposed |
| virtual | مجازی | proposed |
| write | اكتب | lexicon |

### D Python

| Host name | Punjabi Shahmukhi | Provenance |
|---|---|---|
| Object | كائن | lexicon |
| String | نص | lexicon |
| System | نظام | proposed |
| Thread | خيط | lexicon |
| abstract | مجرد | lexicon |
| boolean | منطقی | proposed |
| byte | بائٹ | proposed |
| case | حالة | lexicon |
| catch | امسك | lexicon |
| char | حرف | lexicon |
| const | ثابت | lexicon |
| default | افتراضي | lexicon |
| do | افعل | lexicon |
| double | مزدوج | lexicon |
| extends | يمتد | lexicon |
| final | حتمی | proposed |
| float | عائم | lexicon |
| goto | اذهب | lexicon |
| implements | ينفذ | lexicon |
| instanceof | نمونہ_اے | proposed |
| int | صحيح | lexicon |
| interface | واجهة | lexicon |
| long | لما | proposed |
| main | مکھ | proposed |
| native | مقامی | proposed |
| new | جديد | lexicon |
| package | حزمة | lexicon |
| println | سطر_چھاپو | proposed |
| private | خاص | lexicon |
| protected | محمي | lexicon |
| read | اقرأ | lexicon |
| short | چھوٹا | proposed |
| sleep | نوم | lexicon |
| sqrt | جذر | proposed |
| static | ساكن | lexicon |
| super | أعلى | lexicon |
| switch | بدل | lexicon |
| this | هذا | lexicon |
| throw | ارم | lexicon |
| throws | سٹدا | proposed |
| void | فراغ | lexicon |
| volatile | متطاير | lexicon |
| write | اكتب | lexicon |

### D BASIC

| Host name | Punjabi Shahmukhi | Provenance |
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

### D LOGO

| Host name | Punjabi Shahmukhi | Provenance |
|---|---|---|
| print | چھاپو | proposed |

## Annex E (informative) Conformance tests

The reference implementation is tested with the programs of samples/gate in the Hindawi repository, which cover the programming content of the GATE Computer Science paper. Recorded on 2026-10-18: 113 of 113 C programs, written in Punjabi Shahmukhi, were lowered, compiled and run, and printed exactly what their English originals print; 1 of 1 Python programs did the same; 117 of 117 files were reversed byte for byte.

The program below, as written in the language, its transliterated form, and the C that the transducer gives:

### E source

```
#ضمن <stdio.h>
/* binary search in a sorted array */
صحيح ثنائی_کھوج(صحيح مل[], صحيح گنتی, صحيح کنجی) {
  صحيح نیواں = 0, اچا = گنتی - 1;
  طالما (نیواں <= اچا) {
    صحيح وچکار = نیواں + (اچا - نیواں) / 2;
    إذا (مل[وچکار] == کنجی) أرجع وچکار;
    إذا (مل[وچکار] < کنجی) نیواں = وچکار + 1; وإلا اچا = وچکار - 1;
  }
  أرجع -1;
}
صحيح مکھ(فراغ) {
  صحيح مل[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  لکھو("%d %d\n", ثنائی_کھوج(مل, 10, 23), ثنائی_کھوج(مل, 10, 7));
  أرجع 0;
}
```

### E script filter

```
#ॹमन <stdio.h>
/* binary search in a sorted array */
स़ह़इह़ स़़नायी_खॉज(स़ह़इह़ मल[], स़ह़इह़ गनती, स़ह़इह़ कनजी) {
  स़ह़इह़ नीवां = 0, इचा = गनती - 1;
  त़ालमा (नीवां <= इचा) {
    स़ह़इह़ वचकार = नीवां + (इचा - नीवां) / 2;
    आज़़ा (मल[वचकार] == कनजी) आरजए वचकार;
    आज़़ा (मल[वचकार] < कनजी) नीवां = वचकार + 1; वआला इचा = वचकार - 1;
  }
  आरजए -1;
}
स़ह़इह़ मख(फ़राग़) {
  स़ह़इह़ मल[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  लखॉ("%d %d\n", स़़नायी_खॉज(मल, 10, 23), स़़नायी_खॉज(मल, 10, 7));
  आरजए 0;
}
```

### E Romenagri

```
#_jzamana <stdio.h>
/* binary search in a sorted array */
sza_hza_i_hza szzanaayee_khauja(sza_hza_i_hza mala[], sza_hza_i_hza gana_tee, sza_hza_i_hza kanajee) {
  sza_hza_i_hza neewaa_m = 0, _ichaa = gana_tee - 1;
  _tzaalamaa (neewaa_m <= _ichaa) {
    sza_hza_i_hza wachakaara = neewaa_m + (_ichaa - neewaa_m) / 2;
    _aajzzaa (mala[wachakaara] == kanajee) _aaraja_aee wachakaara;
    _aajzzaa (mala[wachakaara] < kanajee) neewaa_m = wachakaara + 1; wa_aalaa _ichaa = wachakaara - 1;
  }
  _aaraja_aee -1;
}
sza_hza_i_hza makha(phzaraagza) {
  sza_hza_i_hza mala[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  lakhau("%d %d\n", szzanaayee_khauja(mala, 10, 23), szzanaayee_khauja(mala, 10, 7));
  _aaraja_aee 0;
}
```

### E C

```
#include <stdio.h>
/* binary search in a sorted array */
int szzanaayee_khauja(int mala[], int gana_tee, int kanajee) {
  int neewaa_m = 0, _ichaa = gana_tee - 1;
  while (neewaa_m <= _ichaa) {
    int wachakaara = neewaa_m + (_ichaa - neewaa_m) / 2;
    if (mala[wachakaara] == kanajee) return wachakaara;
    if (mala[wachakaara] < kanajee) neewaa_m = wachakaara + 1; else _ichaa = wachakaara - 1;
  }
  return -1;
}
int main(void) {
  int mala[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  printf("%d %d\n", szzanaayee_khauja(mala, 10, 23), szzanaayee_khauja(mala, 10, 7));
  return 0;
}
```

## Annex F (informative) Provenance of the bindings

| Provenance | Bindings |
|---|---|
| lexicon | 150 |
| proposed | 80 |

## Bibliography

- Hindawi Programming System, first public release 15 August 2004, savannah.nongnu.org/projects/hindawi
- Chintamani, hindawiai/chintamani: the Hindawi transducers and the Romenagri tools
- Hindawi 2026.10, hindawiai/hindawi2026.10, concept DOI 10.5281/zenodo.23424410
- IS 12 : 2005, Guide for drafting and presentation of Indian Standards
- ISO/IEC 10279, Information technology, Programming languages, Full BASIC
- Berkeley Logo reference manual, Brian Harvey

