#include <stdio.h>
#include <string.h>
/* number representation: the sign, exponent and fraction of an IEEE 754 single-precision number */
पूर्णाङ्क मुख्यम्(शून्य) {
  भिन्न सङ्ख्या = -6.25f;
  अचिह्नित द्वयङ्काः;
  स्मृतिं_प्रतिलिख(&द्वयङ्काः, &सङ्ख्या, परिमाण द्वयङ्काः);
  लिख("sign %u exponent %u fraction %06X\n", द्वयङ्काः >> 31, ((द्वयङ्काः >> 23) & 0xFF) - 127, द्वयङ्काः & 0x7FFFFF);
  प्रत्यागम 0;
}
