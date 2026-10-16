#!/usr/bin/env python3
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""ingest_project.py: carry a whole upstream project into one or many languages in one run.

The tree is copied whole for each language; every C and C++ source and header is ingested through ingest.py with
one dictionary per language for the whole project, so names crossing files keep one native name. Build files and
data are copied unchanged. With --localize-files, source and header files are renamed to their translated names
and every quoted #include follows; the renames go into the dictionary, so the build restores them.
(The design of ingest_project and build_project follows the HINDAWI2026_10-regression-fixed drop.)

  python3 ingest_project.py ROOT --lang hindi,urdu,bengali --out OUT [--localize-files]
  OUT/<lang>/ is the native tree; OUT/<lang>/.hindawi/dictionary.json its dictionary.
"""
import argparse, json, shutil, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import ingest as ing

EXTS = {".c", ".h", ".cc", ".cpp", ".cxx", ".hpp"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root"); ap.add_argument("--lang", default="hindi"); ap.add_argument("--out", required=True)
    ap.add_argument("--localize-files", action="store_true")
    ap.add_argument("--exclude", action="append", default=[], help="a path prefix copied as it is (host build tools)")
    ap.add_argument("--keep-macros", action="store_true", help="leave ALL-CAPS names as they are")
    a = ap.parse_args()
    if a.keep_macros:
        ing.KEEP_MACROS = True
    root, out = Path(a.root).resolve(), Path(a.out).resolve()
    for lang in [l.strip() for l in a.lang.split(",") if l.strip()]:
        dst_root = out / lang; dpath = dst_root / ".hindawi" / "dictionary.json"
        d = ing.load(dpath, lang)
        files = [p for p in sorted(root.rglob("*")) if p.is_file() and ".hindawi" not in p.parts]
        if a.localize_files:   # names first, so every #include can follow them
            for p in files:
                if p.suffix.lower() in EXTS and not any(str(p.relative_to(root)).startswith(x) for x in a.exclude):
                    stem = ing.native_name(p.stem, d, lang)
                    d["files"][str(p.relative_to(root))] = str(p.relative_to(root).with_name(stem + p.suffix))
                    d["files"].setdefault(p.name, stem + p.suffix)
        n = 0
        for p in files:
            rel = str(p.relative_to(root)); target = dst_root / d["files"].get(rel, rel)
            target.parent.mkdir(parents=True, exist_ok=True)
            if p.suffix.lower() in EXTS and not any(rel.startswith(x) for x in a.exclude):
                target.write_text(ing.ingest(p.read_text(encoding="utf-8", errors="replace"), lang, d, a.localize_files),
                                  encoding="utf-8"); n += 1
            else:
                shutil.copy2(p, target)
        d["excluded"] = a.exclude
        ing.save(d, dpath)
        print(json.dumps({"language": lang, "sources": n, "names": len(d["forward"]), "files_renamed": len(d["files"]),
                          "tree": str(dst_root)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
