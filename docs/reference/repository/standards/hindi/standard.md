# HLS hi 2026.10

**Hindi bindings for programming languages: lexical mapping and lowering to the host standards**

Edition 2026.10, working draft, 2026-10-18. © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

## Foreword

This document was prepared by AyeAI, Hindawi project (Project ILM). It is generated from the Hindi cell of Hindawi 2026.10 by lang/hindawi/tools/standards.py, so that the published standard and the reference implementation cannot drift apart. Its stage is a working draft: the words marked proposed in Annex A await review by the Hindi language community, through the review pages of the Hindawi project.

## Introduction

This document lets programs be written in Hindi, in the Devanagari script, in each of the programming languages listed in Clause 1. Each binding is a programming language in its own right, Hindi C for example, whose programs are lowered by the function defined in Clause 6 to programs of the host language, and are then processed by any conforming implementation of the host standard. The host standards are incorporated by reference and are not restated. Names keep a defined form down to object code (Clause 7), so programs written in Hindi remain debuggable at the level of firmware, kernels and libraries.

## 1 Scope

This document specifies, for the Hindi language written in the Devanagari script, bindings to the following host programming languages: C, C preprocessor, C++, Java, Python, BASIC, LOGO. For each binding it specifies the native keywords and directives, the lowering of native programs to host programs, the treatment of names, and the requirements for conformance.

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

- binding: programming language defined by this document whose programs are written in Hindi and lowered to one host language

- native keyword: word of this document that stands for one keyword, directive or standard library name of a host language

- lowering: function from native programs to host programs defined in Clause 6

- raising: inverse of lowering applied to a host program with a dictionary of names, giving back the native program exactly

- name transformation: function from native names to host identifiers defined in Clause 7

- C-level form: result of the name transformation; the form a native name takes in host source and in object code

## 4 Conformance

A conforming Hindi program of a binding shall be a text that meets Clause 5 and whose lowering is a conforming program of the host language.

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

| Host | Hindi | Source |
|---|---|---|
| auto | स्वतः | Chintamani |
| break | अवरोध | Chintamani |
| case | हाल | Chintamani |
| char | अक्षर | Chintamani |
| const | स्थिर | Chintamani |
| continue | जारी | Chintamani |
| default | शेष | Chintamani |
| do | करो | Chintamani |
| double | द्विगुन | Chintamani |
| else | अन्यथा | Chintamani |
| enum | क्रमागत | Chintamani |
| extern | बाह्य | Chintamani |
| float | भग्न | Chintamani |
| for | क्रम | Chintamani |
| goto | जाओ | Chintamani |
| if | अगर | Chintamani |
| inline | अंतरभूत | Chintamani |
| int | पूर्णांक | Chintamani |
| long | दीर्घ | Chintamani |
| register | रेजिस्टर | Chintamani |
| restrict | restrict | host form (no native word yet) |
| return | वापस | Chintamani |
| short | लघु | Chintamani |
| signed | चिन्हित | Chintamani |
| sizeof | माप | Chintamani |
| static | अटल | Chintamani |
| struct | काष्ठा | Chintamani |
| switch | चयन | Chintamani |
| typedef | प्रकार | Chintamani |
| union | जोड़ | Chintamani |
| unsigned | अचिन्हित | Chintamani |
| void | व्योम | Chintamani |
| volatile | अस्थिर | Chintamani |
| while | जबतक | Chintamani |
| main | मुख्य | Chintamani |

Standard library and runtime names of the C binding:

