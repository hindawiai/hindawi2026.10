# WP-T-10: Hindi: Chintamani's character-literal rule swallows keywords on lines with two character literals (2 of 113 GATE programs)

Asked: found 18 Oct 2026. Status: open.

What exists: recursive_descent_parser.c and regex_matcher.c fail in Hindi only.

Next step: build Hindi's h2c with the standard literal rule, Chintamani's source untouched; record in DEVIATIONS.md.

Done when the change is merged with its tests, every covenant in TASKS.md still holds, and `hindawi test` passes.

Originator: Abhishek Choudhary, AyeAI. © 1993–2026 Abhishek Choudhary. All rights reserved. Whoever completes this package is credited for it in CREDITS.md; the originator's credit stays on everything derived from it.
