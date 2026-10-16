# Audit: BUILD-0070

## Coverage

| category | count |
|---|---|
| Languages with complete .uhin (9 fwd + 9 rev) | 31 |
| Languages with keyword CSV | 68 |
| Languages with keyword TSV | 22 |
| Script projection tables with content | 41 |
| .uhin files total | ~580 |

## Languages with complete stack

Arabic, Aramaic, Assamese, Awadhi, Bengali, Bhojpuri, Burmese, Dzongkha, Gujarati, Hebrew, Kannada, Khmer, Lao, Malayalam, Marathi, Nepali, Odia, Pali, Pashto, Persian, Phoenician, Prakrit, Punjabi, Sanskrit, Sinhala, Syriac, Tamil, Telugu, Thai, Tibetan, Urdu.

## Gaps

| gap | languages |
|---|---|
| CSV but no .uhin | Chhattisgarhi, Magahi, Sindhi, Maithili, Konkani, Dogri, Bodo, Kashmiri, Rajasthani, Newari, Santali, Tulu, Javanese, Sundanese, Balinese, Batak, Buginese, Tagalog, Shan, Limbu, Lepcha, and others |
| Hindi partial | h2cpp, h2b, h2py, h2yacc, h2l in original dirs |

## Architecture compliance

| item | status |
|---|---|
| Flex .uhin structure | yes |
| Original Hindi files unchanged | yes |
| String literal handling | partial (added to some) |
| Header mappings | original Hindi only |
| Preprocessor mappings | original Hindi only |
| Keyword vocabulary | original Hindi for Devanagari; generated for others |

## Compilation

| test | result |
|---|---|
| Flex available | yes |
| Bengali, Urdu, Tibetan compiled | yes |
| Full end-to-end | not tested for all |

## Honest summary

31 languages have complete .uhin stacks. 37 languages have keyword data but no .uhin. The original Hindi architecture is preserved. Generated files follow the Flex structure but use language-specific vocabularies that differ from the original Hindi keyword set.
