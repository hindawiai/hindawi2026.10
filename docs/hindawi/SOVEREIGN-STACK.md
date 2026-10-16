# Where Hindawi sits in a sovereign stack

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

A sovereign stack is the ability of a language community to go from its own language, through programming,
mathematics, AI and high-performance computing, into operating systems, firmware, embedded and medical devices,
robotics, semiconductors and industrial production, and back through data, while keeping control of identity,
provenance, security and standards. Hindawi is the gateway into it, not the stack itself: it lets every layer be
programmed in the community's own language, and keeps its names debuggable down to firmware through Romenagri.

What this repository exercises today, each a script that passes or fails by execution:

| Layer | Check |
|---|---|
| Language and paradigms | `tests/fundamental.py`: the nine Chintamani shailis, forward and reverse |
| Compiler and name ABI | F5: a native name to the ELF symbol and back through Romenagri |
| Projects and libraries | F4: a multi-file project ingested, compiled with gcc's flags, and reversed |
| Firmware | `scripts/upstream/seabios.sh`: SeaBIOS built and booted under qemu-system-x86_64 |
| Silicon, Shakti class | `scripts/upstream/riscv.sh`: a Hindi program on RV64IMAC under qemu-system-riscv64 |
| Kernel | `scripts/upstream/linux.sh`: the Linux kernel through a language, tinyconfig |

Education maps onto this without carrying any syllabus text: each official syllabus (GATE and the school and
university boards) is fetched from its own URL at run time and matched against our standard syllabus, as
zistgah/rahnuma does.
