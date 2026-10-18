#!/usr/bin/env python3
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""check_standards_register.py: the checks for the standards, the review data, the trademark and credit documents, the
task register and its work packages, and the visible compilation stages. Every check names what it protects."""
import json, os, re, shutil, sys
from pathlib import Path

R = Path(__file__).resolve().parents[1]
FAILED, PASSED = [], 0


def check(name, ok, detail=""):
    global PASSED
    if ok:
        PASSED += 1
        print(f"  PASS  {name}")
    else:
        FAILED.append(name)
        print(f"  FAIL  {name}" + (f": {detail}" if detail else ""))


CLAUSES = ["## Foreword", "## Introduction", "## 1 Scope", "## 2 Normative references", "## 3 Terms and definitions",
           "## 4 Abbreviated terms", "## 5 Conformance", "## 6 Source text", "## 7 Lexical structure", "## 8 Lowering",
           "## 9 Name transformation", "## 10 Reversal", "## 11 Maintenance of the bindings",
           "## Annex A (normative) Keyword bindings", "## Annex B (normative) Name transformation test vectors",
           "## Annex C (normative) Script filter", "## Annex D (informative) Library names",
           "## Annex E (informative) Conformance tests", "## Annex F (informative) Provenance of the bindings", "## Bibliography"]
C_IDENT = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")

print("== standards: drafted only where the bindings are complete, and complete where drafted")
index = json.loads((R / "standards/index.json").read_text(encoding="utf-8"))
drafted = [x for x in index if x["status"] == "draft proposal"]
check("at least one language is drafted", len(drafted) >= 1, f"{len(drafted)} drafted")
for x in drafted:
    d = R / "standards" / x["lang"]
    md = (d / "standard.md").read_text(encoding="utf-8") if (d / "standard.md").exists() else ""
    check(f"{x['lang']}: Markdown, JSON and Word files exist", all((d / f).exists() for f in ("standard.md", "standard.json", "standard.docx")))
    missing = [c for c in CLAUSES if c not in md]
    check(f"{x['lang']}: every clause and annex is present", not missing, ", ".join(missing))
    annex_a = md.split("## Annex A (normative) Keyword bindings")[1].split("## Annex B")[0] if "## Annex A" in md else ""
    empty = [l for l in annex_a.splitlines() if l.startswith("| ") and re.match(r"^\| [^|]+ \|\s*\|", l)]
    check(f"{x['lang']}: Annex A binds every host keyword", not empty and "no native word yet" not in md, f"{len(empty)} unbound")
    annex_b = md.split("## Annex B (normative) Name transformation test vectors")[1].split("## Annex C")[0] if "## Annex B" in md else ""
    vec = [l.split("|")[2].strip() for l in annex_b.splitlines() if l.startswith("| ") and "---" not in l and "C-level form" not in l]
    check(f"{x['lang']}: Annex B has test vectors, each a C identifier", len(vec) >= 10 and all(C_IDENT.fullmatch(v) for v in vec),
          f"{len(vec)} vectors")
    check(f"{x['lang']}: the conformance annex cites a dated record", "Recorded on 20" in md)
for x in index:
    if x["status"] != "draft proposal":
        d = R / "standards" / x["lang"]
        check(f"{x['lang']}: no stub standard, and a work package instead",
              not (d / "standard.md").exists() and (R / x["work_package"]).exists())

print("== review data: one source, Hindi included, host keywords first")
st = json.loads((R / "docs/hindawi/data/standards.json").read_text(encoding="utf-8"))
hi = st["languages"].get("hindi", {}).get("words", {})
check("Hindi is on the review page with its words for if and break", bool(hi.get("if")) and bool(hi.get("break")))
bn = st["languages"].get("bengali", {}).get("words", {})
check("Bengali's words for if and break are keyed by the host keyword", bool(bn.get("if")) and bool(bn.get("break")))
check("the C paradigm lists host keywords before library names", st["constructs"]["guru"][0] in ("auto", "break", "case", "char", "if"),
      st["constructs"]["guru"][:3])
check("the retired keyword data is gone and no page reads it",
      not (R / "docs/hindawi/data/keywords.json").exists() and
      not any("data/keywords.json" in p.read_text(encoding="utf-8") for p in (R / "docs").rglob("*.html")))

print("== trademarks and credits")
tm = (R / "legal/TRADEMARKS.md").read_text(encoding="utf-8")
check("the three triad marks are asserted as registered in India", all(m in tm for m in ("AyeAI®", "AyeCNSe®", "AyeAM®")) and "India" in tm)
check("licences are stated not to license the marks", "grant permissions under copyright only" in tm)
check("credits are kept: the originator's credit is never removed", "never removed" in tm and (R / "CREDITS.md").exists())

print("== task register and work packages")
reg = json.loads((R / "work-packages/tasks.json").read_text(encoding="utf-8"))
check("every register entry has id, title, status and evidence", all({"id", "title", "status", "evidence"} <= set(t) for t in reg))
tasks_md = (R / "TASKS.md").read_text(encoding="utf-8")
check("TASKS.md lists every entry of the register", all(t["id"] in tasks_md for t in reg))
for t in reg:
    if t["status"] in ("open", "in progress"):
        wp = R / "work-packages/tasks" / f"WP-{t['id']}.md"
        check(f"{t['id']} has a work package carrying the originator's credit",
              wp.exists() and "Originator: Abhishek Choudhary" in wp.read_text(encoding="utf-8"))

print("== the compilation path shows every stage, and compiles what it shows")
rmn = R / ".build/chintamani/Romenagri"
if rmn.exists() and shutil.which("flex"):
    os.environ["PATH"] = f"{rmn}{os.pathsep}{os.environ['PATH']}"; os.environ.setdefault("ROMENAGRI", str(rmn))
    sys.path.insert(0, str(R / "lang/hindawi/tools"))
    import hindawi_chain as hc
    src = "صحیح مین(خالی) { واپس 0; }\n"
    st_ = hc.stages(src, "urdu")
    check("Urdu shows source, script filter, Romenagri and C", [n for n, _ in st_] == ["source", "script filter", "Romenagri", "C"])
    check("to_c is the last stage shown", hc.to_c(src, "urdu") == st_[-1][1] and "int" in st_[-1][1] and "return" in st_[-1][1])
else:
    print("  UNJUDGED  stages: the Romenagri tools are not built here (hindawi setup builds them)")

print(f"{PASSED} passed, {len(FAILED)} failed")
sys.exit(1 if FAILED else 0)
