# The Hindawi linguistics lab

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

One container for linguistics collaborators, from the repository root:

    docker compose -f lab/docker-compose.yml up --build

- **JupyterLab** on http://localhost:8888, with the whole repository at `/lab/hindawi` and your own work kept in `lab/work`.
- **The review page** on http://localhost:8000/hindawi/review.html: your language's word for every construct, paradigm by
  paradigm, with a link that proposes a change as an issue.
- **BURP** to ingest any project into your language: `python3 lang/hindawi/burp/burp.py ingest SRC --langs urdu --out OUT`.
- **Filling the gaps** with machine translation, marked unreviewed for you to check:
  `python3 lang/hindawi/tools/complete_cells.py --fill glossary,argos --langs urdu`.
- **Praat** for phonetics, and Argos Translate with models for the languages named in `ARGOS_LANGS`.

The general ILM laboratory is project-ilm/linguistics-labs; this one adds Hindawi and BURP.