| Host | Hindi | Source |
|---|---|---|
| BUFSIZ | बफ_मान | Chintamani |
| CHAR_BIT | अक्षर_बिट | Chintamani |
| CHAR_MAX | अक्षर_उच्च | Chintamani |
| CHAR_MIN | अक्षर_न्यून | Chintamani |
| CHILD_MAX | शिशु_उच्च | Chintamani |
| CLK_TCK | घड़ी_टिक | Chintamani |
| DBL_DIG | द्विग_भग्न | Chintamani |
| DBL_EPSILON | द्विग_अंतर | Chintamani |
| DBL_MANT_DIG | द्विग_पूर्ण | Chintamani |
| DBL_MAX | द्विग_उच्च | Chintamani |
| DBL_MIN | द्विग_न्यून | Chintamani |
| DIR | सूची | Chintamani |
| EDOM | गलत_तर्क | Chintamani |
| EOF | खातापूर्ण | Chintamani |
| ERANGE | दुस्फल | Chintamani |
| EXIT_FAILURE | निकास_त्रुटि | Chintamani |
| EXIT_SUCCESS | निकास_सफल | Chintamani |
| FILE | खाता | Chintamani |
| FILENAME_MAX | खातानाम_उच्च | Chintamani |
| FLT_DIG | भग्न_भग्न | Chintamani |
| FLT_EPSILON | भग्न_अंतर | Chintamani |
| FLT_MANT_DIG | भग्न_पूर्ण | Chintamani |
| FLT_MAX | भग्न_उच्च | Chintamani |
| FLT_MIN | भग्न_न्यून | Chintamani |
| FLT_RADIX | भग्न_आधार | Chintamani |
| FOPEN_MAX | ख_खोलो_उच्च | Chintamani |
| HUGE_VAL | विशाल_मान | Chintamani |
| INFINITY | अनन्त | Chintamani |
| INT_MAX | पूर्णांक_उच्च | Chintamani |
| INT_MIN | पूर्णांक_न्यून | Chintamani |
| LDBL_DIG | द_द्वि_भग्न | Chintamani |
| LDBL_EPSILON | द_द्वि_अंतर | Chintamani |
| LDBL_MANT_DIG | द_द्वि_पूर्ण | Chintamani |
| LDBL_MAX | द_द्वि_उच्च | Chintamani |
| LDBL_MIN | द_द्वि_न्यून | Chintamani |
| LONG_MAX | दीर्घ_उच्च | Chintamani |
| LONG_MIN | दीर्घ_न्यून | Chintamani |
| L_tmpnam | ब_क्षणिक | Chintamani |
| NAN | न_अंक | Chintamani |
| NDEBUG | न_संशोधन | Chintamani |
| NULL | शून्य | Chintamani |
| RAND_MAX | अक्रम_उच्च | Chintamani |
| SCHAR_MAX | च_अक्षर_उच्च | Chintamani |
| SCHAR_MIN | च_अक्षर_न्यून | Chintamani |
| SEEK_CUR | प्रस्तुत_से | Chintamani |
| SEEK_END | अंत_से | Chintamani |
| SEEK_SET | शुरू_से | Chintamani |
| SHRT_MAX | लघु_उच्च | Chintamani |
| SHRT_MIN | लघु_न्यून | Chintamani |
| SIBGABRT | संक_पात | Chintamani |
| SIGFPE | संक_भ_त्रुटि | Chintamani |
| SIGILL | संक_अवैध | Chintamani |
| SIGINT | संक_विघ्न | Chintamani |
| SIGSEGV | संक_अंश | Chintamani |
| SIGTERM | संक_इति | Chintamani |
| SIG_DFL | संक_पूर्व | Chintamani |
| SIG_ERR | संक_त्रुटि | Chintamani |
| SIG_IGN | संक_छोड़ो | Chintamani |
| TMP_MAX | क्षणिक_उच्च | Chintamani |
| UCHAR_MAX | अच_अक्षर_उच्च | Chintamani |
| UINT_MAX | अच_पूर्णांक_उच्च | Chintamani |
| ULONG_MAX | अच_दीर्घ_उच्च | Chintamani |
| USHRT_MAX | अच_लघु_उच्च | Chintamani |
| __DATE__ | __दिन__ | Chintamani |
| __FILE__ | __खाता__ | Chintamani |
| __LINE__ | __पंक्ति__ | Chintamani |
| __STDC__ | __मानक__ | Chintamani |
| __TIME__ | __समय__ | Chintamani |
| _exit | _निकास | Chintamani |
| abort | पात | Chintamani |
| abs | असल | Chintamani |
| asctime | समय_ठीक | Chintamani |
| asm | यंत्र | Chintamani |
| assert | निश्चित | Chintamani |
| atexit | निकास_पर | Chintamani |
| atof | म_से_भ | Chintamani |
| atoi | म_से_प | Chintamani |
| atol | म_से_द | Chintamani |
| bsearch | द्वा_खोज | Chintamani |
| calloc | सुस्मृति | Chintamani |
| ceil | उच्चमान | Chintamani |
| chdir | स_बदलो | Chintamani |
| clearerr | साफ_त्रुटि | Chintamani |
| clock | घड़ी | Chintamani |
| clock_t | घड़ी_प्रकार | Chintamani |
| close | बंद | Chintamani |
| closedir | बंद_सूची | Chintamani |
| ctime | स_समय | Chintamani |
| difftime | स_अंतर | Chintamani |
| dirname | स_नाम | Chintamani |
| div | भाग | Chintamani |
| div_t | भाग_प्रकार | Chintamani |
| errno | त्रुटि_सं | Chintamani |
| exit | निकास | Chintamani |
| fabs | भ_असल | Chintamani |
| fclose | ख_बंद | Chintamani |
| feof | ख_पूर्ण | Chintamani |
| ferror | ख_त्रुटि | Chintamani |
| fflush | ख_साफ | Chintamani |
| fgetc | ख_अक्षर_लो | Chintamani |
| fgetpos | ख_स्थान_लो | Chintamani |
| fgets | ख_माला_लो | Chintamani |
| floor | न्यूनमान | Chintamani |
| fmod | भ_शेष | Chintamani |
| fopen | ख_खोलो | Chintamani |
| fork | विभाजन | Chintamani |
| fpos_t | ख_स्थान_प्रकार | Chintamani |
| fprintf | ख_लिखो | Chintamani |
| fputc | ख_अक्षर_दो | Chintamani |
| fputs | ख_माला_दो | Chintamani |
| fread | ख_पढ़ो | Chintamani |
| free | मुक्त | Chintamani |
| freopen | ख_व_खोलो | Chintamani |
| friend | मित्र | Chintamani |
| fscanf | ख_पूछो | Chintamani |
| fseek | ख_जाओ | Chintamani |
| fsetpos | ख_स्थान_दो | Chintamani |
| fstat | ख_स्थिति | Chintamani |
| ftell | ख_बताओ | Chintamani |
| fwrite | ख_डालो | Chintamani |
| getc | अ_लो | Chintamani |
| getchar | अक्षर_लो | Chintamani |
| getenv | दो_पर्या | Chintamani |
| gets | माला_लो | Chintamani |
| gettime | समय_लो | Chintamani |
| gmtime | स_जमट | Chintamani |
| isalnum | है_अक्षर_अंक | Chintamani |
| isalpha | है_अक्षर | Chintamani |
| iscntrl | है_नियंत्रण | Chintamani |
| isdigit | है_अंक | Chintamani |
| isfinite | है_सीमित | Chintamani |
| isgraph | है_चित्र | Chintamani |
| islower | है_छोटा | Chintamani |
| isodigit | है_अष्टक | Chintamani |
| isprint | है_छाप | Chintamani |
| ispunct | है_विराम | Chintamani |
| isspace | है_खाली | Chintamani |
| isupper | है_बड़ा | Chintamani |
| isxdigit | है_षष्ठादशक | Chintamani |
| jmp_buf | लाँघ_बफ | Chintamani |
| kill | समाप्त | Chintamani |
| labs | द_असल | Chintamani |
| lconv | स्था_बदल | Chintamani |
| ldiv | द_भाग | Chintamani |
| ldiv_t | द_भाग_प्रकार | Chintamani |
| localeconv | क्षेत्र_बदलो | Chintamani |
| localtime | स_स्थानीय | Chintamani |
| longjmp | दीर्घ_लाँघ | Chintamani |
| malloc | दो_स्मृति | Chintamani |
| memchr | स_प्रथम | Chintamani |
| memcmp | स_भेद | Chintamani |
| memcpy | स_नकल | Chintamani |
| memmove | स_हटाओ | Chintamani |
| memset | स_रखो | Chintamani |
| mkdir | सूची_गढ़ो | Chintamani |
| mktime | स_गढ़ो | Chintamani |
| offsetof | दुरत्व | Chintamani |
| open | खोलो | Chintamani |
| opendir | सूची_खोलो | Chintamani |
| operator | चालक | Chintamani |
| pause | छोड़ो | Chintamani |
| perror | लिखो_त्रुटि | Chintamani |
| pow | घात | Chintamani |
| printf | म_लिखो | Chintamani |
| private | निजी | Chintamani |
| protected | रक्षित | Chintamani |
| ptrdiff_t | सूचक_भेद_प्रकार | Chintamani |
| public | खुला | Chintamani |
| putc | अ_दो | Chintamani |
| putchar | अक्षर_दो | Chintamani |
| puts | माला_दो | Chintamani |
| qsort | क्विक | Chintamani |
| raise | उठाओ | Chintamani |
| rand | अक्रम | Chintamani |
| read | पढ़ो | Chintamani |
| readdir | सूची_पढ़ो | Chintamani |
| realloc | पुनः_स्मृति | Chintamani |
| remove | हटाओ | Chintamani |
| rename | नाम | Chintamani |
| rewind | शुरुआत | Chintamani |
| rewinddir | सूची_शुरु | Chintamani |
| rmdir | सूची_हटाओ | Chintamani |
| scanf | म_पूछो | Chintamani |
| setbuf | रखो_बफ | Chintamani |
| setjmp | बनाओ_लाँघ | Chintamani |
| setlocale | रखो_क्षेत्र | Chintamani |
| settime | समय_रखो | Chintamani |
| setvbuf | रखो_भबफ | Chintamani |
| sig_atomic_t | संक_पूर्ण_प्रकार | Chintamani |
| signal | संकेत | Chintamani |
| sigpending | संक_बाकी | Chintamani |
| sigsuspend | संक_रोको | Chintamani |
| size_t | माप_प्रकार | Chintamani |
| sprintf | प्र_लिखो | Chintamani |
| sqrt | वर्ग_मूल | Chintamani |
| srand | बेक्रम | Chintamani |
| sscanf | माला_पूछो | Chintamani |
| stderr | मानक_त्रुटि | Chintamani |
| stdin | मानक_निवेश | Chintamani |
| stdout | मानक_निकास | Chintamani |
| strcat | म_जोड़ो | Chintamani |
| strchr | म_अक्षर | Chintamani |
| strcmp | म_भेद | Chintamani |
| strcpy | म_नकल | Chintamani |
| strcspn | म_खोज | Chintamani |
| strerror | म_त्रुटि | Chintamani |
| strftime | स_माला | Chintamani |
| strlen | म_माप | Chintamani |
| strncat | म_जोड़न | Chintamani |
| strncmp | म_भेदन | Chintamani |
| strncpy | म_नकलन | Chintamani |
| strrchr | म_खोजप | Chintamani |
| strspn | म_अखोज | Chintamani |
| strstr | म_माला | Chintamani |
| strtod | म_से_भग्न | Chintamani |
| strtok | म_मोहर | Chintamani |
| strtol | म_से_दीर्घ | Chintamani |
| strtoul | म_से_अदीर्घ | Chintamani |
| system | प्रणाली | Chintamani |
| template | ढाँचा | Chintamani |
| time | समय | Chintamani |
| time_t | समय_प्रकार | Chintamani |
| times | बार | Chintamani |
| tm | पंचांग | Chintamani |
| tmpfile | क्षणिक_ख | Chintamani |
| tmpnam | क्षणिक | Chintamani |
| tolower | छोटे | Chintamani |
| toupper | बड़े | Chintamani |
| ungetc | अक्षर_वापस | Chintamani |
| va_arg | बहु_तर्क | Chintamani |
| va_end | बहु_पूर्ण | Chintamani |
| va_list | बहु_सूची | Chintamani |
| va_start | बहु_शुरू | Chintamani |
| vfprintf | भख_लिखो | Chintamani |
| virtual | भव | Chintamani |
| vprintf | भ_लिखो | Chintamani |
| vsprintf | भम_लिखो | Chintamani |
| wait | रुको | Chintamani |
| wchar_t | ब_अक्षर_प्रकार | Chintamani |
| write | ग_लिखो | Chintamani |

