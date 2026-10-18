#include <stdio.h>
/* linear algebra: LU decomposition (Doolittle) of a 3 by 3 matrix */
int main(void) {
  double matrix[3][3] = {{2, -1, -2}, {-4, 6, 3}, {-4, -2, 8}}, lower[3][3] = {{0}}, upper[3][3] = {{0}};
  for (int row = 0; row < 3; row++) {
    for (int col = row; col < 3; col++) {
      double sum = 0;
      for (int index = 0; index < row; index++) sum += lower[row][index] * upper[index][col];
      upper[row][col] = matrix[row][col] - sum;
    }
    lower[row][row] = 1;
    for (int below = row + 1; below < 3; below++) {
      double sum = 0;
      for (int index = 0; index < row; index++) sum += lower[below][index] * upper[index][row];
      lower[below][row] = (matrix[below][row] - sum) / upper[row][row];
    }
  }
  for (int row = 0; row < 3; row++) printf("%g %g %g | %g %g %g\n", lower[row][0], lower[row][1], lower[row][2], upper[row][0], upper[row][1], upper[row][2]);
  return 0;
}
