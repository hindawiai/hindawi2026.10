# Tasks and covenants

Originator: Abhishek Choudhary, AyeAI. © 1993–2026 Abhishek Choudhary. All rights reserved. Whoever completes this package is credited for it in CREDITS.md; the originator's credit stays on everything derived from it.

Every point of his requests, from the register `work-packages/tasks.json`. Covenants hold always; done means the evidence named is in this repository; open tasks are work packages anyone can take.

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

## Done

| Id | Task | Evidence | Next |
|---|---|---|---|
| T-01 | Assert all trademarks: the triad's registered marks and the claimed marks, separate from code licences | legal/TRADEMARKS.md; estate kit assert_trademarks.sh with 144 of his repositories, 36 third-party forks excluded, 2 to confirm | run assert_trademarks.sh --push |
| T-02 | Standards of a quality a standards body can take: drafted to Indian Standard practice for LITD 15 | standards/<lang>/standard.{md,json,docx}: foreword, scope, normative references, terms, conformance, source text, EBNF lexical structure, lowering, name transformation, normative keyword annex, computed test vectors, script filter, conformance record, worked example | complete Hindi (T-03) and the other languages (WP-LANG-*) |
| T-04 | Remove stub standards: no standard for a language whose keyword bindings are incomplete | 67 languages not drafted; each has a language work package |  |
| T-07 | Python in every language through the original pipeline | hindawi_chain.to_py; tests/gate/run.py runs every Python program through each language's own transducer |  |
| T-08 | A keyword is never matched inside a longer name | whole-word rule in every generated forward transducer; nine languages 113/113 |  |
| T-09 | One source for the review and localisation pages; Hindi on them; host keywords before library names | review.html and contribute.html read one source (data/standards.json) with Hindi included and host keywords first; localize.html redirects; keywords.json retired; tested |  |
| T-15 | Write down the further tools and utilities for deliberation | docs/hindawi/TOOLS-PROPOSED.md: fourteen tools, each a proposal | his deliberation |

## In progress

| Id | Task | Evidence | Next |
|---|---|---|---|
| T-05 | Notebooks must show the whole compilation flow | hindawi_chain.stages(): source, script filter, Romenagri, C; Python through soochee h2py (seven languages verified) | rebuild the notebooks and the IDE on stages() (T-06) |

## Open

| Id | Task | Evidence | Next |
|---|---|---|---|
| T-03 | Complete Hindi: bind the keywords Chintamani's 2004-lineage transducers do not carry (C++ 10, Java 6, Python 25, LOGO 14, restrict), as a supplement composed in front of Chintamani's own, never changing its rules | coverage: Hindi C 34/35, C++ 51/61, Java 45/51, Python 11/36, BASIC 21/21, LOGO 0/14 | a supplement transducer composed like h2l with h2c; then the Hindi standard |
| T-06 | Rebuild the notebooks on Chintamani's pattern: installation, the NB UI practice area (Build, Run, Daemon, Hin2Std, Std2Hin, New, Upload, Download), and edit, input and run cells per shaili, every stage shown | pattern read from hindawiai/chintamani Notebooks/हिंदवी_2022_8_स्मरण_पुस्तिका.ipynb | executed headless in every language before shipping |
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
