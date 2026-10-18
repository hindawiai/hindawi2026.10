# HLS dari 2026.10

**Information technology, Programming languages, Dari keyword bindings for C, C++, Java, Python, BASIC and LOGO, and their lowering to the host language standards**

Edition 2026.10, draft proposal, 2026-10-18. © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

## Foreword

This draft is proposed by Abhishek Choudhary, AyeAI, for consideration by the Data Management System Sectional Committee, LITD 15, of the Bureau of Indian Standards, whose scope includes programming languages, their environments and system software interfaces. It is an indigenous draft: it adopts no International Standard, binds the language it names to the host programming language standards listed in Clause 2 by reference, and reproduces no text from them.

The method it standardizes was first published as the Hindawi Programming System on 15 August 2004, and has been developed since through the Hindawi releases. This draft is generated from the Dari cell of Hindawi 2026.10 by lang/hindawi/tools/standards.py, so that the document and its reference implementation cannot diverge; a revision of either is a revision of both.

Annexes A, B and C are normative. Annexes D, E and F are informative.

Every binding in Annex A records its provenance. A binding recorded as proposed has not yet been reviewed by the Dari language community; its review is part of the work towards an Indian Standard.

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. Hindawi™ and Romenagri™ are trademarks of Abhishek Choudhary. This document is an original work. It defines new programming languages by reference to the host language standards listed in Clause 2 and reproduces no text from them. Permission to adopt, translate or publish it as a standard is given by the copyright holder to a standards body on request.

## Introduction

A program has three properties that this draft keeps apart: the script it is written in, the human language its words come from, and the programming language standard that defines its meaning. The script is handled by transliteration, the language by the keyword bindings of Annex A, and the meaning by the host standard, which this draft does not alter.

A source text in the language is lowered to a source text of the host language and compiled by any conforming host translator. Native names reach the compiled program, and the debugger, in one fixed transliterated form, so that a program written in the language remains readable in that language at every level down to the machine.

## 1 Scope

This draft specifies, for programs written in Dari in the Arabic script:

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

3.3 native keyword: a word of Dari, written in the Arabic script, bound by Annex A to a host keyword.

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

The bindings of Annex A are maintained as a living register. A proposed binding becomes reviewed when the Dari language community accepts it; a change to a reviewed binding is a revision of this draft. The construct, not the host keyword, is primary: one native keyword serves one construct in every binding where that construct occurs.

## Annex A (normative) Keyword bindings

### A.1 C

Host standard: ISO/IEC 9899, Information technology, Programming languages, C. Names are lowered by name transformation.

| Host keyword | Dari | Provenance |
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
| long | دراز | proposed |
| register | سجل | lexicon |
| restrict | محدود | proposed |
| return | أرجع | lexicon |
| short | کوتاه | proposed |
| signed | علامتدار | proposed |
| sizeof | حجم | lexicon |
| static | ساكن | lexicon |
| struct | بنية | lexicon |
| switch | بدل | lexicon |
| typedef | تعريفنوع | lexicon |
| union | اتحاد | lexicon |
| unsigned | بیعلامت | proposed |
| void | فراغ | lexicon |
| volatile | متطاير | lexicon |
| while | طالما | lexicon |
| main | اصلی | proposed |

### A.2 C preprocessor

Host standard: ISO/IEC 9899, Information technology, Programming languages, C (preprocessing directives). Names are lowered by name transformation.

| Host keyword | Dari | Provenance |
|---|---|---|
| #define | #تعریف_کن | proposed |
| #include | #ضمن | lexicon |
| #if | #إذا | lexicon |
| #ifdef | #اگر_تعریف_شده | proposed |
| #ifndef | #اگر_تعریف_نشده | proposed |
| #else | #وإلا | lexicon |
| #elif | #وإلاإذا | lexicon |
| #endif | #پایان_اگر | proposed |
| #undef | #لغو_تعریف | proposed |
| #pragma | #رهنمود | proposed |
| #error | #خطا | proposed |
| #line | #سطر | proposed |

### A.3 C++

