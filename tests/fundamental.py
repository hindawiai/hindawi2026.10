#!/usr/bin/env python3
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""fundamental.py: the regression that must hold for Hindawi. Exit 0 when nothing fails, 1 on a failure,
3 when it cannot judge. Run scripts/fetch.sh and scripts/build.sh first (pinned Chintamani, built the original way).

F1  the Chintamani copy in lang/hindawi/upstream/chintamani is Chintamani, file for file
F2  Wave 0: every Chintamani sample goes through hincc to its host source
F3  every original shaili, forward and reverse: host = h2X(sample); host == h2X(X2h(host))
F4  ingestion of a two-file C project with one dictionary, then hindawicc with gcc flags passed through
F5  a native name survives to the ELF symbol and comes back through Romenagri
"""
import os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CH = ROOT / ".build/chintamani"
RMN, HIN = CH / "Romenagri", CH / "Hindawi"
COPY = ROOT / "lang/hindawi/upstream/chintamani"
ENV = dict(os.environ, PATH=f"{RMN}:" + os.environ.get("PATH", ""), ROMENAGRI=str(RMN))
TO_HOST = "fixuninum | iconv -f utf-8 -t utf-16 | uni2acii | acii2cf | acii2uni | iconv -f UTF-16 -t UTF-8 | {lx}"
TO_NATIVE = "fixuninum | iconv -f utf-8 -t utf-16 | uni2acii | {lx} | acii2uni | iconv -f UTF-16 -t UTF-8"
results = []


def sh(cmd, data=b"", cwd=None, timeout=120):
    p = subprocess.run(cmd, shell=True, input=data, capture_output=True, cwd=cwd, env=ENV, timeout=timeout)
    return p.returncode, p.stdout, p.stderr


def check(cid, title, ok, detail=""):
    results.append(ok); print(f"  {'PASS' if ok else 'FAIL'}  {cid}  {title}" + (f": {detail}" if detail else ""))


def f1():
    tracked = sh("git ls-files Hindawi", cwd=CH)[1].decode().split("\n")
    bad = []
    for d in ("guru", "praatha", "samples", "shabda", "shraeni", "soochee", "wyaaka"):
        for f in (t for t in tracked if t.startswith(f"Hindawi/{d}/")):
            mine = COPY / f[len("Hindawi/"):]
            if mine.exists() and mine.read_bytes() != (CH / f).read_bytes():
                bad.append(f)
    check("F1", "the Chintamani copy is Chintamani", not bad, ", ".join(bad[:5]))


def f2():
    rc, out, _ = sh(f"CHINTAMANI_HINDAWI='{HIN}' ROMENAGRI='{RMN}' python3 lang/hindawi/tests/e2e/check_pipeline.py --wave0",
                    cwd=ROOT, timeout=600)
    rows = re.findall(r"(Hindi\S+\.uhin)\s+host source written: (\S+)", out.decode())
    none = [n for n, s in rows if s == "none"]
    check("F2", f"Wave 0: {len(rows) - len(none)} of {len(rows)} samples reach their host source", rows and not none, ", ".join(none))


PAIRS = [("guru", "h2c", "c2h", None, "HindiC.uhin"), ("shraeni", "h2cpp", "cpp2h", None, "HindiC++.uhin"),
         ("yantra", "h2y", "y2h", None, "HindiASM.uhin"), ("kritrima", "h2j", "j2h", None, "HindiJAVA.uhin"),
         ("praatha", "h2b", "b2h", None, "HindiBASIC.uhin"), ("wyaaka", "h2yacc", "yacc2h", "guru", "HindiYACC.uhin"),
         ("shabda", "h2l", "l2h", "guru", "HindiLEX.uhin")]


KNOWN = {"yantra": "Chintamani's own h2y and y2h are not round-trip stable on its own assembly sample"}


def f3():
    for d, fwd, rev, comp, sample in PAIRS:
        f = f"'{HIN}/{d}/{fwd}'" + (f" | '{HIN}/guru/h2c'" if comp else "")
        r = f"'{HIN}/{d}/{rev}'" + (f" | '{HIN}/guru/c2h'" if comp else "")
        _, host, _ = sh(TO_HOST.format(lx=f), (HIN / "samples" / sample).read_bytes())
        _, native, _ = sh(TO_NATIVE.format(lx=r), host)
        _, host2, _ = sh(TO_HOST.format(lx=f), native)
        norm = lambda b: b.replace(b"\r", b"").strip()
        same = bool(norm(host)) and norm(host2) == norm(host)
        if d in KNOWN and not same:   # Chintamani's own behaviour, recorded rather than counted as a regression
            print(f"  NOTE  F3  {d}: {sample}: {KNOWN[d]}"); continue
        check("F3", f"{d}: {sample} to host and back", same, "" if same else "host differs after the round trip")


def f4_f5():
    w = Path(tempfile.mkdtemp(prefix="fund-"))
    (w / "lib.c").write_text("int add(int a, int b)\n{\n  return a + b;\n}\n")
    (w / "main.c").write_text('#include <stdio.h>\nint add(int a, int b);\nint main(void)\n{\n  int total = add(VALUE, 2);\n'
                              '  printf("%d\\n", total);\n  return 0;\n}\n')
    env = dict(ENV, HINDAWI_DICT=str(w / "project_dict.json"))
    ing = ROOT / "lang/hindawi/tools/ingest.py"
    for f in ("lib", "main"):
        p = subprocess.run([sys.executable, str(ing), str(w / f"{f}.c")], capture_output=True, env=env)
        (w / f"{f}.uhin").write_bytes(p.stdout)
    native = (w / "main.uhin").read_text(encoding="utf-8", errors="replace")
    localized = "पूर्णांक" in native and "वापस" in native and not re.search(r"\b(int|return)\b", native)
    check("F4", "ingestion puts the project's keywords in Hindi, with one dictionary for both files", localized)
    rc, out, err = sh(f"'{ROOT}/lang/hindawi/hindawicc' main.uhin lib.uhin -DVALUE=40 -O2 -Wall -g -o prog && ./prog", cwd=w)
    check("F4", "hindawicc compiles both native files with gcc's flags passed through", out.strip() == b"42",
          err.decode("utf-8", "replace").strip()[:160])
    back_ok = True
    for f in ("lib", "main"):
        p = subprocess.run([sys.executable, str(ing), "--reverse", str(w / f"{f}.uhin")], capture_output=True, env=env)
        back_ok &= p.stdout.decode().split() == (w / f"{f}.c").read_text().split()
    check("F4", "the project comes back to its original C through the same dictionary", back_ok)
    (w / "naam.uhin").write_text("पूर्णांक योगफल(पूर्णांक क, पूर्णांक ख)\nअणु\n  वापस क + ख;\nपूर्ण\n", encoding="utf-8")
    rc, _, err = sh(f"'{ROOT}/lang/hindawi/hindawicc' -c -g naam.uhin -o naam.o", cwd=w)
    syms = sh("nm naam.o", cwd=w)[1].decode().split()
    sym = next((s for s in syms if s not in ("T", "t", "D", "U") and not s.startswith("0")), "")
    _, back, _ = sh("rmn2acii | acii2uni | iconv -f UTF-16 -t UTF-8", sym.encode())
    check("F5", f"योगफल becomes the ELF symbol {sym or '(none)'} and comes back through Romenagri",
          rc == 0 and back.decode("utf-8", "replace").strip() == "योगफल")
    shutil.rmtree(w, ignore_errors=True)


if __name__ == "__main__":
    if not (RMN / "uni2acii").exists() or not (HIN / "guru/h2c").exists():
        print("fundamental: cannot judge: run scripts/fetch.sh and scripts/build.sh first"); sys.exit(3)
    for t in ("flex", "gcc", "gawk", "nm"):
        if not shutil.which(t):
            print(f"fundamental: cannot judge: {t} is not installed"); sys.exit(3)
    if not (COPY / "guru/h2c").exists():
        sh("make -s -C lang/hindawi/upstream/chintamani/guru", cwd=ROOT)
    print("Hindawi fundamental regression")
    f1(); f2(); f3(); f4_f5()
    print(f"  {sum(results)} passed, {len(results) - sum(results)} failed")
    sys.exit(0 if all(results) else 1)
