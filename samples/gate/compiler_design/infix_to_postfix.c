#include <stdio.h>
#include <ctype.h>
/* syntax-directed translation: each grammar rule emits postfix as it is recognised */
const char *text;
void expression(void);
void factor(void) {
  if (*text == '(') { text++; expression(); text++; return; }
  while (isdigit(*text)) putchar(*text++);
  putchar(' ');
}
void term(void) { factor(); while (*text == '*' || *text == '/') { char symbol = *text++; factor(); printf("%c ", symbol); } }
void expression(void) { term(); while (*text == '+' || *text == '-') { char symbol = *text++; term(); printf("%c ", symbol); } }
int main(void) { text = "2+3*4-(5-1)/2"; expression(); printf("\n"); return 0; }
