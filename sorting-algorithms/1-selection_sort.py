# Best Case Time: O(n^2)
# Worst Case Time: O(n^2)
# Average Case Time: O(n^2)

import numpy as np

def argmin(array):
    # Get the index of the smallest
    # element in the array
    arg = 0
    for i in range(1, len(array)):
        if array[i] < array[arg]:
            arg = i
    return arg

def selection_sort(array):
    n = len(array)
    for i in range(n):
        j = argmin(array[i:n]) + i
        array[i], array[j] = array[j], array[i]
    return array

# Input:
selection_sort([]) == []

# Output:
# True

# Input:
array = list(np.random.randint(100, size=120))
np.array_equal(selection_sort(array), np.sort(array))

# Output:
# True