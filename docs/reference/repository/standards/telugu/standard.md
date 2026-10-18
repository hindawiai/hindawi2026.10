# HLS te 2026.10

**Information technology, Programming languages, Telugu keyword bindings for C, C++, Java, Python, BASIC and LOGO, and their lowering to the host language standards**

Edition 2026.10, draft proposal, 2026-10-18. © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

## Foreword

This draft is proposed by Abhishek Choudhary, AyeAI, for consideration by the Data Management System Sectional Committee, LITD 15, of the Bureau of Indian Standards, whose scope includes programming languages, their environments and system software interfaces. It is an indigenous draft: it adopts no International Standard, binds the language it names to the host programming language standards listed in Clause 2 by reference, and reproduces no text from them.

The method it standardizes was first published as the Hindawi Programming System on 15 August 2004, and has been developed since through the Hindawi releases. This draft is generated from the Telugu cell of Hindawi 2026.10 by lang/hindawi/tools/standards.py, so that the document and its reference implementation cannot diverge; a revision of either is a revision of both.

Annexes A, B and C are normative. Annexes D, E and F are informative.

Every binding in Annex A records its provenance. A binding recorded as proposed has not yet been reviewed by the Telugu language community; its review is part of the work towards an Indian Standard.

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. Hindawi™ and Romenagri™ are trademarks of Abhishek Choudhary. This document is an original work. It defines new programming languages by reference to the host language standards listed in Clause 2 and reproduces no text from them. Permission to adopt, translate or publish it as a standard is given by the copyright holder to a standards body on request.

## Introduction

A program has three properties that this draft keeps apart: the script it is written in, the human language its words come from, and the programming language standard that defines its meaning. The script is handled by transliteration, the language by the keyword bindings of Annex A, and the meaning by the host standard, which this draft does not alter.

A source text in the language is lowered to a source text of the host language and compiled by any conforming host translator. Native names reach the compiled program, and the debugger, in one fixed transliterated form, so that a program written in the language remains readable in that language at every level down to the machine.

## 1 Scope

This draft specifies, for programs written in Telugu in the Telugu script:

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

3.3 native keyword: a word of Telugu, written in the Telugu script, bound by Annex A to a host keyword.

3.4 binding: the pairing of one host keyword with one native keyword, for one host language.

3.5 construct: the programming construct a keyword denotes, which is the same across host languages, so that one native keyword serves it in every binding.

3.6 source text: a program, or part of one, written using native keywords, native names, or both.

3.7 native name: an identifier of a source text written wholly or partly in the Telugu script.

3.8 lowering: the transformation of a source text into a source text of the host language.

3.9 C-level form: the identifier of the host language that a native name becomes by name transformation, and under which it appears in compiled programs and to debuggers.

3.10 name transformation: the mapping of native names to C-level forms specified in Clause 9.

3.11 script filter: the mapping of the Telugu script to Devanagari that precedes transliteration, specified in Annex C.

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

6.2 Native letters are the characters of the Telugu block of ISO/IEC 10646 whose general category is a letter or a mark. Text written right to left is stored in logical order.

6.3 The Telugu script is written left to right.

6.4 The native digits below are equivalent, in numerals, to the decimal digits of the host language with the same value. A translator shall accept either.

| Code point | Digit | Value |
|---|---|---|
| U+0C66 | ౦ | 0 |
| U+0C67 | ౧ | 1 |
| U+0C68 | ౨ | 2 |
| U+0C69 | ౩ | 3 |
| U+0C6A | ౪ | 4 |
| U+0C6B | ౫ | 5 |
| U+0C6C | ౬ | 6 |
| U+0C6D | ౭ | 7 |
| U+0C6E | ౮ | 8 |
| U+0C6F | ౯ | 9 |

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

The bindings of Annex A are maintained as a living register. A proposed binding becomes reviewed when the Telugu language community accepts it; a change to a reviewed binding is a revision of this draft. The construct, not the host keyword, is primary: one native keyword serves one construct in every binding where that construct occurs.

