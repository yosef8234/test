# QUESTION: Implement an algorithm to determine if a string has all unique characters.
# Assuming ASCII (non-extended) 128 max unique characters

testString = 'abc'

def isUniqueChars(str):
    if len(str) > 128:
        return False
    arr = [False] * 128 # arr [False, False, False,..]
    for char in str:
        if arr[ord(char)] is False: # ord('a') 97
            arr[ord(char)] == True
        else:
            return False
    return True

print(isUniqueChars(testString)) #True