#include <stdio.h>
/* routing: link state; router 0 runs Dijkstra over the whole map and keeps the first hop to every router */
int main(void) {
  int cost[5][5] = {{0, 2, 5, 1, 0}, {2, 0, 3, 2, 0}, {5, 3, 0, 3, 1}, {1, 2, 3, 0, 1}, {0, 0, 1, 1, 0}};
  int distance[5], via[5], done[5] = {0};
  for (int router = 0; router < 5; router++) { distance[router] = 1000; via[router] = -1; }
  distance[0] = 0;
  for (int round = 0; round < 5; round++) {
    int nearest = -1;
    for (int router = 0; router < 5; router++) if (!done[router] && (nearest < 0 || distance[router] < distance[nearest])) nearest = router;
    done[nearest] = 1;
    for (int router = 0; router < 5; router++)
      if (cost[nearest][router] && distance[nearest] + cost[nearest][router] < distance[router]) {
        distance[router] = distance[nearest] + cost[nearest][router];
        via[router] = nearest == 0 ? router : via[nearest];
      }
  }
  for (int router = 1; router < 5; router++) printf("%d:%d via %d  ", router, distance[router], via[router]);
  printf("\n");
  return 0;
}