### A.2 C preprocessor

Host: ISO/IEC 9899, Information technology, Programming languages, C (preprocessing directives). Names: name transformation.

| Host | Hindi | Source |
|---|---|---|
| #define | #घोषणा | Chintamani |
| #include | #समावेश | Chintamani |
| #if | #अगर | Chintamani |
| #ifdef | #अगर_घोषित | Chintamani |
| #ifndef | #अगर_अघोषित | Chintamani |
| #else | #अन्यथा | Chintamani |
| #elif | #या_अगर | Chintamani |
| #endif | #पूर्ण_अगर | Chintamani |
| #undef | #अघोषित | Chintamani |
| #pragma | #आशय | Chintamani |
| #error | #त्रुटि | Chintamani |
| #line | #पंक्ति | Chintamani |

### A.3 C++

Host: ISO/IEC 14882, Programming languages, C++. Names: name transformation.

| Host | Hindi | Source |
|---|---|---|
| auto | स्वतः | Chintamani |
| break | अवरोध | Chintamani |
| case | हाल | Chintamani |
| char | अक्षर | Chintamani |
| const | स्थिर | Chintamani |
| continue | जारी | Chintamani |
| default | शेष | Chintamani |
| do | करो | Chintamani |
| double | द्विगुन | Chintamani |
| else | अन्यथा | Chintamani |
| enum | क्रमागत | Chintamani |
| extern | बाह्य | Chintamani |
| float | भग्न | Chintamani |
| for | क्रम | Chintamani |
| goto | जाओ | Chintamani |
| if | अगर | Chintamani |
| inline | अंतरभूत | Chintamani |
| int | पूर्णांक | Chintamani |
| long | दीर्घ | Chintamani |
| register | रेजिस्टर | Chintamani |
| restrict | restrict | host form (no native word yet) |
| return | वापस | Chintamani |
| short | लघु | Chintamani |
| signed | चिन्हित | Chintamani |
| sizeof | माप | Chintamani |
| static | अटल | Chintamani |
| struct | काष्ठा | Chintamani |
| switch | चयन | Chintamani |
| typedef | प्रकार | Chintamani |
| union | जोड़ | Chintamani |
| unsigned | अचिन्हित | Chintamani |
| void | व्योम | Chintamani |
| volatile | अस्थिर | Chintamani |
| while | जबतक | Chintamani |
| main | मुख्य | Chintamani |
| bool | bool | host form (no native word yet) |
| catch | पकड़ो | Chintamani |
| class | श्रेणी | Chintamani |
| delete | मिटाओ | Chintamani |
| explicit | explicit | host form (no native word yet) |
| false | false | host form (no native word yet) |
| friend | मित्र | Chintamani |
| mutable | mutable | host form (no native word yet) |
| namespace | namespace | host form (no native word yet) |
| new | नया | Chintamani |
| nullptr | nullptr | host form (no native word yet) |
| operator | चालक | Chintamani |
| private | निजी | Chintamani |
| protected | रक्षित | Chintamani |
| public | खुला | Chintamani |
| template | ढाँचा | Chintamani |
| this | यह | Chintamani |
| throw | फेंको | Chintamani |
| true | true | host form (no native word yet) |
| try | प्रयास | Chintamani |
| typename | typename | host form (no native word yet) |
| using | using | host form (no native word yet) |
| virtual | भव | Chintamani |
| cout | अ_बाहर | Chintamani |
| cin | अ_अंदर | Chintamani |
| endl | प_पूर्ण | Chintamani |

Standard library and runtime names of the C++ binding:

