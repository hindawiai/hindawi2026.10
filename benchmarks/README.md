# Benchmarks

These scripts measure a job. They do not rank projects.

## What the others are

Vidyut is a Sanskrit word generator. You give it a root or stem and the grammatical arguments. It returns the surface form and the prakriyā. That is text generation with a rule trace. It is not meaningless. It is also not analysis. Their sandhi and segmentation crates are separate lookup tools.

sanskrit_parser is the one with a reverse step. It splits sandhi, then looks the pieces up in a form database. The reverse stops at the split. The morphological knowledge is mostly in the lexicon, not in a sūtra execution. Their generator is a smaller forward engine.

vyakarana is a limited forward simulator. No licence file. It is listed and not scored.

## What to run

Analysis, on surface forms:

```bash
node benchmarks/local_inverse.js
python3 benchmarks/run_benchmarks.py
```

This scores the local inverse slice on `उपेन्द्रो` and `किताब`. A pass means the prefix and the candidates match the fixture, or the no-match case stays a no-match. It does not score ending reduction.

Generation, only if the other tool is installed:

- Vidyut: derive `BU + lat` and check the surface is `Bavati` and that the trace cites rule codes.
- sanskrit_parser: split `चैव` and check `च + एव` is among the splits.

Do not score a generator on analysis. Do not score an analyzer on generation. A missing install is reported. It is not a failure of this repository.
