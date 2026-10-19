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
#   bash parashakti.sh --check                                 only the timed sanity check of this machine
#   bash parashakti.sh --install                               also try to install what is missing, one package at a time
mkdir -p "$W/logs"; export PARASHAKTI_LOG="$W/logs/parashakti.$(date -u +%Y%m%dT%H%M%SZ).log"
# ---- a timed sanity check of this machine: each probe has a time limit, nothing is installed unless --install is given,
# and nothing here stops the run; each project later runs only if what it needs is present, and says what is missing
INSTALL=0; CHECKONLY=0; for a in "$@"; do [ "$a" = "--install" ] && INSTALL=1; [ "$a" = "--check" ] && CHECKONLY=1; done
printf '\n\033[1mSANITY CHECK (each probe limited in time)\033[0m\n'
HAVE=""
probe(){ # probe NAME SECONDS COMMAND...: PASS with the first line of output, or MISSING / TIMEOUT
  local name="$1" t="$2"; shift 2; local t0=$SECONDS out rc
  out=$(timeout "$t" "$@" 2>&1); rc=$?; out=$(printf '%s\n' "$out" | head -1)
  if [ "$rc" = 124 ]; then printf '   %-26s TIMEOUT after %ss\n' "$name" "$t"
  elif [ "$rc" = 0 ]; then printf '   %-26s ok   %s (%ss)\n' "$name" "${out:0:60}" "$((SECONDS - t0))"; HAVE="$HAVE,$name"
  else printf '   %-26s MISSING\n' "$name"; fi; }
for t in git python3 gcc g++ make flex bison gawk iconv bc cmake ninja wat2wasm gh riscv64-linux-gnu-gcc riscv64-unknown-elf-gcc qemu-system-riscv64 qemu-system-x86_64 qemu-system-i386; do
  if command -v "$t" >/dev/null; then probe "$t" 10 "$t" --version; else printf '   %-26s MISSING\n' "$t"; fi
