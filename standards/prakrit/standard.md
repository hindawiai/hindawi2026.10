# HLS prakrit 2026.10

**Prakrit bindings for programming languages: lexical mapping and lowering to the host standards**

Edition 2026.10, working draft, 2026-10-18. © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

## Foreword

This document was prepared by AyeAI, Hindawi project (Project ILM). It is generated from the Prakrit cell of Hindawi 2026.10 by lang/hindawi/tools/standards.py, so that the published standard and the reference implementation cannot drift apart. Its stage is a working draft: the words marked proposed in Annex A await review by the Prakrit language community, through the review pages of the Hindawi project.

## Introduction

This document lets programs be written in Prakrit, in the Devanagari script, in each of the programming languages listed in Clause 1. Each binding is a programming language in its own right, Prakrit C for example, whose programs are lowered by the function defined in Clause 6 to programs of the host language, and are then processed by any conforming implementation of the host standard. The host standards are incorporated by reference and are not restated. Names keep a defined form down to object code (Clause 7), so programs written in Prakrit remain debuggable at the level of firmware, kernels and libraries.

## 1 Scope

This document specifies, for the Prakrit language written in the Devanagari script, bindings to the following host programming languages: C, C preprocessor, C++, Java, Python, BASIC, LOGO. For each binding it specifies the native keywords and directives, the lowering of native programs to host programs, the treatment of names, and the requirements for conformance.

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

- binding: programming language defined by this document whose programs are written in Prakrit and lowered to one host language

- native keyword: word of this document that stands for one keyword, directive or standard library name of a host language

- lowering: function from native programs to host programs defined in Clause 6

- raising: inverse of lowering applied to a host program with a dictionary of names, giving back the native program exactly

- name transformation: function from native names to host identifiers defined in Clause 7

- C-level form: result of the name transformation; the form a native name takes in host source and in object code

## 4 Conformance

A conforming Prakrit program of a binding shall be a text that meets Clause 5 and whose lowering is a conforming program of the host language.

A conforming implementation of a binding shall accept every conforming program of that binding and shall behave as the lowering of the program, processed by a conforming implementation of the host language, behaves.

An implementation that raises host programs into a binding shall produce native programs whose lowering, with the same dictionary of names, is identical to the host program it raised.

## 5 Character set and encoding

A native program shall be encoded in UTF-8 and shall be in Normalization Form C. Native keywords and names are written in the Devanagari script, whose direction is left to right. Numeric literals are written with the digits 0 to 9 (U+0030 to U+0039). A native keyword written as several words is one token, its words joined by LOW LINE (U+005F).

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

| Host | Prakrit | Source |
|---|---|---|
| auto | auto | host form (no native word yet) |
| break | भङ्ग | lexicon |
| case | पक्ष | lexicon |
| char | वर्ण | lexicon |
| const | ध्रुव | lexicon |
| continue | अनुवर्त | lexicon |
| default | स्वभाव | lexicon |
| do | करेहि | lexicon |
| double | द्विगुण | lexicon |
| else | अण्णहा | lexicon |
| enum | गणना | lexicon |
| extern | बाह्य | lexicon |
| float | भिन्न | lexicon |
| for | प्रति | lexicon |
| goto | गच्छ | lexicon |
| if | जइ | lexicon |
| inline | अन्तःस्थ | lexicon |
| int | पूर्णाङ्क | lexicon |
| long | long | host form (no native word yet) |
| register | पञ्जिका | lexicon |
| restrict | restrict | host form (no native word yet) |
| return | प्रत्यागम | lexicon |
| short | short | host form (no native word yet) |
| signed | signed | host form (no native word yet) |
| sizeof | परिमाण | lexicon |
| static | स्थिर | lexicon |
| struct | संरचना | lexicon |
| switch | विकल्प | lexicon |
| typedef | प्रकारनिर्देश | lexicon |
| union | सङ्घ | lexicon |
| unsigned | unsigned | host form (no native word yet) |
| void | शून्य | lexicon |
| volatile | चञ्चल | lexicon |
| while | जाव | lexicon |
| main | main | host form (no native word yet) |

Standard library and runtime names of the C binding:

| Host | Prakrit | Source |
|---|---|---|
| NULL | रिक्त | lexicon |
| assert | प्रतिज्ञा | lexicon |
| free | मुक्त | lexicon |
| private | गुप्त | lexicon |
| protected | रक्षित | lexicon |
| public | सार्वजनिक | lexicon |
| raise | उत्थापय | lexicon |
| read | पठ | lexicon |
| signal | सङ्केत | lexicon |
| virtual | आभास | lexicon |
| write | लिख | lexicon |

