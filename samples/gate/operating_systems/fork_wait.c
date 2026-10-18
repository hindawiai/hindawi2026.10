#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
/* processes: fork a child that sums 1..10 and returns it as its exit status; the parent waits for it */
int main(void) {
  pid_t child = fork();
  if (child == 0) { int sum = 0; for (int number = 1; number <= 10; number++) sum += number; exit(sum); }
  int status;
  waitpid(child, &status, 0);
  printf("child returned %d\n", WEXITSTATUS(status));
  return 0;
}