Host standard: ISO/IEC 14882, Programming languages, C++. Names are lowered by name transformation.

| Host keyword | Dari | Provenance |
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
| long | دراز | proposed |
| register | سجل | lexicon |
| restrict | محدود | proposed |
| return | أرجع | lexicon |
| short | کوتاه | proposed |
| signed | علامتدار | proposed |
| sizeof | حجم | lexicon |
| static | ساكن | lexicon |
| struct | بنية | lexicon |
| switch | بدل | lexicon |
| typedef | تعريفنوع | lexicon |
| union | اتحاد | lexicon |
| unsigned | بیعلامت | proposed |
| void | فراغ | lexicon |
| volatile | متطاير | lexicon |
| while | طالما | lexicon |
| main | اصلی | proposed |
| bool | منطقي | lexicon |
| catch | امسك | lexicon |
| class | صنف | lexicon |
| delete | حذف | proposed |
| explicit | صریح | proposed |
| false | خطأ | lexicon |
| friend | دوست | proposed |
| mutable | تغییرپذیر | proposed |
| namespace | نطاق | lexicon |
| new | جديد | lexicon |
| nullptr | اشاره_تهی | proposed |
| operator | عملگر | proposed |
| private | خاص | lexicon |
| protected | محمي | lexicon |
| public | عام | lexicon |
| template | قالب | proposed |
| this | هذا | lexicon |
| throw | ارم | lexicon |
| true | درست | proposed |
| try | حاول | lexicon |
| typename | نام_نوع | proposed |
| using | استفاده | proposed |
| virtual | مجازی | proposed |
| cout | خروجی | proposed |
| cin | ورودی | proposed |
| endl | پایان_سطر | proposed |

### A.4 Java

Host standard: The Java Language Specification, Oracle, current edition. Names are lowered by unchanged.

| Host keyword | Dari | Provenance |
|---|---|---|
| abstract | مجرد | lexicon |
| assert | أكد | lexicon |
| boolean | منطقی | proposed |
| break | اكسر | lexicon |
| byte | بایت | proposed |
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
| final | نهایی | proposed |
| finally | أخيرا | lexicon |
| float | عائم | lexicon |
| for | لكل | lexicon |
| if | إذا | lexicon |
| implements | ينفذ | lexicon |
| import | استورد | lexicon |
| instanceof | نمونه_از | proposed |
| int | صحيح | lexicon |
| interface | واجهة | lexicon |
| long | دراز | proposed |
| native | بومی | proposed |
| new | جديد | lexicon |
| package | حزمة | lexicon |
| private | خاص | lexicon |
| protected | محمي | lexicon |
| public | عام | lexicon |
| return | أرجع | lexicon |
| short | کوتاه | proposed |
| static | ساكن | lexicon |
| super | أعلى | lexicon |
| switch | بدل | lexicon |
| synchronized | همگام | proposed |
| this | هذا | lexicon |
| throw | ارم | lexicon |
| throws | پرتاب_میکند | proposed |
| try | حاول | lexicon |
| void | فراغ | lexicon |
| volatile | متطاير | lexicon |
| while | طالما | lexicon |
| true | درست | proposed |
| false | خطأ | lexicon |
| null | عدم | lexicon |
| String | نص | lexicon |
| System | سیستم | proposed |

### A.5 Python

Host standard: The Python Language Reference, Python Software Foundation, current version. Names are lowered by unchanged.

| Host keyword | Dari | Provenance |
|---|---|---|
| False | خطأ | lexicon |
| None | هیچ | proposed |
| True | درست | proposed |
| and | و | lexicon |
| as | كـ | lexicon |
| assert | أكد | lexicon |
| break | اكسر | lexicon |
| class | صنف | lexicon |
| continue | استمر | lexicon |
| def | تعریف | proposed |
| del | پاک | proposed |
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
| is | است | proposed |
| lambda | مجهول | lexicon |
| nonlocal | غیرمحلی | proposed |
| not | ليس | lexicon |
| or | أو | lexicon |
| pass | بگذر | proposed |
| raise | ارفع | lexicon |
| return | أرجع | lexicon |
| try | حاول | lexicon |
| while | طالما | lexicon |
| with | با | proposed |
| yield | أنتج | lexicon |
| print | چاپ | proposed |
| range | دامنه | proposed |
| len | طول | proposed |

