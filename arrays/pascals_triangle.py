

# n lines
def pascals_triangle(n):
    a = []
    for j in range(n):
        a.append([None for i in range(j+1)])

    for line in range(0, n):
        if line == 0:
            a[line][0] = 1
        elif line == 1:
            a[line][0] = 1
            a[line][1] = 1
        else:
            a[line][0] = 1
            a[line][line] = 1
            for i in range(1, line):
                a[line][i] = a[line-1][i-1] + a[line-1][i]

    #print the pascals triangle

    for i in range(n):
        for j in a[i]:
            print("{:4}".format(j), end=" ")

        print("")

pascals_triangle(10)