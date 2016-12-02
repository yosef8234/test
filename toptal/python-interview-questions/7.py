# Q:
# Given a list of N numbers, use a single list comprehension to produce a new list that only contains those values that are:
# (a) even numbers, and
# (b) from elements in the original list that had even indices

# For example, if list[2] contains a value that is even, that value should be included in the new list, since it is also at an even index (i.e., 2) in the original list. However, if list[3] contains an even number, that number should not be included in the new list since it is at an odd index (i.e., 3) in the original list.

# A:
# A simple solution to this problem would be as follows

[x for x in list[::2] if x%2 == 0]
# For example, given the following list:

#        0   1   2   3    4    5    6    7    8
list = [ 1 , 3 , 5 , 8 , 10 , 13 , 18 , 36 , 78 ]
# the list comprehension [x for x in list[::2] if x%2 == 0] will evaluate to:
# list[::2] -> [1, 5, 10, 18, 78]

[10, 18, 78]
# The expression works by first taking the numbers that are at the even indices, and then filtering out all the odd numbers.

