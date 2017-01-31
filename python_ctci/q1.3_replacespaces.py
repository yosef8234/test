# Write a method to replace all spaces in a string with '%20'.
# For example "  i love python  " == "i%20love%20python"

# def replacespaces(str):
#     res = ''
#     start = False
#     for char in reversed(str):
#         if char != ' ':
#             start = True
#         if(char == ' ' and start == True):
#             res += '02%'
#         else:
#             res += char
#     return res[::-1]

# print(replacespaces("  i love python  "))

def urlifyString_pythonc(str):
    return str.strip().replace(" ", "%20")

def urlifyString(str):
    res = ''
    start = False
    str = str.strip() # Removes white space from the beginning and end of the string
    for char in str:
        if(char == ' '):
            res += '%20'
        else: res += char
    return res

print(urlifyString("       Mr John Smith           ")) # Mr%20John%20Smith
print(urlifyString_pythonc("  i love python  ")) # i%20love%20python