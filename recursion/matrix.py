
def matrix_traversal(x, y, n, result):


    if (x < n):
        if (y < n):
            print("(", x, y, ")", end=' ')

            matrix_traversal(x, y+1, n, result)
        else:
            print("\n")
            matrix_traversal(x+1, 0, n, result)

matrix_traversal(0, 0, 3, [])
