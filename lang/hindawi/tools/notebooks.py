#!/usr/bin/env python3
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""notebooks.py: the Colab notebooks. Each is written once, in English, here; every other language's copy is made by
ingesting its code cells with BURP, the same way every program in this repository reaches its languages.

  python3 lang/hindawi/tools/notebooks.py [--langs L]       notebooks/<lang>/*.ipynb and docs/hindawi/notebooks.html
"""
import argparse, json, re, subprocess, sys, tempfile, shutil
from pathlib import Path

R = Path(__file__).resolve().parents[3]
REPO = "hindawiai/hindawi2026.10"
DEFAULT = "english,hindi,urdu,sindhi,punjabi,punjabi_shahmukhi,dari,pashto,telugu,kannada,sanskrit"
SETUP = '''import os, subprocess, sys
REPO = os.environ.get("HINDAWI_REPO", "/content/hindawi2026.10")
if not os.path.isdir(REPO):            # in Colab: fetch Hindawi and the one tool Colab lacks
    subprocess.run(["git", "clone", "--depth", "1", "https://github.com/hindawiai/hindawi2026.10", REPO], check=True)
    subprocess.run("apt-get -qq install -y flex > /dev/null", shell=True)
subprocess.run(["bash", REPO + "/scripts/build.sh"], check=True)
sys.path.insert(0, REPO + "/lang/hindawi"); import colab
HINDAWI = REPO + "/bin/hindawi"
LANG = "english"   # the language this notebook is written in
SHOW = "urdu"      # the language the tools below are shown on'''
QUICK = '''%%hindawi_c english
#include <stdio.h>
/* quick sort */
void swap(int *first, int *second) { int temp = *first; *first = *second; *second = temp; }
int partition(int values[], int low, int high) {
  int pivot = values[high], index = low - 1;
  for (int scan = low; scan < high; scan++)
    if (values[scan] <= pivot) { index++; swap(&values[index], &values[scan]); }
  swap(&values[index + 1], &values[high]);
  return index + 1;
}
void quick_sort(int values[], int low, int high) {
  if (low < high) { int middle = partition(values, low, high); quick_sort(values, low, middle - 1); quick_sort(values, middle + 1, high); }
}
int main(void) {
  int values[] = {29, 3, 72, 14, 8, 55, 1, 40};
  quick_sort(values, 0, 7);
  for (int index = 0; index < 8; index++) printf("%d ", values[index]);
  printf("\\n");
  return 0;
}'''
SEARCH = '''%%hindawi_py english
def binary_search(values, key):
    low, high = 0, len(values) - 1
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == key:
            return middle
        if values[middle] < key:
            low = middle + 1
        else:
            high = middle - 1
    return None

