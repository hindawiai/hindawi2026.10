#!/usr/bin/env python3
"""Automated test suite for Hindawi pipeline.
Generates localized test code and tests compilation.
"""
import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PARAMS = ROOT / "lang/hindawi/pipeline/language_params.json"
CHINT = ROOT / "lang/hindawi/upstream/chintamani"
LANGS = ROOT / "lang/hindawi/languages"
FLEX = __import__("os").environ.get("FLEX") or __import__("shutil").which("flex") or "/tmp/flexroot/usr/bin/flex"
FLIB = "-L/tmp/flexroot/usr/lib/x86_64-linux-gnu -lfl"

# canonical test: fibonacci
CANONICAL = '''
int fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}
int main() {
    int result = fib(10);
    return result;
}
'''

def load_params():
    if PARAMS.exists():
        return json.loads(PARAMS.read_text())
    return {}

def generate_localized(lang, params):
    """Generate localized version using keyword mappings."""
    if lang not in params:
        return CANONICAL
    kw = params[lang]
    src = CANONICAL
    # map construct_id to native
    mapping = {
        "KW_IF": "if", "KW_RETURN": "return", "KW_INT": "int",
    }
    for cid, c_tok in mapping.items():
        if cid in kw and kw[cid].get("native"):
            src = src.replace(c_tok, kw[cid]["native"])
    return src

def test_language(lang):
    """Test if language uhin compiles."""
    uhin = LANGS / lang / "h2c.uhin"
    if not uhin.exists():
        return "NO_UHIN"
    c_out = f"/tmp/test_{lang}.c"
    bin_out = f"/tmp/test_{lang}"
    r = subprocess.run([FLEX, "-o", c_out, str(uhin)], capture_output=True)
    if r.returncode != 0:
        return "FLEX_FAIL"
    r = subprocess.run(["gcc", "-o", bin_out, c_out, "-L/tmp/flexroot/usr/lib/x86_64-linux-gnu", "-lfl"], capture_output=True)
    if r.returncode != 0:
        return "GCC_FAIL"
    return "PASS"

def main():
    params = load_params()
    langs = sorted(params.keys())
    results = {}
    for lang in langs:
        results[lang] = test_language(lang)
    # summary
    from collections import Counter
    counts = Counter(results.values())
    print("=== TEST SUITE ===")
    for status, count in counts.most_common():
        print(f"  {status}: {count}")
    print(f"\n=== FAILURES ===")
    for lang, status in results.items():
        if status != "PASS":
            print(f"  {lang}: {status}")
    # write report
    report = ROOT / "lang/hindawi/tests/suite/REPORT.md"
    report.write_text(f"# Test Report\n\n| status | count |\n|---|---|\n" + 
                      "\n".join(f"| {s} | {c} |" for s, c in counts.most_common()))
    print(f"\nreport: {report}")

if __name__ == "__main__":
    main()
