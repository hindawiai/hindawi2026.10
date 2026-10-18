# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""colab.py: Hindawi in a notebook, for every language: the equivalent of Chintamani's notebook UI.

    import colab as H
    H.ide("urdu")                         the practice area: program, input and output; Build, Run, Stages, To host,
                                          From host, New, Load demo, Upload, Download
    H.show("program.c", "urdu", "C")      every stage of the compilation path, the build, and the run
    %%hindawi C urdu                      a cell written in Urdu: every stage shown, compiled and run (C, C++ or Python)

Everything goes through the original pipeline: the script filter, Romenagri, the language's own transducer for the
shaili, then the host compiler. Nothing is compiled from Unicode directly.
"""
import os, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(os.environ.get("HINDAWI_REPO") or Path(__file__).resolve().parents[2])
RMN = ROOT / ".build/chintamani/Romenagri"
os.environ["PATH"] = f"{RMN}{os.pathsep}{os.environ.get('PATH', '')}"
os.environ.setdefault("ROMENAGRI", str(RMN))
for p in ("lang/hindawi/tools", "lang/hindawi/burp"):
    if str(ROOT / p) not in sys.path:
        sys.path.insert(0, str(ROOT / p))
import hindawi_chain as hc  # noqa: E402
import burp  # noqa: E402

# shaili name, the language's own forward transducer, file extension, host compiler
SHAILIS = {"C": ("guru", "h2c", ".c"), "C++": ("shraeni", "h2cpp", ".cpp"), "Python": ("soochee", "h2py", ".py")}
WORK = Path(tempfile.gettempdir()) / "hindawi-notebook"
STAGE_NAMES = {"source": "1. the program as written", "script filter": "2. the script filter (to Devanagari)",
               "Romenagri": "3. Romenagri: the transliterated form the compiler works on",
               "C": "4. the transducer's C", "C++": "4. the transducer's C++", "Python": "4. the transducer's Python"}


def compiles(lang):
    """Whether the language has a compilation path: a script filter for its script, or Devanagari."""
    try:
        hc.script_filter(lang)
        return True
    except SystemExit:
        return False


def demos(lang, shaili="C"):
    """The GATE programs of the repository, in the language, as BURP ingests them: name -> source text."""
    ext = SHAILIS[shaili][2]
    out = WORK / "demos" / lang
    if not (out / lang).exists():
        out.mkdir(parents=True, exist_ok=True)
        subprocess.run([sys.executable, str(ROOT / "lang/hindawi/burp/burp.py"), "ingest", str(ROOT / "samples/gate"),
                        "--langs", lang, "--out", str(out)], capture_output=True, check=True)
    files = sorted(p for p in (out / lang).rglob(f"*{ext}") if ".hindawi" not in p.parts)
    return {str(p.relative_to(out / lang)): p.read_text(encoding="utf-8") for p in files}


def stages(src, lang, shaili="C"):
    """Every stage of the compilation path for the source, as (name, text); the last is what the host compiler gets."""
    if lang == "english":
        return [("source", src), (shaili, src)]
    return hc.stages(src, lang, SHAILIS[shaili][1])


def to_host(src, lang, shaili="C"):
    """The program in the host language: Chintamani's Hin2Std."""
    return stages(src, lang, shaili)[-1][1]


def from_host(src, lang, shaili="C"):
    """A host-language program in the language, through BURP: Chintamani's Std2Hin."""
    d = Path(tempfile.mkdtemp(prefix="hindawi-std2hin-"))
    (d / "src").mkdir()
    (d / "src" / f"program{SHAILIS[shaili][2]}").write_text(src, encoding="utf-8")
    subprocess.run([sys.executable, str(ROOT / "lang/hindawi/burp/burp.py"), "ingest", str(d / "src"), "--langs", lang,
                    "--out", str(d / "n")], capture_output=True, check=True)
    return (d / "n" / lang / f"program{SHAILIS[shaili][2]}").read_text(encoding="utf-8")


def build(src, lang, shaili="C"):
    """Lower the program through the original pipeline and build it. Returns (ok, log)."""
    WORK.mkdir(parents=True, exist_ok=True)
    try:
        host = to_host(src, lang, shaili)
    except SystemExit as e:
        return False, str(e)
    (WORK / "prog.py").unlink(missing_ok=True); (WORK / "prog").unlink(missing_ok=True)
    if shaili == "Python":
        (WORK / "prog.py").write_text(host, encoding="utf-8")
        r = subprocess.run([sys.executable, "-m", "py_compile", str(WORK / "prog.py")], capture_output=True, text=True)
        return r.returncode == 0, r.stderr or "built: prog.py"
    f = WORK / f"prog{SHAILIS[shaili][2]}"
    f.write_text(host, encoding="utf-8")
    cc = ["g++"] if shaili == "C++" else ["gcc"]
    r = subprocess.run(cc + ["-O2", "-g", "-o", str(WORK / "prog"), str(f), "-lm"], capture_output=True, text=True)
    return r.returncode == 0, (r.stderr or f"built: {WORK / 'prog'}")


