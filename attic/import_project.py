#!/usr/bin/env python3
"""Walk a source tree and emit a Hindawi build description.
Does not concatenate sources. Preserves paths.
"""
import argparse, json, os
from pathlib import Path

EXT_SHAILI = {
    ".c": "guru", ".h": "guru",
    ".cpp": "shraeni", ".cc": "shraeni", ".hpp": "shraeni",
    ".s": "yantra", ".S": "yantra", ".asm": "yantra",
    ".java": "kritrima",
    ".py": "soochee",
    ".bas": "praatha",
    ".y": "wyaaka", ".yacc": "wyaaka",
    ".l": "shabda", ".lex": "shabda",
    ".logo": "robot",
    ".vhd": "vhdl", ".vhdl": "vhdl",
    ".v": "verilog", ".sv": "systemverilog",
}

def walk(root):
    root = Path(root)
    files = []
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            p = Path(dirpath) / name
            ext = p.suffix.lower() if p.suffix.lower() in EXT_SHAILI else p.suffix
            shaili = EXT_SHAILI.get(ext) or EXT_SHAILI.get(p.suffix)
            if not shaili:
                continue
            rel = p.relative_to(root)
            files.append({
                "path": str(rel),
                "ext": p.suffix,
                "shaili": shaili,
                "size": p.stat().st_size,
            })
    return files

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--lang", default="hindi")
    ap.add_argument("-o", "--output")
    args = ap.parse_args()
    files = walk(args.root)
    desc = {
        "project": str(Path(args.root).name),
        "target_lang": args.lang,
        "file_count": len(files),
        "by_shaili": {},
        "files": files,
    }
    for f in files:
        desc["by_shaili"].setdefault(f["shaili"], 0)
        desc["by_shaili"][f["shaili"]] += 1
    text = json.dumps(desc, indent=2)
    if args.output:
        Path(args.output).write_text(text)
        print(f"wrote {args.output} ({len(files)} files)")
    else:
        print(text)

if __name__ == "__main__":
    main()
