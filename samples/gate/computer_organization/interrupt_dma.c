#include <stdio.h>
/* I/O: the share of processor cycles spent moving a block by interrupts, word by word, and by DMA in one burst */
int main(void) {
  double words = 4096, cycles_per_interrupt = 50, cycles_per_word = 2, burst_setup = 200, block_time = 1000000;
  double interrupt_cycles = words * (cycles_per_interrupt + cycles_per_word);
  double burst_cycles = burst_setup + cycles_per_interrupt;
  printf("%.2f%% %.2f%%\n", 100 * interrupt_cycles / block_time, 100 * burst_cycles / block_time);
  return 0;
}