## Annex A (normative) Keyword bindings

### A.1 C

Host standard: ISO/IEC 9899, Information technology, Programming languages, C. Names are lowered by name transformation.

| Host keyword | Telugu | Provenance |
|---|---|---|
| auto | స్వయంచాలక | proposed |
| break | ఆపు | lexicon |
| case | స్థితి | lexicon |
| char | అక్షరం | lexicon |
| const | స్థిరరాశి | lexicon |
| continue | కొనసాగు | lexicon |
| default | అప్రమేయ | lexicon |
| do | చేయి | lexicon |
| double | ద్విగుణ | lexicon |
| else | లేకపోతే | lexicon |
| enum | గణన | lexicon |
| extern | బాహ్య | lexicon |
| float | దశాంశం | lexicon |
| for | కొరకు | lexicon |
| goto | వెళ్ళు | lexicon |
| if | ఒకవేళ | lexicon |
| inline | అంతఃవరుస | lexicon |
| int | పూర్ణాంకం | lexicon |
| long | దీర్ఘ | proposed |
| register | నమోదు | lexicon |
| restrict | పరిమిత | proposed |
| return | తిరిగి | lexicon |
| short | పొట్టి | proposed |
| signed | గుర్తుగల | proposed |
| sizeof | పరిమాణం | lexicon |
| static | స్థిర | lexicon |
| struct | నిర్మాణం | lexicon |
| switch | ఎంపిక | lexicon |
| typedef | రకనిర్వచనం | lexicon |
| union | సంఘం | lexicon |
| unsigned | గుర్తులేని | proposed |
| void | శూన్య | lexicon |
| volatile | అస్థిర | lexicon |
| while | అయితే | lexicon |
| main | ప్రధాన | lexicon |

### A.2 C preprocessor

Host standard: ISO/IEC 9899, Information technology, Programming languages, C (preprocessing directives). Names are lowered by name transformation.

| Host keyword | Telugu | Provenance |
|---|---|---|
| #define | #నిర్వచించు | proposed |
| #include | #అన్తర్భావ | lexicon |
| #if | #ఒకవేళ | lexicon |
| #ifdef | #నిర్వచితమైతే | proposed |
| #ifndef | #నిర్వచితం_కాకపోతే | proposed |
| #else | #లేకపోతే | lexicon |
| #elif | #లేదావేళ | lexicon |
| #endif | #అయితే_ముగింపు | proposed |
| #undef | #నిర్వచనం_రద్దు | proposed |
| #pragma | #సూచన | proposed |
| #error | #దోషం | proposed |
| #line | #పంక్తి | proposed |

### A.3 C++

Host standard: ISO/IEC 14882, Programming languages, C++. Names are lowered by name transformation.

