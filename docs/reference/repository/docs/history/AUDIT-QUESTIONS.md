# Audit questions: corrections and architecture

## Corrections made during development

### 1. Keyword vocabulary
**Correction:** "Have you deviated from original Hindawi architecture and keywords?"
**Issue:** Generated files used lang_*.csv vocabulary (यदि, यावत्) instead of original Hindi (अगर, जबतक).
**Fix:** Regenerated Devanagari languages with original 321 mappings.

### 2. Reverse .uhin missing
**Correction:** "Why have you left out reverse for a few?"
**Issue:** asm2h, java2h, logo2h not generated.
**Fix:** Added all 9 reverse .uhin files.

### 3. Flex not found
**Correction:** "You had earlier compiled flex from sources.... Check the zip!"
**Issue:** Claimed Flex unavailable when it existed at /tmp/flexroot.
**Fix:** Located and used existing Flex build.

### 4. Only C Shaili
**Correction:** "I see only C!!!!! All Shaili please"
**Issue:** Only guru (C) had complete files.
**Fix:** Generated all 9 Shailis for all languages.

### 5. SAARC classification
**Correction:** "Telugu is not SAARC??.. [correction]"
**Issue:** Telugu classified as non-SAARC.
**Fix:** Corrected: 35 SAARC languages including Telugu, Tamil, Kannada, etc.

### 6. Romanized keywords
**Correction:** "There should be NO romanized keywords!!!!! Fix it"
**Issue:** Thai, Tibetan, etc. had "yadi" instead of native script.
**Fix:** Replaced with actual translations (ถ้า, གལ་ཏེ, etc.).

### 7. Transliteration not translation
**Correction:** "What is Yadi in Tibetan???? You were supposed to translate"
**Issue:** Used transliteration of Sanskrit instead of actual translation.
**Fix:** Added real translations for all keywords.

### 8. Hindi braces for all
**Correction:** "Are braces localized or are you using Hindi version?"
**Issue:** to_native.py hardcoded अणु/पूर्ण for all languages.
**Fix:** Added language-specific braces (খোলো/বন্ধ for Bengali, etc.).

### 9. Hindi leakage
**Correction:** "Why मुख्य in Bangla?????"
**Issue:** Bengali output contained Hindi keywords.
**Fix:** All keywords now from target language parameter table.

### 10. Hand translation
**Correction:** "Why are you not using translate tools"
**Issue:** Left placeholders instead of using argostranslate.
**Fix:** Installed language pairs, used automated translation.

### 11. Transliteration bypass
**Correction:** "All languages must use transliteration"
**Issue:** CJK passed through without transliteration.
**Fix:** Added pypinyin → Devanagari for CJK.

### 12. Mixed scripts in output
**Correction:** "For Bangla your output shows roman and Devnagri?????"
**Issue:** Library import used Hindi translation for Bengali.
**Fix:** import_library.py now uses target language code.

## Audit questions

### Architecture
1. Does every language use the transliteration pipeline (script → Devanagari → .uhin)?
2. Is the original Hindi .uhin (guru/h2c.uhin) unchanged with 323 mappings?
3. Does one .uhin serve all languages after transliteration?
4. Are all 9 Shailis present for all languages?

### Keywords
5. Are all keywords in the target language's native script?
6. Are there any romanized keywords (yadi, prati, etc.)?
7. Are keywords translations, not transliterations of Sanskrit?
8. Do braces use language-specific terms, not hardcoded Hindi?

### Translation
9. Are translation tools (argostranslate) used for identifiers?
10. Are library functions translated to the target language?
11. Do standard documents generate correctly for any language × paradigm?

### Pipeline
12. Does hindawicc call transliterate.py automatically?
13. Does the full pipeline work for all 9 Shailis (C, C++, Assembly, Java, BASIC, Python, Yacc, LOGO, Lex)?
14. Are all scripts covered (Brahmi, Perso-Arabic, Cyrillic, CJK)?

### Testing
15. Have complex programs (BST, hashtable, quicksort) been converted and tested?
16. Does round-trip conversion preserve semantics?
17. Are format specifiers (%d, %s) preserved correctly?

## Implications

This work enables:
- Any upstream project (C, C++, Python, Java, etc.) to be presented in any supported language and script
- Native-script programs to compile to C via the original Hindawi pipeline
- Automated generation of language standards for any language × paradigm tuple
- Library import with automatic translation of function names

The architecture is: one .uhin, many scripts, automated translation.
