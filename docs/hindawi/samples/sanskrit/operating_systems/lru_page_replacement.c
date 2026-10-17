#include <stdio.h>
/* least recently used page replacement with three frames: count the faults */
पूर्णाङ्क मुख्यम्(शून्य) {
  पूर्णाङ्क pages[] = {7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2}, चौकटः[3] = {-1, -1, -1}, used[3] = {0}, faults = 0;
  प्रति (पूर्णाङ्क time = 0; time < 13; time++) {
    पूर्णाङ्क hit = -1;
    प्रति (पूर्णाङ्क स्थानम् = 0; स्थानम् < 3; स्थानम्++) यदि (चौकटः[स्थानम्] == pages[time]) hit = स्थानम्;
    यदि (hit < 0) {
      hit = 0;
      प्रति (पूर्णाङ्क स्थानम् = 1; स्थानम् < 3; स्थानम्++) यदि (used[स्थानम्] < used[hit]) hit = स्थानम्;
      चौकटः[hit] = pages[time]; faults++;
    }
    used[hit] = time + 1;
  }
  लिख("%d\n", faults);
  प्रत्यागम 0;
}
