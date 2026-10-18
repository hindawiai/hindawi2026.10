#!/usr/bin/env bash
# parashakti.sh: Parashakti, the sovereign stack through Hindawi, proved on QEMU on this laptop.
# Each stage fetches its upstream at a pinned point, ingests it with BURP into every chosen language (keywords and names),
# lowers it through the original Hindawi pipeline (script filter, Romenagri, the language's transducer), cross-compiles it
# under hindawicc, boots or runs it on QEMU, and checks what it prints. Nothing is claimed that the run does not show:
# REPORT.md records, per stage and language, the pinned source, the result, and the console lines that prove it.
#   bash parashakti.sh                                  every stage, the default languages
#   bash parashakti.sh --langs urdu,tamil --stage xv6   one stage, chosen languages
#   bash parashakti.sh --repo DIR                       an existing checkout of hindawiai/hindawi2026.10
# Stages: shakti (bare metal on QEMU's SHAKTI C-class machine), xv6 (the xv6 kernel and shell on QEMU's RISC-V virt
# machine), seabios (the x86 BIOS on QEMU), tinycc (a localised TinyCC that then compiles a program). Everything is
# written under ./parashakti; sources are deleted after each stage's language builds, so disk use stays small.
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. Parashakti™, Hindawi™ and BURP™ are his trademarks.
set -uo pipefail
W="$PWD/parashakti"; REPO=""; STAGES="shakti,xv6,seabios,tinycc"
LANGS="hindi,sanskrit,urdu,arabic,persian,tamil,telugu,kannada,kashmiri,punjabi,punjabi_shahmukhi,sindhi,pashto,dari,bengali,marathi,gujarati,odia"
while [ $# -gt 0 ]; do
  case "$1" in --repo) REPO="$2"; shift 2 ;; --langs) LANGS="$2"; shift 2 ;; --stage) STAGES="$2"; shift 2 ;;
    *) echo "parashakti: unknown option $1"; exit 2 ;; esac
