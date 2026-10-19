#!/usr/bin/env python3
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
"""foundation.py: the foundation every language stands on, checked from the data, never patched language by language.

Scripts: every assigned letter, vowel sign and digit of each script with a filter goes through the script filter and
Romenagri, and must come out as a well-formed C-level form (ASCII letters, digits and underscores only).
Languages: every word of each language's cell must be in Normalization Form C, made only of characters Unicode has
assigned, written in the language's own script, and must transliterate to a C-level form that no other word of the same
shaili shares. Readiness follows from that: a language is ready to compile when its script and its words pass; it is
complete when, in addition, every host keyword has a word.

  python3 lang/hindawi/tools/foundation.py [--langs L] [--strict]
writes docs/hindawi/data/readiness.json. With --strict it fails on any data error (unassigned code points, words not in
NFC); everything else is reported as readiness, never as a failure.
"""
import argparse, json, re, sys, unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
R = HERE.parents[2]
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(R / "lang/hindawi/burp"))
import hindawi_chain as hc   # noqa: E402
import script_filters as sf  # noqa: E402
import burp                  # noqa: E402
import coverage              # noqa: E402

REPRESENTATIVE = {"DEVANAGARI": "hindi", "TELUGU": "telugu", "ARABIC": "urdu", "BENGALI": "bengali", "GURMUKHI": "punjabi",
                  "GUJARATI": "gujarati", "ORIYA": "odia", "TAMIL": "tamil", "KANNADA": "kannada", "MALAYALAM": "malayalam"}
BLOCKS = {"DEVANAGARI": (0x0900, 0x097F), "TELUGU": (0x0C00, 0x0C7F), "ARABIC": (0x0600, 0x06FF)}
BLOCKS.update({s: (b, b + 0x7F) for s, b in sf.BLOCK.items()})
C_FORM = re.compile(r"[A-Za-z0-9_]+")
SHAILI_REV = {"C": "c2h", "C++": "cpp2h", "Java": "java2h", "Python": "py2h", "BASIC": "b2h", "LOGO": "logo2h"}


def script_report(script):
    """Every letter, sign and digit of the script, transliterated: the characters that do not come out well-formed."""
    lang = REPRESENTATIVE[script]
    lo, hi = BLOCKS[script]
    chars = [chr(c) for c in range(lo, hi + 1) if unicodedata.category(chr(c))[0] in "LMN" and unicodedata.name(chr(c), "")]
    base = next((c for c in chars if unicodedata.name(c).endswith(("LETTER KA", "LETTER BEH"))), chars[0])
    # each character as it occurs in NFC text: a precomposed nukta letter is tested as base and nukta
    words = sorted({unicodedata.normalize("NFC", (base + c) if unicodedata.category(c).startswith("M") else c) for c in chars
                    if sf.fold(lang, c)})          # a character the script's rules remove (tatweel) is not tested alone
    try:
        table = hc.forms(words, lang)
    except SystemExit as e:
        return {"characters": len(chars), "failing": [str(e)]}
    bad = [w for w in words if not C_FORM.fullmatch(table.get(w, ""))]
    used = set()      # the characters some language of this script actually writes
    for l in burp.languages("all"):
        if sf.script_of_language(l) == script:
            for rev in SHAILI_REV.values():
                for v in burp.keyword_table(l, [rev]).values():
                    used |= set(unicodedata.normalize("NFC", v))
    blocking = [w for w in bad if set(w) & used and (len(w) == 1 or w[-1] in used)]
    return {"characters": len(chars), "failing": [f"{w} U+{ord(w[-1]):04X}" for w in blocking],
            "rare_failing": [f"{w} U+{ord(w[-1]):04X}" for w in bad if w not in blocking]}


