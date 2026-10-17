#!/usr/bin/env bash
# stack.sh: the sovereign stack, layer by layer, through Hindawi. From a processor described in VHDL, through the
# firmware, the kernel, the C library, binutils and the compiler, to libraries, every upstream is fetched at a pinned
# release, ingested by BURP into every language at once, measured for how much of it is localised (the target is
# 100%), reversed to prove nothing is lost, and, with --build, built through the compilation path. --bootstrap adds
# the T-diagram test: TinyCC, ingested into a language, built, then rebuilding itself from its own native source.
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
#
#   bash scripts/sovereign/stack.sh                      every layer, every language, measure and reverse
#   bash scripts/sovereign/stack.sh --langs hindi,urdu,punjabi_shahmukhi --only seabios,tinycc --build
#   bash scripts/sovereign/stack.sh --scripts brahmi      also render Devanagari ingestions in every Brahmi script
#   bash scripts/sovereign/stack.sh --full                whole trees where the default takes a subsystem
#   bash scripts/sovereign/stack.sh --bootstrap --langs hindi
#
# Run it from the repository root. Everything goes under .build/sovereign/. Each step is recorded in
# .build/sovereign/report.tsv as PASS, FAIL, UNJUDGED (a tool or network is missing) or SKIP, with its reason; a
# failing step never stops the run. Exit 0 when nothing failed, 1 otherwise. It needs git, python3, gcc and make;
# --build needs flex and the pinned Chintamani (scripts/fetch.sh and scripts/build.sh); GHDL checks the VHDL.
set -uo pipefail
cd "$(dirname "$0")/../.." || exit 3
R="$PWD"; W="$R/.build/sovereign"; mkdir -p "$W/src" "$W/out" "$W/logs"
LANGS=all; SCRIPTS=""; ONLY=""; BUILD=0; FULL=0; BOOT=0; JOBS="$(nproc 2>/dev/null || echo 2)"
while [ $# -gt 0 ]; do case "$1" in
  --langs) LANGS="$2"; shift ;; --scripts) SCRIPTS="$2"; shift ;; --only) ONLY="$2"; shift ;;
  --build) BUILD=1 ;; --full) FULL=1 ;; --bootstrap) BOOT=1 ;; --jobs) JOBS="$2"; shift ;;
  -h|--help) sed -n '2,20p' "$0"; exit 0 ;; *) echo "stack: unknown option $1"; exit 3 ;; esac; shift; done

REPORT="$W/report.tsv"; printf 'layer\tproject\tstep\tstatus\treason\n' > "$REPORT"
record() { printf '%s\t%s\t%s\t%s\t%s\n' "$1" "$2" "$3" "$4" "$5" >> "$REPORT"; printf '  %-8s %-12s %-10s %-9s %s\n' "$1" "$2" "$3" "$4" "$5"; }

# layer | project | repository on GitHub | pinned tag | subtree ingested by default ("." for all)
PROJECTS="L0-hw|neorv32|stnolting/neorv32|v1.10.6|rtl/core
L1-fw|seabios|coreboot/seabios|rel-1.16.3|src
L2-os|linux|torvalds/linux|v6.6|kernel/sched
L3-libc|musl|bminor/musl|v1.2.5|src/string
L4-tool|binutils|bminor/binutils-gdb|binutils-2_42|binutils
L4-tool|tinycc|TinyCC/tinycc|release_0_9_27|.
L4-tool|gcc|gcc-mirror/gcc|releases/gcc-13.2.0|gcc/c
L5-lib|zlib|madler/zlib|v1.3.1|.
L5-lib|cjson|DaveGamble/cJSON|v1.7.18|.
L5-lib|openblas|OpenMathLib/OpenBLAS|v0.3.28|interface"

