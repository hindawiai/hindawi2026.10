#!/usr/bin/env python3
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""coverage.py: how complete a language is. For each paradigm, the share of the host language's reserved words that have
a word in the language's cell; for the GATE programs, the share of keywords, library calls and the programs' own names
that come out in the language. Lists what is missing, so it can be filled in lang/hindawi/lexicons/<lang>.tsv (keywords,
library calls) or lang/hindawi/burp/glossary/<lang>.tsv (names).

  python3 lang/hindawi/tools/coverage.py --langs urdu,sindhi [--missing]
"""
import argparse, json, re, subprocess, sys, tempfile, shutil
from pathlib import Path
R = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(R / "lang/hindawi/burp"))
import burp  # noqa: E402

C = """auto break case char const continue default do double else enum extern float for goto if inline int long register
restrict return short signed sizeof static struct switch typedef union unsigned void volatile while main""".split()
PARADIGM_WORDS = {
    "C": (["c2h"], C),
    "C++": (["cpp2h"], C + """bool catch class delete explicit false friend mutable namespace new nullptr operator private
        protected public template this throw true try typename using virtual cout cin endl""".split()),
    "Java": (["java2h"], """abstract assert boolean break byte case catch char class continue default do double else enum
        extends final finally float for if implements import instanceof int interface long native new package private
        protected public return short static super switch synchronized this throw throws try void volatile while true false
        null String System""".split()),
    "Python": (["py2h"], """False None True and as assert break class continue def del elif else except finally for from
        global if import in is lambda nonlocal not or pass raise return try while with yield print range len""".split()),
    "BASIC": (["b2h"], "dim end for gosub goto if input let next print rem return step then to wend while and or not mod".split()),
    "LOGO": (["logo2h"], "forward back left right penup pendown repeat to end make if ifelse home clearscreen".split()),
    "C preprocessor": (["c2h"], "#define #include #if #ifdef #ifndef #else #elif #endif #undef #pragma #error #line".split()),
}


def keywords(lang):
    out = {}
    for name, (rev, words) in PARADIGM_WORDS.items():
        table = {k.lower(): v for k, v in burp.keyword_table(lang, rev).items()}
        missing = [w for w in words if w.lower() not in table]
        out[name] = (len(words) - len(missing), len(words), missing)
    return out


def gate_names(lang, work):
    subprocess.run([sys.executable, str(R / "lang/hindawi/burp/burp.py"), "ingest", str(R / "samples/gate"), "--langs", lang,
                    "--out", str(work)], check=True, capture_output=True)
    d = json.loads((work / lang / ".hindawi/dictionary.json").read_text(encoding="utf-8"))
    names = d.get("identifiers", {})
    latin = re.compile(r"[A-Za-z]")
    names = {k: v for k, v in names.items() if len(k) > 1}    # single letters (a, b, n, x) stay as written
    done = [k for k, v in names.items() if v != k and not latin.search(v)]
    words = sorted({w.lower() for k, v in names.items() if latin.search(v) for w in re.split(r"_|(?<=[a-z0-9])(?=[A-Z])", k) if w and not w.isdigit()})
    text = " ".join(p.read_text(encoding="utf-8", errors="replace") for p in (work / lang).rglob("*.c"))
    text = re.sub(r'/\*[\s\S]*?\*/|//[^\n]*|"(?:\\.|[^"\\\n])*"', " ", text)   # code only: comments and strings stay English
    lib = sorted({w for w in re.findall(r"\b(printf|scanf|puts|putchar|getchar|malloc|calloc|free|strlen|strcpy|strcmp|memset|"
                                       r"memcpy|sqrt|pow|abs|exit|sin|cos|exp|log|toupper|sscanf|strstr|strncmp|isdigit|isalpha|isalnum|isspace|INT_MAX)\b", text)})
    return len(done), len(names), words, lib


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--langs", required=True)
    ap.add_argument("--missing", action="store_true", help="list what is missing")
    a = ap.parse_args()
    work = Path(tempfile.mkdtemp(prefix="coverage-"))
    for lang in a.langs.split(","):
        kw = keywords(lang)
        done, total, words, lib = gate_names(lang, work)
        print(f"{lang}: " + ", ".join(f"{p} {h}/{t}" for p, (h, t, _) in kw.items())
              + f"; GATE programs: {done}/{total} names in {lang}, library calls left in English: {' '.join(lib) or 'none'}")
        if a.missing:
            for p, (_, _, miss) in kw.items():
                if miss:
                    print(f"  {p} keywords without a word: {' '.join(miss)}")
            if words:
                print(f"  words of untranslated names: {' '.join(words)}")
    shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    main()
