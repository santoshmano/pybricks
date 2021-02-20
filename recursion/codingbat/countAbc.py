
def countAbc(str):
    if len(str) == 0:
        return 0

    if str[:3] == 'abc':
        count = 1
    else:
        count = 0

    if str[:3] == 'aba':
        count += 1

    if str[:4] == 'abcd':
        count += 1

    return count + countAbc(str[1:])

print(countAbc("abcababcd"))