# HLS ne 2026.10

**Nepali bindings for programming languages: lexical mapping and lowering to the host standards**

Edition 2026.10, working draft, 2026-10-18. © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

## Foreword

This document was prepared by AyeAI, Hindawi project (Project ILM). It is generated from the Nepali cell of Hindawi 2026.10 by lang/hindawi/tools/standards.py, so that the published standard and the reference implementation cannot drift apart. Its stage is a working draft: the words marked proposed in Annex A await review by the Nepali language community, through the review pages of the Hindawi project.

## Introduction

This document lets programs be written in Nepali, in the Devanagari script, in each of the programming languages listed in Clause 1. Each binding is a programming language in its own right, Nepali C for example, whose programs are lowered by the function defined in Clause 6 to programs of the host language, and are then processed by any conforming implementation of the host standard. The host standards are incorporated by reference and are not restated. Names keep a defined form down to object code (Clause 7), so programs written in Nepali remain debuggable at the level of firmware, kernels and libraries.

## 1 Scope

This document specifies, for the Nepali language written in the Devanagari script, bindings to the following host programming languages: C, C preprocessor, C++, Java, Python, BASIC, LOGO. For each binding it specifies the native keywords and directives, the lowering of native programs to host programs, the treatment of names, and the requirements for conformance.

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

- binding: programming language defined by this document whose programs are written in Nepali and lowered to one host language

- native keyword: word of this document that stands for one keyword, directive or standard library name of a host language

- lowering: function from native programs to host programs defined in Clause 6

- raising: inverse of lowering applied to a host program with a dictionary of names, giving back the native program exactly

- name transformation: function from native names to host identifiers defined in Clause 7

- C-level form: result of the name transformation; the form a native name takes in host source and in object code

## 4 Conformance

A conforming Nepali program of a binding shall be a text that meets Clause 5 and whose lowering is a conforming program of the host language.

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

| Host | Nepali | Source |
|---|---|---|
| auto | स्वतः | delivered cell |
| break | रोक | lexicon |
| case | पक्ष | lexicon |
| char | वर्ण | lexicon |
| const | अचर | lexicon |
| continue | जारी | lexicon |
| default | स्वभाव | lexicon |
| do | गर | lexicon |
| double | द्विगुण | lexicon |
| else | अन्यथा | lexicon |
| enum | गणना | lexicon |
| extern | बाह्य | lexicon |
| float | भिन्न | lexicon |
| for | लागि | lexicon |
| goto | गच्छ | lexicon |
| if | यदि | lexicon |
| inline | अन्तःस्थ | lexicon |
| int | पूर्णाङ्क | lexicon |
| long | दीर्घ | delivered cell |
| register | पञ्जिका | lexicon |
| restrict | restrict | host form (no native word yet) |
| return | फर्काऊ | lexicon |
| short | लघु | delivered cell |
| signed | चिन्हित | delivered cell |
| sizeof | परिमाण | lexicon |
| static | स्थिर | lexicon |
| struct | संरचना | lexicon |
| switch | विकल्प | lexicon |
| typedef | प्रकारनिर्देश | lexicon |
| union | सङ्घ | lexicon |
| unsigned | अचिन्हित | delivered cell |
| void | शून्य | lexicon |
| volatile | चञ्चल | lexicon |
| while | जबसम्म | lexicon |
| main | main | host form (no native word yet) |

Standard library and runtime names of the C binding:

