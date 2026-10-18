# HLS sindhi 2026.10

**Information technology, Programming languages, Sindhi keyword bindings for C, C++, Java, Python, BASIC and LOGO, and their lowering to the host language standards**

Edition 2026.10, draft proposal, 2026-10-18. © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

## Foreword

This draft is proposed by Abhishek Choudhary, AyeAI, for consideration by the Data Management System Sectional Committee, LITD 15, of the Bureau of Indian Standards, whose scope includes programming languages, their environments and system software interfaces. It is an indigenous draft: it adopts no International Standard, binds the language it names to the host programming language standards listed in Clause 2 by reference, and reproduces no text from them.

The method it standardizes was first published as the Hindawi Programming System on 15 August 2004, and has been developed since through the Hindawi releases. This draft is generated from the Sindhi cell of Hindawi 2026.10 by lang/hindawi/tools/standards.py, so that the document and its reference implementation cannot diverge; a revision of either is a revision of both.

Annexes A, B and C are normative. Annexes D, E and F are informative.

Every binding in Annex A records its provenance. A binding recorded as proposed has not yet been reviewed by the Sindhi language community; its review is part of the work towards an Indian Standard.

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. Hindawi™ and Romenagri™ are trademarks of Abhishek Choudhary. This document is an original work. It defines new programming languages by reference to the host language standards listed in Clause 2 and reproduces no text from them. Permission to adopt, translate or publish it as a standard is given by the copyright holder to a standards body on request.

## Introduction

A program has three properties that this draft keeps apart: the script it is written in, the human language its words come from, and the programming language standard that defines its meaning. The script is handled by transliteration, the language by the keyword bindings of Annex A, and the meaning by the host standard, which this draft does not alter.

A source text in the language is lowered to a source text of the host language and compiled by any conforming host translator. Native names reach the compiled program, and the debugger, in one fixed transliterated form, so that a program written in the language remains readable in that language at every level down to the machine.

## 1 Scope

This draft specifies, for programs written in Sindhi in the Arabic script:

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

3.3 native keyword: a word of Sindhi, written in the Arabic script, bound by Annex A to a host keyword.

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

The bindings of Annex A are maintained as a living register. A proposed binding becomes reviewed when the Sindhi language community accepts it; a change to a reviewed binding is a revision of this draft. The construct, not the host keyword, is primary: one native keyword serves one construct in every binding where that construct occurs.

## Annex A (normative) Keyword bindings

### A.1 C

Host standard: ISO/IEC 9899, Information technology, Programming languages, C. Names are lowered by name transformation.

| Host keyword | Sindhi | Provenance |
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

### A.2 C preprocessor

Host standard: ISO/IEC 9899, Information technology, Programming languages, C (preprocessing directives). Names are lowered by name transformation.

| Host keyword | Sindhi | Provenance |
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

Host standard: ISO/IEC 14882, Programming languages, C++. Names are lowered by name transformation.

| Host keyword | Sindhi | Provenance |
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

### A.4 Java

Host standard: The Java Language Specification, Oracle, current edition. Names are lowered by unchanged.

| Host keyword | Sindhi | Provenance |
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

### A.5 Python

Host standard: The Python Language Reference, Python Software Foundation, current version. Names are lowered by unchanged.

| Host keyword | Sindhi | Provenance |
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

### A.6 BASIC

Host standard: ISO/IEC 10279, Information technology, Programming languages, Full BASIC. Names are lowered by name transformation.

| Host keyword | Sindhi | Provenance |
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

### A.7 LOGO

Host standard: No international standard; the host is the Berkeley Logo dialect (bibliography). Names are lowered by name transformation.

| Host keyword | Sindhi | Provenance |
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

## Annex B (normative) Name transformation test vectors

Each native name shall be given the C-level form shown. The vectors are computed by the reference implementation when this draft is generated.

| Native name | C-level form |
|---|---|
| آخري | _aakhzara_i |
| آمد | _aama_da |
| ابتو | _iba_tau |
| استعمال_ٿيل | _isa_ta_aeemaala__tha_ila |
| استعمال_ڪري | _isa_ta_aeemaala_kara_i |
| استعمال_ڪري_اڳيون | _isa_ta_aeemaala_kara_i__aagayouna |
| استعمال_ڪندڙ | _isa_ta_aeemaala_kana_da_rda |
| اشارا | _ishaaraa |
| اشارو | _ishaarau |
| اشاريو_رجسٽر | _ishaarayou_rajasatara |
| اشاريي_وارو | _ishaara_i_i_waarau |
| اضافي | _i_jzaaphza_i |
| اظهار | _i_jzza_haara |
| اقل_جزا | _ikzala_jajzaa |
| انتظار | _ina_ta_jzzaara |
| اندروني | _ina_darauna_i |
| اندروني_درجو | _ina_darauna_i__darajau |
| اندريون_ترتيب | _ina_darayouna__tara_ta_iba |
| انعڪاسي | _ina_aeekaasa_i |
| اوسط | _ousa_tza |
| اونهائي | _ouna_haaya_i |
| اوچائي | _ouchaaya_i |
| ايندڙ | _i_ina_da_rda |
| اڳواٽ | _igawaata |
| اڳياڙي | _igayyaa_rda_i |
| اڳين_ترتيب | _iga_ina__tara_ta_iba |
| اڳيون | _igayouna |
| اڻ_استعمال_ٿيل | _ina__aasa_ta_aeemaala__tha_ila |
| اڻسڌو | _inasa_dhau |
| بائيٽون | baaya_itauna |

## Annex C (normative) Script filter

The Arabic script is mapped to Devanagari by the filter of the Hindawi tools for this script (fltr_ur_hi), unchanged since its publication in Chintamani.

