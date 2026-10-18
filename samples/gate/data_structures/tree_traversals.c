#include <stdio.h>
/* trees: preorder, postorder and level-order traversal of a binary tree kept in arrays */
int key[7] = {50, 30, 70, 20, 40, 60, 80}, left[7] = {1, 3, 5, -1, -1, -1, -1}, right[7] = {2, 4, 6, -1, -1, -1, -1};
void preorder(int node) { if (node < 0) return; printf("%d ", key[node]); preorder(left[node]); preorder(right[node]); }
void postorder(int node) { if (node < 0) return; postorder(left[node]); postorder(right[node]); printf("%d ", key[node]); }
int main(void) {
  preorder(0); printf("| "); postorder(0); printf("| ");
  int queue[7], head = 0, tail = 0;
  queue[tail++] = 0;
  while (head < tail) {
    int node = queue[head++];
    printf("%d ", key[node]);
    if (left[node] >= 0) queue[tail++] = left[node];
    if (right[node] >= 0) queue[tail++] = right[node];
  }
  printf("\n");
  return 0;
}
