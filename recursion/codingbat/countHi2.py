"""
Given a string, compute recursively the number of times lowercase "hi"
appears in the string, however do not count "hi" that have an 'x'
immedately before them.

countHi2("ahixhi") → 1
countHi2("ahibhi") → 2
countHi2("xhixhi") → 0
"""

def countHi2(s):

    if len(s) == 0:
        return 0

    if s[0] == 'x':
        if s[1:3] == 'hi':
            return countHi2(s[3:])

    if s[:2] == 'hi':
        return 1 + countHi2(s[2:])

    return countHi2[1:]

s = "abd"

print(s[1:)

s = ['a', 'b', 'c']
print(s[1:])