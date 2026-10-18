# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""colab.py: Hindawi in a notebook (Colab, Jupyter, JupyterLite with a kernel that can run gcc).

    import sys; sys.path.insert(0, REPO + "/lang/hindawi"); import colab

    %%hindawi_c urdu        a C program written in Urdu: compiled through the original pipeline and run
    %%hindawi_py telugu     Python written in Telugu: its keywords lowered, its names kept, and run in the notebook
    %%hindawi_show sindhi c English code shown in Sindhi (c or py), as BURP ingests it

"english" as the language runs the cell as it stands.
"""
import os, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(os.environ.get("HINDAWI_REPO") or Path(__file__).resolve().parents[2])
sys.path.insert(0, str(ROOT / "lang/hindawi/burp"))
import burp  # noqa: E402
from IPython.core.magic import register_cell_magic  # noqa: E402
from IPython import get_ipython  # noqa: E402


def _env(lang):
    return dict(os.environ, HINDAWI_LANG=lang, HINDAWI_NATIVE_SOURCE="1", ROMENAGRI=str(ROOT / ".build/chintamani/Romenagri"),
                PATH=str(ROOT / ".build/chintamani/Romenagri") + os.pathsep + os.environ.get("PATH", ""))


@register_cell_magic
def hindawi_c(line, cell):
    lang = (line.split() or ["english"])[0]
    d = Path(tempfile.mkdtemp(prefix="hindawi-")); src, exe = d / "program.c", d / "program"
    src.write_text(cell, encoding="utf-8")
    cc = ["gcc"] if lang == "english" else [str(ROOT / "lang/hindawi/hindawicc")]
    r = subprocess.run(cc + ["-O2", "-o", str(exe), str(src), "-lm"], capture_output=True, text=True, env=_env(lang))
    if r.returncode:
        print(r.stderr); return
    print(subprocess.run([str(exe)], capture_output=True, text=True).stdout, end="")


@register_cell_magic
def hindawi_py(line, cell):
    lang = (line.split() or ["english"])[0]
    if lang != "english":
        native = {v: k for k, v in burp.keyword_table(lang, ["py2h"]).items()}
        cell = burp.scanner("py").sub(lambda m: native.get(m.group(0), m.group(0)) if m.group("word") else m.group(0), cell)
    exec(compile(cell, f"<hindawi {lang}>", "exec"), get_ipython().user_ns)


@register_cell_magic
def hindawi_show(line, cell):
    lang, kind = (line.split() + ["urdu", "c"])[:2] if line.split() else ("urdu", "c")
    d = Path(tempfile.mkdtemp(prefix="hindawi-")); (d / "src").mkdir()
    (d / "src" / f"program.{kind}").write_text(cell, encoding="utf-8")
    subprocess.run([sys.executable, str(ROOT / "lang/hindawi/burp/burp.py"), "ingest", str(d / "src"), "--langs", lang, "--out", str(d / "n")],
                   capture_output=True)
    print((d / "n" / lang / f"program.{kind}").read_text(encoding="utf-8"))
