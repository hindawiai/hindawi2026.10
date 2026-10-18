#include <stdio.h>
/* minimisation: prime implicants by the tabular (Quine-McCluskey) method for f = sum of minterms 0,1,2,5,6,7,8,9,10,14 */
int value[64], mask[64], used[64], count = 0;
int main(void) {
  int minterms[] = {0, 1, 2, 5, 6, 7, 8, 9, 10, 14};
  for (int index = 0; index < 10; index++) { value[count] = minterms[index]; mask[count++] = 0; }
  for (int start = 0, end = count; start < end; start = end, end = count)
    for (int first = start; first < end; first++)
      for (int second = first + 1; second < end; second++) {
        int differ = value[first] ^ value[second];
        if (mask[first] != mask[second] || (differ & (differ - 1))) continue;
        used[first] = used[second] = 1;
        int known = 0;
        for (int index = end; index < count; index++) if (mask[index] == (mask[first] | differ) && value[index] == (value[first] & ~differ)) known = 1;
        if (!known) { value[count] = value[first] & ~differ; mask[count++] = mask[first] | differ; }
      }
  for (int index = 0; index < count; index++) {
    if (used[index]) continue;
    for (int bit = 3; bit >= 0; bit--) putchar(mask[index] >> bit & 1 ? '-' : '0' + (value[index] >> bit & 1));
    putchar(' ');
  }
  printf("\n");
  return 0;
}
