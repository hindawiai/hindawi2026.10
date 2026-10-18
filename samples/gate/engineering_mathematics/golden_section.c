#include <stdio.h>
#include <math.h>
/* calculus: the minimum of (x - 2)^2 + 1 on [0, 5] by golden-section search */
double curve(double point) { return (point - 2) * (point - 2) + 1; }
int main(void) {
  double ratio = (sqrt(5) - 1) / 2, low = 0, high = 5;
  for (int step = 0; step < 60; step++) {
    double first = high - ratio * (high - low), second = low + ratio * (high - low);
    if (curve(first) < curve(second)) high = second; else low = first;
  }
  printf("%.4f %.4f\n", (low + high) / 2, curve((low + high) / 2));
  return 0;
}
