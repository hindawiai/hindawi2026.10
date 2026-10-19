#!/usr/bin/env bash
# build.sh: rebuild apcisr.wasm from these sources and check it against the native build of the original.
# The sources are hindawiai/chintamani APCISR/ (© 2003–2006 Abhishek Choudhary, GPL-2.0-or-later, see copying) with two
# lines added to acii2csr.c, each "APCISR_TRACE;", and one #include: they record state for the visualisation and change
# nothing else. Needs clang, wasi-libc and libclang-rt-dev-wasm32 (Ubuntu: apt install clang lld wasi-libc libclang-rt-18-dev-wasm32).
set -euo pipefail
cd "$(dirname "$0")"
clang --target=wasm32-wasi --sysroot=/usr -O2 -w -nostartfiles -Wl,--no-entry -Wl,--gc-sections -I . -o apcisr.wasm wasm.c acii2csr.c
gcc -w -O0 -DTRACED -I . -o drv drv.c acii2csr.c
echo "built apcisr.wasm ($(wc -c < apcisr.wasm) bytes); compare it with: ./drv < inputs > expected; node test_wasm.js"
