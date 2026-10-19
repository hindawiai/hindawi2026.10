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

EXTS = {".c", ".h", ".cc", ".cpp", ".cxx", ".hpp", ".hh"}
CPP = {".cc", ".cpp", ".cxx", ".hpp", ".hh"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tree"); ap.add_argument("--lang", default="hindi"); ap.add_argument("--work")
    ap.add_argument("--lower-only", action="store_true", help="write the lowered tree and stop: the project then builds with its own tools")
    ap.add_argument("--cxx", action="store_true", help="a C++ project: headers are C++, lowered with the language's h2cpp")
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
    pending = []
    for p in sorted(tree.rglob("*")):
        if not p.is_file() or ".hindawi" in p.parts:
            continue
        rel = str(p.relative_to(tree)); dst = work / back.get(rel, rel)
        dst.parent.mkdir(parents=True, exist_ok=True)
        if p.suffix.lower() in EXTS and not any(rel.startswith(x) for x in excluded):
            pending.append((p, dst))            # lowered together below: one transliteration for the whole tree
        elif sym and p.suffix in (".S", ".s", ".lds", ".ld") and not any(rel.startswith(x) for x in excluded):
            t = p.read_text(encoding="utf-8", errors="replace")
            dst.write_text(word.sub(lambda m: sym.get(m.group(0), m.group(0)), t), encoding="utf-8")
        else:
            shutil.copy2(p, dst)
    # C through h2c; C++ (and, in a C++ project, every header) through h2cpp: each group lowered as a whole
    is_cpp = lambda p: p.suffix.lower() in CPP or (a.cxx and p.suffix.lower() == ".h")
    lowered = {}
    for fwdname, group in (("h2c", [x for x in pending if not is_cpp(x[0])]), ("h2cpp", [x for x in pending if is_cpp(x[0])])):
        if group:
            texts = [p.read_text(encoding="utf-8", errors="replace") for p, _ in group]
            lowered.update(zip((d for _, d in group), chain.lower_many(texts, a.lang, fwdname)))
    for p, dst in pending:
        c = lowered[dst]
        for native, orig in back.items():   # quoted #include of a renamed file
            c = c.replace(f'"{Path(native).name}"', f'"{Path(orig).name}"')
        dst.write_text(c, encoding="utf-8"); n += 1
    cc = Path(__file__).resolve().parents[1] / "hindawicc"
    env = dict(os.environ, HINDAWI_LANG=a.lang, HINDAWI_NATIVE_SOURCE="0")
    if dpath.exists():
        env["HINDAWI_DICT"] = str(dpath)
    make = [m for m in make if m != "--"]
    print(f"build_project: {n} sources and headers through the compilation path into {work}")
    if a.lower_only:
        sys.exit(0)
    r = subprocess.run(["make", f"CC={cc}"] + make, cwd=work, env=env)
    print(f"build_project: make exited {r.returncode}")
    sys.exit(r.returncode)


if __name__ == "__main__":
    main()