| Host | Hindi | Source |
|---|---|---|
| BUFSIZ | बफ_मान | Chintamani |
| CHAR_BIT | अक्षर_बिट | Chintamani |
| CHAR_MAX | अक्षर_उच्च | Chintamani |
| CHAR_MIN | अक्षर_न्यून | Chintamani |
| CHILD_MAX | शिशु_उच्च | Chintamani |
| CLK_TCK | घड़ी_टिक | Chintamani |
| DBL_DIG | द्विग_भग्न | Chintamani |
| DBL_EPSILON | द्विग_अंतर | Chintamani |
| DBL_MANT_DIG | द्विग_पूर्ण | Chintamani |
| DBL_MAX | द्विग_उच्च | Chintamani |
| DBL_MIN | द्विग_न्यून | Chintamani |
| DIR | सूची | Chintamani |
| EDOM | गलत_तर्क | Chintamani |
| EOF | खातापूर्ण | Chintamani |
| ERANGE | दुस्फल | Chintamani |
| EXIT_FAILURE | निकास_त्रुटि | Chintamani |
| EXIT_SUCCESS | निकास_सफल | Chintamani |
| FILE | खाता | Chintamani |
| FILENAME_MAX | खातानाम_उच्च | Chintamani |
| FLT_DIG | भग्न_भग्न | Chintamani |
| FLT_EPSILON | भग्न_अंतर | Chintamani |
| FLT_MANT_DIG | भग्न_पूर्ण | Chintamani |
| FLT_MAX | भग्न_उच्च | Chintamani |
| FLT_MIN | भग्न_न्यून | Chintamani |
| FLT_RADIX | भग्न_आधार | Chintamani |
| FOPEN_MAX | ख_खोलो_उच्च | Chintamani |
| HUGE_VAL | विशाल_मान | Chintamani |
| INFINITY | अनन्त | Chintamani |
| INT_MAX | पूर्णांक_उच्च | Chintamani |
| INT_MIN | पूर्णांक_न्यून | Chintamani |
| LDBL_DIG | द_द्वि_भग्न | Chintamani |
| LDBL_EPSILON | द_द्वि_अंतर | Chintamani |
| LDBL_MANT_DIG | द_द्वि_पूर्ण | Chintamani |
| LDBL_MAX | द_द्वि_उच्च | Chintamani |
| LDBL_MIN | द_द्वि_न्यून | Chintamani |
| LONG_MAX | दीर्घ_उच्च | Chintamani |
| LONG_MIN | दीर्घ_न्यून | Chintamani |
| L_tmpnam | ब_क्षणिक | Chintamani |
| NAN | न_अंक | Chintamani |
| NDEBUG | न_संशोधन | Chintamani |
| NULL | शून्य | Chintamani |
| RAND_MAX | अक्रम_उच्च | Chintamani |
| SCHAR_MAX | च_अक्षर_उच्च | Chintamani |
| SCHAR_MIN | च_अक्षर_न्यून | Chintamani |
| SEEK_CUR | प्रस्तुत_से | Chintamani |
| SEEK_END | अंत_से | Chintamani |
| SEEK_SET | शुरू_से | Chintamani |
| SHRT_MAX | लघु_उच्च | Chintamani |
| SHRT_MIN | लघु_न्यून | Chintamani |
| SIBGABRT | संक_पात | Chintamani |
| SIGFPE | संक_भ_त्रुटि | Chintamani |
| SIGILL | संक_अवैध | Chintamani |
| SIGINT | संक_विघ्न | Chintamani |
| SIGSEGV | संक_अंश | Chintamani |
| SIGTERM | संक_इति | Chintamani |
| SIG_DFL | संक_पूर्व | Chintamani |
| SIG_ERR | संक_त्रुटि | Chintamani |
| SIG_IGN | संक_छोड़ो | Chintamani |
| TMP_MAX | क्षणिक_उच्च | Chintamani |
| UCHAR_MAX | अच_अक्षर_उच्च | Chintamani |
| UINT_MAX | अच_पूर्णांक_उच्च | Chintamani |
| ULONG_MAX | अच_दीर्घ_उच्च | Chintamani |
| USHRT_MAX | अच_लघु_उच्च | Chintamani |
| __DATE__ | __दिन__ | Chintamani |
| __FILE__ | __खाता__ | Chintamani |
| __LINE__ | __पंक्ति__ | Chintamani |
| __STDC__ | __मानक__ | Chintamani |
| __TIME__ | __समय__ | Chintamani |
| _exit | _निकास | Chintamani |
| abort | पात | Chintamani |
| abs | असल | Chintamani |
| app | नत्थी | Chintamani |
| asctime | समय_ठीक | Chintamani |
| asm | यंत्र | Chintamani |
| assert | निश्चित | Chintamani |
| ate | अंत_पर | Chintamani |
| atexit | निकास_पर | Chintamani |
| atof | म_से_भ | Chintamani |
| atoi | म_से_प | Chintamani |
| atol | म_से_द | Chintamani |
| bad | बुरा | Chintamani |
| binary | द्विग | Chintamani |
| bsearch | द्वा_खोज | Chintamani |
| calloc | सुस्मृति | Chintamani |
| ceil | उच्चमान | Chintamani |
| cerr | अ_त्रुटि | Chintamani |
| chdir | स_बदलो | Chintamani |
| clear | सफा | Chintamani |
| clearerr | साफ_त्रुटि | Chintamani |
| clock | घड़ी | Chintamani |
| clock_t | घड़ी_प्रकार | Chintamani |
| close | बंद | Chintamani |
| closedir | बंद_सूची | Chintamani |
| ctime | स_समय | Chintamani |
| dec | डेसी | Chintamani |
| difftime | स_अंतर | Chintamani |
| dirname | स_नाम | Chintamani |
| div | भाग | Chintamani |
| div_t | भाग_प्रकार | Chintamani |
| ends | म_पूर्ण | Chintamani |
| eof | खप | Chintamani |
| errno | त्रुटि_सं | Chintamani |
| exit | निकास | Chintamani |
| fabs | भ_असल | Chintamani |
| fail | हार | Chintamani |
| fclose | ख_बंद | Chintamani |
| feof | ख_पूर्ण | Chintamani |
| ferror | ख_त्रुटि | Chintamani |
| fflush | ख_साफ | Chintamani |
| fgetc | ख_अक्षर_लो | Chintamani |
| fgetpos | ख_स्थान_लो | Chintamani |
| fgets | ख_माला_लो | Chintamani |
| fixed | जड़ | Chintamani |
| floor | न्यूनमान | Chintamani |
| flush | सफाई | Chintamani |
| fmod | भ_शेष | Chintamani |
| fopen | ख_खोलो | Chintamani |
| fork | विभाजन | Chintamani |
| fpos_t | ख_स्थान_प्रकार | Chintamani |
| fprintf | ख_लिखो | Chintamani |
| fputc | ख_अक्षर_दो | Chintamani |
| fputs | ख_माला_दो | Chintamani |
| fread | ख_पढ़ो | Chintamani |
| free | मुक्त | Chintamani |
| freopen | ख_व_खोलो | Chintamani |
| fscanf | ख_पूछो | Chintamani |
| fseek | ख_जाओ | Chintamani |
| fsetpos | ख_स्थान_दो | Chintamani |
| fstat | ख_स्थिति | Chintamani |
| fstream | ख_प्रवाह | Chintamani |
| ftell | ख_बताओ | Chintamani |
| fwrite | ख_डालो | Chintamani |
| get | लो | Chintamani |
| getc | अ_लो | Chintamani |
| getchar | अक्षर_लो | Chintamani |
| getenv | दो_पर्या | Chintamani |
| getline | लो_पंक्ति | Chintamani |
| gets | माला_लो | Chintamani |
| gettime | समय_लो | Chintamani |
| gmtime | स_जमट | Chintamani |
| good | अच्छा | Chintamani |
| hex | षष्ठ | Chintamani |
| ifstream | अख_प्रवाह | Chintamani |
| ins | म_लो | Chintamani |
| ios | पनप | Chintamani |
| iostream | पन_प्रवाह | Chintamani |
| isalnum | है_अक्षर_अंक | Chintamani |
| isalpha | है_अक्षर | Chintamani |
| iscntrl | है_नियंत्रण | Chintamani |
| isdigit | है_अंक | Chintamani |
| isfinite | है_सीमित | Chintamani |
| isgraph | है_चित्र | Chintamani |
| islower | है_छोटा | Chintamani |
| isodigit | है_अष्टक | Chintamani |
| isprint | है_छाप | Chintamani |
| ispunct | है_विराम | Chintamani |
| isspace | है_खाली | Chintamani |
| istream | अ_प्रवाह | Chintamani |
| istrstream | अम_प्रवाह | Chintamani |
| isupper | है_बड़ा | Chintamani |
| isxdigit | है_षष्ठादशक | Chintamani |
| jmp_buf | लाँघ_बफ | Chintamani |
| kill | समाप्त | Chintamani |
| labs | द_असल | Chintamani |
| lconv | स्था_बदल | Chintamani |
| ldiv | द_भाग | Chintamani |
| ldiv_t | द_भाग_प्रकार | Chintamani |
| left | बाँए | Chintamani |
| localeconv | क्षेत्र_बदलो | Chintamani |
| localtime | स_स्थानीय | Chintamani |
| longjmp | दीर्घ_लाँघ | Chintamani |
| malloc | दो_स्मृति | Chintamani |
| memchr | स_प्रथम | Chintamani |
| memcmp | स_भेद | Chintamani |
| memcpy | स_नकल | Chintamani |
| memmove | स_हटाओ | Chintamani |
| memset | स_रखो | Chintamani |
| mkdir | सूची_गढ़ो | Chintamani |
| mktime | स_गढ़ो | Chintamani |
| nocreate | न_नया | Chintamani |
| noreplace | न_प्रति | Chintamani |
| oct | अष्ट | Chintamani |
| offsetof | दुरत्व | Chintamani |
| ofstream | बख_प्रवाह | Chintamani |
| open | खोलो | Chintamani |
| opendir | सूची_खोलो | Chintamani |
| ostream | ब_प्रवाह | Chintamani |
| ostrstream | बम_प्रवाह | Chintamani |
| outs | म_दो | Chintamani |
| pause | छोड़ो | Chintamani |
| perror | लिखो_त्रुटि | Chintamani |
| pow | घात | Chintamani |
| printf | म_लिखो | Chintamani |
| ptrdiff_t | सूचक_भेद_प्रकार | Chintamani |
| put | दो | Chintamani |
| putc | अ_दो | Chintamani |
| putchar | अक्षर_दो | Chintamani |
| puts | माला_दो | Chintamani |
| qsort | क्विक | Chintamani |
| raise | उठाओ | Chintamani |
| rand | अक्रम | Chintamani |
| read | पढ़ो | Chintamani |
| readdir | सूची_पढ़ो | Chintamani |
| realloc | पुनः_स्मृति | Chintamani |
| remove | हटाओ | Chintamani |
| rename | नाम | Chintamani |
| resetiosflags | पुनः_पन_झंडे | Chintamani |
| rewind | शुरुआत | Chintamani |
| rewinddir | सूची_शुरु | Chintamani |
| right | दाँए | Chintamani |
| rmdir | सूची_हटाओ | Chintamani |
| scanf | म_पूछो | Chintamani |
| scientific | वैज्ञानिक | Chintamani |
| seekg | ग_स्थान | Chintamani |
| seekp | प_स्थान | Chintamani |
| setbase | रखो_आधार | Chintamani |
| setbuf | रखो_बफ | Chintamani |
| setfill | रखो_भरो | Chintamani |
| setiosflags | रखो_पन_झंडे | Chintamani |
| setjmp | बनाओ_लाँघ | Chintamani |
| setlocale | रखो_क्षेत्र | Chintamani |
| setprecision | रखो_सटीक | Chintamani |
| settime | समय_रखो | Chintamani |
| setvbuf | रखो_भबफ | Chintamani |
| setw | रखो_चौड़ाई | Chintamani |
| showbase | लिखो_आधार | Chintamani |
| showpoint | लिखो_बिंदु | Chintamani |
| showpos | लिखो_चिन्ह | Chintamani |
| sig_atomic_t | संक_पूर्ण_प्रकार | Chintamani |
| signal | संकेत | Chintamani |
| sigpending | संक_बाकी | Chintamani |
| sigsuspend | संक_रोको | Chintamani |
| size_t | माप_प्रकार | Chintamani |
| skipws | छोड़ो_खाली | Chintamani |
| sprintf | प्र_लिखो | Chintamani |
| sqrt | वर्ग_मूल | Chintamani |
| srand | बेक्रम | Chintamani |
| sscanf | माला_पूछो | Chintamani |
| stderr | मानक_त्रुटि | Chintamani |
| stdin | मानक_निवेश | Chintamani |
| stdio | मानकपन | Chintamani |
| stdout | मानक_निकास | Chintamani |
| strcat | म_जोड़ो | Chintamani |
| strchr | म_अक्षर | Chintamani |
| strcmp | म_भेद | Chintamani |
| strcpy | म_नकल | Chintamani |
| strcspn | म_खोज | Chintamani |
| strerror | म_त्रुटि | Chintamani |
| strftime | स_माला | Chintamani |
| strlen | म_माप | Chintamani |
| strncat | म_जोड़न | Chintamani |
| strncmp | म_भेदन | Chintamani |
| strncpy | म_नकलन | Chintamani |
| strrchr | म_खोजप | Chintamani |
| strspn | म_अखोज | Chintamani |
| strstr | म_माला | Chintamani |
| strstream | म_प्रवाह | Chintamani |
| strtod | म_से_भग्न | Chintamani |
| strtok | म_मोहर | Chintamani |
| strtol | म_से_दीर्घ | Chintamani |
| strtoul | म_से_अदीर्घ | Chintamani |
| system | प्रणाली | Chintamani |
| time | समय | Chintamani |
| time_t | समय_प्रकार | Chintamani |
| times | बार | Chintamani |
| tm | पंचांग | Chintamani |
| tmpfile | क्षणिक_ख | Chintamani |
| tmpnam | क्षणिक | Chintamani |
| tolower | छोटे | Chintamani |
| toupper | बड़े | Chintamani |
| trunc | छाँटो | Chintamani |
| ungetc | अक्षर_वापस | Chintamani |
| uppercase | बड़ा | Chintamani |
| va_arg | बहु_तर्क | Chintamani |
| va_end | बहु_पूर्ण | Chintamani |
| va_list | बहु_सूची | Chintamani |
| va_start | बहु_शुरू | Chintamani |
| vfprintf | भख_लिखो | Chintamani |
| vprintf | भ_लिखो | Chintamani |
| vsprintf | भम_लिखो | Chintamani |
| wait | रुको | Chintamani |
| wchar_t | ब_अक्षर_प्रकार | Chintamani |
| write | ग_लिखो | Chintamani |
| ws | खाली | Chintamani |