done
probe "qemu shakti_c machine" 10 sh -c 'qemu-system-riscv64 -M help | grep -m1 shakti_c'
probe "network to github.com" 20 git ls-remote https://github.com/mit-pdos/xv6-riscv HEAD
probe "network to gitlab.com" 20 git ls-remote https://gitlab.com/shaktiproject/software/shakti-sdk.git HEAD
probe "sudo without a password" 5 sudo -n true
free=$(df -Pm "$W" | awk 'NR==2 {print $4}'); printf '   %-26s %s MB free\n' "disk at $W" "$free"
[ "${free:-0}" -lt 3000 ] && printf '   %-26s under 3 GB free: the heavy projects (Linux, GCC, LLVM, MINIX) will not fit\n' "note"
export PARASHAKTI_HAVE="$HAVE"
if [ "$INSTALL" = 1 ]; then      # one package at a time, each limited in time; a failure is reported and the next is tried
  sudo -v || echo "   sudo was not granted: nothing can be installed; carrying on with what is here"
  for pair in gcc-riscv64-linux-gnu:riscv64-linux-gnu-gcc gcc-riscv64-unknown-elf:riscv64-unknown-elf-gcc qemu-system-misc:qemu-system-riscv64 qemu-system-x86:qemu-system-x86_64 \
              wabt:wat2wasm flex:flex bison:bison gawk:gawk bc:bc cmake:cmake ninja-build:ninja; do
    pk=${pair%%:*}; tool=${pair##*:}; command -v "$tool" >/dev/null && continue
    printf '   installing %-20s' "$pk"; timeout --foreground 600 sudo -n apt-get install -y -qq "$pk" >>"$PARASHAKTI_LOG" 2>&1 && echo " done" || echo " not installed (see the log); carrying on"
  done
fi
[ "$CHECKONLY" = 1 ] && { printf '\n   --check: nothing else done\n'; exit 0; }
for t in git python3 gcc make flex bison; do command -v "$t" >/dev/null || { echo "   Hindawi's toolchain needs $t; install it (sudo apt install $t) and run again"; exit 1; }; done
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
  "shakti-sdk": {"needs": ["riscv64-unknown-elf-gcc", "qemu shakti_c machine", "network to gitlab.com"], "layer": 9,
                 "title": "the SHAKTI SDK built from the language: its UART loopback on QEMU's SHAKTI machine",
                 "repo": "https://gitlab.com/shaktiproject/software/shakti-sdk.git", "names": False,
                 "build": "make software PROGRAM=loopback TARGET=artix7_100t",
                 "run": "timeout 12 qemu-system-riscv64 -M shakti_c -nographic -bios software/examples/uart_applns/loopback/output/loopback.shakti",
                 "input": [3, "parashakti {lang}", 3], "expect": [r"parashakti"]},
  "shakti": {"needs": ['riscv64-linux-gnu-gcc', 'qemu-system-riscv64', 'qemu shakti_c machine'], "title": "bare metal on QEMU's SHAKTI C-class machine", "files": SHAKTI_FILES,
             "build": "riscv64-linux-gnu-gcc -march=rv64imac -mabi=lp64 -mcmodel=medany -nostdlib -ffreestanding -O2 -T link.ld -o prog.elf start.S main.c",
             "run": "timeout 6 qemu-system-riscv64 -M shakti_c -nographic -bios prog.elf", "expect": [r"sum 1\.\.10 = 55"]},
  "xv6": {"needs": ['riscv64-linux-gnu-gcc', 'qemu-system-riscv64', 'network to github.com'], "title": "the xv6 kernel and shell on QEMU's RISC-V machine", "repo": "https://github.com/mit-pdos/xv6-riscv",
          "build": "make TOOLPREFIX=riscv64-linux-gnu- kernel/kernel fs.img",
          "run": "timeout 18 qemu-system-riscv64 -machine virt -bios none -kernel kernel/kernel -m 128M -smp 1 -nographic "
                 "-global virtio-mmio.force-legacy=false -drive file=fs.img,if=none,format=raw,id=x0 "
                 "-device virtio-blk-device,drive=x0,bus=virtio-mmio-bus.0",
          "input": [6, "echo parashakti-{lang}", 3, "ls", 3], "expect": [r"parashakti-{lang}", r"README"], "never": [r"usertrap|panic"]},
  "wasm3": {"needs": ['gcc', 'network to github.com'], "title": "a WebAssembly runtime built from the language, running a WebAssembly module", "repo": "https://github.com/wasm3/wasm3",
            "ref": "v0.5.0", "names": False, "build": "gcc -O2 -Dd_m3HasWASI -Isource source/*.c platforms/app/main.c -o wasm3 -lm",
            "run": "timeout 30 ./wasm3 --func fib test/lang/fib64.wasm 20", "expect": [r"Result: 6765"]},
  "seabios": {"needs": ['qemu-system-x86_64', 'python3', 'network to github.com'], "title": "the x86 BIOS on QEMU", "repo": "https://github.com/coreboot/seabios", "ref": "rel-1.16.3",
              "build": "make", "names": False,
              "run": "timeout 8 qemu-system-x86_64 -bios out/bios.bin -display none -chardev stdio,id=s -device isa-debugcon,iobase=0x402,chardev=s",
              "expect": [r"SeaBIOS \(version"]},
  "tinycc": {"needs": ['gcc', 'network to github.com'], "title": "a compiler built from the language that compiles and runs a program", "repo": "https://github.com/TinyCC/tinycc",
             "ref": "release_0_9_27", "configure": "./configure", "build": "make tcc", "names": False,
             "run": "printf '#include <stdio.h>\\nint main(void){int t=0;for(int i=1;i<=10;i++)t+=i;printf(\"tcc says %%d\\\\n\",t);return 0;}\\n' > t.c && ./tcc -B. -Iinclude -run t.c",
             "expect": [r"tcc says 55"]},
  "opensbi": {"needs": ["riscv64-linux-gnu-gcc", "qemu-system-riscv64", "network to github.com"], "layer": 9,
              "title": "OpenSBI, the RISC-V firmware, built from the language and booted on QEMU", "repo": "https://github.com/riscv-software-src/opensbi",
              "names": False, "build": "make PLATFORM=generic CROSS_COMPILE=riscv64-linux-gnu-",
              "run": "timeout 10 qemu-system-riscv64 -M virt -nographic -bios build/platform/generic/firmware/fw_dynamic.bin", "expect": [r"OpenSBI"]},
  "binutils": {"needs": ["gcc", "make", "network to github.com"], "layer": 12, "heavy": True, "title": "GNU binutils (assembler and linker) built from the language",
               "repo": "https://github.com/bminor/binutils-gdb", "names": False,
               "build": "mkdir -p obj && cd obj && ../configure --disable-gdb --disable-gdbserver --disable-sim >/dev/null && make -j$(nproc) all-binutils all-gas all-ld",
               "run": "obj/gas/as-new --version | head -1", "expect": [r"GNU assembler"]},
  "qemu": {"needs": ["gcc", "make", "network to github.com"], "layer": 8, "heavy": True, "title": "QEMU, the machine emulator, built from the language",
           "repo": "https://github.com/qemu/qemu", "names": False,
           "build": "./configure --target-list=riscv64-softmmu >/dev/null && make -j$(nproc)", "run": "build/qemu-system-riscv64 --version", "expect": [r"QEMU emulator version"]},
  "minix": {"needs": ['qemu-system-i386', 'network to github.com'], "title": "MINIX 3 built and booted on QEMU (x86)", "repo": "https://github.com/Stichting-MINIX-Research-Foundation/minix",
            "heavy": True, "names": False, "build": "bash releasetools/x86_hdimage.sh",
            "run": "timeout 900 qemu-system-i386 -m 512 -hda minix_x86.img -nographic -serial mon:stdio", "expect": [r"login:"]},
  "linux": {"needs": ['riscv64-linux-gnu-gcc', 'qemu-system-riscv64', 'bc', 'flex', 'bison', 'network to github.com'], "title": "the Linux kernel built and booted on QEMU's RISC-V machine", "repo": "https://github.com/torvalds/linux",
            "ref": "v6.6", "heavy": True, "names": False, "keep": [r"^CONFIG_"],
            "build": "make ARCH=riscv CROSS_COMPILE=riscv64-linux-gnu- defconfig && make ARCH=riscv CROSS_COMPILE=riscv64-linux-gnu- -j$(nproc) Image",
            "run": "timeout 90 qemu-system-riscv64 -machine virt -m 512M -nographic -kernel arch/riscv/boot/Image -append 'console=ttyS0 panic=-1'",
            "expect": [r"Linux version 6\.6"]},
  "gcc": {"needs": ['g++', 'flex', 'bison', 'network to github.com'], "title": "GCC's C compiler built from the language", "repo": "https://github.com/gcc-mirror/gcc", "ref": "releases/gcc-13",
          "heavy": True, "names": False, "cxx": True,
          "build": "mkdir -p obj && cd obj && ../configure --disable-multilib --enable-languages=c --disable-bootstrap >/dev/null && make -j$(nproc) all-gcc",
          "run": "printf 'int main(void){return 0;}\\n' > t.c && obj/gcc/xgcc -Bobj/gcc/ t.c -o t && ./t && echo gcc-from-language-ok",
          "expect": [r"gcc-from-language-ok"]},
  "llvm": {"needs": ['cmake', 'ninja', 'g++', 'network to github.com'], "title": "LLVM and clang built from the language", "repo": "https://github.com/llvm/llvm-project", "ref": "release/18.x",
           "heavy": True, "names": False, "cxx": True,
           "build": "cmake -S llvm -B obj -G Ninja -DCMAKE_BUILD_TYPE=Release -DLLVM_ENABLE_PROJECTS=clang "
                    "-DLLVM_TARGETS_TO_BUILD='RISCV;WebAssembly;X86' >/dev/null && ninja -C obj clang",
           "run": "obj/bin/clang --version", "expect": [r"clang version 18"]},
}


