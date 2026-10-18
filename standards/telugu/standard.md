# HLS te 2026.10

**Telugu bindings for programming languages: lexical mapping and lowering to the host standards**

Edition 2026.10, working draft, 2026-10-18. © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

## Foreword

This document was prepared by AyeAI, Hindawi project (Project ILM). It is generated from the Telugu cell of Hindawi 2026.10 by lang/hindawi/tools/standards.py, so that the published standard and the reference implementation cannot drift apart. Its stage is a working draft: the words marked proposed in Annex A await review by the Telugu language community, through the review pages of the Hindawi project.

## Introduction

This document lets programs be written in Telugu, in the Telugu script, in each of the programming languages listed in Clause 1. Each binding is a programming language in its own right, Telugu C for example, whose programs are lowered by the function defined in Clause 6 to programs of the host language, and are then processed by any conforming implementation of the host standard. The host standards are incorporated by reference and are not restated. Names keep a defined form down to object code (Clause 7), so programs written in Telugu remain debuggable at the level of firmware, kernels and libraries.

## 1 Scope

This document specifies, for the Telugu language written in the Telugu script, bindings to the following host programming languages: C, C preprocessor, C++, Java, Python, BASIC, LOGO. For each binding it specifies the native keywords and directives, the lowering of native programs to host programs, the treatment of names, and the requirements for conformance.

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

- binding: programming language defined by this document whose programs are written in Telugu and lowered to one host language

- native keyword: word of this document that stands for one keyword, directive or standard library name of a host language

- lowering: function from native programs to host programs defined in Clause 6

- raising: inverse of lowering applied to a host program with a dictionary of names, giving back the native program exactly

- name transformation: function from native names to host identifiers defined in Clause 7

- C-level form: result of the name transformation; the form a native name takes in host source and in object code

## 4 Conformance

A conforming Telugu program of a binding shall be a text that meets Clause 5 and whose lowering is a conforming program of the host language.

A conforming implementation of a binding shall accept every conforming program of that binding and shall behave as the lowering of the program, processed by a conforming implementation of the host language, behaves.

An implementation that raises host programs into a binding shall produce native programs whose lowering, with the same dictionary of names, is identical to the host program it raised.

## 5 Character set and encoding

A native program shall be encoded in UTF-8 and shall be in Normalization Form C. Native keywords and names are written in the Telugu script, whose direction is left to right. Numeric literals are written with the digits 0 to 9 (U+0030 to U+0039). A native keyword written as several words is one token, its words joined by LOW LINE (U+005F).

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

| Host | Telugu | Source |
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

Standard library and runtime names of the C binding:

| Host | Telugu | Source |
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

### A.2 C preprocessor

Host: ISO/IEC 9899, Information technology, Programming languages, C (preprocessing directives). Names: name transformation.

| Host | Telugu | Source |
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

Host: ISO/IEC 14882, Programming languages, C++. Names: name transformation.

| Host | Telugu | Source |
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

Standard library and runtime names of the C++ binding:

| Host | Telugu | Source |
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

### A.4 Java

Host: The Java Language Specification, Oracle, current edition. Names: unchanged.

| Host | Telugu | Source |
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

Standard library and runtime names of the Java binding:

| Host | Telugu | Source |
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

### A.5 Python

Host: The Python Language Reference, Python Software Foundation, current version. Names: unchanged.

| Host | Telugu | Source |
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

Standard library and runtime names of the Python binding:

| Host | Telugu | Source |
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

### A.6 BASIC

Host: ISO/IEC 10279, Information technology, Programming languages, Full BASIC. Names: name transformation.

| Host | Telugu | Source |
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

Standard library and runtime names of the BASIC binding:

| Host | Telugu | Source |
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

### A.7 LOGO

Host: No international standard; the host is the Berkeley Logo dialect (bibliography). Names: name transformation.

| Host | Telugu | Source |
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

Standard library and runtime names of the LOGO binding:

| Host | Telugu | Source |
|---|---|---|
| print | ముద్రించు | proposed |

## Annex B (informative) Coverage and review

| Binding | Host keywords with a native word | Library names |
|---|---|---|
| C | 35 of 35 | 37 |
| C preprocessor | 12 of 12 | 0 |
| C++ | 61 of 61 | 35 |
| Java | 51 of 51 | 50 |
| Python | 36 of 36 | 44 |
| BASIC | 21 of 21 | 10 |
| LOGO | 14 of 14 | 1 |

The lowering of Telugu programs to C is verified by the reference implementation: runs, same output. Source Chintamani means a word of the original Hindawi transducers; lexicon, a word of the language's lexicon; proposed, a word proposed by the project and not yet reviewed by the language community.

## Annex C (normative) Script filter

The script filter is Chintamani's own (fltr_te_hi).

## Annex D (informative) Rights and provenance

This document is an original work. It defines new programming languages by reference to the host language standards listed in Clause 2 and reproduces no text from them. Permission to adopt, translate or publish it as a standard is given by the copyright holder to a standards body on request.

Single words and the keywords of the host languages are not reproduced from any copyrighted text; the native words of Annex A were chosen by the Hindawi project, taken from the language's lexicon in the Hindawi repository, or, for Hindi, taken from the Chintamani transducers of the original Hindawi, whose author holds their copyright.

## Bibliography

- Hindawi 2026.10, hindawiai/hindawi2026.10, the reference implementation
- Chintamani, hindawiai/chintamani, the Hindawi transducers and the Romenagri tools
- Berkeley Logo reference manual, Brian Harvey