Letters of the Perso-Arabic orthographies that the filter does not distinguish are first folded to the nearest Urdu letter: ٻ to ب, ټ to ٹ, ٽ to ٹ, ٿ to تھ, ڀ to بھ, ځ to ز, ڄ to ج, څ to س, ڇ to چھ, ډ to ڈ, ڊ to ڈ, ڌ to دھ, ڍ to ڈھ, ڏ to د, ړ to ڑ, ږ to ژ, ڙ to ڑ, ښ to ش, ڦ to پھ, ڪ to ک, ګ to گ, ڱ to نگ, ڳ to گ, ڻ to ن, ڼ to ن, ۀ to ہ, ۍ to ی, ې to ی.

## Annex D (informative) Library names

### D C

| Host name | Sindhi | Provenance |
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

### D C++

| Host name | Sindhi | Provenance |
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

### D Java

| Host name | Sindhi | Provenance |
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

### D Python

| Host name | Sindhi | Provenance |
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

### D BASIC

| Host name | Sindhi | Provenance |
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

| Host name | Sindhi | Provenance |
|---|---|---|
| print | ڇاپيو | proposed |

## Annex E (informative) Conformance tests

The reference implementation is tested with the programs of samples/gate in the Hindawi repository, which cover the programming content of the GATE Computer Science paper. Recorded on 2026-10-18: 113 of 113 C programs, written in Sindhi, were lowered, compiled and run, and printed exactly what their English originals print; 1 of 1 Python programs did the same; 117 of 117 files were reversed byte for byte.

The program below, as written in the language, its transliterated form, and the C that the transducer gives:

### E source

```
#ضمن <stdio.h>
/* binary search in a sorted array */
صحيح ٻٽو_ڳولا(صحيح قدرون[], صحيح ڳڻپ, صحيح ڪنجي) {
  صحيح هيٺيون = 0, مٿاهون = ڳڻپ - 1;
  طالما (هيٺيون <= مٿاهون) {
    صحيح وچ = هيٺيون + (مٿاهون - هيٺيون) / 2;
    إذا (قدرون[وچ] == ڪنجي) أرجع وچ;
    إذا (قدرون[وچ] < ڪنجي) هيٺيون = وچ + 1; وإلا مٿاهون = وچ - 1;
  }
  أرجع -1;
}
صحيح مکيه(فراغ) {
  صحيح قدرون[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  لکو("%d %d\n", ٻٽو_ڳولا(قدرون, 10, 23), ٻٽو_ڳولا(قدرون, 10, 7));
  أرجع 0;
}
```

### E script filter

```
#ॹमन <stdio.h>
/* binary search in a sorted array */
स़ह़इह़ बटॉ_गॉला(स़ह़इह़ क़दरॉन[], स़ह़इह़ गनप, स़ह़इह़ कनजइ) {
  स़ह़इह़ हइٺयौन = 0, मथाहॉन = गनप - 1;
  त़ालमा (हइٺयौन <= मथाहॉन) {
    स़ह़इह़ वच = हइٺयौन + (मथाहॉन - हइٺयौन) / 2;
    आज़़ा (क़दरॉन[वच] == कनजइ) आरजए वच;
    आज़़ा (क़दरॉन[वच] < कनजइ) हइٺयौन = वच + 1; वआला मथाहॉन = वच - 1;
  }
  आरजए -1;
}
स़ह़इह़ मकइह(फ़राग़) {
  स़ह़इह़ क़दरॉन[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  लकॉ("%d %d\n", बटॉ_गॉला(क़दरॉन, 10, 23), बटॉ_गॉला(क़दरॉन, 10, 7));
  आरजए 0;
}
```

### E Romenagri

```
#_jzamana <stdio.h>
/* binary search in a sorted array */
sza_hza_i_hza batau_gaulaa(sza_hza_i_hza kza_darauna[], sza_hza_i_hza ganapa, sza_hza_i_hza kanaja_i) {
  sza_hza_i_hza _ha_izyouna = 0, ma_thaa_hauna = ganapa - 1;
  _tzaalamaa (_ha_izyouna <= ma_thaa_hauna) {
    sza_hza_i_hza wacha = _ha_izyouna + (ma_thaa_hauna - _ha_izyouna) / 2;
    _aajzzaa (kza_darauna[wacha] == kanaja_i) _aaraja_aee wacha;
    _aajzzaa (kza_darauna[wacha] < kanaja_i) _ha_izyouna = wacha + 1; wa_aalaa ma_thaa_hauna = wacha - 1;
  }
  _aaraja_aee -1;
}
sza_hza_i_hza maka_i_ha(phzaraagza) {
  sza_hza_i_hza kza_darauna[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  lakau("%d %d\n", batau_gaulaa(kza_darauna, 10, 23), batau_gaulaa(kza_darauna, 10, 7));
  _aaraja_aee 0;
}
```

### E C

```
#include <stdio.h>
/* binary search in a sorted array */
int batau_gaulaa(int kza_darauna[], int ganapa, int kanaja_i) {
  int _ha_izyouna = 0, ma_thaa_hauna = ganapa - 1;
  while (_ha_izyouna <= ma_thaa_hauna) {
    int wacha = _ha_izyouna + (ma_thaa_hauna - _ha_izyouna) / 2;
    if (kza_darauna[wacha] == kanaja_i) return wacha;
    if (kza_darauna[wacha] < kanaja_i) _ha_izyouna = wacha + 1; else ma_thaa_hauna = wacha - 1;
  }
  return -1;
}
int main(void) {
  int kza_darauna[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  printf("%d %d\n", batau_gaulaa(kza_darauna, 10, 23), batau_gaulaa(kza_darauna, 10, 7));
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

