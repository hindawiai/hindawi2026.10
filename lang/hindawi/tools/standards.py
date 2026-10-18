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


LITD = ("the Data Management System Sectional Committee, LITD 15, of the Bureau of Indian Standards, whose scope "
        "includes programming languages, their environments and system software interfaces")
COMPLETE_NOTE = "A standard is drafted only for a language whose keyword bindings are complete in every binding of Annex A."


def digits(script):
    """The native decimal digits of a script, from the Unicode Character Database: (code point, character, value)."""
    names = {"ARABIC": ("ARABIC-INDIC DIGIT", "EXTENDED ARABIC-INDIC DIGIT")}.get(script, (f"{script} DIGIT",))
    out = []
    for cp in range(0x0600, 0x1100):
        c = chr(cp); n = unicodedata.name(c, "")
        if unicodedata.category(c) == "Nd" and any(n.startswith(x + " ") for x in names):
            out.append((f"U+{cp:04X}", c, unicodedata.digit(c)))
    return out


def complete(lang):
    """True when every host keyword of every binding has a native word: the condition for drafting a standard."""
    for title, rev, _, _ in BINDINGS:
        table = {k.lower(): v for k, v in burp.keyword_table(lang, rev).items()}
        if any(h.lower() not in table for h in coverage.PARADIGM_WORDS[title][1]):
            return False
    return True


def test_vectors(lang, limit=30):
    """Annex B: native names from the language's GATE dictionary and the C-level form the reference implementation
    gives each, computed here, now, by the same function the compiler uses."""
    import hindawi_chain
    g = R / "docs/hindawi/samples" / lang / "dictionary.json"
    if not g.exists():
        return []
    names = json.loads(g.read_text(encoding="utf-8")).get("identifiers", {})
    natives = sorted({v for k, v in names.items() if v != k and len(k) > 2 and not v.isascii()})[:limit]
    try:
        forms = hindawi_chain.c_names(natives, lang)
    except SystemExit:
        return []
    return [[n, forms[n]] for n in natives if forms.get(n) and forms[n].isascii()]


def example(lang):
    """Annex E: one GATE program as the language writes it, its Romenagri form and its C, by the reference pipeline."""
    import hindawi_chain
    src = R / "docs/hindawi/samples" / lang / "algorithms/searching/binary_search.c"
    if not src.exists():
        return []
    try:
        return hindawi_chain.stages(src.read_text(encoding="utf-8"), lang)
    except SystemExit:
        return []


