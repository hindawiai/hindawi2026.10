#!/usr/bin/env python3
"""Convert upstream to native Hindawi."""
import argparse, json, re, sys
from pathlib import Path

PARAMS_PATH = Path(__file__).resolve().parents[1] / "pipeline/language_params.json"
_cache = {}
_params = None

def get_params():
    global _params
    if _params is None:
        _params = json.loads(PARAMS_PATH.read_text()) if PARAMS_PATH.exists() else {}
    return _params

def translate(text):
    if text in _cache:
        return _cache[text]
    try:
        import argostranslate.translate
        result = argostranslate.translate.translate(text, "en", "hi")
        result = result.replace(" ", "_").replace("-", "_")
        _cache[text] = result
        return result
    except Exception:
        return text

def convert(src, lang):
    params = get_params()
    kw = params.get(lang, {})
    # keywords
    keywords = {cid[3:].lower(): data["native"] for cid, data in kw.items() if cid.startswith("KW_") and data.get("native")}
    # protect format specifiers first
    formats = kw.get("FORMATS", {})
    protected = {}
    for i, (c_fmt, native_fmt) in enumerate(formats.items()):
        placeholder = f"__FMT{i}__"
        src = src.replace(c_fmt, placeholder)
        protected[placeholder] = native_fmt
    # identifiers (skip short ones that might be format letters)
    idents = set(re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', src)) - set(keywords.keys())
    ident_map = {}
    for ident in idents:
        if len(ident) > 1 and not ident.startswith("_") and not ident.isupper():
            parts = ident.split("_")
            translated = "_".join(translate(p) for p in parts if p)
            if translated != ident:
                ident_map[ident] = translated
    # apply keywords and identifiers
    for c_tok, native in sorted(keywords.items(), key=lambda x: -len(x[0])):
        src = re.sub(rf'\b{re.escape(c_tok)}\b', native, src)
    for eng, native in sorted(ident_map.items(), key=lambda x: -len(x[0])):
        src = re.sub(rf'\b{re.escape(eng)}\b', native, src)
    # braces
    src = src.replace("{", kw.get("BRACE_OPEN", {}).get("native", "{"))
    src = src.replace("}", kw.get("BRACE_CLOSE", {}).get("native", "}"))
    # restore formats
    for placeholder, native_fmt in protected.items():
        src = src.replace(placeholder, native_fmt)
    return src

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", default="hindi")
    ap.add_argument("input", nargs="?", default="-")
    args = ap.parse_args()
    src = sys.stdin.read() if args.input == "-" else Path(args.input).read_text()
    print(convert(src, args.lang))

if __name__ == "__main__":
    main()
