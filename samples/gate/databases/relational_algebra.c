#include <stdio.h>
/* relational algebra: selection, projection and natural join over two small relations */
int student[4][2] = {{1, 81}, {2, 72}, {3, 95}, {4, 60}};              /* (id, marks) */
int course[5][2] = {{3, 101}, {1, 102}, {3, 103}, {5, 104}, {2, 105}};  /* (id, course) */
int main(void) {
  printf("select marks > 70:");
  for (int row = 0; row < 4; row++) if (student[row][1] > 70) printf(" (%d,%d)", student[row][0], student[row][1]);
  printf("\nproject course ids:");
  for (int row = 0; row < 5; row++) {
    int seen = 0;
    for (int prior = 0; prior < row; prior++) if (course[prior][0] == course[row][0]) seen = 1;
    if (!seen) printf(" %d", course[row][0]);
  }
  printf("\njoin on id:");
  for (int first = 0; first < 4; first++)
    for (int second = 0; second < 5; second++)
      if (student[first][0] == course[second][0]) printf(" (%d,%d,%d)", student[first][0], student[first][1], course[second][1]);
  printf("\n");
  return 0;
}
