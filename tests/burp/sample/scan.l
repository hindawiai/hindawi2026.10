%{
#include <stdio.h>
%}
%%
[0-9]+ { printf("number\n"); return 1; }
%%
