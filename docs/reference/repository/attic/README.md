# attic

Tools that earlier builds shipped and that something better now does. They are kept so the history stays readable
and a result from an earlier release can be reproduced; nothing in the repository calls them any more.

| Retired tool | From | Now done by |
|---|---|---|
| `ingest.py` | Grok, C10; kept on the original chain in C11 | `hindawi ingest` (BURP, `lang/hindawi/burp/burp.py`) |
| `import_project.py` | Grok, C10 | `hindawi ingest` on the project's directory |
| `ingest_dir.py` | Grok, C10 | `hindawi ingest` on the directory |
| `identifier_map.py` | Grok, C10 | BURP's per-project dictionary (`.hindawi/dictionary.json`) |
| `ingest_project.py` | C16 | `hindawi ingest` (BURP superseded it in C17) |
| `native_convert.py` | BUILD-0102 | `hindawi ingest` and `hindawi reverse` |
| `to_upstream.py` | BUILD-0102 | `hindawi reverse` |
| `regression.sh` | Grok, C10 | `hindawi test` (the build's suite and `tests/fundamental.py`) |
| `import_full_dataset.py` | BUILD-0102 | nothing calls it; the datasets it imported are in the language cells |

`lang/hindawi/tools/to_native.py` stays where it is: BUILD-0102's own test suite (`lang/hindawi/tests/comprehensive`)
still uses it.
