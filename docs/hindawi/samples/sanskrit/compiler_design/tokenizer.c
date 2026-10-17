#include <stdio.h>
#include <ctype.h>
/* a hand-written lexer: identifiers, numbers and operators */
पूर्णाङ्क मुख्यम्(शून्य) {
  वर्ण स्रोतः[] = "total = count1 + 42 * rate;";
  पूर्णाङ्क index = 0, शब्दांशाः = 0;
  यावत् (स्रोतः[index]) {
    यदि (isspace(स्रोतः[index])) { index++; अनुवर्त; }
    पूर्णाङ्क आरम्भः = index;
    यदि (isalpha(स्रोतः[index])) { यावत् (isalnum(स्रोतः[index])) index++; लिख("ID "); }
    अन्यथा यदि (isdigit(स्रोतः[index])) { यावत् (isdigit(स्रोतः[index])) index++; लिख("NUM "); }
    अन्यथा { index++; लिख("OP "); }
    शब्दांशाः++;
    (शून्य)आरम्भः;
  }
  लिख("\n%d\n", शब्दांशाः);
  प्रत्यागम 0;
}
