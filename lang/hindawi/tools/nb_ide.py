"""nb_ide: the Hindawi IDE inside a notebook. ide("urdu") shows it: a language, a shaili (C, C++, Python, Java, BASIC, Lex,
Yacc, assembly), the GATE syllabus and introductory programs by section, an editor, input and output, and the buttons
Build and run, Stages, Host program, From English, New, Upload and Download. Everything runs through hin and BURP.
© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI."""
import os, subprocess, sys, tempfile
from pathlib import Path

H = Path(os.environ.get("HINDAWI_HOME") or Path(__file__).resolve().parents[3])
SHAILIS = [("C", ".c"), ("C++", ".cpp"), ("Python", ".py"), ("Java", ".java"), ("BASIC", ".bas"), ("Lex", ".l"), ("Yacc", ".y"), ("Assembly", ".s")]
GIVEN = {".l": "one two three\nfour five\n", ".y": "2+3*4\n10*10+1\n"}


def languages():
    """Every language ready to compile, from the readiness record."""
    import json
    f = H / "docs/hindawi/data/readiness.json"
    if f.exists():
        return sorted(k for k, v in json.loads(f.read_text(encoding="utf-8"))["languages"].items() if v.get("ready_to_compile"))
    return ["urdu"]


def programs(lang, ext):
    """{section: [path, ...]}: the language's own gallery (the GATE syllabus), then the shaili samples in English."""
    out = {}
    for base in (H / "docs/hindawi/samples" / lang, H / "samples/gate"):
        if base.exists():
            for f in sorted(base.rglob("*" + ext)):
                out.setdefault(str(f.parent.relative_to(base)).replace("_", " "), []).append(f)
        if out:
            break
    for f in sorted((H / "samples/shailis").glob("*" + ext)):
        out.setdefault("shaili samples", []).append(f)
    return out


def hin(*args, given=""):
    r = subprocess.run([sys.executable, str(H / "bin/hin"), *map(str, args)], input=given, capture_output=True, text=True, timeout=300)
    return (r.stdout + ("\n" + r.stderr if r.returncode and r.stderr else "")).strip()


def from_english(text, ext, lang):
    with tempfile.TemporaryDirectory() as d:
        src = Path(d) / "in"; src.mkdir(); (src / ("program" + ext)).write_text(text, encoding="utf-8")
        subprocess.run([sys.executable, str(H / "lang/hindawi/burp/burp.py"), "ingest", str(src), "--langs", lang, "--out", str(Path(d) / "out"),
                        "--translators", "glossary"], capture_output=True)
        f = Path(d) / "out" / lang / ("program" + ext)
        return f.read_text(encoding="utf-8") if f.exists() else text


def ide(lang="urdu"):
    import ipywidgets as w
    from IPython.display import display, FileLink
    langs = languages()
    L = w.Dropdown(options=langs, value=lang if lang in langs else langs[0], description="Language")
    S = w.ToggleButtons(options=[(t, e) for t, e in SHAILIS], value=".c")
    sec = w.Dropdown(description="Section"); prog = w.Dropdown(description="Program", layout=w.Layout(width="420px"))
    ed = w.Textarea(layout=w.Layout(width="99%", height="340px"))
    given = w.Textarea(placeholder="input for the program", layout=w.Layout(width="49%", height="110px"))
    shown = w.Textarea(placeholder="output", layout=w.Layout(width="49%", height="110px"))
    view = w.Output(layout=w.Layout(width="99%", border="1px solid #bbb"))
    up = w.FileUpload(multiple=False, description="Upload"); cur = {}

    def tmp():
        f = Path(tempfile.gettempdir()) / ("hindawi_program" + S.value)
        if S.value == ".java" and prog.value:
            f = Path(tempfile.gettempdir()) / Path(str(prog.value)).name
        f.write_text(ed.value, encoding="utf-8"); return f

    def fill(*_):
        cur.clear(); cur.update(programs(L.value, S.value)); sec.options = list(cur) or ["(none yet)"]; pick()

    def pick(*_):
        prog.options = [(p.name, p) for p in cur.get(sec.value, [])]
        load()

    def load(*_):
        if prog.value:
            t = Path(prog.value).read_text(encoding="utf-8")
            if (H / "samples") in Path(prog.value).parents:     # an English program: brought into the language as it opens
                t = from_english(t, S.value, L.value)
            ed.value = t; given.value = GIVEN.get(S.value, ""); shown.value = ""

    def act(f):
        def h(_):
            shown.value = "working ..."
            try:
                f()
            except Exception as e:                       # a button never leaves a trace of Python behind it
                shown.value = f"{type(e).__name__}: {e}"
        return h

    def run_():
        shown.value = hin("run", L.value, tmp(), given=given.value) or "(no output)"

    def stages_():
        view.clear_output()
        with view:
            print(hin("stages", L.value, tmp()))
        shown.value = "the stages are shown below"

    def host_():
        shown.value = hin("host", L.value, tmp())

    def english_():
        ed.value = from_english(ed.value, S.value, L.value); shown.value = f"brought into {L.value}"

    def new_():
        ed.value = given.value = shown.value = ""; view.clear_output()

    def download_():
        f = Path("program" + S.value); f.write_text(ed.value, encoding="utf-8")
        if "google.colab" in sys.modules:
            from google.colab import files; files.download(str(f))
        else:
            with view:
                display(FileLink(str(f)))
        shown.value = f"saved as {f}"

    def upload_(c):
        v = up.value
        for item in (v if isinstance(v, (list, tuple)) else v.values()):
            ed.value = bytes(item["content"]).decode("utf-8", "replace")

    L.observe(fill, "value"); S.observe(fill, "value"); sec.observe(pick, "value"); prog.observe(load, "value"); up.observe(upload_, "value")
    acts = [("▶ Build and run", run_), ("Stages", stages_), ("Host program", host_), ("From English", english_), ("New", new_), ("Download", download_)]
    bar = w.HBox([w.Button(description=n, layout=w.Layout(width="auto"), button_style="success" if i == 0 else "") for i, (n, _) in enumerate(acts)] + [up])
    for b, (_, f) in zip(bar.children, acts):
        b.on_click(act(f))
    fill()
    display(w.VBox([w.HBox([L]), S, w.HBox([sec, prog]), bar, ed, w.HBox([given, shown]), view]))