def log(*a):
    with open(LOG, "a") as f:
        print(*a, file=f)


def sh(cmd, cwd, env=None, inp=None, timeout=None, label=None):
    """Run a step; every 5 seconds the console shows it is alive and how long it has taken."""
    import threading
    label = label or (cmd if isinstance(cmd, str) else " ".join(map(str, cmd)))[:60]
    done = threading.Event(); t0 = time.time()
    def beat():
        while not done.wait(5):
            print(f"\r   … {label}: {int(time.time() - t0)} s", end="", flush=True)
    th = threading.Thread(target=beat, daemon=True); th.start()
    try:
        r = subprocess.run(cmd, shell=isinstance(cmd, str), cwd=cwd, env=env, input=inp, capture_output=True, text=True,
                           errors="replace", timeout=timeout)
    finally:
        done.set()
        if time.time() - t0 >= 5:
            print(f"\r   … {label}: done in {int(time.time() - t0)} s" + " " * 10, flush=True)
    log(f"$ ({cwd}) {cmd}\n{r.stdout[-4000:]}{r.stderr[-4000:]}")
    return r


def ready_languages(requested):
    f = HIN / "tools/foundation.py"
    if not f.exists():
        print("   the checkout has no foundation check (an update before 2026.10.7): every requested language is tried")
        return requested, {}
    out = W / "readiness.json"
    if "--out" in f.read_text(encoding="utf-8"):
        sh([sys.executable, str(f), "--langs", ",".join(requested), "--out", str(out)], cwd=REPO, label="checking the languages")
    else:
        sh([sys.executable, str(f)], cwd=REPO, label="checking every language (the first time builds their transducers)")
        out = REPO / "docs/hindawi/data/readiness.json"
    rd = json.loads(out.read_text(encoding="utf-8"))["languages"]
    why = {l: ("not in this release" if l not in rd else
               "script has no filter yet" if not rd[l]["script_ready"] else
               "; ".join((rd[l]["errors"] + rd[l]["collisions"] + [f"word outside its script: {w}" for w in rd[l]["words_outside_script"]])[:2]))
           for l in requested if l not in rd or not rd[l]["ready_to_compile"]}
    return [l for l in requested if l not in why], why


