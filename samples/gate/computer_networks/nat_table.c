#include <stdio.h>
/* NAT: private address and port pairs mapped to ports of one public address, both ways */
int main(void) {
  unsigned private_address[3] = {0xC0A80002, 0xC0A80003, 0xC0A80002}, private_port[3] = {5000, 5000, 6000}, public_port[3];
  int count = 0;
  for (int index = 0; index < 3; index++) { public_port[count++] = 40000 + index; printf("192.168.0.%u:%u -> 203.0.113.9:%u\n", private_address[index] & 255, private_port[index], public_port[index]); }
  unsigned arriving = 40001;
  for (int index = 0; index < count; index++)
    if (public_port[index] == arriving) printf("reply to %u goes to 192.168.0.%u:%u\n", arriving, private_address[index] & 255, private_port[index]);
  return 0;
}
