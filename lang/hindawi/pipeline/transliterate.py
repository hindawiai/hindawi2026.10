#!/usr/bin/env python3
"""Unified transliteration pipeline.
All scripts → Devanagari → original Hindi .uhin → C
"""
import sys
from pathlib import Path

TABLES = Path("/tmp/spt/tables")
PERSO = Path("/tmp/pk19/pushkalavati-integrated/tools/pushkalavati-compiler/vendor/romenagri/upstream/filters")

# script detection by unicode block
SCRIPTS = {
    "bengali": (0x0980, 0x09FF, "bengali_to_deva.tsv"),
    "gujarati": (0x0A80, 0x0AFF, "gujarati_to_deva.tsv"),
    "gurmukhi": (0x0A00, 0x0A7F, "gurmukhi_to_deva.tsv"),
    "oriya": (0x0B00, 0x0B7F, "oriya_to_deva.tsv"),
    "tamil": (0x0B80, 0x0BFF, "tamil_to_deva.tsv"),
    "telugu": (0x0C00, 0x0C7F, "telugu_to_deva.tsv"),
    "kannada": (0x0C80, 0x0CFF, "kannada_to_deva.tsv"),
    "malayalam": (0x0D00, 0x0D7F, "malayalam_to_deva.tsv"),
    "sinhala": (0x0D80, 0x0DFF, "sinhala_to_deva.tsv"),
    "thai": (0x0E00, 0x0E7F, "thai_to_deva.tsv"),
    "lao": (0x0E80, 0x0EFF, "lao_to_deva.tsv"),
    "tibetan": (0x0F00, 0x0FFF, "tibetan_to_deva.tsv"),
    "myanmar": (0x1000, 0x109F, "myanmar_to_deva.tsv"),
    "khmer": (0x1780, 0x17FF, "khmer_to_deva.tsv"),
    "cyrillic": (0x0400, 0x04FF, "cyrillic_to_deva.tsv"),
}

def load_table(name):
    t = {}
    p = TABLES / name
    if not p.exists():
        return t
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.startswith("#") or not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) >= 2:
            t[parts[0]] = parts[1]
    return t


def cjk_to_deva(text):
    """Chinese/Japanese/Korean → pinyin → Devanagari."""
    try:
        from pypinyin import pinyin, Style
        py = pinyin(text, style=Style.NORMAL)
        result = []
        table = load_table("pinyin_to_deva.tsv")
        for syllable in py:
            s = syllable[0].lower()
            # try full syllable, then parts
            if s in table:
                result.append(table[s])
            else:
                for c in s:
                    result.append(table.get(c, c))
        return "".join(result)
    except Exception:
        return text

def detect_script(text):
    for ch in text:
        cp = ord(ch)
        for name, (lo, hi, _) in SCRIPTS.items():
            if lo <= cp <= hi:
                return name
        if 0x0600 <= cp <= 0x06FF:
            return "perso"
        if 0x0400 <= cp <= 0x04FF:
            return "cyrillic"
        if 0x4E00 <= cp <= 0x9FFF:
            return "cjk"
    return "deva"

def project(text, script):
    if script == "deva":
        return text
    if script == "perso":
        sys.path.insert(0, str(PERSO))
        from perso2deva_heur import project as perso_project
        return perso_project(text)
    if script == "cjk":
        return cjk_to_deva(text)
    if script in SCRIPTS:
        table = load_table(SCRIPTS[script][2])
        return "".join(table.get(c, c) for c in text)
    return text

def main():
    src = sys.stdin.read()
    script = detect_script(src)
    result = project(src, script)
    print(result, end="")

if __name__ == "__main__":
    main()
