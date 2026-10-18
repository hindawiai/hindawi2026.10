# Verifying Hindawi 2026.10.4 by hand

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

Each step gives the command and the result it gives on a correct installation. `hindawi verify` runs steps 2 to 6
for the nine completed languages and prints PASS or FAIL for each; the steps below are the same, one at a time.
NINE stands for `dari,pashto,urdu,punjabi,punjabi_shahmukhi,sindhi,telugu,kannada,sanskrit`.

1. **Install.** `bash install.sh`
   Ends with `install.sh: installed`, after two lines proving it:
   `urdu: quick_sort.c compiles from urdu and prints: 1 3 8 14 29 40 55 72` and the same for Telugu.

2. **The toolchain.** `hindawi doctor`
   Every required tool `ok`, the Chintamani toolchain `ok`, and `doctor: ready`.

3. **The regressions.** `hindawi test`
   `ALL AVAILABLE TESTS PASSED`, then `12 passed, 0 failed`. The twelve include: Chintamani's own sources unchanged,
   its Hindi samples compiled and run, a two-file project ingested by BURP and built with `-DVALUE=40`, and a Hindi
   name surviving into the ELF symbol table and back through Romenagri.

4. **Each language complete.** `hindawi coverage --langs NINE`
   For every language: `C 35/35, C++ 61/61, Java 51/51, Python 36/36, BASIC 21/21, LOGO 14/14; GATE programs: 199/199
   names in <language>, library calls left in English: none` (Sanskrit: 198/198).

5. **Every paradigm reversible.** `hindawi check tests/burp/sample --langs all --scripts brahmi`
   `burp check: 355 ingestions, 355 reverse to the original byte for byte`.

6. **Every GATE program compiled from each language.** `hindawi gate --langs NINE`
   For every language: `60 of 60 C programs compile from <language> and print what the originals print; 64 of 64
   files reverse byte for byte`.

7. **One program, by hand, in Urdu.**

       hindawi ingest samples/gate/algorithms/sorting --langs urdu --out /tmp/u
       cat /tmp/u/urdu/quick_sort.c
       HINDAWI_LANG=urdu HINDAWI_NATIVE_SOURCE=1 HINDAWI_DICT=/tmp/u/urdu/.hindawi/dictionary.json \
         hindawicc -O2 -g -o /tmp/q /tmp/u/urdu/quick_sort.c && /tmp/q
       hindawi reverse /tmp/u/urdu --out /tmp/back && diff -r samples/gate/algorithms/sorting /tmp/back && echo same

   The file reads in Urdu: `اگر`, `واپس`, `صحیح` and names such as `محور` and `تقسیم`. The program prints
   `1 3 8 14 29 40 55 72`, and the last line prints `same`. `nm /tmp/q` shows the names in their Romenagri form.

8. **Every language's compilation status.** `hindawi languages --refresh`
   `47 of 76 languages compile and run`. The rest ingest and reverse in full; their scripts have no filter yet.

9. **The samples on the site.** After publishing, `docs/hindawi/samples/index.html`: choose a language and a program,
   and each GATE program shows beside its English original.