done
mkdir -p "$W/logs"; LOG="$W/logs/parashakti.$(date -u +%Y%m%dT%H%M%SZ).log"; REPORT="$W/REPORT.md"
b(){ printf '\n\033[1m%s\033[0m\n' "$*"; }; i(){ printf '   %s\n' "$*"; }
# ---- prerequisites: installed here, not listed for the operator to fetch
need=(git python3 gcc make flex bison gawk iconv qemu-system-riscv64 qemu-system-x86_64 riscv64-linux-gnu-gcc)
pkg=(git python3 gcc make flex bison gawk libc-bin qemu-system-misc qemu-system-x86 gcc-riscv64-linux-gnu)
miss=(); for k in "${!need[@]}"; do command -v "${need[$k]}" >/dev/null || miss+=("${pkg[$k]}"); done
if [ ${#miss[@]} -gt 0 ]; then
  b "INSTALLING ${miss[*]} (sudo asks for your password once)"
  sudo apt-get update -qq && sudo apt-get install -y -qq "${miss[@]}" python3-setuptools >>"$LOG" 2>&1 || { i "apt failed: see $LOG"; exit 1; }
fi
# ---- Hindawi, its toolchain, and the two capabilities this needs (patched in place only where the checkout lacks them)
if [ -z "$REPO" ]; then
  REPO="$W/hindawi2026.10"
  [ -d "$REPO/.git" ] || git clone -q --depth 1 https://github.com/hindawiai/hindawi2026.10 "$REPO" >>"$LOG" 2>&1
fi
CC_H="$REPO/lang/hindawi/hindawicc"; BP="$REPO/lang/hindawi/tools/build_project.py"; BURP="$REPO/lang/hindawi/burp/burp.py"
grep -q 'HINDAWI_GCC' "$CC_H" || sed -i 's|^exec gcc "\${args\[@\]}"|exec "${HINDAWI_GCC:-gcc}" "${args[@]}"|' "$CC_H"
grep -q 'HINDAWI_GCC' "$CC_H" || { i "hindawicc cannot take a cross compiler and its anchor moved; stopping"; exit 1; }
python3 - "$BP" <<'PY'
import sys; p = sys.argv[1]; s = open(p).read()
old = 'word = re.compile(r"\\b[A-Za-z_][A-Za-z0-9_]*\\b")'
if old in s:   # a symbol in assembly or a linker script, never a piece of a path (kernel/entry.o stays itself)
    open(p, "w").write(s.replace(old, 'word = re.compile(r"(?<![\\w/.])[A-Za-z_][A-Za-z0-9_]*(?![\\w/.])")'))
PY
if [ ! -x "$REPO/.build/chintamani/Romenagri/rmn2acii" ]; then
  b "BUILDING the Hindawi toolchain: Romenagri and the original transducers"
  (cd "$REPO" && bash scripts/build.sh) >>"$LOG" 2>&1 || { i "toolchain build failed: $LOG"; exit 1; }
fi
# Lexicon words once made by shifting Devanagari code points into other scripts land on code points those scripts never
# assigned (Tamil, Bengali, Gurmukhi); each is rewritten as the script writes that sound, and the affected cells rebuilt.
fixed=$(python3 - "$REPO/lang/hindawi/pipeline/language_params.json" <<'FIX'
import json, sys, unicodedata
p = sys.argv[1]; d = json.load(open(p, encoding="utf-8"))
fix = {"\u09b5": "\u09ac", "\u0a37": "\u0a36", "\u0a43": "\u0a4d\u0a30\u0a3f", "\u0a0b": "\u0a30\u0a3f", "\u0b96": "\u0b95",
       "\u0b97": "\u0b95", "\u0b98": "\u0b95", "\u0b9b": "\u0b9a", "\u0ba0": "\u0b9f", "\u0ba1": "\u0b9f", "\u0ba5": "\u0ba4",
       "\u0ba6": "\u0ba4", "\u0ba7": "\u0ba4", "\u0bac": "\u0baa", "\u0bad": "\u0baa", "\u0bc3": "\u0bcd\u0bb0\u0bc1", "\u0b8b": "\u0bb0\u0bc1"}
langs = set()
for lang, e in d.items():
    for v in (e.values() if isinstance(e, dict) else []):
        if isinstance(v, dict) and isinstance(v.get("native"), str) and any(unicodedata.category(c) == "Cn" for c in v["native"]):
            w = v["native"]
            for a, b in fix.items():
                w = w.replace(a, "\u09f1" if (lang == "assamese" and a == "\u09b5") else b)
            v["native"] = w; langs.add(lang)
if langs:
    json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(",".join(sorted(langs)))
FIX
)
[ -n "$fixed" ] && python3 "$REPO/lang/hindawi/tools/complete_cells.py" --langs "$fixed" >>"$LOG" 2>&1 && i "lexicon words corrected and cells rebuilt for: $fixed"
export PATH="$REPO/.build/chintamani/Romenagri:$PATH" ROMENAGRI="$REPO/.build/chintamani/Romenagri"
{ echo "# Parashakti report"; echo; echo "Run $(date -u +%Y-%m-%dT%H:%M:%SZ) on $(uname -srm); Hindawi $(git -C "$REPO" rev-parse --short HEAD 2>/dev/null);";
  echo "$(qemu-system-riscv64 --version | head -1); $(riscv64-linux-gnu-gcc --version | head -1)."; echo;
  echo "| Stage | Language | Ingested | Built | Ran on QEMU | Evidence |"; echo "|---|---|---|---|---|---|"; } > "$REPORT"
row(){ echo "| $1 | $2 | $3 | $4 | $5 | $6 |" >> "$REPORT"; i "$1 · $2: ingest $3, build $4, run $5"; }
keep_list(){ python3 - "$1" <<'PY'
import re, sys, pathlib
names = set()       # names the assembly, linker scripts, build files and generators refer to stay as they are
for p in pathlib.Path(sys.argv[1]).rglob("*"):
    if p.is_file() and (p.suffix in (".S", ".s", ".ld", ".lds", ".pl", ".py", ".mk", ".sh") or p.name.lower().startswith(("makefile", "gnumakefile", "kconfig"))):
        names |= set(re.findall(r"[A-Za-z_][A-Za-z0-9_]*", p.read_text(errors="replace")))
print("^(" + "|".join(sorted(names)) + ")$" if names else "^$")
PY
}
restore_build_files(){ (cd "$1" && find . -type f \( -name "*.S" -o -name "*.s" -o -name "*.ld" -o -name "*.lds" -o -name "*.pl" -o -name "*.py" \
  -o -name "*.sh" -o -iname "makefile*" -o -name "*.mk" -o -name "Kconfig*" -o -name "configure" -o -name "*.in" \) -exec cp --parents {} "$2/" \;); }
ingest(){ # $1 upstream tree, $2 output: BURP into every language at once, names kept where non-C files refer to them
  python3 "$BURP" ingest "$1" --langs "$LANGS" --out "$2" --translators glossary --keep "$(keep_list "$1")" >>"$LOG" 2>&1; }
build(){ # $1 lang, $2 ingested tree, $3 work dir, rest: make arguments
  local L="$1" N="$2" O="$3"; shift 3
  HINDAWI_GCC="${HGCC:-gcc}" python3 "$BP" "$N" --lang "$L" --work "$O" -- "$@" >>"$LOG" 2>&1; }
IFS=, read -ra LL <<< "$LANGS"
has(){ [[ ",$STAGES," == *",$1,"* ]]; }

# ---- shakti: a bare-metal program on QEMU's SHAKTI C-class board, through its UART
if has shakti; then
  b "STAGE shakti: bare metal on QEMU's SHAKTI C-class machine"
  S="$W/shakti"; rm -rf "$S"; mkdir -p "$S/src"
  cat > "$S/src/main.c" <<'EOF'
#define UART_TX ((volatile unsigned int *) 0x11304)
void put(const char *text) { while (*text) { *UART_TX = (unsigned char) *text; text++; } }
int sum(int count) { int total = 0; for (int index = 1; index <= count; index++) total += index; return total; }
int main(void) {
  int value = sum(10);
  put("Parashakti: Hindawi on SHAKTI, sum 1..10 = ");
  *UART_TX = (unsigned char) ('0' + value / 10);
  *UART_TX = (unsigned char) ('0' + value % 10);
  put("\n");
  for (;;) { }
}
EOF
  printf '  .section .text.start\n  .global _start\n_start:\n  la sp, stack_top\n  call main\n1: j 1b\n  .bss\n  .space 4096\nstack_top:\n' > "$S/src/start.S"
  printf 'ENTRY(_start)\nSECTIONS { . = 0x80000000; .text : { *(.text.start) *(.text*) } .rodata : { *(.rodata*) } .data : { *(.data*) } .bss : { *(.bss*) } }\n' > "$S/src/link.ld"
  printf 'all: prog.elf\nprog.elf: start.S main.c link.ld\n\t$(CC) -march=rv64imac -mabi=lp64 -mcmodel=medany -nostdlib -ffreestanding -O2 -T link.ld -o prog.elf start.S main.c\n' > "$S/src/Makefile"
  ingest "$S/src" "$S/n"
  for L in "${LL[@]}"; do
    [ -d "$S/n/$L" ] || { row shakti "$L" no - - "not ingested"; continue; }
    restore_build_files "$S/src" "$S/n/$L"
    if HGCC=riscv64-linux-gnu-gcc build "$L" "$S/n/$L" "$S/b/$L" CC="$CC_H"; then
      out=$(timeout 5 qemu-system-riscv64 -M shakti_c -nographic -bios "$S/b/$L/prog.elf" 2>/dev/null | head -1)
      [[ "$out" == *"= 55"* ]] && row shakti "$L" yes yes yes "\`$out\`" || row shakti "$L" yes yes NO "\`${out:-no output}\`"
    else row shakti "$L" yes NO - "see the log"; fi
  done
fi

# ---- xv6: the xv6-riscv kernel and its shell, on QEMU's RISC-V virt machine
if has xv6; then
  b "STAGE xv6: the xv6 kernel and shell on QEMU's RISC-V virt machine"
  S="$W/xv6"; rm -rf "$S"; mkdir -p "$S"
  git clone -q --depth 1 https://github.com/mit-pdos/xv6-riscv "$S/up" >>"$LOG" 2>&1 && PIN=$(git -C "$S/up" rev-parse --short HEAD)
  ingest "$S/up" "$S/n"
  for L in "${LL[@]}"; do
    [ -d "$S/n/$L" ] || { row xv6 "$L" no - - "not ingested"; continue; }
    restore_build_files "$S/up" "$S/n/$L"
    if HGCC=riscv64-linux-gnu-gcc build "$L" "$S/n/$L" "$S/b/$L" TOOLPREFIX=riscv64-linux-gnu- kernel/kernel fs.img; then
      out=$( (sleep 6; printf 'echo parashakti-%s\n' "$L"; sleep 3; printf 'ls\n'; sleep 3) | timeout 16 qemu-system-riscv64 -machine virt \
        -bios none -kernel "$S/b/$L/kernel/kernel" -m 128M -smp 1 -nographic -global virtio-mmio.force-legacy=false \
        -drive file="$S/b/$L/fs.img",if=none,format=raw,id=x0 -device virtio-blk-device,drive=x0,bus=virtio-mmio-bus.0 2>&1 )
      sym=$(riscv64-linux-gnu-nm "$S/b/$L/kernel/kernel" | awk '$2 ~ /[Tt]/ {print $3}' | grep -E '^_?[a-z]+(_[a-z]+)+$' | head -3 | tr '\n' ' ')
      if grep -q "parashakti-$L" <<<"$out" && grep -q README <<<"$out" && ! grep -q usertrap <<<"$out"; then
        row xv6 "$L" yes yes yes "xv6 $PIN booted; the shell ran \`echo\` and \`ls\`; kernel symbols from $L names: \`$sym\`"
      else row xv6 "$L" yes yes NO "xv6 $PIN: $(grep -a -m1 'usertrap\|panic' <<<"$out" | head -c 80)"; fi
    else row xv6 "$L" yes NO - "xv6 $PIN: see the log"; fi
    rm -rf "$S/b/$L"
  done
  rm -rf "$S/up" "$S/n"
fi

# ---- seabios: the x86 BIOS, built from the language, booted by QEMU; its banner read from the debug port
if has seabios; then
  b "STAGE seabios: the x86 BIOS on QEMU"
  S="$W/seabios"; rm -rf "$S"; mkdir -p "$S"
  git clone -q --depth 1 --branch rel-1.16.3 https://github.com/coreboot/seabios "$S/up" >>"$LOG" 2>&1
  ingest "$S/up" "$S/n"
  for L in "${LL[@]}"; do
    [ -d "$S/n/$L" ] || { row seabios "$L" no - - "not ingested"; continue; }
    restore_build_files "$S/up" "$S/n/$L"
    if build "$L" "$S/n/$L" "$S/b/$L" && [ -f "$S/b/$L/out/bios.bin" ]; then
      out=$(timeout 8 qemu-system-x86_64 -bios "$S/b/$L/out/bios.bin" -display none -chardev stdio,id=s \
        -device isa-debugcon,iobase=0x402,chardev=s 2>/dev/null | grep -a -m1 "SeaBIOS (version")
      [ -n "$out" ] && row seabios "$L" yes yes yes "\`$out\`" || row seabios "$L" yes yes NO "no banner"
    else row seabios "$L" yes NO - "see the log"; fi
    rm -rf "$S/b/$L"
  done
  rm -rf "$S/up" "$S/n"
fi

# ---- tinycc: TinyCC built from the language, then used to compile and run a program
if has tinycc; then
  b "STAGE tinycc: a localised compiler that compiles"
  S="$W/tinycc"; rm -rf "$S"; mkdir -p "$S"
  git clone -q --depth 1 --branch release_0_9_27 https://github.com/TinyCC/tinycc "$S/up" >>"$LOG" 2>&1
  (cd "$S/up" && ./configure >>"$LOG" 2>&1)            # config.h and config.mak, in host notation, for every language
  ingest "$S/up" "$S/n"
  printf '#include <stdio.h>\nint main(void){ int t=0; for(int i=1;i<=10;i++) t+=i; printf("tcc says %%d\\n", t); return 0; }\n' > "$S/t.c"
  for L in "${LL[@]}"; do
    [ -d "$S/n/$L" ] || { row tinycc "$L" no - - "not ingested"; continue; }
    restore_build_files "$S/up" "$S/n/$L"; cp "$S/up/config.h" "$S/up/config.mak" "$S/n/$L/" 2>/dev/null
    if build "$L" "$S/n/$L" "$S/b/$L" tcc && [ -x "$S/b/$L/tcc" ]; then
      out=$( "$S/b/$L/tcc" -B"$S/b/$L" -I"$S/b/$L/include" -run "$S/t.c" 2>&1 | head -1 )
      [ "$out" = "tcc says 55" ] && row tinycc "$L" yes yes yes "the $L-built tcc compiled and ran a program: \`$out\`" \
        || row tinycc "$L" yes yes NO "\`${out:-no output}\`"
    else row tinycc "$L" yes NO - "see the log"; fi
    rm -rf "$S/b/$L"
  done
  rm -rf "$S/up" "$S/n"
fi
b "DONE: $(grep -c '| yes | yes | yes |' "$REPORT") of $(grep -c '^| [a-z]' "$REPORT") stage-language runs proved; report $REPORT; log $LOG"
