#include <stdio.h>
/* IPv4: fragmenting a 4000-byte datagram (20-byte header) for a 1500-byte MTU; offsets are in 8-byte units */
int main(void) {
  int total = 4000, header = 20, largest = 1500, data = total - header, room = (largest - header) / 8 * 8, offset = 0;
  while (data > 0) {
    int size = data > room ? room : data, more = data > room;
    printf("length %d offset %d more %d\n", size + header, offset / 8, more);
    offset += size; data -= size;
  }
  return 0;
}
