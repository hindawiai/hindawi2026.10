# WP-JS-06: A C compiler in the browser

Replaces or complements: gcc, as hindawicc calls it.

TinyCC or Clang compiled to WebAssembly, run under WASI, so a native program compiles and runs in the page.

Done when: Every GATE C program compiled in the page prints what gcc's build prints.

Write it in plain JavaScript (ES modules), with no build step beyond what the static site needs, and keep the Python tool as the reference until the parity check passes.
