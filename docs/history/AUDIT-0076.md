# Transliteration Audit

## Summary

| status | count |
|---|---|
| PASSTHROUGH | 44 |
| CONVERTED | 32 |

## Architecture

```
native script → transliterate.py → Devanagari → original Hindi h2c.uhin → C
```

## Script tables

| script | table | status |
|---|---|---|
| Bengali | bengali_to_deva.tsv | exists |
| Telugu | telugu_to_deva.tsv | exists |
| Tamil | tamil_to_deva.tsv | exists |
| Cyrillic | cyrillic_to_deva.tsv | added |
| Perso-Arabic | perso2deva_heur.py | exists |
| CJK | — | not available |

## Converted languages

- arabic: إذا → अज़अ
- assamese: যদি → यदि
- balochi: إذا → अज़अ
- bengali: যদি → यदि
- bulgarian: ако → अकओ
- dari: إذا → अज़अ
- gujarati: જો → जो
- hausa_ajami: إذا → अज़अ
- kannada: ಆದರೆ → आदरे
- kashmiri: إذا → अज़अ
- kurdish_sorani: إذا → अज़अ
- malay_jawi: إذا → अज़अ
- malayalam: എങ്കിൽ → एङ्किൽ
- mandaic: إذا → अज़अ
- manipuri_beng: যদি → यदि
- nabataean: إذا → अज़अ
- odia: ଯଦି → यदि
- pashto: إذا → अज़अ
- persian: اگر → अगर
- punjabi: ਜੇ → जੇ
- punjabi_shahmukhi: إذا → अज़अ
- russian: если → एसलइ
- samaritan: إذا → अज़अ
- saraiki: إذا → अज़अ
- serbian: ако → अकओ
- sindhi: إذا → अज़अ
- tamil: எனில் → एऩिल्
- telugu: ఒకవేళ → ओकवేळ
- tulu: ಯದಿ → यदि
- ukrainian: якщо → याकश्चओ
- urdu: اگر → अगर
- uyghur: إذا → अज़अ

## Passthrough languages

- aramaic
- awadhi
- balinese
- batak
- bhojpuri
- bodo
- buginese
- burmese
- chhattisgarhi
- chinese
- dogri
- dzongkha
- hebrew
- hindi
- japanese
- javanese
- kashmiri_dev
- khmer
- konkani
- korean
- lao
- lepcha
- limbu
- magahi
- maithili
- marathi
- marwari
- nepali
- newari
- pali
- phoenician
- prakrit
- rajasthani
- sanskrit
- santali
- shan
- sindhi_dev
- sinhala
- sundanese
- syriac
- tagalog
- thai
- tibetan
- vietnamese

## Context

The pipeline projects all scripts to Devanagari. The original Hindi .uhin handles keyword mapping. One .uhin serves all languages. Cyrillic table added in BUILD-0075. CJK requires dictionary-based transliteration (pinyin/romaji), not implemented.
