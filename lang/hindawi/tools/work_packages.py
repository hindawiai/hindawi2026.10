#!/usr/bin/env python3
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""work_packages.py: the work anyone, student or AI, can pick up, written out as packages under work-packages/.

  languages/<lang>/   the words a language still needs (keywords.tsv, names.tsv) and how to fill them
  gate/WP-GATE-nn.md  one GATE topic each, with its program contract and acceptance check
  js/WP-JS-nn.md      the move of the tooling to JavaScript, so setup becomes the browser
  index.json          every package, for docs/hindawi/work-packages.html, where each is claimed as a GitHub issue

  python3 lang/hindawi/tools/work_packages.py
"""
import json, re, sys, subprocess, tempfile, shutil
from pathlib import Path

R = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(R / "lang/hindawi/burp")); sys.path.insert(0, str(R / "lang/hindawi/tools"))
import burp, coverage  # noqa: E402

W = R / "work-packages"
REPO = "hindawiai/hindawi2026.10"
MEANING = {
    "auto": "automatic storage duration", "break": "leave the loop or switch", "case": "a branch of a switch",
    "char": "character type", "const": "read-only qualifier", "continue": "next iteration of the loop",
    "default": "the switch branch taken otherwise", "do": "loop whose test comes after its body", "double": "double-precision real type",
    "else": "otherwise", "enum": "enumeration type", "extern": "defined elsewhere", "float": "real type", "for": "counting loop",
    "goto": "jump to a label", "if": "if", "inline": "expand at the call", "int": "integer type", "long": "long integer type",
    "register": "keep in a register", "restrict": "the only pointer to its object", "return": "return from the function",
    "short": "short integer type", "signed": "signed integer type", "sizeof": "size of", "static": "static storage, or private to the file",
    "struct": "structure", "switch": "choose by value", "typedef": "name a type", "union": "union type", "unsigned": "unsigned integer type",
    "void": "no value", "volatile": "may change outside the program", "while": "loop while true", "main": "the program's entry function",
    "bool": "true-or-false type", "catch": "handle an exception", "class": "class", "delete": "free an object", "explicit": "no implicit conversion",
    "false": "false", "friend": "may see private members", "mutable": "changeable in a const object", "namespace": "a space of names",
    "new": "create an object", "nullptr": "the null pointer", "operator": "operator function", "private": "private", "protected": "protected",
    "public": "public", "template": "template", "this": "this object", "throw": "raise an exception", "true": "true", "try": "try",
    "typename": "a type name", "using": "use a name or namespace", "virtual": "overridable", "cout": "standard output stream",
    "cin": "standard input stream", "endl": "end of line", "abstract": "abstract", "assert": "assert", "boolean": "true-or-false type",
    "byte": "byte type", "extends": "derives from", "final": "cannot change or be overridden", "finally": "always run at the end",
    "implements": "implements an interface", "import": "bring in", "instanceof": "is an instance of", "interface": "interface",
    "native": "implemented outside Java", "package": "package", "super": "the parent class", "synchronized": "one thread at a time",
    "throws": "may raise", "null": "no object", "String": "text string type", "System": "the system class",
    "None": "no value", "True": "true", "False": "false", "and": "and", "as": "as", "def": "define a function", "del": "delete",
    "elif": "otherwise if", "except": "on exception", "from": "from", "global": "global", "in": "in", "is": "is the same object",
    "lambda": "anonymous function", "nonlocal": "from the enclosing function", "not": "not", "or": "or", "pass": "do nothing",
    "raise": "raise an exception", "with": "with a context", "yield": "yield a value", "print": "print", "range": "a range of numbers",
    "len": "length", "dim": "dimension an array", "end": "end", "gosub": "go to a subroutine", "input": "read input", "let": "let",
    "next": "next iteration", "rem": "remark (comment)", "step": "step size", "then": "then", "to": "to", "wend": "end of while",
    "mod": "remainder", "forward": "move forward", "back": "move back", "left": "turn left", "right": "turn right", "penup": "lift the pen",
    "pendown": "put the pen down", "repeat": "repeat", "make": "make a variable", "ifelse": "if, otherwise", "home": "go home",
    "clearscreen": "clear the screen", "#define": "define a macro", "#include": "include a header", "#if": "compile if",
    "#ifdef": "compile if defined", "#ifndef": "compile if not defined", "#else": "otherwise compile", "#elif": "otherwise compile if",
    "#endif": "end of conditional compilation", "#undef": "remove a macro", "#pragma": "implementation directive",
    "#error": "stop with an error", "#line": "set the line number"}


def languages():
    """The packages for each language not yet complete: its missing keywords and names, measured, not guessed."""
    lw = W / "languages"; shutil.rmtree(lw, ignore_errors=True); lw.mkdir(parents=True)
    names_all = [l.split("\t")[0] for l in (R / "lang/hindawi/burp/glossary/multi.tsv").read_text(encoding="utf-8").splitlines()
                 if l and not l.startswith("# ") and not l.startswith("english\t")]
    work = Path(tempfile.mkdtemp(prefix="wp-")); out = []
    for lang in burp.languages("all"):
        kw = coverage.keywords(lang)
        done, total, words, lib = coverage.gate_names(lang, work)
        missing_kw = [w for _, (_, _, miss) in kw.items() for w in miss]
        if not missing_kw and done == total and not lib:
            continue
        d = lw / lang; d.mkdir()
        table = {k: v for r in ("c2h", "cpp2h", "java2h", "py2h", "b2h", "logo2h") for k, v in burp.keyword_table(lang, [r]).items()}
        rows = ["token\tmeaning\tword"] + [f"{t}\t{MEANING.get(t, '')}\t" for t in dict.fromkeys(missing_kw + lib)]
        (d / "keywords.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
        nrows = ["english\tword"] + [f"{w}\t" for w in sorted(set(words) | set(names_all)) if len(w) > 1 and w.isalpha()]
        (d / "names.tsv").write_text("\n".join(nrows) + "\n", encoding="utf-8")
        name = lang.replace("_", " ").title()
        examples = ", ".join(f"{k} = {v}" for k, v in list(table.items())[:6])
        (d / "README.md").write_text(f"""# Work package: {name}

