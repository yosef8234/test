# Best Case Time: O(n)
# Worst Case Time: O(n^2)
# Average Case Time: O(n^2)

import numpy as np

# Sort while moving forward or backward
def partly_sort(array, i, forward):
    n = len(array)
    # Range of forward traverse
    if forward == True:
        interval = range(i, n-i-1)
    # Range of backward traverse
    elif forward == False:
        interval = reversed(range(i, n-i-2))
    # Partly sort
    changed = False
    for j in interval:
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
            changed = True
    return (array, changed)

# Cocktail sort
def cocktail_sort(array):
    n = len(array)
    for i in range(n):
        (array, changed) = partly_sort(array, i, True)
        if not changed:
            break
        (array, changed) = partly_sort(array, i, False)
        if not changed:
            break
    return array

# Input:
cocktail_sort([]) == []

# Output:
# True

# Input:
array = [i for i in range(10)]
cocktail_sort(array) == array

# Output:
# True

# Input:
array = list(np.random.randint(100, size=120))
np.array_equal(cocktail_sort(array), np.sort(array))

# Output:
# True