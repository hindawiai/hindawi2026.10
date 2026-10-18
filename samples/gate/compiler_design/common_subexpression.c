#include <stdio.h>
/* local optimisation: value numbering finds common subexpressions in a basic block */
int main(void) {
  const char *names[] = {"a", "b", "c", "d", "t1", "t2", "t3"};
  int code[4][4] = {{4, 0, '+', 1}, {5, 0, '+', 1}, {6, 4, '*', 2}, {3, 5, '*', 2}};   /* t1 = a + b; t2 = a + b; ... */
  int number[7] = {0, 1, 2, 3, 4, 5, 6}, table[8][4], count = 0;
  for (int index = 0; index < 4; index++) {
    int left = number[code[index][1]], right = number[code[index][3]], found = -1;
    for (int entry = 0; entry < count; entry++)
      if (table[entry][0] == left && table[entry][1] == code[index][2] && table[entry][2] == right) found = table[entry][3];
    if (found >= 0) { number[code[index][0]] = found; printf("%s = %s\n", names[code[index][0]], names[found]); }
    else {
      table[count][0] = left; table[count][1] = code[index][2]; table[count][2] = right; table[count++][3] = code[index][0];
      number[code[index][0]] = code[index][0];
      printf("%s = %s %c %s\n", names[code[index][0]], names[left], code[index][2], names[right]);
    }
  }
  return 0;
}
