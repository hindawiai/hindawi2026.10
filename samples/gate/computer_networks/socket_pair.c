#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/wait.h>
/* the socket API: a connected pair of sockets; the child answers each message in capitals */
int main(void) {
  int ends[2];
  socketpair(AF_UNIX, SOCK_STREAM, 0, ends);
  if (fork() == 0) {
    char text[64]; ssize_t length = read(ends[1], text, sizeof text);
    for (ssize_t index = 0; index < length; index++) text[index] = toupper((unsigned char)text[index]);
    exit(write(ends[1], text, length) == length ? 0 : 1);
  }
  const char *message = "hello over a socket";
  char reply[64] = {0};
  if (write(ends[0], message, strlen(message)) < 0 || read(ends[0], reply, sizeof reply - 1) < 0) return 1;
  wait(NULL);
  printf("%s\n", reply);
  return 0;
}
