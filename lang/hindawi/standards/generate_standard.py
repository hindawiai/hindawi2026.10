#!/usr/bin/env python3
"""Generate language specification.
Substitutes keywords only. Does not translate prose.
"""
import argparse, json
from pathlib import Path

PARAMS = Path(__file__).resolve().parents[1] / "pipeline/language_params.json"
TEMPLATES = Path(__file__).parent / "templates"

def generate(lang, paradigm):
    params = json.loads(PARAMS.read_text()) if PARAMS.exists() else {}
    kw = params.get(lang, {})
    
    template_file = TEMPLATES / f"{paradigm.lower()}.md"
    if not template_file.exists():
        template_file = TEMPLATES / "c.md"
    template = template_file.read_text()
    
    # keyword substitutions only
    subs = {
        "{LANG}": lang.capitalize(),
        "{BRACE_OPEN}": kw.get("BRACE_OPEN", {}).get("native", "{"),
        "{BRACE_CLOSE}": kw.get("BRACE_CLOSE", {}).get("native", "}"),
        "{KW_IF}": kw.get("KW_IF", {}).get("native", "if"),
        "{KW_ELSE}": kw.get("KW_ELSE", {}).get("native", "else"),
        "{KW_WHILE}": kw.get("KW_WHILE", {}).get("native", "while"),
        "{KW_FOR}": kw.get("KW_FOR", {}).get("native", "for"),
        "{KW_RETURN}": kw.get("KW_RETURN", {}).get("native", "return"),
        "{KW_BREAK}": kw.get("KW_BREAK", {}).get("native", "break"),
        "{KW_CONTINUE}": kw.get("KW_CONTINUE", {}).get("native", "continue"),
        "{KW_MAIN}": kw.get("KW_MAIN", {}).get("native", "main"),
        "{TYPE_INT}": kw.get("KW_INT", {}).get("native", "int"),
        "{TYPE_FLOAT}": kw.get("KW_FLOAT", {}).get("native", "float"),
        "{TYPE_CHAR}": kw.get("KW_CHAR", {}).get("native", "char"),
        "{TYPE_VOID}": kw.get("KW_VOID", {}).get("native", "void"),
    }
    
    # keywords list
    keywords = [data["native"] for cid, data in sorted(kw.items()) 
                if cid.startswith("KW_") and data.get("native")]
    subs["{KEYWORDS}"] = "\n".join(keywords) if keywords else "(none)"
    
    for placeholder, value in subs.items():
        template = template.replace(placeholder, value)
    
    return template

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", required=True)
    ap.add_argument("--paradigm", default="c")
    ap.add_argument("-o", "--output")
    args = ap.parse_args()
    doc = generate(args.lang, args.paradigm)
    if args.output:
        Path(args.output).write_text(doc)
        print(f"wrote {args.output}")
    else:
        print(doc)

if __name__ == "__main__":
    main()
