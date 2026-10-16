# Where this repository deviates from legacy Hindawi (Chintamani)

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

Legacy Hindawi is `hindawiai/chintamani` at 3ad8778. Its copy in `lang/hindawi/upstream/chintamani` is byte for
byte Chintamani, and `tests/fundamental.py` F1 checks that it stays so. Everything below differs from it. It is
recorded here and nothing in it has been changed.

## In the generated language cells (`lang/hindawi/languages/`, BUILD-0102)

1. **The cells exist at all.** Legacy Hindawi has Hindi only. The other 75 cells were generated.
2. **The Hindi cell is not Chintamani's Hindi.** Its `h2c.uhin` differs in 676 lines, has 325 rules against 323,
   and has lost the 2003 to 2006 copyright and GPL notice.
3. **Five languages carry Hindi's transducer.** Sanskrit, Marathi, Nepali, Awadhi and Bhojpuri have Hindi's
   transducer, byte for byte.
4. **Keywords are replaced inside longer words.** The cells have no rule for identifiers, so a keyword is
   replaced wherever it appears: `interval` becomes `<int>erval`, `printf` becomes `pr<int>f`. They also map the
   single letter `c` to `native`.
5. **Fifty-two cells' reverse transducers run the wrong way.** They map native to English instead of English to
   native, and some emit placeholders (`KW_IF`) rather than C.
6. **Seventeen languages have Latin keywords,** although most of them have scripts of their own. All 76 store a
   hand-made romanised column in `pipeline/language_params.json`.
7. **Some cells disagree with themselves.** In Bengali and Tamil, `c2h` and `h2c` use different words for the
   same keyword, so a program ingested through one does not compile through the other.
8. **The Makefiles skip the script filter.** Non-Devanagari cells' Makefiles feed their text straight to `uni2acii`,
   which reads Devanagari only.

## In the tools around them

9. **Grok's original `hindawicc`** sent every language through Hindi's `h2c`, bypassed Romenagri, and fell back to
   compiling the raw source. C11 rewrote it on the original chain.
10. **`pipeline/transliterate.py`** carries every script to Devanagari before h2c. Legacy Hindawi had script
    filters for Telugu and Urdu only (`fltr_*`).
11. **The script tables** (`tools/pushkalavati-compiler/vendor/romenagri/upstream/tables`) are headers only.
    Where they are empty, `transliterate.py` projects by Unicode name, as their headers say they do.
12. **BURP's ingestion path reads each cell's rules and applies them per token in Python,** outside literals,
    comments and `#include` names. It does not run the cells' flex lexers. That avoids deviation 4 without
    editing any cell. The compilation path still runs the lexers.

## Legacy behaviour, not deviations, recorded because they matter

- **Underscores.** Romenagri's `acii2cf` doubles every underscore in ASCII identifiers (`debug_putc` becomes
  `debug__putc`).
- **Assembly.** Chintamani's own assembly pair is not round-trip stable on its sample.
- **Format strings.** `c2h` localises format strings (`%d` becomes `%द`), and `gurucc` repairs only `%प`,
  `%भ` and `\न` on the way back.