| Host | Nepali | Source |
|---|---|---|
| BUFSIZ | बफ_मान | delivered cell |
| CHAR_BIT | अक्षर_बिट | delivered cell |
| CHAR_MAX | अक्षर_उच्च | delivered cell |
| CHAR_MIN | अक्षर_न्यून | delivered cell |
| CHILD_MAX | शिशु_उच्च | delivered cell |
| CLK_TCK | घड़ी_टिक | delivered cell |
| DBL_DIG | द्विग_भग्न | delivered cell |
| DBL_EPSILON | द्विग_अंतर | delivered cell |
| DBL_MANT_DIG | द्विग_पूर्ण | delivered cell |
| DBL_MAX | द्विग_उच्च | delivered cell |
| DBL_MIN | द्विग_न्यून | delivered cell |
| DIR | सूची | delivered cell |
| EDOM | गलत_तर्क | delivered cell |
| EOF | खातापूर्ण | delivered cell |
| ERANGE | दुस्फल | delivered cell |
| EXIT_FAILURE | निकास_त्रुटि | delivered cell |
| EXIT_SUCCESS | निकास_सफल | delivered cell |
| FILE | खाता | delivered cell |
| FILENAME_MAX | खातानाम_उच्च | delivered cell |
| FLT_DIG | भग्न_भग्न | delivered cell |
| FLT_EPSILON | भग्न_अंतर | delivered cell |
| FLT_MANT_DIG | भग्न_पूर्ण | delivered cell |
| FLT_MAX | भग्न_उच्च | delivered cell |
| FLT_MIN | भग्न_न्यून | delivered cell |
| FLT_RADIX | भग्न_आधार | delivered cell |
| FOPEN_MAX | ख_खोलो_उच्च | delivered cell |
| HUGE_VAL | विशाल_मान | delivered cell |
| INFINITY | अनन्त | delivered cell |
| INT_MAX | पूर्णांक_उच्च | delivered cell |
| INT_MIN | पूर्णांक_न्यून | delivered cell |
| LDBL_DIG | द_द्वि_भग्न | delivered cell |
| LDBL_EPSILON | द_द्वि_अंतर | delivered cell |
| LDBL_MANT_DIG | द_द्वि_पूर्ण | delivered cell |
| LDBL_MAX | द_द्वि_उच्च | delivered cell |
| LDBL_MIN | द_द्वि_न्यून | delivered cell |
| LONG_MAX | दीर्घ_उच्च | delivered cell |
| LONG_MIN | दीर्घ_न्यून | delivered cell |
| L_tmpnam | ब_क्षणिक | delivered cell |
| NAN | न_अंक | delivered cell |
| NDEBUG | न_संशोधन | delivered cell |
| NULL | रिक्त | lexicon |
| RAND_MAX | अक्रम_उच्च | delivered cell |
| SCHAR_MAX | च_अक्षर_उच्च | delivered cell |
| SCHAR_MIN | च_अक्षर_न्यून | delivered cell |
| SEEK_CUR | प्रस्तुत_से | delivered cell |
| SEEK_END | अंत_से | delivered cell |
| SEEK_SET | शुरू_से | delivered cell |
| SHRT_MAX | लघु_उच्च | delivered cell |
| SHRT_MIN | लघु_न्यून | delivered cell |
| SIBGABRT | संक_पात | delivered cell |
| SIGFPE | संक_भ_त्रुटि | delivered cell |
| SIGILL | संक_अवैध | delivered cell |
| SIGINT | संक_विघ्न | delivered cell |
| SIGSEGV | संक_अंश | delivered cell |
| SIGTERM | संक_इति | delivered cell |
| SIG_DFL | संक_पूर्व | delivered cell |
| SIG_ERR | संक_त्रुटि | delivered cell |
| SIG_IGN | संक_छोड़ो | delivered cell |
| TMP_MAX | क्षणिक_उच्च | delivered cell |
| UCHAR_MAX | अच_अक्षर_उच्च | delivered cell |
| UINT_MAX | अच_पूर्णांक_उच्च | delivered cell |
| ULONG_MAX | अच_दीर्घ_उच्च | delivered cell |
| USHRT_MAX | अच_लघु_उच्च | delivered cell |
| __DATE__ | __दिन__ | delivered cell |
| __FILE__ | __खाता__ | delivered cell |
| __LINE__ | __पंक्ति__ | delivered cell |
| __STDC__ | __मानक__ | delivered cell |
| __TIME__ | __समय__ | delivered cell |
| abort | पात | delivered cell |
| abs | असल | delivered cell |
| asctime | समय_ठीक | delivered cell |
| asm | यंत्र | delivered cell |
| assert | प्रतिज्ञा | lexicon |
| atexit | निकास_पर | delivered cell |
| atof | म_से_भ | delivered cell |
| atoi | म_से_प | delivered cell |
| atol | म_से_द | delivered cell |
| bsearch | द्वा_खोज | delivered cell |
| calloc | सुस्मृति | delivered cell |
| ceil | उच्चमान | delivered cell |
| chdir | स_बदलो | delivered cell |
| clearerr | साफ_त्रुटि | delivered cell |
| clock | घड़ी | delivered cell |
| clock_t | घड़ी_प्रकार | delivered cell |
| close | बंद | delivered cell |
| closedir | बंद_सूची | delivered cell |
| ctime | स_समय | delivered cell |
| difftime | स_अंतर | delivered cell |
| dirname | स_नाम | delivered cell |
| div | भाग | delivered cell |
| div_t | भाग_प्रकार | delivered cell |
| errno | त्रुटि_सं | delivered cell |
| exit | निकास | delivered cell |
| fabs | भ_असल | delivered cell |
| fclose | ख_बंद | delivered cell |
| feof | ख_पूर्ण | delivered cell |
| ferror | ख_त्रुटि | delivered cell |
| fflush | ख_साफ | delivered cell |
| fgetc | ख_अक्षर_लो | delivered cell |
| fgetpos | ख_स्थान_लो | delivered cell |
| fgets | ख_माला_लो | delivered cell |
| floor | न्यूनमान | delivered cell |
| fmod | भ_शेष | delivered cell |
| fopen | ख_खोलो | delivered cell |
| fork | विभाजन | delivered cell |
| fpos_t | ख_स्थान_प्रकार | delivered cell |
| fprintf | ख_लिखो | delivered cell |
| fputc | ख_अक्षर_दो | delivered cell |
| fputs | ख_माला_दो | delivered cell |
| fread | ख_पढ़ो | delivered cell |
| free | मुक्त | lexicon |
| freopen | ख_व_खोलो | delivered cell |
| friend | मित्र | delivered cell |
| fscanf | ख_पूछो | delivered cell |
| fseek | ख_जाओ | delivered cell |
| fsetpos | ख_स्थान_दो | delivered cell |
| fstat | ख_स्थिति | delivered cell |
| ftell | ख_बताओ | delivered cell |
| fwrite | ख_डालो | delivered cell |
| getc | अ_लो | delivered cell |
| getchar | अक्षर_लो | delivered cell |
| getenv | दो_पर्या | delivered cell |
| gets | माला_लो | delivered cell |
| gettime | समय_लो | delivered cell |
| gmtime | स_जमट | delivered cell |
| isalnum | है_अक्षर_अंक | delivered cell |
| isalpha | है_अक्षर | delivered cell |
| iscntrl | है_नियंत्रण | delivered cell |
| isdigit | है_अंक | delivered cell |
| isfinite | है_सीमित | delivered cell |
| isgraph | है_चित्र | delivered cell |
| islower | है_छोटा | delivered cell |
| isodigit | है_अष्टक | delivered cell |
| isprint | है_छाप | delivered cell |
| ispunct | है_विराम | delivered cell |
| isspace | है_खाली | delivered cell |
| isupper | है_बड़ा | delivered cell |
| isxdigit | है_षष्ठादशक | delivered cell |
| jmp_buf | लाँघ_बफ | delivered cell |
| kill | समाप्त | delivered cell |
| labs | द_असल | delivered cell |
| lconv | स्था_बदल | delivered cell |
| ldiv | द_भाग | delivered cell |
| ldiv_t | द_भाग_प्रकार | delivered cell |
| localeconv | क्षेत्र_बदलो | delivered cell |
| localtime | स_स्थानीय | delivered cell |
| longjmp | दीर्घ_लाँघ | delivered cell |
| malloc | दो_स्मृति | delivered cell |
| memchr | स_प्रथम | delivered cell |
| memcmp | स_भेद | delivered cell |
| memcpy | स_नकल | delivered cell |
| memmove | स_हटाओ | delivered cell |
| memset | स_रखो | delivered cell |
| mkdir | सूची_गढ़ो | delivered cell |
| mktime | स_गढ़ो | delivered cell |
| offsetof | दुरत्व | delivered cell |
| open | खोलो | delivered cell |
| opendir | सूची_खोलो | delivered cell |
| operator | चालक | delivered cell |
| pause | छोड़ो | delivered cell |
| perror | लिखो_त्रुटि | delivered cell |
| pow | घात | delivered cell |
| printf | म_लिखो | delivered cell |
| private | गुप्त | lexicon |
| protected | रक्षित | lexicon |
| ptrdiff_t | सूचक_भेद_प्रकार | delivered cell |
| public | सार्वजनिक | lexicon |
| putc | अ_दो | delivered cell |
| putchar | अक्षर_दो | delivered cell |
| puts | माला_दो | delivered cell |
| qsort | क्विक | delivered cell |
| raise | उत्थापय | lexicon |
| rand | अक्रम | delivered cell |
| read | पठ | lexicon |
| readdir | सूची_पढ़ो | delivered cell |
| realloc | पुनः_स्मृति | delivered cell |
| remove | हटाओ | delivered cell |
| rename | नाम | delivered cell |
| rewind | शुरुआत | delivered cell |
| rewinddir | सूची_शुरु | delivered cell |
| rmdir | सूची_हटाओ | delivered cell |
| scanf | म_पूछो | delivered cell |
| setbuf | रखो_बफ | delivered cell |
| setjmp | बनाओ_लाँघ | delivered cell |
| setlocale | रखो_क्षेत्र | delivered cell |
| settime | समय_रखो | delivered cell |
| setvbuf | रखो_भबफ | delivered cell |
| sig_atomic_t | संक_पूर्ण_प्रकार | delivered cell |
| signal | सङ्केत | lexicon |
| sigpending | संक_बाकी | delivered cell |
| sigsuspend | संक_रोको | delivered cell |
| size_t | माप_प्रकार | delivered cell |
| sprintf | प्र_लिखो | delivered cell |
| sqrt | वर्ग_मूल | delivered cell |
| srand | बेक्रम | delivered cell |
| sscanf | माला_पूछो | delivered cell |
| stderr | मानक_त्रुटि | delivered cell |
| stdin | मानक_निवेश | delivered cell |
| stdout | मानक_निकास | delivered cell |
| strcat | म_जोड़ो | delivered cell |
| strchr | म_अक्षर | delivered cell |
| strcmp | म_भेद | delivered cell |
| strcpy | म_नकल | delivered cell |
| strcspn | म_खोज | delivered cell |
| strerror | म_त्रुटि | delivered cell |
| strftime | स_माला | delivered cell |
| strlen | म_माप | delivered cell |
| strncat | म_जोड़न | delivered cell |
| strncmp | म_भेदन | delivered cell |
| strncpy | म_नकलन | delivered cell |
| strrchr | म_खोजप | delivered cell |
| strspn | म_अखोज | delivered cell |
| strstr | म_माला | delivered cell |
| strtod | म_से_भग्न | delivered cell |
| strtok | म_मोहर | delivered cell |
| strtol | म_से_दीर्घ | delivered cell |
| strtoul | म_से_अदीर्घ | delivered cell |
| system | प्रणाली | delivered cell |
| template | ढाँचा | delivered cell |
| time | समय | delivered cell |
| time_t | समय_प्रकार | delivered cell |
| times | बार | delivered cell |
| tm | पंचांग | delivered cell |
| tmpfile | क्षणिक_ख | delivered cell |
| tmpnam | क्षणिक | delivered cell |
| tolower | छोटे | delivered cell |
| toupper | बड़े | delivered cell |
| ungetc | अक्षर_वापस | delivered cell |
| va_arg | बहु_तर्क | delivered cell |
| va_end | बहु_पूर्ण | delivered cell |
| va_list | बहु_सूची | delivered cell |
| va_start | बहु_शुरू | delivered cell |
| vfprintf | भख_लिखो | delivered cell |
| virtual | आभास | lexicon |
| vprintf | भ_लिखो | delivered cell |
| vsprintf | भम_लिखो | delivered cell |
| wait | रुको | delivered cell |
| wchar_t | ब_अक्षर_प्रकार | delivered cell |
| write | लिख | lexicon |

