# The Hindawi linguistics lab: everything a linguistics collaborator needs, in one container, offline once built.
# JupyterLab on port 8888, the review and contribution pages on port 8000, Praat for phonetics, Argos Translate for
# the dictionaries, and Hindawi itself built from the pinned Chintamani the original way.
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
#   docker compose -f lab/docker-compose.yml up --build     (from the repository root)
FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive LANG=C.UTF-8 PIP_BREAK_SYSTEM_PACKAGES=1
RUN apt-get update && apt-get install -y --no-install-recommends \
      git make gcc g++ flex bison gawk libfl-dev python3 python3-pip praat ca-certificates curl \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install --no-cache-dir jupyterlab argostranslate
# English to the lab's languages for the dictionaries; set ARGOS_LANGS at build time to choose (codes, space-separated)
ARG ARGOS_LANGS="hi bn ur ta te mr gu pa fa ar"
RUN argospm update && for l in $ARGOS_LANGS; do argospm install translate-en_$l || echo "no Argos model for en to $l"; done
COPY . /lab/hindawi
WORKDIR /lab/hindawi
RUN bash scripts/fetch.sh && bash scripts/build.sh && python3 lang/hindawi/tools/script_filters.py build
EXPOSE 8888 8000
CMD ["bash", "-c", "(cd docs && python3 -m http.server 8000 &) && jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --notebook-dir=/lab"]