have() { command -v "$1" >/dev/null 2>&1; }
for t in git python3 gcc make; do have "$t" || { echo "stack: $t is required"; exit 3; }; done
echo "Sovereign stack through Hindawi · languages: $LANGS · scripts: ${SCRIPTS:-own only} · build: $BUILD · bootstrap: $BOOT"
FAILED=0
while IFS='|' read -r layer name repo tag sub; do
  [ -n "$ONLY" ] && ! grep -qw "$name" <<<"${ONLY//,/ }" && continue
  [ "$FULL" = 1 ] && sub="."
  S="$W/src/$name"; O="$W/out/$name"; L="$W/logs/$name"
  # 1. fetch, shallow, at the pinned tag
  if [ ! -d "$S/.git" ]; then
    if git clone -q --depth 1 --branch "$tag" "https://github.com/$repo.git" "$S" > "$L.fetch.log" 2>&1; then
      record "$layer" "$name" fetch PASS "$repo $tag"
    else record "$layer" "$name" fetch UNJUDGED "clone failed: $(tail -1 "$L.fetch.log")"; continue; fi
  else record "$layer" "$name" fetch PASS "cached at $(git -C "$S" describe --tags 2>/dev/null || echo "$tag")"; fi
  [ -e "$S/$sub" ] || { record "$layer" "$name" ingest FAIL "no $sub in $tag"; FAILED=1; continue; }
  # 2. ingest into every language at once (and every requested script)
  extra=(); [ -n "$SCRIPTS" ] && extra=(--scripts "$SCRIPTS")
  if python3 lang/hindawi/burp/burp.py ingest "$S/$sub" --langs "$LANGS" --out "$O" --jobs "$JOBS" "${extra[@]}" \
      > "$L.ingest.log" 2>&1; then
    record "$layer" "$name" ingest PASS "$(grep -c '^burp:' "$L.ingest.log") ingestions"
  else record "$layer" "$name" ingest FAIL "$(tail -1 "$L.ingest.log")"; FAILED=1; continue; fi
  # 3. measure: how much is localised, per language and paradigm
  if python3 scripts/sovereign/measure.py "$S/$sub" "$O" --project "$name" --tsv "$L.measure.tsv" > "$L.measure.log" 2>&1; then
    full="$(awk -F'\t' '$4==100.0 && ($5==100.0 || $5=="None")' "$L.measure.tsv" | wc -l)"
    record "$layer" "$name" measure PASS "$full of $(wc -l < "$L.measure.tsv") ingestions fully localised (keywords and names)"
  else record "$layer" "$name" measure FAIL "$(tail -1 "$L.measure.log")"; FAILED=1; fi
  # 4. reverse every ingestion and compare with upstream byte for byte
  bad=0; n=0
  for f in "$O"/*/; do
    n=$((n+1)); b="$W/back/$name/$(basename "$f")"
    python3 lang/hindawi/burp/burp.py reverse "$f" --out "$b" >/dev/null 2>&1 && diff -rq "$S/$sub" "$b" -x .git >/dev/null 2>&1 || bad=$((bad+1))
  done
  [ "$bad" = 0 ] && record "$layer" "$name" reverse PASS "$n of $n back byte for byte" \
                 || { record "$layer" "$name" reverse FAIL "$bad of $n differ from upstream"; FAILED=1; }
  # 5. VHDL: the reversed tree must still analyse (GHDL); a native analysis needs the language's vhdl2h tables
  if [ "$name" = neorv32 ]; then
    if have ghdl; then
      b="$W/back/$name/$(ls "$O" | head -1)"
      (cd "$b" && ghdl -i --std=08 --work=neorv32 *.vhd >/dev/null 2>&1 && ghdl -m --std=08 --work=neorv32 neorv32_top >/dev/null 2>&1) \
        && record "$layer" "$name" vhdl PASS "reversed core analyses and elaborates with GHDL" \
        || record "$layer" "$name" vhdl FAIL "GHDL rejects the reversed core"
    else record "$layer" "$name" vhdl UNJUDGED "ghdl not installed"; fi
  fi
  # 6. build through the compilation path, language by language
  if [ "$BUILD" = 1 ] && [ "$name" != neorv32 ]; then
    for f in "$O"/*/; do
      lang="$(basename "$f")"; lang="${lang%@*}"
      if python3 lang/hindawi/tools/build_project.py "$f" --lang "$lang" --work "$W/build/$name/$(basename "$f")" \
          > "$L.build.$(basename "$f").log" 2>&1; then record "$layer" "$name" "build:$(basename "$f")" PASS "built"
      else record "$layer" "$name" "build:$(basename "$f")" FAIL "$(tail -1 "$L.build.$(basename "$f").log")"; FAILED=1; fi
    done
  fi
done <<< "$PROJECTS"

# 7. the T-diagram: TinyCC in a language builds itself from its own native source
if [ "$BOOT" = 1 ]; then
  T="$W/out/tinycc"
  for f in "$T"/*/; do
    lang="$(basename "$f")"; b1="$W/boot/$lang/stage1"; b2="$W/boot/$lang/stage2"
    if python3 lang/hindawi/tools/build_project.py "$f" --lang "${lang%@*}" --work "$b1" > "$W/logs/boot.$lang.log" 2>&1 \
       && [ -x "$b1/tcc" ] \
       && CC="$b1/tcc" python3 lang/hindawi/tools/build_project.py "$f" --lang "${lang%@*}" --work "$b2" >> "$W/logs/boot.$lang.log" 2>&1 \
       && [ -x "$b2/tcc" ]; then
      printf 'int main(void){return 42;}\n' > "$W/boot/$lang/t.c"
      "$b2/tcc" -run "$W/boot/$lang/t.c"; rc=$?
      [ "$rc" = 42 ] && record L4-tool tinycc "bootstrap:$lang" PASS "stage 2, built by the native stage 1, runs" \
                     || record L4-tool tinycc "bootstrap:$lang" FAIL "stage 2 returned $rc"
    else record L4-tool tinycc "bootstrap:$lang" FAIL "$(tail -1 "$W/logs/boot.$lang.log")"; FAILED=1; fi
  done
fi
echo; echo "report: $REPORT"; echo "per-language localisation: $W/logs/<project>.measure.tsv"
awk -F'\t' 'NR>1 {c[$4]++} END {for (s in c) printf "  %s %d\n", s, c[s]}' "$REPORT"
exit "$FAILED"
