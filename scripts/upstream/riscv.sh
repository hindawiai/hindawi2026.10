#!/usr/bin/env bash
# riscv.sh: a Shakti-class bootstrap check. A native program goes through hindawicc's chain to C, is compiled for
# RV64IMAC bare metal with picolibc, and runs on system QEMU's virt machine. Pass or fail, it reports.
# Needs riscv64-unknown-elf-gcc, picolibc-riscv64-unknown-elf and qemu-system-riscv64.
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
set -uo pipefail
cd "$(dirname "$0")/../.."; B="$PWD/.build"; export ROMENAGRI="$B/chintamani/Romenagri" PATH="$B/chintamani/Romenagri:$PATH"
w="$(mktemp -d)"; trap 'rm -rf "$w"' EXIT
printf '#समावेश <मानकपन.स>\nपूर्णांक मुख्य(व्योम)\nअणु\n  पूर्णांक क = 6, ख = 7;\n  म_लिखो("rv64 %%प\\न", क * ख);\n  वापस 0;\nपूर्ण\n' > "$w/p.uhin"
fixuninum < "$w/p.uhin" | iconv -f utf-8 -t utf-16 | uni2acii | acii2cf | acii2uni | iconv -f UTF-16 -t UTF-8 | "$B/chintamani/Hindawi/guru/h2c" > "$w/p.c"
sed -i 's/\\न/\\n/g; s/\%भ/\%f/g; s/\%प/\%d/g;' "$w/p.c"
riscv64-unknown-elf-gcc --specs=picolibc.specs --oslib=semihost -march=rv64imac_zicsr -mabi=lp64 -mcmodel=medany -g \
  -Wl,--defsym=__flash=0x80000000 -Wl,--defsym=__flash_size=0x400000 -Wl,--defsym=__ram=0x80400000 -Wl,--defsym=__ram_size=0x400000 \
  -o "$w/p.elf" "$w/p.c" || { echo "riscv: FAIL, did not compile"; exit 1; }
timeout 10 qemu-system-riscv64 -machine virt -bios none -kernel "$w/p.elf" -nographic -semihosting-config enable=on,target=native \
  < /dev/null > "$w/run.out" 2>&1
grep -q "^rv64 42" "$w/run.out" && echo "riscv: PASS, the Hindi program ran on RV64IMAC under qemu-system-riscv64" \
  || echo "riscv: FAIL ($(head -c 80 "$w/run.out"))"
