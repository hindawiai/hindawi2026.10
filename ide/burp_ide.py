#!/usr/bin/env python3
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""burp_ide.py: one codebase, each person working in their own language, in any editor.

  burp_ide.py view  CANON --lang tamil --out VIEW   make, or refresh, a Tamil view of the canonical tree
  burp_ide.py save  VIEW                            carry the edits made in a view back to the canonical tree,
                                                    then refresh every other view of that tree
  burp_ide.py watch VIEW [--every 2]                save on every change, for as long as it runs
  burp_ide.py geany --lang tamil [--dest DIR]       Geany filetype: the language's keywords highlighted, and
                                                    compile, build and run through hindawicc

The canonical tree is the project as its repository keeps it. A tech lead reading Gujarati C opens a Gujarati view
of the same tree a colleague edits as Tamil C; each save goes through BURP's reverse to the canonical tree, and the
other views are refreshed from it. The views are listed in ~/.config/hindawi/views.json. A name typed in a view that
the dictionary does not know reaches the canonical tree as typed, and every view then shows it as typed.
Debugging: build with -g through hindawicc; in gdb, `source ide/burp_gdb.py` shows native names (see docs).
"""
import argparse, json, os, shutil, subprocess, sys, tempfile, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BURP = ROOT / "lang/hindawi/burp/burp.py"
REG = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config")) / "hindawi/views.json"
sys.path.insert(0, str(BURP.parent))
import burp  # noqa: E402


def registry():
    return json.loads(REG.read_text()) if REG.exists() else {}


def register(view, canon, lang):
    r = registry(); r[str(Path(view).resolve())] = {"canon": str(Path(canon).resolve()), "lang": lang}
    REG.parent.mkdir(parents=True, exist_ok=True); REG.write_text(json.dumps(r, ensure_ascii=False, indent=1))


def snapshot(tree):
    return {str(p.relative_to(tree)): p.stat().st_mtime for p in Path(tree).rglob("*")
            if p.is_file() and ".hindawi" not in p.relative_to(tree).parts}


def make_view(canon, lang, view):
    tmp = Path(tempfile.mkdtemp(prefix="burp-view-"))
    subprocess.run([sys.executable, str(BURP), "ingest", str(canon), "--langs", lang, "--out", str(tmp), "--jobs", "1"],
                   check=True, stdout=subprocess.DEVNULL)
    view = Path(view)
    if view.exists():
        shutil.rmtree(view)
    shutil.move(str(tmp / lang), str(view)); shutil.rmtree(tmp, ignore_errors=True)
    (view / ".hindawi").mkdir(exist_ok=True)
    (view / ".hindawi/sync.json").write_text(json.dumps(snapshot(view)))
    register(view, canon, lang)
    print(f"burp_ide: {view} shows {canon} in {lang}")


def save(view):
    view = Path(view).resolve(); entry = registry().get(str(view))
    if not entry:
        sys.exit(f"burp_ide: {view} is not a registered view; make it with: burp_ide.py view")
    before = json.loads((view / ".hindawi/sync.json").read_text())
    changed = [f for f, t in snapshot(view).items() if before.get(f) != t]
    if not changed:
        return 0
    back = Path(tempfile.mkdtemp(prefix="burp-back-"))
    subprocess.run([sys.executable, str(BURP), "reverse", str(view), "--out", str(back / "t")], check=True, stdout=subprocess.DEVNULL)
    d = json.loads((view / burp.DICT_NAME).read_text(encoding="utf-8"))
    renamed = {v: k for k, v in d.get("files", {}).items()}
    for f in changed:
        orig = renamed.get(f, f); src = back / "t" / orig
        if src.exists():
            dst = Path(entry["canon"]) / orig; dst.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(src, dst)
    shutil.rmtree(back, ignore_errors=True)
    (view / ".hindawi/sync.json").write_text(json.dumps(snapshot(view)))
    print(f"burp_ide: {len(changed)} file(s) saved from {entry['lang']} into {entry['canon']}")
    for other, e in registry().items():
        if other != str(view) and e["canon"] == entry["canon"] and Path(other).exists():
            make_view(e["canon"], e["lang"], other)
    return len(changed)


def geany(lang, dest):
    words = sorted({v for k, v in burp.keyword_table(lang, ["c2h"]).items()})
    name = "Hindawi" + "".join(p.capitalize() for p in lang.split("_"))
    cc = f'ROMENAGRI="{ROOT}/.build/chintamani/Romenagri" HINDAWI_LANG={lang} HINDAWI_NATIVE_SOURCE=1 "{ROOT}/lang/hindawi/hindawicc"'
    conf = (f"[styling=C]\n\n[keywords]\nprimary={' '.join(words)}\n\n[settings]\nlexer_filetype=C\nextension=c\n"
            f"comment_single=//\ncomment_open=/*\ncomment_close=*/\n\n[build-menu]\n"
            f"FT_00_LB=Compile ({lang})\nFT_00_CM={cc} -c -g \"%f\"\nFT_00_WD=%d\n"
            f"FT_01_LB=Build ({lang})\nFT_01_CM={cc} -g -o \"%e\" \"%f\"\nFT_01_WD=%d\n"
            f"EX_00_LB=Run\nEX_00_CM=\"./%e\"\nEX_00_WD=%d\n")
    dest = Path(dest).expanduser(); dest.mkdir(parents=True, exist_ok=True)
    (dest / f"filetypes.{name}.conf").write_text(conf, encoding="utf-8")
    print(f"burp_ide: {dest}/filetypes.{name}.conf ({len(words)} keywords). Add `{name}=*.c;*.h;` under [Extensions]\n"
          f"in ~/.config/geany/filetype_extensions.conf, or choose Document > Set Filetype > {name} per file.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("view"); v.add_argument("canon"); v.add_argument("--lang", required=True); v.add_argument("--out", required=True)
    s = sub.add_parser("save"); s.add_argument("view")
    w = sub.add_parser("watch"); w.add_argument("view"); w.add_argument("--every", type=float, default=2.0)
    g = sub.add_parser("geany"); g.add_argument("--lang", required=True); g.add_argument("--dest", default="~/.config/geany/filedefs")
    a = ap.parse_args()
    if a.cmd == "view":
        make_view(a.canon, a.lang, a.out)
    elif a.cmd == "save":
        save(a.view)
    elif a.cmd == "watch":
        print(f"burp_ide: watching {a.view}; Ctrl-C stops")
        while True:
            save(a.view); time.sleep(a.every)
    else:
        geany(a.lang, a.dest)
