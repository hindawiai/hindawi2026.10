#include <stdio.h>
/* groups: check closure, associativity, identity and inverses for multiplication modulo a number */
int is_group(int size) {
  int identity = -1;
  for (int first = 1; first < size; first++)
    for (int second = 1; second < size; second++)
      if (first * second % size == 0) return 0;                         /* not closed on 1..size-1 */
  for (int first = 1; first < size; first++)
    for (int second = 1; second < size; second++)
      for (int third = 1; third < size; third++)
        if (first * second % size * third % size != first * (second * third % size) % size) return 0;
  for (int first = 1; first < size && identity < 0; first++) {
    int works = 1;
    for (int second = 1; second < size; second++) if (first * second % size != second) works = 0;
    if (works) identity = first;
  }
  for (int first = 1; first < size; first++) {
    int found = 0;
    for (int second = 1; second < size; second++) if (first * second % size == identity) found = 1;
    if (!found) return 0;
  }
  return identity > 0;
}
int main(void) { printf("%d %d %d\n", is_group(5), is_group(7), is_group(8)); return 0; }
