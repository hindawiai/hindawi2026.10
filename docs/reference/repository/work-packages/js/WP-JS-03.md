# WP-JS-03: Script filters in JavaScript

Replaces or complements: lang/hindawi/tools/script_filters.py, Chintamani fltr_ur_hi and fltr_te_hi.

Port the generated filters, the folds and the aliases, and Chintamani's two filters from their flex sources.

Done when: Identical output to the C filters on every word of every cell.

Write it in plain JavaScript (ES modules), with no build step beyond what the static site needs, and keep the Python tool as the reference until the parity check passes.
