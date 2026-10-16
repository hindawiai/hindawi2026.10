# Conversion test: language × script

## Result

| status | count |
|---|---|
| PASS | 24 |

All 24 languages converted successfully.

## Languages

Arabic, Aramaic, Assamese, Awadhi, Bengali, Bhojpuri, Gujarati, Hebrew, Hindi, Kannada, Malayalam, Marathi, Nepali, Odia, Pali, Persian, Phoenician, Prakrit, Punjabi, Sanskrit, Syriac, Tamil, Telugu, Urdu.

## Test

Input: `int counter = 0; while (counter < 10) { counter = counter + 1; } return counter;`

Check: keywords converted, braces converted.

## Shaili coverage

The conversion tool uses `c2h.uhin` (C reverse). Other Shailis have their own `.uhin` files:

| Shaili | .uhin tested earlier |
|---|---|
| h2c, h2cpp, h2asm, h2java, h2b, h2py, h2yacc, h2logo, h2l | 210/216 pass |

The conversion tool currently targets C (guru). Other Shailis require their own reverse tables (`cpp2h`, `py2h`, etc.) to be used.

## Note

Translation uses argostranslate (English → Hindi). Non-Hindi languages get Hindi keywords from their `c2h.uhin` if it was regenerated with the original vocabulary. Languages that still have the old generated vocabulary will produce different output.
