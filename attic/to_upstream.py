#!/usr/bin/env python3
"""Convert native Hindawi project back to upstream C.
Usage: to_upstream.py --lang sanskrit input.uhin > output.c
"""
import argparse, csv, re, sys
from pathlib import Path

TABLES = Path(__file__).parent / "tables"
CHINT = Path(__file__).resolve().parents[1] / "upstream/chintamani"
LANGS = Path(__file__).resolve().parents[1] / "languages"

def load_idents_reverse(lang):
    m = {}
    p = TABLES / "identifiers.csv"
    if not p.exists():
        return m
    for row in csv.DictReader(p.open()):
        if row.get("english") and row.get(lang):
            m[row[lang]] = row["english"]
    return m

def load_keywords(lang):
    """Load native -> c_token from forward uhin."""
    uhin = LANGS / lang / "h2c.uhin"
    if not uhin.exists():
        return {}
    m = {}
    for line in uhin.read_text().splitlines():
        match = re.match(r'^(\S+)\s+\{printf\("([^"]+)"\);\}', line)
        if match:
            m[match.group(1)] = match.group(2)
    return m

def convert(src, lang):
    idents = load_idents_reverse(lang)
    keywords = load_keywords(lang)
    # keywords first
    for native, c_tok in sorted(keywords.items(), key=lambda x: -len(x[0])):
        src = src.replace(native, c_tok)
    # identifiers
    for native, eng in sorted(idents.items(), key=lambda x: -len(x[0])):
        src = src.replace(native, eng)
    # braces
    src = src.replace("अणु", "{").replace("पूर्ण", "}")
    return src

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", default="sanskrit")
    ap.add_argument("input", nargs="?", default="-")
    args = ap.parse_args()
    src = sys.stdin.read() if args.input == "-" else Path(args.input).read_text()
    print(convert(src, args.lang))

if __name__ == "__main__":
    main()