### A.4 Java

Host: The Java Language Specification, Oracle, current edition. Names: unchanged.

| Host | Hindi | Source |
|---|---|---|
| abstract | सार | Chintamani |
| assert | assert | host form (no native word yet) |
| boolean | द्वाफल | Chintamani |
| break | अवरोध | Chintamani |
| byte | बाईट | Chintamani |
| case | हाल | Chintamani |
| catch | पकड़ो | Chintamani |
| char | अक्षर | Chintamani |
| class | श्रेणी | Chintamani |
| continue | जारी | Chintamani |
| default | शेष | Chintamani |
| do | करो | Chintamani |
| double | द्विगुन | Chintamani |
| else | अन्यथा | Chintamani |
| enum | enum | host form (no native word yet) |
| extends | पूर्वज | Chintamani |
| final | अन्तिम | Chintamani |
| finally | अन्तिमतः | Chintamani |
| float | भग्न | Chintamani |
| for | क्रम | Chintamani |
| if | अगर | Chintamani |
| implements | लागु | Chintamani |
| import | आयात | Chintamani |
| instanceof | अवतार | Chintamani |
| int | पूर्णांक | Chintamani |
| interface | स्वरूप | Chintamani |
| long | दीर्घ | Chintamani |
| native | यांत्रिक | Chintamani |
| new | नया | Chintamani |
| package | कोष | Chintamani |
| private | निजी | Chintamani |
| protected | रक्षित | Chintamani |
| public | खुला | Chintamani |
| return | वापस | Chintamani |
| short | लघु | Chintamani |
| static | जड़ | Chintamani |
| super | मह | Chintamani |
| switch | चयन | Chintamani |
| synchronized | synchronized | host form (no native word yet) |
| this | यह | Chintamani |
| throw | फेंको | Chintamani |
| throws | फेंकता_है | Chintamani |
| try | प्रयास | Chintamani |
| void | व्योम | Chintamani |
| volatile | अस्थिर | Chintamani |
| while | जबतक | Chintamani |
| true | true | host form (no native word yet) |
| false | false | host form (no native word yet) |
| null | null | host form (no native word yet) |
| String | माला_श्रेणी | Chintamani |
| System | प्रणाली | Chintamani |

Standard library and runtime names of the Java binding:

| Host | Hindi | Source |
|---|---|---|
| Applet | प्रयोग_श्रेणी | Chintamani |
| ArithmeticException | गणित_त्रुटि | Chintamani |
| ArrayIndexOutOfBoundsException | व्यूह_सूचकांक_खेद_त्रुटि | Chintamani |
| ArrayStateException | व्यूह_स्थिति_त्रुटि | Chintamani |
| AudioClip | ध्वनि_अंश | Chintamani |
| BufferedReader | बफर_पाठक | Chintamani |
| ClassCastException | श्रेणी_साँचा_त्रुटि | Chintamani |
| ClassNotFoundException | श्रेणी_उपलब्ध_नहीं_त्रुटि | Chintamani |
| ClassNotSupportedException | श्रेणी_निराधार_त्रुटि | Chintamani |
| Date | दिन | Chintamani |
| FileInputStream | खाता_प्रवेश_प्रवाह | Chintamani |
| FileOutputStream | खाता_निकास_प्रवाह | Chintamani |
| GetFieldID | लो_क्षेत्र_सूचकांक | Chintamani |
| GetIntField | लो_पूर्ण_क्षेत्र | Chintamani |
| GetObjectClass | लो_वस्तु_श्रेणी | Chintamani |
| Graphics | चित्रांकन | Chintamani |
| IllegalAccessException | अवैध_प्रवेश_त्रुटि | Chintamani |
| IllegalArgumentException | अवैध_तर्क_त्रुटि | Chintamani |
| IllegalMonitorStateException | अवैध_योजक_त्रुटि | Chintamani |
| IllegalStateException | अवैध_स्थिति_त्रुटि | Chintamani |
| IllegalThreadStateException | अवैध_कड़ी_स्थिति_त्रुटि | Chintamani |
| Image | छवि | Chintamani |
| IndexOutOfBoundsException | सूचकांक_भेद_त्रुटि | Chintamani |
| InputStream | प्रवेश_प्रवाह | Chintamani |
| InputStreamReader | प्रवेश_प्रवाह_पाठक | Chintamani |
| InstantiationException | अवतारण_त्रुटि | Chintamani |
| InterruptedException | विघ्न_त्रुटि | Chintamani |
| MAX_PRIORITY | उच्च_प्राथमिकता | Chintamani |
| MIN_PRIORITY | न्यून_प्राथमिकता | Chintamani |
| Math | गणित | Chintamani |
| NORM_PRIORITY | सामान्य_प्राथमिकता | Chintamani |
| NegativeArraySizeException | ऋण_व्यूह_माप_त्रुटि | Chintamani |
| NoSuchFieldException | कोई_ऐसा_क्षेत्र_नहीं_त्रुटि | Chintamani |
| NoSuchMethodException | कोई_ऐसी_क्रिया_नहीं_त्रुटि | Chintamani |
| NullPointerException | शून्य_सूचक_त्रुटि | Chintamani |
| NumberFormatException | अंक_रचना-त्रुटि | Chintamani |
| Object | वस्तु | Chintamani |
| OutputStream | निकास_प्रवाह | Chintamani |
| PrintWriter | छापाकार | Chintamani |
| Reader | पाठक | Chintamani |
| Runnable | आरम्भ_लायक | Chintamani |
| SecurityException | सुरक्षा_त्रुटि | Chintamani |
| SetIntField | रखो_पूर्ण_क्षेत्र | Chintamani |
| StringBuffer | माला_बफर | Chintamani |
| StringIndexOutOfBounds | माला_सूचकांक_सीमा_खेद | Chintamani |
| Thread | कड़ी | Chintamani |
| Throwable | फेंकने_लायक | Chintamani |
| URL | वसंज्ञ | Chintamani |
| URLConnection | वसंज्ञ_सम्बन्ध | Chintamani |
| UnsupportedOperationException | क्रिया_उपलब्ध_नहीं_त्रुटि | Chintamani |
| Writer | लेखक | Chintamani |
| applet | प्रयोग | Chintamani |
| args | तर्क | Chintamani |
| awt | औसंख | Chintamani |
| charAt | अक्षर_स्थान | Chintamani |
| clone | नकल | Chintamani |
| close | बंद | Chintamani |
| compareTo | भेद | Chintamani |
| concat | संयोग | Chintamani |
| const | स्थिर | Chintamani |
| currentThread | यह_कड़ी | Chintamani |
| destroy | मिटाओ | Chintamani |
| drawString | माला_लिखो | Chintamani |
| endsWith | अंत_में | Chintamani |
| equals | बराबर | Chintamani |
| equalsIgnoreCase | बराबर_न | Chintamani |
| fillInStackTrace | भरो_ढेर | Chintamani |
| finalize | अंतिम | Chintamani |
| getAudioClip | लो_ध्वनि_अंश | Chintamani |
| getBytes | लो_बाइट | Chintamani |
| getChars | लो_अक्षर | Chintamani |
| getClass | लो_श्रेणी | Chintamani |
| getContentLength | लो_अंश_माप | Chintamani |
| getContentType | लो_अंश_प्रकार | Chintamani |
| getDate | लो_दिन | Chintamani |
| getExpiration | लो_अन्त | Chintamani |
| getImage | लो_छवि | Chintamani |
| getInputStream | लो_प्रवेश_प्रवाह | Chintamani |
| getLastModified | लो_पूर्व_बदली | Chintamani |
| getLocalizedMessage | लो_स्थानीय_संदेश | Chintamani |
| getMessage | लो_संकेत | Chintamani |
| getName | लो_नाम | Chintamani |
| getParameter | लो_तर्क | Chintamani |
| getPriority | लो_प्राथमिक | Chintamani |
| goto | जाओ | Chintamani |
| hashCode | हैश_कूट | Chintamani |
| indexOf | सूचकांक | Chintamani |
| init | उपसर्ग | Chintamani |
| io | पन | Chintamani |
| isAlive | जीवित_है | Chintamani |
| java | कृत्रिम | Chintamani |
| join | मेल | Chintamani |
| lastIndexOf | पूर्व_सूचकांक | Chintamani |
| length | माप | Chintamani |
| loadLibrary | लो_कोष | Chintamani |
| loop | दोहराओ | Chintamani |
| main | मुख्य | Chintamani |
| net | नेट | Chintamani |
| nextdouble | अगला_द्वि | Chintamani |
| notify | संकेत | Chintamani |
| notifyAll | संकेत_सब | Chintamani |
| openConnection | खोलो_सम्बन्ध | Chintamani |
| out | बाहर | Chintamani |
| paint | बनाओ | Chintamani |
| play | बजाओ | Chintamani |
| printStackTrace | दिखाओ_ढेर | Chintamani |
| println | म_लिखो_न | Chintamani |
| rand | अक्रम | Chintamani |
| read | म_पढ़ो | Chintamani |
| readLine | पंक्ति_पढ़ो | Chintamani |
| regionMatches | क्षेत्र_मेल | Chintamani |
| replace | प्रतिस्थापन | Chintamani |
| resume | पुनः_आरम्भ | Chintamani |
| run | आरम्भ | Chintamani |
| setName | रखो_नाम | Chintamani |
| setPriority | रखो_प्राथमिकता | Chintamani |
| sleep | सो_जाओ | Chintamani |
| sqrt | वर्ग_मूल | Chintamani |
| start | शुरू | Chintamani |
| startsWith | शुरू_में | Chintamani |
| stop | विराम | Chintamani |
| strictfp | दृढ़भग्न | Chintamani |
| substring | उपमाला | Chintamani |
| suspend | स्थगित | Chintamani |
| synchronised | समप्रवाह | Chintamani |
| toCharArray | करो_अक्षर_व्यूह | Chintamani |
| toLowerCase | करो_छोटे | Chintamani |
| toString | करो_माला | Chintamani |
| toUpperCase | करो_बड़े | Chintamani |
| transient | अस्थायी | Chintamani |
| trim | छाँटो | Chintamani |
| update | नया_हाल | Chintamani |
| util | उपयोग | Chintamani |
| valueof | मान | Chintamani |
| wait | रुको | Chintamani |
| write | म_लिखो | Chintamani |

### A.5 Python

Host: The Python Language Reference, Python Software Foundation, current version. Names: unchanged.

| Host | Hindi | Source |
|---|---|---|
| False | False | host form (no native word yet) |
| None | None | host form (no native word yet) |
| True | True | host form (no native word yet) |
| and | and | host form (no native word yet) |
| as | as | host form (no native word yet) |
| assert | assert | host form (no native word yet) |
| break | अवरोध | Chintamani |
| class | श्रेणी | Chintamani |
| continue | जारी | Chintamani |
| def | def | host form (no native word yet) |
| del | del | host form (no native word yet) |
| elif | elif | host form (no native word yet) |
| else | अन्यथा | Chintamani |
| except | except | host form (no native word yet) |
| finally | अन्तिमतः | Chintamani |
| for | क्रम | Chintamani |
| from | from | host form (no native word yet) |
| global | global | host form (no native word yet) |
| if | अगर | Chintamani |
| import | आयात | Chintamani |
| in | in | host form (no native word yet) |
| is | is | host form (no native word yet) |
| lambda | lambda | host form (no native word yet) |
| nonlocal | nonlocal | host form (no native word yet) |
| not | not | host form (no native word yet) |
| or | or | host form (no native word yet) |
| pass | pass | host form (no native word yet) |
| raise | raise | host form (no native word yet) |
| return | वापस | Chintamani |
| try | प्रयास | Chintamani |
| while | जबतक | Chintamani |
| with | with | host form (no native word yet) |
| yield | yield | host form (no native word yet) |
| print | print | host form (no native word yet) |
| range | range | host form (no native word yet) |
| len | len | host form (no native word yet) |