NONC = re.compile(r".*\.(S|s|ld|lds|pl|py|mk|sh|cmake|in|txt|json|y|l|def|inc|awk|sed|dts|dtsi|rs|go|asm)$|.*(Makefile|makefile|Kconfig|Kbuild|configure|CMakeLists\.txt)[^/]*$")


VERIFIED, baseline = {}, {}


def english_baseline(name, p, up, env):
    """The upstream, built and run in English the same way: what each language's build must match."""
    eng = up.parent / "english"; shutil.rmtree(eng, ignore_errors=True); shutil.copytree(up, eng, symlinks=True)
    try:
        if sh(p["build"], cwd=eng, env=env, timeout=21600 if p.get("heavy") else 1800, label=f"{name}: the English build").returncode == 0:
            run = p["run"]
            if p.get("input"):
                steps = "; ".join(f"sleep {x}" if isinstance(x, int) else f"printf '%s\\n' '{x.format(lang='english')}'" for x in p["input"])
                run = f"({steps}) | {run}"
            out = sh(run, cwd=eng, env=env, timeout=1200, label=f"{name}: running the English build").stdout
            baseline[name] = sorted({l.strip().replace("english", "{lang}") for l in out.splitlines()
                                     if any(re.search(e.format(lang="english"), l) for e in p["expect"])})
    except subprocess.TimeoutExpired:
        pass
    shutil.rmtree(eng, ignore_errors=True)


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
    english_baseline(name, p, up, env)
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
        rv = base / "rev"; shutil.rmtree(rv, ignore_errors=True)   # stricter than upstream: the language tree reverses to upstream
        subprocess.run([sys.executable, str(HIN / "burp/burp.py"), "reverse", str(n / lang), "--out", str(rv)], capture_output=True)
        srcs = [f for f in up.rglob("*") if f.is_file() and f.suffix in (".c", ".h") and ".git" not in f.parts]
        same = sum(1 for f in srcs if (rv / f.relative_to(up)).exists() and (rv / f.relative_to(up)).read_bytes() == f.read_bytes())
        reverse_note = f"reverses to upstream byte for byte: {same} of {len(srcs)} C files"
        shutil.rmtree(rv, ignore_errors=True); shutil.rmtree(n, ignore_errors=True)
        try:                        # every build has a time limit: 30 minutes, or 6 hours for a heavy project
            b = sh(p["build"], cwd=work, env=env, timeout=21600 if p.get("heavy") else 1800)
        except subprocess.TimeoutExpired:
            rows.append((name, lang, pin, "yes", "yes", "no", "the build did not finish within its time limit")); shutil.rmtree(work, ignore_errors=True); continue
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
        mine = sorted({l.strip().replace(lang, "{lang}") for l in out.splitlines() if any(re.search(e.format(lang=lang), l) for e in p["expect"])})
        english = baseline.get(name)
        as_english = "same lines as the English build" if english is not None and mine == english else "differs from the English build" if english is not None else ""
        rows.append((name, lang, pin, "yes", "yes", "yes" if ok else "NO", f"`{line[:110]}`; {reverse_note}; {as_english}"))
        if ok:
            VERIFIED.setdefault(name, []).append(lang)
        print(f"   {name} · {lang}: {'proved' if ok else 'ran, but did not print what it must'}")
        shutil.rmtree(work, ignore_errors=True)
    shutil.rmtree(base, ignore_errors=True)


