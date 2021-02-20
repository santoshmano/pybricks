"""
def find_next_wildcard(s, n):
    for i in range(n, len(s)):
        if s[i] == '?':
            index = i
            break
        else:
            index = i+1
    return index

def wildcard_main(s):
    #print(len(s), [n for n in range(3,2)])
    wildcard(s, find_next_wildcard(s, 0))

def wildcard(s, n):
    if n == len(s):
        print(s)
    elif n < len(s):
        for i in (0,1):
            s[n] = str(i)
            wildcard(s, find_next_wildcard(s,n))
        s[n] = '?'

wildcard_main(list("0?1?"))

"""
def _wildcard(str, i):
    if i == len(str):
        print("".join(str))
        return

    if str[i] == "?":
        str[i] = "0"
        _wildcard(str, i+1)
        str[i] = "1"
        _wildcard(str, i+1)
        str[i] = "?"
    else:
        _wildcard(str, i+1)


def wildcard(str):
    _wildcard(list(str), 0)

strings = ["i",
           "",
           "?",
           "??",
           "???",
           "0?",
           "?1",
           "1?0?"]
for str in strings:
    print("Wildcards of {}:".format(str))
    wildcard(str)
