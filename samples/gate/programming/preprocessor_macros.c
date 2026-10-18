#include <stdio.h>
/* the preprocessor: object-like and function-like macros, and conditional compilation */
#define SIZE 5
#define SQUARE(value) ((value) * (value))
#ifndef LIMIT
#define LIMIT 20
#endif
int main(void) {
  int total = 0;
  for (int index = 1; index <= SIZE; index++) total += SQUARE(index);
#ifdef LIMIT
  printf("%d %d\n", total, total > LIMIT);
#else
  printf("%d\n", total);
#endif
  return 0;
}
