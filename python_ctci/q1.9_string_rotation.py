# Assume you have method isSubstring which checks if one string is a substring of another.
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring.

s1 = "waterbottle"
s2 = "erbottlewat"

def isSubstring(s1,s2):
    # if s2 in s1:
    #     return True
    # else:
    #     return False
    return True if s2 in s1 else False

def isRotation(s1,s2):
    if len(s1) != len(s2):
        return False
    else:
        s1 += s1 #waterbottlewaterbottle
        return isSubstring(s1,s2)

print(isRotation(s1,s2)) # True