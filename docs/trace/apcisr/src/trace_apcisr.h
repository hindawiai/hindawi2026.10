#ifndef TRACE_APCISR_H
#define TRACE_APCISR_H
#include <string.h>
#define TR_MAX 512
#define TR_W 96
typedef struct { int matrik, lipik, purak, purna, varna_purna, prev_hal, prev_ra_hal, flag, entry, offset;
                 unsigned char u[TR_W], m[TR_W], n[TR_W]; } TR;
extern TR tr[TR_MAX]; extern int tr_n;
#define APCISR_TRACE do { if (tr_n < TR_MAX) { TR *t_ = &tr[tr_n++]; t_->matrik = matrik; t_->lipik = lipik; \
  t_->purak = purak; t_->purna = purna; t_->varna_purna = varna_purna; t_->prev_hal = prev_hal; \
  t_->prev_ra_hal = prev_ra_hal; t_->flag = flag; t_->entry = i; t_->offset = (int) (aci - actmp); \
  memcpy (t_->u, urdha, TR_W); memcpy (t_->m, madhya, TR_W); memcpy (t_->n, nimna, TR_W); } } while (0)
#endif
