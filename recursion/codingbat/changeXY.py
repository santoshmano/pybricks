"""
Given a string, compute recursively (no loops) a new string where all the lowercase 'x' chars have been changed to 'y' chars.

changeXY("codex") → "codey"
changeXY("xxhixx") → "yyhiyy"
changeXY("xhixhix") → "yhiyhiy"
"""

def changeXY(s):
    if len(s) == 0:
        return

    if s[0] == 'x':
        s[0] = 'y'
        print(s)

    changeXY(s[1:])

s = list("codex")
changeXY(s)
print(s)
