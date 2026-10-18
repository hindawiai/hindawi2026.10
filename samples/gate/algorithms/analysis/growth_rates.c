#include <stdio.h>
/* asymptotic analysis: count the basic steps of linear search, binary search and insertion sort as the size grows */
int main(void) {
  for (int size = 16; size <= 4096; size *= 4) {
    long linear = size, binary = 0, sorting = 0;
    for (int low = 0, high = size - 1; low <= high; binary++) { int middle = (low + high) / 2; if (middle < size - 1) low = middle + 1; else high = middle - 1; }
    for (int next = 1; next < size; next++) sorting += next;           /* worst case: reverse order */
    printf("%d: %ld %ld %ld\n", size, linear, binary, sorting);
  }
  return 0;
}
