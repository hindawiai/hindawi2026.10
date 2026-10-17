#include <stdio.h>
#include <limits.h>
/* matrix chain multiplication order */
पूर्णाङ्क मुख्यम्(शून्य) {
  पूर्णाङ्क size[] = {40, 20, 30, 10, 30}, गणना_2 = 4, मूल्यव्ययः[8][8] = {{0}};
  प्रति (पूर्णाङ्क length = 2; length <= गणना_2; length++)
    प्रति (पूर्णाङ्क first = 1; first + length - 1 <= गणना_2; first++) {
      पूर्णाङ्क last = first + length - 1;
      मूल्यव्ययः[first][last] = INT_MAX;
      प्रति (पूर्णाङ्क split = first; split < last; split++) {
        पूर्णाङ्क योगः = मूल्यव्ययः[first][split] + मूल्यव्ययः[split + 1][last] + size[first - 1] * size[split] * size[last];
        यदि (योगः < मूल्यव्ययः[first][last]) मूल्यव्ययः[first][last] = योगः;
      }
    }
  लिख("%d\n", मूल्यव्ययः[1][गणना_2]);
  प्रत्यागम 0;
}
