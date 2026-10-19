# Tasks and covenants

Originator: Abhishek Choudhary, AyeAI. © 1993–2026 Abhishek Choudhary. All rights reserved. Whoever completes this package is credited for it in CREDITS.md; the originator's credit stays on everything derived from it.

Every point of his requests, from the register `work-packages/tasks.json`. Covenants hold always; done means the nothing is called done until he accepts it; open tasks are work packages anyone can take.

## Covenants

| Id | Task | Evidence | Next |
|---|---|---|---|
| COV-01 | Everything survives to the silicon layers: compilation always on the transliterated (Romenagri) form, names reach binaries and debuggers | tests/fundamental.py F5 (a Hindi name becomes an ELF symbol and comes back); every GATE program compiled through the original pipeline |  |
| COV-02 | Do not reinvent: retrieve the existing repository first, reuse, refactor, minimise components | inventory of 182 public repositories in work-packages/estate-inventory.json |  |
| COV-03 | Test-driven, component-based engineering; strong tests; nothing ships unverified | scripts/test_all.sh, tests/fundamental.py, tests/gate/run.py |  |
| COV-04 | No placeholders, nothing fake; inputs from other AI are verified before use | docs/hindawi/PANIR.md records what in the PANIR inputs was not adopted and why |  |
| COV-05 | Provenance on everything: a proposal stays a proposal, what is proven is proven, precedence is never inferred | provenance column in every standard; coverage published as status, never as a gate |  |
| COV-06 | Credits: every artefact keeps the originator's credit and copyright; contributors are credited, never in place of the originator | legal/TRADEMARKS.md section 4; CREDITS.md |  |
| COV-07 | Code licences stay as published (GPL, MIT and others); trademarks are claimed separately and asserted everywhere | legal/TRADEMARKS.md |  |
| COV-08 | Nothing is called done until he can see it done: what is delivered awaits his acceptance | every status in this register |  |
| COV-09 | Originals stay byte for byte: Chintamani's files, the BUILD-0102 sources and the recorded source stages; nothing writes into them | ORIGINALS.sha256 and tests/check_originals.sh, first in scripts/test_all.sh |  |

## Delivered, awaiting his acceptance

