# WP-JS-02: Transducer rules in JavaScript

Replaces or complements: lang/hindawi/languages/*/*.uhin.

Read the cells' flex rules and apply them by longest match, replacing the compiled flex lexers at runtime.

Done when: Identical token output to each compiled c2h and h2c on the GATE programs.

Write it in plain JavaScript (ES modules), with no build step beyond what the static site needs, and keep the Python tool as the reference until the parity check passes.
