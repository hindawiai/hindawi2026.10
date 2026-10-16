# Translation tools for BURP's dictionary: suggestions

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

BURP builds each project's dictionary while it ingests, never in advance. Every identifier and comment not yet in
the dictionary goes to the translators in turn, and whatever they return is recorded, so the same name always gets
the same translation and the reverse is exact. Any program that reads lines and writes lines can be a translator
through `HINDAWI_TRANSLATE_CMD`.

| Tool | What it is | Fit for identifiers and comments |
|---|---|---|
| Argos Translate | Offline neural translation (OpenNMT models), Python; built in as `argos` | Good default where a model for the pair exists; runs on a laptop |
| LibreTranslate | A server around Argos | The same, shared across a team or a build farm |
| IndicTrans2 (AI4Bharat) | Neural translation for the 22 scheduled Indian languages | The strongest open choice for Indian languages |
| NLLB-200 (Meta), run with CTranslate2 | One model, 200 languages | Broad coverage, including many of the tajziya languages |
| OPUS-MT / MarianMT (Helsinki-NLP) | Many small pair models | Light and fast, where a pair exists |
| Bergamot / Firefox Translations | Small offline models | Fast; few language pairs |
| Apertium | Rule-based translation | Predictable output for close pairs; useful for related Indian languages |
| A local LLM (Llama, Qwen, Gemma through llama.cpp or Ollama) | General model, prompted | Can be told that it is naming a variable: short, consistent, one word per concept, with the project's glossary in the prompt |
| Bhashini (Government of India) | Translation APIs | Wide Indian coverage; a network service |
| Cloud APIs (Google, Microsoft, DeepL) | Hosted | Good quality, but not sovereign; fine for a draft the community then fixes |

For identifiers, prefer short and consistent output: split `counter_value` or `counterValue` into words,
translate the phrase, and join the words with `_`. BURP then keeps only characters that are valid in an identifier,
and makes each name unique and distinct from the language's keywords. A per-language glossary in
`lang/hindawi/burp/glossary/<language>.tsv` is consulted before any model, and that is where reviewed names go.