Standard library and runtime names of the Python binding:

| Host | Hindi | Source |
|---|---|---|
| Applet | प्रयोग_श्रेणी | Chintamani |
| ArithmeticException | गणित_त्रुटि | Chintamani |
| ArrayIndexOutOfBoundsException | व्यूह_सूचकांक_खेद_त्रुटि | Chintamani |
| ArrayStateException | व्यूह_स्थिति_त्रुटि | Chintamani |
| AudioClip | ध्वनि_अंश | Chintamani |
| BufferedReader | बफर_पाठक | Chintamani |
| ClassCastException | श्रेणी_साँचा_त्रुटि | Chintamani |
| ClassNotFoundException | श्रेणी_उपलब्ध_नहीं_त्रुटि | Chintamani |
| ClassNotSupportedException | श्रेणी_निराधार_त्रुटि | Chintamani |
| Date | दिन | Chintamani |
| FileInputStream | खाता_प्रवेश_प्रवाह | Chintamani |
| FileOutputStream | खाता_निकास_प्रवाह | Chintamani |
| GetFieldID | लो_क्षेत्र_सूचकांक | Chintamani |
| GetIntField | लो_पूर्ण_क्षेत्र | Chintamani |
| GetObjectClass | लो_वस्तु_श्रेणी | Chintamani |
| Graphics | चित्रांकन | Chintamani |
| IllegalAccessException | अवैध_प्रवेश_त्रुटि | Chintamani |
| IllegalArgumentException | अवैध_तर्क_त्रुटि | Chintamani |
| IllegalMonitorStateException | अवैध_योजक_त्रुटि | Chintamani |
| IllegalStateException | अवैध_स्थिति_त्रुटि | Chintamani |
| IllegalThreadStateException | अवैध_कड़ी_स्थिति_त्रुटि | Chintamani |
| Image | छवि | Chintamani |
| IndexOutOfBoundsException | सूचकांक_भेद_त्रुटि | Chintamani |
| InputStream | प्रवेश_प्रवाह | Chintamani |
| InputStreamReader | प्रवेश_प्रवाह_पाठक | Chintamani |
| InstantiationException | अवतारण_त्रुटि | Chintamani |
| InterruptedException | विघ्न_त्रुटि | Chintamani |
| MAX_PRIORITY | उच्च_प्राथमिकता | Chintamani |
| MIN_PRIORITY | न्यून_प्राथमिकता | Chintamani |
| Math | गणित | Chintamani |
| NORM_PRIORITY | सामान्य_प्राथमिकता | Chintamani |
| NegativeArraySizeException | ऋण_व्यूह_माप_त्रुटि | Chintamani |
| NoSuchFieldException | कोई_ऐसा_क्षेत्र_नहीं_त्रुटि | Chintamani |
| NoSuchMethodException | कोई_ऐसी_क्रिया_नहीं_त्रुटि | Chintamani |
| NullPointerException | शून्य_सूचक_त्रुटि | Chintamani |
| NumberFormatException | अंक_रचना-त्रुटि | Chintamani |
| Object | वस्तु | Chintamani |
| OutputStream | निकास_प्रवाह | Chintamani |
| PrintWriter | छापाकार | Chintamani |
| Reader | पाठक | Chintamani |
| Runnable | आरम्भ_लायक | Chintamani |
| SecurityException | सुरक्षा_त्रुटि | Chintamani |
| SetIntField | रखो_पूर्ण_क्षेत्र | Chintamani |
| String | माला_श्रेणी | Chintamani |
| StringBuffer | माला_बफर | Chintamani |
| StringIndexOutOfBounds | माला_सूचकांक_सीमा_खेद | Chintamani |
| System | प्रणाली | Chintamani |
| Thread | कड़ी | Chintamani |
| Throwable | फेंकने_लायक | Chintamani |
| URL | वसंज्ञ | Chintamani |
| URLConnection | वसंज्ञ_सम्बन्ध | Chintamani |
| UnsupportedOperationException | क्रिया_उपलब्ध_नहीं_त्रुटि | Chintamani |
| Writer | लेखक | Chintamani |
| abstract | सार | Chintamani |
| applet | प्रयोग | Chintamani |
| args | तर्क | Chintamani |
| awt | औसंख | Chintamani |
| boolean | द्वाफल | Chintamani |
| byte | बाईट | Chintamani |
| case | हाल | Chintamani |
| catch | पकड़ो | Chintamani |
| char | अक्षर | Chintamani |
| charAt | अक्षर_स्थान | Chintamani |
| clone | नकल | Chintamani |
| close | बंद | Chintamani |
| compareTo | भेद | Chintamani |
| concat | संयोग | Chintamani |
| const | स्थिर | Chintamani |
| currentThread | यह_कड़ी | Chintamani |
| default | शेष | Chintamani |
| destroy | मिटाओ | Chintamani |
| do | करो | Chintamani |
| double | द्विगुन | Chintamani |
| drawString | माला_लिखो | Chintamani |
| endsWith | अंत_में | Chintamani |
| equals | बराबर | Chintamani |
| equalsIgnoreCase | बराबर_न | Chintamani |
| extends | पूर्वज | Chintamani |
| fillInStackTrace | भरो_ढेर | Chintamani |
| final | अन्तिम | Chintamani |
| finalize | अंतिम | Chintamani |
| float | भग्न | Chintamani |
| getAudioClip | लो_ध्वनि_अंश | Chintamani |
| getBytes | लो_बाइट | Chintamani |
| getChars | लो_अक्षर | Chintamani |
| getClass | लो_श्रेणी | Chintamani |
| getContentLength | लो_अंश_माप | Chintamani |
| getContentType | लो_अंश_प्रकार | Chintamani |
| getDate | लो_दिन | Chintamani |
| getExpiration | लो_अन्त | Chintamani |
| getImage | लो_छवि | Chintamani |
| getInputStream | लो_प्रवेश_प्रवाह | Chintamani |
| getLastModified | लो_पूर्व_बदली | Chintamani |
| getLocalizedMessage | लो_स्थानीय_संदेश | Chintamani |
| getMessage | लो_संकेत | Chintamani |
| getName | लो_नाम | Chintamani |
| getParameter | लो_तर्क | Chintamani |
| getPriority | लो_प्राथमिक | Chintamani |
| goto | जाओ | Chintamani |
| hashCode | हैश_कूट | Chintamani |
| implements | लागु | Chintamani |
| indexOf | सूचकांक | Chintamani |
| init | उपसर्ग | Chintamani |
| instanceof | अवतार | Chintamani |
| int | पूर्णांक | Chintamani |
| interface | स्वरूप | Chintamani |
| io | पन | Chintamani |
| isAlive | जीवित_है | Chintamani |
| java | कृत्रिम | Chintamani |
| join | मेल | Chintamani |
| lastIndexOf | पूर्व_सूचकांक | Chintamani |
| length | माप | Chintamani |
| loadLibrary | लो_कोष | Chintamani |
| long | दीर्घ | Chintamani |
| loop | दोहराओ | Chintamani |
| main | मुख्य | Chintamani |
| native | यांत्रिक | Chintamani |
| net | नेट | Chintamani |
| new | नया | Chintamani |
| nextdouble | अगला_द्वि | Chintamani |
| notify | संकेत | Chintamani |
| notifyAll | संकेत_सब | Chintamani |
| openConnection | खोलो_सम्बन्ध | Chintamani |
| out | बाहर | Chintamani |
| package | कोष | Chintamani |
| paint | बनाओ | Chintamani |
| play | बजाओ | Chintamani |
| printStackTrace | दिखाओ_ढेर | Chintamani |
| println | म_लिखो_न | Chintamani |
| private | निजी | Chintamani |
| protected | रक्षित | Chintamani |
| public | खुला | Chintamani |
| rand | अक्रम | Chintamani |
| read | म_पढ़ो | Chintamani |
| readLine | पंक्ति_पढ़ो | Chintamani |
| regionMatches | क्षेत्र_मेल | Chintamani |
| replace | प्रतिस्थापन | Chintamani |
| resume | पुनः_आरम्भ | Chintamani |
| run | आरम्भ | Chintamani |
| setName | रखो_नाम | Chintamani |
| setPriority | रखो_प्राथमिकता | Chintamani |
| short | लघु | Chintamani |
| sleep | सो_जाओ | Chintamani |
| sqrt | वर्ग_मूल | Chintamani |
| start | शुरू | Chintamani |
| startsWith | शुरू_में | Chintamani |
| static | जड़ | Chintamani |
| stop | विराम | Chintamani |
| strictfp | दृढ़भग्न | Chintamani |
| substring | उपमाला | Chintamani |
| super | मह | Chintamani |
| suspend | स्थगित | Chintamani |
| switch | चयन | Chintamani |
| synchronised | समप्रवाह | Chintamani |
| this | यह | Chintamani |
| throw | फेंको | Chintamani |
| throws | फेंकता_है | Chintamani |
| toCharArray | करो_अक्षर_व्यूह | Chintamani |
| toLowerCase | करो_छोटे | Chintamani |
| toString | करो_माला | Chintamani |
| toUpperCase | करो_बड़े | Chintamani |
| transient | अस्थायी | Chintamani |
| trim | छाँटो | Chintamani |
| update | नया_हाल | Chintamani |
| util | उपयोग | Chintamani |
| valueof | मान | Chintamani |
| void | व्योम | Chintamani |
| volatile | अस्थिर | Chintamani |
| wait | रुको | Chintamani |
| write | म_लिखो | Chintamani |

