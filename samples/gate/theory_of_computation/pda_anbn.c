#include <stdio.h>
/* pushdown automata: accept a^n b^n (n >= 1) with a stack, reading a's then b's */
int accepts(const char *word) {
  char stack[64]; int top = 0, state = 0, index = 0;           /* state 0 reads a's, state 1 reads b's */
  for (; word[index]; index++) {
    if (state == 0 && word[index] == 'a') stack[top++] = 'A';
    else if (word[index] == 'b' && top > 0 && stack[top - 1] == 'A') { state = 1; top--; }
    else return 0;
  }
  return state == 1 && top == 0;
}
int main(void) { printf("%d %d %d %d\n", accepts("ab"), accepts("aaabbb"), accepts("aabbb"), accepts("abab")); return 0; }
