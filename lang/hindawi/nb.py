# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""nb.py: Hindawi in a notebook, after Chintamani's Hindawi NB UI (Notebooks/हिंदवी_2022_8_स्मरण_पुस्तिका.ipynb).

    import sys; sys.path.insert(0, REPO + "/lang/hindawi"); import nb
    nb.ide("urdu")                          the practice area: demos, program, input, output, and the buttons
    nb.build_and_run(src, "urdu", "guru")   compile a C program written in Urdu and run it
    nb.show_stages(src, "urdu", "guru")     every stage: source, script filter, Romenagri, the host language

Every program goes through the original pipeline (script filter, Romenagri, the language's transducer) before gcc or
Python sees it; nothing here compiles Unicode directly.
"""
import os, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(os.environ.get("HINDAWI_REPO") or Path(__file__).resolve().parents[2])
RMN = ROOT / ".build/chintamani/Romenagri"
os.environ["PATH"] = f"{RMN}{os.pathsep}{os.environ.get('PATH', '')}"
os.environ.setdefault("ROMENAGRI", str(RMN))
sys.path.insert(0, str(ROOT / "lang/hindawi/tools")); sys.path.insert(0, str(ROOT / "lang/hindawi/burp"))
import hindawi_chain  # noqa: E402

SHAILI = {"guru": ("C", ".c", "h2c"), "soochee": ("Python", ".py", "h2py")}
WORK = Path(tempfile.mkdtemp(prefix="hindawi-nb-"))
DEMOS_C = ["algorithms/searching/binary_search.c", "algorithms/sorting/quick_sort.c", "algorithms/sorting/merge_sort.c",
           "algorithms/dynamic_programming/longest_common_subsequence.c", "algorithms/graphs/breadth_first_search.c",
           "algorithms/graphs/dijkstra.c", "data_structures/stack.c", "data_structures/linked_list.c",
           "programming/recursion_fibonacci.c", "discrete_mathematics/sieve_of_eratosthenes.c",
           "operating_systems/round_robin.c", "computer_networks/crc32.c"]
DEMOS_PY = ["paradigms/binary_search.py"]


def stages(source, lang, shaili="guru"):
    """[(name, text)]: the source, the script filter's Devanagari (scripts with a filter), the Romenagri form, the host text."""
    return hindawi_chain.stages(source, lang, SHAILI[shaili][2])


def to_host(source, lang, shaili="guru"):
    """Hin2Std: the host-language text the pipeline gives (the last stage)."""
    return stages(source, lang, shaili)[-1][1]


def from_host(host_source, lang, shaili="guru"):
    """Std2Hin: a host-language program written in the language, by BURP's ingestion."""
    d = Path(tempfile.mkdtemp(dir=WORK)); (d / "src").mkdir()
    (d / "src" / f"program{SHAILI[shaili][1]}").write_text(host_source, encoding="utf-8")
    subprocess.run([sys.executable, str(ROOT / "lang/hindawi/burp/burp.py"), "ingest", str(d / "src"), "--langs", lang,
                    "--out", str(d / "n")], capture_output=True, check=True)
    return (d / "n" / lang / f"program{SHAILI[shaili][1]}").read_text(encoding="utf-8")


def build(source, lang, shaili="guru"):
    """(ok, messages, artefact): for C, a binary compiled by gcc from the pipeline's C; for Python, the Python text."""
    try:
        host = to_host(source, lang, shaili)
    except SystemExit as e:
        return False, str(e), None
    if shaili == "soochee":
        try:
            compile(host, "<hindawi>", "exec")
        except SyntaxError as e:
            return False, f"Python: {e}", None
        return True, "Python ready", host
    d = Path(tempfile.mkdtemp(dir=WORK)); c, exe = d / "program.c", d / "hin.exe"
    c.write_text(host, encoding="utf-8")
    r = subprocess.run(["gcc", "-O2", "-o", str(exe), str(c), "-lm"], capture_output=True, text=True)
    return r.returncode == 0, (r.stderr.strip() or f"compiled: {exe}"), (exe if r.returncode == 0 else None)


def run(artefact, shaili="guru", stdin=""):
    """The program's output, given its input."""
    cmd = [sys.executable, "-c", artefact] if shaili == "soochee" else [str(artefact)]
    r = subprocess.run(cmd, input=stdin, capture_output=True, text=True, timeout=20)
    return r.stdout + (r.stderr if r.returncode else "")


def build_and_run(source, lang, shaili="guru", stdin=""):
    ok, msg, art = build(source, lang, shaili)
    if not ok:
        print(msg); return None
    out = run(art, shaili, stdin); print(out, end=""); return out


def show_stages(source, lang, shaili="guru"):
    for name, text in stages(source, lang, shaili):
        print(f"===== {name}\n{text.rstrip()}\n")


def demos(lang, shaili="guru"):
    """{name: source}: the GATE programs as the language writes them, from the site's gallery or, where the gallery has
    none for this language, ingested now from the English originals by BURP."""
    names = DEMOS_C if shaili == "guru" else DEMOS_PY
    gallery = ROOT / "docs/hindawi/samples" / lang
    out = {}
    for n in names:
        g = gallery / n
        if g.exists():
            out[Path(n).stem] = g.read_text(encoding="utf-8")
        else:
            out[Path(n).stem] = from_host((ROOT / "samples/gate" / n).read_text(encoding="utf-8"), lang, shaili)
    return out


def ide(lang, shailis=("guru", "soochee")):
    """The practice area, after Chintamani's Hindawi NB UI: choose a shaili and a demo, edit, Build and Run, see every
    stage, convert to and from the host language, start anew, upload and download."""
    import ipywidgets as W
    from IPython.display import display
    mono = W.Layout(width="98%", height="300px")
    shaili = W.Dropdown(options=[(f"{SHAILI[s][0]} (shaili {s})", s) for s in shailis], description="Shaili")
    demo = W.Dropdown(description="Demo")
    program = W.Textarea(layout=mono, placeholder="program")
    stdin = W.Textarea(layout=W.Layout(width="48%", height="120px"), placeholder="input")
    output = W.Textarea(layout=W.Layout(width="48%", height="120px"), placeholder="output")
    flow = W.Output(layout=W.Layout(width="98%"))
    state = {"art": None, "demos": {}}

    def load_demos(_=None):
        state["demos"] = demos(lang, shaili.value)
        demo.options = list(state["demos"])
        if demo.options:
            demo.value = demo.options[0]; program.value = state["demos"][demo.value]

    def pick(_=None):
        if demo.value:
            program.value = state["demos"][demo.value]; state["art"] = None

    def do_build(_=None):
        ok, msg, art = build(program.value, lang, shaili.value); state["art"] = art
        output.value = msg if not ok else msg + "\n" + run(art, shaili.value, stdin.value)

    def do_run(_=None):
        output.value = run(state["art"], shaili.value, stdin.value) if state["art"] else "Build first."

    def do_stages(_=None):
        flow.clear_output()
        with flow:
            show_stages(program.value, lang, shaili.value)

    def do_to_host(_=None):
        program.value = to_host(program.value, lang, shaili.value)

    def do_from_host(_=None):
        program.value = from_host(program.value, lang, shaili.value)

    def do_new(_=None):
        program.value = stdin.value = output.value = ""; state["art"] = None; flow.clear_output()

    upload = W.FileUpload(description="Upload", accept=".c,.py,.uhin,.txt", multiple=False)

    def do_upload(change):
        v = change["new"]
        items = list(v.values()) if isinstance(v, dict) else list(v)
        if items:
            program.value = bytes(items[0]["content"]).decode("utf-8", "replace")

    def do_download(_=None):
        f = Path.cwd() / f"hindawi-{lang}{SHAILI[shaili.value][1]}"
        f.write_text(program.value, encoding="utf-8")
        try:
            from google.colab import files
            files.download(str(f))
        except ImportError:
            output.value = f"saved: {f}"

    buttons = []
    for label, fn in (("Build and run", do_build), ("Run", do_run), ("Stages", do_stages),
                      ("To host (Hin2Std)", do_to_host), ("From host (Std2Hin)", do_from_host), ("New", do_new),
                      ("Download", do_download)):
        b = W.Button(description=label); b.on_click(fn); buttons.append(b)
    shaili.observe(load_demos, "value"); demo.observe(pick, "value"); upload.observe(do_upload, "value")
    load_demos()
    display(W.VBox([W.HBox([shaili, demo]), W.HBox(buttons + [upload]), program, W.HBox([stdin, output]), flow]))
