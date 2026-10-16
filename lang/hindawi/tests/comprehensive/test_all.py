#!/usr/bin/env python3
"""Comprehensive test: all languages × all Shailis × complex programs."""
import json, subprocess, sys
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[4]
PARAMS = ROOT / "lang/hindawi/pipeline/language_params.json"
CHINT = ROOT / "lang/hindawi/upstream/chintamani"
TOOLS = ROOT / "lang/hindawi/tools"
FLEX = "/tmp/flexroot/usr/bin/flex"

SHAILIS = ["h2c", "h2cpp", "h2asm", "h2java", "h2b", "h2py", "h2yacc", "h2logo", "h2l"]

# complex test programs
PROGRAMS = {
    "fibonacci": '''
int fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}
int main() { return fib(10); }
''',
    "linked_list": '''
struct node { int value; struct node *next; };
struct node *create(int value) {
    struct node *temp = malloc(sizeof(struct node));
    temp->value = value;
    temp->next = NULL;
    return temp;
}
''',
    "loop": '''
int sum(int n) {
    int total = 0;
    int i = 0;
    while (i < n) { total = total + i; i = i + 1; }
    return total;
}
''',
}

def test_uhin_compiles(lang, shaili):
    uhin = CHINT / lang / f"{shaili}.uhin"
    if not uhin.exists():
        return "NO_UHIN"
    r = subprocess.run([FLEX, "-o", f"/tmp/t_{lang}_{shaili}.c", str(uhin)], capture_output=True)
    if r.returncode != 0:
        return "FLEX_FAIL"
    r = subprocess.run(["gcc", "-o", f"/tmp/t_{lang}_{shaili}", f"/tmp/t_{lang}_{shaili}.c",
                        "-L/tmp/flexroot/usr/lib/x86_64-linux-gnu", "-lfl"], capture_output=True)
    return "PASS" if r.returncode == 0 else "GCC_FAIL"

def test_conversion(lang, program):
    r = subprocess.run(
        ["python3", str(TOOLS / "to_native.py"), "--lang", lang],
        input=PROGRAMS[program].encode(), capture_output=True, timeout=30
    )
    if r.returncode != 0:
        return "FAIL"
    out = r.stdout.decode()
    # check if conversion happened
    if "int" in out and "return" in out:
        return "NO_CONVERT"
    return "PASS"

def main():
    params = json.loads(PARAMS.read_text())
    langs = sorted(params.keys())
    
    print("=== UHIN COMPILATION ===")
    uhin_results = Counter()
    for lang in langs[:20]:  # sample
        for shaili in SHAILIS:
            result = test_uhin_compiles(lang, shaili)
            uhin_results[result] += 1
    for status, count in uhin_results.most_common():
        print(f"  {status}: {count}")
    
    print("\n=== CONVERSION ===")
    conv_results = Counter()
    for lang in ["bengali", "tamil", "hindi", "urdu", "russian"]:
        for prog in PROGRAMS:
            result = test_conversion(lang, prog)
            conv_results[result] += 1
            if result != "PASS":
                print(f"  {lang}/{prog}: {result}")
    for status, count in conv_results.most_common():
        print(f"  {status}: {count}")
    
    # write report
    report = ROOT / "lang/hindawi/tests/comprehensive/REPORT.md"
    report.write_text(f"# Comprehensive Test Report\n\n## UHIN\n{dict(uhin_results)}\n\n## Conversion\n{dict(conv_results)}\n")
    print(f"\nreport: {report}")

if __name__ == "__main__":
    main()
