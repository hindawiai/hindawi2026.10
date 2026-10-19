%{
#include <stdio.h>
#include <ctype.h>
int yylex(void);
void yyerror(const char *s) { fprintf(stderr, "%s\n", s); }
%}
%token NUM
%left '+'
%left '*'
%%
input: | input line ;
line: '\n' | expr '\n' { printf("%d\n", $1); } ;
expr: NUM | expr '+' expr { $$ = $1 + $3; } | expr '*' expr { $$ = $1 * $3; } ;
%%
int yylex(void) {
  int c = getchar();
  while (c == ' ') c = getchar();
  if (isdigit(c)) { yylval = c - '0'; while (isdigit(c = getchar())) yylval = yylval * 10 + c - '0'; ungetc(c, stdin); return NUM; }
  return c == EOF ? 0 : c;
}
int main(void) { return yyparse(); }
