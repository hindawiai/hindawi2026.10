# Hindawi 79×9 Shaili deficit report

## Accounting

| metric | count |
|---|---|
| TOTAL CELLS | 783 |
| profiles in registry | 87 |
| profiles with keyword data | 68 |
| shailis | 9 |
| IMPLEMENTED (.uhin exists) | 4 |
| KEYWORD-TABLE-ONLY | 608 |
| LINGUISTIC-BLOCKED | 171 |
| UNDECIPHERED | 0 |
| BUILD-BLOCKED | 0 |
| FAILED | 0 |
| TESTED | 0 |

## What is implemented

The .uhin files exist only for Hindi:

| shaili | paradigm | file |
|---|---|---|
| guru | C | upstream/chintamani/guru/h2c.uhin |
| shraeni | C++ | upstream/chintamani/shraeni/h2cpp.uhin |
| soochee | Python | upstream/chintamani/soochee/h2py.uhin |
| wyaaka | Yacc | upstream/chintamani/wyaaka/h2yacc.uhin |

These are the Hindi implementations. They are not localized to other languages.

## What is not an implementation

- Keyword CSV tables (608 cells). These are data. They do not transform source.
- Language registry entries. These are inventories.
- The generated port tables under ports/. These are derived views.

## What is blocked

- 171 cells: no keyword data in langspec. Linguistic data not present.
- Robot, Yantra, Kritrima, Praatha, Shabda: no .uhin exists for any language.
- No language other than Hindi has a .uhin.

## What was not done

- No new .uhin generated. The existing .uhin mechanism is Hindi-specific and was not redesigned.
- No linguistic data fabricated for languages without keyword inventories.
- No claim that keyword tables constitute implementations.

## Architecture preserved

The existing path remains:

native source → Hindi .uhin → Romenagri identifier → backend

Extending this to other languages requires either:
1. Localized .uhin files that call the same Romenagri mechanism, or
2. A data-driven .uhin that reads the keyword tables.

Neither was introduced. The keyword tables are the data layer. The .uhin remains the implementation layer, and it is Hindi-only.
