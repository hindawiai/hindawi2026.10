#include <stdio.h>
#include <math.h>
/* probability: binomial P(X = 3) with n = 10, p = 0.3, and Poisson P(X = 2) with rate 3 */
double choose(int total, int count) { double result = 1; for (int index = 1; index <= count; index++) result = result * (total - count + index) / index; return result; }
int main(void) {
  double binomial = choose(10, 3) * pow(0.3, 3) * pow(0.7, 7);
  double poisson = exp(-3.0) * pow(3.0, 2) / 2;
  printf("%.4f %.4f\n", binomial, poisson);
  return 0;
}
