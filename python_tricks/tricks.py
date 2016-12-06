# Trick #1
# Reversing a string in Python

a = "python"
print("Reverse string is",a[::-1])

# Trick #2
# Transposing a Matrix

mat = [[1, 2, 3], [4, 5, 6]]
zip(*mat) # [(1, 4), (2, 5), (3, 6)]

# Trick #3
# Store all three values of the list in 3 new variables

a = [1, 2, 3]
x, y, z = a

# Trick #4
# Create a single string from all the elements in list above.

a = ["Code", "123", "Python", "Developer"]
print(" ".join(a)) #Code 123 Python Developer

# Trick #5
# Write a Python code to print
# ap
# bq
# cr
# ds

list1 = ['a', 'b', 'c', 'd']
list2 = ['p', 'q', 'r', 's']

for x, y in zip(list1,list2):
    print x, y

# Trick #6
# Swap two numbers with one line of code.

a=7
b=5
b, a = a, b
a #5
b #7

# Trick #7
# print "codecodecodecode mentormentormentormentormentor" without using loops

print("code"*4+' '+"mentor"*5)

# Trick #8
# Convert it to a single list without using any loops.
# Output:- [1, 2, 3, 4, 5, 6]

a = [[1, 2], [3, 4], [5, 6]]
import itertools
list(itertools.chain.from_iterable(a)) #[1, 2, 3, 4, 5, 6]

# Trick #9
# Checking if two words are anagrams

from collections import Counter
def is_anagram(str1, str2):
    """Checks whether the words are anagrams.
    str1: string
    str2: string
    returns: boolean
    """
    return Counter(str1) == Counter(str2)
is_anagram('abcd','dbca') #True
is_anagram('abcd','dbaa') #False

# Trick #10.
# Take a string input.
# For example "1 2 3 4" and return [1, 2, 3, 4]
# Remember list being returned has integers in it. Don't use more than one line of code.

a = "1 2 3 4"
result = map(lambda x:int(x), a.split())
print(result)