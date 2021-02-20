"""

Given a string, compute recursively (no loops) the number of times lowercase "hi" appears in the string.

countHi("xxhixx") → 1
countHi("xhixhix") → 2
countHi("hi") → 1
"""

def countHi(s):
    if len(s) == 0:
        return 0

    if s[:2] == "hi":
        return 1 + countHi(s[1:])

    return countHi(s[1:])


print(countHi("asdf"))
print(countHi("hi"))
print(countHi("ahidf"))
print(countHi("asdfhi"))
print(countHi("hihiasdfhi"))
