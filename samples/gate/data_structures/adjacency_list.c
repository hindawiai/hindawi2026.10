#include <stdio.h>
/* graphs: adjacency lists kept in arrays, and breadth-first distances from vertex 0 */
int head[6], target[16], next[16], edges = 0;
void add(int from, int to) { target[edges] = to; next[edges] = head[from]; head[from] = edges++; }
int main(void) {
  for (int vertex = 0; vertex < 6; vertex++) head[vertex] = -1;
  int pairs[7][2] = {{0, 1}, {0, 2}, {1, 3}, {2, 3}, {3, 4}, {4, 5}, {1, 5}};
  for (int index = 0; index < 7; index++) { add(pairs[index][0], pairs[index][1]); add(pairs[index][1], pairs[index][0]); }
  int distance[6], queue[6], first = 0, last = 0;
  for (int vertex = 0; vertex < 6; vertex++) distance[vertex] = -1;
  distance[0] = 0; queue[last++] = 0;
  while (first < last) {
    int vertex = queue[first++];
    for (int edge = head[vertex]; edge >= 0; edge = next[edge])
      if (distance[target[edge]] < 0) { distance[target[edge]] = distance[vertex] + 1; queue[last++] = target[edge]; }
  }
  for (int vertex = 0; vertex < 6; vertex++) printf("%d ", distance[vertex]);
  printf("\n");
  return 0;
}
