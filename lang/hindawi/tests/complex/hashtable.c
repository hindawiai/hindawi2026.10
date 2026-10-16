#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TABLE_SIZE 16

struct entry {
    char *key;
    int value;
    struct entry *next;
};

struct hashtable {
    struct entry *buckets[TABLE_SIZE];
    int count;
};

unsigned int hash(const char *key) {
    unsigned int result = 0;
    while (*key)
        result = result * 31 + *key++;
    return result % TABLE_SIZE;
}

struct hashtable *create_table() {
    struct hashtable *temp = malloc(sizeof(struct hashtable));
    for (int index = 0; index < TABLE_SIZE; index++)
        temp->buckets[index] = NULL;
    temp->count = 0;
    return temp;
}

void insert(struct hashtable *table, const char *key, int value) {
    unsigned int index = hash(key);
    struct entry *current = table->buckets[index];
    while (current) {
        if (strcmp(current->key, key) == 0) {
            current->value = value;
            return;
        }
        current = current->next;
    }
    struct entry *temp = malloc(sizeof(struct entry));
    temp->key = strdup(key);
    temp->value = value;
    temp->next = table->buckets[index];
    table->buckets[index] = temp;
    table->count++;
}

int lookup(struct hashtable *table, const char *key) {
    unsigned int index = hash(key);
    struct entry *current = table->buckets[index];
    while (current) {
        if (strcmp(current->key, key) == 0)
            return current->value;
        current = current->next;
    }
    return -1;
}

void free_table(struct hashtable *table) {
    for (int index = 0; index < TABLE_SIZE; index++) {
        struct entry *current = table->buckets[index];
        while (current) {
            struct entry *temp = current;
            current = current->next;
            free(temp->key);
            free(temp);
        }
    }
    free(table);
}

int main() {
    struct hashtable *table = create_table();
    insert(table, "alpha", 1);
    insert(table, "beta", 2);
    insert(table, "gamma", 3);
    printf("alpha: %d\n", lookup(table, "alpha"));
    printf("beta: %d\n", lookup(table, "beta"));
    printf("delta: %d\n", lookup(table, "delta"));
    printf("count: %d\n", table->count);
    free_table(table);
    return 0;
}
