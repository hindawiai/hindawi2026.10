#!/usr/bin/env python3
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""notebooks.py: one notebook per language, in the structure of Chintamani's Hindawi notebook
(hindawiai/chintamani, Notebooks/हिंदवी_2022_8_स्मरण_पुस्तिका.ipynb): installation; the Hindawi NB UI practice area;
then, for each shaili verified for the language, program editing, input editing, the compilation flow, execution, and
the English original brought into the language. A shaili is included only if its demo was built through the original
pipeline and printed what the English original prints (notebooks/verified.json, written by --verify).

  python3 lang/hindawi/tools/notebooks.py --verify      check every language, then write the notebooks and the page
  python3 lang/hindawi/tools/notebooks.py               write them from the last verification
"""
import argparse, json, subprocess, sys
from pathlib import Path

R = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(R / "lang/hindawi")); sys.path.insert(0, str(R / "lang/hindawi/tools"))
NB_DIR, PAGE = R / "notebooks", R / "docs/hindawi/notebooks.html"
REPO_URL = "https://github.com/hindawiai/hindawi2026.10"
COLAB = "https://colab.research.google.com/github/hindawiai/hindawi2026.10/blob/main/notebooks/{lang}/hindawi_{lang}.ipynb"
CREDIT = "© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI."
SHAILI_TEXT = {
    "guru": ("C", ".c", "algorithms/searching/binary_search.c",
             "Shaili guru is C written in the language: the language of systems, memory and the machine, for high school, "
             "undergraduate and GATE students. A program here goes through the script filter and Romenagri, the "
             "language's transducer gives C, and gcc compiles it; the names reach the binary in their Romenagri form."),
    "soochee": ("Python", ".py", "paradigms/binary_search.py",
                "Shaili soochee is Python written in the language. It goes through the same path as C, with the "
                "language's Python transducer at the end, so a name has the same form in Python as in C."),
}


def cell(kind, text):
    c = {"cell_type": kind, "metadata": {}, "source": text.splitlines(keepends=True)}
    if kind == "code":
        c.update(outputs=[], execution_count=None)
    return c


def notebook(lang, shailis, demos):
    name = lang.replace("_", " ").title()
    colab = COLAB.format(lang=lang)
    cells = [
        cell("markdown", f"# Hindawi Programming System 2026.10: {name}\n\n{CREDIT}\n\n"
             f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab})"),
        cell("markdown", "## Introduction\n\nHindawi makes programming possible in the mother tongue, from school to the "
             "GATE Computer Science level and on to systems work. You write the program in "
             f"{name}; Hindawi carries it through the script filter and Romenagri to the host language, and the "
             "ordinary compiler builds it. Every stage is shown below, so nothing is hidden between what you write and "
             "what runs.\n\nThis notebook follows Chintamani's Hindawi notebook: installation, the practice area, then "
             "each shaili in turn."),
        cell("markdown", "## Installation\n\nRun this cell once before the others. In Colab it takes a minute or two: "
             "it fetches Hindawi and builds Chintamani's Romenagri tools from source."),
        cell("code", "#@title Installation { vertical-output: true }\n"
             "import os, subprocess, sys\n"
             "here = os.path.abspath(os.path.join(os.getcwd(), '..', '..'))\n"
             "REPO = next((p for p in (os.environ.get('HINDAWI_REPO', ''), here, '/content/hindawi2026.10',\n"
             "                          os.path.abspath('hindawi2026.10')) if p and os.path.isfile(p + '/lang/hindawi/nb.py')), None)\n"
             "if REPO is None:\n"
             "    REPO = '/content/hindawi2026.10' if os.path.isdir('/content') else os.path.abspath('hindawi2026.10')\n"
             f"    subprocess.run(['git', 'clone', '-q', '--depth', '1', '{REPO_URL}', REPO], check=True)\n"
             "if not os.path.isfile(REPO + '/.build/chintamani/Romenagri/acii2cf'):\n"
             "    if os.path.isdir('/content'):\n"
             "        subprocess.run('apt-get -qq install -y flex bison gawk > /dev/null', shell=True)\n"
             "    r = subprocess.run(['bash', 'scripts/build.sh'], cwd=REPO, capture_output=True, text=True)\n"
             "    print(r.stdout[-400:], r.stderr[-400:])\n"
             "os.environ['HINDAWI_REPO'] = REPO\n"
             "sys.path.insert(0, REPO + '/lang/hindawi')\n"
             "import nb\n"
             "print('Hindawi is ready:', REPO)"),
        cell("markdown", f"## Hindawi NB UI: the practice area\n\nChoose a shaili and a demo, change the program, and "
             "press **Build and run**. **Stages** shows the whole compilation flow; **To host (Hin2Std)** shows the "
             "host-language text; **From host (Std2Hin)** turns a host-language program into "
             f"{name}; **Upload** and **Download** move programs in and out."),
        cell("code", f"#@title Practice area {{ vertical-output: true }}\nnb.ide({lang!r}, shailis={tuple(shailis)!r})"),
        cell("markdown", "## Detailed description"),
    ]
    for s in shailis:
        host, ext, english, text = SHAILI_TEXT[s]
        f = f"program_{s}{ext}"
        cells += [
            cell("markdown", f"### Shaili {s}: {host} in {name}\n\n{text}"),
            cell("markdown", "**Program editing.** Edit the program in the next cell, then run it to save it."),
            cell("code", f"%%writefile {f}\n" + demos[s].rstrip("\n") + "\n"),
            cell("markdown", "**Input editing.** Anything the program reads goes here."),
            cell("code", f"#@title Input editing\nINPUT = \"\"\"\"\"\"   # what the program reads, one value per line\n"
                         f"open('input_{s}.txt', 'w', encoding='utf-8').write(INPUT)"),
            cell("markdown", "**The compilation flow.** The program as written, the script filter's Devanagari (for "
                 "scripts that need one), the Romenagri form the compiler works on, and the host-language text."),
            cell("code", f"nb.show_stages(open({f!r}, encoding='utf-8').read(), {lang!r}, {s!r})"),
            cell("markdown", "**Program execution.**"),
            cell("code", f"nb.build_and_run(open({f!r}, encoding='utf-8').read(), {lang!r}, {s!r},\n"
                         f"                 open('input_{s}.txt', encoding='utf-8').read())"),
            cell("markdown", f"**From the host language (Std2Hin).** The English original of the same program, "
                 f"brought into {name} by BURP."),
            cell("code", f"print(nb.from_host(open(REPO + '/samples/gate/{english}', encoding='utf-8').read(), {lang!r}, {s!r}))"),
        ]
    cells.append(cell("markdown", "---\nAyeAI®, AyeCNSe® and AyeAM® are registered trademarks of Abhishek Choudhary in "
                      "India; Hindawi™ and Romenagri™ are his trademarks. "
                      "[Trademarks](https://github.com/zistgah/zistgah.github.io/blob/main/legal/TRADEMARKS.md) · "
                      "[Disclaimers](https://github.com/zistgah/zistgah.github.io/blob/main/legal/DISCLAIMERS.md)\n\n"
                      + CREDIT))
    for k, c in enumerate(cells):
        c["id"] = f"hindawi-{k:03d}"          # nbformat 4.5 cell ids, stable across regenerations
    return {"cells": cells, "metadata": {"kernelspec": {"name": "python3", "display_name": "Python 3"},
                                         "language_info": {"name": "python"}, "colab": {"provenance": []}},
            "nbformat": 4, "nbformat_minor": 5}


def page(verified, without):
    rows = "\n".join(
        f'<tr><td>{l.replace("_", " ").title()}</td><td>{", ".join(SHAILI_TEXT[s][0] for s in v)}</td>'
        f'<td><a href="{COLAB.format(lang=l)}"><img alt="Open in Colab" src="https://colab.research.google.com/assets/colab-badge.svg"></a></td>'
        f'<td><a href="{REPO_URL}/blob/main/notebooks/{l}/hindawi_{l}.ipynb">view</a></td></tr>'
        for l, v in sorted(verified.items()) if v)
    rest = ", ".join(l.replace("_", " ").title() for l in sorted(without))
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Hindawi notebooks, one per language</title>
<style>:root{{--bg:#fff;--fg:#1d1d1f;--mut:#666;--line:#ddd;--acc:#1f4e79}}
@media (prefers-color-scheme:dark){{:root{{--bg:#141414;--fg:#eee;--mut:#aaa;--line:#333;--acc:#8ab4f8}}}}
body{{font:15px/1.5 system-ui,sans-serif;background:var(--bg);color:var(--fg);max-width:980px;margin:0 auto;padding:16px}}
a{{color:var(--acc)}}table{{border-collapse:collapse;width:100%}}td,th{{border-bottom:1px solid var(--line);padding:6px;text-align:left}}
.mut{{color:var(--mut)}}</style></head><body>
<h1>Hindawi notebooks, one per language</h1>
<p>Each notebook follows Chintamani's Hindawi notebook: installation, the Hindawi NB UI practice area with loadable
demos, and for each shaili the program, its input, the whole compilation flow, its execution, and the English original
brought into the language. Open one in Colab; nothing needs to be installed on your own machine. A shaili is listed for
a language only after its demo was built through the original pipeline and printed what the English original prints.</p>
<table><tr><th>Language</th><th>Shailis</th><th>Colab</th><th>Notebook</th></tr>
{rows}
</table>
<p class="mut">No notebook yet, because the script has no filter on the compilation path (task T-29): {rest}.</p>
<p class="mut">Chintamani's original notebooks, in Hindi and Telugu, remain at
<a href="https://github.com/hindawiai/chintamani/tree/master/Notebooks">hindawiai/chintamani/Notebooks</a>.</p>
<script src="https://zistgah.github.io/legal/notice.js" defer></script>
</body></html>
"""


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--verify", action="store_true")
    a = ap.parse_args()
    vf = NB_DIR / "verified.json"
    if a.verify:
        res = json.loads(subprocess.run([sys.executable, str(R / "tests/check_notebooks.py"), "--json"],
                                        capture_output=True, text=True).stdout)
        vf.parent.mkdir(exist_ok=True)
        vf.write_text(json.dumps(res, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    verified = {l: [s for s, (ok, _) in v.items() if ok] for l, v in json.loads(vf.read_text(encoding="utf-8")).items()}
    import nb
    for old in NB_DIR.glob("*/*.ipynb"):
        old.unlink()
    for lang, shailis in verified.items():
        if not shailis:
            continue
        demos = {s: nb.demos(lang, s)["binary_search"] for s in shailis}
        d = NB_DIR / lang; d.mkdir(parents=True, exist_ok=True)
        (d / f"hindawi_{lang}.ipynb").write_text(json.dumps(notebook(lang, shailis, demos), ensure_ascii=False, indent=1) + "\n",
                                                 encoding="utf-8")
    for d in NB_DIR.iterdir():
        if d.is_dir() and not any(d.iterdir()):
            d.rmdir()
    langs = sorted(p.name for p in (R / "lang/hindawi/languages").iterdir() if (p / "h2c.uhin").exists()) + ["hindi"]
    PAGE.write_text(page(verified, [l for l in langs if not verified.get(l)]), encoding="utf-8")
    print(f"notebooks: {sum(1 for v in verified.values() if v)} languages, "
          f"{sum(len(v) for v in verified.values())} shaili sections; page {PAGE.relative_to(R)}")


if __name__ == "__main__":
    main()
