"""

Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.

countX("xxhixx") → 4
countX("xhixhix") → 3
countX("hi") → 0

"""

def countX_for(s):
    if len(s):
        for i in range (0, len(s)):
            if s[i] == 'x':
                return 1 + countX(s[i + 1:])
        return 0
    else:
        return 0


def countX(s):
    if len(s) == 0:
        return 0
    else:
        if s[0] == 'x':
            return 1 + countX(s[1:])
        else:
            return 0 + countX(s[1:])

print(countX("xxx"), countX("xxhixx"), countX("xhixhix"), countX("hi"))