| Host keyword | Telugu | Provenance |
|---|---|---|
| auto | స్వయంచాలక | proposed |
| break | ఆపు | lexicon |
| case | స్థితి | lexicon |
| char | అక్షరం | lexicon |
| const | స్థిరరాశి | lexicon |
| continue | కొనసాగు | lexicon |
| default | అప్రమేయ | lexicon |
| do | చేయి | lexicon |
| double | ద్విగుణ | lexicon |
| else | లేకపోతే | lexicon |
| enum | గణన | lexicon |
| extern | బాహ్య | lexicon |
| float | దశాంశం | lexicon |
| for | కొరకు | lexicon |
| goto | వెళ్ళు | lexicon |
| if | ఒకవేళ | lexicon |
| inline | అంతఃవరుస | lexicon |
| int | పూర్ణాంకం | lexicon |
| long | దీర్ఘ | proposed |
| register | నమోదు | lexicon |
| restrict | పరిమిత | proposed |
| return | తిరిగి | lexicon |
| short | పొట్టి | proposed |
| signed | గుర్తుగల | proposed |
| sizeof | పరిమాణం | lexicon |
| static | స్థిర | lexicon |
| struct | నిర్మాణం | lexicon |
| switch | ఎంపిక | lexicon |
| typedef | రకనిర్వచనం | lexicon |
| union | సంఘం | lexicon |
| unsigned | గుర్తులేని | proposed |
| void | శూన్య | lexicon |
| volatile | అస్థిర | lexicon |
| while | అయితే | lexicon |
| main | ప్రధాన | lexicon |
| bool | తార్కిక | lexicon |
| catch | పట్టుకో | lexicon |
| class | తరగతి | lexicon |
| delete | తొలగించు | proposed |
| explicit | స్పష్టమైన | proposed |
| false | అబద్ధం | lexicon |
| friend | మిత్ర | proposed |
| mutable | మార్చదగిన | proposed |
| namespace | నామాకాశ | lexicon |
| new | కొత్త | lexicon |
| nullptr | శూన్యసూచిక | proposed |
| operator | క్రియాకారకం | proposed |
| private | అంతరంగ | lexicon |
| protected | రక్షిత | lexicon |
| public | బహిరంగ | lexicon |
| template | మూస | proposed |
| this | ఇది | lexicon |
| throw | విసురు | lexicon |
| true | నిజం | lexicon |
| try | ప్రయత్నించు | lexicon |
| typename | రకం_పేరు | proposed |
| using | ఉపయోగించి | proposed |
| virtual | మాయా | lexicon |
| cout | బయటకు | proposed |
| cin | లోపలికి | proposed |
| endl | పంక్తి_ముగింపు | proposed |

### A.4 Java

Host standard: The Java Language Specification, Oracle, current edition. Names are lowered by unchanged.

| Host keyword | Telugu | Provenance |
|---|---|---|
| abstract | నైరూప్య | lexicon |
| assert | ప్రతిజ్ఞా | lexicon |
| boolean | తార్కిక | proposed |
| break | ఆపు | lexicon |
| byte | బైటు | proposed |
| case | స్థితి | lexicon |
| catch | పట్టుకో | lexicon |
| char | అక్షరం | lexicon |
| class | తరగతి | lexicon |
| continue | కొనసాగు | lexicon |
| default | అప్రమేయ | lexicon |
| do | చేయి | lexicon |
| double | ద్విగుణ | lexicon |
| else | లేకపోతే | lexicon |
| enum | గణన | lexicon |
| extends | విస్తరించు | lexicon |
| final | తుది | proposed |
| finally | చివరగా | lexicon |
| float | దశాంశం | lexicon |
| for | కొరకు | lexicon |
| if | ఒకవేళ | lexicon |
| implements | అమలుచేయు | lexicon |
| import | దిగుమతి | lexicon |
| instanceof | నమూనా_ఔనా | proposed |
| int | పూర్ణాంకం | lexicon |
| interface | అంతరముఖం | lexicon |
| long | దీర్ఘ | proposed |
| native | స్థానిక | proposed |
| new | కొత్త | lexicon |
| package | సంచి | lexicon |
| private | అంతరంగ | lexicon |
| protected | రక్షిత | lexicon |
| public | బహిరంగ | lexicon |
| return | తిరిగి | lexicon |
| short | పొట్టి | proposed |
| static | స్థిర | lexicon |
| super | పర | lexicon |
| switch | ఎంపిక | lexicon |
| synchronized | సమకాలిక | proposed |
| this | ఇది | lexicon |
| throw | విసురు | lexicon |
| throws | విసురుతుంది | proposed |
| try | ప్రయత్నించు | lexicon |
| void | శూన్య | lexicon |
| volatile | అస్థిర | lexicon |
| while | అయితే | lexicon |
| true | నిజం | lexicon |
| false | అబద్ధం | lexicon |
| null | ఖాళీ | lexicon |
| String | పదబంధం | lexicon |
| System | వ్యవస్థ | proposed |

### A.5 Python

