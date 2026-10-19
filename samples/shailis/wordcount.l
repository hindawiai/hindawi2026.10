%{
#include <stdio.h>
int words = 0, lines = 0;
%}
%%
[a-zA-Z]+   { words++; }
\n          { lines++; }
.           { }
%%
int yywrap(void) { return 1; }
int main(void) { yylex(); printf("%d words, %d lines\n", words, lines); return 0; }
