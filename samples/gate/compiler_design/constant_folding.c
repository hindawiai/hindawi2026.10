#include <stdio.h>
/* local optimisation: constant folding and propagation over three-address code (a, b, c, d are variables 0..3) */
int main(void) {
  /* target = left op right; an operand below 100 is a constant, 100 + k is variable k */
  int code[4][4] = {{0, 4, '*', 2}, {1, 100, '+', 3}, {2, 101, '*', 100}, {3, 102, '-', 1}};
  int known[4] = {0}, value[4];
  for (int index = 0; index < 4; index++) {
    int left = code[index][1], right = code[index][3], symbol = code[index][2];
    int left_known = left < 100 || known[left - 100], right_known = right < 100 || known[right - 100];
    int first = left < 100 ? left : value[left - 100], second = right < 100 ? right : value[right - 100];
    if (left_known && right_known) {
      value[code[index][0]] = symbol == '*' ? first * second : symbol == '+' ? first + second : first - second;
      known[code[index][0]] = 1;
      printf("%c = %d\n", 'a' + code[index][0], value[code[index][0]]);
    }
  }
  return 0;
}
