#include <stdio.h>
#include "lib.h"
// the counter starts at the value
int main(void)
{
  int counter = VALUE;
  int total = add_values(counter, LIMIT);
  if (total > 0) printf("%d\n", total); else printf("none\n");
  return 0;
}
