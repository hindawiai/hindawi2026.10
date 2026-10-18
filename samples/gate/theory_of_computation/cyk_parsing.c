#include <stdio.h>
#include <string.h>
/* context-free grammars: CYK parsing for S->AB|BC, A->BA|a, B->CC|b, C->AB|a (symbols S=1, A=2, B=4, C=8 as bits) */
int main(void) {
  int rules[5][3] = {{1, 2, 4}, {1, 4, 8}, {2, 4, 2}, {4, 8, 8}, {8, 2, 4}};   /* head, first, second */
  const char *word = "baaba";
  int length = strlen(word), table[8][8] = {{0}};
  for (int index = 0; index < length; index++) table[index][index] = word[index] == 'a' ? (2 | 8) : 4;
  for (int span = 2; span <= length; span++)
    for (int start = 0; start + span - 1 < length; start++)
      for (int split = start; split < start + span - 1; split++)
        for (int rule = 0; rule < 5; rule++)
          if ((table[start][split] & rules[rule][1]) && (table[split + 1][start + span - 1] & rules[rule][2]))
            table[start][start + span - 1] |= rules[rule][0];
  printf("%s\n", table[0][length - 1] & 1 ? "accepted" : "rejected");
  return 0;
}
