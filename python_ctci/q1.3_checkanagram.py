# Write a method to decide if two strings are anagrams or not
# listen == silent

def checkAnagram(str1, str2):
    if ''.join(sorted(str1.lower())).strip() == ''.join(sorted(str2.lower())).strip():
        return True
    else:
        return False

print(checkAnagram('listen','silent')) # True