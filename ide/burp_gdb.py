# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""burp_gdb.py: debug native programs with native names. In gdb:  source ide/burp_gdb.py

  burp-bt        the backtrace, each function by its native name
  burp-locals    the current frame's arguments and locals, by their native names

Needs ROMENAGRI (a built Romenagri folder) and BURP_DICT (the view's .hindawi/dictionary.json). A C-level name is
mapped back only when the dictionary holds the native name it came from: each native name is carried through the
compilation path's own Romenagri chain once, so the map is exact and an English name is never mistaken for one.
"""
import json, os, subprocess
import gdb

CHAIN = "fixuninum | iconv -f utf-8 -t utf-16 | uni2acii | acii2cf | acii2uni | iconv -f UTF-16 -t UTF-8"


def _load():
    rmn, path = os.environ.get("ROMENAGRI"), os.environ.get("BURP_DICT")
    if not rmn or not path or not os.path.exists(path):
        print("burp_gdb: set ROMENAGRI and BURP_DICT to show native names"); return {}
    natives = sorted({v for v in json.load(open(path, encoding="utf-8")).get("identifiers", {}).values()})
    env = dict(os.environ, PATH=f"{rmn}:" + os.environ.get("PATH", ""))
    out = subprocess.run(CHAIN, shell=True, input="\n".join(natives).encode(), capture_output=True, env=env)
    return dict(zip(out.stdout.decode("utf-8").replace("\r", "").split("\n"), natives))


NAMES = _load()


def native(name):
    return NAMES.get(name, name)


class BurpBt(gdb.Command):
    def __init__(self):
        super().__init__("burp-bt", gdb.COMMAND_STACK)

    def invoke(self, arg, from_tty):
        f, i = gdb.newest_frame(), 0
        while f:
            sal = f.find_sal()
            where = f"{sal.symtab.filename}:{sal.line}" if sal and sal.symtab else "?"
            print(f"#{i}  {native(f.name() or '??')}  at {where}")
            f, i = f.older(), i + 1


class BurpLocals(gdb.Command):
    def __init__(self):
        super().__init__("burp-locals", gdb.COMMAND_DATA)

    def invoke(self, arg, from_tty):
        frame = gdb.selected_frame(); block = frame.block()
        while block and not block.is_global:
            for sym in block:
                if sym.is_variable or sym.is_argument:
                    print(f"{native(sym.name)} = {sym.value(frame)}")
            block = block.superblock


BurpBt(); BurpLocals()
print(f"burp_gdb: {len(NAMES)} native names loaded; commands burp-bt and burp-locals")
