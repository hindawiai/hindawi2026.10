# Audit results: BUILD-0093

## Tested

| # | question | result |
|---|---|---|
| 1 | Transliteration pipeline | PASS: যদি→यदि, если→एसलइ, 如果→रउगउओ |
| 2 | Original Hindi .uhin | PASS: 323 mappings, unchanged |
| 3 | All 9 Shailis | PASS: 75/76 languages |
| 4 | Romanized keywords | PASS: 0 found |
| 5 | Keywords are translations | PASS: যদি, གལ་ཏེ, ถ้า |
| 6 | Braces localized | PASS: খোলো/বন্ধ, திற/மூடு |
| 7 | Format specifiers | PASS: %d→%প, \n→\ন |
| 8 | hindawicc driver | PASS: exit 55 |
| 9 | Complex programs | PARTIAL: mixed scripts in output |
| 10 | Round trip | FAIL: to_upstream returns input unchanged |
| 11 | All scripts | PASS: Brahmi, Perso-Arabic, Cyrillic, CJK |
| 12 | Standard documents | NOT TESTED this run |
| 13 | Library translation | PARTIAL: works for languages with argostranslate pairs |

## Failures

### Round trip
`to_upstream.py` does not reverse the conversion. Input `int काउंटर = 0;` returns unchanged.

### Mixed scripts in complex programs
Bengali conversion shows Hindi identifiers (स्टेडियो, स्वैप) mixed with Bengali keywords (শূন্য, পূর্ণসংখ্যা).

## Gaps

- 1 language missing some Shailis
- Tamil, Telugu, Kannada, Malayalam have no argostranslate pairs
- Round-trip conversion broken
- Identifier translation always goes to Hindi, not target language
