#include <stdio.h>
/* indexing: the order of B+ tree nodes for a block size, and the levels needed for a million records */
int main(void) {
  int block = 512, key = 9, pointer = 6, record_pointer = 7;
  int internal = (block + key) / (key + pointer);                  /* p pointers and p - 1 keys fit in a block */
  int leaf = (block - pointer) / (key + record_pointer);             /* keys with record pointers, and one next-leaf pointer */
  long records = 1000000, reach = leaf;
  int levels = 1;
  while (reach < records) { reach *= internal; levels++; }
  printf("internal %d leaf %d levels %d\n", internal, leaf, levels);
  return 0;
}
