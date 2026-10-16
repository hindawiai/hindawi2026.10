# Architecture and keyword audit

## Deviations found

### 1. Keyword vocabulary

| construct | original Hindi | generated Sanskrit |
|---|---|---|
| if | अगर | यदि |
| else | अन्यथा | अन्यथा |
| while | जबतक | यावत् |
| for | के_लिये | प्रति |
| int | पूर्णांक | पूर्णाङ्क |
| return | वापस | प्रत्यागम |
| main | मुख्य | (not in generated) |
| { | अणु | अणु (added later) |
| } | पूर्ण | पूर्ण (added later) |

The original uses a specific Hindi vocabulary. The generated files use a different Sanskrit vocabulary from `lang_sanskrit.csv`. These are not the same.

### 2. Header mappings

Original has 20+ header mappings:
- मानकपन.स → stdio.h
- मानककोष.स → stdlib.h
- गणित.स → math.h
- माला.स → string.h

Generated files have none of these.

### 3. Library function mappings

Original maps constants and some functions. Generated files have partial additions (printf, scanf, malloc, free) that were added later and are not in the original vocabulary.

### 4. Preprocessor

Original maps:
- #घोषणा → #define
- #समावेश → #include
- #अगर → #if
- #पूर्ण_अगर → #endif

Generated files have none of these.

### 5. Count

| file | mappings |
|---|---|
| original h2c.uhin | 323 |
| generated sanskrit h2c.uhin | 217 |

### 6. String literal handling

Original preserves string literals:
```
\"("\\\""|[^\"^\n]*)*\"  {printf("%s",yytext);}
```

Generated files do not have this rule.

## What matches

- Flex .uhin structure
- Makefile structure (after fix)
- Wrapper structure (after fix)
- Brace mappings (अणु/पूर्ण) — added later, matches original

## Verdict

The generated `.uhin` files follow the Flex structure but use a different keyword vocabulary and are missing header mappings, preprocessor mappings, and string literal handling. This is a deviation from the original Hindawi keyword set.
