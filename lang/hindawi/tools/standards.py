#!/usr/bin/env python3
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""standards.py: the language standards. For each language, one document that defines its programming-language
bindings (a C, a C++, a Java, a Python, a BASIC, a LOGO, and the C preprocessor, written in that language and script)
and how each is lowered to the host language's own standard. The document follows the structure standards bodies use
(scope, normative references, terms, conformance, requirements, normative annexes, bibliography), cites every host
standard by reference only and reproduces none of its text, and records where each word came from.

  python3 lang/hindawi/tools/standards.py [--langs L]      writes standards/<lang>/standard.json and standard.md
  node lang/hindawi/tools/standards_docx.js [standards]      writes standard.docx beside each, from the JSON

The document's metadata (copyright, rights statement, edition) is in standards/config.json.
"""
import argparse, json, sys, unicodedata
from datetime import date
from pathlib import Path

R = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(R / "lang/hindawi/burp")); sys.path.insert(0, str(R / "lang/hindawi/tools"))
import burp, coverage, script_filters  # noqa: E402

OUT = R / "standards"
CONFIG = {
    "edition": "2026.10",
    "stage": "Working draft",
    "copyright": "© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.",
    "rights": ("This document is an original work. It defines new programming languages by reference to the host language "
               "standards listed in Clause 2 and reproduces no text from them. Permission to adopt, translate or publish it "
               "as a standard is given by the copyright holder to a standards body on request."),
    "publisher": "AyeAI, Hindawi project (Project ILM)",
}
# The paradigm bindings: host, its normative reference (cited, never quoted), and how its identifiers are lowered.
BINDINGS = [
    ("C", ["c2h"], "ISO/IEC 9899, Information technology, Programming languages, C", "name transformation"),
    ("C preprocessor", ["c2h"], "ISO/IEC 9899, Information technology, Programming languages, C (preprocessing directives)", "name transformation"),
    ("C++", ["cpp2h"], "ISO/IEC 14882, Programming languages, C++", "name transformation"),
    ("Java", ["java2h"], "The Java Language Specification, Oracle, current edition", "unchanged"),
    ("Python", ["py2h"], "The Python Language Reference, Python Software Foundation, current version", "unchanged"),
    ("BASIC", ["b2h"], "ISO/IEC 10279, Information technology, Programming languages, Full BASIC", "name transformation"),
    ("LOGO", ["logo2h"], "No international standard; the host is the Berkeley Logo dialect (bibliography)", "name transformation"),
]
UNICODE_REFS = ["ISO/IEC 10646, Information technology, Universal coded character set (UCS)",
                "Unicode Standard Annex #15, Unicode normalization forms",
                "Unicode Standard Annex #31, Unicode identifiers and syntax"]
RTL = {"ARABIC", "HEBREW", "SYRIAC", "SAMARITAN", "MANDAIC", "NKO", "THAANA"}


def provenance(lang):
    data = json.loads((R / "docs/hindawi/data/standards.json").read_text(encoding="utf-8"))
    return data.get("languages", {}).get(lang, {}).get("provenance", {})


def compile_status(lang):
    t = R / "docs/hindawi/burp-status.tsv"
    for line in t.read_text(encoding="utf-8").splitlines()[1:] if t.exists() else []:
        f = line.split("\t")
        if f[0] == lang:
            return f[3] if len(f) > 3 else ""
    return ""


def status_word(p):
    if p == "legacy":
        return "Chintamani"
    if p == "lexicon":
        return "lexicon"
    if p.startswith("proposed"):
        return "proposed"
    if p.startswith("machine"):
        return "machine-translated"
    return p or "lexicon"


def model(lang):
    script = script_filters.script_of_language(lang)
    name = lang.replace("_", " ").title()
    code = burp.ISO.get(lang, lang)
    prov = provenance(lang)
    today = date.today().isoformat()
    B = []                                               # the document as blocks: h1, h2, p, list, table
    h1 = lambda t: B.append({"type": "h1", "text": t})
    h2 = lambda t: B.append({"type": "h2", "text": t})
    p = lambda t: B.append({"type": "p", "text": t})
    li = lambda items: B.append({"type": "list", "items": items})
    tables, counts = [], []
    for title, rev, ref, ids in BINDINGS:
        table = burp.keyword_table(lang, rev)
        host_words = coverage.PARADIGM_WORDS[title][1]
        rows = []
        for host in host_words:
            native = table.get(host) or table.get(host.lower())
            src = "Chintamani" if lang == "hindi" and native else status_word(prov.get(host, "")) if native else ""
            rows.append([host, native or host, src if native else "host form (no native word yet)"])
        extra = [] if title == "C preprocessor" else sorted(          # directives are their own binding
            k for k in table if k not in host_words and k.lower() not in host_words and not k.startswith("#"))
        lib = [[k, table[k], "Chintamani" if lang == "hindi" else status_word(prov.get(k, ""))] for k in extra]
        have = sum(1 for r in rows if r[1] != r[0])
        counts.append((title, have, len(rows), len(lib)))
        tables.append((title, ref, ids, rows, lib))
    meta = {"language": name, "code": code, "script": script.title(), "direction": "right to left" if script in RTL else "left to right",
            "edition": CONFIG["edition"], "stage": CONFIG["stage"], "date": today, "copyright": CONFIG["copyright"],
            "identifier": f"HLS {code} {CONFIG['edition']}", "publisher": CONFIG["publisher"],
            "title": f"{name} bindings for programming languages: lexical mapping and lowering to the host standards",
            "compilation": compile_status(lang)}

    h1("Foreword")
    p(f"This document was prepared by {CONFIG['publisher']}. It is generated from the {name} cell of Hindawi "
      f"{CONFIG['edition']} by lang/hindawi/tools/standards.py, so that the published standard and the reference "
      "implementation cannot drift apart. Its stage is a working draft: the words marked proposed in Annex A await "
      f"review by the {name} language community, through the review pages of the Hindawi project.")
    h1("Introduction")
    p(f"This document lets programs be written in {name}, in the {script.title()} script, in each of the programming "
      f"languages listed in Clause 1. Each binding is a programming language in its own right, {name} C for example, "
      "whose programs are lowered by the function defined in Clause 6 to programs of the host language, and are then "
      "processed by any conforming implementation of the host standard. The host standards are incorporated by reference "
      "and are not restated. Names keep a defined form down to object code (Clause 7), so programs written in "
      f"{name} remain debuggable at the level of firmware, kernels and libraries.")
    h1("1 Scope")
    p(f"This document specifies, for the {name} language written in the {script.title()} script, bindings to the "
      "following host programming languages: " + ", ".join(t for t, *_ in BINDINGS) + ". For each binding it specifies "
      "the native keywords and directives, the lowering of native programs to host programs, the treatment of names, "
      "and the requirements for conformance.")
    p("It does not specify the syntax or semantics of any host language beyond what is needed to define the lowering, "
      "and it does not specify translations of comments, string literals or documentation.")
    h1("2 Normative references")
    p("The following documents are referred to in the text in such a way that some or all of their content constitutes "
      "requirements of this document. For undated references, the latest edition of the referenced document (including "
      "any amendments) applies.")
    li(list(dict.fromkeys(ref.split(" (")[0] for _, _, ref, _ in BINDINGS if not ref.startswith("No international"))) + UNICODE_REFS)
    h1("3 Terms and definitions")
    for term, d in [
        ("host language", "programming language defined by a normative reference, to which a native program is lowered"),
        ("binding", f"programming language defined by this document whose programs are written in {name} and lowered to one host language"),
        ("native keyword", "word of this document that stands for one keyword, directive or standard library name of a host language"),
        ("lowering", "function from native programs to host programs defined in Clause 6"),
        ("raising", "inverse of lowering applied to a host program with a dictionary of names, giving back the native program exactly"),
        ("name transformation", "function from native names to host identifiers defined in Clause 7"),
        ("C-level form", "result of the name transformation; the form a native name takes in host source and in object code")]:
        li([f"{term}: {d}"])
    h1("4 Conformance")
    p(f"A conforming {name} program of a binding shall be a text that meets Clause 5 and whose lowering is a conforming "
      "program of the host language.")
    p("A conforming implementation of a binding shall accept every conforming program of that binding and shall behave "
      "as the lowering of the program, processed by a conforming implementation of the host language, behaves.")
    p("An implementation that raises host programs into a binding shall produce native programs whose lowering, with "
      "the same dictionary of names, is identical to the host program it raised.")
    h1("5 Character set and encoding")
    p(f"A native program shall be encoded in UTF-8 and shall be in Normalization Form C. Native keywords and names are "
      f"written in the {script.title()} script, whose direction is {meta['direction']}. Numeric literals are written "
      "with the digits 0 to 9 (U+0030 to U+0039). A native keyword written as several words is one token, its words "
      "joined by LOW LINE (U+005F).")
    h1("6 Lowering")
    p("A native program is lowered by the following steps, applied in order to the tokens the host language's lexical "
      "rules yield when the letters and marks of the script are treated as identifier characters.")
    li(["Each native keyword of the binding's table in Annex A is replaced by the host keyword, directive or name it stands for.",
        "A host keyword for which Annex A gives no native word is written in its host form.",
        "Every other name is lowered as the binding requires: by the name transformation of Clause 7 for C, the C "
        "preprocessor, C++, BASIC and LOGO; unchanged for Java and Python, whose host standards accept such names.",
        "String literals, character constants, header names in include directives, and comments are not changed.",
        "Every other character is not changed."])
    h1("7 Name transformation")
    p("The C-level form of a native name is obtained by passing the name, alone, through the script filter of the "
      "script (Annex C), then through the Romenagri transliteration (uni2acii followed by acii2cf), and writing each "
      "circumflex accent (U+005E) that results as LOW LINE (U+005F). Names already written in the digits, Latin "
      "letters and LOW LINE of the Basic Latin block are not transformed.")
    p("Two names declared in the same scope shall not have the same C-level form.")
    h1("8 Reference implementation")
    p(f"Hindawi {CONFIG['edition']} is the reference implementation: hindawicc lowers and compiles, BURP raises and "
      "lowers projects, and the Romenagri tools of Chintamani at commit 3ad87785a75dc2b18438a8b068807103cb920c81 give "
      "the name transformation. Where this document and the reference implementation differ, this document governs.")
    h1("Annex A (normative) Native keywords")
    for title, ref, ids, rows, lib in tables:
        h2(f"A.{len([b for b in B if b['type'] == 'h2']) + 1} {title}")
        p(f"Host: {ref}. Names: {ids}.")
        B.append({"type": "table", "head": ["Host", name, "Source"], "rows": rows})
        if lib:
            p(f"Standard library and runtime names of the {title} binding:")
            B.append({"type": "table", "head": ["Host", name, "Source"], "rows": lib})
    h1("Annex B (informative) Coverage and review")
    B.append({"type": "table", "head": ["Binding", "Host keywords with a native word", "Library names"],
              "rows": [[t, f"{h} of {n}", str(l)] for t, h, n, l in counts]})
    p(f"The lowering of {name} programs to C is verified by the reference implementation: {meta['compilation'] or 'not yet measured'}. "
      "Source Chintamani means a word of the original Hindawi transducers; lexicon, a word of the language's lexicon; "
      "proposed, a word proposed by the project and not yet reviewed by the language community.")
    h1("Annex C (normative) Script filter")
    folds = [[a, b] for a, b in sorted(script_filters.FOLD_PAIRS.items())] if script == "ARABIC" else []
    if script == "DEVANAGARI":
        p("Devanagari text passes to Romenagri without a script filter.")
    elif script in ("ARABIC", "TELUGU"):
        p(f"The script filter is Chintamani's own ({script_filters.ORIGINAL.get(script)}).")
    else:
        p("The script filter maps each letter and sign of the script to the Devanagari letter or sign of the same Unicode "
          "name, as generated by lang/hindawi/tools/script_filters.py.")
    if folds:
        p("Before the filter, these letters are written as the letters that follow them:")
        B.append({"type": "table", "head": ["Letter", "Written as"], "rows": folds})
    h1("Annex D (informative) Rights and provenance")
    p(CONFIG["rights"])
    p("Single words and the keywords of the host languages are not reproduced from any copyrighted text; the native "
      "words of Annex A were chosen by the Hindawi project, taken from the language's lexicon in the Hindawi "
      "repository, or, for Hindi, taken from the Chintamani transducers of the original Hindawi, whose author holds "
      "their copyright.")
    h1("Bibliography")
    li(["Hindawi 2026.10, hindawiai/hindawi2026.10, the reference implementation",
        "Chintamani, hindawiai/chintamani, the Hindawi transducers and the Romenagri tools",
        "Berkeley Logo reference manual, Brian Harvey"])
    return {"meta": meta, "blocks": B}


def markdown(m):
    md = [f"# {m['meta']['identifier']}", "", f"**{m['meta']['title']}**", "",
          f"Edition {m['meta']['edition']}, {m['meta']['stage'].lower()}, {m['meta']['date']}. {m['meta']['copyright']}", ""]
    for b in m["blocks"]:
        if b["type"] == "h1":
            md += [f"## {b['text']}", ""]
        elif b["type"] == "h2":
            md += [f"### {b['text']}", ""]
        elif b["type"] == "p":
            md += [b["text"], ""]
        elif b["type"] == "list":
            md += [f"- {i}" for i in b["items"]] + [""]
        elif b["type"] == "table":
            md += ["| " + " | ".join(b["head"]) + " |", "|" + "---|" * len(b["head"])]
            md += ["| " + " | ".join(str(c).replace("|", "\\|") for c in r) + " |" for r in b["rows"]] + [""]
    return "\n".join(md)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--langs", default="all")
    a = ap.parse_args()
    cfg = OUT / "config.json"
    if cfg.exists():
        CONFIG.update(json.loads(cfg.read_text(encoding="utf-8")))
    else:
        OUT.mkdir(exist_ok=True); cfg.write_text(json.dumps(CONFIG, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    langs = burp.languages(a.langs)
    index = []
    for lang in langs:
        m = model(lang)
        d = OUT / lang; d.mkdir(parents=True, exist_ok=True)
        (d / "standard.json").write_text(json.dumps(m, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        (d / "standard.md").write_text(markdown(m) + "\n", encoding="utf-8")
        cov = next(b for b in m["blocks"] if b["type"] == "table" and b["head"][0] == "Binding")["rows"]
        index.append({"lang": lang, "language": m["meta"]["language"], "script": m["meta"]["script"],
                      "identifier": m["meta"]["identifier"], "coverage": cov, "compilation": m["meta"]["compilation"]})
    if a.langs == "all":
        (OUT / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"standards: {len(langs)} standards written to {OUT.relative_to(R)}/")


if __name__ == "__main__":
    main()