Host standard: The Python Language Reference, Python Software Foundation, current version. Names are lowered by unchanged.

| Host keyword | Telugu | Provenance |
|---|---|---|
| False | అబద్ధం | lexicon |
| None | ఏమీలేదు | proposed |
| True | నిజం | lexicon |
| and | మరియు | lexicon |
| as | ఇవ | lexicon |
| assert | ప్రతిజ్ఞా | lexicon |
| break | ఆపు | lexicon |
| class | తరగతి | lexicon |
| continue | కొనసాగు | lexicon |
| def | నిర్వచనం | proposed |
| del | తీసివేయి | proposed |
| elif | లేదావేళ | lexicon |
| else | లేకపోతే | lexicon |
| except | మినహాయింపు | lexicon |
| finally | చివరగా | lexicon |
| for | కొరకు | lexicon |
| from | తః | lexicon |
| global | వైశ్విక | lexicon |
| if | ఒకవేళ | lexicon |
| import | దిగుమతి | lexicon |
| in | లో | lexicon |
| is | అయిన | proposed |
| lambda | అజ్ఞాత | lexicon |
| nonlocal | స్థానికేతర | proposed |
| not | కాదు | lexicon |
| or | లేదా | lexicon |
| pass | దాటు | proposed |
| raise | లేపు | lexicon |
| return | తిరిగి | lexicon |
| try | ప్రయత్నించు | lexicon |
| while | అయితే | lexicon |
| with | తోడుగా | proposed |
| yield | ఇవ్వు | lexicon |
| print | ముద్రించు | proposed |
| range | శ్రేణి | proposed |
| len | పొడవు | proposed |

### A.6 BASIC

Host standard: ISO/IEC 10279, Information technology, Programming languages, Full BASIC. Names are lowered by name transformation.

| Host keyword | Telugu | Provenance |
|---|---|---|
| dim | పరిమాణం | proposed |
| end | ముగింపు | lexicon |
| for | కొరకు | lexicon |
| gosub | ఉప_వెళ్ళు | proposed |
| goto | వెళ్ళు | lexicon |
| if | ఒకవేళ | lexicon |
| input | తీసుకో | proposed |
| let | అనుకో | lexicon |
| next | తదుపరి_చక్రం | proposed |
| print | ముద్రించు | proposed |
| rem | వ్యాఖ్య | proposed |
| return | తిరిగి | lexicon |
| step | అడుగుతో | proposed |
| then | అప్పుడు | proposed |
| to | వరకు | proposed |
| wend | అంతవరకు_ముగింపు | proposed |
| while | అయితే | lexicon |
| and | మరియు | lexicon |
| or | లేదా | lexicon |
| not | కాదు | lexicon |
| mod | శేషం | proposed |

### A.7 LOGO

Host standard: No international standard; the host is the Berkeley Logo dialect (bibliography). Names are lowered by name transformation.

| Host keyword | Telugu | Provenance |
|---|---|---|
| forward | అగ్రప్రసార | lexicon |
| back | వెనుకకు | proposed |
| left | ఎడమ | proposed |
| right | కుడి | proposed |
| penup | కలం_ఎత్తు | proposed |
| pendown | కలం_దించు | proposed |
| repeat | పునరావృతం | proposed |
| to | వరకు | proposed |
| end | ముగింపు | lexicon |
| make | చేయి | proposed |
| if | ఒకవేళ | lexicon |
| ifelse | అయితే_లేకపోతే | proposed |
| home | ఇల్లు | proposed |
| clearscreen | తెర_శుభ్రం | proposed |

## Annex B (normative) Name transformation test vectors

Each native name shall be given the C-level form shown. The vectors are computed by the reference implementation when this draft is generated.

