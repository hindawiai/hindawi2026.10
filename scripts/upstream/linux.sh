#!/usr/bin/env bash
# linux.sh: the Linux kernel through Hindawi, pass or fail. Fetches a pinned release from GitHub, carries one
# subsystem's C (lib/ by default) through a language's Guru pair and back, and builds tinyconfig both ways.
# It takes tens of minutes and a few GB; it is never part of the gate. Needs make, gcc, flex, bison, bc, libelf.
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
set -uo pipefail
cd "$(dirname "$0")/../.."; R="$PWD"; B="$R/.build"; TAG="${LINUX_TAG:-v6.6}"; SUB="${LINUX_SUBDIR:-lib}"
export ROMENAGRI="$B/chintamani/Romenagri"; CELL="${1:-$B/chintamani/Hindawi/guru}"
[ -d "$B/linux-$TAG" ] || { mkdir -p "$B" && curl -sL "https://codeload.github.com/torvalds/linux/tar.gz/refs/tags/$TAG" | tar -xz -C "$B" && mv "$B/linux-${TAG#v}" "$B/linux-$TAG"; }
for t in orig native; do rm -rf "$B/lx-$t"; cp -a "$B/linux-$TAG" "$B/lx-$t"; done
python3 lang/hindawi/tests/cells/cells.py tree --cell "$CELL" --src "$B/lx-native/$SUB"
for t in orig native; do
  (cd "$B/lx-$t" && make -s tinyconfig >/dev/null && make -s -j"$(nproc)" vmlinux > build.log 2>&1) \
    && echo "linux $t: vmlinux built" || echo "linux $t: BUILD FAILED (see $B/lx-$t/build.log)"
done
