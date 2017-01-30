# Given two strings, write a method to decide if one is a permutation of the other.
# For example string abc is a premutation of cbc

def checkPermutaion(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        return ''.join(sorted(str1)) == ''.join(sorted(str2))

print(checkPermutaion('abc','cba')) # True