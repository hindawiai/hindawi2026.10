#include <stdio.h>
/* towers of Hanoi */
पूर्णाङ्क चालाः = 0;
शून्य hanoi(पूर्णाङ्क चक्रिकाः, वर्ण from, वर्ण to, वर्ण spare) {
  यदि (चक्रिकाः == 0) प्रत्यागम;
  hanoi(चक्रिकाः - 1, from, spare, to);
  लिख("%c>%c ", from, to); चालाः++;
  hanoi(चक्रिकाः - 1, spare, to, from);
}
पूर्णाङ्क मुख्यम्(शून्य) { hanoi(3, 'A', 'C', 'B'); लिख("\nmoves %d\n", चालाः); प्रत्यागम 0; }
