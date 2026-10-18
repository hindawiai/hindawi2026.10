#!/usr/bin/env python3
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""complete_cells.py: every language's eighteen transducers, complete from the language's own lexicon.

The cells as delivered carried the same 28 rules in all eighteen files, while each language's lexicon
(lang/hindawi/pipeline/language_params.json) holds a word for about 204 constructs. This regenerates each cell in the
form of Chintamani's own transducers: for every shaili, the tokens Chintamani's Hindi transducer handles plus the host
language's reserved words; for every token, the language's word for that construct (the construct is primary: one word
per construct, shared by every shaili that has it). Rules the delivered cells carried are kept where the lexicon has no
word. A word rule after the keywords stops a keyword from being replaced inside a longer name. Each cell gets a Makefile
and a driver on the original pipeline (script filter, then Romenagri, then the transducer), and STATUS.tsv, which lists
every construct that still has no word: that is the review list for the language's community.

  python3 lang/hindawi/tools/complete_cells.py [--langs a,b]     regenerate the cells and docs/hindawi/data/standards.json
  python3 lang/hindawi/tools/complete_cells.py --fill argos      first fill missing words with a translator (glossary,
                                                                  argos, llm, cmd as in BURP), marked machine-translated
"""
import argparse, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO, HIN = HERE.parents[2], HERE.parent
CELLS, PARAMS = HIN / "languages", HIN / "pipeline/language_params.json"
CHINT = REPO / ".build/chintamani/Hindawi"
# shaili: forward, reverse, Chintamani's Hindi forward transducer, the host's reserved words
SHAILIS = {
    "guru": ("h2c", "c2h", "guru/h2c.uhin", "auto break case char const continue default do double else enum extern float for goto if inline int long register restrict return short signed sizeof static struct switch typedef union unsigned void volatile while main printf scanf"),
    "shraeni": ("h2cpp", "cpp2h", "shraeni/h2cpp.uhin", "bool catch class const_cast delete dynamic_cast explicit false friend mutable namespace new operator private protected public reinterpret_cast static_cast template this throw true try typeid typename using virtual cout cin endl"),
    "yantra": ("h2asm", "asm2h", "yantra/h2y.uhin", "mov add sub mul div jmp call ret push pop cmp section global db dw dd"),
    "kritrima": ("h2java", "java2h", "kritrima/h2j.uhin", "abstract boolean byte class extends final finally implements import instanceof interface native new package private protected public super synchronized this throw throws try String System"),
    "praatha": ("h2b", "b2h", "praatha/h2b.uhin", "dim end for gosub goto if input let next print rem return step then to while wend"),
    "soochee": ("h2py", "py2h", "soochee/h2py.uhin", "and as assert break class continue def del elif else except finally for from global if import in is lambda nonlocal not or pass raise return try while with yield None True False print range len"),
    "wyaaka": ("h2yacc", "yacc2h", "wyaaka/h2yacc.uhin", "token left right nonassoc type start union"),
    "shabda": ("h2l", "l2h", "shabda/h2l.uhin", "option noyywrap yytext yyleng yylex"),
    "robot": ("h2logo", "logo2h", None, "forward back left right repeat to end make if ifelse print penup pendown home clearscreen"),
}
# host words every language's standard needs beyond what the legacy tables list
EXTRA = {"shraeni": "nullptr cout cin endl auto", "kritrima": "true false null String System super synchronized throws println",
         "soochee": "None True False print range len", "praatha": "mod and or not"}
SHAILIS = {s: v[:3] + (v[3] + " " + EXTRA.get(s, ""),) for s, v in SHAILIS.items()}
C_SHARED = {"shraeni", "kritrima", "wyaaka", "shabda"}
# vocabularies beyond the shailis, offered to each language's community for review alongside them
DOMAINS = {"hardware (VHDL, Verilog)": (HIN / "burp/paradigms/vhdl_keywords.txt"),
           "IoT and Arduino": "setup loop pinMode digitalWrite digitalRead analogRead analogWrite delay millis micros Serial begin print println HIGH LOW INPUT OUTPUT INPUT_PULLUP attachInterrupt tone",
           "robotics": "robot motor servo sensor actuator actuate move turn stop speed angle distance grip release forward back left right home",
           "AI and numerics": "tensor matrix vector shape train infer model layer weight bias activation relu sigmoid softmax loss gradient optimizer batch epoch predict"}      # their action code and expressions are C's too
WORD_OK = re.compile(r"[^\W\d][\w\u200c\u200d\u0300-\u036f\u0900-\u0dff\u0e00-\u0fff\u1000-\u109f\u1780-\u18af\u1900-\u1cff\ua800-\uabff]*")
RULE = re.compile(r'^(\S+)\s+\{\s*printf\("((?:[^"\\]|\\.)*)"\);\s*\}')
# Character and string literals pass through untouched. Chintamani's own character-literal rule, \'("\\\'"|.*)*\',
# is greedy: on a line with two character literals it swallows everything between them, keywords included. The cells
# use the standard patterns instead (DEVIATIONS.md); Hindi keeps Chintamani's transducers as they are.
STRINGS = (r"\'(\\.|[^\\\'\n])*\'" + " " * 23 + '{printf("%s",yytext);}\n'
           + r'\"(\\.|[^\\\"\n])*\"' + " " * 23 + '{printf("%s",yytext);}\n')


def chintamani_tokens(rel):
    """The English side of Chintamani's Hindi transducer: what that shaili's host needs translated."""
    p = CHINT / rel if rel else None
    if not p or not p.exists():
        return set()
    out = set()
    for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
        m = RULE.match(line.strip())
        if m:
            t = re.sub(r"\\(.)", r"\1", m.group(2))
            if re.fullmatch(r"#?[A-Za-z_][A-Za-z0-9_]*", t):
                out.add(t)
    return out


def cell_rules(path):
    rules = {}
    if path.exists():
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            m = RULE.match(line.strip())
            if m:
                rules[re.sub(r"\\(.)", r"\1", m.group(1))] = re.sub(r"\\(.)", r"\1", m.group(2))
    return rules


def esc(word):
    return re.sub(r'([\\"\[\](){}.*+?|^$/#%<>-])', r"\\\1", word)


def uhin(lang, name, pairs, src_is_english):
    lines = [f"%{{\n/* {lang} {name}.uhin: generated from the {lang} lexicon by lang/hindawi/tools/complete_cells.py,",
             "   in the form of Chintamani's own transducers. Constructs without a word are in STATUS.tsv. */\n%}\n%%", STRINGS]
    for a, b in sorted(pairs, key=lambda p: (-len(p[0]), p[0])):
        lines.append(f'{esc(a):<28}{{printf("{b.replace(chr(92), chr(92) * 2).replace(chr(34), chr(92) + chr(34))}");}}')
    lines.append('[A-Za-z_][A-Za-z0-9_]*      {printf("%s",yytext);}' if src_is_english else "")
    return "\n".join(lines) + "\n%%\n"


MAKE = """# Makefile for Hindawi {lang}, in the form of Chintamani's guru/Makefile: each transducer goes through the script
# filter and Romenagri (uni2acii, acii2cf) before flex. Generated by lang/hindawi/tools/complete_cells.py.
ROOT ?= $(abspath ../../../..)
ROMENAGRI ?= $(ROOT)/.build/chintamani/Romenagri
FILTER ?= python3 $(ROOT)/lang/hindawi/tools/script_filters.py prepare {lang}
FLEX ?= flex
ALL = {targets}
all: $(ALL)
%: %.uhin
\tcat $< | $(FILTER) | iconv -f utf-8 -t utf-16 | $(ROMENAGRI)/uni2acii | $(ROMENAGRI)/acii2cf > $@.lex
\t$(FLEX) -8 -o $@_lex.c $@.lex
\tgcc -o $@ $@_lex.c -lfl
clean:
\trm -f $(ALL) *.lex *_lex.c
"""
DRIVER = """#!/usr/bin/env bash
# {lang}cc: compile a {lang} Guru (C) program, in the form of Chintamani's hincc and gurucc: the script filter, then
# fixuninum and Romenagri, then this language's h2c, then the original driver's repairs. Generated by complete_cells.py.
DIR="$(cd "$(dirname "$0")" && pwd)"; ROOT="$(cd "$DIR/../../../.." && pwd)"
ROMENAGRI="${{ROMENAGRI:-$ROOT/.build/chintamani/Romenagri}}"; export PATH="$ROMENAGRI:$PATH"
FILTER="$(python3 "$ROOT/lang/hindawi/tools/script_filters.py" which {lang})" || {{ echo "{lang}cc: $FILTER" >&2; exit 1; }}
[ -x "$DIR/h2c" ] || make -s -C "$DIR" h2c || exit 1
cat "$1" | ${{FILTER:-cat}} | fixuninum | iconv -f utf-8 -t utf-16 | uni2acii | acii2cf | acii2uni | iconv -f UTF-16 -t UTF-8 \\
  | "$DIR/h2c" > tempfil0123.tmphin.c
