# Audit: Hindawi 2026.10, Parashakti and the work around them

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. State as of 19 October 2026 (Navami). Evidence states follow
AyeKnow: defined, implemented, executed, verified, open. Nothing is called done that he has not accepted.

## 1. Released and minted

| What | Where | Identifier |
|---|---|---|
| Hindawi 2026.10, versions 2026.10.3 to 2026.10.7 | hindawiai/hindawi2026.10 | concept 10.5281/zenodo.23424410; 2026.10.3 23437358, 2026.10.4 23446805, 2026.10.5 23450594, 2026.10.6 23469266, 2026.10.7 recorded in its README |
| UISA, the living research record | pvjournal/uisa, https://pvjournal.github.io/uisa/ | 10.5281/zenodo.23471398 |
| Master contract clauses C38 (the intention is the author's; an unverified claim carries a disclaimer) and C39 (gates guard the release only) | zistgah/governance CONTRACT.md | pushed 19 Oct 2026 |
| Trademark notices, central texts in one place | zistgah/zistgah.github.io/legal and the repositories the run reached | about a third of the estate (his count) |

## 2. Done in the repository, with its evidence

| Area | State | Evidence |
|---|---|---|
| Nine complete languages (Dari, Pashto, Urdu, Punjabi in both scripts, Sindhi, Telugu, Kannada, Sanskrit) | verified | 113 of 113 GATE C programs and the Python program compile from each and print what English prints; 117 of 117 files reversed byte for byte |
| Tamil, Hindi and others on the same path | verified | Tamil 113 of 113; Hindi 111 of 113 (the original character-literal rule, T-10) |
| The foundation: one normalisation, whole-tree lowering, readiness and round trip from the data | verified | 48 of 76 languages ready to compile; lowering a tree at once equals file by file (xv6, three languages); 117 bindings kept in host form by the round trip |
| Originals byte for byte | verified | 96 files restored in 2026.10.6 and reported by `hindawi test` |
| Parashakti | verified for SHAKTI bare metal and xv6 in Urdu, Tamil and Hindi on QEMU | a timed sanity check now runs first; nothing is installed unless asked |
| Explainer site, inside-the-machine page | verified | the APCISR engine is the original C in WebAssembly, identical to the native build on 1,497 inputs; pages driven headless without errors |
| Practice notebooks, ten languages, Colab links | executed headless | Build, Run, To C, From English and Python checked in Urdu and Hindi; not yet recorded in Colab itself |
| Robots: sketches, phone control page, instructions | implemented | syntax checked in English and six languages after lowering; not yet recorded on a built robot |
| Standards | rework required | drafts exist for nine languages; his review asks for complete language definitions, global bodies, semantics through PANIR |
| PANIR | defined | a proposal (docs/hindawi/PANIR.md) |
| Products, register, work packages | implemented | PRODUCTS.md; TASKS.md and work-packages/ |

## 3. Pending, in the order that converges fastest

1. Physical robot runs recorded (he is building them now); the sketches compiled against the real AVR and ESP32 cores.
2. Parashakti on his laptop: `--check`, then the light projects; then WebAssembly, SeaBIOS and TinyCC passing; then MINIX,
   Linux, GCC and LLVM (hours and gigabytes each; disk is the limit).
3. Trademark notices for the rest of the estate, from a complete inventory (`gh api` with pagination, not web pages).
4. Standards rebuilt as complete language definitions (character set, literals, types, grammar, semantics through PANIR),
   for the global standards bodies.
5. Scripts without filters (Cyrillic, Han, Hangul, Kana, Thai, Lao, Khmer, Myanmar, Tibetan, Sinhala, Javanese and others:
   24 languages); Hebrew, Syriac, Phoenician and Aramaic given their own scripts.
6. Hindi completed (LOGO, Python, C++ keywords) and its character-literal rule fixed in front of the original rules.
7. The hardware layers for Parashakti and Qwan-tum Tum Tum: RTL, simulation, synthesis, FPGA (Spartan-3A), a measured signal.
8. Several languages in one program (a per-file language tag) and configuration management of a multilingual codebase.
9. Web-first and phone guides; the central notice script adopted by the web pages; cross-repository links.
10. The economic analysis of what earlier focus on Hindawi would have earned; the APCISR paper on the site when he shares it.
11. UISA's research package (code, tests, benchmark) added so its gate re-runs it.
12. Rahnuma updated and checked against the original architecture; the software factory with the student networks;
    posters to Zenodo (lawh first); VARZISH and the cyclers; the PANINI family architecture note; estate deduplication.
13. Open topic, his: material that lets a doubtful reader check each claim before dismissing it (expected results and
    checks are now on the robot and machine pages; the rest is open).

## 4. How the other projects relate

| Project | Relation to this work | State |
|---|---|---|
| hindawiai/chintamani (the Telugu version of Hindawi) | carries the original transducers and APCISR; reused, never changed | live |
| hindawiai/sanskrit (Pushkalāvatī) | Sanskrit's bindings | minted, 10.5281/zenodo.23382730 |
| zistgah/tajziya | the classical-language front end in the PANINI picture | minted, 0.7.0 |
| zistgah/panini, humanesque, paniniq, paniniphy, paninib | the PANINI family that PANIR would serve | per their own records |
| misty-doi | mints every DOI above | live |
| zistgah/governance | the master contract, C1 to C39 | live |
| ayecnse/sims, ayecnse/ayeam-robot, icansee.life | the robots' simulator and control interface | live |
| ayehandsum/ayehandsum (AyeCode) | its alphabets in the explainer site | live |
| pvjournal/uisa | the inverse problem to Qwan-tum's representation path | minted |

## 5. Order of runs to converge by Navami

1. `bash update_hindawi2026.sh --all` (2026.10.8: the robot page and phone control, the machine page's composition view and
   ideas, the files and AI section, Start here, this audit).
2. `bash parashakti.sh --check`, then `bash parashakti.sh`.
3. Build Stage 1, upload, the first test, and open an issue with the result.
