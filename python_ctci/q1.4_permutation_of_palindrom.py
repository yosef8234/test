# Write a function to check if a string is a permutation of a palindrome.
# Permutation it is "abc" == "cba"
# Palindrome it is "Madam, I'm Adam'
# A palindrome is word or phrase that is the same backwards as it is forwards. (Not limited to dictionary words)
# A permutation is a rearrangement of letters.

import string

def isPermutationOfPalindrome(str):
    # {'a': False, 'c': False, 'b': False, 'e': False, 'd': False, 'g': False, 'f': False, 'i': False, 'h': False, 'k': False, 'j': False, 'm': False, 'l': False, 'o': False, 'n': False, 'q': False, 'p': False, 's': False, 'r': False, 'u': False, 't': False, 'w': False, 'v': False, 'y': False, 'x': False, 'z': False}
    d = dict.fromkeys(string.ascii_lowercase, False)
    count = 0
    for char in str:
        if(ord(char) > 96 and ord(char) < 123):
            d[char] = not d[char]
    for key in d:
        if d[key] is True:
            count += 1
            if count > 1:
                return False
    return True


print(isPermutationOfPalindrome("abcecba")) # True
print(isPermutationOfPalindrome("aa bb cc eee f")) # False