#!/usr/bin/env bash
# seed_notebooks.sh: write the Hindawi 2026.10 notebooks into ./notebooks/, one per language, in the design of the
# Hindawi NB UI of the Chintamani notebooks: a practice area where the learner picks a shaili, a GATE section and a
# program in their own language, edits it, gives it input, and presses Build, Run, Stages, To C, From English, New,
# Upload or Download. Every GATE program of the repository is selectable; each GATE section has a place to teach it in
# the mother tongue. Runs in Colab or any Jupyter with gcc.
#   bash seed_notebooks.sh                       ten languages, using a shallow clone of hindawiai/hindawi2026.10
#   bash seed_notebooks.sh --langs urdu,telugu   chosen languages
#   bash seed_notebooks.sh --repo DIR            an existing checkout instead of cloning
# Only ./notebooks/ (and ./.hindawi2026.10 when cloning) is written.
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
set -euo pipefail
W="$PWD"; REPO=""; LANGS="urdu,hindi,punjabi,punjabi_shahmukhi,sindhi,telugu,kannada,sanskrit,dari,pashto"
while [ $# -gt 0 ]; do
  case "$1" in --repo) REPO="$2"; shift 2 ;; --langs) LANGS="$2"; shift 2 ;; *) echo "seed_notebooks: unknown $1"; exit 2 ;; esac
done
if [ -z "$REPO" ]; then
  [ -d "$W/.hindawi2026.10/.git" ] || git clone -q --depth 1 https://github.com/hindawiai/hindawi2026.10 "$W/.hindawi2026.10"
  REPO="$W/.hindawi2026.10"
