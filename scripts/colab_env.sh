#!/usr/bin/env bash
# colab_env.sh: put Hindawi's command-line tools on the PATH of the notebook and of Colab's terminal (the icon at the
# bottom left), and set their environment for every new shell.
# © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
H="$(cd "$(dirname "$0")/.." && pwd)"
for t in bin/hin bin/hindawi lang/hindawi/hindawicc; do [ -e "$H/$t" ] && ln -sf "$H/$t" "/usr/local/bin/$(basename "$t")"; done
for t in "$H"/.build/chintamani/Romenagri/*; do [ -x "$t" ] && [ -f "$t" ] && ln -sf "$t" "/usr/local/bin/$(basename "$t")"; done
ENV="export HINDAWI_HOME='$H' ROMENAGRI='$H/.build/chintamani/Romenagri'"
echo "$ENV" > /etc/profile.d/hindawi.sh 2>/dev/null
grep -q HINDAWI_HOME ~/.bashrc 2>/dev/null || echo "$ENV" >> ~/.bashrc
command -v flex >/dev/null && command -v bison >/dev/null || apt-get -qq install -y flex bison >/dev/null 2>&1
echo "Hindawi tools ready here and in the terminal: hin, hindawi, hindawicc"