| Native name | C-level form |
|---|---|
| అంచు | _a_mchu |
| అంచులు | _a_mchulu |
| అంతరాయం_చక్రాలు | _a_m_taraaya_m_chakraalu |
| అంతర్గత | _a_m_targa_ta |
| అందుబాటు | _a_m_dubaatu |
| అంశం | _a_msha_m |
| అంశాలు | _a_mshaalu |
| అక్షరశ్రేణులు | _akxarashraee_nnulu |
| అడుగు | _adugu |
| అడుగులు | _adugulu |
| అడ్డువరుస | _adduwarusa |
| అడ్డువరుసలు | _adduwarusalu |
| అతిచిన్న | _a_tichinna |
| అతితక్కువ | _a_ti_takkuwa |
| అతిపెద్ద | _a_tipae_d_da |
| అత్యంతలోతు | _a_tya_m_taloa_tu |
| అత్యల్ప | _a_tyalpa |
| అత్యవసర | _a_tyawasara |
| అదనపు | _a_danapu |
| అధికప్రవాహం | _a_dhikaprawaa_ha_m |
| అభ్యర్థనలు | _abhyar_thanalu |
| ఆకు | _aaku |
| ఆధారం | _aa_dhaara_m |
| ఇరుసు | _irusu |
| ఉంచు | _u_mchu |
| ఉత్తమ | _u_t_tama |
| ఉత్తమ_విభాగిత | _u_t_tama_wibhaagi_ta |
| ఉత్తమ_శుద్ధ | _u_t_tama_shu_d_dha |
| ఉత్పాదకుడు | _u_tpaa_dakudu |
| ఉపయోగిస్తుంది | _upayoagis_tu_m_di |

## Annex C (normative) Script filter

The Telugu script is mapped to Devanagari by the filter of the Hindawi tools for this script (fltr_te_hi), unchanged since its publication in Chintamani.

## Annex D (informative) Library names

### D C

| Host name | Telugu | Provenance |
|---|---|---|
| INT_MAX | గరిష్ఠ_పూర్ణాంకం | proposed |
| NULL | ఖాళీ | lexicon |
| abs | నిరపేక్ష | proposed |
| assert | ప్రతిజ్ఞా | lexicon |
| calloc | సున్నా_జ్ఞాపకం_ఇవ్వు | proposed |
| cos | కోజ్యా | proposed |
| exit | నిష్క్రమించు | proposed |
| exp | ఘాతాంకం | proposed |
| free | విడుదల | lexicon |
| friend | మిత్ర | proposed |
| isalnum | అక్షరమా_అంకెనా | proposed |
| isalpha | అక్షరమా | proposed |
| isdigit | అంకెనా | proposed |
| isspace | ఖాళీనా | proposed |
| log | సంవర్గమానం | proposed |
| malloc | జ్ఞాపకం_ఇవ్వు | proposed |
| memcpy | జ్ఞాపకం_నకలు | proposed |
| operator | క్రియాకారకం | proposed |
| pow | ఘాతం | proposed |
| printf | రాయి | proposed |
| private | అంతరంగ | lexicon |
| protected | రక్షిత | lexicon |
| public | బహిరంగ | lexicon |
| putchar | అక్షరం_రాయి | proposed |
| raise | లేపు | lexicon |
| read | పఠ | lexicon |
| signal | సంకేతం | lexicon |
| sin | జ్యా | proposed |
| sqrt | వర్గమూలం | proposed |
| sscanf | అక్షరశ్రేణి_చదువు | proposed |
| strlen | అక్షరశ్రేణి_పొడవు | proposed |
| strncmp | అక్షరశ్రేణి_పోలిక | proposed |
| strstr | అక్షరశ్రేణి_శోధన | proposed |
| template | మూస | proposed |
| toupper | పెద్ద_అక్షరం | proposed |
| virtual | మాయా | lexicon |
| write | లిఖ | lexicon |

### D C++

