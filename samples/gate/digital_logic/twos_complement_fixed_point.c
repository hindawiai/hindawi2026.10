#include <stdio.h>
#include <stdint.h>
/* number representation: two's complement in eight bits, overflow, and fixed-point (Q4.4) multiplication */
int main(void) {
  int8_t value = -5;
  int sum = 100 + 50;
  int overflow = sum > 127 || sum < -128;
  int first = (int)(2.5 * 16), second = (int)(1.75 * 16), product = (first * second) >> 4;
  printf("%02X %d %d %.4f\n", (uint8_t)value, (int8_t)sum, overflow, product / 16.0);
  return 0;
}
