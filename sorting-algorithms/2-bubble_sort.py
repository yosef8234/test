# Best Case Time: O(n)
# Worst Case Time: O(n^2)
# Average Case Time: O(n^2)

import numpy as np

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        changed = False
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                changed = True
        if not changed:
            break
    return array

# Input:
bubble_sort([]) == []

# Output:
# True

# Input:
array = [i for i in range(10)]
bubble_sort(array) == array

# Output:
# True

# Input:
array = list(np.random.randint(100, size=120))
np.array_equal(bubble_sort(array), np.sort(array))

# Output:
# True