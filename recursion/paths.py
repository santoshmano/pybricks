#!/usr/bin/env python3

# Problem: Count all paths from top left to bottom right,
# given that you can only go right or down.

# Every move there are two choices, move right or left
#   - recursively take choice 1/2 till you reach dest(rows, cols)
#
# Recurrence relation
# T(m,n) = T(m-1, n) + T(m, n-1)
# T(0,1) = 1
# T(1,0) = 1
#
# Time O(m,n) = 2**(m+n)
# Space O(n) = n+m

def paths_count(matrix, rows, cols):
    if rows == len(matrix)-1 and cols == len(matrix[0])-1:
        return 1
    if rows == len(matrix) or cols == len(matrix[0]):
        return 0

    r = paths_count(matrix, rows+1, cols)
    d = paths_count(matrix, rows, cols+1)

    return r+d

def paths_count2(grid, row, col):
    if row == len(grid)-1 or col == len(grid[0])-1:
        return 1

    return paths_count2(grid, row+1, col) + paths_count2(grid, row, col+1)


def paths_print(matrix, rows, cols, path, k):
    if rows == len(matrix)-1 and cols == len(matrix[0])-1:
        path[k] = matrix[rows][cols]
        print(path)
        return
    if rows == len(matrix) or cols == len(matrix[0]):
       return

    path[k] = matrix[rows][cols]
    paths_print(matrix, rows+1, cols, path, k+1)
    paths_print(matrix, rows, cols+1, path, k+1)


def paths_print_steps(matrix, rows, cols, path, k, steps):
    if rows == len(matrix)-1 and cols == len(matrix[0])-1:
        path[k] = matrix[rows][cols]
        print(path, steps)
        return
    if rows == len(matrix) or cols == len(matrix[0]):
        return

    path[k] = matrix[rows][cols]
    steps.append("right")
    paths_print_steps(matrix, rows+1, cols, path, k+1, steps)
    steps.pop()

    steps.append("down")
    paths_print_steps(matrix, rows, cols+1, path, k+1, steps)
    steps.pop()

# 2D matrix of characters. Some cells are marked *, meaning you
# can’t go there. Now, count all paths. No closed form solution
# to this one
def paths_count_mines(matrix, rows, cols):

    if rows == len(matrix)-1 and cols == len(matrix[0])-1:
        return 1
    if rows == len(matrix) or cols == len(matrix[0]):
        return 0
    if matrix[rows][cols] == "*":
        return 0

    r = paths_count_mines(matrix, rows+1, cols)
    d = paths_count_mines(matrix, rows, cols+1)

    return r+d

# Problem - Count(Print) Paths with only even numbers

def paths_count_print_even(matrix, rows, cols, path, k):
    if rows == len(matrix)-1 and cols == len(matrix[0])-1:
        if matrix[rows][cols] %2 != 0:
            return 0
        path[k] = matrix[rows][cols]
        print(path)
        return 1
    if rows == len(matrix) or cols == len(matrix[0]):
        return 0

    if matrix[rows][cols] %2 != 0:
        return 0

    path[k] = matrix[rows][cols]
    l = paths_count_print_even(matrix, rows+1, cols, path, k+1)
    r = paths_count_print_even(matrix, rows, cols+1, path, k+1)

    return l+r

def matrix_print(matrix, format="d"):
    """
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print("{:3d}".format(matrix[row][col]), end="")
        print()
    print()
    """
    # another way of printing a matrix
    for row in matrix:
        for val in row:

            if format == "d":
                print("{:3d}".format(val), end='')
            if format == "s":
                print("{:3s}".format(val), end="")

        print()

    """
    # another way of printing in programs

    row = len(matrix)
    col = len(matrix[0])

    for i in range(row):
        for j in range(col):

        print()
    """

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    print("orig matrix")
    matrix_print(matrix)
    print("Num paths:", paths_count(matrix, 0, 0), paths_count2(matrix, 0, 0))

    paths_print(matrix, 0, 0, [None for x in range(3+2)], 0)
    paths_print_steps(matrix, 0, 0, [None for x in range(3+2)], 0, [])


'''
    mines = [["0", "0", "0"],
             ["*", "0", "0"],
             ["0", "*", "0"]]
    print("orig matrix")
    matrix_print(mines, "s")
    print("Num valid paths:", paths_count_mines(mines, 0, 0))


    matrix = [[0, 0, 0],
              [0, 0, 1],
              [1, 0, 0]]
    print("orig matrix")
    matrix_print(matrix, "d")
    print("num of valid paths:", paths_count_print_even(matrix, 0, 0, [None for x in range(3+2)], 0))
'''