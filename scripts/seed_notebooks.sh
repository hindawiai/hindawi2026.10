#!/usr/bin/env bash
# seed_notebooks.sh: write the practice notebooks (notebooks/practice/hindawi_<language>.ipynb) in the design of the
# Chintamani notebooks: a hidden one-cell installation, then for each shaili a program to edit in the language and hidden
# cells that run it and show its stages, then the same programs in English for reference.
#   bash scripts/seed_notebooks.sh [--langs urdu,telugu]
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
set -euo pipefail
cd "$(dirname "$0")/.."
LANGS="urdu,hindi,punjabi,punjabi_shahmukhi,sindhi,telugu,kannada,sanskrit,dari,pashto"
[ "${1:-}" = "--langs" ] && LANGS="$2"
export PATH="$PWD/.build/chintamani/Romenagri:$PATH" ROMENAGRI="$PWD/.build/chintamani/Romenagri"
python3 - "$LANGS" <<'PY'
import json, subprocess, sys, tempfile
from pathlib import Path
R = Path.cwd(); langs = sys.argv[1].split(",")
NATIVE = {"urdu": "اردو", "hindi": "हिन्दी", "punjabi": "ਪੰਜਾਬੀ", "punjabi_shahmukhi": "پنجابی", "sindhi": "سنڌي", "telugu": "తెలుగు",
          "kannada": "ಕನ್ನಡ", "sanskrit": "संस्कृतम्", "dari": "دری", "pashto": "پښتو"}
SHAILIS = [("C", "guru", "algorithms/searching/binary_search.c", None), ("C++", "shraeni", "paradigms/bst.cpp", None),
           ("Python", "soochee", "paradigms/binary_search.py", None), ("Java", "kritrima", "paradigms/Stack.java", None),
           ("BASIC", "praatha", "paradigms/primes.bas", None), ("Lex", "shabda", "shailis/wordcount.l", "one two three\\nfour five\\n"),
           ("Yacc", "wyaaka", "shailis/calculator.y", "2+3*4\\n10*10+1\\n"), ("Assembly", "yantra", "shailis/hello.s", None)]
INSTALL = """%%shell
#@title **Installation** (press ▶ once; about a minute) { vertical-output: true }
#@markdown Run this once before the other cells. It fetches Hindawi's prebuilt tools, so nothing has to be compiled,
#@markdown and puts the commands `hin`, `hindawi` and `hindawicc` here and in the terminal (the terminal icon, bottom left).
cd /content
if [ ! -x /usr/local/bin/hin ]; then
  printf 'Fetching the prebuilt tools... '
  if curl -fsSL -o tools.tgz https://github.com/hindawiai/hindawi2026.10/releases/latest/download/hindawi-tools-linux-x86_64.tar.gz \\
     && mkdir -p hindawi && tar -xzf tools.tgz -C hindawi && rm -f tools.tgz; then echo done
  else
    echo 'not available yet; building from source instead (a few minutes)'
    apt-get -qq install -y gawk flex bison >/dev/null 2>&1
    git clone -q --depth 1 https://github.com/hindawiai/hindawi2026.10 hindawi && (cd hindawi && bash scripts/build.sh >/dev/null 2>&1)
  fi
  bash /content/hindawi/scripts/colab_env.sh
fi
mkdir -p /content/hin && echo 'Ready. Write your program in the cells below and press ▶.'
"""
def code(src, hidden=True):
    return {"cell_type": "code", "metadata": {"cellView": "form"} if hidden else {}, "execution_count": None, "outputs": [], "source": src}
