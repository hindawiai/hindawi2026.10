# binary search, in Python
def binary_search(values, कुंजी):
    low, high = 0, len(values) - 1
    जबतक low <= high:
        middle = (low + high) // 2
        अगर values[middle] == कुंजी:
            वापस middle
        अगर values[middle] < कुंजी:
            low = middle + 1
        अन्यथा:
            high = middle - 1
    वापस -1

print(binary_search([2, 5, 8, 12, 16, 23, 38], 23), binary_search([2, 5, 8], 7))
