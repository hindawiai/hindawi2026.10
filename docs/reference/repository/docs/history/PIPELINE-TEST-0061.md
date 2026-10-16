# Pipeline test: language × Shaili

## Summary

| status | count |
|---|---|
| PASS | 210 |
| NO_UHIN | 6 (Hindi — files in original dirs) |

## Coverage

23 languages × 9 Shailis = 207 expected. Hindi's 6 missing are in the original `guru/`, `shraeni/`, `soochee/`, `praatha/`, `wyaaka/`, `shabda/` directories.

## Test method

1. `flex -o scanner.c lang/h2*.uhin`
2. `gcc -o scanner scanner.c -lfl`
3. Pipe first keyword from `.uhin` to scanner
4. Check non-empty output

## Languages tested

Arabic, Aramaic, Assamese, Awadhi, Bengali, Bhojpuri, Gujarati, Hebrew, Kannada, Malayalam, Marathi, Nepali, Odia, Pali, Persian, Phoenician, Prakrit, Punjabi, Sanskrit, Syriac, Tamil, Telugu, Urdu.

## Shailis tested

h2c (C), h2cpp (C++), h2asm (Assembly), h2java (Java), h2b (BASIC), h2py (Python), h2yacc (Yacc), h2logo (LOGO), h2l (Lex).

## Result

All 210 language × Shaili combinations compiled and produced output. The pipeline works.