The {name} standard needs {len(set(missing_kw + lib))} keyword and library words and {len(nrows) - 1} name words.
Fill the empty `word` column of `keywords.tsv` and `names.tsv`, in {name} and its own script, then submit it with
`hindawi standard import {lang} keywords.tsv names.tsv --by "your name"`, or attach both files to an issue.

The rules: one word per line; a phrase is joined with underscores; a directive keeps its `#`; no word may be an
English keyword or repeat another word in the same file; use the word {name} speakers and teachers would use, not a
transliteration of the English unless that is what the community writes. Words already in the standard, for
reference: {examples}.

To have an AI fill it, give it both files and this instruction:

> Fill the empty word column of these two tab-separated files with {name} words in the script {name} is normally
> written in. keywords.tsv lists programming-language keywords with their meaning; names.tsv lists English words used
> as variable and function names in teaching programs. One word per line, a phrase joined with underscores, keep the
> # on directives, never an English keyword, no word used twice in one file. Return both files complete, as tab-separated text.
""", encoding="utf-8")
        out.append({"id": f"WP-LANG-{lang}", "kind": "language", "title": f"Complete the {name} standard",
                    "size": f"{len(set(missing_kw + lib))} keywords, {len(nrows) - 1} names", "path": f"work-packages/languages/{lang}/"})
    shutil.rmtree(work, ignore_errors=True)
    return out


GATE = [  # section, topic, what the program shows (our words, after the GATE 2027 CS syllabus sections)
    ("discrete_mathematics", "truth_table", "the truth table of a propositional formula, and whether it is a tautology"),
    ("discrete_mathematics", "relation_properties", "whether a relation on a small set is reflexive, symmetric and transitive"),
    ("discrete_mathematics", "group_axioms", "that addition modulo n forms a group, by checking closure, identity and inverses"),
    ("discrete_mathematics", "graph_colouring", "a greedy colouring of a small graph and the number of colours used"),
    ("discrete_mathematics", "bipartite_matching", "a maximum matching in a bipartite graph by augmenting paths"),
    ("discrete_mathematics", "recurrence_table", "a recurrence solved by tabulation, compared with its closed form"),
    ("engineering_mathematics", "power_iteration", "the dominant eigenvalue of a matrix by power iteration"),
    ("engineering_mathematics", "lu_decomposition", "the LU decomposition of a 3 by 3 matrix"),
    ("engineering_mathematics", "finite_differences", "a derivative and a limit estimated by finite differences"),
    ("engineering_mathematics", "golden_section", "the minimum of a function by golden-section search"),
    ("engineering_mathematics", "binomial_poisson", "binomial and Poisson probabilities for given parameters"),
    ("engineering_mathematics", "distribution_sampling", "uniform, normal and exponential samples from a fixed generator, with their means"),
    ("digital_logic", "quine_mccluskey", "prime implicants of a Boolean function by the tabular method"),
    ("digital_logic", "sequence_detector", "a modulo-6 counter as a state machine of D flip-flops"),
    ("digital_logic", "twos_complement_fixed_point", "two's complement and fixed-point arithmetic on 8-bit values"),
    ("computer_organization", "addressing_modes", "a small instruction set with immediate, direct and indirect addressing, executed"),
    ("computer_organization", "alu_flags", "an ALU computing the zero, carry, sign and overflow flags"),
    ("computer_organization", "microprogrammed_control", "a microprogrammed control sequencer stepping through a microcode table"),
    ("computer_organization", "memory_access_time", "the average memory access time of a two-level hierarchy"),
    ("computer_organization", "interrupt_dma", "transfer time with programmed, interrupt-driven and DMA input and output"),
    ("data_structures", "tree_traversals", "pre-order, post-order and level-order traversals of one binary tree"),
    ("data_structures", "adjacency_list", "a graph stored as adjacency lists, with its degrees"),
    ("algorithms/graphs", "prim", "Prim's minimum spanning tree"),
    ("algorithms/greedy", "huffman_code_lengths", "Huffman code lengths for given symbol frequencies"),
    ("algorithms/analysis", "growth_rates", "operation counts of linear, quadratic and logarithmic algorithms as n grows"),
    ("theory_of_computation", "regex_matcher", "a matcher for regular expressions with concatenation, alternation and star"),
    ("theory_of_computation", "pda_anbn", "a pushdown automaton accepting a^n b^n"),
    ("theory_of_computation", "cyk_parsing", "CYK parsing of a grammar in Chomsky normal form"),
    ("compiler_design", "infix_to_postfix", "infix to postfix translation by a syntax-directed scheme"),
    ("compiler_design", "activation_records", "activation records of a recursive call, by depth"),
    ("compiler_design", "constant_folding", "constant folding and constant propagation over three-address code"),
    ("compiler_design", "liveness_analysis", "live variables at each point of a small control-flow graph"),
    ("compiler_design", "common_subexpression", "common subexpression elimination in a basic block"),
    ("operating_systems", "fork_wait", "a process created with fork and waited for"),
    ("operating_systems", "threads_mutex", "threads adding to a shared total under a mutex (link with -lpthread)"),
    ("operating_systems", "pipe_ipc", "two processes communicating through a pipe"),
    ("operating_systems", "producer_consumer", "a bounded buffer with semaphores, its final counts"),
    ("operating_systems", "cpu_scheduling", "FCFS, SJF and priority scheduling on one job set, with waiting times"),
    ("operating_systems", "disk_scheduling", "head movement under FCFS, SSTF and SCAN"),
    ("operating_systems", "inode_blocks", "how many blocks direct and indirect inode pointers reach"),
    ("databases", "relational_algebra", "selection, projection and natural join over arrays of rows"),
    ("databases", "candidate_keys", "the candidate keys of a relation from its functional dependencies"),
    ("databases", "bplus_tree_order", "the order and height of a B+ tree for given block, key and pointer sizes"),
    ("computer_networks", "delay_throughput", "transmission and propagation delay, and throughput, for given links"),
    ("computer_networks", "aloha_efficiency", "the efficiency of pure and slotted ALOHA"),
    ("computer_networks", "link_state", "link-state routing tables by Dijkstra from each router"),
    ("computer_networks", "ip_fragmentation", "the fragments of an IPv4 datagram for a given MTU"),
    ("computer_networks", "nat_table", "a NAT table translating outgoing and incoming connections"),
    ("computer_networks", "sliding_window", "Go-Back-N sliding-window flow control over a lossy channel"),
    ("computer_networks", "socket_pair", "an echo between two ends of a socket pair"),
    ("computer_networks", "dns_name_encoding", "a domain name in DNS wire format"),
    ("computer_networks", "http_request", "the method, path and headers of an HTTP request"),
]

JS = [
    ("BURP in JavaScript", "lang/hindawi/burp/burp.py", "An ES module with ingest, reverse and check over in-memory files; the same dictionary format.",
     "Byte-identical outputs to the Python BURP on tests/burp/sample and samples/gate, for all 76 languages."),
    ("Transducer rules in JavaScript", "lang/hindawi/languages/*/*.uhin", "Read the cells' flex rules and apply them by longest match, replacing the compiled flex lexers at runtime.",
     "Identical token output to each compiled c2h and h2c on the GATE programs."),
    ("Script filters in JavaScript", "lang/hindawi/tools/script_filters.py, Chintamani fltr_ur_hi and fltr_te_hi", "Port the generated filters, the folds and the aliases, and Chintamani's two filters from their flex sources.",
     "Identical output to the C filters on every word of every cell."),
    ("Romenagri in the browser", "Chintamani Romenagri (uni2acii, acii2cf, acii2uni, fixuninum)", "Compile the C sources to WebAssembly with Emscripten, or port them; expose one function per tool.",
     "Identical C-level forms to the native tools for every name in samples/gate in every language."),
    ("The compilation path in JavaScript", "lang/hindawi/tools/hindawi_chain.py", "to_c and c_names over the pieces above.",
     "Identical C to the Python chain for all 61 GATE programs in the nine complete languages."),
    ("A C compiler in the browser", "gcc, as hindawicc calls it", "TinyCC or Clang compiled to WebAssembly, run under WASI, so a native program compiles and runs in the page.",
     "Every GATE C program compiled in the page prints what gcc's build prints."),
    ("Cells, coverage and standards in JavaScript", "complete_cells.py, coverage.py, standards.py", "Regenerate cells, measure a language and write its standard in the page.",
     "Identical cells, coverage lines and standard.json to the Python tools."),
    ("The GATE runner in the browser", "tests/gate/run.py", "Run the GATE suite for a chosen language in the page, with the side-by-side view.",
     "The same counts as the Python runner for the nine complete languages."),
    ("Notebooks in the browser", "notebooks/*.ipynb", "The notebooks under JupyterLite, so they run without Colab or an install.",
     "Every notebook runs to the end in JupyterLite."),
    ("Arduino from the browser", "ide/arduino", "Transduce in the page and flash through Web Serial, so students need no local toolchain for their boards.",
     "The Arduino sample compiles from a native sketch and runs on an ESP32 and an Uno."),
    ("The npm package", "bin/hindawi", "Package the JavaScript tools as an npm package with a hindawi command for Node, mirroring the Python command.",
     "hindawi verify passes under Node on Linux, macOS and Windows."),
    ("Browser-first setup", "install.sh", "The site becomes the installer: everything above loads in the page; the local toolchain is optional.",
     "A newcomer compiles and runs a GATE program in their language from the site alone."),
]


def gate():
    g = W / "gate"; shutil.rmtree(g, ignore_errors=True); g.mkdir(parents=True); out = []
    for i, (section, topic, shows) in enumerate(GATE, 1):
        if (W.parent / "samples/gate" / section / f"{topic}.c").exists():
            continue                       # written already: a package is only for a topic still without a program
        wid = f"WP-GATE-{i:02d}"
        (g / f"{wid}.md").write_text(f"""# {wid}: {topic.replace('_', ' ')}

