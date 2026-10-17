#!/usr/bin/env python3
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""run.py: the GATE programs in a language. samples/gate is ingested by BURP into each language; every C program is
then compiled from the language through the original pipeline (script filter, Romenagri, the language's h2c) and run,
and must print exactly what the English original prints. The other paradigms are ingested and reversed byte for byte.

  python3 tests/gate/run.py --langs sanskrit [--gallery]     --gallery copies the ingested programs to docs/hindawi/samples/
"""
import argparse, filecmp, json, os, shutil, subprocess, sys, tempfile
from pathlib import Path
R = Path(__file__).resolve().parents[2]; SRC = R / "samples/gate"
ENV = dict(os.environ, ROMENAGRI=str(R / ".build/chintamani/Romenagri"), HINDAWI_NATIVE_SOURCE="1")
ap = argparse.ArgumentParser(); ap.add_argument("--langs", default="sanskrit"); ap.add_argument("--gallery", action="store_true")
a = ap.parse_args()
w = Path(tempfile.mkdtemp(prefix="gate-"))
burp = [sys.executable, str(R / "lang/hindawi/burp/burp.py")]
subprocess.run(burp + ["ingest", str(SRC), "--langs", a.langs, "--out", str(w / "n")], check=True, capture_output=True)
programs = sorted(p.relative_to(SRC) for p in SRC.rglob("*.c"))
want = {}
for p in programs:
    exe = w / "orig"; subprocess.run(["gcc", "-O2", "-o", str(exe), str(SRC / p), "-lm"], check=True)
    want[p] = subprocess.run([str(exe)], capture_output=True, timeout=20).stdout
failed = 0
for lang in a.langs.split(","):
    n = w / "n" / lang; ok = 0
    env = dict(ENV, HINDAWI_LANG=lang, HINDAWI_DICT=str(n / ".hindawi/dictionary.json"))
    for p in programs:
        exe = w / "native"
        c = subprocess.run([str(R / "lang/hindawi/hindawicc"), "-O2", "-o", str(exe), str(n / p), "-lm"], capture_output=True, env=env)
        got = subprocess.run([str(exe)], capture_output=True, timeout=20).stdout if c.returncode == 0 else None
        if got == want[p]:
            ok += 1
        else:
            failed += 1
            print(f"  {lang}: {p}: " + ("does not compile: " + c.stderr.decode("utf-8", "replace").strip().splitlines()[0][:150] if c.returncode else "prints something else"))
    back = w / "back" / lang
    subprocess.run(burp + ["reverse", str(n), "--out", str(back)], check=True, capture_output=True)
    same = sum(filecmp.cmp(SRC / f, back / f, shallow=False) for f in (p.relative_to(SRC) for p in SRC.rglob("*") if p.is_file()))
    total = sum(1 for p in SRC.rglob("*") if p.is_file())
    print(f"gate: {lang}: {ok} of {len(programs)} C programs compile from {lang} and print what the originals print; "
          f"{same} of {total} files reverse byte for byte")
    if a.gallery:
        dst = R / "docs/hindawi/samples" / lang
        shutil.rmtree(dst, ignore_errors=True); shutil.copytree(n, dst, ignore=shutil.ignore_patterns(".hindawi"))
        shutil.copy(n / ".hindawi/dictionary.json", dst / "dictionary.json")
shutil.rmtree(w, ignore_errors=True)
sys.exit(1 if failed else 0)
