#include <stdio.h>
/* Euclid's algorithm */
पूर्णाङ्क महत्तमसमापवर्तकः(पूर्णाङ्क first, पूर्णाङ्क second) { प्रत्यागम second == 0 ? first : महत्तमसमापवर्तकः(second, first % second); }
पूर्णाङ्क मुख्यम्(शून्य) { पूर्णाङ्क first = 84, second = 36; लिख("%d %d\n", महत्तमसमापवर्तकः(first, second), first / महत्तमसमापवर्तकः(first, second) * second); प्रत्यागम 0; }
