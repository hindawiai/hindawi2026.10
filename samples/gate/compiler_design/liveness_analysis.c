#include <stdio.h>
/* data-flow analysis: live variables over a control-flow graph, iterated to a fixed point (bits a=1, b=2, c=4, d=8) */
int main(void) {
  int uses[4] = {0, 1 | 2, 4, 1 | 8}, defines[4] = {1 | 2, 4, 8, 0};
  int successors[4][2] = {{1, -1}, {2, 3}, {1, -1}, {-1, -1}}, live_in[4] = {0}, live_out[4] = {0}, changed = 1, rounds = 0;
  while (changed) {
    changed = 0; rounds++;
    for (int block = 3; block >= 0; block--) {
      int out = 0;
      for (int index = 0; index < 2; index++) if (successors[block][index] >= 0) out |= live_in[successors[block][index]];
      int in = uses[block] | (out & ~defines[block]);
      if (in != live_in[block] || out != live_out[block]) { live_in[block] = in; live_out[block] = out; changed = 1; }
    }
  }
  for (int block = 0; block < 4; block++) {
    for (int bit = 0; bit < 4; bit++) if (live_in[block] >> bit & 1) putchar('a' + bit);
    putchar(' ');
  }
  printf("\nrounds %d\n", rounds);
  return 0;
}
