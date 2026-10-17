#include <stdio.h>
#include <limits.h>
/* Dijkstra's shortest paths from vertex 0 */
पूर्णाङ्क मुख्यम्(शून्य) {
  पूर्णाङ्क भारः[5][5] = {{0,10,0,30,100},{10,0,50,0,0},{0,50,0,20,10},{30,0,20,0,60},{100,0,10,60,0}};
  पूर्णाङ्क distance[5], done[5] = {0};
  प्रति (पूर्णाङ्क शीर्षम् = 0; शीर्षम् < 5; शीर्षम्++) distance[शीर्षम्] = INT_MAX;
  distance[0] = 0;
  प्रति (पूर्णाङ्क round = 0; round < 5; round++) {
    पूर्णाङ्क nearest = -1;
    प्रति (पूर्णाङ्क शीर्षम् = 0; शीर्षम् < 5; शीर्षम्++) यदि (!done[शीर्षम्] && (nearest < 0 || distance[शीर्षम्] < distance[nearest])) nearest = शीर्षम्;
    done[nearest] = 1;
    प्रति (पूर्णाङ्क next = 0; next < 5; next++)
      यदि (भारः[nearest][next] && distance[nearest] + भारः[nearest][next] < distance[next]) distance[next] = distance[nearest] + भारः[nearest][next];
  }
  प्रति (पूर्णाङ्क शीर्षम् = 0; शीर्षम् < 5; शीर्षम्++) लिख("%d ", distance[शीर्षम्]);
  लिख("\n");
  प्रत्यागम 0;
}
