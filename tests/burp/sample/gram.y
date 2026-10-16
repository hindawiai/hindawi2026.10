%{
#include <stdio.h>
%}
%token NUMBER
%%
expr: NUMBER { printf("value\n"); } ;
%%