fi
python3 - "$REPO" "$LANGS" "$W/notebooks" <<'PY'
import json, sys
from pathlib import Path
repo, langs, out = Path(sys.argv[1]), sys.argv[2].split(","), Path(sys.argv[3])
md = lambda t: {"cell_type": "markdown", "metadata": {}, "source": t}
code = lambda t: {"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [], "source": t}
sections = sorted({str(p.parent.relative_to(repo / "samples/gate")) for p in (repo / "samples/gate").rglob("*") if p.suffix in (".c", ".py")})
SETUP = r'''import os, subprocess, sys, tempfile, pathlib
REPO = os.environ.get('HINDAWI_REPO') or os.path.abspath('hindawi2026.10')
if not os.path.isdir(REPO):
    subprocess.run(['git', 'clone', '-q', '--depth', '1', 'https://github.com/hindawiai/hindawi2026.10', REPO], check=True)
if 'google.colab' in sys.modules:
    subprocess.run('apt-get -qq install -y flex bison gawk > /dev/null', shell=True)
RMN = os.path.join(REPO, '.build/chintamani/Romenagri')
if not os.path.exists(os.path.join(RMN, 'rmn2acii')):
    subprocess.run(['bash', os.path.join(REPO, 'scripts/build.sh')], check=True)
os.environ['PATH'] = RMN + os.pathsep + os.environ['PATH']; os.environ['ROMENAGRI'] = RMN
sys.path.insert(0, os.path.join(REPO, 'lang/hindawi/tools'))
import hindawi_chain as hc
GATE = pathlib.Path(REPO, 'samples/gate'); GALLERY = pathlib.Path(REPO, 'docs/hindawi/samples', LANG)

def english_to_language(text, name='program.c'):
    """English source into LANG with BURP; every error is shown, never hidden."""
    d = pathlib.Path(tempfile.mkdtemp(prefix='hindawi-')); (d / 'src').mkdir()
    (d / 'src' / pathlib.Path(name).name).write_text(text, encoding='utf-8')
    r = subprocess.run([sys.executable, os.path.join(REPO, 'lang/hindawi/burp/burp.py'), 'ingest', str(d / 'src'),
                        '--langs', LANG, '--out', str(d / 'n'), '--translators', 'glossary'], capture_output=True, text=True)
    f = d / 'n' / LANG / pathlib.Path(name).name
    if r.returncode != 0 or not f.exists():
        raise RuntimeError('BURP could not put this into ' + LANG + ':\n' + r.stdout + r.stderr)
    return f.read_text(encoding='utf-8')

def program_text(rel):
    """The GATE program rel (a path under samples/gate) as written in LANG: from the gallery, or by BURP."""
    p = GALLERY / rel
    return p.read_text(encoding='utf-8') if p.exists() else english_to_language((GATE / rel).read_text(encoding='utf-8'), rel)

def stages(src, shaili='guru'):
    return hc.stages(src, LANG, 'h2py' if shaili == 'soochee' else 'h2c')

def build(src):
    """Compile a C program written in LANG through the original pipeline: (executable or None, messages)."""
    d = pathlib.Path(tempfile.mkdtemp(prefix='hindawi-')); f = d / 'program.c'; f.write_text(src, encoding='utf-8')
    env = dict(os.environ, HINDAWI_LANG=LANG, HINDAWI_NATIVE_SOURCE='1')
    r = subprocess.run([os.path.join(REPO, 'lang/hindawi/hindawicc'), '-O2', '-o', str(d / 'program'), str(f), '-lm'],
                       capture_output=True, text=True, env=env)
    return (d / 'program' if r.returncode == 0 else None), (r.stderr or 'built')

def run(exe, stdin=''):
    r = subprocess.run([str(exe)], input=stdin, capture_output=True, text=True, timeout=20)
    return r.stdout + r.stderr

def run_python(src, stdin=''):
    r = subprocess.run([sys.executable, '-c', hc.to_py(src, LANG)], input=stdin, capture_output=True, text=True, timeout=20)
    return r.stdout + r.stderr
print('ready:', LANG, 'from', REPO)'''

UI = r'''import ipywidgets as w
from IPython.display import display, FileLink
progs = {s: sorted(p.name for p in (GATE / s).iterdir() if p.suffix in ('.c', '.py')) for s in SECTIONS}
shaili = w.ToggleButtons(options=[('C (guru)', 'guru'), ('Python (soochee)', 'soochee')], value='guru')
section = w.Dropdown(options=SECTIONS, description='Section')
program = w.Dropdown(description='Program')
editor = w.Textarea(layout=w.Layout(width='99%', height='340px'))
given = w.Textarea(placeholder='input for the program', layout=w.Layout(width='49%', height='120px'))
shown = w.Textarea(placeholder='output', layout=w.Layout(width='49%', height='120px'))
view = w.Output(layout=w.Layout(width='99%', border='1px solid #bbb', padding='4px'))
upload = w.FileUpload(accept='.c,.py,.txt', multiple=False, description='Upload')
state = {'exe': None}

def fill_programs(*_):
    ext = '.py' if shaili.value == 'soochee' else '.c'
    names = [n for n in progs.get(section.value, []) if n.endswith(ext)]
    program.options = names or ['(none in this section)']
def load(*_):
    state['exe'] = None
    if program.value and not program.value.startswith('('):
        try: editor.value = program_text(section.value + '/' + program.value); shown.value = ''
        except Exception as e: shown.value = str(e)
def do_build(_):
    if shaili.value == 'soochee': shown.value = 'Python needs no build: press Run.'; return
    state['exe'], msg = build(editor.value); shown.value = msg
def do_run(_):
    if shaili.value == 'soochee': shown.value = run_python(editor.value, given.value); return
    shown.value = run(state['exe'], given.value) if state['exe'] else 'Press Build first.'
def do_stages(_):
    view.clear_output()
    with view:
        try:
            for name, text in stages(editor.value, shaili.value):
                print('===== ' + name); print(text)
        except SystemExit as e: print(e)
def do_to_c(_):
    try: shown.value = stages(editor.value, shaili.value)[-1][1]
    except SystemExit as e: shown.value = str(e)
def do_from_english(_):
    rel = section.value + '/' + program.value
    try: editor.value = english_to_language((GATE / rel).read_text(encoding='utf-8'), rel); shown.value = 'from ' + rel
    except Exception as e: shown.value = str(e)
def do_new(_):
    editor.value = given.value = shown.value = ''; state['exe'] = None; view.clear_output()
def do_upload(change):
    v = upload.value
    for f in (v if isinstance(v, (list, tuple)) else v.values()):
        editor.value = bytes(f['content']).decode('utf-8', 'replace')
def do_download(_):
    name = program.value if program.value and not program.value.startswith('(') else 'program.c'
    p = pathlib.Path(name); p.write_text(editor.value, encoding='utf-8')
    if 'google.colab' in sys.modules:
        from google.colab import files; files.download(str(p))
    else:
        with view: display(FileLink(str(p)))

shaili.observe(lambda c: (fill_programs(), load()), 'value')
section.observe(lambda c: (fill_programs(), load()), 'value')
program.observe(lambda c: load(), 'value')
upload.observe(do_upload, 'value')
acts = [('Build', do_build), ('Run', do_run), ('Stages', do_stages), ('To C', do_to_c),
        ('From English', do_from_english), ('New', do_new), ('Download', do_download)]
bar = w.HBox([w.Button(description=n, layout=w.Layout(width='auto')) for n, _ in acts] + [upload])
for b, (_, f) in zip(bar.children, acts): b.on_click(f)
fill_programs(); load()
display(w.VBox([shaili, w.HBox([section, program]), bar, editor, w.HBox([given, shown]), view]))'''

written = []
for lang in langs:
    if not (repo / "docs/hindawi/samples" / lang).exists():
        print(f"seed_notebooks: {lang}: no GATE gallery in the repository, skipped"); continue
    name = lang.replace("_", " ").title()
    cells = [
        md(f"# Hindawi 2026.10 in {name}\n\nProgram in {name}: every GATE program, in C and in Python, compiled through the "
           "original Hindawi pipeline, with every step shown.\n\n© 1993–2026 Abhishek Choudhary. All rights reserved. "
           "AyeAI. Hindawi™ and Romenagri™ are his trademarks; AyeAI®, AyeCNSe® and AyeAM® are his registered trademarks "
           "in India."),
        md("## 1. Installation\n\nRun this once. It fetches Hindawi, builds the Romenagri tools and the original "
           "transducers, and loads the compilation path."),
        code(f"LANG = {lang!r}\nSECTIONS = {sections!r}\n" + SETUP),
        md(f"## 2. Practice area\n\nChoose **C (guru)** or **Python (soochee)**, a GATE section and a program: it opens in "
           f"{name}. Edit it, put any input in the left box, then:\n\n"
           "| Button | What it does |\n|---|---|\n"
           "| Build | compiles the C program through the original pipeline |\n"
           "| Run | runs it with your input (a Python program runs directly) |\n"
           "| Stages | shows every step: the source, the script filter, the Romenagri form, and the C or Python it becomes |\n"
           "| To C | shows only the C (or Python) the compiler gets |\n"
           f"| From English | brings the English original of the chosen program into {name} with BURP |\n"
           "| New | clears everything, to write your own |\n"
           "| Upload, Download | open a program from your computer, or save the one in the editor |"),
        code(UI),
        md("## 3. Teach GATE in your language\n\nEach section below is a place to explain the topic in your own words, "
           "beside its programs. Write in the cell, or claim the section as a work package on the work-packages page of "
           "hindawiai/hindawi2026.10, so the explanation joins the repository with your name on it."),
    ]
    for s in sections:
        names = sorted(p.name for p in (repo / "samples/gate" / s).iterdir() if p.suffix in (".c", ".py"))
        cells.append(md(f"### {s.replace('_', ' ').replace('/', ': ')}\n\nPrograms: " + ", ".join(f"`{n}`" for n in names) +
                        f"\n\n*Explain this section in {name} here.*"))
    cells.append(md("## 4. Robots\n\nThe same language drives the robots: Arduino UNO first, then ESP32. The sketches, in "
                    "this language and in English, and how to load them, are in `robot_coding/` beside these notebooks."))
    nb = {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                                       "language_info": {"name": "python"}}, "nbformat": 4, "nbformat_minor": 5}
    out.mkdir(parents=True, exist_ok=True)
    (out / f"hindawi_{lang}.ipynb").write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
    written.append(lang)
print(f"seed_notebooks: {len(written)} notebooks in {out}: {', '.join(written)}; {len(sections)} GATE sections each")
PY