| Host name | Telugu | Provenance |
|---|---|---|
| INT_MAX | గరిష్ఠ_పూర్ణాంకం | proposed |
| NULL | ఖాళీ | lexicon |
| abs | నిరపేక్ష | proposed |
| assert | ప్రతిజ్ఞా | lexicon |
| calloc | సున్నా_జ్ఞాపకం_ఇవ్వు | proposed |
| cos | కోజ్యా | proposed |
| exit | నిష్క్రమించు | proposed |
| exp | ఘాతాంకం | proposed |
| free | విడుదల | lexicon |
| isalnum | అక్షరమా_అంకెనా | proposed |
| isalpha | అక్షరమా | proposed |
| isdigit | అంకెనా | proposed |
| isspace | ఖాళీనా | proposed |
| left | ఎడమ | proposed |
| log | సంవర్గమానం | proposed |
| malloc | జ్ఞాపకం_ఇవ్వు | proposed |
| memcpy | జ్ఞాపకం_నకలు | proposed |
| pipe | ప్రణాల | lexicon |
| pow | ఘాతం | proposed |
| printf | రాయి | proposed |
| putchar | అక్షరం_రాయి | proposed |
| raise | లేపు | lexicon |
| read | పఠ | lexicon |
| right | కుడి | proposed |
| signal | సంకేతం | lexicon |
| sin | జ్యా | proposed |
| sleep | సుషుప్తి | lexicon |
| sqrt | వర్గమూలం | proposed |
| sscanf | అక్షరశ్రేణి_చదువు | proposed |
| strlen | అక్షరశ్రేణి_పొడవు | proposed |
| strncmp | అక్షరశ్రేణి_పోలిక | proposed |
| strstr | అక్షరశ్రేణి_శోధన | proposed |
| sync | సమకాలీకరణ | lexicon |
| toupper | పెద్ద_అక్షరం | proposed |
| write | లిఖ | lexicon |

### D Java

| Host name | Telugu | Provenance |
|---|---|---|
| INT_MAX | గరిష్ఠ_పూర్ణాంకం | proposed |
| Object | వస్తువు | lexicon |
| Thread | తంతువు | lexicon |
| abs | నిరపేక్ష | proposed |
| auto | స్వయంచాలక | proposed |
| calloc | సున్నా_జ్ఞాపకం_ఇవ్వు | proposed |
| const | స్థిరరాశి | lexicon |
| cos | కోజ్యా | proposed |
| exit | నిష్క్రమించు | proposed |
| exp | ఘాతాంకం | proposed |
| extern | బాహ్య | lexicon |
| free | విడుదల | lexicon |
| friend | మిత్ర | proposed |
| goto | వెళ్ళు | lexicon |
| inline | అంతఃవరుస | lexicon |
| isalnum | అక్షరమా_అంకెనా | proposed |
| isalpha | అక్షరమా | proposed |
| isdigit | అంకెనా | proposed |
| isspace | ఖాళీనా | proposed |
| log | సంవర్గమానం | proposed |
| main | ప్రధాన | lexicon |
| malloc | జ్ఞాపకం_ఇవ్వు | proposed |
| memcpy | జ్ఞాపకం_నకలు | proposed |
| operator | క్రియాకారకం | proposed |
| pow | ఘాతం | proposed |
| printf | రాయి | proposed |
| println | పంక్తి_ముద్రించు | proposed |
| putchar | అక్షరం_రాయి | proposed |
| raise | లేపు | lexicon |
| read | పఠ | lexicon |
| register | నమోదు | lexicon |
| restrict | పరిమిత | proposed |
| signal | సంకేతం | lexicon |
| signed | గుర్తుగల | proposed |
| sin | జ్యా | proposed |
| sizeof | పరిమాణం | lexicon |
| sleep | సుషుప్తి | lexicon |
| sqrt | వర్గమూలం | proposed |
| sscanf | అక్షరశ్రేణి_చదువు | proposed |
| strlen | అక్షరశ్రేణి_పొడవు | proposed |
| strncmp | అక్షరశ్రేణి_పోలిక | proposed |
| strstr | అక్షరశ్రేణి_శోధన | proposed |
| struct | నిర్మాణం | lexicon |
| template | మూస | proposed |
| toupper | పెద్ద_అక్షరం | proposed |
| typedef | రకనిర్వచనం | lexicon |
| union | సంఘం | lexicon |
| unsigned | గుర్తులేని | proposed |
| virtual | మాయా | lexicon |
| write | లిఖ | lexicon |

