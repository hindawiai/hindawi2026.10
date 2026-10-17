#!/usr/bin/env bash
# stack.sh: the sovereign stack through Hindawi, one stage at a time. Every upstream is fetched at a pinned release
# (or its default branch where no release is pinned, the commit then recorded), ingested by BURP into every language
# at once, measured for how much is localised (the target is 100%), reversed to prove nothing is lost, and, with
# --build, built through the compilation path. Nothing here is per architecture: the host's own toolchain builds,
# and CROSS_COMPILE, if set, passes through to every build unchanged (x86, Power, ARM, RISC-V, Xtensa, MCUs alike).
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
#
#   bash scripts/sovereign/stack.sh --list                     the stack, stage by stage
#   bash scripts/sovereign/stack.sh --stage L07                 one stage (firmware); the way to work through it
#   bash scripts/sovereign/stack.sh --only seabios,tinycc --langs hindi,urdu,sindhi --build
#   bash scripts/sovereign/stack.sh --stage gate                the GATE programming domains, from Rosetta Code
#   bash scripts/sovereign/stack.sh --summary                   the self-hosting and boundary table from the report
#   options: --scripts brahmi   render Devanagari ingestions in every Brahmi script;  --full   whole trees
#
# Run from the repository root. Everything goes under .build/sovereign/. Each step lands in
# .build/sovereign/report.tsv as PASS, FAIL, UNJUDGED (a tool or the network is missing) or SKIP, with its reason; a
# failing step never stops the run. Exit 0 when nothing failed. Needs git, python3, gcc and make; --build also needs
# flex and the pinned Chintamani (scripts/fetch.sh, scripts/build.sh); the hardware checks use whichever of ghdl,
# yosys, iverilog, nextpnr, openroad and icepack are installed, and are UNJUDGED otherwise.
set -uo pipefail
cd "$(dirname "$0")/../.." || exit 3
R="$PWD"; W="$R/.build/sovereign"; mkdir -p "$W/src" "$W/out" "$W/logs" "$W/back"
LANGS=all; SCRIPTS=""; ONLY=""; STAGE=""; BUILD=0; FULL=0; LIST=0; SUMMARY=0; JOBS="$(nproc 2>/dev/null || echo 2)"
while [ $# -gt 0 ]; do case "$1" in
  --langs) LANGS="$2"; shift ;; --scripts) SCRIPTS="$2"; shift ;; --only) ONLY="$2"; shift ;; --stage) STAGE="$2"; shift ;;
  --build) BUILD=1 ;; --full) FULL=1 ;; --list) LIST=1 ;; --summary) SUMMARY=1 ;; --jobs) JOBS="$2"; shift ;;
  -h|--help) sed -n '2,22p' "$0"; exit 0 ;; *) echo "stack: unknown option $1"; exit 3 ;; esac; shift; done
REPORT="$W/report.tsv"; [ -f "$REPORT" ] || printf 'stage\tproject\tstep\tstatus\treason\n' > "$REPORT"
record() { printf '%s\t%s\t%s\t%s\t%s\n' "$1" "$2" "$3" "$4" "$5" >> "$REPORT"; printf '  %-6s %-16s %-14s %-9s %s\n' "$1" "$2" "$3" "$4" "$5"; }
have() { command -v "$1" >/dev/null 2>&1; }

