#include <stdio.h>
#include <ctype.h>
/* evaluate a postfix (reverse Polish) expression with a stack */
पूर्णाङ्क मुख्यम्(शून्य) {
  वर्ण व्यञ्जकम्[] = "3 4 + 2 * 7 -";
  पूर्णाङ्क राशिः[16], top = 0;
  प्रति (पूर्णाङ्क index = 0; व्यञ्जकम्[index]; index++) {
    वर्ण चिह्नम् = व्यञ्जकम्[index];
    यदि (isdigit(चिह्नम्)) राशिः[top++] = चिह्नम् - '0';
    अन्यथा यदि (चिह्नम् != ' ') {
      पूर्णाङ्क right = राशिः[--top], left = राशिः[--top];
      राशिः[top++] = चिह्नम् == '+' ? left + right : चिह्नम् == '-' ? left - right : चिह्नम् == '*' ? left * right : left / right;
    }
  }
  लिख("%d\n", राशिः[0]);
  प्रत्यागम 0;
}
