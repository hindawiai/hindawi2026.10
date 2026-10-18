#!/usr/bin/env python3
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""standard_import.py: a filled language work package, back into the language's standard.

  hindawi standard import LANG keywords.tsv [names.tsv] --by "name"

Each word is checked: it is written in the language's script, it is one token (a phrase joined by underscores, a
directive keeping its #), it is not a host keyword, and no two entries of one file share a word. Words that pass go
into lang/hindawi/lexicons/LANG.tsv (keywords) and lang/hindawi/burp/glossary/LANG.tsv (names), each with its
contributor; anything refused is listed with the reason. Then the language's cell and standard are regenerated.
"""
import argparse, subprocess, sys, unicodedata
from pathlib import Path

R = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(R / "lang/hindawi/tools")); sys.path.insert(0, str(R / "lang/hindawi/burp"))
import complete_cells, script_filters  # noqa: E402


def script_ok(word, script):
    letters = [unicodedata.name(c, "?").split(" ")[0] for c in word if c.isalpha()]
    return bool(letters) and max(set(letters), key=letters.count) == script


def read(path):
    rows = [l.rstrip("\n").split("\t") for l in Path(path).read_text(encoding="utf-8").splitlines() if l.strip()]
    return [(r[0], r[-1].strip()) for r in rows[1:] if len(r) >= 2 and r[-1].strip()]


def merge(target, entries, by, kind):
    target.parent.mkdir(parents=True, exist_ok=True)
    have = {}
    if target.exists():
        for l in target.read_text(encoding="utf-8").splitlines():
            if "\t" in l and not l.startswith("# "):
                have[l.split("\t")[0]] = l
    for k, w in entries:
        have[k] = f"{k}\t{w}\t# {kind} by {by}"
    head = [l for l in (target.read_text(encoding="utf-8").splitlines() if target.exists() else []) if l.startswith("#") and "\t" not in l]
    target.write_text("\n".join(head + list(have.values())) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lang"); ap.add_argument("keywords"); ap.add_argument("names", nargs="?")
    ap.add_argument("--by", required=True, help="who proposed these words")
    a = ap.parse_args()
    script = script_filters.script_of_language(a.lang)
    host = set().union(*({t for t in v[3].split()} for v in complete_cells.SHAILIS.values()))
    accepted, refused = {"keywords": [], "names": []}, []
    for kind, path in (("keywords", a.keywords), ("names", a.names)):
        if not path:
            continue
        seen = {}
        for key, word in read(path):
            bare = word.lstrip("#")
            why = ("not one token" if not complete_cells.WORD_OK.fullmatch(bare) else
                   f"not in the {script.title()} script" if not script_ok(bare, script) else
                   "a host keyword" if word in host else
                   f"the same word as {seen[word]}" if word in seen else
                   "a directive must keep its #" if key.startswith("#") != word.startswith("#") else "")
            if why:
                refused.append(f"{kind}: {key} = {word}: {why}")
            else:
                seen[word] = key; accepted[kind].append((key, word))
    merge(R / f"lang/hindawi/lexicons/{a.lang}.tsv", accepted["keywords"], a.by, "proposed")
    if accepted["names"]:
        merge(R / f"lang/hindawi/burp/glossary/{a.lang}.tsv", accepted["names"], a.by, "proposed")
    for r in refused:
        print(f"  refused  {r}")
    print(f"standard import: {a.lang}: {len(accepted['keywords'])} keywords and {len(accepted['names'])} names taken, {len(refused)} refused")
    for cmd in ([sys.executable, R / "lang/hindawi/tools/complete_cells.py", "--langs", a.lang],
                [sys.executable, R / "lang/hindawi/tools/standards.py", "--langs", a.lang],
                [sys.executable, R / "lang/hindawi/tools/coverage.py", "--langs", a.lang]):
        subprocess.run([str(c) for c in cmd])


if __name__ == "__main__":
    main()
