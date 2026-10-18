#!/usr/bin/env python3
"""Convert C source to native Hindawi. Keywords via .uhin reverse, identifiers via dictionary."""
import re, sys
from pathlib import Path

TERMS = {
    "counter": "गणक", "count": "गणना", "total": "योग", "sum": "योग",
    "index": "सूचकांक", "value": "मान", "result": "परिणाम", "temp": "अस्थायी",
    "buffer": "बफर", "size": "आकार", "length": "लंबाई", "data": "तथ्य",
    "input": "निवेश", "output": "निर्गम", "error": "त्रुटि", "status": "स्थिति",
    "main": "मुख्य", "function": "क्रिया", "return": "प्रत्यागम",
    "if": "यदि", "else": "अन्यथा", "while": "यावत्", "for": "प्रति",
    "int": "पूर्णाङ्क", "char": "वर्ण", "void": "शून्य", "float": "भिन्न",
    "printf": "लेखय", "scanf": "पठ", "malloc": "स्मृतिविभाग", "free": "स्मृतिमुक्त",
    "NULL": "रिक्त", "true": "सत्य", "false": "असत्य",
    "break": "भङ्ग", "continue": "अनुवर्त", "struct": "संरचना",
    "node": "नोड", "next": "अग्र", "prev": "पूर्व", "left": "वाम", "right": "दक्षिण",
    "root": "मूल", "head": "शीर्ष", "tail": "पुच्छ", "key": "कुंजी",
}

def translate_ident(name):
    parts = re.split(r'[_\s]+', name)
    return "_".join(TERMS.get(p.lower(), p) for p in parts if p)

def convert(src):
    # keywords
    for en, hi in sorted(TERMS.items(), key=lambda x: -len(x[0])):
        src = re.sub(rf'\b{en}\b', hi, src)
    # braces
    src = src.replace("{", "अणु").replace("}", "पूर्ण")
    return src

if __name__ == "__main__":
    print(convert(sys.stdin.read()))
