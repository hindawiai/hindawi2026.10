#!/usr/bin/env python3
"""Import upstream library with auto-translation to target language."""
import argparse, re
from pathlib import Path

LANG_CODES = {
    "hindi": "hi", "bengali": "bn", "tamil": "ta", "telugu": "te",
    "arabic": "ar", "chinese": "zh", "japanese": "ja", "korean": "ko",
    "persian": "fa", "russian": "ru", "thai": "th", "urdu": "ur",
}

def translate(text, target_lang):
    code = LANG_CODES.get(target_lang, "hi")
    try:
        import argostranslate.translate
        result = argostranslate.translate.translate(text, "en", code)
        return result.replace(" ", "_")
    except Exception:
        return text

def extract_functions(header_path):
    try:
        content = Path(header_path).read_text(errors="ignore")
        return re.findall(r'\b(\w+)\s*\([^)]*\)\s*;', content)[:30]
    except Exception:
        return []

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", default="hindi")
    ap.add_argument("header")
    args = ap.parse_args()
    native_header = translate(args.header.replace(".h", ""), args.lang) + ".स"
    print(f"# {args.header} → {native_header}")
    print(f"# Language: {args.lang}")
    for func in extract_functions(f"/usr/include/{args.header}"):
        native = translate(func, args.lang)
        print(f"{native:<30} # {func}")

if __name__ == "__main__":
    main()
