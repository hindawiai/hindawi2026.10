# Tools proposed for deliberation

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

Every entry is a **proposal**: nothing here is built. Each says what it is for, what existing work it reuses, and how it
keeps the covenant that everything survives to the silicon layers. Accepted entries become work packages in TASKS.md.

| Tool | Purpose | Reuses | Survives to silicon by |
|---|---|---|---|
| PANIR schema and validator | Make PANIR machine-checkable: node kinds, fields, cardinalities, versions | docs/hindawi/PANIR.md | validating before any rendering |
| C frontend to PANIR | Build PANIR from C source with an existing C parser | the GATE programs as its test set | rendering back to C through the existing pipeline |
| PANIR renderer to C | Lower PANIR to C that enters the existing compilation path | hindawi_chain.stages() | being that path's input |
| De-punctuated Hindawi renderer and its parser | A reading surface with words for operators, parsed back to PANIR | the standards' keyword bindings | round trip to PANIR, then to C |
| Python frontend to PANIR | Build PANIR from Python with the standard `ast` module | the Python GATE programs | rendering to the soochee path |
| Name ABI checker | Find two native names of one program that share a C-level form | hindawi_chain.c_names() | the forms are the binary's symbols |
| Standards linter | Check a draft against Indian Standard drafting practice: clause order, normative wording, references | standards/ | not applicable: documentation |
| Robot control protocol | One message format for the simulator and the ESP32 and Arduino firmware, so a program moves either | ayecnse/sims, ayeam-robot, ide/arduino | the same compiled firmware runs the robot |
| ThinkGear parser | Read NeuroSky MindWave packets into attention and meditation values that drive the protocol | the robot control protocol | compiled C on the controller |
| VARZISH test generator | Generate exercises and tests from the GATE programs: changed inputs, expected outputs by running the English original | samples/gate, tests/gate/run.py | every expected output comes from a compiled run |
| Poster-to-book cycler | Turn a poster corpus into a book written in text through matba's print cycle | zistgah/matba, the PANINI cyclers | not applicable: publication |
| Trademark notice checker | Confirm every one of his repositories carries the trademark notice | assert_trademarks.sh | not applicable: legal |
| Estate register | One record per repository: owner, licence, status, DOI, site, tests | zistgah/estate, work-packages/estate-inventory.json | not applicable: configuration management |
| Work-package sharer | Post an open package to social media with its claim link | docs/hindawi/work-packages.html | not applicable |
