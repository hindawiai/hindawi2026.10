#include <stdio.h>
#include <math.h>
/* medium access control: throughput of pure and slotted ALOHA, and the load at which each peaks */
int main(void) {
  double best_pure = 0, best_slotted = 0, load_pure = 0, load_slotted = 0;
  for (double load = 0.05; load <= 2.0; load += 0.05) {
    double pure = load * exp(-2 * load), slotted = load * exp(-load);
    if (pure > best_pure) { best_pure = pure; load_pure = load; }
    if (slotted > best_slotted) { best_slotted = slotted; load_slotted = load; }
  }
  printf("pure %.3f at %.2f, slotted %.3f at %.2f\n", best_pure, load_pure, best_slotted, load_slotted);
  return 0;
}