### A.2 C preprocessor

Host: ISO/IEC 9899, Information technology, Programming languages, C (preprocessing directives). Names: name transformation.

| Host | Nepali | Source |
|---|---|---|
| #define | #define | host form (no native word yet) |
| #include | #अन्तर्भाव | lexicon |
| #if | #यदि | lexicon |
| #ifdef | #ifdef | host form (no native word yet) |
| #ifndef | #ifndef | host form (no native word yet) |
| #else | #अन्यथा | lexicon |
| #elif | #अथवायदि | lexicon |
| #endif | #endif | host form (no native word yet) |
| #undef | #undef | host form (no native word yet) |
| #pragma | #pragma | host form (no native word yet) |
| #error | #error | host form (no native word yet) |
| #line | #line | host form (no native word yet) |

### A.3 C++

Host: ISO/IEC 14882, Programming languages, C++. Names: name transformation.

| Host | Nepali | Source |
|---|---|---|
| auto | स्वतः | delivered cell |
| break | रोक | lexicon |
| case | पक्ष | lexicon |
| char | वर्ण | lexicon |
| const | अचर | lexicon |
| continue | जारी | lexicon |
| default | स्वभाव | lexicon |
| do | गर | lexicon |
| double | द्विगुण | lexicon |
| else | अन्यथा | lexicon |
| enum | गणना | lexicon |
| extern | बाह्य | lexicon |
| float | भिन्न | lexicon |
| for | लागि | lexicon |
| goto | गच्छ | lexicon |
| if | यदि | lexicon |
| inline | अन्तःस्थ | lexicon |
| int | पूर्णाङ्क | lexicon |
| long | दीर्घ | delivered cell |
| register | पञ्जिका | lexicon |
| restrict | restrict | host form (no native word yet) |
| return | फर्काऊ | lexicon |
| short | लघु | delivered cell |
| signed | चिन्हित | delivered cell |
| sizeof | परिमाण | lexicon |
| static | स्थिर | lexicon |
| struct | संरचना | lexicon |
| switch | विकल्प | lexicon |
| typedef | प्रकारनिर्देश | lexicon |
| union | सङ्घ | lexicon |
| unsigned | अचिन्हित | delivered cell |
| void | शून्य | lexicon |
| volatile | चञ्चल | lexicon |
| while | जबसम्म | lexicon |
| main | main | host form (no native word yet) |
| bool | तार्किक | lexicon |
| catch | गृहाण | lexicon |
| class | वर्ग | lexicon |
| delete | delete | host form (no native word yet) |
| explicit | explicit | host form (no native word yet) |
| false | असत्य | lexicon |
| friend | मित्र | delivered cell |
| mutable | mutable | host form (no native word yet) |
| namespace | नामाकाश | lexicon |
| new | नूतन | lexicon |
| nullptr | nullptr | host form (no native word yet) |
| operator | चालक | delivered cell |
| private | गुप्त | lexicon |
| protected | रक्षित | lexicon |
| public | सार्वजनिक | lexicon |
| template | ढाँचा | delivered cell |
| this | एतत् | lexicon |
| throw | क्षिप | lexicon |
| true | सत्य | lexicon |
| try | यत्न | lexicon |
| typename | typename | host form (no native word yet) |
| using | using | host form (no native word yet) |
| virtual | आभास | lexicon |
| cout | cout | host form (no native word yet) |
| cin | cin | host form (no native word yet) |
| endl | endl | host form (no native word yet) |

Standard library and runtime names of the C++ binding:

