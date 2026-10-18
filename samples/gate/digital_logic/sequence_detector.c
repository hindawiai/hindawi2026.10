#include <stdio.h>
/* sequential circuits: a Moore state machine that detects 101 in a bit stream, overlaps allowed */
int main(void) {
  int next[4][2] = {{0, 1}, {2, 1}, {0, 3}, {2, 1}};      /* states: none, seen 1, seen 10, seen 101 */
  const char *stream = "1101011010";
  int state = 0;
  for (int index = 0; stream[index]; index++) {
    state = next[state][stream[index] - '0'];
    printf("%d", state == 3);
  }
  printf("\n");
  return 0;
}
