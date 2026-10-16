#include <stdio.h>
#include <stdlib.h>

struct नोड {
    int मान;
    struct नोड *अग्र;
};

struct नोड *नूतन(int म) {
    struct नोड *न = malloc(sizeof(struct नोड));
    न->मान = म;
    न->अग्र = NULL;
    return न;
}

void मुद्रण(struct नोड *शीर्ष) {
    while (शीर्ष) {
        printf("%d ", शीर्ष->मान);
        शीर्ष = शीर्ष->अग्र;
    }
    printf("\n");
}

int main() {
    struct नोड *क = नूतन(1);
    क->अग्र = नूतन(2);
    क->अग्र->अग्र = नूतन(3);
    मुद्रण(क);
    return 0;
}