| Id | Task | Evidence | Next |
|---|---|---|---|
| T-01 | Assert all trademarks: the triad's registered marks and the claimed marks, separate from code licences | the full texts (TRADEMARKS.md, DISCLAIMERS.md, notice.js) live only in zistgah/zistgah.github.io/legal/; assert_trademarks.sh puts a short pointer in every one of his repositories, one at a time, deleting each clone | his run of assert_trademarks.sh; then the web pages include legal/notice.js (T-35) |
| T-04 | Remove stub standards: no standard for a language whose keyword bindings are incomplete | 67 languages not drafted; each has a language work package |  |
| T-05 | Notebooks must show the whole compilation flow | every notebook shows source, script filter, Romenagri and host text before running |  |
| T-07 | Python in every language through the original pipeline | hindawi_chain.to_py; tests/gate/run.py runs every Python program through each language's own transducer |  |
| T-08 | A keyword is never matched inside a longer name | whole-word rule in every generated forward transducer; nine languages 113/113 |  |
| T-06 | Rebuild the notebooks on Chintamani's pattern: installation, the NB UI practice area (Build, Run, Daemon, Hin2Std, Std2Hin, New, Upload, Download), and edit, input and run cells per shaili, every stage shown | notebooks/<language>/hindawi_<language>.ipynb for 47 languages, after Chintamani's notebook: installation, the NB UI practice area (Build and run, Run, Stages, Hin2Std, Std2Hin, New, Upload, Download, loadable demos), and per shaili (C, Python) program, input, compilation flow, execution and Std2Hin; all 47 executed headless without error; Colab links on docs/hindawi/notebooks.html; the fresh installation path simulated | his use in Colab |
| T-09 | One source for the review and localisation pages; Hindi on them; host keywords before library names | review.html and contribute.html read one source (data/standards.json) with Hindi included and host keywords first; localize.html redirects; keywords.json retired; tested |  |
| T-15 | Write down the further tools and utilities for deliberation | docs/hindawi/TOOLS-PROPOSED.md: fourteen tools, each a proposal | his deliberation |
| T-37 | Restore the originals the 2026.10.5 push re-normalised (10 Chintamani files, 3 BUILD-0102 and source-stage files) | the 2026.10.6 update restores them from 9054423 and checks every original's hash; .gitattributes now excludes them |  |
| T-38 | Remove the build output that had been committed into the Chintamani copy (7 files) | removed; Hindi's transducers now build in a cache copy |  |
| T-43 | Lexicon words made by shifting Devanagari code points into other scripts (177 words in Tamil, Bengali, Assamese, Manipuri and Punjabi) held code points Unicode never assigned; rewritten as each script writes the sound, with a guard and a test | language_params.json corrected; the compilation path names any such word; check_standards_register.py tests the data |  |
| T-44 | Terminology: Chintamani is the Telugu version of Hindawi, which also carries his Urdu Perso-Arabic work; the transducers and the toolchain are the original Hindawi ones, never called Chintamani's own | corrected in the scripts and documents written this cycle |  |
| T-45 | The foundation: languages are data, checked as data. One function gives every native word its C-level form; a whole tree is lowered with one transliteration and one transducer run per 32 MB; Unicode NFC and whole-script rules apply before any filter; every script and every language is checked, and readiness is computed, never patched language by language | lang/hindawi/tools/foundation.py, hindawi_chain.forms and lower_many; docs/hindawi/data/readiness.json: 48 of 76 languages ready to compile |  |
| T-48 | Round trip: a keyword binding is used only if the language's own transducer turns its word back into the keyword; the foundation records the others and BURP keeps them in host form | lang/hindawi/data/roundtrip.json; found because Hindi's __LINE__ did not come back while building wasm3 |  |
| T-49 | The explainer site, for every script: one character followed from human language through encoding, compilers and machines to the physical signal and back, with Qwan-tum Tum Tum, the 7-bit lab, Romenagri and Hindawi's real stages, each layer's AyeKnow evidence state, and the posters with each claim's evidence | docs/trace/ (index.html, data.js built by lang/hindawi/tools/trace_site.py, posters/); driven headless: no errors, the 7-bit round trip verified in Devanagari, Arabic and Hangul |  |
| T-50 | Master contract: the intention is the author's and an unverified claim carries a disclaimer; gates guard the release and nothing else | update_contract.sh adds them to zistgah/governance as C38 and C39 after his PUSH; this repository's audits now report without refusing | his run of update_contract.sh |
| T-51 | AyeCode: reuse what it has for the explainer site | AyeCode found in ayehandsum/ayehandsum (commit f338cba); its alphabets are reused by the explainer site, which writes the typed text in any of them and reads it back (round trip verified) |  |
| T-53 | UISA, the living research record: seed it in pvjournal/uisa and mint it | uisa.json and uisa_payload.tar.gz for estate.sh: the record as authored, README and landing page with each claim's evidence state, its own gate (11 checks, refuses a record altered by one byte) | his run of estate.sh seed uisa.json; the research package added when available |

## Rework required

| Id | Task | Evidence | Next |
|---|---|---|---|
| T-02 | Standards of a quality a standards body can take: drafted to Indian Standard practice for LITD 15 | his review, 18 Oct 2026: the drafts are not acceptable. Standards target the global standards bodies, BIS being one; one self-contained standard per language, script and shaili; the semantics are defined through PANIR and the language being lowered to is not named; the PANIR, SOUP and ROTI names belong in them; quality a standards body can take | define PANIR core normatively first (T-14), then one exemplar per shaili for one language, for his review, then roll out |

## In progress