# stage | project | repository (owner/name on GitHub, or a full URL, or local:path) | release ("-" default branch) | subtree
PROJECTS="L00|shakti-cclass|https://gitlab.com/shaktiproject/cores/c-class.git|-|src
L00|shakti-soc|https://gitlab.com/shaktiproject/cores/shakti-soc.git|-|.
L00|neorv32|stnolting/neorv32|-|rtl/core
L00|serv|olofk/serv|-|rtl
L00|ibex|lowRISC/ibex|-|rtl
L00|esp-idf|espressif/esp-idf|v5.2|components/esp_system
L01|yosys|YosysHQ/yosys|-|kernel
L01|nextpnr|YosysHQ/nextpnr|-|common
L01|openroad|The-OpenROAD-Project/OpenROAD|-|src/gpl
L02|flex|westes/flex|v2.6.4|src
L02|bison|akimd/bison|v3.8.2|src
L03|gcc-c|gcc-mirror/gcc|releases/gcc-13.2.0|gcc/c
L03|gcc-cxx|gcc-mirror/gcc|releases/gcc-13.2.0|gcc/cp
L03|libstdcxx|gcc-mirror/gcc|releases/gcc-13.2.0|libstdc++-v3/src
L03|libgcc|gcc-mirror/gcc|releases/gcc-13.2.0|libgcc
L03|gas|bminor/binutils-gdb|binutils-2_42|gas
L03|ld|bminor/binutils-gdb|binutils-2_42|ld
L03|binutils|bminor/binutils-gdb|binutils-2_42|binutils
L03|gdb|bminor/binutils-gdb|binutils-2_42|gdb
L03|llvm-clang|llvm/llvm-project|llvmorg-17.0.6|clang/lib/Lex
L03|tinycc|TinyCC/tinycc|release_0_9_27|.
L04|make|mirror/make|-|src
L04|buildroot|buildroot/buildroot|2024.02|support
L05|musl|bminor/musl|v1.2.5|src/string
L05|glibc|bminor/glibc|glibc-2.39|string
L05|ld.so|bminor/glibc|glibc-2.39|elf
L05|newlib|bminor/newlib|-|newlib/libc/string
L06|patchelf|NixOS/patchelf|0.18.0|src
L07|seabios|coreboot/seabios|rel-1.16.3|src
L07|coreboot|coreboot/coreboot|24.02|src/lib
L08|xv6|mit-pdos/xv6-riscv|-|kernel
L08|freertos|FreeRTOS/FreeRTOS-Kernel|V11.0.1|.
L08|zephyr|zephyrproject-rtos/zephyr|v3.6.0|kernel
L08|linux|torvalds/linux|v6.6|kernel/sched
L09|bash|bminor/bash|bash-5.2|builtins
L09|busybox|mirror/busybox|1_36_1|coreutils
L09|coreutils|coreutils/coreutils|v9.5|src
L10|tvm|apache/tvm|v0.15.0|src/tir/transforms
L10|onnxruntime|microsoft/onnxruntime|v1.17.0|onnxruntime/core/common
L10|llama.cpp|ggerganov/llama.cpp|-|common
L11|openblas|OpenMathLib/OpenBLAS|v0.3.28|interface
L11|onednn|oneapi-src/oneDNN|v3.4|src/common
L11|xnnpack|google/XNNPACK|-|src/subgraph
L12|micro-ros|ros2/rclc|-|rclc/src
L12|opencv|opencv/opencv|4.9.0|modules/core/src
L13|lua|lua/lua|v5.4.6|.
L13|micropython|micropython/micropython|v1.22.2|py
L14|sutram|hindawiai/sanskrit|-|lang
L14|pushkalavati|hindawiai/sanskrit|-|tools/pushkalavati-compiler/src
L14|romenagri|hindawiai/chintamani|-|Romenagri
L14|shailis|hindawiai/chintamani|-|Hindawi
L14|burp|local:lang/hindawi/burp|-|.
L14|name-abi|local:lang/hindawi/tools|-|.
L14|provenance|local:ops|-|."

STAGES="L00 processor RTL (Shakti C-Class and SoC, NEORV32, SERV, Ibex, ESP-IDF)
L01 synthesis, FPGA and physical design (Yosys, nextpnr, OpenROAD)
L02 lexer and parser generators (flex, bison)
L03 compiler, assembler, linker, debugger (GCC C, C++, libstdc++, libgcc; binutils gas, ld, ar, objcopy; gdb; LLVM/Clang; TinyCC)
L04 build automation and distribution (make, Buildroot)
L05 C libraries and the dynamic linker (musl, glibc, ld.so, Newlib)
L06 ELF middleware (patchelf)
L07 firmware and bootloaders (SeaBIOS, coreboot)
L08 kernels (xv6-riscv, FreeRTOS, Zephyr, Linux)
L09 shell and userland (Bash, BusyBox, coreutils)
L10 AI graph compilation and runtime (TVM, ONNX Runtime, llama.cpp)
L11 numerical and tensor acceleration (OpenBLAS, oneDNN, XNNPACK)
L12 robotics and peripherals (micro-ROS, OpenCV)
L13 language runtimes (Lua, MicroPython)
L14 our own infrastructure (Sūtram, Pushkalāvatī, Romenagri, the shailis, BURP, the name ABI, provenance)
gate GATE programming domains (Rosetta Code programs per domain, not syllabus text)"
if [ "$LIST" = 1 ]; then echo "$STAGES"; exit 0; fi

