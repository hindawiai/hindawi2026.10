#!/usr/bin/env python3
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""measure.py: how much of an ingested project is localised, per language and paradigm. The target is 100%.

  python3 scripts/sovereign/measure.py SRC OUT [--tsv FILE] [--json FILE]

SRC is the upstream tree as fetched; OUT is BURP's output for it (OUT/<language>/...). For every source file it
counts, outside literals and comments:
  keywords      reserved words of the file's paradigm, and how many of them the language's transducer localises
  identifiers   names the project defines, and how many the dictionary gave a native name
  comments      comment blocks, and how many were translated
Keywords are the transducers' coverage; identifiers and comments are the translators' coverage.
"""
import argparse, json, keyword, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "lang/hindawi/burp"))
import burp  # noqa: E402

C = set("""auto break case char const continue default do double else enum extern float for goto if inline int long
register restrict return short signed sizeof static struct switch typedef union unsigned void volatile while""".split())
RESERVED = {"guru": C, "wyaaka": C, "shabda": C,
            "shraeni": C | set("""bool catch class const_cast delete dynamic_cast explicit false friend mutable namespace
                new operator private protected public reinterpret_cast static_cast template this throw true try typeid
                typename using virtual""".split()),
            "kritrima": set("""abstract assert boolean break byte case catch char class const continue default do double
                else enum extends final finally float for goto if implements import instanceof int interface long native
                new package private protected public return short static super switch synchronized this throw throws
                try void volatile while""".split()),
            "soochee": set(keyword.kwlist),
            "praatha": set("""dim end for gosub goto if input let next print rem return step then to while wend""".split()),
            "robot": set("""forward back left right repeat to end make if ifelse print""".split()),
            "vhdl": burp.VHDL_WORDS, "yantra": set()}


def measure(src, folder):
    d = json.loads((folder / burp.DICT_NAME).read_text(encoding="utf-8"))
    rows, comments_total = {}, 0
    for f in sorted(p for p in Path(src).rglob("*") if p.is_file() and p.suffix in burp.PARADIGMS):
        shaili, rev, style = burp.PARADIGMS[f.suffix]
        table = {k.lower() if style in ("vhdl", "basic") else k: v for k, v in burp.keyword_table(d["language"], rev).items()}
        r = rows.setdefault(shaili, {"files": 0, "keywords": 0, "localised": 0, "comments": 0})
        r["files"] += 1
        text = f.read_text(encoding="utf-8", errors="replace")
        for m in burp.scanner(style).finditer(text):
            if m.lastgroup == "com":
                r["comments"] += 1
            w = m.group("word")
            if not w:
                continue
            key = w.lower() if style in ("vhdl", "basic") else w
            if key in RESERVED.get(shaili, set()):
                r["keywords"] += 1
                r["localised"] += key in table
        comments_total += r["comments"]
    ids = d.get("identifiers", {})
    named = sum(1 for k, v in ids.items() if v != k)
    pct = lambda a, b: round(100 * a / b, 1) if b else None
    kw_all = sum(r["keywords"] for r in rows.values()); kw_loc = sum(r["localised"] for r in rows.values())
    com_all = sum(r["comments"] for r in rows.values())
    return {"language": d["language"], "script": d.get("rendered", {}).get("to", d.get("script")),
            "keywords_pct": pct(kw_loc, kw_all), "identifiers_pct": pct(named, len(ids)),
            "comments_pct": pct(len(d.get("comments", {})), com_all),
            "paradigms": {s: {"files": r["files"], "keywords_pct": pct(r["localised"], r["keywords"])} for s, r in rows.items()}}


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("src"); ap.add_argument("out")
    ap.add_argument("--tsv"); ap.add_argument("--json"); ap.add_argument("--project", default="")
    a = ap.parse_args()
    results = [measure(a.src, f) for f in sorted(Path(a.out).iterdir()) if (f / burp.DICT_NAME).exists()]
    lines = ["project\tlanguage\tscript\tkeywords_%\tidentifiers_%\tcomments_%\tparadigms"]
    for r in results:
        par = " ".join(f"{s}:{v['keywords_pct']}" for s, v in sorted(r["paradigms"].items()))
        lines.append(f"{a.project}\t{r['language']}\t{r['script']}\t{r['keywords_pct']}\t{r['identifiers_pct']}\t{r['comments_pct']}\t{par}")
    print("\n".join(lines))
    if a.tsv:
        Path(a.tsv).write_text("\n".join(lines[1:]) + "\n", encoding="utf-8")
    if a.json:
        Path(a.json).write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")
