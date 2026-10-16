#!/usr/bin/env bash
# fetch.sh: the pinned upstreams this kit builds against, into .build/ inside the kit. Nothing is vendored.
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
set -euo pipefail
cd "$(dirname "$0")/.."; mkdir -p .build; B="$PWD/.build"
CHINTAMANI=3ad87785a75dc2b18438a8b068807103cb920c81      # hindawiai/chintamani: Hindawi and Romenagri, the oracle
SEABIOS=rel-1.16.3                                        # the coreboot/seabios mirror on GitHub, commit a6ed6b7
if [ ! -d "$B/chintamani/.git" ]; then
  git init -q "$B/chintamani"
  git -C "$B/chintamani" fetch -q --depth 1 https://github.com/hindawiai/chintamani.git "$CHINTAMANI"
  git -C "$B/chintamani" checkout -q FETCH_HEAD
fi
[ "$(git -C "$B/chintamani" rev-parse HEAD)" = "$CHINTAMANI" ] || { echo "fetch: chintamani is not at its pin"; exit 1; }
if [ ! -d "$B/seabios/.git" ]; then
  git clone -q --depth 1 --branch "$SEABIOS" https://github.com/coreboot/seabios.git "$B/seabios"
fi
echo "fetch: chintamani $(git -C "$B/chintamani" rev-parse --short HEAD), seabios $(git -C "$B/seabios" describe --tags 2>/dev/null || git -C "$B/seabios" rev-parse --short HEAD)"
