# Products

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

Each product says who it is for, how they get it, what is shown to work today (AyeKnow states), and what stands between
it and a release. A product is released when every line of its release gap is closed; until then it is offered as it
is, with its states shown.

## Hindawi Practice: programming in your language on a phone

- **For** students and teachers whose computer is a phone.
- **Get it** in a browser, nothing to install: open a notebook in Google Colab and run its first cell.
  [Urdu](https://colab.research.google.com/github/hindawiai/hindawi2026.10/blob/main/notebooks/practice/hindawi_urdu.ipynb),
  [Hindi](https://colab.research.google.com/github/hindawiai/hindawi2026.10/blob/main/notebooks/practice/hindawi_hindi.ipynb),
  [Punjabi](https://colab.research.google.com/github/hindawiai/hindawi2026.10/blob/main/notebooks/practice/hindawi_punjabi.ipynb),
  [Punjabi Shahmukhi](https://colab.research.google.com/github/hindawiai/hindawi2026.10/blob/main/notebooks/practice/hindawi_punjabi_shahmukhi.ipynb),
  [Sindhi](https://colab.research.google.com/github/hindawiai/hindawi2026.10/blob/main/notebooks/practice/hindawi_sindhi.ipynb),
  [Telugu](https://colab.research.google.com/github/hindawiai/hindawi2026.10/blob/main/notebooks/practice/hindawi_telugu.ipynb),
  [Kannada](https://colab.research.google.com/github/hindawiai/hindawi2026.10/blob/main/notebooks/practice/hindawi_kannada.ipynb),
  [Sanskrit](https://colab.research.google.com/github/hindawiai/hindawi2026.10/blob/main/notebooks/practice/hindawi_sanskrit.ipynb),
  [Dari](https://colab.research.google.com/github/hindawiai/hindawi2026.10/blob/main/notebooks/practice/hindawi_dari.ipynb),
  [Pashto](https://colab.research.google.com/github/hindawiai/hindawi2026.10/blob/main/notebooks/practice/hindawi_pashto.ipynb).
- **Shown to work**: verified headless in Urdu and Hindi (Build, Run, To C, From English, the Python path).
- **Release gap**: a recorded run in Colab itself; the Stages panel seen in a live notebook; a phone walk-through
  with screenshots; a Bluetooth keyboard and screen guide for phones.

## Hindawi CLI: the compiler and tools on a laptop

- **For** engineers, colleges and labs on Ubuntu.
- **Get it**: `git clone https://github.com/hindawiai/hindawi2026.10 && cd hindawi2026.10 && bash install.sh`, then
  `hindawi verify` and `hindawi test`.
- **Shown to work**: 113 GATE programs compile from the complete languages and print what English prints; the local
  harness (TESTING.md).
- **Release gap**: prebuilt toolchain binaries so no build is needed; a Debian package and a container image; release
  assets with checksums on each tagged version.

## Hindawi Robots: the classroom robot kit

- **For** schools: Arduino UNO first, then ESP32; the basic robot meant to cost under 1000 rupees.
- **Get it**: `robot_coding/` (README.md, the sketches in English and six languages).
- **Shown to work**: the sketches pass a C++ syntax check against stand-in headers, also after lowering.
- **Release gap**: compiled against the real AVR and ESP32 cores; run on a built robot; the bill of materials with
  current prices; the simulator and the robot driven by the same commands, recorded.

## Parashakti: the sovereign stack, proved on QEMU

- **For** systems engineers, researchers and institutions evaluating a sovereign stack.
- **Get it**: `bash scripts/parashakti.sh --list`, then `--stage` and `--langs`.
- **Shown to work**: SHAKTI bare metal and xv6, built from Urdu, Tamil and Hindi, verified on QEMU.
- **Release gap**: the WebAssembly, SeaBIOS and TinyCC stages passing; MINIX, Linux, GCC and LLVM run; the hardware
  layers (RTL to the Spartan-3A and a measured signal).

## Trace: can a language survive the whole computing stack?

- **For** anyone asking what happens to a character after Unicode, in any script.
- **Get it**: `docs/trace/` on the repository's site.
- **Shown to work**: driven headless with its real data: no errors, the 7-bit and AyeCode round trips verified.
- **Release gap**: checked on phones of several sizes; translated into the languages it explains.

## UISA: a living research record

- **For** researchers in information theory, signal processing and steganalysis.
- **Get it**: pvjournal/uisa, minted on Zenodo when seeded.
- **Shown to work**: the record is deposited as authored; its numbers are as stated in the record.
- **Release gap**: the research package (code, tests, benchmark JSON, figures) added, so the gate re-executes it.
