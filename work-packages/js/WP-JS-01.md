# WP-JS-01: BURP in JavaScript

Replaces or complements: lang/hindawi/burp/burp.py.

An ES module with ingest, reverse and check over in-memory files; the same dictionary format.

Done when: Byte-identical outputs to the Python BURP on tests/burp/sample and samples/gate, for all 76 languages.

Write it in plain JavaScript (ES modules), with no build step beyond what the static site needs, and keep the Python tool as the reference until the parity check passes.
