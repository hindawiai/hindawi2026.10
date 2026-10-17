#include <stdio.h>
/* Floyd-Warshall all-pairs shortest paths; 999 means no edge */
पूर्णाङ्क मुख्यम्(शून्य) {
  पूर्णाङ्क distance[4][4] = {{0,5,999,10},{999,0,3,999},{999,999,0,1},{999,999,999,0}};
  प्रति (पूर्णाङ्क via = 0; via < 4; via++)
    प्रति (पूर्णाङ्क from = 0; from < 4; from++)
      प्रति (पूर्णाङ्क to = 0; to < 4; to++)
        यदि (distance[from][via] + distance[via][to] < distance[from][to]) distance[from][to] = distance[from][via] + distance[via][to];
  प्रति (पूर्णाङ्क from = 0; from < 4; from++) { प्रति (पूर्णाङ्क to = 0; to < 4; to++) लिख("%d ", distance[from][to]); लिख("\n"); }
  प्रत्यागम 0;
}