### A.6 BASIC

Host standard: ISO/IEC 10279, Information technology, Programming languages, Full BASIC. Names are lowered by name transformation.

| Host keyword | Dari | Provenance |
|---|---|---|
| dim | ابعاد | proposed |
| end | انته | lexicon |
| for | لكل | lexicon |
| gosub | برو_زیربرنامه | proposed |
| goto | اذهب | lexicon |
| if | إذا | lexicon |
| input | بگیر | proposed |
| let | ليكن | lexicon |
| next | بعدی_دور | proposed |
| print | چاپ | proposed |
| rem | توضیح | proposed |
| return | أرجع | lexicon |
| step | گام_به | proposed |
| then | آنگاه | proposed |
| to | تا | proposed |
| wend | پایان_مادامی | proposed |
| while | طالما | lexicon |
| and | و | lexicon |
| or | أو | lexicon |
| not | ليس | lexicon |
| mod | باقیمانده | proposed |

### A.7 LOGO

Host standard: No international standard; the host is the Berkeley Logo dialect (bibliography). Names are lowered by name transformation.

| Host keyword | Dari | Provenance |
|---|---|---|
| forward | أمامي | lexicon |
| back | عقب | proposed |
| left | چپ | proposed |
| right | راست | proposed |
| penup | قلم_بالا | proposed |
| pendown | قلم_پایین | proposed |
| repeat | تکرار | proposed |
| to | تا | proposed |
| end | انته | lexicon |
| make | بساز | proposed |
| if | إذا | lexicon |
| ifelse | اگر_وگرنه | proposed |
| home | خانه | proposed |
| clearscreen | پاک_صفحه | proposed |

## Annex B (normative) Name transformation test vectors

Each native name shall be given the C-level form shown. The vectors are computed by the reference implementation when this draft is generated.

| Native name | C-level form |
|---|---|
| آخرین | _aakhzareena |
| آدرس | _aa_darasa |
| آدرسها | _aa_darasa_haa |
| آرگومان | _aaragaumaana |
| آرگومانها | _aaragaumaana_haa |
| آستانه | _aasa_taana_ha |
| آیا_گروه | _aayaa_garau_ha |
| ادغام | _i_dagzaama |
| ادغام_مرتب_سازی | _i_dagzaama_mara_taba_saajzee |
| ارتفاع | _ira_taphzaa_aee |
| ارسال | _irasaala |
| از_طریق | _ijza__tzareekza |
| استخراج | _isa_takhzaraaja |
| استفاده_شده | _isa_taphzaa_da_ha_sha_da_ha |
| استفاده_میکند | _isa_taphzaa_da_ha_meekana_da |
| استفاده_میکند_قبلی | _isa_taphzaa_da_ha_meekana_da_kzabalee |
| استفادهنشده | _isa_taphzaa_da_hanasha_da_ha |
| اشاره_گر | _ishaara_ha_gara |
| اشارهگرها | _ishaara_hagara_haa |
| اصابت | _iszaaba_ta |
| اصابتها | _iszaaba_ta_haa |
| اضطراری | _i_jza_tzaraaree |
| افراز | _iphzaraajza |
| افزودن_به_صف | _iphzajzau_dana_ba_ha_szaphza |
| اقلام | _ikzalaama |
| الگو | _ilagau |
| امن | _imana |
| انباشته | _inabaasha_ta_ha |
| انباشتگر | _inabaasha_tagara |
| انتخاب | _ina_takhzaaba |

## Annex C (normative) Script filter

The Arabic script is mapped to Devanagari by the filter of the Hindawi tools for this script (fltr_ur_hi), unchanged since its publication in Chintamani.

