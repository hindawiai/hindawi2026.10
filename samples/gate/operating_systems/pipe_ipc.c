#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
/* inter-process communication: the parent sends numbers down one pipe, the child sends their sum back up another */
int main(void) {
  int down[2], up[2];
  if (pipe(down) != 0 || pipe(up) != 0) return 1;
  if (fork() == 0) {
    int number, sum = 0;
    close(down[1]);
    while (read(down[0], &number, sizeof number) == sizeof number) sum += number;
    exit(write(up[1], &sum, sizeof sum) == sizeof sum ? 0 : 1);
  }
  close(down[0]);
  for (int number = 1; number <= 100; number++) if (write(down[1], &number, sizeof number) != sizeof number) return 1;
  close(down[1]);
  int sum;
  if (read(up[0], &sum, sizeof sum) != sizeof sum) return 1;
  wait(NULL);
  printf("%d\n", sum);
  return 0;
}
