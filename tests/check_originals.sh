#!/usr/bin/env bash
# check_originals.sh: the original Hindawi files, the BUILD-0102 sources and the recorded source stages are byte for byte
# as received (ORIGINALS.sha256, taken from the history before any normalisation), and nothing has been added among
# them. Any change fails the build. Restore from the history; never edit them.
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
set -euo pipefail
cd "$(dirname "$0")/.."
n=$(grep -c . ORIGINALS.sha256)
sha256sum --quiet -c ORIGINALS.sha256 || { echo "originals: CHANGED (listed above)"; exit 1; }
extra=$(comm -13 <(cut -c67- ORIGINALS.sha256 | sort) <(git ls-files lang/hindawi/upstream/chintamani lang/suktam docs/source-stages | sort))
[ -z "$extra" ] || { echo "originals: files added among them:"; echo "$extra"; exit 1; }
echo "originals: all $n files byte for byte as received, none added"