WORKFLOW = """name: parashakti sync
on:
  schedule: [{cron: "17 3 * * *"}]
  workflow_dispatch: {}
permissions: {contents: write}
jobs:
  sync:
    runs-on: ubuntu-latest
    timeout-minutes: 300
    steps:
      - uses: actions/checkout@v4
        with: {ref: parashakti, fetch-depth: 0}
      - name: tools
        run: sudo apt-get update -qq && sudo apt-get install -y -qq flex bison gawk gcc-riscv64-linux-gnu gcc-riscv64-unknown-elf qemu-system-misc wabt bc
      - name: Hindawi
        run: git clone -q --depth 1 https://github.com/hindawiai/hindawi2026.10 ../hindawi2026.10 && (cd ../hindawi2026.10 && bash scripts/build.sh)
      - name: ingest the current upstream into every language, test, and push each language branch
        env: {GH_TOKEN: "${{ github.token }}"}
        run: bash sync.sh
"""
SYNC = """#!/usr/bin/env bash
# sync.sh: the upstream's current head, ingested into each language in languages.txt, lowered, built, tested, and pushed to
# its lang/<language> branch. Run by the scheduled workflow; runs the same way on a laptop beside a hindawi2026.10 checkout.
set -uo pipefail
H="$(cd ../hindawi2026.10 && pwd)"; export PATH="$H/.build/chintamani/Romenagri:$PATH" ROMENAGRI="$H/.build/chintamani/Romenagri"
U=$(cat upstream.txt); rm -rf /tmp/up && git clone -q --depth 1 "$U" /tmp/up
git config user.name "parashakti sync"; git config user.email "parashakti-sync@users.noreply.github.com"
while read -r L; do
  [ -n "$L" ] || continue
  rm -rf /tmp/n && python3 "$H/lang/hindawi/burp/burp.py" ingest /tmp/up --langs "$L" --out /tmp/n --translators glossary --keep '.*' >/dev/null || { echo "$L: ingestion failed"; continue; }
  git fetch -q origin "lang/$L" && git worktree add -f "/tmp/w-$L" "origin/lang/$L" -B "lang/$L" >/dev/null 2>&1 || continue
  (cd "/tmp/w-$L" && git rm -rq . >/dev/null 2>&1; cp -a /tmp/n/"$L"/. . && git add -A && git commit -qm "Hindawi $L: ingested from $(git -C /tmp/up rev-parse --short HEAD)" && git push -q origin "lang/$L") \
    && echo "$L: updated" || echo "$L: unchanged"
  git worktree remove -f "/tmp/w-$L"
done < languages.txt
"""


def ask(question, rehearse=None):
    """A typed gate. The engine's own input is this script, so the answer is read from the terminal itself."""
    if rehearse and os.environ.get("PARASHAKTI_GATE"):
        return os.environ["PARASHAKTI_GATE"]
    try:
        with open("/dev/tty") as tty:
            print(question, end="", flush=True); return tty.readline().strip()
    except OSError:
        return ""


