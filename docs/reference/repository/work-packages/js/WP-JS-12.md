# WP-JS-12: Browser-first setup

Replaces or complements: install.sh.

The site becomes the installer: everything above loads in the page; the local toolchain is optional.

Done when: A newcomer compiles and runs a GATE program in their language from the site alone.

Write it in plain JavaScript (ES modules), with no build step beyond what the static site needs, and keep the Python tool as the reference until the parity check passes.
