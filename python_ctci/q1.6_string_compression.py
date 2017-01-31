# Implement a method to perform basic string compression using the counts of repeated characters method.
# "aabccccaaa" -> "a2b1c4a3"
# "cat" -> "c1a1t1"
# Return original string if result is not smaller than the original
# String can contain only upper and lower case letters (a-z) (A-Z)

def StringCompession(str1):
    res = []
    cnt = 0
    prev = str1[0]
    for char in str1:
        if char == prev:
            cnt += 1
        else:
            res += prev + str(cnt)
            prev = char
            cnt = 1
    res += prev + str(cnt)
    res = ''.join(res)
    if len(res) < len(str1):
        return res
    else:
        return str1

print(StringCompession("aabccccaaa")) #a2b1c4a3
print(StringCompession("bbbaaazz")) #b3a3z2
print(StringCompession("bbbaaazzasq")) #bbbaaazzasq