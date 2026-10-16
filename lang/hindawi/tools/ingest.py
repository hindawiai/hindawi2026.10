#!/usr/bin/env python3
"""Ingest and reverse using original c2h/h2c and identifier dictionary.
Dictionary reversal is separate from transliteration round-trip.
"""
import argparse, json, os, re, subprocess, sys
from pathlib import Path

# One dictionary per ingestion (a file or a project); HINDAWI_DICT names it, so a project shares one map.
DICT_PATH = Path(os.environ.get("HINDAWI_DICT", Path(__file__).parent / "identifier_dict.json"))
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
    base, k = native, 1
    while native in rev and rev[native] != ident:   # one native name per identifier, or reversal is ambiguous
        k += 1; native = f"{base}_{k}"
    fwd[ident] = native
    rev[native] = ident
    return native

def get_original(native, dictionary):
    """Reverse lookup: native → original. Dictionary reversal, not transliteration."""
    rev = dictionary.get("reverse", {})
    return rev.get(native, native)

# String and character literals, comments and #include <file> names are not code: identifiers are taken,
# and replaced, outside them only, so a file name never enters the dictionary.
LEXEME = re.compile(r'(#\s*include\s*<[^>\n]*>|"(?:\\.|[^"\\\n])*"|\'(?:\\.|[^\'\\\n])*\'|/\*.*?\*/|//[^\n]*)|\b([A-Za-z_][A-Za-z0-9_]*)\b', re.S)
KEYWORDS = {"int", "char", "float", "double", "void", "if", "else", "while", "for", "return", "break", "continue",
            "switch", "case", "default", "struct", "typedef", "const", "static", "extern", "sizeof", "main",
            "unsigned", "signed", "long", "short", "union", "enum", "do", "goto", "volatile", "register", "auto",
            "include", "define", "ifdef", "ifndef", "endif", "pragma", "undef",
            "printf", "scanf", "malloc", "free", "NULL", "true", "false"}

def extract_identifiers(src):
    return {m.group(2) for m in LEXEME.finditer(src) if m.group(2)} - KEYWORDS

def replace_code(text, mapping):
    """Replace whole identifiers outside literals and comments."""
    return LEXEME.sub(lambda m: m.group(0) if m.group(1) else mapping.get(m.group(2), m.group(2)), text)

ROMENAGRI = os.environ.get("ROMENAGRI", "")
# The original chain, as Chintamani's drivers run it. C to the language: Romenagri's encoding in, c2h, back to
# Unicode. The language to C: fixuninum, Romenagri (uni2acii | acii2cf | acii2uni), h2c. A lexer that is missing,
# or a chain that fails, stops the ingestion: nothing passes through unconverted.
CHAIN = {"c2h": "fixuninum | iconv -f utf-8 -t utf-16 | uni2acii | '{lx}' | acii2uni | iconv -f UTF-16 -t UTF-8",
         "h2c": "fixuninum | iconv -f utf-8 -t utf-16 | uni2acii | acii2cf | acii2uni | iconv -f UTF-16 -t UTF-8 | '{lx}'"}

def run_lexer(lexer, src):
    if not lexer.exists():
        sys.exit(f"ingest: {lexer} is not built (make it, with Romenagri on the PATH)")
    if not ROMENAGRI:
        sys.exit("ingest: set ROMENAGRI to a built Romenagri folder; the lexers read Romenagri's encoding")
    env = dict(os.environ, PATH=f"{ROMENAGRI}:" + os.environ.get("PATH", ""))
    r = subprocess.run(CHAIN[lexer.name].format(lx=lexer), shell=True, input=src.encode(), capture_output=True, env=env)
    if r.returncode != 0:
        sys.exit(f"ingest: {lexer.name} failed: {r.stderr.decode('utf-8', 'replace')[:200]}")
    return r.stdout.decode("utf-8").replace("\r", "")

def ingest(src, target_lang="hi"):
    dictionary = load_dict()
    converted = run_lexer(C2H, src)
    mapping = {ident: get_native(ident, dictionary, target_lang) for ident in extract_identifiers(src)}
    converted = replace_code(converted, mapping)
    save_dict(dictionary)
    return converted

def c_names(natives):
    """The C-level name of each native identifier: its Romenagri form, which is what h2c's chain leaves in the C
    (the name ABI: योगफल becomes yoagaphala). Computed by the same chain, so the reversal cannot drift from it."""
    if not natives:
        return {}
    env = dict(os.environ, PATH=f"{ROMENAGRI}:" + os.environ.get("PATH", ""))
    chain = "fixuninum | iconv -f utf-8 -t utf-16 | uni2acii | acii2cf | acii2uni | iconv -f UTF-16 -t UTF-8"
    out = subprocess.run(chain, shell=True, input="\n".join(natives).encode(), capture_output=True, env=env)
    forms = out.stdout.decode("utf-8").replace("\r", "").split("\n")
    return dict(zip(natives, forms))

def reverse(src):
    """Native to original: keywords through h2c's chain, then each identifier's C-level name back to the
    original through this ingestion's dictionary. Dictionary reversal, not transliteration reversal."""
    dictionary = load_dict()
    converted = run_lexer(H2C, src)
    rev = dictionary.get("reverse", {})
    forms = c_names(sorted(rev))
    return replace_code(converted, {forms[n]: rev[n] for n in rev if forms.get(n)})

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
