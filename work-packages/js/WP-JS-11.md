# WP-JS-11: The npm package

Replaces or complements: bin/hindawi.

Package the JavaScript tools as an npm package with a hindawi command for Node, mirroring the Python command.

Done when: hindawi verify passes under Node on Linux, macOS and Windows.

Write it in plain JavaScript (ES modules), with no build step beyond what the static site needs, and keep the Python tool as the reference until the parity check passes.
