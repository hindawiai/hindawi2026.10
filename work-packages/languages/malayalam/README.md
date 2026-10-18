# Work package: Malayalam

The Malayalam standard needs 87 keyword and library words and 342 name words.
Fill the empty `word` column of `keywords.tsv` and `names.tsv`, in Malayalam and its own script, then submit it with
`hindawi standard import malayalam keywords.tsv names.tsv --by "your name"`, or attach both files to an issue.

The rules: one word per line; a phrase is joined with underscores; a directive keeps its `#`; no word may be an
English keyword or repeat another word in the same file; use the word Malayalam speakers and teachers would use, not a
transliteration of the English unless that is what the community writes. Words already in the standard, for
reference: protected = സംരക്ഷിത, #include = #അന്തര്ഭാവ, continue = തുടരുക, register = രജിസ്റ്റർ, volatile = അസ്ഥിര, default = സ്ഥിരസ്ഥിതി.

To have an AI fill it, give it both files and this instruction:

> Fill the empty word column of these two tab-separated files with Malayalam words in the script Malayalam is normally
> written in. keywords.tsv lists programming-language keywords with their meaning; names.tsv lists English words used
> as variable and function names in teaching programs. One word per line, a phrase joined with underscores, keep the
> # on directives, never an English keyword, no word used twice in one file. Return both files complete, as tab-separated text.