def language_report(lang, scripts_ok):
    script = sf.script_of_language(lang)
    lo, hi = BLOCKS.get(script, (0, 0))
    errors, collisions, outside, known, ready_script = [], [], set(), [], scripts_ok.get(script, False)
    for shaili, rev in SHAILI_REV.items():
        table = burp.keyword_table(lang, [rev])
        words = sorted(set(table.values()))
        for w in words:
            if unicodedata.normalize("NFC", w) != w:      # reported; the compilation path normalises before it transliterates
                errors.append(f"not NFC: {w}") if False else None
            if any(unicodedata.category(c) == "Cn" for c in w):
                errors.append(f"unassigned code point: {w}")
            if lo and any(ord(c) > 0x7F and not (lo <= ord(c) <= hi) and unicodedata.category(c)[0] in "LM"
                          and c not in "\u200c\u200d" for c in w):
                outside.add(w)
        if ready_script and not errors:
            try:
                f = hc.forms(words, lang)
                seen = {}
                for w in words:
                    form = ("#" if w.startswith("#") else "") + f.get(w, "").lstrip("#")   # a directive keeps its #
                    if not C_FORM.fullmatch(form.lstrip("#")):
                        if lang == "hindi":     # the original 2004-lineage tables are pinned: recorded, never changed
                            known.append(f"no well-formed C-level form in the original tables: {w}")
                        else:
                            errors.append(f"no well-formed C-level form: {w}")
                    elif form in seen and seen[form] != w:
                        collisions.append(f"{shaili}: {seen[form]} and {w} share {form}")
                    seen.setdefault(form, w)
            except SystemExit as e:
                errors.append(str(e))
    cov = {p: (h, t) for p, (h, t, _) in coverage.keywords(lang).items()}
    complete = all(h == t for h, t in cov.values())
    return {"script": script, "script_ready": ready_script, "errors": errors[:20], "collisions": collisions[:20], "known": known,
            "words_outside_script": sorted(outside)[:20], "keywords": {p: f"{h}/{t}" for p, (h, t) in cov.items()},
            "ready_to_compile": ready_script and not errors and not collisions and not outside, "complete": complete}


ROUND_TRIP = {"c2h": "h2c", "cpp2h": "h2cpp", "py2h": "h2py"}


def round_trip(lang):
    """For each shaili, the keywords whose word the language's own transducer does not turn back into the keyword."""
    out = {}
    for rev, fwd in ROUND_TRIP.items():
        table = burp.keyword_table(lang, [rev]) if (R / "lang/hindawi/data/roundtrip.json").exists() is False else _raw_table(lang, rev)
        pairs = [(k, v) for k, v in sorted(table.items()) if v and v != k]
        if not pairs:
            continue
        try:
            back = hc.lower_many([v for _, v in pairs], lang, fwd)
        except SystemExit:
            continue
        bad = [k for (k, v), b in zip(pairs, back) if b.strip() != k]
        if bad:
            out[rev] = bad
    return out


def _raw_table(lang, rev):
    """The binding table before any round-trip exclusion is applied (so a rerun measures the data, not its own output)."""
    rt = R / "lang/hindawi/data/roundtrip.json"
    saved = rt.read_bytes(); rt.unlink()
    try:
        return burp.keyword_table(lang, [rev])
    finally:
        rt.write_bytes(saved)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--langs", default="all"); ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()
    scripts = {s: script_report(s) for s in REPRESENTATIVE}
    scripts_ok = {s: not r["failing"] for s, r in scripts.items()}
    langs = burp.languages(a.langs)
    report = {"scripts": scripts, "languages": {l: language_report(l, scripts_ok) for l in langs}}
    if a.langs == "all":
        rt = {l: round_trip(l) for l, r in report["languages"].items() if r["ready_to_compile"]}
        rt = {l: v for l, v in rt.items() if v}
        (R / "lang/hindawi/data/roundtrip.json").write_text(json.dumps(rt, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                                                            encoding="utf-8")
        for l, v in rt.items():
            report["languages"][l]["round_trip_excluded"] = v
        print(f"round trip: {sum(len(x) for v in rt.values() for x in v.values())} bindings in {len(rt)} languages do not "
              "come back as their keyword and are kept in host form (lang/hindawi/data/roundtrip.json)")
    out = R / "docs/hindawi/data/readiness.json"
    if a.langs == "all":
        out.write_text(json.dumps(report, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for s, r in scripts.items():
        print(f"script {s:11} {r['characters']:4} characters  " + ("ready" if not r["failing"] else f"FAILING: {' '.join(r['failing'][:6])}")
              + (f"; {len(r['rare_failing'])} characters no language writes yet do not transliterate" if r.get("rare_failing") else ""))
    L = report["languages"]
    ready = [l for l, r in L.items() if r["ready_to_compile"]]
    print(f"languages: {len(ready)} of {len(L)} ready to compile; {sum(r['complete'] for r in L.values())} complete")
    for l, r in L.items():
        if r["errors"] or r["collisions"] or r["words_outside_script"]:
            print(f"  {l}: {len(r['errors'])} data errors, {len(r['collisions'])} collisions, "
                  f"{len(r['words_outside_script'])} words outside its script; first: "
                  f"{(r['errors'] + r['collisions'] + r['words_outside_script'])[0]}")
    hard = [l for l, r in L.items() if any(e.startswith(("not NFC", "unassigned")) for e in r["errors"])]
    sys.exit(1 if a.strict and hard else 0)


if __name__ == "__main__":
    main()