# summary: the self-hosting items and the hardware boundary, read from the report
summary() {
  echo; echo "Self-hosting and boundary (PASS once any language built the named projects):"
  while IFS='|' read -r item needs; do
    st="not yet"; for p in ${needs//,/ }; do grep -qP "\t$p\tbuild:[^\t]*\tPASS" "$REPORT" && st=PASS; done
    printf '  %-34s %-8s %s\n' "$item" "$st" "$needs"
  done <<'MAP'
native compiler|gcc-c,tinycc
native assembler|gas
native linker|ld
native lexer generator|flex
native parser generator|bison
native build system|make
native libc|musl,glibc,newlib
native shell|bash,busybox
native core utilities|coreutils,busybox
native debugger|gdb
native object and binary utilities|binutils,patchelf
native root filesystem|buildroot
native OS kernel|linux,xv6,zephyr,freertos
native firmware|seabios,coreboot
native hardware toolchain|yosys,nextpnr,openroad
native AI compilation and runtime|tvm,onnxruntime,llama.cpp
MAP
  for t in ghdl yosys iverilog nextpnr-ice40 openroad icepack verilator; do printf '  %-34s %s\n' "tool: $t" "$(have $t && echo installed || echo 'not installed (its checks are UNJUDGED)')"; done
}
if [ "$SUMMARY" = 1 ]; then summary; exit 0; fi
for t in git python3 gcc make; do have "$t" || { echo "stack: $t is required"; exit 3; }; done
echo "Sovereign stack through Hindawi · stage: ${STAGE:-all} · languages: $LANGS · build: $BUILD"
FAILED=0
ingest_measure_reverse() {   # stage name src
  local stage="$1" name="$2" src="$3" O="$W/out/$2" L="$W/logs/$2" extra=()
  [ -n "$SCRIPTS" ] && extra=(--scripts "$SCRIPTS")
  if python3 lang/hindawi/burp/burp.py ingest "$src" --langs "$LANGS" --out "$O" --jobs "$JOBS" "${extra[@]}" > "$L.ingest.log" 2>&1; then
    record "$stage" "$name" ingest PASS "$(grep -c '^burp:' "$L.ingest.log") ingestions"
  else record "$stage" "$name" ingest FAIL "$(tail -1 "$L.ingest.log")"; FAILED=1; return 1; fi
  if python3 scripts/sovereign/measure.py "$src" "$O" --project "$name" --tsv "$L.measure.tsv" > "$L.measure.log" 2>&1; then
    record "$stage" "$name" measure PASS "keywords localised, best to worst: $(sort -t$'\t' -k4 -gr "$L.measure.tsv" | awk -F'\t' 'NR==1{b=$2":"$4} {w=$2":"$4} END{print b" .. "w}')"
  else record "$stage" "$name" measure FAIL "$(tail -1 "$L.measure.log")"; FAILED=1; fi
  local bad=0 n=0 f b
  for f in "$O"/*/; do n=$((n+1)); b="$W/back/$name/$(basename "$f")"
    python3 lang/hindawi/burp/burp.py reverse "$f" --out "$b" >/dev/null 2>&1 && diff -rq "$src" "$b" -x .git >/dev/null 2>&1 || bad=$((bad+1)); done
  [ "$bad" = 0 ] && record "$stage" "$name" reverse PASS "$n of $n back byte for byte" || { record "$stage" "$name" reverse FAIL "$bad of $n differ"; FAILED=1; }
}
hardware_checks() {   # name reversed-tree
  local name="$1" b="$2"
  case "$name" in
    neorv32) have ghdl && { (cd "$b" && ghdl -i --std=08 --work=neorv32 *.vhd >/dev/null 2>&1 && ghdl -m --std=08 --work=neorv32 neorv32_top >/dev/null 2>&1) \
               && record L00 "$name" vhdl PASS "GHDL elaborates the reversed core" || record L00 "$name" vhdl FAIL "GHDL rejects it"; } \
             || record L00 "$name" vhdl UNJUDGED "ghdl not installed" ;;
    serv)    have yosys && { yosys -q -p "read_verilog $(ls "$b"/*.v | tr '\n' ' '); synth -top serv_rf_top" >/dev/null 2>&1 \
               && record L00 "$name" synth PASS "Yosys synthesises the reversed core" || record L00 "$name" synth FAIL "Yosys rejects it"; } \
             || record L00 "$name" synth UNJUDGED "yosys not installed" ;;
    ibex)    have verilator && { verilator --lint-only -Wno-fatal "$b"/*.sv >/dev/null 2>&1 \
               && record L00 "$name" lint PASS "Verilator reads the reversed SystemVerilog" || record L00 "$name" lint FAIL "Verilator rejects it"; } \
             || record L00 "$name" lint UNJUDGED "verilator not installed" ;;
  esac
}
while IFS='|' read -r stage name repo tag sub; do
  [ -n "$STAGE" ] && [ "$STAGE" != "$stage" ] && continue
  [ -n "$ONLY" ] && ! grep -qw -- "$name" <<<"${ONLY//,/ }" && continue
  [ "$FULL" = 1 ] && sub="."
  S="$W/src/$name"
  case "$repo" in
    local:*) S="$R/${repo#local:}"; record "$stage" "$name" fetch PASS "this repository" ;;
    *) url="$repo"; [[ "$repo" == *://* ]] || url="https://github.com/$repo.git"
       if [ ! -d "$S/.git" ]; then
         args=(--depth 1); [ "$tag" != "-" ] && args+=(--branch "$tag")
         git clone -q "${args[@]}" "$url" "$S" > "$W/logs/$name.fetch.log" 2>&1 \
           && record "$stage" "$name" fetch PASS "$url ${tag/-/default branch} at $(git -C "$S" rev-parse --short HEAD)" \
           || { record "$stage" "$name" fetch UNJUDGED "clone failed: $(tail -1 "$W/logs/$name.fetch.log")"; continue; }
       else record "$stage" "$name" fetch PASS "cached at $(git -C "$S" rev-parse --short HEAD)"; fi ;;
  esac
  [ -e "$S/$sub" ] || { record "$stage" "$name" ingest FAIL "no $sub there"; FAILED=1; continue; }
  ingest_measure_reverse "$stage" "$name" "$S/$sub" || continue
  hardware_checks "$name" "$W/back/$name/$(ls "$W/out/$name" | head -1)"
  if [ "$BUILD" = 1 ] && [ "$stage" != L00 ] && [ "$stage" != L01 ]; then
    for f in "$W/out/$name"/*/; do t="$(basename "$f")"
      python3 lang/hindawi/tools/build_project.py "$f" --lang "${t%@*}" --work "$W/build/$name/$t" > "$W/logs/$name.build.$t.log" 2>&1 \
        && record "$stage" "$name" "build:$t" PASS built || { record "$stage" "$name" "build:$t" FAIL "$(tail -1 "$W/logs/$name.build.$t.log")"; FAILED=1; }
    done
  fi
done <<< "$PROJECTS"

# the GATE programming domains: Rosetta Code's programs for each domain, fetched sparsely, ingested like any project
if [ -z "$ONLY" ] && { [ -z "$STAGE" ] || [ "$STAGE" = gate ]; }; then
  G="$W/src/rosetta"; T="$W/src/gate"
  DOMAINS="algorithms/sorting Sorting-algorithms-Quicksort Sorting-algorithms-Merge-sort Sorting-algorithms-Heapsort
algorithms/searching Binary-search
algorithms/greedy Huffman-coding Knapsack-problem-Continuous
algorithms/dynamic-programming Knapsack-problem-0-1 Longest-common-subsequence Levenshtein-distance
algorithms/graphs Dijkstras-algorithm Floyd-Warshall-algorithm Topological-sort
algorithms/divide-and-conquer Towers-of-Hanoi Matrix-multiplication
algorithms/backtracking N-queens-problem
data-structures Stack Queue-Definition Tree-traversal Priority-queue Hash-from-two-arrays
programming/recursion Fibonacci-sequence Ackermann-function Greatest-common-divisor
discrete-mathematics Sieve-of-Eratosthenes Primality-by-trial-division Combinations
theory-of-computation Finite-state-machine Universal-Turing-machine
compiler-design Parsing-RPN-calculator-algorithm Arithmetic-evaluation Tokenize-a-string-with-escaping
operating-systems Dining-philosophers
computer-networks CRC-32 Parse-an-IP-Address
digital-logic Gray-code Bitwise-operations Four-bit-adder
databases Hash-join"
  if [ ! -d "$G/.git" ]; then
    git clone -q --depth 1 --filter=blob:none --sparse https://github.com/acmeism/RosettaCodeData.git "$G" > "$W/logs/gate.fetch.log" 2>&1 \
      || { record gate rosetta fetch UNJUDGED "clone failed: $(tail -1 "$W/logs/gate.fetch.log")"; DOMAINS=""; }
  fi
  if [ -n "$DOMAINS" ]; then
    pats=(); while read -r dom tasks; do for t in $tasks; do for l in C C++ Java Python VHDL Verilog; do pats+=("/Task/$t/$l/"); done; done; done <<< "$DOMAINS"
    git -C "$G" sparse-checkout set --no-cone "${pats[@]}" > "$W/logs/gate.sparse.log" 2>&1
    rm -rf "$T"; n=0
    while read -r dom tasks; do for t in $tasks; do for l in C C++ Java Python VHDL Verilog; do
      [ -d "$G/Task/$t/$l" ] || continue; mkdir -p "$T/$dom/$t/$l"; cp "$G/Task/$t/$l"/* "$T/$dom/$t/$l/" 2>/dev/null && n=$((n+1)); done; done; done <<< "$DOMAINS"
    record gate rosetta fetch PASS "$n task-language sets across $(grep -c . <<< "$DOMAINS") domains"
    [ "$n" -gt 0 ] && ingest_measure_reverse gate gate "$T"
  fi
fi
summary
echo; echo "report: $REPORT · per-language localisation: $W/logs/<project>.measure.tsv"
awk -F'\t' 'NR>1 {c[$4]++} END {for (s in c) printf "  %s %d\n", s, c[s]}' "$REPORT"
exit "$FAILED"
