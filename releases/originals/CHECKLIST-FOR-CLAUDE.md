# Checklist for Claude — HINDAWI2026.10-best

## Regression results (executed)

| test | result |
|---|---|
| Forward lexers (h2c, h2cpp, h2asm, h2java, h2b, h2py, h2yacc, h2logo, h2l) | 679 PASS, 5 NO_FILE |
| Reverse lexers (c2h, cpp2h, asm2h, java2h, b2h, py2h, yacc2h, logo2h, l2h) | 679 PASS, 5 NO_FILE |
| Languages | 76 |
| Ingest | `int total_count` → `int कुल` |
| Multi-file | exit 42 |
| hindawicc | exit 55 |

## Paths in zip

| component | path |
|---|---|
| Forward lexers | `lang/hindawi/upstream/chintamani/<lang>/h2*.uhin` |
| Reverse lexers | `lang/hindawi/upstream/chintamani/<lang>/*2h.uhin` |
| Original Hindi | `lang/hindawi/upstream/chintamani/guru/h2c.uhin` |
| hindawicc | `lang/hindawi/hindawicc` |
| ingest | `lang/hindawi/tools/ingest.py` |
| to_native | `lang/hindawi/tools/to_native.py` |
| to_upstream | `lang/hindawi/tools/to_upstream.py` |
| transliterate | `lang/hindawi/pipeline/transliterate.py` |
| language params | `lang/hindawi/pipeline/language_params.json` |
| import_project | `lang/hindawi/tools/import_project.py` |

## Deviations from original

| deviation | what I did | original |
|---|---|---|
| `transliterate.py` | I wrote this | Original uses Romenagri filters |
| `normalize.py` | I invented, then removed | Not in original |
| Single underscore | I used `_` | Original uses `__` for Romenagri survival |
| Assembly lexer | I invented 6 rules | Original Yantra not in tree |
| `ingest.py` | I wrote this | Not in original |

## What works

- 76 languages × 9 Shailis × 2 directions = 1358 lexers compile
- Hindi pipeline: `पूर्णांक मुख्य()` → `int main()`
- Bengali: `পূর্ণসংখ্যা` → `int`, `ফেরত` → `return`
- Multi-file compilation
- hindawicc drop-in
- ingest with dictionary

## What was NOT tested

- Romenagri round-trip (binary broken in environment)
- All 76 languages execution (only Hindi, Bengali tested)
- ELF/DWARF symbol preservation
- Assembly execution through original Yantra
- Hardware languages
