#!/usr/bin/env bash
# parashakti.sh: Parashakti, the sovereign stack through Hindawi, proved on QEMU on this laptop. Parametric: the stack is
# a manifest of projects (built in below; --manifest FILE replaces it), and every project goes through the same steps:
# fetch at a pinned point, configure in host notation, ingest into a language with BURP, lower the whole tree through
# the original Hindawi pipeline (script filter, Romenagri, the language's transducer), build with the project's own
# tools, run on QEMU or its runtime, and check what it prints. Languages come from the foundation's readiness report
# (lang/hindawi/tools/foundation.py): a language whose data is not ready is skipped with the reason, never patched here.
#   bash parashakti.sh --list                                   the projects in the manifest
#   bash parashakti.sh                                          the light projects, every ready default language
#   bash parashakti.sh --stage xv6,minix --langs urdu,tamil     chosen projects and languages
#   bash parashakti.sh --stage linux --langs hindi              a heavy project (Linux, GCC, LLVM, MINIX): hours, disk
#   bash parashakti.sh --repo DIR                               an existing checkout of hindawiai/hindawi2026.10
# One language at a time, everything under ./parashakti, each language's trees deleted as soon as it is done.
# REPORT.md records per project and language: the pinned source, each step's result, and the lines that prove it.
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. Parashakti™, Hindawi™ and BURP™ are his trademarks.
set -uo pipefail
W="$PWD/parashakti"; REPO=""; ARGS=("$@")
for ((k = 0; k < $#; k++)); do [ "${ARGS[$k]}" = "--repo" ] && REPO="${ARGS[$((k + 1))]}"; done
mkdir -p "$W/logs"; export PARASHAKTI_LOG="$W/logs/parashakti.$(date -u +%Y%m%dT%H%M%SZ).log"
need=(git python3 gcc g++ make flex bison gawk iconv qemu-system-riscv64 qemu-system-x86_64 qemu-system-i386 riscv64-linux-gnu-gcc wat2wasm bc)
pkg=(git python3 gcc g++ make flex bison gawk libc-bin qemu-system-misc qemu-system-x86 qemu-system-x86 gcc-riscv64-linux-gnu wabt bc)
miss=(); for k in "${!need[@]}"; do command -v "${need[$k]}" >/dev/null || miss+=("${pkg[$k]}"); done
if [ ${#miss[@]} -gt 0 ]; then
  printf '\n\033[1mINSTALLING %s (sudo asks once)\033[0m\n' "${miss[*]}"
  sudo apt-get update -qq && sudo apt-get install -y -qq "${miss[@]}" libssl-dev libelf-dev cmake ninja-build >>"$PARASHAKTI_LOG" 2>&1 \
    || { echo "apt failed: see $PARASHAKTI_LOG"; exit 1; }
fi
if [ -z "$REPO" ]; then
  REPO="$W/hindawi2026.10"
  [ -d "$REPO/.git" ] || git clone -q --depth 1 https://github.com/hindawiai/hindawi2026.10 "$REPO" >>"$PARASHAKTI_LOG" 2>&1
fi
if [ ! -x "$REPO/.build/chintamani/Romenagri/rmn2acii" ]; then
  printf '\n\033[1mBUILDING the Hindawi toolchain: Romenagri and the original transducers\033[0m\n'
  (cd "$REPO" && bash scripts/build.sh) >>"$PARASHAKTI_LOG" 2>&1 || { echo "toolchain build failed: $PARASHAKTI_LOG"; exit 1; }
fi
export PATH="$REPO/.build/chintamani/Romenagri:$PATH" ROMENAGRI="$REPO/.build/chintamani/Romenagri" PARASHAKTI_REPO="$REPO" PARASHAKTI_W="$W"
exec python3 - "$@" <<'ENGINE'
import argparse, json, os, re, shutil, subprocess, sys, time
from pathlib import Path

REPO, W, LOG = Path(os.environ["PARASHAKTI_REPO"]), Path(os.environ["PARASHAKTI_W"]), Path(os.environ["PARASHAKTI_LOG"])
HIN = REPO / "lang/hindawi"
DEFAULT_LANGS = "hindi,sanskrit,urdu,arabic,persian,tamil,telugu,kannada,kashmiri,punjabi,punjabi_shahmukhi,sindhi,pashto,dari,bengali,marathi,gujarati,odia,malayalam"
SHAKTI_FILES = {
    "main.c": "#define UART_TX ((volatile unsigned int *) 0x11304)\n"
              "void put(const char *text) { while (*text) { *UART_TX = (unsigned char) *text; text++; } }\n"
              "int sum(int count) { int total = 0; for (int index = 1; index <= count; index++) total += index; return total; }\n"
              "int main(void) {\n  int value = sum(10);\n  put(\"Parashakti: Hindawi on SHAKTI, sum 1..10 = \");\n"
              "  *UART_TX = (unsigned char) ('0' + value / 10);\n  *UART_TX = (unsigned char) ('0' + value % 10);\n"
              "  put(\"\\n\");\n  for (;;) { }\n}\n",
    "start.S": "  .section .text.start\n  .global _start\n_start:\n  la sp, stack_top\n  call main\n1: j 1b\n  .bss\n  .space 4096\nstack_top:\n",
    "link.ld": "ENTRY(_start)\nSECTIONS { . = 0x80000000; .text : { *(.text.start) *(.text*) } .rodata : { *(.rodata*) } .data : { *(.data*) } .bss : { *(.bss*) } }\n",
}
# The stack. Each project: where it comes from, how it is configured in host notation, whether names are translated
# (small trees) or kept so the keywords alone are in the language (very large trees, first), how the lowered tree is
# built, how it is run, and what it must print. "heavy" projects run only when named with --stage.
MANIFEST = {
  "shakti": {"title": "bare metal on QEMU's SHAKTI C-class machine", "files": SHAKTI_FILES,
             "build": "riscv64-linux-gnu-gcc -march=rv64imac -mabi=lp64 -mcmodel=medany -nostdlib -ffreestanding -O2 -T link.ld -o prog.elf start.S main.c",
             "run": "timeout 6 qemu-system-riscv64 -M shakti_c -nographic -bios prog.elf", "expect": [r"sum 1\.\.10 = 55"]},
  "xv6": {"title": "the xv6 kernel and shell on QEMU's RISC-V machine", "repo": "https://github.com/mit-pdos/xv6-riscv",
          "build": "make TOOLPREFIX=riscv64-linux-gnu- kernel/kernel fs.img",
          "run": "timeout 18 qemu-system-riscv64 -machine virt -bios none -kernel kernel/kernel -m 128M -smp 1 -nographic "
                 "-global virtio-mmio.force-legacy=false -drive file=fs.img,if=none,format=raw,id=x0 "
                 "-device virtio-blk-device,drive=x0,bus=virtio-mmio-bus.0",
          "input": [6, "echo parashakti-{lang}", 3, "ls", 3], "expect": [r"parashakti-{lang}", r"README"], "never": [r"usertrap|panic"]},
  "wasm3": {"title": "a WebAssembly runtime built from the language, running a WebAssembly module", "repo": "https://github.com/wasm3/wasm3",
            "ref": "v0.5.0", "names": False, "build": "gcc -O2 -Dd_m3HasWASI -Isource source/*.c platforms/app/main.c -o wasm3 -lm",
            "run": "timeout 30 ./wasm3 --func fib test/lang/fib64.wasm 20", "expect": [r"Result: 6765"]},
  "seabios": {"title": "the x86 BIOS on QEMU", "repo": "https://github.com/coreboot/seabios", "ref": "rel-1.16.3",
              "build": "make", "names": False,
              "run": "timeout 8 qemu-system-x86_64 -bios out/bios.bin -display none -chardev stdio,id=s -device isa-debugcon,iobase=0x402,chardev=s",
              "expect": [r"SeaBIOS \(version"]},
  "tinycc": {"title": "a compiler built from the language that compiles and runs a program", "repo": "https://github.com/TinyCC/tinycc",
             "ref": "release_0_9_27", "configure": "./configure", "build": "make tcc", "names": False,
             "run": "printf '#include <stdio.h>\\nint main(void){int t=0;for(int i=1;i<=10;i++)t+=i;printf(\"tcc says %%d\\\\n\",t);return 0;}\\n' > t.c && ./tcc -B. -Iinclude -run t.c",
             "expect": [r"tcc says 55"]},
  "minix": {"title": "MINIX 3 built and booted on QEMU (x86)", "repo": "https://github.com/Stichting-MINIX-Research-Foundation/minix",
            "heavy": True, "names": False, "build": "bash releasetools/x86_hdimage.sh",
            "run": "timeout 900 qemu-system-i386 -m 512 -hda minix_x86.img -nographic -serial mon:stdio", "expect": [r"login:"]},
  "linux": {"title": "the Linux kernel built and booted on QEMU's RISC-V machine", "repo": "https://github.com/torvalds/linux",
            "ref": "v6.6", "heavy": True, "names": False, "keep": [r"^CONFIG_"],
            "build": "make ARCH=riscv CROSS_COMPILE=riscv64-linux-gnu- defconfig && make ARCH=riscv CROSS_COMPILE=riscv64-linux-gnu- -j$(nproc) Image",
            "run": "timeout 90 qemu-system-riscv64 -machine virt -m 512M -nographic -kernel arch/riscv/boot/Image -append 'console=ttyS0 panic=-1'",
            "expect": [r"Linux version 6\.6"]},
  "gcc": {"title": "GCC's C compiler built from the language", "repo": "https://github.com/gcc-mirror/gcc", "ref": "releases/gcc-13",
          "heavy": True, "names": False, "cxx": True,
          "build": "mkdir -p obj && cd obj && ../configure --disable-multilib --enable-languages=c --disable-bootstrap >/dev/null && make -j$(nproc) all-gcc",
          "run": "printf 'int main(void){return 0;}\\n' > t.c && obj/gcc/xgcc -Bobj/gcc/ t.c -o t && ./t && echo gcc-from-language-ok",
          "expect": [r"gcc-from-language-ok"]},
  "llvm": {"title": "LLVM and clang built from the language", "repo": "https://github.com/llvm/llvm-project", "ref": "release/18.x",
           "heavy": True, "names": False, "cxx": True,
           "build": "cmake -S llvm -B obj -G Ninja -DCMAKE_BUILD_TYPE=Release -DLLVM_ENABLE_PROJECTS=clang "
                    "-DLLVM_TARGETS_TO_BUILD='RISCV;WebAssembly;X86' >/dev/null && ninja -C obj clang",
           "run": "obj/bin/clang --version", "expect": [r"clang version 18"]},
}


def log(*a):
    with open(LOG, "a") as f:
        print(*a, file=f)


def sh(cmd, cwd, env=None, inp=None, timeout=None):
    r = subprocess.run(cmd, shell=True, cwd=cwd, env=env, input=inp, capture_output=True, text=True, errors="replace", timeout=timeout)
    log(f"$ ({cwd}) {cmd}\n{r.stdout[-4000:]}{r.stderr[-4000:]}")
    return r


def ready_languages(requested):
    f = HIN / "tools/foundation.py"
    if not f.exists():
        print("   the checkout has no foundation check (an update before 2026.10.7): every requested language is tried")
        return requested, {}
    subprocess.run([sys.executable, str(f)], capture_output=True)
    rd = json.loads((REPO / "docs/hindawi/data/readiness.json").read_text(encoding="utf-8"))["languages"]
    why = {l: ("not in this release" if l not in rd else
               "script has no filter yet" if not rd[l]["script_ready"] else
               "; ".join((rd[l]["errors"] + rd[l]["collisions"] + [f"word outside its script: {w}" for w in rd[l]["words_outside_script"]])[:2]))
           for l in requested if l not in rd or not rd[l]["ready_to_compile"]}
    return [l for l in requested if l not in why], why


NONC = re.compile(r".*\.(S|s|ld|lds|pl|py|mk|sh|cmake|in|txt|json|y|l|def|inc|awk|sed|dts|dtsi|rs|go|asm)$|.*(Makefile|makefile|Kconfig|Kbuild|configure|CMakeLists\.txt)[^/]*$")


def run_project(name, p, langs, rows):
    base = W / name
    shutil.rmtree(base, ignore_errors=True); base.mkdir(parents=True)
    up = base / "up"
    if "files" in p:
        up.mkdir(); [(up / f).write_text(t) for f, t in p["files"].items()]; pin = "inline"
    else:
        ref = ["--branch", p["ref"]] if p.get("ref") else []
        r = sh(" ".join(["git clone -q --depth 1"] + ref + [p["repo"], str(up)]), cwd=base)
        if r.returncode:
            rows.append((name, "-", "fetch failed", "", "", "", "see the log")); return
        pin = (p.get("ref", "") + " " + sh("git rev-parse --short HEAD", cwd=up).stdout.strip()).strip()
    if p.get("configure"):
        sh(p["configure"], cwd=up)
    keep = base / "keep.txt"                 # names the assembly, linker scripts and build files refer to
    names = set()
    for f in up.rglob("*"):
        if f.is_file() and NONC.match(f.name) and f.stat().st_size < 4 << 20:
            names |= set(re.findall(r"[A-Za-z_][A-Za-z0-9_]*", f.read_text(errors="replace")))
    keep.write_text("\n".join(sorted(names)))
    env = dict(os.environ)
    for lang in langs:
        n, work = base / "n", base / "work"
        shutil.rmtree(n, ignore_errors=True); shutil.rmtree(work, ignore_errors=True)
        cmd = [sys.executable, str(HIN / "burp/burp.py"), "ingest", str(up), "--langs", lang, "--out", str(n),
               "--translators", "glossary", "--keep-file", str(keep)]
        for k in p.get("keep", []) + ([] if p.get("names", True) else [".*"]):
            cmd += ["--keep", k]
        r = subprocess.run(cmd, capture_output=True, text=True); log(r.stdout, r.stderr)
        if r.returncode or not (n / lang).exists():
            rows.append((name, lang, pin, "no", "", "", "ingestion failed: see the log")); continue
        for f in up.rglob("*"):                # build files and assembly stay in host notation
            if f.is_file() and NONC.match(f.name):
                dst = n / lang / f.relative_to(up); dst.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(f, dst)
        low = [sys.executable, str(HIN / "tools/build_project.py"), str(n / lang), "--lang", lang, "--work", str(work), "--lower-only"]
        r = subprocess.run(low + (["--cxx"] if p.get("cxx") else []), capture_output=True, text=True); log(r.stdout, r.stderr)
        if r.returncode:
            rows.append((name, lang, pin, "yes", "no", "", (r.stderr.strip().splitlines() or ["lowering failed"])[-1][:120])); continue
        shutil.rmtree(n, ignore_errors=True)
        b = sh(p["build"], cwd=work, env=env)
        if b.returncode:
            err = next((l for l in (b.stderr + b.stdout).splitlines() if "error" in l.lower()), "build failed")
            rows.append((name, lang, pin, "yes", "yes", "no", err[:140])); shutil.rmtree(work, ignore_errors=True); continue
        run = p["run"]
        if p.get("input"):                    # typed into the console, with the pauses a person would leave
            steps = "; ".join(f"sleep {x}" if isinstance(x, int) else f"printf '%s\\n' '{x.format(lang=lang)}'" for x in p["input"])
            run = f"({steps}) | {run}"
        try:
            out = sh(run, cwd=work, env=env, timeout=1200).stdout
        except subprocess.TimeoutExpired as e:
            out = (e.stdout or b"").decode("utf-8", "replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
        ok = all(re.search(e.format(lang=lang), out) for e in p["expect"]) and not any(re.search(e, out) for e in p.get("never", []))
        line = next((l.strip() for l in out.splitlines() if re.search(p["expect"][0].format(lang=lang), l)), out.strip()[-120:])
        rows.append((name, lang, pin, "yes", "yes", "yes" if ok else "NO", f"`{line[:150]}`"))
        print(f"   {name} · {lang}: {'proved' if ok else 'ran, but did not print what it must'}")
        shutil.rmtree(work, ignore_errors=True)
    shutil.rmtree(base, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--langs", default=DEFAULT_LANGS); ap.add_argument("--stage", default="")
    ap.add_argument("--manifest"); ap.add_argument("--list", action="store_true"); ap.add_argument("--repo")
    a = ap.parse_args()
    man = json.loads(Path(a.manifest).read_text()) if a.manifest else MANIFEST
    if a.list:
        for k, v in man.items():
            print(f"{k:8} {'heavy ' if v.get('heavy') else 'light '} {v['title']}")
        return
    stages = [s for s in a.stage.split(",") if s] or [k for k, v in man.items() if not v.get("heavy")]
    langs, why = ready_languages(a.langs.split(","))
    for l, w in why.items():
        print(f"   skipped {l}: {w}")
    rows = []
    for s in stages:
        print(f"\n\033[1mSTAGE {s}: {man[s]['title']}\033[0m", flush=True)
        run_project(s, man[s], langs, rows)
    rep = W / "REPORT.md"
    with open(rep, "w") as f:
        f.write(f"# Parashakti report\n\nRun {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}; Hindawi "
                f"{subprocess.run(['git', '-C', str(REPO), 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()}; "
                f"{subprocess.run(['qemu-system-riscv64', '--version'], capture_output=True, text=True).stdout.splitlines()[0]}.\n\n"
                "| Project | Language | Source | Ingested | Lowered | Built, ran and printed | Evidence | AyeKnow state |\n|---|---|---|---|---|---|---|---|\n")
        for r in rows:   # AyeKnow: verified (ran and printed what it must), executed, implemented, defined
            state = {"yes": "verified", "NO": "executed"}.get(r[5], "implemented" if r[4] == "yes" else "defined")
            f.write("| " + " | ".join(r) + f" | {state} |\n")
        for l, w in why.items():
            f.write(f"\nSkipped {l}: {w}.")
    proved = sum(1 for r in rows if r[5] == "yes")
    print(f"\n\033[1mDONE: {proved} of {len(rows)} project-language runs proved; report {rep}\033[0m")


main()
ENGINE
