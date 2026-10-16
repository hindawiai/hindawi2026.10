#!/usr/bin/env python3
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""cells.py: Hindawi language cells measured by execution. It reports status; it never gates.

  cells.py roundtrip --cells DIR --corpus DIR [--langs a,b] [--json OUT]
      Every folder in DIR holding h2c.uhin and c2h.uhin is a language's Guru cell. Each is built the original
      way (iconv | uni2acii | acii2cf | flex | gcc), every C file of the corpus is carried to the language (c2h)
      and back (h2c) through the original chain, and the report gives, per language: files that come back byte
      for byte (the 2004 transducers write CRLF, which is set aside), whether the native text is valid UTF-8,
      the share of its letters in the language's own script, and the share of C keywords carried.
  cells.py tree --cell DIR --src DIR
      Carries every .c and .h under SRC through one cell and back, in place. SeaBIOS is built from the result.

Needs ROMENAGRI (a built Romenagri folder), flex, gcc and iconv.
"""
import argparse, json, os, re, shutil, subprocess, sys, tempfile, unicodedata
from collections import Counter
from multiprocessing import Pool
from pathlib import Path

RMN = os.environ.get("ROMENAGRI", "")
ENV = dict(os.environ, PATH=f"{RMN}:" + os.environ.get("PATH", ""))
FWD = "fixuninum | iconv -f utf-8 -t utf-16 | uni2acii | {c2h} | acii2uni | iconv -f UTF-16 -t UTF-8"
REV = "fixuninum | iconv -f utf-8 -t utf-16 | uni2acii | acii2cf | acii2uni | iconv -f UTF-16 -t UTF-8 | {h2c}"
C_KEYWORDS = re.compile(rb"\b(int|char|void|if|else|while|for|return|struct|static|const|unsigned|switch|case|break|"
                        rb"continue|sizeof|typedef|enum|union|extern|long|short|signed|do|goto|default|volatile|inline)\b")


def run(cmd, data=b"", cwd=None, timeout=60):
    p = subprocess.run(cmd, shell=True, input=data, capture_output=True, cwd=cwd, env=ENV, timeout=timeout)
    return p.returncode, p.stdout, p.stderr


def build_cell(src, work):
    """Copy a cell and build its Guru pair with the original commands; return (ok, message)."""
    shutil.copytree(src, work, dirs_exist_ok=True)
    for t in ("h2c", "c2h"):
        rc, _, err = run(f"cat {t}.uhin | iconv -f utf-8 -t utf-16 | uni2acii | acii2cf > {t}.lex && "
                         f"flex -o {t}_lex.c -8 {t}.lex && gcc -o {t} {t}_lex.c -lfl", cwd=work, timeout=120)
        if rc != 0:
            return False, f"{t} does not build: {err.decode('utf-8', 'replace').strip().splitlines()[-1:]}"
    return True, "built"


def script_of(text):
    names = Counter(unicodedata.name(c, "?").split(" ")[0] for c in text if ord(c) > 0x7F and c.isalpha())
    return names.most_common(1)[0][0] if names else None


def carry(cell, data):
    _, native, _ = run(FWD.format(c2h=f"'{cell}/c2h'"), data)
    _, back, _ = run(REV.format(h2c=f"'{cell}/h2c'"), native)
    return native, back.replace(b"\r", b"")


def measure(args):
    name, cell_src, corpus, work_root = args
    work = Path(work_root, name)
    ok, msg = build_cell(cell_src, work)
    row = {"language": name, "built": ok, "note": msg}
    if not ok:
        return row
    script = script_of((work / "h2c.uhin").read_text(encoding="utf-8", errors="replace"))
    files = exact = valid = kw_in = kw_left = letters = in_script = 0
    for f in sorted(Path(corpus).rglob("*")):
        if f.suffix not in (".c", ".h") or not f.is_file():
            continue
        data = f.read_bytes()
        native, back = carry(work, data)
        files += 1
        exact += back == data.replace(b"\r", b"")
        try:
            text = native.decode("utf-8"); valid += 1
            for c in text:
                if ord(c) > 0x7F and c.isalpha():
                    letters += 1
                    in_script += unicodedata.name(c, "?").split(" ")[0] == script
        except UnicodeDecodeError:
            pass
        kw_in += len(C_KEYWORDS.findall(data)); kw_left += len(C_KEYWORDS.findall(native))
    row.update(script=script, files=files, exact=exact, valid_utf8=valid,
               purity=round(100 * in_script / letters, 1) if letters else None,
               keywords_carried=round(100 * (kw_in - kw_left) / kw_in, 1) if kw_in else None)
    return row


def cmd_roundtrip(a):
    cells = sorted(d for d in Path(a.cells).iterdir() if (d / "h2c.uhin").exists() and (d / "c2h.uhin").exists())
    if a.langs:
        want = set(a.langs.split(",")); cells = [d for d in cells if d.name in want]
    work_root = tempfile.mkdtemp(prefix="cells-")
    with Pool(min(8, os.cpu_count() or 2)) as pool:
        rows = pool.map(measure, [(d.name, d, a.corpus, work_root) for d in cells])
    shutil.rmtree(work_root, ignore_errors=True)
    print(f"{'language':20} {'built':6} {'script':12} {'exact':>9} {'utf-8':>7} {'in script':>9} {'keywords':>9}")
    for r in rows:
        if not r["built"]:
            print(f"{r['language']:20} no     {r['note']}"); continue
        print(f"{r['language']:20} yes    {str(r['script']):12} {r['exact']:>4}/{r['files']:<4} {r['valid_utf8']:>7} "
              f"{str(r['purity']) + '%':>9} {str(r['keywords_carried']) + '%':>9}")
    if a.json:
        Path(a.json).write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")


def cmd_tree(a):
    work = Path(tempfile.mkdtemp(prefix="cell-"))
    ok, msg = build_cell(a.cell, work)
    if not ok:
        print(f"tree: {msg}"); return 1
    n = same = 0
    for f in sorted(Path(a.src).rglob("*")):
        if f.suffix in (".c", ".h") and f.is_file():
            data = f.read_bytes(); _, back = carry(work, data)
            n += 1; same += back == data.replace(b"\r", b""); f.write_bytes(back)
    shutil.rmtree(work, ignore_errors=True)
    print(f"tree: {same} of {n} files came back byte for byte"); return 0


if __name__ == "__main__":
    if not RMN or not Path(RMN, "uni2acii").exists():
        print("cells.py: cannot judge: set ROMENAGRI to a built Romenagri folder"); sys.exit(3)
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("roundtrip"); r.add_argument("--cells", required=True); r.add_argument("--corpus", required=True)
    r.add_argument("--langs"); r.add_argument("--json")
    t = sub.add_parser("tree"); t.add_argument("--cell", required=True); t.add_argument("--src", required=True)
    a = ap.parse_args()
    sys.exit(cmd_roundtrip(a) if a.cmd == "roundtrip" else cmd_tree(a))
