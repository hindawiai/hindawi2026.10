#!/usr/bin/env bash
# install.sh: let every Arduino core on this machine build sketches written in a human language, through Hindawi.
# It adds a sketch pre-build hook to each core's platform.local.txt, so it works the same for AVR, ESP32, RP2040, STM32
# and any other core: the core's own compiler builds what Hindawi hands it. Arduino IDE 2 and arduino-cli both read it.
#   bash ide/arduino/install.sh --lang hindi      install, or switch the language
#   bash ide/arduino/install.sh --remove          take it out again
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
set -euo pipefail
root="$(cd "$(dirname "$0")/../.." && pwd)"; lang=hindi; remove=0
while [ $# -gt 0 ]; do case "$1" in --lang) lang="$2"; shift ;; --remove) remove=1 ;; *) echo "install: unknown option $1"; exit 3 ;; esac; shift; done
cores=()
for base in "${ARDUINO_DIRECTORIES_DATA:-$HOME/.arduino15}/packages" "$HOME/Library/Arduino15/packages" "$HOME/Arduino/hardware"; do
  [ -d "$base" ] || continue
  while IFS= read -r p; do cores+=("$(dirname "$p")"); done < <(find "$base" -name platform.txt -path '*hardware*' 2>/dev/null)
done
[ "${#cores[@]}" -gt 0 ] || { echo "install: no Arduino core found; install a board package in the Arduino IDE first"; exit 1; }
for d in "${cores[@]}"; do
  f="$d/platform.local.txt"
  [ -f "$f" ] && sed -i '/^## hindawi begin/,/^## hindawi end/d' "$f"
  if [ "$remove" = 1 ]; then echo "hindawi: removed from $d"; continue; fi
  { echo "## hindawi begin: sketches in any language, through Hindawi (hindawi2026.10, ide/arduino/install.sh)"
    echo "hindawi.lang=$lang"
    echo "hindawi.root=$root"
    echo 'recipe.hooks.sketch.prebuild.90.pattern=bash "{hindawi.root}/ide/arduino/transduce.sh" "{build.path}/sketch" "{hindawi.lang}"'
    echo "## hindawi end"; } >> "$f"
  echo "hindawi: $d now builds $lang sketches"
done
echo "Restart the Arduino IDE. Romenagri must be built once: (cd $root && bash scripts/fetch.sh && bash scripts/build.sh)"