### D Python

| Host name | Telugu | Provenance |
|---|---|---|
| Object | వస్తువు | lexicon |
| String | పదబంధం | lexicon |
| System | వ్యవస్థ | proposed |
| Thread | తంతువు | lexicon |
| abstract | నైరూప్య | lexicon |
| boolean | తార్కిక | proposed |
| byte | బైటు | proposed |
| case | స్థితి | lexicon |
| catch | పట్టుకో | lexicon |
| char | అక్షరం | lexicon |
| const | స్థిరరాశి | lexicon |
| default | అప్రమేయ | lexicon |
| do | చేయి | lexicon |
| double | ద్విగుణ | lexicon |
| extends | విస్తరించు | lexicon |
| final | తుది | proposed |
| float | దశాంశం | lexicon |
| goto | వెళ్ళు | lexicon |
| implements | అమలుచేయు | lexicon |
| instanceof | నమూనా_ఔనా | proposed |
| int | పూర్ణాంకం | lexicon |
| interface | అంతరముఖం | lexicon |
| long | దీర్ఘ | proposed |
| main | ప్రధాన | lexicon |
| native | స్థానిక | proposed |
| new | కొత్త | lexicon |
| package | సంచి | lexicon |
| println | పంక్తి_ముద్రించు | proposed |
| private | అంతరంగ | lexicon |
| protected | రక్షిత | lexicon |
| public | బహిరంగ | lexicon |
| read | పఠ | lexicon |
| short | పొట్టి | proposed |
| sleep | సుషుప్తి | lexicon |
| sqrt | వర్గమూలం | proposed |
| static | స్థిర | lexicon |
| super | పర | lexicon |
| switch | ఎంపిక | lexicon |
| this | ఇది | lexicon |
| throw | విసురు | lexicon |
| throws | విసురుతుంది | proposed |
| void | శూన్య | lexicon |
| volatile | అస్థిర | lexicon |
| write | లిఖ | lexicon |

### D BASIC

| Host name | Telugu | Provenance |
|---|---|---|
| AS | ఇవ | lexicon |
| CALL | పిలువు | lexicon |
| CONST | స్థిరరాశి | lexicon |
| DO | చేయి | lexicon |
| ELSE | లేకపోతే | lexicon |
| INT | పూర్ణాంకం | lexicon |
| SHARED | సహభాజిత | lexicon |
| STATIC | స్థిర | lexicon |
| STRING | పదబంధం | lexicon |
| TIMER | కాలయన్త్ర | lexicon |

### D LOGO

| Host name | Telugu | Provenance |
|---|---|---|
| print | ముద్రించు | proposed |

## Annex E (informative) Conformance tests

The reference implementation is tested with the programs of samples/gate in the Hindawi repository, which cover the programming content of the GATE Computer Science paper. Recorded on 2026-10-18: 113 of 113 C programs, written in Telugu, were lowered, compiled and run, and printed exactly what their English originals print; 1 of 1 Python programs did the same; 117 of 117 files were reversed byte for byte.

The program below, as written in the language, its transliterated form, and the C that the transducer gives:

### E source

