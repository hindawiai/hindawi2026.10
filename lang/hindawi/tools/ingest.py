#!/usr/bin/env python3
"""Ingest and reverse using original c2h/h2c and identifier dictionary.
Dictionary reversal is separate from transliteration round-trip.
"""
import argparse, json, re, subprocess, sys
from pathlib import Path

DICT_PATH = Path(__file__).parent / "identifier_dict.json"
C2H = Path(__file__).resolve().parents[1] / "upstream/chintamani/guru/c2h"
H2C = Path(__file__).resolve().parents[1] / "upstream/chintamani/guru/h2c"

PHONETIC = {
    "a": "अ", "b": "ब", "c": "च", "d": "द", "e": "ए", "f": "फ",
    "g": "ग", "h": "ह", "i": "इ", "j": "ज", "k": "क", "l": "ल",
    "m": "म", "n": "न", "o": "ओ", "p": "प", "q": "क", "r": "र",
    "s": "स", "t": "त", "u": "उ", "v": "व", "w": "व", "x": "क्ष",
    "y": "य", "z": "ज़",
}

def load_dict():
    if DICT_PATH.exists():
        return json.loads(DICT_PATH.read_text())
    return {"forward": {}, "reverse": {}}

def save_dict(d):
    DICT_PATH.write_text(json.dumps(d, ensure_ascii=False, indent=2))

def translate_word(word, target="hi"):
    try:
        import argostranslate.translate
        result = argostranslate.translate.translate(word, "en", target)
        return result.replace(" ", "_").replace("-", "_")
    except Exception:
        return word

def transliterate_char(char):
    return PHONETIC.get(char.lower(), char)

def get_native(ident, dictionary, target="hi"):
    fwd = dictionary.setdefault("forward", {})
    rev = dictionary.setdefault("reverse", {})
    if ident in fwd:
        return fwd[ident]
    native = transliterate_char(ident) if len(ident) == 1 else translate_word(ident, target)
    fwd[ident] = native
    rev[native] = ident
    return native

def get_original(native, dictionary):
    """Reverse lookup: native → original. Dictionary reversal, not transliteration."""
    rev = dictionary.get("reverse", {})
    return rev.get(native, native)

def extract_identifiers(src):
    keywords = {"int", "char", "float", "double", "void", "if", "else", "while",
                "for", "return", "break", "continue", "switch", "case", "default",
                "struct", "typedef", "const", "static", "extern", "sizeof", "main"}
    return set(re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', src)) - keywords

def run_lexer(lexer, src):
    if not lexer.exists():
        return src
    r = subprocess.run([str(lexer)], input=src.encode(), capture_output=True)
    return r.stdout.decode() if r.returncode == 0 else src

def ingest(src, target_lang="hi"):
    dictionary = load_dict()
    converted = run_lexer(C2H, src)
    for ident in sorted(extract_identifiers(src), key=len, reverse=True):
        native = get_native(ident, dictionary, target_lang)
        if native != ident:
            converted = re.sub(rf'\b{re.escape(ident)}\b', native, converted)
    save_dict(dictionary)
    return converted

def reverse(src):
    """Reverse identifiers using dictionary. Not transliteration reversal."""
    dictionary = load_dict()
    converted = run_lexer(H2C, src)
    rev = dictionary.get("reverse", {})
    for native in sorted(rev.keys(), key=len, reverse=True):
        original = rev[native]
        converted = converted.replace(native, original)
    return converted

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reverse", action="store_true", help="Reverse: native → original")
    ap.add_argument("--lang", default="hi")
    ap.add_argument("input", nargs="?", default="-")
    args = ap.parse_args()
    src = sys.stdin.read() if args.input == "-" else Path(args.input).read_text()
    print(reverse(src) if args.reverse else ingest(src, args.lang))

if __name__ == "__main__":
    main()
