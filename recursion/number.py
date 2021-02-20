

def count(c):
    if c == 5:
        return

    print("before call to count", c)
    count(c+1)
    print("after call to count", c)


count(0)