sed -i 's/\\\\न/\\\\n/g; s/\\%भ/\\%f/g; s/\\%प/\\%d/g;' tempfil0123.tmphin.c
gcc tempfil0123.tmphin.c -o hin.exe -lm
"""


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--langs"); ap.add_argument("--fill")
    a = ap.parse_args()
    params = json.load(open(PARAMS, encoding="utf-8"))
    langs = sorted(d.name for d in CELLS.iterdir() if d.is_dir() and d.name != "hindi" and (d / "c2h.uhin").exists())
    if a.langs:
        langs = [l for l in langs if l in a.langs.split(",")]
    tokens = {s: chintamani_tokens(v[2]) | set(v[3].split()) for s, v in SHAILIS.items()}
    for s in C_SHARED:
        tokens[s] |= tokens["guru"]
    tr = None
    if a.fill:
        sys.path.insert(0, str(HIN / "burp")); import burp  # noqa: E402
    dom = {}
    for d, src in DOMAINS.items():
        text = src.read_text(encoding="utf-8") if isinstance(src, Path) else src
        dom[d] = sorted({w for l in text.splitlines() if not l.startswith("#") for w in l.split()})
    standards = {"constructs": {**{s: sorted(t) for s, t in tokens.items()}, **dom}, "languages": {}}
    for lang in langs:
        # a keyword is one token: a word written with spaces joins them with underscores, as names do
        lex = {k: re.sub(r"\s+", "_", v["native"].strip()) for k, v in params.get(lang, {}).items()
               if isinstance(v, dict) and v.get("native", "").strip()}
        host = set().union(*tokens.values())
        bad = {k: w for k, w in lex.items() if not WORD_OK.fullmatch(w) or w in host}
        lex = {k: w for k, w in lex.items() if k not in bad}   # a word that is not a name, or is a host token, is reported
        word, prov = {}, {}
        for t in set().union(*tokens.values(), *dom.values()):
            key = {"{": "BRACE_OPEN", "}": "BRACE_CLOSE"}.get(t, "KW_" + t.lstrip("#").upper())
            if key in lex:   # a directive keeps its #, so #if and if stay two words, as #समावेश and समावेश do
                word[t], prov[t] = ("#" if t.startswith("#") else "") + lex[key], "lexicon"
        overlay, drop_delivered = {}, False          # lang/hindawi/lexicons/<lang>.tsv: proposed words for the gaps
        ov = HIN / "lexicons" / f"{lang}.tsv"
        if ov.exists():
            for line in ov.read_text(encoding="utf-8").splitlines():
                if line.strip() == "!drop-delivered":
                    drop_delivered = True
                elif line and not line.startswith("# ") and "\t" in line:
                    t, w = line.split("\t")[:2]
                    if WORD_OK.fullmatch(w.lstrip("#")) and w not in host:
                        overlay[t] = w
        src = {t: f"lexicons/{lang}.tsv" for t in overlay}
        multi = HIN / "lexicons" / "multi.tsv"           # one table, a column per language; the language's own file wins
        if multi.exists():
            rows = [l.split("\t") for l in multi.read_text(encoding="utf-8").splitlines() if l and not l.startswith("# ")]
            col = rows[0].index(lang) if lang in rows[0] else None
            for r in rows[1:] if col else []:
                w = r[col].strip() if col < len(r) else ""
                if w and r[0] not in overlay and WORD_OK.fullmatch(w.lstrip("#")) and w not in host:
                    overlay[r[0]], src[r[0]] = w, "lexicons/multi.tsv"
        for t, w in overlay.items():
            if t not in word:
                word[t], prov[t] = w, f"proposed in {src[t]}, unreviewed"
        d = CELLS / lang
        for s, (fwd, rev, _, _) in SHAILIS.items():          # what the delivered cells knew, where the lexicon is silent
            if drop_delivered:
                break
            for k, v in cell_rules(d / f"{rev}.uhin").items():
                if k in tokens[s] and k not in word and len(k) > 1 and WORD_OK.fullmatch(v) and v not in host:
                    word[k], prov[k] = v, "delivered cell"
        if a.fill:
            tr = burp.Translator(lang, a.fill.split(","))
            for t in sorted(set().union(*tokens.values()) - set(word)):
                w = tr.phrase(t.lstrip("#"))
                if w:
                    word[t], prov[t] = re.sub(r"\s+", "_", w.strip()), "machine-translated, unreviewed"
        status = ["shaili\ttokens\twith a word\tmissing"] + [f"rejected\t{k}\t{w}\tnot a name, or the host's own token" for k, w in sorted(bad.items())]
        for s, (fwd, rev, _, _) in SHAILIS.items():
            have = {t: word[t] for t in tokens[s] if t in word}
            seen, inv = set(), []
            for t, w in sorted(have.items(), key=lambda kv: (kv[0].startswith('#'), kv[0])):
                if w not in seen:
                    seen.add(w); inv.append((w, t))
            (d / f"{rev}.uhin").write_text(uhin(lang, rev, list(have.items()), True), encoding="utf-8")
            (d / f"{fwd}.uhin").write_text(uhin(lang, fwd, inv, False), encoding="utf-8")
            missing = sorted(tokens[s] - set(have))
            status.append(f"{s}\t{len(tokens[s])}\t{len(have)}\t{' '.join(missing)}")
        (d / "STATUS.tsv").write_text("\n".join(status) + "\n", encoding="utf-8")
        (d / "Makefile").write_text(MAKE.format(lang=lang, targets=" ".join(x for v in SHAILIS.values() for x in v[:2])), encoding="utf-8")
        drv = d / f"{lang}cc"; drv.write_text(DRIVER.format(lang=lang), encoding="utf-8"); drv.chmod(0o755)
        standards["languages"][lang] = {"words": word, "provenance": prov}
        total = sum(len(tokens[s]) for s in SHAILIS); got = sum(1 for s in SHAILIS for t in tokens[s] if t in word)
        print(f"complete_cells: {lang:22} {got}/{total} token rules across the nine shailis")
    out = REPO / "docs/hindawi/data/standards.json"
    out.write_text(json.dumps(standards, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")


if __name__ == "__main__":
    main()