### A.2 C preprocessor

Host: ISO/IEC 9899, Information technology, Programming languages, C (preprocessing directives). Names: name transformation.

| Host | Prakrit | Source |
|---|---|---|
| #define | #define | host form (no native word yet) |
| #include | #अन्तर्भाव | lexicon |
| #if | #जइ | lexicon |
| #ifdef | #ifdef | host form (no native word yet) |
| #ifndef | #ifndef | host form (no native word yet) |
| #else | #अण्णहा | lexicon |
| #elif | #नोचेद्यदि | lexicon |
| #endif | #endif | host form (no native word yet) |
| #undef | #undef | host form (no native word yet) |
| #pragma | #pragma | host form (no native word yet) |
| #error | #error | host form (no native word yet) |
| #line | #line | host form (no native word yet) |

### A.3 C++

Host: ISO/IEC 14882, Programming languages, C++. Names: name transformation.

| Host | Prakrit | Source |
|---|---|---|
| auto | auto | host form (no native word yet) |
| break | भङ्ग | lexicon |
| case | पक्ष | lexicon |
| char | वर्ण | lexicon |
| const | ध्रुव | lexicon |
| continue | अनुवर्त | lexicon |
| default | स्वभाव | lexicon |
| do | करेहि | lexicon |
| double | द्विगुण | lexicon |
| else | अण्णहा | lexicon |
| enum | गणना | lexicon |
| extern | बाह्य | lexicon |
| float | भिन्न | lexicon |
| for | प्रति | lexicon |
| goto | गच्छ | lexicon |
| if | जइ | lexicon |
| inline | अन्तःस्थ | lexicon |
| int | पूर्णाङ्क | lexicon |
| long | long | host form (no native word yet) |
| register | पञ्जिका | lexicon |
| restrict | restrict | host form (no native word yet) |
| return | प्रत्यागम | lexicon |
| short | short | host form (no native word yet) |
| signed | signed | host form (no native word yet) |
| sizeof | परिमाण | lexicon |
| static | स्थिर | lexicon |
| struct | संरचना | lexicon |
| switch | विकल्प | lexicon |
| typedef | प्रकारनिर्देश | lexicon |
| union | सङ्घ | lexicon |
| unsigned | unsigned | host form (no native word yet) |
| void | शून्य | lexicon |
| volatile | चञ्चल | lexicon |
| while | जाव | lexicon |
| main | main | host form (no native word yet) |
| bool | तार्किक | lexicon |
| catch | गृहाण | lexicon |
| class | वर्ग | lexicon |
| delete | delete | host form (no native word yet) |
| explicit | explicit | host form (no native word yet) |
| false | मिच्छ | lexicon |
| friend | friend | host form (no native word yet) |
| mutable | mutable | host form (no native word yet) |
| namespace | नामाकाश | lexicon |
| new | नूतन | lexicon |
| nullptr | nullptr | host form (no native word yet) |
| operator | operator | host form (no native word yet) |
| private | गुप्त | lexicon |
| protected | रक्षित | lexicon |
| public | सार्वजनिक | lexicon |
| template | template | host form (no native word yet) |
| this | एतत् | lexicon |
| throw | क्षिप | lexicon |
| true | सच्च | lexicon |
| try | यत्न | lexicon |
| typename | typename | host form (no native word yet) |
| using | using | host form (no native word yet) |
| virtual | आभास | lexicon |
| cout | cout | host form (no native word yet) |
| cin | cin | host form (no native word yet) |
| endl | endl | host form (no native word yet) |

Standard library and runtime names of the C++ binding:

| Host | Prakrit | Source |
|---|---|---|
| NULL | रिक्त | lexicon |
| assert | प्रतिज्ञा | lexicon |
| free | मुक्त | lexicon |
| pipe | प्रणाल | lexicon |
| raise | उत्थापय | lexicon |
| read | पठ | lexicon |
| signal | सङ्केत | lexicon |
| sleep | सुषुप्ति | lexicon |
| sync | समकाल | lexicon |
| write | लिख | lexicon |

### A.4 Java

Host: The Java Language Specification, Oracle, current edition. Names: unchanged.

