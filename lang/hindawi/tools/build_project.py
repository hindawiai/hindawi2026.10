#!/usr/bin/env python3
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""build_project.py: build a native tree with the project's own build system, through the compilation path.

Every C and C++ source and header of the native tree goes through hindawi_chain.to_c into a build tree (headers
too, so every #include meets C), files renamed at ingestion get their original names back, and the project's own
make runs there with CC=hindawicc, which maps every -D and -U name through the same dictionary.

  python3 build_project.py NATIVE_TREE --lang hindi [--work DIR] [-- make arguments]
"""
import argparse, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import hindawi_chain as chain

EXTS = {".c", ".h", ".cc", ".cpp", ".cxx", ".hpp"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tree"); ap.add_argument("--lang", default="hindi"); ap.add_argument("--work")
    a, make = ap.parse_known_args()   # everything else goes to make
    tree = Path(a.tree).resolve(); work = Path(a.work or tempfile.mkdtemp(prefix="hindawi-build-")).resolve()
    dpath = tree / ".hindawi" / "dictionary.json"
    d = json.loads(dpath.read_text(encoding="utf-8")) if dpath.exists() else {"files": {}}
    back = {v: k for k, v in d.get("files", {}).items()}
    excluded = d.get("excluded", [])
    # assembly and linker scripts name C symbols too: they get each translated name's C-level form
    fwd = {o: nv for o, nv in d.get("forward", {}).items() if o != nv}
    forms = chain.c_names(sorted(set(fwd.values())), a.lang) if fwd else {}
    sym = {o: forms[nv] for o, nv in fwd.items() if forms.get(nv)}
    # a symbol in assembly or a linker script; never a piece of a path or a file name (kernel/entry.o stays itself)
    word = re.compile(r"(?<![\w/.])[A-Za-z_][A-Za-z0-9_]*(?![\w/.])")
    n = 0
    for p in sorted(tree.rglob("*")):
        if not p.is_file() or ".hindawi" in p.parts:
            continue
        rel = str(p.relative_to(tree)); dst = work / back.get(rel, rel)
        dst.parent.mkdir(parents=True, exist_ok=True)
        if p.suffix.lower() in EXTS and not any(rel.startswith(x) for x in excluded):
            c = chain.to_c(p.read_text(encoding="utf-8", errors="replace"), a.lang)
            for native, orig in back.items():   # quoted #include of a renamed file
                c = c.replace(f'"{Path(native).name}"', f'"{Path(orig).name}"')
            dst.write_text(c, encoding="utf-8"); n += 1
        elif sym and p.suffix in (".S", ".s", ".lds", ".ld") and not any(rel.startswith(x) for x in excluded):
            t = p.read_text(encoding="utf-8", errors="replace")
            dst.write_text(word.sub(lambda m: sym.get(m.group(0), m.group(0)), t), encoding="utf-8")
        else:
            shutil.copy2(p, dst)
    cc = Path(__file__).resolve().parents[1] / "hindawicc"
    env = dict(os.environ, HINDAWI_LANG=a.lang, HINDAWI_NATIVE_SOURCE="0")
    if dpath.exists():
        env["HINDAWI_DICT"] = str(dpath)
    make = [m for m in make if m != "--"]
    print(f"build_project: {n} sources and headers through the compilation path into {work}")
    r = subprocess.run(["make", f"CC={cc}"] + make, cwd=work, env=env)
    print(f"build_project: make exited {r.returncode}")
    sys.exit(r.returncode)


if __name__ == "__main__":
    main()
