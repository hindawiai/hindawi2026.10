#!/usr/bin/env python3
"""Target-language-aware identifier mapping.
native <-> canonical <-> backend. Does not force Hindi intermediate.
"""
import json
from pathlib import Path

MAPS = Path(__file__).parent / "maps"

def load_map(lang):
    p = MAPS / f"{lang}.json"
    if p.exists():
        return json.loads(p.read_text())
    return {"forward": {}, "reverse": {}}

def save_map(lang, data):
    MAPS.mkdir(exist_ok=True)
    (MAPS / f"{lang}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2))

def map_identifier(ident, lang, direction="forward"):
    """direction: forward (native->canonical) or reverse (canonical->native)."""
    m = load_map(lang)
    table = m.get(direction, {})
    if ident in table:
        return table[ident]
    # no mapping: preserve as-is (do not invent)
    return ident

def register(lang, native, canonical):
    m = load_map(lang)
    m.setdefault("forward", {})[native] = canonical
    m.setdefault("reverse", {})[canonical] = native
    save_map(lang, m)
