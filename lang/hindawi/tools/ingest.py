#!/usr/bin/env python3
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""ingest.py: carry existing code into one or many languages, and back.

Ingestion is for people, so it needs no transliteration: keywords become the language's keywords in its own
script (hindawi_chain.to_native), identifiers and comments are translated, and a dictionary records every
choice so the reverse is exact. The dictionary is dynamic: it starts empty and grows as names are met, each
filled by the translator (Grok's design, kept). One dictionary per language per ingestion; a project shares it.

  python3 ingest.py FILE.c                         Hindi, to stdout; dictionary at HINDAWI_DICT
  python3 ingest.py FILE.c --lang hindi,bengali,urdu --out DIR    every language at once, DIR/<lang>/FILE.c
  python3 ingest.py --reverse FILE.native [--lang L]               back to the original, through the dictionary

Translator, in order: HINDAWI_TRANSLATE (a command reading text on stdin and writing the translation, with
{src} and {tgt} replaced by language codes), else Argos Translate if installed, else none: names and comments
then stay as they are and are recorded as such. A translated name has spaces and punctuation turned into
underscores, and is made unique, so the reverse is never ambiguous.
"""
import argparse, json, os, re, subprocess, sys, unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hindawi_chain as chain

ISO = {"hindi": "hi", "bengali": "bn", "urdu": "ur", "tamil": "ta", "telugu": "te", "marathi": "mr", "gujarati": "gu",
       "kannada": "kn", "malayalam": "ml", "punjabi": "pa", "odia": "or", "nepali": "ne", "sanskrit": "sa",
       "arabic": "ar", "persian": "fa", "russian": "ru", "chinese": "zh", "japanese": "ja", "korean": "ko"}
PHONETIC = {"a": "अ", "b": "ब", "c": "च", "d": "द", "e": "ए", "f": "फ", "g": "ग", "h": "ह", "i": "इ", "j": "ज",
            "k": "क", "l": "ल", "m": "म", "n": "न", "o": "ओ", "p": "प", "q": "क", "r": "र", "s": "स", "t": "त",
            "u": "उ", "v": "व", "w": "व", "x": "क्ष", "y": "य", "z": "ज़"}   # Grok's, for one-letter names in Hindi
# Literals, comments and #include <file> are not code: names are taken, and replaced, outside them only.
LEXEME = re.compile(r'(#\s*include\s*<[^>\n]*>|"(?:\\.|[^"\\\n])*"|\'(?:\\.|[^\'\\\n])*\')|(/\*.*?\*/|//[^\n]*)'
                    r'|\b([A-Za-z_][A-Za-z0-9_]*)\b', re.S)
RESERVED = {"int", "char", "float", "double", "void", "if", "else", "while", "for", "return", "break", "continue",
            "switch", "case", "default", "struct", "typedef", "const", "static", "extern", "sizeof", "main",
            "unsigned", "signed", "long", "short", "union", "enum", "do", "goto", "volatile", "register", "auto",
            "include", "define", "ifdef", "ifndef", "endif", "pragma", "undef", "elif", "defined", "error",
            "printf", "scanf", "malloc", "free", "NULL", "true", "false", "inline", "asm"}


def load(path, lang):
    p = Path(path)
    d = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
    for k in ("forward", "reverse", "comments", "files"):
        d.setdefault(k, {})
    d.setdefault("lang", lang)
    return d


def save(d, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")


def translate(text, lang):
    tgt = ISO.get(lang, lang)
    cmd = os.environ.get("HINDAWI_TRANSLATE")
    try:
        if cmd:
            p = subprocess.run(cmd.replace("{src}", "en").replace("{tgt}", tgt), shell=True, input=text.encode(),
                               capture_output=True, timeout=60)
            return p.stdout.decode("utf-8").strip() if p.returncode == 0 and p.stdout.strip() else text
        import argostranslate.translate
        return argostranslate.translate.translate(text, "en", tgt)
    except Exception:
        return text


KEEP_MACROS = os.environ.get("HINDAWI_KEEP_MACROS") == "1"


def native_name(ident, d, lang):
    fwd, rev = d["forward"], d["reverse"]
    if ident in fwd:
        return fwd[ident]
    # the C reserved namespace (__func__, __attribute__, _start ...) is never renamed; with HINDAWI_KEEP_MACROS=1
    # neither are ALL-CAPS names, which upstream projects share with assembly, linker scripts and their configuration
    if ident.startswith("_") or (KEEP_MACROS and ident.upper() == ident and any(ch.isalpha() for ch in ident)):
        fwd[ident] = rev[ident] = ident
        return ident
    if len(ident) == 1 and lang == "hindi":
        native = PHONETIC.get(ident.lower(), ident)
    else:
        words = re.sub(r"([a-z])([A-Z])", r"\1 \2", ident).replace("_", " ").strip()
        native = translate(words, lang) if words else ident
        if native.strip() == words:   # nothing translated it: the name keeps its exact identity
            fwd[ident] = rev[ident] = ident
            return ident
        # letters, combining marks (the vowel signs of Brahmi scripts), digits; anything else becomes an underscore
        native = "".join(c if unicodedata.category(c)[0] in "LMN" or c == "_" else "_" for c in native)
        native = re.sub(r"_+", "_", native).strip("_") or ident
        if native[0].isdigit():
            native = "_" + native
    base, k = native, 1
    while native in rev and rev[native] != ident:   # one native name per identifier
        k += 1; native = f"{base}_{k}"
    fwd[ident], rev[native] = native, ident
    return native


def native_comment(text, d, lang):
    body = text[2:-2] if text.startswith("/*") else text[2:]
    out = translate(body, lang) if body.strip() else body
    if out == body:
        return text
    new = f"/*{out}*/" if text.startswith("/*") else f"//{out}"
    d["comments"][new] = text
    return new


def ingest(src, lang, d, localize_files=False):
    """Keywords through the language's c2h; names and comments never pass through it. The 2004 lexers match a
    keyword anywhere (the int in print), so names and comments are held aside as plain tokens and put back."""
    names = {m.group(3) for m in LEXEME.finditer(src) if m.group(3)} - RESERVED
    mapping = {n: native_name(n, d, lang) for n in names}
    held = []
    def hold(text):
        held.append(text); return f"QZXQ{len(held) - 1:06d}QXZQ"
    def code(m):
        if m.group(1):
            inc = re.match(r'(#\s*include\s*<)([^>\n]*)(>)', m.group(1))
            if localize_files and not inc and m.group(1).startswith('"') and m.group(1)[1:-1] in d["files"]:
                return hold('"' + d["files"][m.group(1)[1:-1]] + '"')
            return m.group(1)
        if m.group(2):
            return hold(native_comment(m.group(2), d, lang))
        return hold(mapping[m.group(3)]) if m.group(3) in mapping else m.group(3)
    out = chain.to_native(LEXEME.sub(code, src), lang)
    return re.sub(r"QZXQ(\d{6})QXZQ", lambda m: held[int(m.group(1))], out)


def reverse(src, lang, d):
    for new, old in d["comments"].items():   # comments come back exactly as they were
        src = src.replace(new, old)
    c = chain.to_c(src, lang)
    forms = chain.c_names(sorted(d["reverse"]), lang)
    back = {forms[n]: d["reverse"][n] for n in d["reverse"] if forms.get(n)}
    files = {v: k for k, v in d["files"].items()}
    def code(m):
        if m.group(1):
            if m.group(1).startswith('"') and m.group(1)[1:-1] in files:
                return '"' + files[m.group(1)[1:-1]] + '"'
            return m.group(1)
        return m.group(0) if m.group(2) else back.get(m.group(3), m.group(3))
    return LEXEME.sub(code, c)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file"); ap.add_argument("--lang", default="hindi")
    ap.add_argument("--out"); ap.add_argument("--reverse", action="store_true")
    ap.add_argument("--localize-files", action="store_true")
    a = ap.parse_args()
    src = Path(a.file).read_text(encoding="utf-8", errors="replace")
    langs = [l.strip() for l in a.lang.split(",") if l.strip()]
    for lang in langs:
        dpath = (Path(a.out) / lang / ".hindawi" / "dictionary.json") if a.out else \
            Path(os.environ.get("HINDAWI_DICT", Path(a.file).parent / f".hindawi-{lang}.json"))
        d = load(dpath, lang)
        text = reverse(src, lang, d) if a.reverse else ingest(src, lang, d, a.localize_files)
        save(d, dpath)
        if a.out:
            dst = Path(a.out) / lang / Path(a.file).name
            dst.parent.mkdir(parents=True, exist_ok=True); dst.write_text(text, encoding="utf-8")
        else:
            sys.stdout.write(text)


if __name__ == "__main__":
    main()
