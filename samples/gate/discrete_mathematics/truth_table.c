#include <stdio.h>
/* propositional logic: the truth table of ((p -> q) and (q -> r)) -> (p -> r), and whether it is a tautology */
int implies(int first, int second) { return !first || second; }
int main(void) {
  int tautology = 1;
  for (int row = 0; row < 8; row++) {
    int p = (row >> 2) & 1, q = (row >> 1) & 1, r = row & 1;
    int value = implies(implies(p, q) && implies(q, r), implies(p, r));
    printf("%d%d%d:%d ", p, q, r, value);
    tautology &= value;
  }
  printf("\n%s\n", tautology ? "tautology" : "not a tautology");
  return 0;
}
