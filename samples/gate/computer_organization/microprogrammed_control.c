#include <stdio.h>
/* control unit design: a microprogrammed sequencer; each microinstruction names its control signals and the next one */
const char *signals[] = {"PC->MAR", "MEM->MDR PC+1", "MDR->IR", "dispatch", "IR->MAR", "MEM->MDR", "MDR+ACC->ACC", "MDR->ACC"};
int next[] = {1, 2, 3, -1, 5, 6, 0, 0};
int main(void) {
  int start[2] = {4, 4}, finish[2] = {6, 7};   /* ADD and LOAD share the operand fetch, then differ */
  for (int kind = 0; kind < 2; kind++) {
    int address = 0;
    while (address != -1) {
      printf("%s; ", signals[address]);
      address = next[address];
    }
    for (address = start[kind]; address != 6; address = next[address]) printf("%s; ", signals[address]);
    printf("%s\n", signals[finish[kind]]);
  }
  return 0;
}