```
#అన్తర్భావ <stdio.h>
/* binary search in a sorted array */
పూర్ణాంకం ద్విమాన_శోధన(పూర్ణాంకం విలువలు[], పూర్ణాంకం లెక్క, పూర్ణాంకం కీలకం) {
  పూర్ణాంకం దిగువ = 0, ఎగువ = లెక్క - 1;
  అయితే (దిగువ <= ఎగువ) {
    పూర్ణాంకం మధ్య = దిగువ + (ఎగువ - దిగువ) / 2;
    ఒకవేళ (విలువలు[మధ్య] == కీలకం) తిరిగి మధ్య;
    ఒకవేళ (విలువలు[మధ్య] < కీలకం) దిగువ = మధ్య + 1; లేకపోతే ఎగువ = మధ్య - 1;
  }
  తిరిగి -1;
}
పూర్ణాంకం ప్రధాన(శూన్య) {
  పూర్ణాంకం విలువలు[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  రాయి("%d %d\n", ద్విమాన_శోధన(విలువలు, 10, 23), ద్విమాన_శోధన(విలువలు, 10, 7));
  తిరిగి 0;
}
```

### E script filter

```
#अन्तर्भाव <stdio.h>
/* binary search in a sorted array */
पूर्णांकं द्विमान_शोधन(पूर्णांकं विलुवलु[], पूर्णांकं लॆक्क, पूर्णांकं कीलकं) {
  पूर्णांकं दिगुव = 0, ऎगुव = लॆक्क - 1;
  अयिते (दिगुव <= ऎगुव) {
    पूर्णांकं मध्य = दिगुव + (ऎगुव - दिगुव) / 2;
    ऒकवेळ (विलुवलु[मध्य] == कीलकं) तिरिगि मध्य;
    ऒकवेळ (विलुवलु[मध्य] < कीलकं) दिगुव = मध्य + 1; लेकपोते ऎगुव = मध्य - 1;
  }
  तिरिगि -1;
}
पूर्णांकं प्रधान(शून्य) {
  पूर्णांकं विलुवलु[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  रायि("%d %d\n", द्विमान_शोधन(विलुवलु, 10, 23), द्विमान_शोधन(विलुवलु, 10, 7));
  तिरिगि 0;
}
```

### E Romenagri

```
#_an_tarbhaawa <stdio.h>
/* binary search in a sorted array */
poor_nnaa_mka_m _dwimaana_shoa_dhana(poor_nnaa_mka_m wiluwalu[], poor_nnaa_mka_m laekka, poor_nnaa_mka_m keelaka_m) {
  poor_nnaa_mka_m _diguwa = 0, _aeguwa = laekka - 1;
  _ayi_taee (_diguwa <= _aeguwa) {
    poor_nnaa_mka_m ma_dhya = _diguwa + (_aeguwa - _diguwa) / 2;
    _owkawaeelvra (wiluwalu[ma_dhya] == keelaka_m) _tirigi ma_dhya;
    _owkawaeelvra (wiluwalu[ma_dhya] < keelaka_m) _diguwa = ma_dhya + 1; laeekapoa_taee _aeguwa = ma_dhya - 1;
  }
  _tirigi -1;
}
poor_nnaa_mka_m pra_dhaana(shoonya) {
  poor_nnaa_mka_m wiluwalu[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  raayi("%d %d\n", _dwimaana_shoa_dhana(wiluwalu, 10, 23), _dwimaana_shoa_dhana(wiluwalu, 10, 7));
  _tirigi 0;
}
```

### E C

```
#include <stdio.h>
/* binary search in a sorted array */
int _dwimaana_shoa_dhana(int wiluwalu[], int laekka, int keelaka_m) {
  int _diguwa = 0, _aeguwa = laekka - 1;
  while (_diguwa <= _aeguwa) {
    int ma_dhya = _diguwa + (_aeguwa - _diguwa) / 2;
    if (wiluwalu[ma_dhya] == keelaka_m) return ma_dhya;
    if (wiluwalu[ma_dhya] < keelaka_m) _diguwa = ma_dhya + 1; else _aeguwa = ma_dhya - 1;
  }
  return -1;
}
int main(void) {
  int wiluwalu[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  printf("%d %d\n", _dwimaana_shoa_dhana(wiluwalu, 10, 23), _dwimaana_shoa_dhana(wiluwalu, 10, 7));
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

