# Best Case Time: O(n)
# Worst Case Time: O(n^2)
# Average Case Time: O(n^2)

import numpy as np

def insertion_sort(array):
    n = len(array)
    for i in range(n-1):
        j = i
        while (j+1 > 0) and (array[j] > array[j+1]):
            array[j], array[j+1] = array[j+1], array[j]
            j -= 1
    return array

# Input:
insertion_sort([]) == []

# Output:
# True

# Input:
array = list(np.random.randint(100, size=120))
np.array_equal(insertion_sort(array), np.sort(array))

# Output:
# True