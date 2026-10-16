# Audit: programming language × human language × script

## What exists

### Dimension 1: Shaili (.uhin files)

| language | forward | reverse | total | notes |
|---|---|---|---|---|
| Sanskrit | 9 | 9 | 18 | generated |
| Marathi | 9 | 9 | 18 | generated |
| Nepali | 9 | 9 | 18 | generated |
| Awadhi | 9 | 9 | 18 | generated |
| Bhojpuri | 9 | 9 | 18 | generated |
| Hindi | 3 | 3 | 6 | original (guru, yantra, kritrima, robot only in hindi/) |

Original Hindi `.uhin` in dedicated dirs (guru/, shraeni/, etc.) are unchanged.

### Dimension 2: Keyword data (native script)

| language | keywords | script |
|---|---|---|
| Hindi | 30 | Devanagari |
| Sanskrit | 30 | Devanagari |
| Arabic | 30 | Arabic |
| Urdu | 28 | Perso-Arabic |
| Persian | 28 | Perso-Arabic |
| Bengali | 27 | Bengali |
| Gujarati | 27 | Gujarati |
| Kannada | 27 | Kannada |
| Malayalam | 27 | Malayalam |
| Marathi | 27 | Devanagari |
| Odia | 27 | Odia |
| Punjabi | 27 | Gurmukhi |
| Tamil | 27 | Tamil |
| Telugu | 27 | Telugu |
| Nepali | 12 | Devanagari |
| others | 3–9 | various |

### Dimension 3: Script projection tables

42 tables with content in `script_projection_tables.tar.gz`. Examples:

| script | mappings |
|---|---|
| Bengali | 65 |
| Gujarati | 67 |
| Kannada | 66 |
| Malayalam | 67 |
| Odia | 67 |
| Tamil | 45 |
| Telugu | 66 |
| Gurmukhi | 55 |
| Brahmi | 63 |
| Grantha | 60 |
| Sharada | 65 |
| Tibetan | 46 |

## What does not exist

| gap | detail |
|---|---|
| .uhin for non-Devanagari | Bengali, Tamil, Telugu, Kannada, Malayalam, Gujarati, Odia, Gurmukhi, Urdu, Arabic, Persian have keyword TSV but no .uhin |
| Compilation | Flex is not available. No .uhin has been compiled. |
| Reverse for original Hindi | Original tree has no asm2h, java2h, logo2h. Generated copies exist in hindi/. |
| End-to-end test | No native-script program has been compiled through the .uhin pipeline. |

## Honest count

| category | count |
|---|---|
| Languages with complete .uhin (9×2) | 5 |
| Languages with keyword data only | 17 |
| Script projection tables with content | 42 |
| .uhin files compiled | 0 |
| Native programs compiled through pipeline | 0 |

The .uhin files are Flex lexers. They exist. They have not been compiled. The keyword tables and script projection tables are data. They are not implementations.
