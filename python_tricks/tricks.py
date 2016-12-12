# Trick #1
# Reversing a string\list in Python

a = "python"
print("Reverse string is",a[::-1])

my_list = ['a','b','c','d','e']
reverse_list = my_list[::-1]

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

# Trick #11
# Use the Python 3 print function in Python 2

from __future__ import print_function
print('Python', 'Tips', sep='-', end='')

import sys
print('There was an error!', file=sys.stderr)

with open(filename, 'w') as f:
    print('Python!', file=f)

# Trick #12
# List slice assignment

my_list = ['a','b','c','d','e']
my_list[3:] = ['x','y','z']
print(my_list) # output : ['a', 'b', 'c', 'x', 'y', 'z']

# Trick #13
# Copy a List

a = [1, 2, 3, 4]
''' Considered as one of the weirdest syntax to copy elements.'''
a_copy = a[:]

''' Another way of copying a list.'''
a_copy2 = list()
a_copy2.extend(a) # output a_copy2 = [1, 2, 3, 4]

# Trick #14
# Create a list out of string

data = "abcd"
data_list2 = list(data)  # OutPut: data_list = ['a', 'b', 'c', 'd']

# Trick #15
# Print elements of a list by unpacking (only Python 3)

my_list = [1, 2, 3, 4]
print(*my_list, sep='\t')   # Print elements of my_list separated by a tab

# Trick #16
# Check file or directory exists
# os.path.isfile used only for files

import os.path
os.path.isfile(filename) # True if file exists
os.path.isfile(dirname) # False if directory exists
# os.path.exists used for both files and directories

import os.path
os.path.exists(filename) # True if file exists
os.path.exists(dirname) #True if directory exists
# pathlib.Path method (included in Python 3+, installable with pip for Python 2)

from pathlib import Path
Path(filename).exists()

# Trick #17
# Call an external command

from subprocess import call
call(['ls','-l'])

# Trick #18
# Capture output from an external command

from subprocess import check_output
output = check_output(['ls', '/usr/bin'])

# You can also capture stderr at the same time.

from subprocess import check_output, STDOUT, CalledProcessError
try:
    output = check_output(['ls', '/nonexistent'], stderr=STDOUT)
except CalledProcessError:
    print('Error: {}'.format(output.decode()))
else:
    print('Success: {}'.format(output.decode()))

# Trick #19
# else in for loop
# An else block is executed if the loop body is not terminated by a break statement :

for i in range(5):
    print('Here we go!')
    if i == 2:
        break
else:
    print('There we went.')
# output : Here we go!
#          Here we go!
#          Here we go!

# This for loop will get all the way to else:
for i in range(5):
    print('Here we go!')
    if i == 10:
        break
else:
    print('There we went.')
# output : Here we go!
#          Here we go!
#          Here we go!
#          Here we go!
#          Here we go!
#          There we went.

# Trick #20
# Print to file
# Using `with` and `open`, the file will be closed when the `with` block finishes.

with open(filename, 'w') as outputfile:
    print('Python!', file=outputfile)

# Trick #21
# Reading from file

with open('file.txt', 'r') as inputfile:
    data = inputfile.read()

# Trick #22
# Iterating over lines in a file
# When iterating over lines in a file, this method uses less memory because it reads one line at a time.

with open(filename, 'r') as inputfile:
    for line in inputfile:
        # Lines have a '\n' at the end, like inputfile.readlines().
        print(line, end='')

# Trick #23
# Accessing attributes which start with underscores
# “Private” instance variables that cannot be accessed except from inside an object don’t exist in Python. Since there is a valid use-case for class-private members (namely to avoid name clashes of names with names defined by subclasses), there is limited support for such a mechanism, called name mangling. Any identifier of the form __spam (at least two leading underscores, at most one trailing underscore) is textually replaced with _classname__spam, where classname is the current class name with leading underscore(s) stripped.
# So to access attributes which start with underscores simply run obj_name._ClassName__attr_name .

class MyClass:
    def __init__(self):
        self.__private_attr = None
    def set_private_attr(self, attr_to_private):
        self.__private_attr = attr_to_private

attr = 7
my_class = MyClass()
my_class.set_private_attr(attr)
print(my_class._MyClass__private_attr) #7

# Trick #24
# Trick #25
# Trick #26
