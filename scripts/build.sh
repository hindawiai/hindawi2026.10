#!/usr/bin/env bash
# build.sh: Romenagri and every Chintamani shaili, from the pinned source, the original way (their own Makefiles).
# This is the oracle every language cell is measured against.
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
set -euo pipefail
cd "$(dirname "$0")/.."; B="$PWD/.build/chintamani"
[ -d "$B" ] || bash scripts/fetch.sh
make -s -C "$B/Romenagri" >/dev/null
export PATH="$B/Romenagri:$PATH"
for s in guru shraeni yantra kritrima praatha soochee wyaaka shabda; do
  make -s -C "$B/Hindawi/$s" >/dev/null 2>&1 && printf 'build: %-9s ok\n' "$s" || { printf 'build: %-9s FAILED\n' "$s"; exit 1; }
done