Letters of the Perso-Arabic orthographies that the filter does not distinguish are first folded to the nearest Urdu letter: ٻ to ب, ټ to ٹ, ٽ to ٹ, ٿ to تھ, ڀ to بھ, ځ to ز, ڄ to ج, څ to س, ڇ to چھ, ډ to ڈ, ڊ to ڈ, ڌ to دھ, ڍ to ڈھ, ڏ to د, ړ to ڑ, ږ to ژ, ڙ to ڑ, ښ to ش, ڦ to پھ, ڪ to ک, ګ to گ, ڱ to نگ, ڳ to گ, ڻ to ن, ڼ to ن, ۀ to ہ, ۍ to ی, ې to ی.

## Annex D (informative) Library names

### D C

| Host name | Dari | Provenance |
|---|---|---|
| INT_MAX | بیشترین_صحیح | proposed |
| NULL | عدم | lexicon |
| abs | قدر_مطلق | proposed |
| assert | أكد | lexicon |
| calloc | حافظه_صفر_بده | proposed |
| cos | کسینوس | proposed |
| exit | خروج | proposed |
| exp | نمایی_تابع | proposed |
| free | حرر | lexicon |
| friend | دوست | proposed |
| isalnum | آیا_حرف_یا_رقم | proposed |
| isalpha | آیا_حرف | proposed |
| isdigit | آیا_رقم | proposed |
| isspace | آیا_فاصله | proposed |
| log | لگاریتم | proposed |
| malloc | حافظه_بده | proposed |
| memcpy | کپی_حافظه | proposed |
| operator | عملگر | proposed |
| pow | توان | proposed |
| printf | چاپ_کن | proposed |
| private | خاص | lexicon |
| protected | محمي | lexicon |
| public | عام | lexicon |
| putchar | حرف_چاپ_کن | proposed |
| raise | ارفع | lexicon |
| read | اقرأ | lexicon |
| signal | إشارة | lexicon |
| sin | سینوس | proposed |
| sqrt | جذر | proposed |
| sscanf | از_رشته_بخوان | proposed |
| strlen | طول_رشته | proposed |
| strncmp | مقایسه_رشته | proposed |
| strstr | جستجوی_رشته | proposed |
| template | قالب | proposed |
| toupper | به_بزرگ | proposed |
| virtual | مجازی | proposed |
| write | اكتب | lexicon |

### D C++

| Host name | Dari | Provenance |
|---|---|---|
| INT_MAX | بیشترین_صحیح | proposed |
| NULL | عدم | lexicon |
| abs | قدر_مطلق | proposed |
| assert | أكد | lexicon |
| calloc | حافظه_صفر_بده | proposed |
| cos | کسینوس | proposed |
| exit | خروج | proposed |
| exp | نمایی_تابع | proposed |
| free | حرر | lexicon |
| isalnum | آیا_حرف_یا_رقم | proposed |
| isalpha | آیا_حرف | proposed |
| isdigit | آیا_رقم | proposed |
| isspace | آیا_فاصله | proposed |
| left | چپ | proposed |
| log | لگاریتم | proposed |
| malloc | حافظه_بده | proposed |
| memcpy | کپی_حافظه | proposed |
| pipe | أنبوب | lexicon |
| pow | توان | proposed |
| printf | چاپ_کن | proposed |
| putchar | حرف_چاپ_کن | proposed |
| raise | ارفع | lexicon |
| read | اقرأ | lexicon |
| right | راست | proposed |
| signal | إشارة | lexicon |
| sin | سینوس | proposed |
| sleep | نوم | lexicon |
| sqrt | جذر | proposed |
| sscanf | از_رشته_بخوان | proposed |
| strlen | طول_رشته | proposed |
| strncmp | مقایسه_رشته | proposed |
| strstr | جستجوی_رشته | proposed |
| sync | متزامن | lexicon |
| toupper | به_بزرگ | proposed |
| write | اكتب | lexicon |

### D Java

