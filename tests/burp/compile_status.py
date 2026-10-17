#!/usr/bin/env python3
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""compile_status.py: the compilation path, language by language. The BURP sample is ingested into each language and its
two C files are built by the sample's own Makefile through build_project.py and hindawicc, on the original pipeline (script filter, Romenagri, the language's h2c), with the
Makefile's -D flags carried through the ingestion's dictionary. The program must print what the original prints.
Writes docs/hindawi/burp-status.tsv: language, script, filter, result."""
import json, os, shutil, subprocess, sys, tempfile
from pathlib import Path
R = Path(__file__).resolve().parents[2]; SAMPLE = R / "tests/burp/sample"
sys.path.insert(0, str(R / "lang/hindawi/tools")); import script_filters  # noqa: E402
env = dict(os.environ, ROMENAGRI=str(R / ".build/chintamani/Romenagri"), HINDAWI_NATIVE_SOURCE="1")
w = Path(tempfile.mkdtemp(prefix="cstat-"))
subprocess.run(["gcc", "-O2", "-DVALUE=40", "-DLIMIT=2", f"-I{SAMPLE}/src", "-o", str(w / "orig"), str(SAMPLE / "src/main.c"), str(SAMPLE / "src/lib.c")], check=True)
want = subprocess.run([str(w / "orig")], capture_output=True).stdout
langs = sorted(p.name for p in (R / "lang/hindawi/languages").iterdir() if (p / "h2c.uhin").exists())
subprocess.run([sys.executable, str(R / "lang/hindawi/burp/burp.py"), "ingest", str(SAMPLE), "--langs", ",".join(langs), "--out", str(w / "n")],
               capture_output=True)
rows = ["language\tscript\tfilter\tresult"]
for l in langs:
    f = script_filters.which(l); script = script_filters.script_of_language(l)
    filt = "none needed" if f == "" else ("none yet" if f is None else Path(f).name)
    n = w / "n" / l; d = n / ".hindawi/dictionary.json"
    e = dict(env, HINDAWI_LANG=l, HINDAWI_DICT=str(d) if d.exists() else "")
    p = subprocess.run([sys.executable, str(R / "lang/hindawi/tools/build_project.py"), str(n), "--lang", l, "--work", str(w / "b" / l)],
                       capture_output=True, env=e, timeout=600)
    if p.returncode != 0:
        res = "no filter yet" if f is None else "does not compile"
    else:
        exe = w / "b" / l / "prog"
        res = "runs, same output" if exe.exists() and subprocess.run([str(exe)], capture_output=True).stdout == want else "builds, different output"
    rows.append(f"{l}\t{script}\t{filt}\t{res}"); print(rows[-1])
(R / "docs/hindawi/burp-status.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
shutil.rmtree(w, ignore_errors=True)
print(f"compile_status: {sum('same output' in r for r in rows)} of {len(langs)} languages build and run the sample")
