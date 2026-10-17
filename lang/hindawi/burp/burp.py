#!/usr/bin/env python3
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""BURP, the Bidirectional Universal Resource Parser: Hindawi's ingestion pipeline.

  burp.py ingest  SRC --langs all|hindi,bengali,... --out OUT [--scripts bengali,gurmukhi|brahmi] [--rename-files]
                  [--translators glossary,argos,cmd] [--keep REGEX] [-I DIR] [-D NAME[=V]]
  burp.py reverse NATIVE --out OUT          (NATIVE is one OUT/<language> folder BURP wrote)
  burp.py check   SRC --langs all [--scripts brahmi] [--json FILE]   ingest, reverse, compare byte for byte

Ingestion localises an existing project for people; it needs no transliteration. Per file, by its extension
(the paradigm, or shaili), every token outside string literals, comments and #include names is handled thus:
  a keyword       becomes the language's word, from that language's own reverse transducer rules (*2h.uhin);
  an identifier   is translated once per project and language and kept in the project's dictionary;
  an external     (a name the project does not define: system headers, the host's keywords, --keep) stays.
Comments are translated and kept in the dictionary, so the reverse restores them exactly. Build files carry
-D and -U names through the same dictionary. File names are localised only with --rename-files, which renames
the files and rewrites the #include lines and build files that name them. The compilation path is separate:
hindawicc carries native source through Romenagri, which transliterates, so names survive to the symbol table.

Translators, tried in order for every word or phrase not yet in the dictionary:
  glossary  lang/hindawi/tools/tables/identifiers.csv and lang/hindawi/burp/glossary/<language>.tsv
  argos     Argos Translate, offline, if installed with an English to <language> model
  cmd       any program: HINDAWI_TRANSLATE_CMD, with {lang} for the language code, reads lines, writes lines
A word no translator knows stays as it is, and is recorded as such. See docs/hindawi/TRANSLATION-TOOLS.md.
"""
import argparse, csv, json, os, re, shutil, subprocess, sys, unicodedata
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
HIN = HERE.parent
CELLS, LEGACY = HIN / "languages", HIN / "upstream/chintamani"
DICT_NAME = ".hindawi/dictionary.json"   # where tools/build_project.py and hindawicc read it

# extension: (shaili, reverse transducers in order, comment style); lex and yacc compose with c2h, as in Chintamani
CASELESS = ("basic", "vhdl")   # paradigms whose keywords are matched in any case
PARADIGMS = {}
for exts, shaili, rev, style in [((".c", ".h"), "guru", ["c2h"], "c"),
                                 ((".cpp", ".cc", ".cxx", ".hpp", ".hh"), "shraeni", ["cpp2h"], "c"),
                                 ((".s", ".S", ".asm"), "yantra", ["asm2h"], "asm"),
                                 ((".java",), "kritrima", ["java2h"], "c"), ((".bas",), "praatha", ["b2h"], "basic"),
                                 ((".py",), "soochee", ["py2h"], "py"), ((".y",), "wyaaka", ["yacc2h", "c2h"], "c"),
                                 ((".l",), "shabda", ["l2h", "c2h"], "c"), ((".logo", ".lg"), "robot", ["logo2h"], "logo"),
                                 ((".vhd", ".vhdl"), "vhdl", ["vhdl2h"], "vhdl")]:
    for e in exts:
        PARADIGMS[e] = (shaili, rev, style)
# Chintamani's own reverse transducers, used for Hindi wherever the legacy has them
LEGACY_REV = {"asm2h": "yantra/y2h.uhin", "java2h": "kritrima/j2h.uhin", "c2h": "guru/c2h.uhin", "cpp2h": "shraeni/cpp2h.uhin", "b2h": "praatha/b2h.uhin",
              "py2h": "soochee/py2h.uhin", "yacc2h": "wyaaka/yacc2h.uhin", "l2h": "shabda/l2h.uhin"}
BUILD_FILES = re.compile(r"^(GNUmakefile|[Mm]akefile.*|.*\.mk|CMakeLists\.txt|.*\.cmake|meson\.build)$")
ISO = {"hindi": "hi", "bengali": "bn", "urdu": "ur", "tamil": "ta", "telugu": "te", "marathi": "mr", "gujarati": "gu",
       "punjabi": "pa", "kannada": "kn", "malayalam": "ml", "nepali": "ne", "sanskrit": "sa", "odia": "or", "assamese": "as",
       "arabic": "ar", "persian": "fa", "farsi": "fa", "russian": "ru", "chinese": "zh", "japanese": "ja", "korean": "ko",
       "hebrew": "he", "sinhala": "si", "thai": "th", "tibetan": "bo", "burmese": "my", "khmer": "km", "lao": "lo"}
# VHDL's reserved words stay untranslated as identifiers until a language provides its vhdl2h.uhin
VHDL_WORDS = {w for l in (HERE / "paradigms/vhdl_keywords.txt").read_text(encoding="utf-8").splitlines()
              if not l.startswith("#") for w in l.split()} if (HERE / "paradigms/vhdl_keywords.txt").exists() else set()
HOST_WORDS = set("""auto break case char const continue default do double else enum extern float for goto if inline int
long register restrict return short signed sizeof static struct switch typedef union unsigned void volatile while
_Bool _Complex bool true false NULL main class public private protected virtual namespace template typename this new
delete try catch throw using operator friend import package extends implements interface final abstract boolean byte
def lambda pass yield None True False and or not in is elif from as with global nonlocal assert del raise except
print len range self""".split())
WORD = r"#?[A-Za-z_\u00C0-\u024F\u0300-\u036F\u0370-\u03FF\u0400-\u04FF\u0590-\u06FF\u0700-\u08FF\u0900-\u0DFF" \
       r"\u0E00-\u0FFF\u1000-\u109F\u1780-\u18AF\u1900-\u1CFF\u3040-\u30FF\u3400-\u9FFF\uA800-\uABFF\uAC00-\uD7AF" \
       r"\U00010000-\U0001FFFF][\w\u0300-\u036F\u0900-\u0DFF\u0E00-\u0FFF\u1000-\u109F\u1780-\u18AF\u1A00-\u1CFF" \
       r"\uA800-\uABFF\U00010000-\U0001FFFF\u200C\u200D\uAC00-\uD7AF\u1100-\u11FF\u1900-\u19FF\u3130-\u318F]*"
COMMENTS = {"vhdl": r"--[^\n]*", "c": r"//[^\n]*|/\*[\s\S]*?\*/", "py": r"#[^\n]*", "asm": r";[^\n]*", "logo": r";[^\n]*",
            "basic": r"(?im:^[ \t]*REM\b[^\n]*)|'[^\n]*"}
STRINGS = r'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'|"(?:\\.|[^"\\\n])*"|\'(?:\\.|[^\'\\\n])*\''
INCLUDE = r'#[ \t]*include[ \t]*[<"][^>"\n]*[>"]'
RULE = re.compile(r'^(\S+)\s+\{\s*printf\("((?:[^"\\]|\\.)*)"\);\s*\}')


def scanner(style):
    parts = [f"(?P<inc>{INCLUDE})"] if style == "c" else []
    if style == "basic":
        parts += [f"(?P<com>{COMMENTS[style]})", f"(?P<str>{STRINGS})"]
    else:
        parts += [f"(?P<str>{STRINGS})", f"(?P<com>{COMMENTS[style]})"]
    return re.compile("|".join(parts + [f"(?P<word>{WORD})"]))


def load_rules(path):
    """English word to native word, from one transducer's own rules; plain words only."""
    table = {}
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        m = RULE.match(line.strip())
        if not m:
            continue
        pat, out = re.sub(r"\\(.)", r"\1", m.group(1)), re.sub(r"\\(.)", r"\1", m.group(2))
        english = re.compile(r"#?[A-Za-z_][A-Za-z0-9_]*")
        if english.fullmatch(out) and (not english.fullmatch(pat) or (out in HOST_WORDS and pat not in HOST_WORDS)):
            # some generated cells are written the other way round (native to English), some emit KW_ placeholders:
            # read them as they are, so their keywords are used rather than lost (docs/hindawi/DEVIATIONS.md)
            pat, out = (out[3:].lower() if out.startswith("KW_") else out), pat
        if len(pat) > 1 and out and english.fullmatch(pat) and pat not in table:
            table[pat] = out
    return table


def keyword_table(lang, rev):
    table = {}
    for r in rev:
        legacy = next((b / LEGACY_REV.get(r, "-") for b in (LEGACY, HIN.parents[1] / ".build/chintamani/Hindawi")
                       if (b / LEGACY_REV.get(r, "-")).exists()), LEGACY / "-")
        src = legacy if lang == "hindi" and legacy.exists() else CELLS / lang / f"{r}.uhin"
        if src.exists():
            for k, v in load_rules(src).items():
                table.setdefault(k, v)
    return table


def script_of(text):
    names = [unicodedata.name(c, "?").split(" ")[0] for c in text if ord(c) > 0x7F and c.isalpha()]
    return max(set(names), key=names.count) if names else None


def project(text, src, dst):
    """Render one Brahmi-derived script in another by Unicode name projection; characters with no counterpart stay."""
    out = []
    for c in text:
        n = unicodedata.name(c, "")
        if n.startswith(src + " "):
            try:
                t = unicodedata.lookup(dst + n[len(src):])
                if unicodedata.name(t, "") == dst + n[len(src):]:   # aliases do not round-trip: leave those alone
                    out.append(t); continue
            except KeyError:
                pass
        out.append(c)
    return "".join(out)


class Translator:
    def __init__(self, lang, order):
        self.lang, self.code, self.order, self.gloss = lang, ISO.get(lang, lang), order, {}
        rows = []
        g = HIN / "tools/tables/identifiers.csv"
        if g.exists():
            rows += [(r["english"], r.get(lang)) for r in csv.DictReader(l for l in open(g, encoding="utf-8") if l.strip())]
        u = HERE / "glossary" / f"{lang}.tsv"
        if u.exists():
            rows += [tuple(l.rstrip("\n").split("\t")[:2]) for l in open(u, encoding="utf-8") if "\t" in l]
        self.gloss = {e.lower(): n for e, n in rows if e and n}
        self.argos = None
        if "argos" in order:
            try:
                import argostranslate.translate as at
                self.argos = at
            except Exception:
                pass

    def phrase(self, text):
        t = text.strip()
        if not t:
            return text
        for how in self.order:
            if how == "glossary" and t.lower() in self.gloss:
                return self.gloss[t.lower()]
            if how == "argos" and self.argos:
                try:
                    r = self.argos.translate(t, "en", self.code)
                    if r and r != t:
                        return r
                except Exception:
                    pass
            if how == "llm" and os.environ.get("HINDAWI_LLM_URL"):
                r = self.llm(t)
                if r and r != t:
                    return r
            if how == "cmd" and os.environ.get("HINDAWI_TRANSLATE_CMD"):
                p = subprocess.run(os.environ["HINDAWI_TRANSLATE_CMD"].format(lang=self.code), shell=True,
                                   input=t.encode(), capture_output=True)
                r = p.stdout.decode("utf-8", "replace").strip()
                if p.returncode == 0 and r and r != t:
                    return r
        return None

    def llm(self, text):
        """One call to a local model through an OpenAI-compatible endpoint; the answer is the translation only."""
        import urllib.request
        body = {"model": os.environ.get("HINDAWI_LLM_MODEL", "local"), "temperature": 0,
                "messages": [{"role": "system", "content": f"Translate from English into {self.lang.replace('_', ' ')}, "
                              "in that language's own script. Reply with the translation only, nothing else."},
                             {"role": "user", "content": text}]}
        try:
            req = urllib.request.Request(os.environ["HINDAWI_LLM_URL"], json.dumps(body).encode(),
                                         {"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)["choices"][0]["message"]["content"].strip().splitlines()[0].strip()
        except Exception:
            return None

    def identifier(self, ident):
        words = [w for w in re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", ident).split("_") if w]
        whole = self.phrase(" ".join(words))
        parts = [whole] if whole else [self.phrase(w) or w for w in words]
        native = re.sub(r"[^\w\u0300-\u036F\u0900-\u0DFF\u0E00-\u0FFF\u1000-\u109F\u1780-\u18AF\uA800-\uABFF]+", "_",
                        "_".join(parts)).strip("_")
        return native if native and not native[0].isdigit() else ident


def externals(src, includes, defines):
    """Names the project does not define: whatever the system headers declare, by the preprocessor."""
    names = set()
    for f in sorted(p for p in Path(src).rglob("*") if p.suffix in (".c", ".h", ".cpp", ".cc", ".hpp")):
        cmd = ["gcc", "-E", "-x", "c++" if f.suffix in (".cpp", ".cc", ".hpp") else "c", str(f)]
        cmd += [f"-I{d}" for d in [str(f.parent), str(src)] + includes] + [f"-D{d}" for d in defines]
        p = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
        system = False
        for line in p.stdout.splitlines():
            m = re.match(r'# \d+ "([^"]*)"((?: \d)*)', line)
            if m:
                system = " 3" in m.group(2) or m.group(1).startswith("/usr/"); continue
            if system:
                names.update(re.findall(r"\b[A-Za-z_]\w*\b", line))
    return names


class Ingestion:
    def __init__(self, lang, args, external):
        self.lang, self.args, self.external = lang, args, external
        self.tr = Translator(lang, args.translators.split(","))
        self.keep = [re.compile(k) for k in args.keep]
        self.d = {"language": lang, "identifiers": {}, "comments": {}, "files": {}, "sequences": {}}
        self.tables, self.natives = {}, set()

    def table(self, rev):
        key = tuple(rev)
        if key not in self.tables:
            self.tables[key] = keyword_table(self.lang, rev)
            self.natives |= set(self.tables[key].values())
        return self.tables[key]

    def name(self, ident):
        ids = self.d["identifiers"]
        if ident not in ids:
            native, k = self.tr.identifier(ident), 1
            base = native
            taken = set(ids.values()) | self.natives
            while native != ident and native in taken:
                k += 1; native = f"{base}_{k}"
            ids[ident] = native
        return ids[ident]

    def comment(self, text):
        m = re.match(r"(//|/\*|#|;|'|REM\b)([\s\S]*?)(\*/)?$", text, re.I)
        if not m:
            return text
        inner = m.group(2)
        lines = [self.tr.phrase(l) or l if l.strip() else l for l in inner.split("\n")]
        native = m.group(1) + "\n".join(lines) + (m.group(3) or "")
        if native != text:
            self.d["comments"][native] = text
        return native

    def source(self, rel, text):
        shaili, rev, style = PARADIGMS[Path(rel).suffix]
        table, seq, ambiguous = self.table(rev), [], {}
        caseless = style in CASELESS
        if caseless:
            table = {k.lower(): v for k, v in table.items()}
        natives = set(table.values())   # every word the reverse could read as a keyword is recorded, so it reads it right
        for k, v in table.items():
            ambiguous.setdefault(v, []).append(k)

        def sub(m):
            if m.group("word") is None:
                if m.lastgroup == "com":
                    return self.comment(m.group(0))
                if m.lastgroup == "inc" and self.args.rename_files:
                    return re.sub(r'"([^"]+)"', lambda q: '"' + self.renamed(rel, q.group(1)) + '"', m.group(0))
                return m.group(0)
            w = m.group("word")
            key = w.lower() if caseless else w
            if key in table:
                seq.append(w)
                return table[key]
            if w in natives:            # a name spelled like one of the language's keywords stays itself on the way back
                seq.append(w)
            if w.startswith("#") or w[0].isdigit() or style == "asm" or w in HOST_WORDS or (style == "vhdl" and w.lower() in VHDL_WORDS) or w in self.external \
                    or any(k.search(w) for k in self.keep) or not re.fullmatch(r"[A-Za-z_]\w*", w):
                return w
            return self.name(w)
        out = scanner(style).sub(sub, text)
        if seq:
            self.d["sequences"][rel] = seq
        return out

    def renamed(self, rel, inc):
        target = os.path.normpath(str(Path(rel).parent / inc))
        return os.path.relpath(self.d["files"][target], str(Path(self.d["files"].get(rel, rel)).parent)) \
            if target in self.d["files"] else inc

    def build_file(self, text):
        ids = self.d["identifiers"]
        text = re.sub(r"(-[DU])([A-Za-z_]\w*)", lambda m: m.group(1) + ids.get(m.group(2), m.group(2)), text)
        for orig, native in self.d["files"].items():
            text = re.sub(rf"(?<![\w/.]){re.escape(Path(orig).name)}(?![\w.])", Path(native).name, text)
        return text


def ingest_one(lang, args, external):
    src, out = Path(args.src), Path(args.out) / lang
    if out.exists():
        shutil.rmtree(out)
    ing = Ingestion(lang, args, external)
    files = sorted(p for p in src.rglob("*") if p.is_file() and ".hindawi" not in p.parts)
    if args.rename_files:
        for p in files:
            if p.suffix in PARADIGMS:
                rel = str(p.relative_to(src)); stem = ing.tr.identifier(p.stem)
                ing.d["files"][rel] = str(Path(rel).with_name(stem + p.suffix))
    written = {}
    for p in files:                      # sources first, so the build files see every identifier's name
        rel = str(p.relative_to(src))
        if p.suffix in PARADIGMS:
            written[rel] = ing.source(rel, p.read_text(encoding="utf-8", errors="surrogateescape"))
    for p in files:
        rel = str(p.relative_to(src))
        if rel in written:
            continue
        if BUILD_FILES.match(p.name):
            written[rel] = ing.build_file(p.read_text(encoding="utf-8", errors="surrogateescape"))
        else:
            dst = out / rel; dst.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(p, dst)
    for rel, text in written.items():
        dst = out / ing.d["files"].get(rel, rel); dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(text, encoding="utf-8", errors="surrogateescape")
    script = script_of("".join(ing.natives)) or "LATIN"
    ing.d["script"] = script
    (out / ".hindawi").mkdir(parents=True, exist_ok=True)
    ing.d["forward"] = dict(ing.d["identifiers"]); ing.d["reverse"] = {v: k for k, v in ing.d["identifiers"].items()}
    (out / DICT_NAME).write_text(json.dumps(ing.d, ensure_ascii=False, indent=1), encoding="utf-8")
    for s in render_targets(args, script):
        alt = Path(args.out) / f"{lang}@{s.lower()}"
        if alt.exists():
            shutil.rmtree(alt)
        shutil.copytree(out, alt)
        for f in alt.rglob("*"):
            if f.is_file() and (f.suffix in PARADIGMS or BUILD_FILES.match(f.name)):
                f.write_text(project(f.read_text(encoding="utf-8", errors="surrogateescape"), script, s), encoding="utf-8", errors="surrogateescape")
        d = json.loads((alt / DICT_NAME).read_text(encoding="utf-8")); d["rendered"] = {"from": script, "to": s}
        (alt / DICT_NAME).write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    return lang, len(written), len(ing.d["identifiers"]), len(ing.d["comments"]), script


BRAHMI = ["DEVANAGARI", "BENGALI", "GURMUKHI", "GUJARATI", "ORIYA", "TAMIL", "TELUGU", "KANNADA", "MALAYALAM", "SINHALA"]


def render_targets(args, script):
    if not args.scripts or script not in BRAHMI:
        return []
    want = BRAHMI if args.scripts == "brahmi" else [s.upper() for s in args.scripts.split(",")]
    return [s for s in want if s != script and s in BRAHMI]


def reverse_tree(native, out):
    native, out = Path(native), Path(out)
    d = json.loads((native / DICT_NAME).read_text(encoding="utf-8"))
    lang, ids = d["language"], {v: k for k, v in d["identifiers"].items()}
    files = {v: k for k, v in d["files"].items()}
    if out.exists():
        shutil.rmtree(out)
    for p in sorted(native.rglob("*")):
        if not p.is_file() or ".hindawi" in p.relative_to(native).parts:
            continue
        rel = str(p.relative_to(native)); orig = files.get(rel, rel)
        dst = out / orig; dst.parent.mkdir(parents=True, exist_ok=True)
        if p.suffix not in PARADIGMS and not BUILD_FILES.match(p.name):
            shutil.copy2(p, dst); continue
        text = p.read_text(encoding="utf-8", errors="surrogateescape")
        if "rendered" in d:
            text = project(text, d["rendered"]["to"], d["rendered"]["from"])
        if BUILD_FILES.match(p.name):
            text = re.sub(r"(-[DU])(\S+?)(?=[=\s'\")]|$)", lambda m: m.group(1) + ids.get(m.group(2), m.group(2)), text)
            for orig_f, native_f in d["files"].items():
                text = re.sub(rf"(?<![\w/.]){re.escape(Path(native_f).name)}(?![\w.])", Path(orig_f).name, text)
            dst.write_text(text, encoding="utf-8", errors="surrogateescape"); continue
        _, rev, style = PARADIGMS[p.suffix]
        table = keyword_table(lang, rev); inverse = {}
        for k, v in table.items():
            inverse.setdefault(v, []).append(k)
        seq = list(d["sequences"].get(orig, []))

        def sub(m):
            if m.group("word") is None:
                if m.lastgroup == "com":
                    return d["comments"].get(m.group(0), m.group(0))
                if m.lastgroup == "inc" and d["files"]:
                    return re.sub(r'"([^"]+)"', lambda q: '"' + unrename(d, orig, rel, q.group(1)) + '"', m.group(0))
                return m.group(0)
            w = m.group("word")
            if w in inverse:
                return seq.pop(0) if seq else inverse[w][0]
            return ids.get(w, w)
        dst.write_text(scanner(style).sub(sub, text), encoding="utf-8", errors="surrogateescape")
    return out


def unrename(d, orig_rel, native_rel, inc):
    target = os.path.normpath(str(Path(native_rel).parent / inc))
    back = {v: k for k, v in d["files"].items()}
    return os.path.relpath(back[target], str(Path(orig_rel).parent)) if target in back else inc


def languages(spec):
    have = sorted(p.name for p in CELLS.iterdir() if p.is_dir() and (p / "c2h.uhin").exists())
    return have if spec == "all" else [l for l in spec.split(",") if l in have or l == "hindi"]


def cmd_ingest(args):
    langs = languages(args.langs)
    ext = externals(args.src, args.I, args.D)
    with ProcessPoolExecutor(max_workers=args.jobs) as pool:
        rows = list(pool.map(ingest_one, langs, [args] * len(langs), [ext] * len(langs)))
    for lang, n, ni, nc, script in rows:
        print(f"burp: {lang:18} {script:12} {n} files, {ni} identifiers, {nc} comments translated")
    return rows


def cmd_check(args):
    import filecmp, tempfile
    args.out = args.out or tempfile.mkdtemp(prefix="burp-")
    cmd_ingest(args)
    report = []
    for folder in sorted(Path(args.out).iterdir()):
        if not (folder / DICT_NAME).exists():
            continue
        back = reverse_tree(folder, Path(args.out) / ".back" / folder.name)
        src_files = sorted(str(p.relative_to(args.src)) for p in Path(args.src).rglob("*") if p.is_file())
        same = [f for f in src_files if (back / f).exists() and filecmp.cmp(Path(args.src) / f, back / f, shallow=False)]
        d = json.loads((folder / DICT_NAME).read_text(encoding="utf-8"))
        localized = {}
        for f in src_files:
            sfx = Path(f).suffix
            if sfx in PARADIGMS:
                orig = (Path(args.src) / f).read_text(encoding="utf-8", errors="replace")
                nat = (folder / d["files"].get(f, f)).read_text(encoding="utf-8", errors="replace")
                localized[PARADIGMS[sfx][0]] = localized.get(PARADIGMS[sfx][0], False) or nat != orig
        report.append({"folder": folder.name, "script": d.get("rendered", {}).get("to", d.get("script")),
                       "files": len(src_files), "exact": len(same), "localised": localized})
    shaili_names = sorted({s for r in report for s in r["localised"]})
    print(f"\n{'folder':28} {'script':11} {'back exact':>11}  localised: " + " ".join(shaili_names))
    for r in report:
        marks = " ".join(("yes" if r["localised"].get(s) else "no ").ljust(len(s)) for s in shaili_names)
        print(f"{r['folder']:28} {str(r['script']):11} {r['exact']:>5}/{r['files']:<5}  {marks}")
    if args.json:
        Path(args.json).write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    bad = [r for r in report if r["exact"] != r["files"]]
    print(f"\nburp check: {len(report)} ingestions, {len(report) - len(bad)} reverse to the original byte for byte")
    return 1 if bad else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("ingest", "check"):
        s = sub.add_parser(name); s.add_argument("src"); s.add_argument("--langs", default="all")
        s.add_argument("--out", required=(name == "ingest")); s.add_argument("--scripts")
        s.add_argument("--rename-files", action="store_true"); s.add_argument("--translators", default="glossary,argos,llm,cmd")
        s.add_argument("--keep", action="append", default=[r"^__"]); s.add_argument("-I", action="append", default=[])
        s.add_argument("-D", action="append", default=[]); s.add_argument("--jobs", type=int, default=os.cpu_count() or 2)
        if name == "check":
            s.add_argument("--json")
    r = sub.add_parser("reverse"); r.add_argument("native"); r.add_argument("--out", required=True)
    a = ap.parse_args()
    if a.cmd == "ingest":
        cmd_ingest(a)
    elif a.cmd == "reverse":
        print(f"burp: reversed into {reverse_tree(a.native, a.out)}")
    else:
        sys.exit(cmd_check(a))
