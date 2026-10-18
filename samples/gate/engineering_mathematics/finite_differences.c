#include <stdio.h>
#include <math.h>
/* calculus: a derivative by central differences, and the limit of sin(x)/x as x approaches 0 */
int main(void) {
  double point = 1.0, step = 1e-5;
  double slope = (sin(point + step) - sin(point - step)) / (2 * step);
  printf("%.6f %.6f\n", slope, cos(point));
  for (double width = 0.1; width > 1e-4; width /= 10) printf("%.8f ", sin(width) / width);
  printf("\n");
  return 0;
}
