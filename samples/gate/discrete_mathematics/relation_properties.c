#include <stdio.h>
/* sets and relations: is a relation on {0,1,2,3} reflexive, symmetric, antisymmetric, transitive? */
int main(void) {
  int relation[4][4] = {{1,1,0,0},{0,1,1,0},{0,0,1,1},{0,0,0,1}};
  int reflexive = 1, symmetric = 1, antisymmetric = 1, transitive = 1;
  for (int first = 0; first < 4; first++) {
    reflexive &= relation[first][first];
    for (int second = 0; second < 4; second++) {
      if (relation[first][second] != relation[second][first]) symmetric = 0;
      if (first != second && relation[first][second] && relation[second][first]) antisymmetric = 0;
      for (int third = 0; third < 4; third++)
        if (relation[first][second] && relation[second][third] && !relation[first][third]) transitive = 0;
    }
  }
  printf("%d %d %d %d\n", reflexive, symmetric, antisymmetric, transitive);
  return 0;
}