### A.6 BASIC

Host: ISO/IEC 10279, Information technology, Programming languages, Full BASIC. Names: name transformation.

| Host | Hindi | Source |
|---|---|---|
| dim | आयाम | Chintamani |
| end | इति | Chintamani |
| for | क्रम | Chintamani |
| gosub | जाओ | Chintamani |
| goto | अगला | Chintamani |
| if | अगर | Chintamani |
| input | पूछो | Chintamani |
| let | मानो | Chintamani |
| next | क्रमांत | Chintamani |
| print | लिखो | Chintamani |
| rem | टिप्पणी | Chintamani |
| return | वापस | Chintamani |
| step | गति | Chintamani |
| then | हो तो | Chintamani |
| to | से | Chintamani |
| wend | तब तक | Chintamani |
| while | जब तक | Chintamani |
| and | तथा | Chintamani |
| or | या | Chintamani |
| not | नहीं | Chintamani |
| mod | शेष | Chintamani |

Standard library and runtime names of the BASIC binding:

| Host | Hindi | Source |
|---|---|---|
| abs | समपूर्ण | Chintamani |
| as | पन्थ | Chintamani |
| asc | इस्कि | Chintamani |
| atn | अटैन | Chintamani |
| call | अनुक्रम | Chintamani |
| chr | लिपी | Chintamani |
| cint | पूर्णान्क | Chintamani |
| circle | वृत | Chintamani |
| close | बंद | Chintamani |
| cls | साफ | Chintamani |
| color | रंग | Chintamani |
| command | पूर्वादेश | Chintamani |
| const | स्थिर | Chintamani |
| cos | कॉस | Chintamani |
| date | दिनाङ्क | Chintamani |
| declare | घोषणा | Chintamani |
| do | करो | Chintamani |
| else | अन्यथा | Chintamani |
| eof | खाता_पूर्ण | Chintamani |
| exists | पूर्वासित | Chintamani |
| exit | निकास | Chintamani |
| exp | प्रतिपादक | Chintamani |
| function | क्रिया | Chintamani |
| hex | षष्ठादशक | Chintamani |
| inkey | चाबी_दबाया | Chintamani |
| instr | अंश | Chintamani |
| int | अन्क | Chintamani |
| lcase | छोटे | Chintamani |
| left | पूर्व | Chintamani |
| len | माप | Chintamani |
| line | रेखा | Chintamani |
| locate | स्थान | Chintamani |
| log | लॉग | Chintamani |
| loop | फिर | Chintamani |
| ltrim | पूर्वक्षय | Chintamani |
| mid | बीच | Chintamani |
| oct | आष्टक | Chintamani |
| open | खोलो | Chintamani |
| pset | बिंदु | Chintamani |
| randomize | बेक्रम_क्रिया | Chintamani |
| right | अन्त | Chintamani |
| rnd | अक्रमाङ्क | Chintamani |
| rtrim | अंतक्षय | Chintamani |
| screen | पर्दा | Chintamani |
| sgn | चिन्ह | Chintamani |
| shared | सार्वजनिक | Chintamani |
| shell | अवकाश | Chintamani |
| sin | साइन | Chintamani |
| space | खाली | Chintamani |
| sqr | वर्गमूल | Chintamani |
| static | जड़ | Chintamani |
| str | अंक_माला | Chintamani |
| string | माला | Chintamani |
| sub | अणु | Chintamani |
| tan | टैन | Chintamani |
| time | समय | Chintamani |
| timer | घड़ी | Chintamani |
| ucase | बड़े | Chintamani |
| val | मान | Chintamani |
| xor | अथवा | Chintamani |

### A.7 LOGO

Host: No international standard; the host is the Berkeley Logo dialect (bibliography). Names: name transformation.

| Host | Hindi | Source |
|---|---|---|
| forward | forward | host form (no native word yet) |
| back | back | host form (no native word yet) |
| left | left | host form (no native word yet) |
| right | right | host form (no native word yet) |
| penup | penup | host form (no native word yet) |
| pendown | pendown | host form (no native word yet) |
| repeat | repeat | host form (no native word yet) |
| to | to | host form (no native word yet) |
| end | end | host form (no native word yet) |
| make | make | host form (no native word yet) |
| if | if | host form (no native word yet) |
| ifelse | ifelse | host form (no native word yet) |
| home | home | host form (no native word yet) |
| clearscreen | clearscreen | host form (no native word yet) |

## Annex B (informative) Coverage and review

| Binding | Host keywords with a native word | Library names |
|---|---|---|
| C | 34 of 35 | 240 |
| C preprocessor | 12 of 12 | 0 |
| C++ | 51 of 61 | 284 |
| Java | 45 of 51 | 136 |
| Python | 11 of 36 | 170 |
| BASIC | 21 of 21 | 60 |
| LOGO | 0 of 14 | 0 |

The lowering of Hindi programs to C is verified by the reference implementation: runs, same output. Source Chintamani means a word of the original Hindawi transducers; lexicon, a word of the language's lexicon; proposed, a word proposed by the project and not yet reviewed by the language community.

## Annex C (normative) Script filter

Devanagari text passes to Romenagri without a script filter.

## Annex D (informative) Rights and provenance

This document is an original work. It defines new programming languages by reference to the host language standards listed in Clause 2 and reproduces no text from them. Permission to adopt, translate or publish it as a standard is given by the copyright holder to a standards body on request.

Single words and the keywords of the host languages are not reproduced from any copyrighted text; the native words of Annex A were chosen by the Hindawi project, taken from the language's lexicon in the Hindawi repository, or, for Hindi, taken from the Chintamani transducers of the original Hindawi, whose author holds their copyright.

## Bibliography

- Hindawi 2026.10, hindawiai/hindawi2026.10, the reference implementation
- Chintamani, hindawiai/chintamani, the Hindawi transducers and the Romenagri tools
- Berkeley Logo reference manual, Brian Harvey

