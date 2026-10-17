#include <stdio.h>
/* activity selection: activities sorted by finish time */
पूर्णाङ्क मुख्यम्(शून्य) {
  पूर्णाङ्क आरम्भः[] = {1, 3, 0, 5, 8, 5}, समाप्तिः[] = {2, 4, 6, 7, 9, 9}, गणना_2 = 6, last = 0, योगः = 1;
  लिख("0 ");
  प्रति (पूर्णाङ्क next = 1; next < गणना_2; next++)
    यदि (आरम्भः[next] >= समाप्तिः[last]) { लिख("%d ", next); last = next; योगः++; }
  लिख("\ntotal %d\n", योगः);
  प्रत्यागम 0;
}