def model(lang):
    script = script_filters.script_of_language(lang)
    name = lang.replace("_", " ").title()
    code = burp.ISO.get(lang, lang)
    prov = provenance(lang)
    today = date.today().isoformat()
    B = []
    h1 = lambda t: B.append({"type": "h1", "text": t})
    h2 = lambda t: B.append({"type": "h2", "text": t})
    p = lambda t: B.append({"type": "p", "text": t})
    li = lambda items: B.append({"type": "list", "items": items})
    note = lambda t: B.append({"type": "note", "text": t})
    codeb = lambda t: B.append({"type": "code", "text": t})
    tables, counts, provcount = [], [], {}
    for title, rev, ref, ids in BINDINGS:
        table = burp.keyword_table(lang, rev)
        host_words = coverage.PARADIGM_WORDS[title][1]
        rows = []
        for host in host_words:
            native = table.get(host) or table.get(host.lower())
            src = "Chintamani" if lang == "hindi" else status_word(prov.get(host, ""))
            provcount[src] = provcount.get(src, 0) + 1
            rows.append([host, native, src])
        extra = [] if title == "C preprocessor" else sorted(
            k for k in table if k not in host_words and k.lower() not in host_words and not k.startswith("#"))
        lib = [[k, table[k], "Chintamani" if lang == "hindi" else status_word(prov.get(k, ""))] for k in extra]
        counts.append((title, len(rows), len(lib)))
        tables.append((title, ref, ids, rows, lib))
    ds = digits(script)
    gate = json.loads((R / "docs/hindawi/data/gate-results.json").read_text(encoding="utf-8")).get(lang, {}) \
        if (R / "docs/hindawi/data/gate-results.json").exists() else {}
    title = f"Information technology, Programming languages, {name} keyword bindings for C, C++, Java, Python, BASIC and LOGO, and their lowering to the host language standards"
    meta = {"language": name, "code": code, "script": script.title(), "direction": "right to left" if script in RTL else "left to right",
            "edition": CONFIG["edition"], "stage": "Draft proposal", "date": today, "copyright": CONFIG["copyright"],
            "identifier": f"HLS {code} {CONFIG['edition']}", "publisher": CONFIG["publisher"], "title": title,
            "compilation": compile_status(lang)}

    h1("Foreword")
    p(f"This draft is proposed by Abhishek Choudhary, AyeAI, for consideration by {LITD}. It is an indigenous draft: it "
      "adopts no International Standard, binds the language it names to the host programming language standards listed "
      "in Clause 2 by reference, and reproduces no text from them.")
    p(f"The method it standardizes was first published as the Hindawi Programming System on 15 August 2004, and has been "
      f"developed since through the Hindawi releases. This draft is generated from the {name} cell of Hindawi "
      f"{CONFIG['edition']} by lang/hindawi/tools/standards.py, so that the document and its reference implementation "
      "cannot diverge; a revision of either is a revision of both.")
    p("Annexes A, B and C are normative. Annexes D, E and F are informative.")
    p(f"Every binding in Annex A records its provenance. A binding recorded as proposed has not yet been reviewed by the "
      f"{name} language community; its review is part of the work towards an Indian Standard.")
    p(f"{CONFIG['copyright']} Hindawi™ and Romenagri™ are trademarks of Abhishek Choudhary. {CONFIG['rights']}")

    h1("Introduction")
    p("A program has three properties that this draft keeps apart: the script it is written in, the human language its "
      "words come from, and the programming language standard that defines its meaning. The script is handled by "
      "transliteration, the language by the keyword bindings of Annex A, and the meaning by the host standard, which this "
      "draft does not alter.")
    p("A source text in the language is lowered to a source text of the host language and compiled by any conforming host "
      "translator. Native names reach the compiled program, and the debugger, in one fixed transliterated form, so that a "
      "program written in the language remains readable in that language at every level down to the machine.")

    h1("1 Scope")
    p(f"This draft specifies, for programs written in {name} in the {script.title()} script:")
    li(["the encoding and character repertoire of source text (Clause 6);",
        "the lexical structure of source text, where it differs from the host language (Clause 7);",
        "the keyword bindings of the language for C, the C preprocessor, C++, Java, Python, BASIC and LOGO (Annex A);",
        "the lowering of a source text to a source text of the host language (Clause 8);",
        "the transformation of native names to identifiers of the host language (Clause 9, Annexes B and C);",
        "the requirements for conformance of programs and of translators (Clause 5)."])
    p("This draft does not specify the semantics of any host language, which remain those of its standard; the names of "
      "host libraries, which are informative (Annex D); or any execution environment.")

    h1("2 Normative references")
    p("The following documents are referred to in the text in such a way that some or all of their content constitutes "
      "requirements of this draft. For dated references, only the edition cited applies. For undated references, the "
      "latest edition of the referenced document, including any amendments, applies.")
    li([r for _, _, r, _ in BINDINGS if not r.startswith("No international")] + UNICODE_REFS + [
        "ISO/IEC 14977, Information technology, Syntactic metalanguage, Extended BNF",
        "IS 13194 : 1991, Indian Script Code for Information Interchange, ISCII"])

    h1("3 Terms and definitions")
    terms = [
        ("host language", "a programming language defined by a standard listed in Clause 2, into which a source text is lowered"),
        ("host keyword", "a reserved word or directive name of a host language"),
        ("native keyword", f"a word of {name}, written in the {script.title()} script, bound by Annex A to a host keyword"),
        ("binding", "the pairing of one host keyword with one native keyword, for one host language"),
        ("construct", "the programming construct a keyword denotes, which is the same across host languages, so that one native keyword serves it in every binding"),
        ("source text", f"a program, or part of one, written using native keywords, native names, or both"),
        ("native name", f"an identifier of a source text written wholly or partly in the {script.title()} script"),
        ("lowering", "the transformation of a source text into a source text of the host language"),
        ("C-level form", "the identifier of the host language that a native name becomes by name transformation, and under which it appears in compiled programs and to debuggers"),
        ("name transformation", "the mapping of native names to C-level forms specified in Clause 9"),
        ("script filter", f"the mapping of the {script.title()} script to Devanagari that precedes transliteration, specified in Annex C"),
        ("translator", "a program that performs lowering and name transformation"),
        ("reversal", "the transformation of a host-language source text into a source text of the language, through a dictionary of names kept with the program"),
        ("provenance", "the record of where a binding came from: the 2004 Hindawi transducers, a language lexicon, or a proposal awaiting review"),
    ]
    for i, (t, d) in enumerate(terms, 1):
        p(f"3.{i} {t}: {d}.")

    h1("4 Abbreviated terms")
    li(["ACII, the eight-bit form of Indic text used by the Romenagri tools, derived from ISCII",
        "BURP, Bidirectional Universal Resource Parser, the reference implementation of reversal",
        "EBNF, Extended Backus-Naur Form as specified in ISO/IEC 14977",
        "ISCII, Indian Script Code for Information Interchange, IS 13194",
        "NFC, Normalization Form C of Unicode Standard Annex #15",
        "UCS, the Universal Coded Character Set of ISO/IEC 10646"])

    h1("5 Conformance")
    p("5.1 A conforming program shall be a source text whose lowering according to Clause 8 is a program that conforms to "
      "the standard of its host language.")
    p("5.2 A conforming translator shall accept every conforming program, shall lower it as Clause 8 requires, using the "
      "bindings of Annex A, and shall transform its native names as Clause 9 requires, giving for every name in Annex B "
      "the C-level form that annex gives.")
    p("5.3 A claim of conformance shall name the bindings of Annex A it covers. A translator conforming for C covers the "
      "bindings of A.1 and A.2.")
    p("5.4 A translator that provides reversal shall reproduce the original host-language source text byte for byte from "
      "its lowering and the dictionary of names kept with it.")

    h1("6 Source text")
    p(f"6.1 Source text shall be encoded in UTF-8, as specified in ISO/IEC 10646, and shall be in Normalization Form C.")
    p(f"6.2 Native letters are the characters of the {script.title()} block of ISO/IEC 10646 whose general category is a "
      "letter or a mark. Text written right to left is stored in logical order.")
    p(f"6.3 The {script.title()} script is written {meta['direction']}.")
    if ds:
        p("6.4 The native digits below are equivalent, in numerals, to the decimal digits of the host language with the "
          "same value. A translator shall accept either.")
        B.append({"type": "table", "head": ["Code point", "Digit", "Value"], "rows": [[a, b, str(c)] for a, b, c in ds]})
    else:
        p("6.4 Numerals are written with the decimal digits of the host language.")

    h1("7 Lexical structure")
    p("7.1 The lexical structure of a source text is that of its host language, with the additions given below in the "
      "notation of ISO/IEC 14977.")
    codeb("native letter    = ? a character of 6.2 ? ;\n"
          "latin letter     = ? A to Z or a to z ? ;\n"
          "digit            = ? 0 to 9, or a native digit of 6.4 ? ;\n"
          "name start       = native letter | latin letter | \"_\" ;\n"
          "identifier       = name start , { name start | digit } ;\n"
          "native keyword   = ? an entry of the native column of Annex A ? ;\n"
          "directive        = \"#\" , ( native keyword | host keyword ) ;\n"
          "word             = native keyword | identifier ;")
    p("7.2 A native keyword is recognized only as a whole word. A word of which a native keyword is a proper part is an "
      "identifier.")
    p("7.3 Character literals, string literals and comments are those of the host language; their content may be written "
      "in any script and is not altered by lowering.")
    p("7.4 A host keyword written in its host form is accepted unchanged, so that a source text may mix native and host "
      "keywords.")

    h1("8 Lowering")
    p("8.1 Lowering shall replace each native keyword by the host keyword Annex A binds it to, for the host language of "
      "the source text; shall leave literals and comments unaltered; shall replace each native digit by the host digit of "
      "the same value; and shall transform each native name as Clause 9 requires.")
    p("8.2 Lowering shall not reorder, insert or remove any other token. The lowered text shall have the same line "
      "structure as the source text.")
    note("The reference implementation lowers in three steps: the script filter of Annex C, transliteration by the "
         "Romenagri tools, and the language's transducer for the host language, a lexical analyser built from the bindings "
         "of Annex A. Lowering is performed on the transliterated form; Unicode text is never compiled directly.")

    h1("9 Name transformation")
    p("9.1 Name transformation shall be deterministic, and shall give one native name the same C-level form wherever the "
      "name stands in a program.")
    p("9.2 Every C-level form shall be an identifier of the host language.")
    p("9.3 Two different native names of one program shall not be given the same C-level form; a translator shall report "
      "such a collision as an error.")
    p("9.4 A name written wholly in Latin letters, digits and underscores is not transformed.")
    p("9.5 The C-level forms of the names in Annex B are normative. They are those of the Romenagri transliteration "
      "applied, word by word, to the output of the script filter of Annex C.")

    h1("10 Reversal")
    p("Reversal is optional. A translator that provides it shall keep with each program a dictionary of its native names, "
      "and shall satisfy 5.4.")

    h1("11 Maintenance of the bindings")
    p(f"The bindings of Annex A are maintained as a living register. A proposed binding becomes reviewed when the {name} "
      "language community accepts it; a change to a reviewed binding is a revision of this draft. The construct, not the "
      "host keyword, is primary: one native keyword serves one construct in every binding where that construct occurs.")

    h1("Annex A (normative) Keyword bindings")
    for i, (t, ref, ids, rows, lib) in enumerate(tables, 1):
        h2(f"A.{i} {t}")
        p(f"Host standard: {ref}. Names are lowered by {ids}.")
        B.append({"type": "table", "head": ["Host keyword", name, "Provenance"], "rows": rows})

    h1("Annex B (normative) Name transformation test vectors")
    vec = test_vectors(lang)
    if vec:
        p("Each native name shall be given the C-level form shown. The vectors are computed by the reference implementation "
          "when this draft is generated.")
        B.append({"type": "table", "head": ["Native name", "C-level form"], "rows": vec})
    else:
        p("The test vectors are computed where the reference implementation is built; they were not computed for this edition.")

    h1("Annex C (normative) Script filter")
    filt = script_filters.which(lang)
    if script == "DEVANAGARI":
        p("Devanagari text needs no script filter: it is transliterated directly.")
    elif filt and ".build/chintamani" in str(filt):
        p(f"The {script.title()} script is mapped to Devanagari by the filter of the Hindawi tools for this script "
          f"({Path(str(filt)).name}), unchanged since its publication in Chintamani.")
    else:
        p(f"The {script.title()} script is mapped to Devanagari letter by letter, by Unicode character name: each letter "
          f"of the {script.title()} block maps to the Devanagari letter of the same name.")
    if script == "ARABIC":
        p("Letters of the Perso-Arabic orthographies that the filter does not distinguish are first folded to the nearest "
          "Urdu letter: " + ", ".join(f"{a} to {b}" for a, b in sorted(script_filters.FOLD_PAIRS.items())) + ".")
    if script == "GURMUKHI":
        p("Gurmukhi signs named differently from Devanagari are mapped by alias: bindi and tippi to anusvara, the vowel "
          "signs EE and OO to E and O. Addak has no Devanagari sign and is dropped.")

    h1("Annex D (informative) Library names")
    for t, ref, ids, rows, lib in tables:
        if lib:
            h2(f"D {t}")
            B.append({"type": "table", "head": ["Host name", name, "Provenance"], "rows": lib})

    h1("Annex E (informative) Conformance tests")
    if gate:
        p(f"The reference implementation is tested with the programs of samples/gate in the Hindawi repository, which "
          f"cover the programming content of the GATE Computer Science paper. Recorded on {gate['date']}: "
          f"{gate['c_ok']} of {gate['c_total']} C programs, written in {name}, were lowered, compiled and run, and printed "
          f"exactly what their English originals print; {gate['py_ok']} of {gate['py_total']} Python programs did the "
          f"same; {gate['reverse_ok']} of {gate['reverse_total']} files were reversed byte for byte.")
    st = example(lang)
    if st:
        p("The program below, as written in the language, its transliterated form, and the C that the transducer gives:")
        for nm, txt in st:
            h2(f"E {nm}")
            codeb("\n".join(txt.splitlines()[:16]))

    h1("Annex F (informative) Provenance of the bindings")
    B.append({"type": "table", "head": ["Provenance", "Bindings"], "rows": [[k, str(v)] for k, v in sorted(provcount.items())]})

    h1("Bibliography")
    li(["Hindawi Programming System, first public release 15 August 2004, savannah.nongnu.org/projects/hindawi",
        "Chintamani, hindawiai/chintamani: the Hindawi transducers and the Romenagri tools",
        "Hindawi 2026.10, hindawiai/hindawi2026.10, concept DOI 10.5281/zenodo.23424410",
        "IS 12 : 2005, Guide for drafting and presentation of Indian Standards",
        "ISO/IEC 10279, Information technology, Programming languages, Full BASIC",
        "Berkeley Logo reference manual, Brian Harvey"])
    return {"meta": meta, "blocks": [b for b in B if b]}


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
        elif b["type"] == "note":
            md += [f"NOTE: {b['text']}", ""]
        elif b["type"] == "code":
            md += ["```", b["text"], "```", ""]
        elif b["type"] == "list":
            md += [f"- {i}" for i in b["items"]] + [""]
        elif b["type"] == "table":
            md += ["| " + " | ".join(b["head"]) + " |", "|" + "---|" * len(b["head"])]
            md += ["| " + " | ".join(str(c).replace("|", "\\|") for c in r) + " |" for r in b["rows"]] + [""]
    return "\n".join(md)


