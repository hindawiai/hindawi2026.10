#include <stdio.h>
/* CRC-32, the polynomial Ethernet uses, bit by bit */
unsigned crc32(ध्रुव वर्ण *पाठः) {
  unsigned चक्रीयपरीक्षा = 0xFFFFFFFFu;
  प्रति (पूर्णाङ्क index = 0; पाठः[index]; index++) {
    चक्रीयपरीक्षा ^= (unsigned वर्ण)पाठः[index];
    प्रति (पूर्णाङ्क bit = 0; bit < 8; bit++) चक्रीयपरीक्षा = (चक्रीयपरीक्षा >> 1) ^ (0xEDB88320u & -(चक्रीयपरीक्षा & 1));
  }
  प्रत्यागम ~चक्रीयपरीक्षा;
}
पूर्णाङ्क मुख्यम्(शून्य) { लिख("%08X\n", crc32("The quick brown fox jumps over the lazy dog")); प्रत्यागम 0; }
