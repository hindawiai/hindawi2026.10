#include <stdio.h>
/* fractional knapsack: items already sorted by value per unit weight */
पूर्णाङ्क मुख्यम्(शून्य) {
  द्विगुण value[] = {60, 100, 120}, भारः[] = {10, 20, 30}, capacity = 50, योगः = 0;
  प्रति (पूर्णाङ्क वस्तु = 0; वस्तु < 3 && capacity > 0; वस्तु++) {
    द्विगुण taken = भारः[वस्तु] < capacity ? भारः[वस्तु] : capacity;
    योगः += value[वस्तु] * taken / भारः[वस्तु];
    capacity -= taken;
  }
  लिख("%.2f\n", योगः);
  प्रत्यागम 0;
}
