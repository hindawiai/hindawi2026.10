#include <stdio.h>
/* greedy: Huffman coding; merge the two lightest trees until one is left, then read each symbol's code length */
int main(void) {
  int weight[11] = {5, 9, 12, 13, 16, 45}, parent[11], active[11] = {1, 1, 1, 1, 1, 1}, count = 6, total = 0;
  for (int round = 0; round < 5; round++) {
    int first = -1, second = -1;
    for (int node = 0; node < count; node++) {
      if (!active[node]) continue;
      if (first < 0 || weight[node] < weight[first]) { second = first; first = node; }
      else if (second < 0 || weight[node] < weight[second]) second = node;
    }
    weight[count] = weight[first] + weight[second]; active[count] = 1;
    parent[first] = parent[second] = count; active[first] = active[second] = 0; count++;
  }
  for (int symbol = 0; symbol < 6; symbol++) {
    int length = 0;
    for (int node = symbol; node != count - 1; node = parent[node]) length++;
    printf("%d ", length); total += length * weight[symbol];
  }
  printf("\nbits %d\n", total);
  return 0;
}
