# binary search, in Python
def binary_search(values, key):
    low, high = 0, len(values) - 1
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == key:
            return middle
        if values[middle] < key:
            low = middle + 1
        else:
            high = middle - 1
    return -1

print(binary_search([2, 5, 8, 12, 16, 23, 38], 23), binary_search([2, 5, 8], 7))