| Host | Prakrit | Source |
|---|---|---|
| abstract | अमूर्त | lexicon |
| assert | प्रतिज्ञा | lexicon |
| boolean | boolean | host form (no native word yet) |
| break | भङ्ग | lexicon |
| byte | byte | host form (no native word yet) |
| case | पक्ष | lexicon |
| catch | गृहाण | lexicon |
| char | वर्ण | lexicon |
| class | वर्ग | lexicon |
| continue | अनुवर्त | lexicon |
| default | स्वभाव | lexicon |
| do | करेहि | lexicon |
| double | द्विगुण | lexicon |
| else | अण्णहा | lexicon |
| enum | गणना | lexicon |
| extends | विस्तृत | lexicon |
| final | final | host form (no native word yet) |
| finally | अन्ततः | lexicon |
| float | भिन्न | lexicon |
| for | प्रति | lexicon |
| if | जइ | lexicon |
| implements | निष्पादित | lexicon |
| import | आनयन | lexicon |
| instanceof | instanceof | host form (no native word yet) |
| int | पूर्णाङ्क | lexicon |
| interface | सन्धि | lexicon |
| long | long | host form (no native word yet) |
| native | native | host form (no native word yet) |
| new | नूतन | lexicon |
| package | पुटक | lexicon |
| private | गुप्त | lexicon |
| protected | रक्षित | lexicon |
| public | सार्वजनिक | lexicon |
| return | प्रत्यागम | lexicon |
| short | short | host form (no native word yet) |
| static | स्थिर | lexicon |
| super | पर | lexicon |
| switch | विकल्प | lexicon |
| synchronized | synchronized | host form (no native word yet) |
| this | एतत् | lexicon |
| throw | क्षिप | lexicon |
| throws | throws | host form (no native word yet) |
| try | यत्न | lexicon |
| void | शून्य | lexicon |
| volatile | चञ्चल | lexicon |
| while | जाव | lexicon |
| true | सच्च | lexicon |
| false | मिच्छ | lexicon |
| null | रिक्त | lexicon |
| String | पदावली | lexicon |
| System | System | host form (no native word yet) |

Standard library and runtime names of the Java binding:

| Host | Prakrit | Source |
|---|---|---|
| Object | वस्तु | lexicon |
| Thread | तन्तु | lexicon |
| const | ध्रुव | lexicon |
| extern | बाह्य | lexicon |
| free | मुक्त | lexicon |
| goto | गच्छ | lexicon |
| inline | अन्तःस्थ | lexicon |
| raise | उत्थापय | lexicon |
| read | पठ | lexicon |
| register | पञ्जिका | lexicon |
| signal | सङ्केत | lexicon |
| sizeof | परिमाण | lexicon |
| sleep | सुषुप्ति | lexicon |
| struct | संरचना | lexicon |
| typedef | प्रकारनिर्देश | lexicon |
| union | सङ्घ | lexicon |
| virtual | आभास | lexicon |
| write | लिख | lexicon |

### A.5 Python

Host: The Python Language Reference, Python Software Foundation, current version. Names: unchanged.

| Host | Prakrit | Source |
|---|---|---|
| False | मिच्छ | lexicon |
| None | None | host form (no native word yet) |
| True | सच्च | lexicon |
| and | य | lexicon |
| as | इव | lexicon |
| assert | प्रतिज्ञा | lexicon |
| break | भङ्ग | lexicon |
| class | वर्ग | lexicon |
| continue | अनुवर्त | lexicon |
| def | def | host form (no native word yet) |
| del | del | host form (no native word yet) |
| elif | नोचेद्यदि | lexicon |
| else | अण्णहा | lexicon |
| except | अपवाद | lexicon |
| finally | अन्ततः | lexicon |
| for | प्रति | lexicon |
| from | तः | lexicon |
| global | वैश्विक | lexicon |
| if | जइ | lexicon |
| import | आनयन | lexicon |
| in | अन्तः | lexicon |
| is | is | host form (no native word yet) |
| lambda | अनामन् | lexicon |
| nonlocal | nonlocal | host form (no native word yet) |
| not | ण | lexicon |
| or | वा | lexicon |
| pass | pass | host form (no native word yet) |
| raise | उत्थापय | lexicon |
| return | प्रत्यागम | lexicon |
| try | यत्न | lexicon |
| while | जाव | lexicon |
| with | with | host form (no native word yet) |
| yield | दा | lexicon |
| print | print | host form (no native word yet) |
| range | range | host form (no native word yet) |
| len | len | host form (no native word yet) |

Standard library and runtime names of the Python binding:

