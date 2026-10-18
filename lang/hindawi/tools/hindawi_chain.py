#!/usr/bin/env python3
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""hindawi_chain.py: the two Hindawi paths, shared by ingest.py, hindawicc and the project tools.

Ingestion path (for people): C to the language. Keywords become the language's own keywords, in its own script.
  Hindi runs Chintamani's own c2h through Romenagri, as C11 established; every other language runs its cell's
  c2h directly on Unicode text. No transliteration is needed here.
Compilation path (for the machine): the language to C. Transliteration is essential here, so names survive to
  the lowest layer. A non-Devanagari source first goes through its script filter, as in the original pipeline
  (Chintamani's fltr_te_hi and fltr_ur_hi; generated filters of the same kind for the other Brahmi scripts), then: fixuninum | iconv | uni2acii | acii2cf | acii2uni | iconv | the language's h2c,
  built from its h2c.uhin through the same filter. Then the original driver's escape repairs. Names already
  in ASCII are held aside and put back unchanged (CONFIG_X, memcpy, __malloc keep their identity); native names
  take their Romenagri form, which is the name ABI.

  python3 hindawi_chain.py to-native --lang L  < file.c    > file.native
  python3 hindawi_chain.py to-c      --lang L  < file.uhin > file.c
  python3 hindawi_chain.py c-name    --lang L  NAME...      the C-level form of each name
Needs ROMENAGRI (a built Romenagri folder), flex, gcc, iconv.
"""
import os, re, shutil, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
HINDAWI = HERE.parent
REPO = HINDAWI.parents[1]
CACHE = Path(os.environ.get("HINDAWI_CACHE", REPO / ".build/cells"))
sys.path.insert(0, str(HERE))
import script_filters  # noqa: E402  the original pipeline's script filter, in front of Romenagri
DEVANAGARI_LANGS = {"hindi", "sanskrit", "marathi", "nepali", "awadhi", "bhojpuri", "maithili", "bodo", "dogri",
                    "konkani", "chhattisgarhi", "magahi", "rajasthani", "braj", "haryanvi"}
ROMENAGRI_CHAIN = "fixuninum | iconv -f utf-8 -t utf-16 | uni2acii | acii2cf | acii2uni | iconv -f UTF-16 -t UTF-8"
REPAIRS = [("\\न", "\\n"), ("%भ", "%f"), ("%प", "%d"), ("%द", "%d")]   # the original gurucc's, and c2h's %d
ASCII_ID = re.compile(r"\b[A-Za-z_][A-Za-z0-9_]*\b")
NAME_RUN = re.compile(r"[\w\u0300-\u036f\u0900-\u0dff\u0e00-\u0fff\u1000-\u109f]+")   # a name, marks included
ASCII_WHOLE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
# a word in a native script, marks and joining underscores included
_NW = r"(?:(?![\x00-\x7f])[\w\u0300-\u036f\u0610-\u061a\u064b-\u065f\u0670\u06d6-\u06ed\u0900-\u0dff\u0e00-\u0fff\u1000-\u109f\u200c\u200d])"
NATIVE_WORD = re.compile(_NW + r"(?:" + _NW + r"|_)*")
ASCII_RUN = re.compile(r"(?<![A-Za-z0-9_])[A-Za-z_][A-Za-z0-9_]*(?![A-Za-z0-9_])")   # ASCII boundaries only


def env():
    rmn = os.environ.get("ROMENAGRI", "") or str(REPO / ".build/chintamani/Romenagri")   # where scripts/build.sh puts it
    if not rmn or not Path(rmn, "uni2acii").exists():
        sys.exit("hindawi_chain: set ROMENAGRI to a built Romenagri folder")
    return dict(os.environ, PATH=f"{rmn}:" + os.environ.get("PATH", ""))


def sh(cmd, data=b"", cwd=None):
    p = subprocess.run(cmd, shell=True, input=data, capture_output=True, cwd=cwd, env=env())
    if p.returncode != 0:
        sys.exit(f"hindawi_chain: failed: {cmd[:90]}: {p.stderr.decode('utf-8', 'replace').strip()[:200]}")
    return p.stdout


def cell_dir(lang):
    if lang == "hindi":
        return HINDAWI / "upstream/chintamani/guru"
    d = HINDAWI / "languages" / lang
    if not (d / "h2c.uhin").exists():
        sys.exit(f"hindawi_chain: no cell for {lang} in {d}")
    return d


def script_filter(lang):
    """The shell fragment for the language's script filter: Chintamani's own (Telugu, Perso-Arabic), a generated one of
    the same kind (other Brahmi scripts), nothing for Devanagari. A script with no filter has no compilation path yet."""
    if lang in DEVANAGARI_LANGS:
        return ""
    f = script_filters.which(lang)
    if f is None:
        sys.exit(f"hindawi_chain: {lang} ({script_filters.script_of_language(lang)}) has no script filter yet, so no "
                 "compilation path; it ingests and reads in full")
    return f"'{f}' | " if f else ""


def lexers(lang):
    """Build (once) the language's ingestion c2h and compilation h2c; return their paths."""
    out = CACHE / lang
    c2h, h2c = out / "c2h", out / "h2c"
    src = cell_dir(lang)
    sources = [src / "h2c.uhin", src / "c2h.uhin", HERE / "script_filters.py"]
    if c2h.exists() and h2c.exists() and all(p.stat().st_mtime <= h2c.stat().st_mtime for p in sources if p.exists()):
        return c2h, h2c                    # built, and no newer than the cell it was built from
    out.mkdir(parents=True, exist_ok=True)
    src = cell_dir(lang)
    if lang == "hindi":   # Chintamani's own pair, built with its own Makefile through Romenagri
        if not (src / "h2c").exists() or not (src / "c2h").exists():
            sh(f"make -s -C '{src}'")
        shutil.copy(src / "c2h", c2h); shutil.copy(src / "h2c", h2c)
        return c2h, h2c
    # ingestion: the cell's c2h straight on Unicode, so keywords come out in the language's own script
    sh(f"flex -8 -o '{out}/c2h_lex.c' '{src}/c2h.uhin' && {{ gcc -O1 -o '{c2h}' '{out}/c2h_lex.c' -lfl 2>/dev/null || "
       f"gcc -O1 -o '{c2h}' '{out}/c2h_lex.c' -ll 2>/dev/null || gcc -O1 -o '{c2h}' '{out}/c2h_lex.c'; }}")
    # compilation: the cell's h2c through the script filter and Romenagri, as the original Makefiles build h2c
    filt = script_filter(lang) and f"python3 '{HERE / 'script_filters.py'}' prepare {lang} | "
    sh(f"cat '{src}/h2c.uhin' | {filt}iconv -f utf-8 -t utf-16 | uni2acii | acii2cf > '{out}/h2c.lex'")
    lex = (out / "h2c.lex").read_bytes().split(b"\n")      # a word's C-level form, as to_c gives it (cform)
    lex = [re.sub(rb"^(\\#)?[A-Za-z0-9_^]+(?=\s+\{)", lambda m: cform(m.group(0).decode()).encode(), l) for l in lex]
    (out / "h2c.lex").write_bytes(b"\n".join(lex))
    sh(f"flex -8 -o '{out}/h2c_lex.c' '{out}/h2c.lex' && {{ gcc -O1 -o '{h2c}' '{out}/h2c_lex.c' -lfl 2>/dev/null || "
       f"gcc -O1 -o '{h2c}' '{out}/h2c_lex.c' -ll 2>/dev/null || gcc -O1 -o '{h2c}' '{out}/h2c_lex.c'; }}")   # libfl, BSD libl, or none
    return c2h, h2c


def to_native(text, lang):
    c2h, _ = lexers(lang)
    if lang == "hindi":
        cmd = f"fixuninum | iconv -f utf-8 -t utf-16 | uni2acii | '{c2h}' | acii2uni | iconv -f UTF-16 -t UTF-8"
    else:
        cmd = f"'{c2h}'"
    return sh(cmd, text.encode("utf-8")).decode("utf-8", "replace").replace("\r", "")


def cform(form):
    """Romenagri marks a vowel-initial syllable inside a word with ^, which no C identifier may contain; it is written _
    instead, as Romenagri itself writes a vowel at the start of a word (DEVIATIONS.md)."""
    return form[:2] + form[2:].replace("^", "_") if form.startswith("\\#") else form.replace("^", "_")


def to_c(text, lang):
    """Native names go through Romenagri (their C-level form is the name ABI). Names already written in ASCII
    need no transliteration, and Romenagri's acii2cf would rewrite their underscores (both _malloc and __malloc
    come out alike), so they are held aside as plain tokens and put back unchanged."""
    _, h2c = lexers(lang)
    held = []
    def hold(m):
        t = m.group(0)
        if not ASCII_WHOLE.fullmatch(t) or not re.search(r"[A-Za-z0-9]", t):
            return t   # underscores alone belong to native words (अगर_घोषित, म_लिखो)
        held.append(t); return f"QZXQ{len(held) - 1:07d}QXZQ"
    guarded = ASCII_RUN.sub(hold, text)
    filt = script_filter(lang)
    # Each native word goes through the script filter and Romenagri on its own, the way the cell's rules were, so a
    # word has one C-level form wherever it stands: Chintamani's Perso-Arabic filter reads a word-initial letter one
    # way after a space and another way after a bracket, which would give one name two forms (DEVIATIONS.md).
    words = sorted({m.group(0) for m in NATIVE_WORD.finditer(guarded)})
    if words:
        forms = sh(f"{filt}{ROMENAGRI_CHAIN}", script_filters.fold(lang, "\n".join(words)).encode("utf-8")).decode("utf-8", "replace").replace("\r", "").split("\n")
        table = {w: cform(f.strip() or w) for w, f in zip(words, forms)}
        guarded = NATIVE_WORD.sub(lambda m: table[m.group(0)], guarded)
    c = sh(f"'{h2c}'", guarded.encode("utf-8")).decode("utf-8", "replace").replace("\r", "")
    for a, b in REPAIRS:
        c = c.replace(a, b)
    return re.sub(r"QZXQ(\d{7})QXZQ", lambda m: held[int(m.group(1))], c)


def c_names(names, lang):
    """The C-level name of each name on the compilation path: the name ABI. Computed by to_c itself, so a
    name gets exactly the form the compiler sees wherever it appears."""
    if not names:
        return {}
    forms = to_c("\n".join(names), lang).split("\n")
    return {n: (f.strip() or n) for n, f in zip(names, forms)}


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["to-native", "to-c", "c-name"]); ap.add_argument("--lang", default="hindi")
    ap.add_argument("names", nargs="*")
    a = ap.parse_intermixed_args()
    if a.cmd == "c-name":
        for n, f in c_names(a.names, a.lang).items():
            print(f)
    else:
        data = sys.stdin.buffer.read().decode("utf-8", "replace")
        sys.stdout.write(to_native(data, a.lang) if a.cmd == "to-native" else to_c(data, a.lang))