REVIEW_SHAILI = {"guru": "C", "shraeni": "C++", "kritrima": "Java", "soochee": "Python", "praatha": "BASIC", "robot": "LOGO"}


def review_data():
    """The review page's data, made whole: Hindi added from Chintamani's own tables, and in every paradigm the host
    keywords listed first, then the library names, so a reviewer meets if and break before BUFSIZ."""
    f = R / "docs/hindawi/data/standards.json"
    d = json.loads(f.read_text(encoding="utf-8"))
    for shaili, toks in d["constructs"].items():
        kw = coverage.PARADIGM_WORDS.get(REVIEW_SHAILI.get(shaili, ""), (None, []))[1]
        first = [t for t in kw if t in toks] + [t for t in toks if t.startswith("#")]
        d["constructs"][shaili] = first + [t for t in toks if t not in first]
    words, prov = {}, {}
    for shaili, rev in (("guru", "c2h"), ("shraeni", "cpp2h"), ("kritrima", "java2h"), ("soochee", "py2h"),
                        ("praatha", "b2h"), ("robot", "logo2h"), ("wyaaka", "yacc2h"), ("shabda", "l2h"), ("yantra", "asm2h")):
        for k, v in burp.keyword_table("hindi", [rev]).items():
            words[k] = v; prov[k] = "legacy"
    d["languages"]["hindi"] = {"words": words, "provenance": prov}
    f.write_text(json.dumps(d, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")


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
    index, drafted = [], 0
    for lang in langs:
        d = OUT / lang
        if not complete(lang):
            # no stub: an incomplete language has a work package, not a standard
            for f in ("standard.json", "standard.md", "standard.docx"):
                (d / f).unlink(missing_ok=True)
            if d.exists() and not any(d.iterdir()):
                d.rmdir()
            index.append({"lang": lang, "status": "not drafted: keyword bindings incomplete",
                          "work_package": f"work-packages/languages/{lang}/"})
            continue
        m = model(lang)
        d.mkdir(parents=True, exist_ok=True)
        (d / "standard.json").write_text(json.dumps(m, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        (d / "standard.md").write_text(markdown(m) + "\n", encoding="utf-8")
        index.append({"lang": lang, "status": "draft proposal", "identifier": m["meta"]["identifier"],
                      "title": m["meta"]["title"], "compilation": m["meta"]["compilation"]})
        drafted += 1
    review_data()
    if a.langs == "all":
        (OUT / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"standards: {drafted} drafts written, {len(langs) - drafted} languages not drafted (bindings incomplete)")


if __name__ == "__main__":
    main()
