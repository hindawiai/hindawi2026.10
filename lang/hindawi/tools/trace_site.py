#!/usr/bin/env python3
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""trace_site.py: write docs/trace/data.js, the data of the explainer site "Can a language survive the whole computing
stack?" (docs/trace/index.html). Everything shown as computed by Hindawi is computed here, by the real pipeline, when
this runs; everything else the page computes in the reader's browser. Run after the toolchain is built:
  python3 lang/hindawi/tools/trace_site.py
"""
import json, subprocess, sys, tempfile, time, unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
R = HERE.parents[2]
sys.path.insert(0, str(HERE))
import hindawi_chain as hc   # noqa: E402

SEGMENTS = {"Devanagari": (0x0900, 0x097F), "Bengali": (0x0980, 0x09FF), "Gurmukhi": (0x0A00, 0x0A7F),
            "Gujarati": (0x0A80, 0x0AFF), "Odia": (0x0B00, 0x0B7F), "Tamil": (0x0B80, 0x0BFF), "Telugu": (0x0C00, 0x0C7F),
            "Kannada": (0x0C80, 0x0CFF), "Malayalam": (0x0D00, 0x0D7F), "Sinhala": (0x0D80, 0x0DFF), "Thai": (0x0E00, 0x0E7F),
            "Lao": (0x0E80, 0x0EFF), "Tibetan": (0x0F00, 0x0FFF), "Arabic": (0x0600, 0x06FF), "Hebrew": (0x0590, 0x05FF),
            "Syriac": (0x0700, 0x074F), "Greek": (0x0370, 0x03FF), "Cyrillic": (0x0400, 0x04FF), "Armenian": (0x0530, 0x058F),
            "Georgian": (0x10A0, 0x10FF), "Ethiopic": (0x1200, 0x137F), "Hangul Jamo": (0x1100, 0x11FF),
            "Hiragana": (0x3040, 0x309F), "Katakana": (0x30A0, 0x30FF), "Khmer": (0x1780, 0x17FF), "Myanmar": (0x1000, 0x109F)}
GREETINGS = {"hindi": "नमस्ते", "sanskrit": "नमः", "marathi": "नमस्कार", "nepali": "नमस्कार", "bengali": "নমস্কার",
             "punjabi": "ਨਮਸਤੇ", "gujarati": "નમસ્તે", "odia": "ନମସ୍କାର", "tamil": "வணக்கம்", "telugu": "నమస్తే",
             "kannada": "ನಮಸ್ಕಾರ", "malayalam": "നമസ്കാരം", "urdu": "سلام", "sindhi": "سلام", "pashto": "سلام", "persian": "سلام"}
PROGRAM = '#include <stdio.h>\nint main(void) {\n    int total = 0;\n    for (int i = 1; i <= 10; i++)\n        total += i;\n    printf("%d\\n", total);\n    return 0;\n}\n'

# What exists in this repository for each layer of the stack (AyeKnow states: defined, implemented, executed, measured,
# verified, reproduced, open). Each says what was run, by what, and where its record is; nothing beyond that.
LAYERS = [
 (15, "Human languages", "verified", "The foundation check finds 48 of 76 languages ready to compile and 8 with every host keyword bound (docs/hindawi/data/readiness.json)."),
 (14, "Hindawi language layer", "verified", "All 113 GATE C programs compile from Urdu and Tamil and print what the English originals print; Hindi 111 of 113 (docs/hindawi/data/gate-results.json)."),
 (13, "IR, lowering and transduction", "verified", "Script filter, Romenagri and each language's transducer, run on every compile; a whole tree lowered at once gives, file for file, what each file gives alone (xv6 in Urdu, Tamil, Hindi). PANIR, the semantic IR, is defined as a proposal only (docs/hindawi/PANIR.md)."),
 (12, "Compilers and toolchains", "executed", "GCC compiles the lowered code for the host and, as a cross compiler, for RISC-V. TinyCC, GCC and LLVM built from a language are in parashakti.sh's manifest and have not been run."),
 (11, "Runtime, libraries and ABI", "verified", "xv6's user library, built from Urdu, Tamil and Hindi, runs its shell. The WebAssembly runtime stage (wasm3) has not yet passed."),
 (10, "Operating systems", "verified", "xv6 built from Urdu, Tamil and Hindi boots on QEMU's RISC-V machine and its shell runs echo and ls (parashakti.sh). MINIX 3 and Linux are in the manifest and have not been run."),
 (9, "Firmware and boot chain", "executed", "The SHAKTI bare-metal start code runs on QEMU (its assembly is kept in host notation). SeaBIOS is in the manifest and has not been run."),
 (8, "ISA", "verified", "RISC-V, in emulation: QEMU's SHAKTI C-class and virt machines run the programs built from Urdu, Tamil and Hindi. No physical SHAKTI silicon has been used."),
 (7, "Microarchitecture", "open", "Nothing in this repository yet."),
 (6, "RTL", "open", "Nothing in this repository yet."),
 (5, "HDL", "open", "Nothing in this repository yet."),
 (4, "Synthesis, place and route, netlist", "open", "Nothing in this repository yet."),
 (3, "FPGA or ASIC (Spartan-3A)", "open", "Nothing in this repository yet."),
 (2, "SoC, board and peripherals", "implemented", "Robot sketches for Arduino UNO and ESP32, in English and six languages, pass a C++ syntax check against stand-in headers; not yet compiled against the real cores or run on a robot (robot_coding/)."),
 (1, "Physical world", "open", "No physical measurement has been recorded yet."),
]
POSTERS = [
 ("qwantum-tum-tum", "Qwan-tum Tum Tum: from horse carts to Planck length",
  "The idea: continuous reality, sampled, quantised into discrete and multi-level states, encoded, and read as symbols.",
  [("The ladder from a continuous variable to symbols", "defined", "This site's Qwan-tum section samples, quantises (2 to 9 levels), and encodes a signal in your browser."),
   ("Variable-length encoding, Gray coding and multi-level quantisation on a Spartan-3A, seen on an oscilloscope", "open", "Not yet built or measured."),
   ("Average code length 17.0 bits fixed-width against 4.8 adaptive, for a text corpus", "open", "An illustration; the corpus and the measurement are not in this repository yet."),
   ("Wavelengths up to the Planck scale", "defined", "A conceptual endpoint of the same journey, not a measurement.")]),
 ("parashakti", "Parashakti: a totally sovereign computing stack, from physical bits to human language",
  "The stack Hindawi builds on, from the physical world to the languages people write in, orchestrated by parashakti.sh.",
  [("SHAKTI bare metal (RISC-V) proved through parashakti.sh", "verified", "Built from Urdu, Tamil and Hindi; printed \"Parashakti: Hindawi on SHAKTI, sum 1..10 = 55\" on QEMU's SHAKTI C-class machine."),
   ("xv6 proved through parashakti.sh", "verified", "Built from Urdu, Tamil and Hindi; booted on QEMU's RISC-V machine; its shell ran echo and ls. The poster's console text is an illustration."),
   ("WebAssembly through a localised runtime", "open", "The wasm3 stage has not yet passed; the console panel is an illustration."),
   ("SeaBIOS (Hindawi) OK", "open", "In the manifest, not yet run; the console panel is an illustration."),
   ("TinyCC, MINIX, Linux, GCC, LLVM", "open", "In the manifest, not yet run."),
   ("Layers 1 to 4: physical world, silicon or FPGA, HDL, RTL", "open", "Nothing in this repository yet.")]),
 ("ayeknow-knowledge-with-evidence", "AyeKnow: knowledge with evidence",
  "The method: every claim carries its trace, from defined to reproduced, and what is unknown stays explicitly open.",
  [("The seven states and the five principles", "defined", "This site marks every layer and every poster claim with its state."),
   ("Parashakti orchestrates the stack: pinned source, configure, ingest, lower, build, run, verify, record", "implemented", "parashakti.sh does these steps; see the Parashakti poster's claims for what has been run.")]),
 ("ayeknow-from-claims-to-evidence", "AyeKnow: from claims to evidence",
  "Not \"we know\": show the trace. The evidence chain, the Hindawi foundation and the projects Parashakti runs.",
  [("Hindawi foundation: script filter, Romenagri, language transducer, BURP ingestion, readiness gate, lowering", "verified", "Each step runs in this repository; the readiness report is docs/hindawi/data/readiness.json."),
   ("Proven through parashakti.sh: SHAKTI, xv6, WebAssembly, SeaBIOS, TinyCC, MINIX, Linux, GCC, LLVM", "open", "SHAKTI and xv6 are verified; the others have not been run yet.")]),
 ("ayeknow-stack-detail", "AyeKnow: the totally sovereign stack, from HDL to human language (detail)",
  "The fifteen layers in detail, with the projects and the evidence that REPORT.md records.",
  [("Fifteen layers from the physical world to human languages", "defined", "The stack section of this site gives each layer's evidence state.")]),
]


def ranges():
    """Consecutive code points sharing a script word, for every assigned character up to U+2FFFF."""
    out, cur = [], None
    for cp in range(0x20, 0x30000):
        name = unicodedata.name(chr(cp), "")
        if not name:
            label = None
        elif name.startswith("CJK"):
            label = "CJK (Han)"
        elif unicodedata.category(chr(cp))[0] in "LMN":
            label = name.split(" ")[0].title()
        else:
            label = "Common"
        if cur and cur[2] == label and cur[1] == cp - 1:
            cur[1] = cp
        else:
            if cur and cur[2]:
                out.append(cur)
            cur = [cp, cp, label]
    if cur and cur[2]:
        out.append(cur)
    return out


def segments():
    seg = {}
    for name, (lo, hi) in SEGMENTS.items():
        chars = [chr(c) for c in range(lo, hi + 1) if unicodedata.name(chr(c), "") and unicodedata.category(chr(c))[0] in "LMN"]
        seg[name] = "".join(chars)
    return seg


def names(text):
    return [[f"U+{ord(c):04X}", unicodedata.name(c, "(unnamed)")] for c in text]


def native_program(lang):
    """The English program put into the language by BURP, as a learner would receive it."""
    with tempfile.TemporaryDirectory() as d:
        (Path(d) / "src").mkdir(); (Path(d) / "src/sum.c").write_text(PROGRAM)
        subprocess.run([sys.executable, str(R / "lang/hindawi/burp/burp.py"), "ingest", f"{d}/src", "--langs", lang,
                        "--out", f"{d}/n", "--translators", "glossary"], capture_output=True, check=True)
        return (Path(d) / "n" / lang / "sum.c").read_text(encoding="utf-8")


def main():
    romenagri = {}
    for lang, word in GREETINGS.items():
        try:
            raw = hc.sh(f"{hc.script_filter(lang)}{hc.ROMENAGRI_CHAIN}", hc.script_filters.normalize(lang, word).encode()).decode().strip()
            romenagri[lang] = {"word": word, "romenagri": raw, "c": hc.forms([word], lang)[word], "code_points": names(word)}
        except SystemExit:
            pass
    stages = {}
    for lang in ("urdu", "hindi", "tamil", "telugu"):
        src = native_program(lang)
        stages[lang] = [[n, t] for n, t in hc.stages(src, lang)]
    ayecode = json.loads((R / "lang/hindawi/data/ayecode_alphabets.json").read_text(encoding="utf-8"))
    data = {"built": time.strftime("%Y-%m-%d", time.gmtime()), "ranges": ranges(), "segments": segments(), "ayecode": ayecode,
            "romenagri": romenagri, "stages": stages, "english_program": PROGRAM,
            "layers": [{"n": n, "name": a, "state": s, "evidence": e} for n, a, s, e in LAYERS],
            "posters": [{"file": f, "title": t, "about": a, "claims": [{"claim": c, "state": s, "evidence": e} for c, s, e in cl]}
                        for f, t, a, cl in POSTERS]}
    out = R / "docs/trace/data.js"
    out.write_text("// Computed by lang/hindawi/tools/trace_site.py with the real pipeline. Do not edit by hand.\n"
                   "window.TRACE = " + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
    print(f"trace_site: {out.relative_to(R)}: {len(data['ranges'])} script ranges, {len(romenagri)} Romenagri examples, "
          f"{len(stages)} compiled examples, {out.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
