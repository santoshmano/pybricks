
def _perm(s, start, result):
    if start == len(s):
        result.append(list(s))
        return
    else:
        for i in range(start, len(s)):
            s[start], s[i] = s[i], s[start]
            _perm(s, start+1, result)
            s[start], s[i] = s[i], s[start]


def _perm_nodup(s, start, result):
    if start == len(s):
        result.append(list(s))
        return

    items = set()
    for i in range(start, len(s)):
        if int(s[i]) not in items:
            print(items, s[i])
            items.add(int(s[i]))
            s[start], s[i] = s[i], s[start]
            _perm_nodup(s, start+1, result)
            s[start], s[i] = s[i], s[start]
        print("in else", items, s[i])
        _perm_nodup(s, start+1, result)

def perm(nums):
    result = []
    _perm_nodup(nums, 0, result)
    print(result)


perm([1, 1])