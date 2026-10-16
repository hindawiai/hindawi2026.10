# Upstream conversion audit

## Tool

`lang/hindawi/tools/to_native.py`

Uses argostranslate (English → Hindi) for identifiers. Keywords from `c2h.uhin`.

## Test: BST

Input:
```c
struct node *create_node(int key) {
    struct node *temp = malloc(sizeof(struct node));
    ...
}
```

Output:
```
काष्ठा नोड *बनाना_नोड(पूर्णांक कुंजी) अणु
    काष्ठा नोड *अस्थायी = दो_स्मृति(माप(काष्ठा नोड));
    ...
पूर्ण
```

## Translation examples

| English | Hindi |
|---|---|
| create_node | बनाना_नोड |
| insert | प्रवेश |
| search | खोज |
| temp | अस्थायी |
| key | कुंजी |
| left | बाएं |
| right | सही |

## Remaining English

None in identifiers. Format specifiers (`%d`, `%s`) preserved.

## Architecture

1. Keywords: `c2h.uhin` (original Hindi vocabulary)
2. Identifiers: argostranslate
3. Braces: अणु/पूर्ण
4. Spaces in translation: replaced with `_`

## Status

The tool converts upstream C to native Hindawi. Translation is automated via argostranslate, not hand-coded.
