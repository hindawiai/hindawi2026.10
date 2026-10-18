#!/usr/bin/env python3
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""check_notebooks.py: the notebooks are real. Every notebook has Chintamani's structure (installation, the practice
area, and per shaili the program, input, compilation flow, execution and Std2Hin cells), and its demos build through
the original pipeline and print what the English originals print.
  python3 tests/check_notebooks.py              structure of every notebook, and the demos run for three languages
  python3 tests/check_notebooks.py --json       the demos for every language with a compilation path, as JSON
"""
import json, os, subprocess, sys
from pathlib import Path
R = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(R / "lang/hindawi"))


def demo_results(langs):
    import nb
    want = {"guru": subprocess.run(["sh", "-c", f"gcc -O2 -o /tmp/nb-eng '{R}/samples/gate/algorithms/searching/binary_search.c' && /tmp/nb-eng"],
                                   capture_output=True, text=True).stdout,
            "soochee": subprocess.run([sys.executable, str(R / "samples/gate/paradigms/binary_search.py")], capture_output=True, text=True).stdout}
    res = {}
    for L in langs:
        res[L] = {}
        for s in ("guru", "soochee"):
            try:
                ok, msg, art = nb.build(nb.demos(L, s)["binary_search"], L, s)
                out = nb.run(art, s) if ok else msg
                res[L][s] = [out == want[s], out.strip()[:80]]
            except Exception as e:
                res[L][s] = [False, f"{type(e).__name__}: {e}"[:120]]
    return res


def compile_langs():
    t = (R / "docs/hindawi/burp-status.tsv").read_text(encoding="utf-8").splitlines()[1:]
    return sorted({l.split("\t")[0] for l in t if l.split("\t")[3:4] == ["runs, same output"]} | {"hindi"})


if "--json" in sys.argv:
    print(json.dumps(demo_results(compile_langs()), ensure_ascii=False)); sys.exit(0)

failed, passed = [], 0
def check(name, ok, detail=""):
    global passed
    if ok: passed += 1
    else: failed.append(name); print(f"  FAIL  {name}" + (f": {detail}" if detail else ""))

verified = json.loads((R / "notebooks/verified.json").read_text(encoding="utf-8"))
for L, v in verified.items():
    shailis = [s for s, (ok, _) in v.items() if ok]
    f = R / "notebooks" / L / f"hindawi_{L}.ipynb"
    if not shailis:
        check(f"{L}: no notebook without a verified shaili", not f.exists()); continue
    nbk = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {"cells": []}
    src = ["".join(c["source"]) for c in nbk["cells"]]
    check(f"{L}: notebook exists", f.exists())
    check(f"{L}: installation cell", any("#@title Installation" in s and "scripts/build.sh" in s for s in src))
    check(f"{L}: practice area (NB UI)", any(s.startswith("#@title Practice area") and "nb.ide(" in s for s in src))
    for s in shailis:
        check(f"{L}/{s}: program, input, flow, execution and Std2Hin cells",
              any(x.startswith("%%writefile program_" + s) for x in src) and any(f"open('input_{s}.txt', 'w'" in x for x in src)
              and any("nb.show_stages(" in x and repr(s) in x for x in src) and any("nb.build_and_run(" in x and repr(s) in x for x in src)
              and any("nb.from_host(" in x and repr(s) in x for x in src))
    check(f"{L}: Open in Colab link on the page", f"notebooks/{L}/hindawi_{L}.ipynb" in (R / "docs/hindawi/notebooks.html").read_text(encoding="utf-8"))
if os.path.isfile(R / ".build/chintamani/Romenagri/acii2cf"):
    for L, v in demo_results(["urdu", "telugu", "hindi"]).items():
        for s, (ok, out) in v.items():
            check(f"{L}/{s}: the demo builds through the original pipeline and prints what English prints", ok, out)
else:
    print("  UNJUDGED  demos: the Romenagri tools are not built here (hindawi setup builds them)")
print(f"notebooks: {passed} passed, {len(failed)} failed")
sys.exit(1 if failed else 0)
