#include <stdio.h>
#include <string.h>
/* HTTP: read the request line and count the header lines of a request */
int main(void) {
  char text[] = "GET /index.html HTTP/1.1\r\nHost: example.com\r\nAccept: text/html\r\nConnection: close\r\n\r\n";
  char method[16], path[64], version[16];
  sscanf(text, "%15s %63s %15s", method, path, version);
  int headers = 0;
  for (char *line = strstr(text, "\r\n") + 2; strncmp(line, "\r\n", 2) != 0; line = strstr(line, "\r\n") + 2) headers++;
  printf("%s %s %s, %d headers\n", method, path, version, headers);
  return 0;
}
