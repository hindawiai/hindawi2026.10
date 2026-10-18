#include <stdio.h>
#include <math.h>
/* linear algebra: the largest eigenvalue of a symmetric matrix by power iteration */
int main(void) {
  double matrix[3][3] = {{4, 1, 0}, {1, 3, 1}, {0, 1, 2}}, vector[3] = {1, 1, 1}, value = 0;
  for (int round = 0; round < 100; round++) {
    double next[3] = {0}, length = 0;
    for (int row = 0; row < 3; row++) for (int col = 0; col < 3; col++) next[row] += matrix[row][col] * vector[col];
    for (int row = 0; row < 3; row++) length += next[row] * next[row];
    length = sqrt(length);
    value = 0;
    for (int row = 0; row < 3; row++) { value += vector[row] * next[row]; vector[row] = next[row] / length; }
  }
  printf("%.4f\n", value);
  return 0;
}