| Host name | Dari | Provenance |
|---|---|---|
| INT_MAX | بیشترین_صحیح | proposed |
| Object | كائن | lexicon |
| Thread | خيط | lexicon |
| abs | قدر_مطلق | proposed |
| auto | خودکار | proposed |
| calloc | حافظه_صفر_بده | proposed |
| const | ثابت | lexicon |
| cos | کسینوس | proposed |
| exit | خروج | proposed |
| exp | نمایی_تابع | proposed |
| extern | خارجي | lexicon |
| free | حرر | lexicon |
| friend | دوست | proposed |
| goto | اذهب | lexicon |
| inline | مضمن | lexicon |
| isalnum | آیا_حرف_یا_رقم | proposed |
| isalpha | آیا_حرف | proposed |
| isdigit | آیا_رقم | proposed |
| isspace | آیا_فاصله | proposed |
| log | لگاریتم | proposed |
| main | اصلی | proposed |
| malloc | حافظه_بده | proposed |
| memcpy | کپی_حافظه | proposed |
| operator | عملگر | proposed |
| pow | توان | proposed |
| printf | چاپ_کن | proposed |
| println | چاپ_سطر | proposed |
| putchar | حرف_چاپ_کن | proposed |
| raise | ارفع | lexicon |
| read | اقرأ | lexicon |
| register | سجل | lexicon |
| restrict | محدود | proposed |
| signal | إشارة | lexicon |
| signed | علامتدار | proposed |
| sin | سینوس | proposed |
| sizeof | حجم | lexicon |
| sleep | نوم | lexicon |
| sqrt | جذر | proposed |
| sscanf | از_رشته_بخوان | proposed |
| strlen | طول_رشته | proposed |
| strncmp | مقایسه_رشته | proposed |
| strstr | جستجوی_رشته | proposed |
| struct | بنية | lexicon |
| template | قالب | proposed |
| toupper | به_بزرگ | proposed |
| typedef | تعريفنوع | lexicon |
| union | اتحاد | lexicon |
| unsigned | بیعلامت | proposed |
| virtual | مجازی | proposed |
| write | اكتب | lexicon |

### D Python

| Host name | Dari | Provenance |
|---|---|---|
| Object | كائن | lexicon |
| String | نص | lexicon |
| System | سیستم | proposed |
| Thread | خيط | lexicon |
| abstract | مجرد | lexicon |
| boolean | منطقی | proposed |
| byte | بایت | proposed |
| case | حالة | lexicon |
| catch | امسك | lexicon |
| char | حرف | lexicon |
| const | ثابت | lexicon |
| default | افتراضي | lexicon |
| do | افعل | lexicon |
| double | مزدوج | lexicon |
| extends | يمتد | lexicon |
| final | نهایی | proposed |
| float | عائم | lexicon |
| goto | اذهب | lexicon |
| implements | ينفذ | lexicon |
| instanceof | نمونه_از | proposed |
| int | صحيح | lexicon |
| interface | واجهة | lexicon |
| long | دراز | proposed |
| main | اصلی | proposed |
| native | بومی | proposed |
| new | جديد | lexicon |
| package | حزمة | lexicon |
| println | چاپ_سطر | proposed |
| private | خاص | lexicon |
| protected | محمي | lexicon |
| read | اقرأ | lexicon |
| short | کوتاه | proposed |
| sleep | نوم | lexicon |
| sqrt | جذر | proposed |
| static | ساكن | lexicon |
| super | أعلى | lexicon |
| switch | بدل | lexicon |
| this | هذا | lexicon |
| throw | ارم | lexicon |
| throws | پرتاب_میکند | proposed |
| void | فراغ | lexicon |
| volatile | متطاير | lexicon |
| write | اكتب | lexicon |

### D BASIC

| Host name | Dari | Provenance |
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

| Host name | Dari | Provenance |
|---|---|---|
| print | چاپ | proposed |

## Annex E (informative) Conformance tests

The reference implementation is tested with the programs of samples/gate in the Hindawi repository, which cover the programming content of the GATE Computer Science paper. Recorded on 2026-10-18: 113 of 113 C programs, written in Dari, were lowered, compiled and run, and printed exactly what their English originals print; 1 of 1 Python programs did the same; 117 of 117 files were reversed byte for byte.

