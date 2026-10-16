# Audit: programming language × human language × script

## Summary

| dimension | count |
|---|---|
| Languages with complete .uhin (9 fwd + 9 rev) | 23 |
| Original Shaili dirs (Hindi reference) | 6 |
| Languages with keyword TSV | 22 |
| Script projection tables with content | 41 |
| .uhin compiled and tested | 2 (Bengali, Urdu) |

## Languages with complete stack

23 languages have 18 `.uhin` files each (9 forward, 9 reverse):

Arabic, Aramaic, Assamese, Awadhi, Bengali, Bhojpuri, Gujarati, Hebrew, Kannada, Malayalam, Marathi, Nepali, Odia, Pali, Persian, Phoenician, Prakrit, Punjabi, Sanskrit, Syriac, Tamil, Telugu, Urdu.

## Keyword data

| keywords | languages |
|---|---|
| 27–30 | Hindi, Sanskrit, Arabic, Urdu, Persian, Bengali, Gujarati, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, Telugu |
| 9–12 | Nepali, Assamese, Hebrew, Pali |
| 3–6 | Aramaic, Phoenician, Prakrit, Syriac |

## Script projection

41 tables with mappings. Examples: Bengali 65, Gujarati 67, Tamil 45, Telugu 66, Kannada 66, Malayalam 67, Odia 67, Gurmukhi 55, Brahmi 63, Grantha 60.

## Compilation

| test | result |
|---|---|
| Bengali h2c.uhin | compiled, `যদি` → `if` |
| Urdu h2c.uhin | compiled, `اگر` → `if` |
| Others | not individually tested |

Flex is at `/tmp/flexroot`. The `.uhin` files compile.

## What is not done

- End-to-end: native program → .uhin → C → gcc → run, for languages other than the two tested.
- Reverse .uhin tested.
- Non-C Shailis (C++, Python, Java, etc.) compiled and tested.
- Languages with fewer than 9 keywords have sparse .uhin. The files exist. The keyword coverage is thin.

## Architecture

Original Hindi `.uhin` in `guru/`, `shraeni/`, `soochee/`, `praatha/`, `wyaaka/`, `shabda/` are unchanged. Generated files follow the same Flex structure.
