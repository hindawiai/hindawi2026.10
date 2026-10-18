#!/usr/bin/env python3
"""Ingest a directory of C files through c2h toolchain and compile."""
import argparse, subprocess, sys
from pathlib import Path

C2H = Path(__file__).resolve().parents[1] / "upstream/chintamani/guru/c2h"
H2C = Path(__file__).resolve().parents[1] / "upstream/chintamani/guru/h2c"

def run_c2h(src):
    r = subprocess.run([str(C2H)], input=src.encode(), capture_output=True)
    return r.stdout.decode() if r.returncode == 0 else src

def run_h2c(src):
    r = subprocess.run([str(H2C)], input=src.encode(), capture_output=True)
    return r.stdout.decode() if r.returncode == 0 else src

def ingest_file(path, out_dir):
    src = path.read_text(errors="ignore")
    converted = run_c2h(src)
    out_path = out_dir / (path.stem + ".uhin")
    out_path.write_text(converted)
    return out_path

def compile_uhin(uhin_path, out_dir, include_dirs):
    src = uhin_path.read_text()
    c_src = run_h2c(src)
    c_path = out_dir / (uhin_path.stem + ".c")
    c_path.write_text(c_src)
    cmd = ["gcc", "-c", "-o", str(out_dir / (uhin_path.stem + ".o")), str(c_path)]
    for d in include_dirs:
        cmd.extend(["-I", str(d)])
    r = subprocess.run(cmd, capture_output=True)
    return r.returncode, r.stderr.decode()[:200]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src_dir", type=Path)
    ap.add_argument("--out", type=Path, default=Path("/tmp/ingested"))
    ap.add_argument("-I", action="append", default=[], dest="includes")
    args = ap.parse_args()
    
    args.out.mkdir(parents=True, exist_ok=True)
    c_files = list(args.src_dir.glob("*.c"))
    print(f"found {len(c_files)} .c files")
    
    for c_file in c_files[:5]:  # limit for test
        uhin = ingest_file(c_file, args.out)
        rc, err = compile_uhin(uhin, args.out, args.includes)
        status = "OK" if rc == 0 else f"FAIL: {err[:50]}"
        print(f"  {c_file.name}: {status}")

if __name__ == "__main__":
    main()
