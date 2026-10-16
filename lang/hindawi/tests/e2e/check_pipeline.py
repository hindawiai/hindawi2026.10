#!/usr/bin/env python3
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""End-to-end status of the Hindawi pipeline, by execution. Reports; never gates.

Needs ROMENAGRI (a built Romenagri directory from hindawiai/chintamani), CHINTAMANI_HINDAWI
(that checkout's Hindawi directory, which carries hindrv), flex, gcc and gawk.

1. Wave 0: each Chintamani C sample through the original hincc chain
   (fixuninum | uni2acii | acii2cf | hincc.awk -> gurucc -> h2c -> gcc), compiled and run.
2. Script axis: every language's native keywords through Romenagri and back
   (iconv | uni2acii | acii2cf, then rmn2acii | acii2uni | iconv); a keyword passes only
   if it returns unchanged.
3. Guru cells: each language's h2c.uhin built the original way (uni2acii | acii2cf | flex),
   then fed its own keywords through the original front end; a keyword passes only if
   the lexer emits the C token it is declared to stand for.
"""
import json, os, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
LANGS = ROOT / "lang/hindawi/languages"
PARAMS = ROOT / "lang/hindawi/pipeline/language_params.json"
RMN = os.environ.get("ROMENAGRI", "/tmp/chintamani/Romenagri")
HIN = os.environ.get("CHINTAMANI_HINDAWI", "/tmp/chintamani/Hindawi")
ENV = dict(os.environ, PATH=f"{RMN}:{HIN}/hindrv:{HIN}/guru:" + os.environ.get("PATH", ""))


def sh(cmd, data=b"", cwd=None, timeout=60):
    p = subprocess.run(cmd, shell=True, input=data, capture_output=True, cwd=cwd, env=ENV, timeout=timeout)
    return p.returncode, p.stdout, p.stderr


def wave0():
    """Build every Chintamani shaili with its own Makefile in a scratch copy, then run every sample."""
    rows = []
    work = tempfile.mkdtemp(prefix="wave0-")
    hin = Path(work, "Hindawi")
    shutil.copytree(HIN, hin, symlinks=True)
    shailis = [d for d in sorted(hin.iterdir()) if d.is_dir() and (d / "Makefile").exists()]
    built = {d.name: sh(f"make -C '{d}'", timeout=300)[0] == 0 for d in shailis}
    env_path = f"{RMN}:{hin}/hindrv:" + ":".join(str(d) for d in shailis) + ":" + os.environ.get("PATH", "")
    for sample in sorted(Path(HIN, "samples").glob("Hindi*.uhin")):
        with tempfile.TemporaryDirectory() as d:
            shutil.copy(sample, d)
            p = subprocess.run(f"bash {hin}/hindrv/hincc {sample.name}", shell=True, capture_output=True, cwd=d,
                               env=dict(ENV, PATH=env_path), timeout=120)
            rc = p.returncode
            # hincc writes the host source as tempfil0123.tmphin.<ext>: .c, .cpp, .asm, .bas, .lex, .yacc ...
            made = [p for p in Path(d).glob("tempfil0123.tmphin.*") if p.stat().st_size > 0]
            ran = Path(d, "hin.exe").exists() and sh("./hin.exe < /dev/null", cwd=d, timeout=10)[0] == 0
            rows.append((sample.name, ",".join(sorted(p.suffix for p in made)) or "none", ran))
    shutil.rmtree(work, ignore_errors=True)
    print("  shailis built with their own Makefiles: " + ", ".join(f"{k} {'yes' if v else 'NO'}" for k, v in built.items()))
    return rows


def forward(word):
    return sh("iconv -f utf-8 -t utf-16 | uni2acii | acii2cf", word.encode())[1].decode("utf-8", "replace").strip()


def back(roman):
    return sh("rmn2acii | acii2uni | iconv -f utf-16 -t utf-8", roman.encode())[1].decode("utf-8", "replace").strip()


def main():
    for tool in ("flex", "gcc", "gawk"):
        if not shutil.which(tool, path=ENV["PATH"]):
            print(f"cannot judge: {tool} is not installed"); return 3
    if not Path(RMN, "uni2acii").exists():
        print(f"cannot judge: no built Romenagri at {RMN} (set ROMENAGRI)"); return 3
    print("Wave 0, the original Hindi pipeline on every Chintamani sample:")
    for name, made, ran in wave0():
        print(f"  {name:28} host source written: {made:6}  compiled and ran: {'yes' if ran else 'no'}")
    if "--wave0" in sys.argv[1:]:
        return 0
    params = json.loads(PARAMS.read_text(encoding="utf-8"))
    print("\nPer language: keywords that survive Romenagri unchanged; Guru keywords its own lexer recognises")
    print(f"  {'language':22} {'round trip':>12} {'guru lexer':>12}")
    totals = [0, 0, 0, 0]
    for lang in sorted(params):
        kws = {cid: e["native"] for cid, e in params[lang].items() if isinstance(e, dict) and e.get("native")}
        ok = sum(1 for w in kws.values() if back(forward(w)) == w)
        cell = LANGS / lang / "h2c.uhin"
        lex_ok = lex_n = 0
        if cell.exists():
            with tempfile.TemporaryDirectory() as d:
                rc = sh(f"cat '{cell}' | iconv -f utf-8 -t utf-16 | uni2acii | acii2cf > h2c.lex && flex -o lexyy.c -8 h2c.lex "
                        f"&& gcc -o h2c lexyy.c -lfl", cwd=d)[0]
                if rc == 0:
                    rules = {}
                    for line in cell.read_text(encoding="utf-8", errors="replace").splitlines():
                        parts = line.split()
                        if len(parts) >= 2 and parts[1].startswith('{printf("') and parts[0] not in rules:
                            rules[parts[0]] = parts[1][len('{printf("'):].split('"')[0]
                    for word, token in rules.items():
                        if not any(ord(ch) > 127 for ch in word):
                            continue
                        lex_n += 1
                        out = sh(f"iconv -f utf-8 -t utf-16 | uni2acii | acii2cf | acii2uni | iconv -f utf-16 -t utf-8 | {d}/h2c",
                                 word.encode())[1].decode("utf-8", "replace").strip()
                        lex_ok += out == token
        totals[0] += ok; totals[1] += len(kws); totals[2] += lex_ok; totals[3] += lex_n
        print(f"  {lang:22} {ok:>5}/{len(kws):<6} {lex_ok:>5}/{lex_n:<6}")
    print(f"\n  all languages: round trip {totals[0]}/{totals[1]}; guru lexers {totals[2]}/{totals[3]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
