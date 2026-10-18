#include <stdio.h>
#include <math.h>
/* probability: uniform, exponential and normal samples from a fixed linear congruential generator, and their means */
unsigned long seed = 12345;
double uniform(void) { seed = (seed * 1103515245UL + 12345UL) % 2147483648UL; return (seed + 0.5) / 2147483648.0; }
int main(void) {
  double total_uniform = 0, total_exponential = 0, total_normal = 0;
  for (int index = 0; index < 20000; index++) {
    total_uniform += uniform();
    total_exponential += -log(uniform()) / 2.0;                                /* rate 2 */
    double first = uniform(), second = uniform();
    total_normal += 10 + 3 * sqrt(-2 * log(first)) * cos(2 * 3.14159265358979 * second);   /* mean 10 */
  }
  printf("%.2f %.2f %.1f\n", total_uniform / 20000, total_exponential / 20000, total_normal / 20000);
  return 0;
}
