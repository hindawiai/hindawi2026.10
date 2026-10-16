# BUILD-0051 filter and compilation report

## Filters found

### Brahmi-derived scripts

Source: `tools/pushkalavati-compiler/vendor/romenagri/upstream/releases/script_projection_tables.tar.gz`

Extracted tables contain actual mappings. The loose `tables/*.tsv` files in the tree are empty headers. The tarball is the operational source.

| table | lines | example |
|---|---|---|
| bengali_to_deva.tsv | 65 | যদি → यदि |
| tamil_to_deva.tsv | 45 | — |
| 73 others | varies | — |

Projection: source character → Devanagari hub character. Longest-match not required; one-to-one code point.

### Perso-Arabic

Source: `tools/pushkalavati-compiler/vendor/romenagri/upstream/filters/perso2deva_heur.py`

BASE map covers the attested consonantal skeleton. Unmapped Arabic-block letters fall back to NFKD strip or `ं`. Short-vowel residue is documented, not hidden.

Test: `اگر ورنہ` → `अगर वरनह`

## Compilation

Flex is not installed and cannot be installed in this environment (`apt-get` returns no installation candidate). The `.uhin` files are Flex lexers. Without Flex they cannot be compiled to executables.

The architecture is preserved: native source → `.uhin` → C → gcc. The `.uhin` files exist. The compilation step is blocked by the missing dependency.

## Test programs written

Complex programs in native scripts are at `lang/hindawi/tests/native/`. They exercise:
- Control flow (if/else/while/for)
- Function definition and call
- Nested blocks
- Multiple keywords

These are ready for the `.uhin` pipeline when Flex is available.
