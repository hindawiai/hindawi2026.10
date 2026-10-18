#include <stdio.h>
/* combinatorics: binary strings with no two adjacent ones (a recurrence), and Catalan numbers, by table */
int main(void) {
  long strings[16] = {1, 2}, catalan[16] = {1};
  for (int length = 2; length < 16; length++) strings[length] = strings[length - 1] + strings[length - 2];
  for (int size = 1; size < 16; size++)
    for (int left = 0; left < size; left++) catalan[size] += catalan[left] * catalan[size - 1 - left];
  printf("%ld %ld\n", strings[10], catalan[10]);
  return 0;
}