| Host | Nepali | Source |
|---|---|---|
| BUFSIZ | बफ_मान | delivered cell |
| CHAR_BIT | अक्षर_बिट | delivered cell |
| CHAR_MAX | अक्षर_उच्च | delivered cell |
| CHAR_MIN | अक्षर_न्यून | delivered cell |
| CHILD_MAX | शिशु_उच्च | delivered cell |
| CLK_TCK | घड़ी_टिक | delivered cell |
| DBL_DIG | द्विग_भग्न | delivered cell |
| DBL_EPSILON | द्विग_अंतर | delivered cell |
| DBL_MANT_DIG | द्विग_पूर्ण | delivered cell |
| DBL_MAX | द्विग_उच्च | delivered cell |
| DBL_MIN | द्विग_न्यून | delivered cell |
| DIR | सूची | delivered cell |
| EDOM | गलत_तर्क | delivered cell |
| EOF | खातापूर्ण | delivered cell |
| ERANGE | दुस्फल | delivered cell |
| EXIT_FAILURE | निकास_त्रुटि | delivered cell |
| EXIT_SUCCESS | निकास_सफल | delivered cell |
| FILE | खाता | delivered cell |
| FILENAME_MAX | खातानाम_उच्च | delivered cell |
| FLT_DIG | भग्न_भग्न | delivered cell |
| FLT_EPSILON | भग्न_अंतर | delivered cell |
| FLT_MANT_DIG | भग्न_पूर्ण | delivered cell |
| FLT_MAX | भग्न_उच्च | delivered cell |
| FLT_MIN | भग्न_न्यून | delivered cell |
| FLT_RADIX | भग्न_आधार | delivered cell |
| FOPEN_MAX | ख_खोलो_उच्च | delivered cell |
| HUGE_VAL | विशाल_मान | delivered cell |
| INFINITY | अनन्त | delivered cell |
| INT_MAX | पूर्णांक_उच्च | delivered cell |
| INT_MIN | पूर्णांक_न्यून | delivered cell |
| LDBL_DIG | द_द्वि_भग्न | delivered cell |
| LDBL_EPSILON | द_द्वि_अंतर | delivered cell |
| LDBL_MANT_DIG | द_द्वि_पूर्ण | delivered cell |
| LDBL_MAX | द_द्वि_उच्च | delivered cell |
| LDBL_MIN | द_द्वि_न्यून | delivered cell |
| LONG_MAX | दीर्घ_उच्च | delivered cell |
| LONG_MIN | दीर्घ_न्यून | delivered cell |
| L_tmpnam | ब_क्षणिक | delivered cell |
| NAN | न_अंक | delivered cell |
| NDEBUG | न_संशोधन | delivered cell |
| NULL | रिक्त | lexicon |
| RAND_MAX | अक्रम_उच्च | delivered cell |
| SCHAR_MAX | च_अक्षर_उच्च | delivered cell |
| SCHAR_MIN | च_अक्षर_न्यून | delivered cell |
| SEEK_CUR | प्रस्तुत_से | delivered cell |
| SEEK_END | अंत_से | delivered cell |
| SEEK_SET | शुरू_से | delivered cell |
| SHRT_MAX | लघु_उच्च | delivered cell |
| SHRT_MIN | लघु_न्यून | delivered cell |
| SIBGABRT | संक_पात | delivered cell |
| SIGFPE | संक_भ_त्रुटि | delivered cell |
| SIGILL | संक_अवैध | delivered cell |
| SIGINT | संक_विघ्न | delivered cell |
| SIGSEGV | संक_अंश | delivered cell |
| SIGTERM | संक_इति | delivered cell |
| SIG_DFL | संक_पूर्व | delivered cell |
| SIG_ERR | संक_त्रुटि | delivered cell |
| SIG_IGN | संक_छोड़ो | delivered cell |
| TMP_MAX | क्षणिक_उच्च | delivered cell |
| UCHAR_MAX | अच_अक्षर_उच्च | delivered cell |
| UINT_MAX | अच_पूर्णांक_उच्च | delivered cell |
| ULONG_MAX | अच_दीर्घ_उच्च | delivered cell |
| USHRT_MAX | अच_लघु_उच्च | delivered cell |
| __DATE__ | __दिन__ | delivered cell |
| __FILE__ | __खाता__ | delivered cell |
| __LINE__ | __पंक्ति__ | delivered cell |
| __STDC__ | __मानक__ | delivered cell |
| __TIME__ | __समय__ | delivered cell |
| abort | पात | delivered cell |
| abs | असल | delivered cell |
| asctime | समय_ठीक | delivered cell |
| asm | यंत्र | delivered cell |
| assert | प्रतिज्ञा | lexicon |
| atexit | निकास_पर | delivered cell |
| atof | म_से_भ | delivered cell |
| atoi | म_से_प | delivered cell |
| atol | म_से_द | delivered cell |
| bsearch | द्वा_खोज | delivered cell |
| calloc | सुस्मृति | delivered cell |
| ceil | उच्चमान | delivered cell |
| chdir | स_बदलो | delivered cell |
| clearerr | साफ_त्रुटि | delivered cell |
| clock | घड़ी | delivered cell |
| clock_t | घड़ी_प्रकार | delivered cell |
| close | बंद | delivered cell |
| closedir | बंद_सूची | delivered cell |
| ctime | स_समय | delivered cell |
| difftime | स_अंतर | delivered cell |
| dirname | स_नाम | delivered cell |
| div | भाग | delivered cell |
| div_t | भाग_प्रकार | delivered cell |
| errno | त्रुटि_सं | delivered cell |
| exit | निकास | delivered cell |
| fabs | भ_असल | delivered cell |
| fclose | ख_बंद | delivered cell |
| feof | ख_पूर्ण | delivered cell |
| ferror | ख_त्रुटि | delivered cell |
| fflush | ख_साफ | delivered cell |
| fgetc | ख_अक्षर_लो | delivered cell |
| fgetpos | ख_स्थान_लो | delivered cell |
| fgets | ख_माला_लो | delivered cell |
| floor | न्यूनमान | delivered cell |
| fmod | भ_शेष | delivered cell |
| fopen | ख_खोलो | delivered cell |
| fork | विभाजन | delivered cell |
| fpos_t | ख_स्थान_प्रकार | delivered cell |
| fprintf | ख_लिखो | delivered cell |
| fputc | ख_अक्षर_दो | delivered cell |
| fputs | ख_माला_दो | delivered cell |
| fread | ख_पढ़ो | delivered cell |
| free | मुक्त | lexicon |
| freopen | ख_व_खोलो | delivered cell |
| fscanf | ख_पूछो | delivered cell |
| fseek | ख_जाओ | delivered cell |
| fsetpos | ख_स्थान_दो | delivered cell |
| fstat | ख_स्थिति | delivered cell |
| ftell | ख_बताओ | delivered cell |
| fwrite | ख_डालो | delivered cell |
| getc | अ_लो | delivered cell |
| getchar | अक्षर_लो | delivered cell |
| getenv | दो_पर्या | delivered cell |
| gets | माला_लो | delivered cell |
| gettime | समय_लो | delivered cell |
| gmtime | स_जमट | delivered cell |
| isalnum | है_अक्षर_अंक | delivered cell |
| isalpha | है_अक्षर | delivered cell |
| iscntrl | है_नियंत्रण | delivered cell |
| isdigit | है_अंक | delivered cell |
| isfinite | है_सीमित | delivered cell |
| isgraph | है_चित्र | delivered cell |
| islower | है_छोटा | delivered cell |
| isodigit | है_अष्टक | delivered cell |
| isprint | है_छाप | delivered cell |
| ispunct | है_विराम | delivered cell |
| isspace | है_खाली | delivered cell |
| isupper | है_बड़ा | delivered cell |
| isxdigit | है_षष्ठादशक | delivered cell |
| jmp_buf | लाँघ_बफ | delivered cell |
| kill | समाप्त | delivered cell |
| labs | द_असल | delivered cell |
| lconv | स्था_बदल | delivered cell |
| ldiv | द_भाग | delivered cell |
| ldiv_t | द_भाग_प्रकार | delivered cell |
| localeconv | क्षेत्र_बदलो | delivered cell |
| localtime | स_स्थानीय | delivered cell |
| longjmp | दीर्घ_लाँघ | delivered cell |
| malloc | दो_स्मृति | delivered cell |
| memchr | स_प्रथम | delivered cell |
| memcmp | स_भेद | delivered cell |
| memcpy | स_नकल | delivered cell |
| memmove | स_हटाओ | delivered cell |
| memset | स_रखो | delivered cell |
| mkdir | सूची_गढ़ो | delivered cell |
| mktime | स_गढ़ो | delivered cell |
| offsetof | दुरत्व | delivered cell |
| open | खोलो | delivered cell |
| opendir | सूची_खोलो | delivered cell |
| pause | छोड़ो | delivered cell |
| perror | लिखो_त्रुटि | delivered cell |
| pipe | प्रणाल | lexicon |
| pow | घात | delivered cell |
| printf | म_लिखो | delivered cell |
| ptrdiff_t | सूचक_भेद_प्रकार | delivered cell |
| putc | अ_दो | delivered cell |
| putchar | अक्षर_दो | delivered cell |
| puts | माला_दो | delivered cell |
| qsort | क्विक | delivered cell |
| raise | उत्थापय | lexicon |
| rand | अक्रम | delivered cell |
| read | पठ | lexicon |
| readdir | सूची_पढ़ो | delivered cell |
| realloc | पुनः_स्मृति | delivered cell |
| remove | हटाओ | delivered cell |
| rename | नाम | delivered cell |
| rewind | शुरुआत | delivered cell |
| rewinddir | सूची_शुरु | delivered cell |
| rmdir | सूची_हटाओ | delivered cell |
| scanf | म_पूछो | delivered cell |
| setbuf | रखो_बफ | delivered cell |
| setjmp | बनाओ_लाँघ | delivered cell |
| setlocale | रखो_क्षेत्र | delivered cell |
| settime | समय_रखो | delivered cell |
| setvbuf | रखो_भबफ | delivered cell |
| sig_atomic_t | संक_पूर्ण_प्रकार | delivered cell |
| signal | सङ्केत | lexicon |
| sigpending | संक_बाकी | delivered cell |
| sigsuspend | संक_रोको | delivered cell |
| size_t | माप_प्रकार | delivered cell |
| sleep | सुषुप्ति | lexicon |
| sprintf | प्र_लिखो | delivered cell |
| sqrt | वर्ग_मूल | delivered cell |
| srand | बेक्रम | delivered cell |
| sscanf | माला_पूछो | delivered cell |
| stderr | मानक_त्रुटि | delivered cell |
| stdin | मानक_निवेश | delivered cell |
| stdout | मानक_निकास | delivered cell |
| strcat | म_जोड़ो | delivered cell |
| strchr | म_अक्षर | delivered cell |
| strcmp | म_भेद | delivered cell |
| strcpy | म_नकल | delivered cell |
| strcspn | म_खोज | delivered cell |
| strerror | म_त्रुटि | delivered cell |
| strftime | स_माला | delivered cell |
| strlen | म_माप | delivered cell |
| strncat | म_जोड़न | delivered cell |
| strncmp | म_भेदन | delivered cell |
| strncpy | म_नकलन | delivered cell |
| strrchr | म_खोजप | delivered cell |
| strspn | म_अखोज | delivered cell |
| strstr | म_माला | delivered cell |
| strtod | म_से_भग्न | delivered cell |
| strtok | म_मोहर | delivered cell |
| strtol | म_से_दीर्घ | delivered cell |
| strtoul | म_से_अदीर्घ | delivered cell |
| sync | समकाल | lexicon |
| system | प्रणाली | delivered cell |
| time | समय | delivered cell |
| time_t | समय_प्रकार | delivered cell |
| times | बार | delivered cell |
| tm | पंचांग | delivered cell |
| tmpfile | क्षणिक_ख | delivered cell |
| tmpnam | क्षणिक | delivered cell |
| tolower | छोटे | delivered cell |
| toupper | बड़े | delivered cell |
| ungetc | अक्षर_वापस | delivered cell |
| va_arg | बहु_तर्क | delivered cell |
| va_end | बहु_पूर्ण | delivered cell |
| va_list | बहु_सूची | delivered cell |
| va_start | बहु_शुरू | delivered cell |
| vfprintf | भख_लिखो | delivered cell |
| vprintf | भ_लिखो | delivered cell |
| vsprintf | भम_लिखो | delivered cell |
| wait | रुको | delivered cell |
| wchar_t | ब_अक्षर_प्रकार | delivered cell |
| write | लिख | lexicon |

