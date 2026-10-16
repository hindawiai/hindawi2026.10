#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int *data, int low, int high) {
    int pivot = data[high];
    int index = low - 1;
    for (int current = low; current < high; current++) {
        if (data[current] < pivot) {
            index++;
            swap(&data[index], &data[current]);
        }
    }
    swap(&data[index + 1], &data[high]);
    return index + 1;
}

void quicksort(int *data, int low, int high) {
    if (low < high) {
        int pivot_index = partition(data, low, high);
        quicksort(data, low, pivot_index - 1);
        quicksort(data, pivot_index + 1, high);
    }
}

void print_array(int *data, int size) {
    for (int index = 0; index < size; index++)
        printf("%d ", data[index]);
    printf("\n");
}

int main() {
    int data[] = {64, 34, 25, 12, 22, 11, 90, 88, 45, 50, 23, 36};
    int size = 12;
    printf("Before: ");
    print_array(data, size);
    quicksort(data, 0, size - 1);
    printf("After: ");
    print_array(data, size);
    return 0;
}
