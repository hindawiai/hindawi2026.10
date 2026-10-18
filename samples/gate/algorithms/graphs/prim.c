#include <stdio.h>
/* minimum spanning trees: Prim's algorithm on a weight matrix (0 means no edge) */
int main(void) {
  int weight[5][5] = {{0, 2, 0, 6, 0}, {2, 0, 3, 8, 5}, {0, 3, 0, 0, 7}, {6, 8, 0, 0, 9}, {0, 5, 7, 9, 0}};
  int cost[5], parent[5], done[5] = {0}, total = 0;
  for (int vertex = 0; vertex < 5; vertex++) { cost[vertex] = 1000; parent[vertex] = -1; }
  cost[0] = 0;
  for (int round = 0; round < 5; round++) {
    int nearest = -1;
    for (int vertex = 0; vertex < 5; vertex++) if (!done[vertex] && (nearest < 0 || cost[vertex] < cost[nearest])) nearest = vertex;
    done[nearest] = 1; total += cost[nearest];
    if (parent[nearest] >= 0) printf("%d-%d ", parent[nearest], nearest);
    for (int vertex = 0; vertex < 5; vertex++)
      if (weight[nearest][vertex] && !done[vertex] && weight[nearest][vertex] < cost[vertex]) { cost[vertex] = weight[nearest][vertex]; parent[vertex] = nearest; }
  }
  printf("\ntotal %d\n", total);
  return 0;
}