| Host | Prakrit | Source |
|---|---|---|
| Object | वस्तु | lexicon |
| String | पदावली | lexicon |
| Thread | तन्तु | lexicon |
| abstract | अमूर्त | lexicon |
| case | पक्ष | lexicon |
| catch | गृहाण | lexicon |
| char | वर्ण | lexicon |
| const | ध्रुव | lexicon |
| default | स्वभाव | lexicon |
| do | करेहि | lexicon |
| double | द्विगुण | lexicon |
| extends | विस्तृत | lexicon |
| float | भिन्न | lexicon |
| goto | गच्छ | lexicon |
| implements | निष्पादित | lexicon |
| int | पूर्णाङ्क | lexicon |
| interface | सन्धि | lexicon |
| new | नूतन | lexicon |
| package | पुटक | lexicon |
| private | गुप्त | lexicon |
| protected | रक्षित | lexicon |
| public | सार्वजनिक | lexicon |
| read | पठ | lexicon |
| sleep | सुषुप्ति | lexicon |
| static | स्थिर | lexicon |
| super | पर | lexicon |
| switch | विकल्प | lexicon |
| this | एतत् | lexicon |
| throw | क्षिप | lexicon |
| void | शून्य | lexicon |
| volatile | चञ्चल | lexicon |
| write | लिख | lexicon |

### A.6 BASIC

Host: ISO/IEC 10279, Information technology, Programming languages, Full BASIC. Names: name transformation.

| Host | Prakrit | Source |
|---|---|---|
| dim | dim | host form (no native word yet) |
| end | अन्त | lexicon |
| for | प्रति | lexicon |
| gosub | gosub | host form (no native word yet) |
| goto | गच्छ | lexicon |
| if | जइ | lexicon |
| input | input | host form (no native word yet) |
| let | अस्तु | lexicon |
| next | next | host form (no native word yet) |
| print | print | host form (no native word yet) |
| rem | rem | host form (no native word yet) |
| return | प्रत्यागम | lexicon |
| step | step | host form (no native word yet) |
| then | then | host form (no native word yet) |
| to | to | host form (no native word yet) |
| wend | wend | host form (no native word yet) |
| while | जाव | lexicon |
| and | य | lexicon |
| or | वा | lexicon |
| not | ण | lexicon |
| mod | mod | host form (no native word yet) |

Standard library and runtime names of the BASIC binding:

| Host | Prakrit | Source |
|---|---|---|
| AS | इव | lexicon |
| CALL | आह्वान | lexicon |
| CONST | ध्रुव | lexicon |
| DO | करेहि | lexicon |
| ELSE | अण्णहा | lexicon |
| INT | पूर्णाङ्क | lexicon |
| SHARED | सहभाजित | lexicon |
| STATIC | स्थिर | lexicon |
| STRING | पदावली | lexicon |
| TIMER | कालयन्त्र | lexicon |

### A.7 LOGO

Host: No international standard; the host is the Berkeley Logo dialect (bibliography). Names: name transformation.

| Host | Prakrit | Source |
|---|---|---|
| forward | अग्रप्रसार | lexicon |
| back | back | host form (no native word yet) |
| left | left | host form (no native word yet) |
| right | right | host form (no native word yet) |
| penup | penup | host form (no native word yet) |
| pendown | pendown | host form (no native word yet) |
| repeat | repeat | host form (no native word yet) |
| to | to | host form (no native word yet) |
| end | अन्त | lexicon |
| make | make | host form (no native word yet) |
| if | जइ | lexicon |
| ifelse | ifelse | host form (no native word yet) |
| home | home | host form (no native word yet) |
| clearscreen | clearscreen | host form (no native word yet) |

## Annex B (informative) Coverage and review

| Binding | Host keywords with a native word | Library names |
|---|---|---|
| C | 28 of 35 | 11 |
| C preprocessor | 4 of 12 | 0 |
| C++ | 42 of 61 | 10 |
| Java | 41 of 51 | 18 |
| Python | 26 of 36 | 32 |
| BASIC | 10 of 21 | 10 |
| LOGO | 3 of 14 | 0 |

The lowering of Prakrit programs to C is verified by the reference implementation: runs, same output. Source Chintamani means a word of the original Hindawi transducers; lexicon, a word of the language's lexicon; proposed, a word proposed by the project and not yet reviewed by the language community.

## Annex C (normative) Script filter

Devanagari text passes to Romenagri without a script filter.

## Annex D (informative) Rights and provenance

This document is an original work. It defines new programming languages by reference to the host language standards listed in Clause 2 and reproduces no text from them. Permission to adopt, translate or publish it as a standard is given by the copyright holder to a standards body on request.

Single words and the keywords of the host languages are not reproduced from any copyrighted text; the native words of Annex A were chosen by the Hindawi project, taken from the language's lexicon in the Hindawi repository, or, for Hindi, taken from the Chintamani transducers of the original Hindawi, whose author holds their copyright.

## Bibliography

- Hindawi 2026.10, hindawiai/hindawi2026.10, the reference implementation
- Chintamani, hindawiai/chintamani, the Hindawi transducers and the Romenagri tools
- Berkeley Logo reference manual, Brian Harvey

