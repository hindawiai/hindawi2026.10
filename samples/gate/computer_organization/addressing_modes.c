#include <stdio.h>
/* instruction sets: an accumulator machine with immediate, direct, indirect and indexed addressing */
enum { IMMEDIATE, DIRECT, INDIRECT, INDEXED };
int memory[16] = {0, 0, 0, 0, 0, 0, 0, 0, 40, 11, 12, 5, 7, 0, 0, 0}, accumulator = 0, index_register = 2;
int operand(int kind, int field) {
  switch (kind) {
    case IMMEDIATE: return field;
    case DIRECT: return memory[field];
    case INDIRECT: return memory[memory[field]];
    default: return memory[field + index_register];
  }
}
int main(void) {
  int program[4][3] = {{0, IMMEDIATE, 5}, {1, DIRECT, 8}, {1, INDIRECT, 9}, {1, INDEXED, 10}};   /* load, add, add, add */
  for (int step = 0; step < 4; step++) {
    int value = operand(program[step][1], program[step][2]);
    accumulator = program[step][0] == 0 ? value : accumulator + value;
    printf("%d ", accumulator);
  }
  printf("\n");
  return 0;
}
