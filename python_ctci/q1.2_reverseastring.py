# Write code to reverse a String
# abcd -> dcba

def reverseString_pythonic(str):
    return str[::-1]

def reverseString_slow(str):
    stack = [] # ['h', 'e', 'l', 'l', 'o']
    for char in str:
        stack.append(char)
    result = ""
    while len(stack) > 0:
        result = result + stack.pop() # o l l e h
    return result

print(reverseString_slow("hello")) #olleh