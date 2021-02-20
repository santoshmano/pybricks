


def tables_iter(n):

    for i in range(1, 11, 1):
        print("{:2} X {:2} = {}".format(n, i, n*i))


def tables(n, i):
    if i == 11:
        return

    print("{:2} X {:2} = {}".format(n, i, n*i))
    tables(n, i+1)

tables_iter(9)
tables(9, 0)
