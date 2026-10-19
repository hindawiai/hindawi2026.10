# WP-T-33: Parashakti: the complete demonstrated sovereign stack on the SHAKTI processor, packaged with the ingestion and sovereign-stack tools: cross compilers, then a self-hosted compiler (GCC, or TinyCC as the least-cost path), nothing external; in Hindi, Sanskrit, Arabic, Farsi, Tamil, Telugu, Kannada, Kashmiri, Urdu, Punjabi and every language that compiles; run on his laptop, not here

Asked: 18 Oct 2026. Status: in progress.

What exists: parashakti.sh is parametric: a manifest of projects (SHAKTI bare metal, xv6, MINIX 3, Linux, GCC, LLVM, wasm3, SeaBIOS, TinyCC), each fetched, ingested, lowered as a whole tree and built with its own tools. Proved here: SHAKTI bare metal and xv6 in Urdu, Tamil and Hindi. MINIX, Linux, GCC and LLVM are written into the manifest and not yet run; they take hours and several gigabytes each.

Next step: his full run; then TinyCC self-hosting and the Linux stack.

Done when the change is merged with its tests, every covenant in TASKS.md still holds, and `hindawi test` passes.

Originator: Abhishek Choudhary, AyeAI. © 1993–2026 Abhishek Choudhary. All rights reserved. Whoever completes this package is credited for it in CREDITS.md; the originator's credit stays on everything derived from it.