def run(shaili="C", stdin=""):
    """Run the last program built, with the given standard input."""
    cmd = [sys.executable, str(WORK / "prog.py")] if shaili == "Python" else [str(WORK / "prog")]
    if not Path(cmd[-1]).exists():
        return "Please build the program first."
    try:
        r = subprocess.run(cmd, input=stdin, capture_output=True, text=True, timeout=20)
        return r.stdout + r.stderr
    except subprocess.TimeoutExpired:
        return "The program ran past twenty seconds and was stopped."


def show(path, lang, shaili="C", input_path=None):
    """Print every stage of the compilation path, then build and run: the execution cell of the notebook."""
    src = Path(path).read_text(encoding="utf-8")
    for name, text in stages(src, lang, shaili):
        print(f"===== {STAGE_NAMES.get(name, name)}\n{text.rstrip()}\n")
    ok, log = build(src, lang, shaili)
    print(f"===== 5. build\n{log.strip()}\n")
    if ok:
        stdin = Path(input_path).read_text(encoding="utf-8") if input_path and Path(input_path).exists() else ""
        print(f"===== 6. run\n{run(shaili, stdin).rstrip()}")


def ide(lang):
    """The practice area, as in Chintamani's notebook: program, input and output areas and the buttons."""
    import ipywidgets as w
    from IPython.display import display
    try:
        from google.colab import files as colab_files
    except ImportError:
        colab_files = None
    ok_lang = lang == "english" or compiles(lang)
    shaili = w.Dropdown(options=list(SHAILIS), value="C", description="Shaili")
    demo = w.Dropdown(options=[], description="Demo", layout=w.Layout(width="60%"))
    program = w.Textarea(rows=18, layout=w.Layout(width="98%"), placeholder="Write the program here, in the language.")
    stdin = w.Textarea(rows=4, layout=w.Layout(width="49%"), placeholder="Input for the program")
    output = w.Textarea(rows=14, layout=w.Layout(width="49%"), placeholder="Output")
    buttons = {n: w.Button(description=n) for n in ("Load demo", "New", "Build", "Run", "Stages", "To host", "From host",
                                                     "Upload", "Download")}

    def refresh(*_):
        names = list(demos(lang, shaili.value)) if lang != "english" else []
        demo.options = names
        demo.value = names[0] if names else None
    shaili.observe(refresh, names="value")

    def act(name):
        def f(_):
            try:
                if name == "Load demo" and demo.value:
                    program.value = demos(lang, shaili.value)[demo.value]
                elif name == "New":
                    program.value = stdin.value = output.value = ""
                elif name == "Build":
                    ok, log = build(program.value, lang, shaili.value)
                    output.value = ("Built.\n" if ok else "Build failed.\n") + log
                elif name == "Run":
                    output.value = run(shaili.value, stdin.value)
                elif name == "Stages":
                    output.value = "\n".join(f"===== {STAGE_NAMES.get(n, n)}\n{t}" for n, t in stages(program.value, lang, shaili.value))
                elif name == "To host":
                    program.value = to_host(program.value, lang, shaili.value)
                elif name == "From host":
                    program.value = from_host(program.value, lang, shaili.value)
                elif name == "Upload" and colab_files:
                    up = colab_files.upload()
                    if up:
                        program.value = next(iter(up.values())).decode("utf-8")
                elif name == "Download":
                    p = Path(f"hindawi-program{SHAILIS[shaili.value][2]}")
                    p.write_text(program.value, encoding="utf-8")
                    if colab_files:
                        colab_files.download(str(p))
                    else:
                        output.value = f"Saved as {p.resolve()}"
            except Exception as e:  # shown to the learner, never hidden
                output.value = f"{name}: {e}"
        return f
    for n, b in buttons.items():
        b.on_click(act(n))
    if not ok_lang:
        output.value = (f"{lang} reads and writes programs (From host shows any program in it), but its script has no "
                        "filter yet, so it cannot be compiled. That work is a package anyone can take.")
    refresh()
    display(w.VBox([w.HBox([shaili, demo, buttons["Load demo"], buttons["New"]]), program,
                    w.HBox([buttons[n] for n in ("Build", "Run", "Stages", "To host", "From host", "Upload", "Download")]),
                    w.HBox([stdin, output])]))


try:  # the cell magic, where IPython is running
    from IPython.core.magic import register_cell_magic

    @register_cell_magic
    def hindawi(line, cell):
        """%%hindawi SHAILI LANGUAGE: the cell is a program in that language; every stage is shown, then it is run."""
        parts = line.split()
        shaili, lang = (parts + ["C", "english"])[:2] if parts else ("C", "english")
        WORK.mkdir(parents=True, exist_ok=True)
        f = WORK / f"cell{SHAILIS[shaili][2]}"
        f.write_text(cell, encoding="utf-8")
        show(f, lang, shaili)
except Exception:  # outside IPython the functions above are all there is
    pass