| Id | Task | Evidence | Next |
|---|---|---|---|
| T-33 | Parashakti: the complete demonstrated sovereign stack on the SHAKTI processor, packaged with the ingestion and sovereign-stack tools: cross compilers, then a self-hosted compiler (GCC, or TinyCC as the least-cost path), nothing external; in Hindi, Sanskrit, Arabic, Farsi, Tamil, Telugu, Kannada, Kashmiri, Urdu, Punjabi and every language that compiles; run on his laptop, not here | parashakti.sh is parametric: a manifest of projects (SHAKTI bare metal, xv6, MINIX 3, Linux, GCC, LLVM, wasm3, SeaBIOS, TinyCC), each fetched, ingested, lowered as a whole tree and built with its own tools. Proved here: SHAKTI bare metal and xv6 in Urdu, Tamil and Hindi. MINIX, Linux, GCC and LLVM are written into the manifest and not yet run; they take hours and several gigabytes each | his full run; then TinyCC self-hosting and the Linux stack |
| T-34 | A local test harness: after seeding, one command tests every feature and function, for every project delivered | hindawi test runs the originals check, the build suite, the standards and register checks and the fundamental regression; hindawi test --full adds the GATE programs in every complete language | the same harness shape for every repository of the estate |
| T-35 | Trademarks and disclaimers from one central place, referred to by every README and web page | central texts and notice.js in the kit | web pages include legal/notice.js, one site at a time, reviewed |
| T-54 | Productization: every product with its audience, how to get it, what is shown to work, and its release gap (PRODUCTS.md); Colab links for phones | PRODUCTS.md; README links each practice notebook to Colab | close each release gap, product by product |

## Open

