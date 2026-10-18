#include <stdio.h>
/* runtime environments: the activation records a recursive factorial pushes, kept on an explicit stack */
struct frame { int argument, result, depth; } stack[16];
int top = 0, deepest = 0;
int factorial(int argument) {
  struct frame *record = &stack[top++];
  record->argument = argument; record->depth = top;
  if (top > deepest) deepest = top;
  record->result = argument <= 1 ? 1 : argument * factorial(argument - 1);
  top--;
  return record->result;
}
int main(void) {
  int result = factorial(5);
  for (int index = 0; index < deepest; index++) printf("%d:%d ", stack[index].argument, stack[index].result);
  printf("\nresult %d, deepest %d frames\n", result, deepest);
  return 0;
}