### A.4 Java

Host: The Java Language Specification, Oracle, current edition. Names: unchanged.

| Host | Nepali | Source |
|---|---|---|
| abstract | अमूर्त | lexicon |
| assert | प्रतिज्ञा | lexicon |
| boolean | boolean | host form (no native word yet) |
| break | रोक | lexicon |
| byte | byte | host form (no native word yet) |
| case | पक्ष | lexicon |
| catch | गृहाण | lexicon |
| char | वर्ण | lexicon |
| class | वर्ग | lexicon |
| continue | जारी | lexicon |
| default | स्वभाव | lexicon |
| do | गर | lexicon |
| double | द्विगुण | lexicon |
| else | अन्यथा | lexicon |
| enum | गणना | lexicon |
| extends | विस्तृत | lexicon |
| final | final | host form (no native word yet) |
| finally | अन्ततः | lexicon |
| float | भिन्न | lexicon |
| for | लागि | lexicon |
| if | यदि | lexicon |
| implements | निष्पादित | lexicon |
| import | आनयन | lexicon |
| instanceof | instanceof | host form (no native word yet) |
| int | पूर्णाङ्क | lexicon |
| interface | सन्धि | lexicon |
| long | दीर्घ | delivered cell |
| native | native | host form (no native word yet) |
| new | नूतन | lexicon |
| package | पुटक | lexicon |
| private | गुप्त | lexicon |
| protected | रक्षित | lexicon |
| public | सार्वजनिक | lexicon |
| return | फर्काऊ | lexicon |
| short | लघु | delivered cell |
| static | स्थिर | lexicon |
| super | पर | lexicon |
| switch | विकल्प | lexicon |
| synchronized | समकाल | delivered cell |
| this | एतत् | lexicon |
| throw | क्षिप | lexicon |
| throws | throws | host form (no native word yet) |
| try | यत्न | lexicon |
| void | शून्य | lexicon |
| volatile | चञ्चल | lexicon |
| while | जबसम्म | lexicon |
| true | सत्य | lexicon |
| false | असत्य | lexicon |
| null | रिक्त | lexicon |
| String | पदावली | lexicon |
| System | प्रणाली | lexicon |

