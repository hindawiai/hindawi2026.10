#include <stdio.h>
#include <stdlib.h>
/* I/O scheduling: total head movement under FCFS, SSTF and SCAN (towards larger cylinders first), from cylinder 53 */
int requests[8] = {98, 183, 37, 122, 14, 124, 65, 67};
int main(void) {
  int in_order = 0, nearest_first = 0, scan = 0, head = 53, done[8] = {0};
  for (int index = 0; index < 8; index++) { in_order += abs(requests[index] - head); head = requests[index]; }
  head = 53;
  for (int round = 0; round < 8; round++) {
    int nearest = -1;
    for (int index = 0; index < 8; index++) if (!done[index] && (nearest < 0 || abs(requests[index] - head) < abs(requests[nearest] - head))) nearest = index;
    nearest_first += abs(requests[nearest] - head); head = requests[nearest]; done[nearest] = 1;
  }
  int lowest = 199;
  for (int index = 0; index < 8; index++) if (requests[index] < lowest) lowest = requests[index];
  scan = (199 - 53) + (199 - lowest);
  printf("%d %d %d\n", in_order, nearest_first, scan);
  return 0;
}
