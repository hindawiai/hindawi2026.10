#include <stdio.h>
/* normal forms: every candidate key of R(A,B,C,D,E) under A->B, B->C, CD->E, E->A (attributes are bits) */
int left[4] = {1, 2, 4 | 8, 16}, right[4] = {2, 4, 16, 1};
int closure(int attributes) {
  for (int changed = 1; changed; ) {
    changed = 0;
    for (int index = 0; index < 4; index++)
      if ((attributes & left[index]) == left[index] && (attributes | right[index]) != attributes) { attributes |= right[index]; changed = 1; }
  }
  return attributes;
}
int main(void) {
  int keys[32], count = 0;
  for (int set = 1; set < 32; set++) {
    if (closure(set) != 31) continue;
    int minimal = 1;
    for (int index = 0; index < count; index++) if ((keys[index] & set) == keys[index]) minimal = 0;
    if (!minimal) continue;
    keys[count++] = set;
    for (int bit = 0; bit < 5; bit++) if (set >> bit & 1) putchar('A' + bit);
    putchar(' ');
  }
  printf("\n");
  return 0;
}
