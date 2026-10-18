#include <stdio.h>
/* the ALU: eight-bit addition and subtraction with zero, sign, carry and overflow flags */
void operate(int first, int second, int subtract) {
  int right = subtract ? (~second & 0xFF) : second, total = first + right + subtract;
  int result = total & 0xFF, carry = total >> 8;
  int overflow = !((first ^ right) & 0x80) && ((first ^ result) & 0x80);
  printf("%02X zero %d sign %d carry %d overflow %d\n", result, result == 0, result >> 7, carry, overflow);
}
int main(void) { operate(0x70, 0x20, 0); operate(0x30, 0x30, 1); operate(0xF0, 0x20, 0); return 0; }
