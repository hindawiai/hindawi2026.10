#!/usr/bin/env bash
# release_tools.sh: build Hindawi's tools once and publish them on GitHub as the release "tools": one common package and
# one package per language, which the notebooks fetch in seconds instead of compiling.
#   bash scripts/release_tools.sh             build inside Ubuntu 22.04 (Colab's base, so the binaries run there), then publish
#   bash scripts/release_tools.sh --no-docker build here instead (the binaries then need this machine's C library)
# Needs: gh, logged in to an account that can write to hindawiai/hindawi2026.10; Docker for the Ubuntu 22.04 build.
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
set -uo pipefail
cd "$(dirname "$0")/.."
REPO=hindawiai/hindawi2026.10; TAG=tools; mkdir -p dist
build() {
  bash scripts/build.sh >/dev/null 2>&1 || { echo "build.sh failed"; return 1; }
  export PATH="$PWD/.build/chintamani/Romenagri:$PATH" ROMENAGRI="$PWD/.build/chintamani/Romenagri"
  python3 - <<'PY'
import sys, pathlib; sys.path.insert(0, "lang/hindawi/tools"); import hindawi_chain as hc
import json
langs = sorted(k for k, v in json.loads(open("docs/hindawi/data/readiness.json", encoding="utf-8").read())["languages"].items() if v.get("ready_to_compile"))
for i, lang in enumerate(langs, 1):
    for fw in ("h2c", "h2cpp", "h2py", "h2java", "h2b", "h2l", "h2yacc", "h2asm"):
        try:
            hc.fwd_lexer(lang, fw)
        except BaseException as e:
            print(f"   {lang} {fw}: not built ({str(e)[:60]})")
    print(f"   {i} of {len(langs)}: {lang}", flush=True)
PY
  tar -czf dist/hindawi-tools-common-linux-x86_64.tar.gz bin lang samples docs/hindawi/samples scripts/colab_env.sh scripts/build.sh scripts/parashakti.sh \
      .build/chintamani .build/filters 2>/dev/null
  for d in .build/cells/*/; do l=$(basename "$d"); tar -czf "dist/hindawi-tools-$l-linux-x86_64.tar.gz" ".build/cells/$l"; done
  ls dist | wc -l | xargs echo "   packages:"
}
if [ "${1:-}" = "--inside" ]; then build; exit $?; fi
if [ "${1:-}" != "--no-docker" ] && command -v docker >/dev/null; then
  echo "building inside Ubuntu 22.04 ..."
  docker run --rm -v "$PWD":/w -w /w ubuntu:22.04 bash -c 'export DEBIAN_FRONTEND=noninteractive; apt-get update -qq && apt-get install -y -qq gawk flex bison gcc make python3 git ca-certificates >/dev/null && git config --global --add safe.directory /w && bash scripts/release_tools.sh --inside' || exit 1
else
  build || exit 1
fi
gh release view "$TAG" -R "$REPO" >/dev/null 2>&1 || gh release create "$TAG" -R "$REPO" --title "Hindawi tools (prebuilt)" \
  --notes "Prebuilt tools for the notebooks and the terminal: hin, hindawi, hindawicc, parashakti, Romenagri and each language's transducers. Built on Ubuntu 22.04." || exit 1
gh release upload "$TAG" -R "$REPO" dist/*.tar.gz --clobber && echo "published: https://github.com/$REPO/releases/tag/$TAG"