Standard library and runtime names of the Java binding:

| Host | Nepali | Source |
|---|---|---|
| BUFSIZ | बफ_मान | delivered cell |
| CHAR_BIT | अक्षर_बिट | delivered cell |
| CHAR_MAX | अक्षर_उच्च | delivered cell |
| CHAR_MIN | अक्षर_न्यून | delivered cell |
| CHILD_MAX | शिशु_उच्च | delivered cell |
| CLK_TCK | घड़ी_टिक | delivered cell |
| DBL_DIG | द्विग_भग्न | delivered cell |
| DBL_EPSILON | द्विग_अंतर | delivered cell |
| DBL_MANT_DIG | द्विग_पूर्ण | delivered cell |
| DBL_MAX | द्विग_उच्च | delivered cell |
| DBL_MIN | द्विग_न्यून | delivered cell |
| DIR | सूची | delivered cell |
| EDOM | गलत_तर्क | delivered cell |
| EOF | खातापूर्ण | delivered cell |
| ERANGE | दुस्फल | delivered cell |
| EXIT_FAILURE | निकास_त्रुटि | delivered cell |
| EXIT_SUCCESS | निकास_सफल | delivered cell |
| FILE | खाता | delivered cell |
| FILENAME_MAX | खातानाम_उच्च | delivered cell |
| FLT_DIG | भग्न_भग्न | delivered cell |
| FLT_EPSILON | भग्न_अंतर | delivered cell |
| FLT_MANT_DIG | भग्न_पूर्ण | delivered cell |
| FLT_MAX | भग्न_उच्च | delivered cell |
| FLT_MIN | भग्न_न्यून | delivered cell |
| FLT_RADIX | भग्न_आधार | delivered cell |
| FOPEN_MAX | ख_खोलो_उच्च | delivered cell |
| HUGE_VAL | विशाल_मान | delivered cell |
| INFINITY | अनन्त | delivered cell |
| INT_MAX | पूर्णांक_उच्च | delivered cell |
| INT_MIN | पूर्णांक_न्यून | delivered cell |
| LDBL_DIG | द_द्वि_भग्न | delivered cell |
| LDBL_EPSILON | द_द्वि_अंतर | delivered cell |
| LDBL_MANT_DIG | द_द्वि_पूर्ण | delivered cell |
| LDBL_MAX | द_द्वि_उच्च | delivered cell |
| LDBL_MIN | द_द्वि_न्यून | delivered cell |
| LONG_MAX | दीर्घ_उच्च | delivered cell |
| LONG_MIN | दीर्घ_न्यून | delivered cell |
| L_tmpnam | ब_क्षणिक | delivered cell |
| NAN | न_अंक | delivered cell |
| NDEBUG | न_संशोधन | delivered cell |
| Object | वस्तु | lexicon |
| RAND_MAX | अक्रम_उच्च | delivered cell |
| SCHAR_MAX | च_अक्षर_उच्च | delivered cell |
| SCHAR_MIN | च_अक्षर_न्यून | delivered cell |
| SEEK_CUR | प्रस्तुत_से | delivered cell |
| SEEK_END | अंत_से | delivered cell |
| SEEK_SET | शुरू_से | delivered cell |
| SHRT_MAX | लघु_उच्च | delivered cell |
| SHRT_MIN | लघु_न्यून | delivered cell |
| SIBGABRT | संक_पात | delivered cell |
| SIGFPE | संक_भ_त्रुटि | delivered cell |
| SIGILL | संक_अवैध | delivered cell |
| SIGINT | संक_विघ्न | delivered cell |
| SIGSEGV | संक_अंश | delivered cell |
| SIGTERM | संक_इति | delivered cell |
| SIG_DFL | संक_पूर्व | delivered cell |
| SIG_ERR | संक_त्रुटि | delivered cell |
| SIG_IGN | संक_छोड़ो | delivered cell |
| TMP_MAX | क्षणिक_उच्च | delivered cell |
| Thread | तन्तु | lexicon |
| UCHAR_MAX | अच_अक्षर_उच्च | delivered cell |
| UINT_MAX | अच_पूर्णांक_उच्च | delivered cell |
| ULONG_MAX | अच_दीर्घ_उच्च | delivered cell |
| USHRT_MAX | अच_लघु_उच्च | delivered cell |
| __DATE__ | __दिन__ | delivered cell |
| __FILE__ | __खाता__ | delivered cell |
| __LINE__ | __पंक्ति__ | delivered cell |
| __STDC__ | __मानक__ | delivered cell |
| __TIME__ | __समय__ | delivered cell |
| abort | पात | delivered cell |
| abs | असल | delivered cell |
| asctime | समय_ठीक | delivered cell |
| asm | यंत्र | delivered cell |
| atexit | निकास_पर | delivered cell |
| atof | म_से_भ | delivered cell |
| atoi | म_से_प | delivered cell |
| atol | म_से_द | delivered cell |
| auto | स्वतः | delivered cell |
| bsearch | द्वा_खोज | delivered cell |
| calloc | सुस्मृति | delivered cell |
| ceil | उच्चमान | delivered cell |
| chdir | स_बदलो | delivered cell |
| clearerr | साफ_त्रुटि | delivered cell |
| clock | घड़ी | delivered cell |
| clock_t | घड़ी_प्रकार | delivered cell |
| close | बंद | delivered cell |
| closedir | बंद_सूची | delivered cell |
| const | अचर | lexicon |
| ctime | स_समय | delivered cell |
| difftime | स_अंतर | delivered cell |
| dirname | स_नाम | delivered cell |
| div | भाग | delivered cell |
| div_t | भाग_प्रकार | delivered cell |
| errno | त्रुटि_सं | delivered cell |
| exit | निकास | delivered cell |
| extern | बाह्य | lexicon |
| fabs | भ_असल | delivered cell |
| fclose | ख_बंद | delivered cell |
| feof | ख_पूर्ण | delivered cell |
| ferror | ख_त्रुटि | delivered cell |
| fflush | ख_साफ | delivered cell |
| fgetc | ख_अक्षर_लो | delivered cell |
| fgetpos | ख_स्थान_लो | delivered cell |
| fgets | ख_माला_लो | delivered cell |
| floor | न्यूनमान | delivered cell |
| fmod | भ_शेष | delivered cell |
| fopen | ख_खोलो | delivered cell |
| fork | विभाजन | delivered cell |
| fpos_t | ख_स्थान_प्रकार | delivered cell |
| fprintf | ख_लिखो | delivered cell |
| fputc | ख_अक्षर_दो | delivered cell |
| fputs | ख_माला_दो | delivered cell |
| fread | ख_पढ़ो | delivered cell |
| free | मुक्त | lexicon |
| freopen | ख_व_खोलो | delivered cell |
| friend | मित्र | delivered cell |
| fscanf | ख_पूछो | delivered cell |
| fseek | ख_जाओ | delivered cell |
| fsetpos | ख_स्थान_दो | delivered cell |
| fstat | ख_स्थिति | delivered cell |
| ftell | ख_बताओ | delivered cell |
| fwrite | ख_डालो | delivered cell |
| getc | अ_लो | delivered cell |
| getchar | अक्षर_लो | delivered cell |
| getenv | दो_पर्या | delivered cell |
| gets | माला_लो | delivered cell |
| gettime | समय_लो | delivered cell |
| gmtime | स_जमट | delivered cell |
| goto | गच्छ | lexicon |
| inline | अन्तःस्थ | lexicon |
| isalnum | है_अक्षर_अंक | delivered cell |
| isalpha | है_अक्षर | delivered cell |
| iscntrl | है_नियंत्रण | delivered cell |
| isdigit | है_अंक | delivered cell |
| isfinite | है_सीमित | delivered cell |
| isgraph | है_चित्र | delivered cell |
| islower | है_छोटा | delivered cell |
| isodigit | है_अष्टक | delivered cell |
| isprint | है_छाप | delivered cell |
| ispunct | है_विराम | delivered cell |
| isspace | है_खाली | delivered cell |
| isupper | है_बड़ा | delivered cell |
| isxdigit | है_षष्ठादशक | delivered cell |
| jmp_buf | लाँघ_बफ | delivered cell |
| kill | समाप्त | delivered cell |
| labs | द_असल | delivered cell |
| lconv | स्था_बदल | delivered cell |
| ldiv | द_भाग | delivered cell |
| ldiv_t | द_भाग_प्रकार | delivered cell |
| localeconv | क्षेत्र_बदलो | delivered cell |
| localtime | स_स्थानीय | delivered cell |
| longjmp | दीर्घ_लाँघ | delivered cell |
| malloc | दो_स्मृति | delivered cell |
| memchr | स_प्रथम | delivered cell |
| memcmp | स_भेद | delivered cell |
| memcpy | स_नकल | delivered cell |
| memmove | स_हटाओ | delivered cell |
| memset | स_रखो | delivered cell |
| mkdir | सूची_गढ़ो | delivered cell |
| mktime | स_गढ़ो | delivered cell |
| offsetof | दुरत्व | delivered cell |
| open | खोलो | delivered cell |
| opendir | सूची_खोलो | delivered cell |
| operator | चालक | delivered cell |
| pause | छोड़ो | delivered cell |
| perror | लिखो_त्रुटि | delivered cell |
| pow | घात | delivered cell |
| printf | म_लिखो | delivered cell |
| ptrdiff_t | सूचक_भेद_प्रकार | delivered cell |
| putc | अ_दो | delivered cell |
| putchar | अक्षर_दो | delivered cell |
| puts | माला_दो | delivered cell |
| qsort | क्विक | delivered cell |
| raise | उत्थापय | lexicon |
| rand | अक्रम | delivered cell |
| read | पठ | lexicon |
| readdir | सूची_पढ़ो | delivered cell |
| realloc | पुनः_स्मृति | delivered cell |
| register | पञ्जिका | lexicon |
| remove | हटाओ | delivered cell |
| rename | नाम | delivered cell |
| rewind | शुरुआत | delivered cell |
| rewinddir | सूची_शुरु | delivered cell |
| rmdir | सूची_हटाओ | delivered cell |
| scanf | म_पूछो | delivered cell |
| setbuf | रखो_बफ | delivered cell |
| setjmp | बनाओ_लाँघ | delivered cell |
| setlocale | रखो_क्षेत्र | delivered cell |
| settime | समय_रखो | delivered cell |
| setvbuf | रखो_भबफ | delivered cell |
| sig_atomic_t | संक_पूर्ण_प्रकार | delivered cell |
| signal | सङ्केत | lexicon |
| signed | चिन्हित | delivered cell |
| sigpending | संक_बाकी | delivered cell |
| sigsuspend | संक_रोको | delivered cell |
| size_t | माप_प्रकार | delivered cell |
| sizeof | परिमाण | lexicon |
| sleep | सुषुप्ति | lexicon |
| sprintf | प्र_लिखो | delivered cell |
| sqrt | वर्ग_मूल | delivered cell |
| srand | बेक्रम | delivered cell |
| sscanf | माला_पूछो | delivered cell |
| stderr | मानक_त्रुटि | delivered cell |
| stdin | मानक_निवेश | delivered cell |
| stdout | मानक_निकास | delivered cell |
| strcat | म_जोड़ो | delivered cell |
| strchr | म_अक्षर | delivered cell |
| strcmp | म_भेद | delivered cell |
| strcpy | म_नकल | delivered cell |
| strcspn | म_खोज | delivered cell |
| strerror | म_त्रुटि | delivered cell |
| strftime | स_माला | delivered cell |
| strlen | म_माप | delivered cell |
| strncat | म_जोड़न | delivered cell |
| strncmp | म_भेदन | delivered cell |
| strncpy | म_नकलन | delivered cell |
| strrchr | म_खोजप | delivered cell |
| strspn | म_अखोज | delivered cell |
| strstr | म_माला | delivered cell |
| strtod | म_से_भग्न | delivered cell |
| strtok | म_मोहर | delivered cell |
| strtol | म_से_दीर्घ | delivered cell |
| strtoul | म_से_अदीर्घ | delivered cell |
| struct | संरचना | lexicon |
| system | प्रणाली | delivered cell |
| template | ढाँचा | delivered cell |
| time | समय | delivered cell |
| time_t | समय_प्रकार | delivered cell |
| times | बार | delivered cell |
| tm | पंचांग | delivered cell |
| tmpfile | क्षणिक_ख | delivered cell |
| tmpnam | क्षणिक | delivered cell |
| tolower | छोटे | delivered cell |
| toupper | बड़े | delivered cell |
| typedef | प्रकारनिर्देश | lexicon |
| ungetc | अक्षर_वापस | delivered cell |
| union | सङ्घ | lexicon |
| unsigned | अचिन्हित | delivered cell |
| va_arg | बहु_तर्क | delivered cell |
| va_end | बहु_पूर्ण | delivered cell |
| va_list | बहु_सूची | delivered cell |
| va_start | बहु_शुरू | delivered cell |
| vfprintf | भख_लिखो | delivered cell |
| virtual | आभास | lexicon |
| vprintf | भ_लिखो | delivered cell |
| vsprintf | भम_लिखो | delivered cell |
| wait | रुको | delivered cell |
| wchar_t | ब_अक्षर_प्रकार | delivered cell |
| write | लिख | lexicon |