Write `samples/gate/{section}/{topic}.c`: a program that shows {shows}.

It keeps the contract in docs/hindawi/GATE-PROGRAMS.md: one self-contained C file under about forty lines; a one-line
comment saying what it shows; no input; a short deterministic result on standard output; exit 0; whole English words in
snake_case for every name; no two calls with side effects in one printf argument list.

Done when `gcc -O2 -Wall` builds it without warnings, every word its names use has a word for each language in
`lang/hindawi/burp/glossary/multi.tsv`, and `hindawi gate --langs dari,pashto,urdu,punjabi,punjabi_shahmukhi,sindhi,telugu,kannada,sanskrit`
reports it compiled and matched in every language.
""", encoding="utf-8")
        out.append({"id": wid, "kind": "gate", "title": f"GATE program: {topic.replace('_', ' ')}", "size": section.replace("_", " "),
                    "path": f"work-packages/gate/{wid}.md"})
    return out


def js():
    j = W / "js"; shutil.rmtree(j, ignore_errors=True); j.mkdir(parents=True); out = []
    for i, (title, frm, what, done) in enumerate(JS, 1):
        wid = f"WP-JS-{i:02d}"
        (j / f"{wid}.md").write_text(f"# {wid}: {title}\n\nReplaces or complements: {frm}.\n\n{what}\n\nDone when: {done}\n\n"
                                     "Write it in plain JavaScript (ES modules), with no build step beyond what the static site needs, and keep "
                                     "the Python tool as the reference until the parity check passes.\n", encoding="utf-8")
        out.append({"id": wid, "kind": "javascript", "title": title, "size": frm, "path": f"work-packages/js/{wid}.md"})
    return out


CREDIT = ("Originator: Abhishek Choudhary, AyeAI. © 1993–2026 Abhishek Choudhary. All rights reserved. Whoever completes "
          "this package is credited for it in CREDITS.md; the originator's credit stays on everything derived from it.")


def tasks():
    """The register (work-packages/tasks.json): one package per open task; covenants and done tasks go to TASKS.md."""
    reg = json.loads((W / "tasks.json").read_text(encoding="utf-8"))
    t = W / "tasks"; shutil.rmtree(t, ignore_errors=True); t.mkdir(parents=True); out = []
    for x in reg:
        if x["status"] not in ("open", "in progress", "rework required"):
            continue
        wid = f"WP-{x['id']}"
        (t / f"{wid}.md").write_text(
            f"# {wid}: {x['title']}\n\nAsked: {x['source']}. Status: {x['status']}.\n\nWhat exists: {x['evidence'] or 'nothing yet'}.\n\n"
            f"Next step: {x['next'] or 'to be set'}.\n\nDone when the change is merged with its tests, every covenant in TASKS.md "
            f"still holds, and `hindawi test` passes.\n\n{CREDIT}\n", encoding="utf-8")
        out.append({"id": wid, "kind": "task", "title": x["title"], "size": x["status"], "path": f"work-packages/tasks/{wid}.md"})
    rows = ["# Tasks and covenants", "", CREDIT, "",
            "Every point of his requests, from the register `work-packages/tasks.json`. Covenants hold always; done means the "
            "nothing is called done until he accepts it; open tasks are work packages anyone can take.", ""]
    for status, head in (("covenant", "Covenants"), ("delivered", "Delivered, awaiting his acceptance"),
                         ("rework", "Rework required"), ("in progress", "In progress"), ("open", "Open")):
        sel = [x for x in reg if x["status"].startswith(status)]
        if sel:
            rows += [f"## {head}", "", "| Id | Task | Evidence | Next |", "|---|---|---|---|"]
            rows += [f"| {x['id']} | {x['title']} | {x['evidence']} | {x['next']} |" for x in sel] + [""]
    (W.parent / "TASKS.md").write_text("\n".join(rows), encoding="utf-8")
    return out


def main():
    W.mkdir(exist_ok=True)
    packages = tasks() + gate() + js() + languages()
    for p in packages:
        p["claim"] = (f"https://github.com/{REPO}/issues/new?title=" + re.sub(r"\s", "+", f"[{p['id']}] {p['title']}")
                      + "&body=" + re.sub(r"\s", "+", f"I am taking {p['id']}: {p['path']}"))
    (W / "index.json").write_text(json.dumps(packages, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    # the site serves docs/ only, so the page reads its own copy
    (W.parent / "docs/hindawi/data/work-packages.json").write_text(json.dumps(packages, ensure_ascii=False) + "\n", encoding="utf-8")
    kinds = {k: sum(1 for p in packages if p["kind"] == k) for k in ("task", "gate", "javascript", "language")}
    print(f"work_packages: {kinds['task']} tasks, {kinds['gate']} GATE, {kinds['javascript']} JavaScript, {kinds['language']} language packages")


if __name__ == "__main__":
    main()