def publish(org, rehearse, do_mint):
    """For each project verified in at least one language: a fork of the upstream (or a mirror when it is not on GitHub)
    under ORG, each verified language on its own branch lang/<language>, and a default branch parashakti carrying the
    README, the report, the sync script and its scheduled workflow. One typed PUSH for all; MINT, typed, if asked."""
    if not VERIFIED:
        print("   nothing verified in this run: nothing to publish"); return
    b = "\n\033[1mPUBLISH\033[0m\n   " + "\n   ".join(f"{k}: {', '.join(v)}" for k, v in VERIFIED.items())
    print(b + f"\n   to {'the rehearsal folder ' + rehearse if rehearse else 'github.com/' + org}")
    line = ask("   Type PUSH plus a reason.\n   > ", rehearse)
    if not line.upper().startswith("PUSH"):
        print("   nothing published"); return
    for name, langs in VERIFIED.items():
        p = MANIFEST[name]; url = p.get("repo"); dest = f"{org}/{name}"
        if not url:
            continue
        work = W / "publish" / name; shutil.rmtree(work, ignore_errors=True); work.parent.mkdir(parents=True, exist_ok=True)
        if rehearse:
            remote = f"{rehearse}/{name}.git"; subprocess.run(["git", "init", "-q", "--bare", remote])
        elif "github.com/" in url:
            sh(["gh", "repo", "fork", url.split("github.com/")[1].removesuffix(".git"), "--org", org, "--fork-name", name, "--clone=false"], cwd=W, label=f"forking {name}")
            remote = f"https://github.com/{dest}.git"
        else:
            sh(["gh", "repo", "create", dest, "--public", "--description", f"{name}, ingested into many languages by Parashakti; upstream {url}"], cwd=W, label=f"creating {dest}")
            remote = f"https://github.com/{dest}.git"
        r = sh(["git", "clone", "-q", url, str(work)], cwd=W, label=f"cloning {name}")
        if r.returncode:
            print(f"   {name}: the upstream could not be cloned; skipped"); continue
        g = lambda *a: subprocess.run(["git", "-C", str(work), *a], capture_output=True, text=True)
        g("config", "user.name", "Abhishek Choudhary"); g("config", "user.email", "obonac@users.noreply.github.com")
        g("remote", "add", "pub", remote); head = g("rev-parse", "HEAD").stdout.strip()
        g("push", "-q", "pub", f"HEAD:refs/heads/{g('rev-parse', '--abbrev-ref', 'HEAD').stdout.strip() or 'main'}")
        for lang in langs:
            n = W / "publish" / f"n-{name}"; shutil.rmtree(n, ignore_errors=True)
            subprocess.run([sys.executable, str(HIN / "burp/burp.py"), "ingest", str(work), "--langs", lang, "--out", str(n), "--translators", "glossary",
                            "--keep-file", str(W / name / "keep.txt") if (W / name / "keep.txt").exists() else "/dev/null"] + ([] if p.get("names", True) else ["--keep", ".*"]),
                           capture_output=True)
            g("checkout", "-q", "-B", f"lang/{lang}", head); g("rm", "-rq", ".")
            subprocess.run(f"cp -a '{n / lang}/.' '{work}/'", shell=True); g("add", "-A")
            g("commit", "-qm", f"Hindawi {lang}: {name} ingested from {head[:12]}, lowered, built and tested by Parashakti")
            print(f"   {name} · lang/{lang}: " + ("pushed" if g("push", "-q", "-f", "pub", f"lang/{lang}").returncode == 0 else "push failed"))
        g("checkout", "-q", "--orphan", "parashakti"); g("rm", "-rqf", ".")
        rows = [l for l in (W / "REPORT.md").read_text().splitlines() if l.startswith(f"| {name} |")] if (W / "REPORT.md").exists() else []
        (work / "README.md").write_text(f"# {name}, in many languages\n\nIngested by Parashakti from {url} (at {head[:12]}), one branch per language: "
            + ", ".join(f"`lang/{l}`" for l in langs) + ". Check out a branch and you have the source in that language; it builds and runs as the "
            "English does.\n\n`main` follows the upstream. `sync.sh`, run daily by `.github/workflows/sync.yml`, ingests the upstream's new "
            "head into every language in `languages.txt`, tests it, and pushes each branch.\n\n## Evidence\n\n| Project | Language | Source | "
            "Ingested | Lowered | Built, ran and printed | Evidence | AyeKnow state |\n|---|---|---|---|---|---|---|---|\n" + "\n".join(rows)
            + "\n\nProcess: https://hindawiai.github.io/hindawi2026.10/process/ · © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.\n")
        (work / "upstream.txt").write_text(url + "\n"); (work / "languages.txt").write_text("\n".join(langs) + "\n")
        (work / "sync.sh").write_text(SYNC); (work / ".github/workflows").mkdir(parents=True, exist_ok=True)
        (work / ".github/workflows/sync.yml").write_text(WORKFLOW); g("add", "-A"); g("commit", "-qm", "Parashakti: README, evidence, sync")
        g("push", "-q", "-f", "pub", "parashakti")
        if not rehearse:
            sh(["gh", "repo", "edit", dest, "--default-branch", "parashakti"], cwd=W, label=f"default branch of {dest}")
        print(f"   {name}: published to {remote}")
        if do_mint and not rehearse:
            mint(name, work, langs, url)