### A.5 Python

Host: The Python Language Reference, Python Software Foundation, current version. Names: unchanged.

| Host | Nepali | Source |
|---|---|---|
| False | असत्य | lexicon |
| None | None | host form (no native word yet) |
| True | सत्य | lexicon |
| and | र | lexicon |
| as | इव | lexicon |
| assert | प्रतिज्ञा | lexicon |
| break | रोक | lexicon |
| class | वर्ग | lexicon |
| continue | जारी | lexicon |
| def | def | host form (no native word yet) |
| del | del | host form (no native word yet) |
| elif | अथवायदि | lexicon |
| else | अन्यथा | lexicon |
| except | अपवाद | lexicon |
| finally | अन्ततः | lexicon |
| for | लागि | lexicon |
| from | तः | lexicon |
| global | वैश्विक | lexicon |
| if | यदि | lexicon |
| import | आनयन | lexicon |
| in | अन्तः | lexicon |
| is | is | host form (no native word yet) |
| lambda | अनामन् | lexicon |
| nonlocal | nonlocal | host form (no native word yet) |
| not | होइन | lexicon |
| or | वा | lexicon |
| pass | pass | host form (no native word yet) |
| raise | उत्थापय | lexicon |
| return | फर्काऊ | lexicon |
| try | यत्न | lexicon |
| while | जबसम्म | lexicon |
| with | with | host form (no native word yet) |
| yield | दा | lexicon |
| print | print | host form (no native word yet) |
| range | range | host form (no native word yet) |
| len | len | host form (no native word yet) |