| Id | Task | Evidence | Next |
|---|---|---|---|
| T-03 | Complete Hindi: bind the keywords the original 2004-lineage Hindawi transducers do not carry (C++ 10, Java 6, Python 25, LOGO 14, restrict), as a supplement composed in front of the original Hindawi, never changing its rules | coverage: Hindi C 34/35, C++ 51/61, Java 45/51, Python 11/36, BASIC 21/21, LOGO 0/14 | a supplement transducer composed like h2l with h2c; then the Hindi standard |
| T-10 | Hindi: Chintamani's character-literal rule swallows keywords on lines with two character literals (2 of 113 GATE programs) | recursive_descent_parser.c and regex_matcher.c fail in Hindi only | build Hindi's h2c with the standard literal rule, Chintamani's source untouched; record in DEVIATIONS.md |
| T-11 | Names that coincide with system-header declarations (index, from glibc's strings.h) stay in English project-wide | coverage counts dictionary names only | count them as untranslated; translate where the project defines the name |
| T-12 | Robotics and Automation: programs for kids' two- and four-wheel robots, drones, RC boats and arms; the GATE 2027 RA paper | simulator traced: icansee.life to ayecnse.net to sims.ayecnse.site (ayecnse/sims, 48 simulations); ayeam-robot control interface | RA program set, as the CS set |
| T-13 | Simulator to real robot with the same ESP32 and Arduino program; IoT control from anywhere; BCI control through NeuroSky MindWave | no network control channel, four-wheel robot, boat or BCI found in ayecnse/sims or ayeam-robot | a control protocol shared by simulator and firmware; ThinkGear parser tested on recorded packets |
| T-14 | PANIR: record the ChatGPT and Gemini intermediate representation as a proposal; lower it through the existing pipeline so it survives to silicon | docs/hindawi/PANIR.md records the proposal, how it must lower through the existing pipeline, and seven defects found in the inputs | docs/hindawi/PANIR.md; formal schema and validator later |
| T-16 | All posters to Zenodo: lawh (20 plates, payload on his machine) and the ten new plates as its next version | lawh is not on GitHub | seed lawh; then a version with the ten plates, AI-generated images marked as such |
| T-17 | PANINI family under one architecture: the browser front ends (humanesque), PANINIphy (physical), PANINIq (quantum, 0.3.0 to package), PANINIb | repos exist in zistgah | an architecture note with pointers, not a merge |
| T-18 | The AyeAI triad kept distinct; commercial; pointers to the libraries, not copies; separate organisations where needed | triad sites read; licences unchanged by his ruling | estate structure note |
| T-19 | VARZISH: how the learning system works; a testing environment; learning and test generation | zistgah/varzish is a skeleton; kitab already routes learning to it | spec and first slice, reusing kitab and the cyclers |
| T-20 | The cyclers in the same package as VARZISH | six cyclers live (matba, khwab, awaz, tilasm, pench, yadein); PANINI owns the runner | package by reference, no second runner |
| T-21 | Posters' theory into books written in text, through the cyclers | matba is the print cycler | one matba cycle per poster corpus |
| T-22 | Software factory and systems factory model: people design, architect, think critically, judge ethics; ingestion does the rest |  | model document with the factory stations mapped to existing tools |
| T-23 | Formal definitions a government can take | the standards' clauses 3, 5, 7 to 9 are the first | formal definitions of the pipeline and of PANIR |
| T-24 | Requirements document | zistgah/mrd exists | requirements for Hindawi 2026, in the MRD repository's form |
| T-25 | Project sheets and estimations | estimate kit built (estimate.sh, COCOMO II), not seeded | project sheets per component, estimates from the kit |
| T-26 | Configuration management across the estate (182 public repositories here; 400 to 500 in all) | work-packages/estate-inventory.json | an estate register with owner, licence, status, DOI, site per repository |
| T-27 | Share work packages on social media |  | a share link on each package on the work-packages page |
| T-28 | Complete every other language's keyword bindings, so each can carry a standard | 67 language work packages | one package per language |
| T-29 | Compilation path for the 29 languages without a script filter (Cyrillic, CJK, Thai, Lao, Khmer, Myanmar, Tibetan, Sinhala and others) | 47 of 76 compile | a filter per script |
| T-30 | Library-wide localisation: the C library, the C++ standard library, the Java API, x86 mnemonics |  |  |
| T-31 | The tools in JavaScript, so the site can be the installer | 12 JavaScript packages |  |
| T-32 | Line-ending rules can re-normalise CRLF files when a whole tree is staged | Chintamani's originals verified byte-identical live; BUILD-0102 files carry CRLF | stage explicit paths in every script |
| T-36 | Cross-repository links for discovery and for using one component from another, so nothing is repeated |  | a related-components block per repository from the estate register |
| T-39 | Recollect the whole conversation; find any deviation from the original architecture; check with Rahnuma and update it | zistgah/rahnuma |  |
| T-40 | The software factory, built and polished with the robotics, IoT and GATE student networks, on component-based engineering, used by us first |  |  |
| T-41 | The basic robot: Arduino first, then ESP32 and higher; parts under 1000 rupees; from the material behind icansee.life | simulator and control pages traced | the robot's bill of materials and pin map from his pages, then the programs |
| T-42 | Standards for the global standards bodies (ISO/IEC JTC 1/SC 22, the Unicode Consortium, and national bodies such as BIS), not one body |  | part of T-02 |
| T-46 | Scripts with no filter yet (Cyrillic, Han, Hangul, Kana, Thai, Lao, Khmer, Myanmar, Tibetan, Sinhala, Javanese and others: 24 languages): one generic transliteration from Unicode data to C-level forms |  | decide the scheme (ISO transliterations, or Unicode names) and generate the filters from Unicode data |
| T-47 | Hebrew, Syriac, Phoenician and Imperial Aramaic are written in their own scripts but bound to the Perso-Arabic filter: give each its script | the foundation check reports their words outside the declared script |  |
| T-52 | The hardware layers below the ISA for Parashakti and Qwan-tum: RTL, simulation, synthesis, formal checks, FPGA (Spartan-3A) bitstream, GPIO and oscilloscope capture, and the measured round trip D(M(E(x))) = x | the layers are open in the explainer site's stack table |  |
