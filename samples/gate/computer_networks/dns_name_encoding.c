#include <stdio.h>
#include <string.h>
/* DNS: a domain name in the wire format of a query, each label preceded by its length, ending with zero */
int main(void) {
  const char *text = "www.example.com";
  unsigned char out[64]; int size = 0, start = 0;
  for (int index = 0; ; index++)
    if (text[index] == '.' || text[index] == '\0') {
      out[size++] = index - start;
      memcpy(out + size, text + start, index - start); size += index - start;
      start = index + 1;
      if (text[index] == '\0') break;
    }
  out[size++] = 0;
  for (int index = 0; index < size; index++) printf(out[index] < 32 ? "[%d]" : "%c", out[index]);
  printf(" (%d bytes)\n", size);
  return 0;
}