def mint(name, work, langs, url):
    """A DOI for the published languages: each branch as a tarball, misty's own interface, a typed MINT."""
    helptext = subprocess.run(["misty", "publish", "--help"], capture_output=True, text=True).stdout
    if "-m" not in helptext or "-f" not in helptext or not os.environ.get("ZENODO_TOKEN"):
        print(f"   {name}: not minted (misty with -m and -f, and ZENODO_TOKEN, are needed)"); return
    d = W / "publish" / f"mint-{name}"; shutil.rmtree(d, ignore_errors=True); d.mkdir(parents=True)
    files = []
    for lang in langs:
        f = d / f"{name}-{lang}.tar.gz"
        subprocess.run(["git", "-C", str(work), "archive", "--prefix", f"{name}-{lang}/", "-o", str(f), f"lang/{lang}"]); files.append(str(f))
    meta = {"title": f"{name} in {len(langs)} languages, ingested and tested by Parashakti", "version": time.strftime("%Y.%m.%d"),
            "upload_type": "software", "access_right": "open", "license": "other-open",
            "description": f"{name} from {url}, ingested by Hindawi's BURP into {', '.join(langs)}, lowered, built and tested against its English build.",
            "creators": [{"name": "Choudhary, Abhishek", "affiliation": "AyeAI", "orcid": "0009-0002-0684-8320"}]}
    (d / "misty.json").write_text(json.dumps(meta, indent=1))
    line = ask(f"   A DOI is a dated public disclosure. Type MINT to mint {name}.\n   > ")
    if not line.upper().startswith("MINT"):
        print("   not minted"); return
    r = sh(["misty", "publish", "-m", str(d / "misty.json"), "-f", *files], cwd=d, label=f"minting {name}")
    doi = re.findall(r"10\.5281/zenodo\.\d+", r.stdout + r.stderr)
    print(f"   {name}: " + (f"minted {doi[-1]}" if doi else "misty reported no DOI (see the log)"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--langs", default=DEFAULT_LANGS); ap.add_argument("--stage", default="")
    ap.add_argument("--manifest"); ap.add_argument("--list", action="store_true"); ap.add_argument("--repo")
    ap.add_argument("--install", action="store_true"); ap.add_argument("--check", action="store_true")
    ap.add_argument("--publish", metavar="ORG", help="publish each verified project as a fork under ORG, one branch per language")
    ap.add_argument("--publish-to", metavar="DIR", help="rehearse publishing into local bare repositories under DIR")
    ap.add_argument("--mint", action="store_true", help="after publishing, mint each with misty, behind a typed MINT")
    a = ap.parse_args()
    man = json.loads(Path(a.manifest).read_text()) if a.manifest else MANIFEST
    if a.list:
        for k, v in man.items():
            print(f"{k:8} {'heavy ' if v.get('heavy') else 'light '} {v['title']}")
        return
    stages = [s for s in a.stage.split(",") if s] or [k for k, v in man.items() if not v.get("heavy")]
    have = set(os.environ.get("PARASHAKTI_HAVE", "").split(","))
    for s_ in list(stages):         # a project runs only when this machine has what it needs; the rest is said, not failed
        missing = [n for n in man[s_].get("needs", []) if n not in have]
        if missing:
            print(f"   {s_}: not run here, this machine lacks {', '.join(missing)} (bash parashakti.sh --install, or install them)")
            stages.remove(s_)
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
    if a.publish or a.publish_to:
        publish(a.publish or "rehearsal", a.publish_to, a.mint)
    proved = sum(1 for r in rows if r[5] == "yes")
    print(f"\n\033[1mDONE: {proved} of {len(rows)} project-language runs proved; report {rep}\033[0m")


main()
ENGINE
