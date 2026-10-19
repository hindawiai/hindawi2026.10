#include <stdio.h>
#include <string.h>
#include "acii2csr.h"
cisr retval;
#ifdef TRACED
#include "trace_apcisr.h"
TR tr[TR_MAX]; int tr_n;
#endif
int main(void) { char line[2048]; static unsigned char in[2048];
  while (fgets(line, sizeof line, stdin)) { line[strcspn(line, "\n")] = 0; strcpy((char *) in, line);
    cisr r = acii2cisr(in, 0); int k;
    for (k = 0; k < 1024 && (r.urdha[k] || r.madhya[k] || r.nimna[k]); k++) printf("%02x%02x%02x ", (unsigned char) r.urdha[k], (unsigned char) r.madhya[k], (unsigned char) r.nimna[k]);
    printf("| %d\n", r.curpos); }
  return 0; }
