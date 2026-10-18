#include <stdio.h>
/* regular expressions: a matcher for literals, . and * (with ^ and $ anchors) */
int match_here(const char *pattern, const char *text);
int match_star(int symbol, const char *pattern, const char *text) {
  do { if (match_here(pattern, text)) return 1; } while (*text != '\0' && (*text++ == symbol || symbol == '.'));
  return 0;
}
int match_here(const char *pattern, const char *text) {
  if (pattern[0] == '\0') return 1;
  if (pattern[1] == '*') return match_star(pattern[0], pattern + 2, text);
  if (pattern[0] == '$' && pattern[1] == '\0') return *text == '\0';
  if (*text != '\0' && (pattern[0] == '.' || pattern[0] == *text)) return match_here(pattern + 1, text + 1);
  return 0;
}
int match(const char *pattern, const char *text) {
  if (pattern[0] == '^') return match_here(pattern + 1, text);
  do { if (match_here(pattern, text)) return 1; } while (*text++ != '\0');
  return 0;
}
int main(void) { printf("%d %d %d %d\n", match("^ab*c$", "abbbc"), match("a.c", "xxabcxx"), match("^ab*c$", "abd"), match("b*$", "")); return 0; }
