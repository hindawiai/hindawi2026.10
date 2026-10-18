#include <stdio.h>
/* graphs: greedy colouring; each vertex takes the smallest colour no neighbour has */
int main(void) {
  int graph[6][6] = {{0,1,1,0,0,1},{1,0,1,1,0,0},{1,1,0,1,1,0},{0,1,1,0,1,0},{0,0,1,1,0,1},{1,0,0,0,1,0}};
  int colour[6], count = 0;
  for (int vertex = 0; vertex < 6; vertex++) {
    int used[6] = {0};
    for (int next = 0; next < vertex; next++) if (graph[vertex][next]) used[colour[next]] = 1;
    colour[vertex] = 0;
    while (used[colour[vertex]]) colour[vertex]++;
    if (colour[vertex] + 1 > count) count = colour[vertex] + 1;
    printf("%d ", colour[vertex]);
  }
  printf("\ncolours %d\n", count);
  return 0;
}