The program below, as written in the language, its transliterated form, and the C that the transducer gives:

### E source

```
#ضمن <stdio.h>
/* binary search in a sorted array */
صحيح دودویی_جستجو(صحيح مقادیر[], صحيح شمار, صحيح کلید) {
  صحيح کم = 0, بالا = شمار - 1;
  طالما (کم <= بالا) {
    صحيح میانه = کم + (بالا - کم) / 2;
    إذا (مقادیر[میانه] == کلید) أرجع میانه;
    إذا (مقادیر[میانه] < کلید) کم = میانه + 1; وإلا بالا = میانه - 1;
  }
  أرجع -1;
}
صحيح اصلی(فراغ) {
  صحيح مقادیر[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  چاپ_کن("%d %d\n", دودویی_جستجو(مقادیر, 10, 23), دودویی_جستجو(مقادیر, 10, 7));
  أرجع 0;
}
```

### E script filter

```
#ॹमन <stdio.h>
/* binary search in a sorted array */
स़ह़इह़ दॉदवीी_जसतजॉ(स़ह़इह़ मक़ादीर[], स़ह़इह़ शमार, स़ह़इह़ कलीद) {
  स़ह़इह़ कम = 0, बाला = शमार - 1;
  त़ालमा (कम <= बाला) {
    स़ह़इह़ मयानह = कम + (बाला - कम) / 2;
    आज़़ा (मक़ादीर[मयानह] == कलीद) आरजए मयानह;
    आज़़ा (मक़ादीर[मयानह] < कलीद) कम = मयानह + 1; वआला बाला = मयानह - 1;
  }
  आरजए -1;
}
स़ह़इह़ इस़ली(फ़राग़) {
  स़ह़इह़ मक़ादीर[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  चाप_कन("%d %d\n", दॉदवीी_जसतजॉ(मक़ादीर, 10, 23), दॉदवीी_जसतजॉ(मक़ादीर, 10, 7));
  आरजए 0;
}
```

### E Romenagri

```
#_jzamana <stdio.h>
/* binary search in a sorted array */
sza_hza_i_hza _dau_daweee_jasa_tajau(sza_hza_i_hza makzaa_deera[], sza_hza_i_hza shamaara, sza_hza_i_hza kalee_da) {
  sza_hza_i_hza kama = 0, baalaa = shamaara - 1;
  _tzaalamaa (kama <= baalaa) {
    sza_hza_i_hza mayaana_ha = kama + (baalaa - kama) / 2;
    _aajzzaa (makzaa_deera[mayaana_ha] == kalee_da) _aaraja_aee mayaana_ha;
    _aajzzaa (makzaa_deera[mayaana_ha] < kalee_da) kama = mayaana_ha + 1; wa_aalaa baalaa = mayaana_ha - 1;
  }
  _aaraja_aee -1;
}
sza_hza_i_hza _iszalee(phzaraagza) {
  sza_hza_i_hza makzaa_deera[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  chaapa_kana("%d %d\n", _dau_daweee_jasa_tajau(makzaa_deera, 10, 23), _dau_daweee_jasa_tajau(makzaa_deera, 10, 7));
  _aaraja_aee 0;
}
```

### E C

```
#include <stdio.h>
/* binary search in a sorted array */
int _dau_daweee_jasa_tajau(int makzaa_deera[], int shamaara, int kalee_da) {
  int kama = 0, baalaa = shamaara - 1;
  while (kama <= baalaa) {
    int mayaana_ha = kama + (baalaa - kama) / 2;
    if (makzaa_deera[mayaana_ha] == kalee_da) return mayaana_ha;
    if (makzaa_deera[mayaana_ha] < kalee_da) kama = mayaana_ha + 1; else baalaa = mayaana_ha - 1;
  }
  return -1;
}
int main(void) {
  int makzaa_deera[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  printf("%d %d\n", _dau_daweee_jasa_tajau(makzaa_deera, 10, 23), _dau_daweee_jasa_tajau(makzaa_deera, 10, 7));
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