Standard library and runtime names of the Python binding:

| Host | Nepali | Source |
|---|---|---|
| Object | वस्तु | lexicon |
| String | पदावली | lexicon |
| Thread | तन्तु | lexicon |
| abstract | अमूर्त | lexicon |
| case | पक्ष | lexicon |
| catch | गृहाण | lexicon |
| char | वर्ण | lexicon |
| close | बंद | delivered cell |
| const | अचर | lexicon |
| default | स्वभाव | lexicon |
| do | गर | lexicon |
| double | द्विगुण | lexicon |
| extends | विस्तृत | lexicon |
| float | भिन्न | lexicon |
| goto | गच्छ | lexicon |
| implements | निष्पादित | lexicon |
| int | पूर्णाङ्क | lexicon |
| interface | सन्धि | lexicon |
| long | दीर्घ | delivered cell |
| new | नूतन | lexicon |
| package | पुटक | lexicon |
| private | गुप्त | lexicon |
| protected | रक्षित | lexicon |
| public | सार्वजनिक | lexicon |
| rand | अक्रम | delivered cell |
| read | पठ | lexicon |
| short | लघु | delivered cell |
| sleep | सुषुप्ति | lexicon |
| sqrt | वर्ग_मूल | delivered cell |
| static | स्थिर | lexicon |
| super | पर | lexicon |
| switch | विकल्प | lexicon |
| this | एतत् | lexicon |
| throw | क्षिप | lexicon |
| void | शून्य | lexicon |
| volatile | चञ्चल | lexicon |
| wait | रुको | delivered cell |
| write | लिख | lexicon |

### A.6 BASIC

Host: ISO/IEC 10279, Information technology, Programming languages, Full BASIC. Names: name transformation.

| Host | Nepali | Source |
|---|---|---|
| dim | dim | host form (no native word yet) |
| end | अन्त्य | lexicon |
| for | लागि | lexicon |
| gosub | gosub | host form (no native word yet) |
| goto | गच्छ | lexicon |
| if | यदि | lexicon |
| input | input | host form (no native word yet) |
| let | अस्तु | lexicon |
| next | next | host form (no native word yet) |
| print | print | host form (no native word yet) |
| rem | rem | host form (no native word yet) |
| return | फर्काऊ | lexicon |
| step | step | host form (no native word yet) |
| then | then | host form (no native word yet) |
| to | to | host form (no native word yet) |
| wend | wend | host form (no native word yet) |
| while | जबसम्म | lexicon |
| and | र | lexicon |
| or | वा | lexicon |
| not | होइन | lexicon |
| mod | mod | host form (no native word yet) |

Standard library and runtime names of the BASIC binding:

| Host | Nepali | Source |
|---|---|---|
| AS | इव | lexicon |
| CALL | आह्वान | lexicon |
| CONST | अचर | lexicon |
| DO | गर | lexicon |
| ELSE | अन्यथा | lexicon |
| EOF | खातापूर्ण | delivered cell |
| INT | पूर्णाङ्क | lexicon |
| SHARED | सहभाजित | lexicon |
| STATIC | स्थिर | lexicon |
| STRING | पदावली | lexicon |
| TIMER | कालयन्त्र | lexicon |

### A.7 LOGO

Host: No international standard; the host is the Berkeley Logo dialect (bibliography). Names: name transformation.

| Host | Nepali | Source |
|---|---|---|
| forward | अग्रप्रसार | lexicon |
| back | back | host form (no native word yet) |
| left | left | host form (no native word yet) |
| right | right | host form (no native word yet) |
| penup | penup | host form (no native word yet) |
| pendown | pendown | host form (no native word yet) |
| repeat | repeat | host form (no native word yet) |
| to | to | host form (no native word yet) |
| end | अन्त्य | lexicon |
| make | make | host form (no native word yet) |
| if | यदि | lexicon |
| ifelse | ifelse | host form (no native word yet) |
| home | home | host form (no native word yet) |
| clearscreen | clearscreen | host form (no native word yet) |

## Annex B (informative) Coverage and review

| Binding | Host keywords with a native word | Library names |
|---|---|---|
| C | 33 of 35 | 239 |
| C preprocessor | 4 of 12 | 0 |
| C++ | 50 of 61 | 235 |
| Java | 45 of 51 | 249 |
| Python | 26 of 36 | 38 |
| BASIC | 10 of 21 | 11 |
| LOGO | 3 of 14 | 0 |

The lowering of Nepali programs to C is verified by the reference implementation: runs, same output. Source Chintamani means a word of the original Hindawi transducers; lexicon, a word of the language's lexicon; proposed, a word proposed by the project and not yet reviewed by the language community.

## Annex C (normative) Script filter

Devanagari text passes to Romenagri without a script filter.

## Annex D (informative) Rights and provenance

This document is an original work. It defines new programming languages by reference to the host language standards listed in Clause 2 and reproduces no text from them. Permission to adopt, translate or publish it as a standard is given by the copyright holder to a standards body on request.

Single words and the keywords of the host languages are not reproduced from any copyrighted text; the native words of Annex A were chosen by the Hindawi project, taken from the language's lexicon in the Hindawi repository, or, for Hindi, taken from the Chintamani transducers of the original Hindawi, whose author holds their copyright.

## Bibliography

- Hindawi 2026.10, hindawiai/hindawi2026.10, the reference implementation
- Chintamani, hindawiai/chintamani, the Hindawi transducers and the Romenagri tools
- Berkeley Logo reference manual, Brian Harvey

