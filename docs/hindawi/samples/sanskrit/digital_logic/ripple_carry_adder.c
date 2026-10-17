#include <stdio.h>
/* a four-bit ripple-carry adder built from full adders */
पूर्णाङ्क मुख्यम्(शून्य) {
  पूर्णाङ्क first = 11, second = 6, वाहः = 0, योगफलम् = 0;
  प्रति (पूर्णाङ्क bit = 0; bit < 4; bit++) {
    पूर्णाङ्क a = (first >> bit) & 1, b = (second >> bit) & 1;
    योगफलम् |= (a ^ b ^ वाहः) << bit;
    वाहः = (a & b) | (वाहः & (a ^ b));
  }
  लिख("%d carry %d\n", योगफलम्, वाहः);
  प्रत्यागम 0;
}
