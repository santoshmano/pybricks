

def sort_chars(s):
    count = [0 for _ in range(0,256)]

    for c in s:
        count[int(ord(c))] += 1

    slist = []
    for i in range(0,256):
        while(count[i]):
            slist.append(chr(i))
            count[i] -= 1
    return "".join(slist)



print(sort_chars("bcdedfa"))
print(sort_chars("abd"))
print(sort_chars("dba"))
print(sort_chars("deadbeef"))
print(sort_chars("xx"))
