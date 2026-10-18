#include <stdio.h>
/* file systems: the largest file an inode with 12 direct, one single, one double and one triple indirect pointer can map */
int main(void) {
  long long block = 1024, pointers = block / 4;
  long long blocks = 12 + pointers + pointers * pointers + pointers * pointers * pointers;
  printf("%lld blocks, %lld bytes\n", blocks, blocks * block);
  return 0;
}