for key in [23, 7]:
    print(key, binary_search([2, 5, 8, 12, 16, 23, 38], key))'''
NOTEBOOKS = [
    ("00_start_here", "Start here: Hindawi in your language", [
        ("md", "This notebook installs Hindawi 2026.10 in the notebook's machine, checks it, and runs the verification."),
        ("code", SETUP),
        ("code", "!{HINDAWI} doctor"),
        ("code", "!{HINDAWI} verify --langs {SHOW}"),
        ("md", "Every step should say PASS. The other notebooks each show one thing Hindawi does.")]),
    ("01_c_in_your_language", "Write C in your language", [
        ("md", "A C program written in the language of this notebook. It goes through the script filter and Romenagri, "
               "the language's transducer gives C, and gcc compiles it. Names keep their form down to the binary."),
        ("code", SETUP), ("code", QUICK),
        ("md", "Change a value and run the cell again. The same program in any other language is in that language's copy of this notebook.")]),
    ("02_python_in_your_language", "Write Python in your language", [
        ("md", "Python written in the language of this notebook: its keywords are lowered to Python's, its names stay as written."),
        ("code", SETUP), ("code", SEARCH)]),
    ("03_projects_with_burp", "A whole project, into every language and back", [
        ("md", "BURP puts a project into any number of languages at once and brings it back byte for byte."),
        ("code", SETUP),
        ("code", "!{HINDAWI} ingest {REPO}/samples/gate/algorithms/sorting --langs {SHOW} --out /tmp/n\n!cat /tmp/n/{SHOW}/merge_sort.c"),
        ("code", "!{HINDAWI} reverse /tmp/n/{SHOW} --out /tmp/back && diff -r {REPO}/samples/gate/algorithms/sorting /tmp/back && echo identical")]),
    ("04_gate_programs", "The GATE programs in your language", [
        ("md", "Every GATE program, compiled from the language through the original pipeline, run, and compared with English."),
        ("code", SETUP), ("code", "!{HINDAWI} gate --langs {SHOW}"),
        ("md", "What the programs cover against the GATE syllabus, and the topics still open to anyone: docs/hindawi/GATE-PROGRAMS.md "
               "and the GATE work packages.")]),
    ("05_language_standard", "Your language's standard", [
        ("md", "Each language's standard is generated from its cell. This shows its coverage, its standard, and what is left to do."),
        ("code", SETUP), ("code", "!{HINDAWI} coverage --langs {SHOW} --missing"),
        ("code", "!{HINDAWI} standard generate --langs {SHOW}\n!head -60 {REPO}/standards/{SHOW}/standard.md"),
        ("code", "!{HINDAWI} wp list language | head -20")]),
    ("06_sovereign_stack", "The sovereign stack", [
        ("md", "The open stack, layer by layer, ingested into the language, measured, reversed, and built through Hindawi."),
        ("code", SETUP), ("code", "!bash {REPO}/scripts/sovereign/stack.sh --list"),
        ("code", "!cd {REPO} && bash scripts/sovereign/stack.sh --only lua --langs {SHOW} --build"),
        ("md", "docs/hindawi/SOVEREIGNTY.md says how far the stack goes today, layer by layer.")]),
]


def cell(kind, text, n=0):
    lines = text.split("\n")
    src = [l + "\n" for l in lines[:-1]] + [lines[-1]]
    c = {"id": f"cell-{n:02d}", "cell_type": "markdown" if kind == "md" else "code", "metadata": {}, "source": src}
    if kind != "md":
        c.update({"execution_count": None, "outputs": []})
    return c


def localise(cells, lang):
    """Every %%hindawi_c and %%hindawi_py cell, ingested into lang by BURP; LANG and SHOW set to lang."""
    if lang == "english":
        return cells
    d = Path(tempfile.mkdtemp(prefix="nb-")); (d / "src").mkdir()
    for i, (kind, text) in enumerate(cells):
        m = re.match(r"%%hindawi_(c|py) english\n", text)
        if m:
            (d / "src" / f"cell{i:02d}.{m.group(1)}").write_text(text[m.end():] + "\n", encoding="utf-8")
    subprocess.run([sys.executable, str(R / "lang/hindawi/burp/burp.py"), "ingest", str(d / "src"), "--langs", lang, "--out", str(d / "n")],
                   capture_output=True)
    out = []
    for i, (kind, text) in enumerate(cells):
        m = re.match(r"%%hindawi_(c|py) english\n", text)
        if m:
            body = (d / "n" / lang / f"cell{i:02d}.{m.group(1)}").read_text(encoding="utf-8").rstrip("\n")
            text = f"%%hindawi_{m.group(1)} {lang}\n{body}"
        text = text.replace('LANG = "english"', f'LANG = "{lang}"').replace('SHOW = "urdu"', f'SHOW = "{lang}"')
        out.append((kind, text))
    shutil.rmtree(d, ignore_errors=True)
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--langs", default=DEFAULT); a = ap.parse_args()
    langs = a.langs.split(",")
    rows = []
    for lang in langs:
        nd = R / "notebooks" / lang; nd.mkdir(parents=True, exist_ok=True)
        for name, title, cells in NOTEBOOKS:
            cs = localise([("md", f"# {title}\n\nHindawi 2026.10, in {lang.replace('_', ' ').title()}. "
                                  "© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.")] + cells, lang)
            nb = {"nbformat": 4, "nbformat_minor": 5, "metadata": {"kernelspec": {"name": "python3", "display_name": "Python 3"},
                  "language_info": {"name": "python"}, "colab": {"name": f"{name}.ipynb"}}, "cells": [cell(k, t, n) for n, (k, t) in enumerate(cs)]}
            (nd / f"{name}.ipynb").write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        rows.append(lang)
    links = "".join(
        f"<tr><th>{t}</th>" + "".join(
            f'<td><a href="https://colab.research.google.com/github/{REPO}/blob/main/notebooks/{l}/{n}.ipynb">{l.replace("_", " ")}</a></td>'
            for l in rows) + "</tr>\n" for n, t, _ in NOTEBOOKS)
    (R / "docs/hindawi/notebooks.html").write_text(f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Hindawi notebooks</title>
<style>:root{{--bg:#fff;--fg:#1d1d1f;--line:#ddd;--acc:#1f4e79}}@media (prefers-color-scheme:dark){{:root{{--bg:#141414;--fg:#eee;--line:#333;--acc:#8ab4f8}}}}
body{{font:15px/1.5 system-ui,sans-serif;background:var(--bg);color:var(--fg);max-width:1200px;margin:0 auto;padding:16px}}
a{{color:var(--acc)}}.wrap{{overflow-x:auto}}table{{border-collapse:collapse}}td,th{{border:1px solid var(--line);padding:6px 8px;text-align:left;white-space:nowrap}}</style>
</head><body><h1>Hindawi notebooks, in Colab</h1>
<p>Each notebook is written once, in English, and each language's copy is made by ingesting its code with BURP. Open
one in Colab, run the cells in order; the first cell installs Hindawi in the notebook's machine.</p>
<div class="wrap"><table>{links}</table></div></body></html>
""", encoding="utf-8")
    print(f"notebooks: {len(NOTEBOOKS)} notebooks in {len(rows)} languages")


if __name__ == "__main__":
    main()