md = lambda t: {"cell_type": "markdown", "metadata": {}, "source": t}
eng_dir = R / "samples"; gallery = lambda l: R / "docs/hindawi/samples" / l
for lang in langs:
    with tempfile.TemporaryDirectory() as d:
        subprocess.run([sys.executable, "lang/hindawi/burp/burp.py", "ingest", "samples/shailis", "--langs", lang, "--out", d,
                        "--translators", "glossary"], capture_output=True)
        def native(rel):
            p = (Path(d) / lang / Path(rel).name) if rel.startswith("shailis/") else gallery(lang) / rel
            return p.read_text(encoding="utf-8") if p.exists() else None
        def english(rel):
            p = (R / "samples" / rel) if rel.startswith("shailis/") else (R / "samples/gate" / rel if (R / "samples/gate" / rel).exists() else gallery("english") / rel)
            return p.read_text(encoding="utf-8") if p.exists() else None
        name = NATIVE.get(lang, lang)
        cells = [md(f"# **हिन्दवी · Hindawi 2026.10** · {name}\n\nWrite programs in {name}, in every style Hindawi offers (C, C++, Python, Java, "
                    f"BASIC, Lex, Yacc and assembly), and run them: each one goes through the original Hindawi pipeline to the machine.\n\n"
                    "**How to use it:** press ▶ on Installation once. Then in each section, edit the program (double-click it), and press ▶ "
                    "on *Run it*. *See every stage* shows how your words became the program the computer runs."),
                 md("# Installation"), code(INSTALL), md(f"# Practice area · {name}")]
        for title, shaili, rel, given in SHAILIS:
            prog = native(rel)
            if not prog:
                continue
            fn = Path(rel).name
            t = Path(d) / "try" / fn; t.parent.mkdir(exist_ok=True); t.write_text(prog, encoding="utf-8")   # only what runs goes in
            r = subprocess.run([sys.executable, "bin/hin", "run", lang, str(t)], input=(given or "").replace("\\n", "\n"),
                               capture_output=True, text=True, timeout=120)
            if "Traceback" in r.stdout + r.stderr or (r.returncode and "is not installed here" not in r.stdout):
                print(f"seed_notebooks: {lang} {title}: left out, it does not run yet ({(r.stdout + r.stderr).strip().splitlines()[-1][:80] if (r.stdout + r.stderr).strip() else r.returncode})")
                continue
            cells += [md(f"## {title} ({shaili})"),
                      code(f"#@title **Your {title} program, in {name}**\n#@markdown Double-click to edit, then run the next cell.\n%%writefile /content/hin/{fn}\n{prog}", hidden=False),
                      code(f"%%shell\n#@title **Run it**\n" + (f"printf '{given}' | " if given else "") + f"hin run {lang} /content/hin/{fn}"),
                      code(f"%%shell\n#@title **See every stage** (how your words became the program)\nhin stages {lang} /content/hin/{fn}")]
        cells.append(md("# Example in English (for reference)\nThe same programs in English, to compare and to cross-check."))
        for title, shaili, rel, given in SHAILIS:
            prog = english(rel)
            if not prog:
                continue
            fn = "english_" + Path(rel).name if not rel.endswith(".java") else Path(rel).name
            cells += [code(f"#@title **{title} in English**\n%%writefile /content/hin/{fn}\n{prog}", hidden=False),
                      code(f"%%shell\n#@title **Run it**\n" + (f"printf '{given}' | " if given else "") + f"hin run english /content/hin/{fn}")]
        cells.append(md("# Next\n- [Every GATE program, in your language](https://github.com/hindawiai/hindawi2026.10/blob/main/docs/hindawi/GATE-PROGRAMS.md)\n"
                        "- [Can a language survive the whole stack?](https://hindawiai.github.io/hindawi2026.10/trace/) and [inside the machine](https://hindawiai.github.io/hindawi2026.10/trace/machine.html)\n"
                        "- [Build and drive the robot](https://hindawiai.github.io/hindawi2026.10/robots/)\n- [Take on a work package](https://hindawiai.github.io/hindawi2026.10/hindawi/work-packages.html)\n\n"
                        "© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. Hindawi™ is his trademark."))
        nb = {"cells": cells, "metadata": {"colab": {"provenance": []}, "kernelspec": {"display_name": "Python 3", "name": "python3"},
              "language_info": {"name": "python"}}, "nbformat": 4, "nbformat_minor": 0}
        out = R / "notebooks/practice" / f"hindawi_{lang}.ipynb"; out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"seed_notebooks: {out.relative_to(R)}: {sum(1 for c in cells if c['cell_type'] == 'code')} code cells")
PY
