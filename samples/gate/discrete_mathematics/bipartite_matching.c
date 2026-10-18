#include <stdio.h>
/* graphs: maximum matching of students to courses by augmenting paths */
int wants[4][4] = {{1,1,0,0},{1,0,0,0},{0,1,1,0},{0,0,1,1}}, course_of[4], student_of[4], visited[4];
int assign(int student) {
  for (int course = 0; course < 4; course++)
    if (wants[student][course] && !visited[course]) {
      visited[course] = 1;
      if (student_of[course] < 0 || assign(student_of[course])) { student_of[course] = student; course_of[student] = course; return 1; }
    }
  return 0;
}
int main(void) {
  int total = 0;
  for (int index = 0; index < 4; index++) student_of[index] = -1;
  for (int student = 0; student < 4; student++) {
    for (int index = 0; index < 4; index++) visited[index] = 0;
    total += assign(student);
  }
  for (int student = 0; student < 4; student++) printf("%d-%d ", student, course_of[student]);
  printf("\nmatched %d\n", total);
  return 0;
}
