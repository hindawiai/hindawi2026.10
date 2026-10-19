/* wasm.c: the original acii2cisr() (Chintamani APCISR, 2003-2006) exported to the browser, with its trace. */
#include "acii2csr.h"
#include "trace_apcisr.h"
cisr retval;
TR tr[TR_MAX]; int tr_n;
static cisr out;
static unsigned char inbuf[4096];
__attribute__((export_name("in_ptr"))) unsigned char *in_ptr (void) { return inbuf; }
__attribute__((export_name("run"))) cisr *run (int cpos) { tr_n = 0; out = acii2cisr (inbuf, cpos); return &out; }
__attribute__((export_name("tr_ptr"))) TR *tr_ptr (void) { return tr; }
__attribute__((export_name("tr_count"))) int tr_count (void) { return tr_n; }
__attribute__((export_name("tr_size"))) int tr_size (void) { return sizeof (TR); }
