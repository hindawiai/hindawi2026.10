#include <stdio.h>
/* CPU scheduling: average waiting time under FCFS, SJF and priority (all jobs arrive at time 0) */
double average(int order[], int burst[], int count) {
  int time = 0, waiting = 0;
  for (int index = 0; index < count; index++) { waiting += time; time += burst[order[index]]; }
  return (double)waiting / count;
}
int main(void) {
  int burst[5] = {10, 1, 2, 1, 5}, priority[5] = {3, 1, 4, 5, 2};          /* smaller priority runs first */
  int arrival[5] = {0, 1, 2, 3, 4}, shortest[5], urgent[5];
  for (int index = 0; index < 5; index++) shortest[index] = urgent[index] = index;
  for (int first = 0; first < 5; first++)
    for (int second = first + 1; second < 5; second++) {
      if (burst[shortest[second]] < burst[shortest[first]]) { int temp = shortest[first]; shortest[first] = shortest[second]; shortest[second] = temp; }
      if (priority[urgent[second]] < priority[urgent[first]]) { int temp = urgent[first]; urgent[first] = urgent[second]; urgent[second] = temp; }
    }
  printf("%.1f %.1f %.1f\n", average(arrival, burst, 5), average(shortest, burst, 5), average(urgent, burst, 5));
  return 0;
}
