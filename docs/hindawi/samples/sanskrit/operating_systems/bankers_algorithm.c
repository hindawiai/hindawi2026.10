#include <stdio.h>
/* Banker's algorithm: find a safe sequence */
पूर्णाङ्क मुख्यम्(शून्य) {
  पूर्णाङ्क allocation[5][3] = {{0,1,0},{2,0,0},{3,0,2},{2,1,1},{0,0,2}}, maximum[5][3] = {{7,5,3},{3,2,2},{9,0,2},{2,2,2},{4,3,3}};
  पूर्णाङ्क available[3] = {3, 3, 2}, finished[5] = {0}, found = 0;
  यावत् (found < 5) {
    पूर्णाङ्क progress = 0;
    प्रति (पूर्णाङ्क कार्यम् = 0; कार्यम् < 5; कार्यम्++) {
      यदि (finished[कार्यम्]) अनुवर्त;
      पूर्णाङ्क fits = 1;
      प्रति (पूर्णाङ्क kind = 0; kind < 3; kind++) यदि (maximum[कार्यम्][kind] - allocation[कार्यम्][kind] > available[kind]) fits = 0;
      यदि (fits) { प्रति (पूर्णाङ्क kind = 0; kind < 3; kind++) available[kind] += allocation[कार्यम्][kind]; finished[कार्यम्] = 1; found++; progress = 1; लिख("P%d ", कार्यम्); }
    }
    यदि (!progress) { लिख("unsafe"); भङ्ग; }
  }
  लिख("\n");
  प्रत्यागम 0;
}
