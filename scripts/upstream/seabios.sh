#!/usr/bin/env bash
# seabios.sh: real firmware through Hindawi. SeaBIOS (pinned by scripts/fetch.sh) is built as it is, then its C
# is carried to a language through that language's Guru pair and back, built again and booted under system QEMU.
# Pass or fail, it reports; it never edits the repository. Needs qemu-system-x86_64, gcc, make, python3, flex.
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
#   bash scripts/upstream/seabios.sh [cell folder]   default: Chintamani's own guru (Hindi)
set -uo pipefail
cd "$(dirname "$0")/../.."; R="$PWD"; B="$R/.build"; [ -d "$B/seabios" ] || bash scripts/fetch.sh
export ROMENAGRI="$B/chintamani/Romenagri"; CELL="${1:-$B/chintamani/Hindawi/guru}"
boot() { timeout 8 qemu-system-x86_64 -bios "$1/out/bios.bin" -display none -no-reboot -m 64 -serial none -monitor none \
  -chardev file,id=d,path="$1/boot.log" -device isa-debugcon,iobase=0x402,chardev=d >/dev/null 2>&1; grep -m1 "SeaBIOS (version" "$1/boot.log"; }
for t in orig native; do rm -rf "$B/sb-$t"; cp -a "$B/seabios" "$B/sb-$t"; done
python3 lang/hindawi/tests/cells/cells.py tree --cell "$CELL" --src "$B/sb-native/src"
for t in orig native; do
  (cd "$B/sb-$t" && make -s defconfig >/dev/null 2>&1; make -s -j"$(nproc)" > build.log 2>&1) \
    && echo "seabios $t: built, $(boot "$B/sb-$t" || echo 'no banner')" || echo "seabios $t: BUILD FAILED (see $B/sb-$t/build.log)"
done
cmp -s "$B/sb-orig/out/bios.bin" "$B/sb-native/out/bios.bin" && echo "seabios: PASS, the firmware built through the language is byte for byte the original" \
  || echo "seabios: FAIL, the firmware differs (identifiers with underscores come back doubled by acii2cf; see docs/hindawi/ADDING-LANGUAGES.md)"
