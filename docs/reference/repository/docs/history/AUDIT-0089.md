# Audit: languages × scripts × paradigms

## Coverage

| dimension | count |
|---|---|
| Languages | 76 |
| Shailis (paradigms) | 9 |
| Script tables | 46 |
| Translation pairs | 10 |

## Shaili coverage

| paradigm | languages |
|---|---|
| C (h2c) | 76 |
| C++ (h2cpp) | 75 |
| Assembly (h2asm) | 76 |
| Java (h2java) | 76 |
| BASIC (h2b) | 75 |
| Python (h2py) | 75 |
| Yacc (h2yacc) | 75 |
| LOGO (h2logo) | 76 |
| Lex (h2l) | 75 |

## Translation pairs (argostranslate)

en→hi, en→bn, en→ur, en→ar, en→fa, en→ru, en→zh, en→ja, en→ko, en→th

## Gaps

| gap | detail |
|---|---|
| Tamil, Telugu, Kannada, Malayalam | no argostranslate pair |
| 1 language missing core keywords | — |
| 1 language missing some Shailis | — |

## Pipeline

```
native script → transliterate.py → Devanagari → guru/h2c.uhin → C → gcc
```

All components exist. Driver (`hindawicc`) wires them together.

## Architecture compliance

| item | status |
|---|---|
| Original Hindi .uhin | intact (323 mappings) |
| Flex structure | preserved |
| Transliteration first | yes |
| One .uhin for all | yes (guru/h2c.uhin) |
