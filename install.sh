#!/usr/bin/env bash
# install.sh: install Hindawi 2026.10 for this user (default ~/.local) or system-wide (--prefix /usr/local).
# It checks what Hindawi needs, builds Chintamani's toolchain from the pinned source the original way, puts the
# commands hindawi and hindawicc on PATH with their manual page, and proves the installation by compiling and running
# a GATE program from Urdu and from Telugu.
#   bash install.sh [--prefix DIR] [--no-build] [--uninstall]
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
PREFIX="${PREFIX:-$HOME/.local}"; BUILD=1; UNINSTALL=0
while [ $# -gt 0 ]; do
  case "$1" in
    --prefix) PREFIX="$2"; shift 2 ;;
    --no-build) BUILD=0; shift ;;
    --uninstall) UNINSTALL=1; shift ;;
    -h|--help) sed -n '2,7p' "$0"; exit 0 ;;
    *) echo "install.sh: unknown option $1" >&2; exit 2 ;;
  esac
done
BIN="$PREFIX/bin"; MAN="$PREFIX/share/man/man1"
if [ "$UNINSTALL" = 1 ]; then
  rm -f "$BIN/hindawi" "$BIN/hindawicc" "$MAN/hindawi.1"
  echo "install.sh: removed hindawi, hindawicc and the manual page from $PREFIX"; exit 0
fi
echo "== what Hindawi needs"
missing=""
for t in python3 gcc flex make iconv git; do
  if command -v "$t" >/dev/null 2>&1; then printf '  ok       %s\n' "$t"; else printf '  MISSING  %s\n' "$t"; missing="$missing $t"; fi
done
for t in g++ bison docker arduino-cli; do
  command -v "$t" >/dev/null 2>&1 && printf '  ok       %s\n' "$t" || printf '  absent   %s (optional)\n' "$t"
done
if [ -n "$missing" ]; then
  echo "install.sh: install these first:$missing"
  echo "  Debian or Ubuntu: sudo apt install python3 gcc g++ flex bison make libc-bin git"
  echo "  Fedora:           sudo dnf install python3 gcc gcc-c++ flex bison make glibc-common git"
  exit 1
fi
if [ "$BUILD" = 1 ]; then
  echo "== Chintamani's toolchain, from the pinned source (the first run fetches it from GitHub)"
  bash "$ROOT/scripts/build.sh"
fi
echo "== the commands"
mkdir -p "$BIN" "$MAN"
ln -sf "$ROOT/bin/hindawi" "$BIN/hindawi"
ln -sf "$ROOT/lang/hindawi/hindawicc" "$BIN/hindawicc"
cp "$ROOT/docs/man/hindawi.1" "$MAN/hindawi.1"
echo "  $BIN/hindawi -> $ROOT/bin/hindawi"
echo "  $BIN/hindawicc -> $ROOT/lang/hindawi/hindawicc"
echo "  $MAN/hindawi.1"
echo "== proof: a GATE program compiled from Urdu and from Telugu, run, and compared with English"
"$BIN/hindawi" doctor
w="$(mktemp -d)"
for lang in urdu telugu; do
  python3 "$ROOT/lang/hindawi/burp/burp.py" ingest "$ROOT/samples/gate/algorithms/sorting" --langs "$lang" --out "$w" >/dev/null
  ROMENAGRI="$ROOT/.build/chintamani/Romenagri" HINDAWI_LANG="$lang" HINDAWI_NATIVE_SOURCE=1 \
    HINDAWI_DICT="$w/$lang/.hindawi/dictionary.json" "$BIN/hindawicc" -O2 -o "$w/native" "$w/$lang/quick_sort.c"
  gcc -O2 -o "$w/english" "$ROOT/samples/gate/algorithms/sorting/quick_sort.c"
  if [ "$("$w/native")" = "$("$w/english")" ]; then echo "  $lang: quick_sort.c compiles from $lang and prints: $("$w/native")"
  else echo "  $lang: FAILED"; exit 1; fi
done
rm -rf "$w"
case ":$PATH:" in *":$BIN:"*) ;; *) echo "install.sh: add $BIN to PATH, for example: echo 'export PATH=\"$BIN:\$PATH\"' >> ~/.bashrc" ;; esac
echo "install.sh: installed. Start with: hindawi --help, man hindawi, and docs/hindawi/MANUAL.md"
