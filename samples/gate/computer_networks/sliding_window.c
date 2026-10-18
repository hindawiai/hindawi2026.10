#include <stdio.h>
/* flow control: Go-Back-N with a window of 4; frame 5 is lost once, so the sender goes back to it */
int main(void) {
  int window = 4, base = 0, next = 0, frames = 10, lost = 5, sent = 0;
  while (base < frames) {
    while (next < base + window && next < frames) { printf("%d ", next); sent++; next++; }
    if (lost >= base && lost < next) { printf("| timeout %d | ", lost); next = lost; base = lost; lost = -1; }
    else base = next;
  }
  printf("\nsent %d\n", sent);
  return 0;
}
