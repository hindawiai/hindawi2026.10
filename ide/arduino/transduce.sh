#!/usr/bin/env bash
# transduce.sh: the Arduino IDE's sketch pre-build hook. Every file the IDE is about to compile that holds native text
# is carried to C through Hindawi's compilation path (lang/hindawi/tools/hindawi_chain.py to-c), in place, in the
# build folder; the sketch the student wrote is never touched. platform.local.txt calls it as:
#   transduce.sh "{build.path}/sketch" LANGUAGE
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
set -uo pipefail
case "${1:-}" in [A-Za-z]:\\*|[A-Za-z]:/*) command -v wslpath >/dev/null && set -- "$(wslpath -u "$1")" "${@:2}" ;; esac   # a Windows IDE under WSL
dir="$1"; lang="${2:-hindi}"; root="$(cd "$(dirname "$0")/../.." && pwd)"
export ROMENAGRI="${ROMENAGRI:-$root/.build/chintamani/Romenagri}"
[ -x "$ROMENAGRI/uni2acii" ] || { echo "hindawi: Romenagri is not built; in $root run: bash scripts/fetch.sh && bash scripts/build.sh" >&2; exit 1; }
status=0
while IFS= read -r -d '' f; do
  LC_ALL=C grep -q $'[\x80-\xff]' "$f" || continue          # all ASCII: nothing native to carry
  if python3 "$root/lang/hindawi/tools/hindawi_chain.py" to-c --lang "$lang" < "$f" > "$f.hindawi"; then mv "$f.hindawi" "$f"
  else echo "hindawi: $(basename "$f") did not transduce from $lang" >&2; rm -f "$f.hindawi"; status=1; fi
done < <(find "$dir" -type f \( -name '*.cpp' -o -name '*.c' -o -name '*.h' -o -name '*.hpp' \) -print0)
exit $status
