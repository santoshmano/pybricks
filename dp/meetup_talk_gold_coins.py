# n * n grid, start at upper left corner and have to end at bottom right.
# each cell has some gold coins

# if you layout all the cells in linear every option is either a -> or bottom arrow (
# number of paths ((n-1) + (m-1))! / (n-1)! * (m-1)!

# let F(x, y)  be the optimal solution.
# overall solution to the problem is f(0,0)

# F(x, y) = max (F(x+1, y) , F(x, y+1))

# After recurrence relations how do you know if you have to solve the problem using DP
# Draw the Tree to see if there are overlapping base cases

def _gold_coins(grid, x, y):

    if x == len(grid) and y == len(grid):
        return grid[x][y]

    if x == len(grid) or y == len(grid):
        return 0

    coins = grid[x][y]
    coins += max(_gold_coins(grid, x+1, y), _gold_coins(grid, x, y+1))

    return coins


# if x can go from 0->M and y can go from 0-N
# Number of states = M * N  all the valid cells in the 2d array

# so O(N) = O(M * N)

def _gold_coins_memo(grid, cache, x, y):

    if x == len(grid) and y == len(grid):
        return grid[x][y]

    if x == len(grid) or y == len(grid):
        return 0

    if cache[x][y] == -1:
        coins = grid[x][y]
        coins += max(_gold_coins(grid, x+1, y), _gold_coins(grid, x, y+1))

        cache[x][y] = coins

    return cache[x][y]


# Time complextit

# TODO finish this solution

# F[x][y] = grid

# for y = maxY-1 to 0
#   for x = maxX-1 to 0
        cache += x,y + max( otehrs)

# TODO draw the cache from backwards and

def _gold_coins_dp(grid, cache, x, y):

    if x == len(grid) and y == len(grid):
        return 0

    if x == len(grid) or y == len(grid):
        return 0

    # here we have to set grid of x+1 and y+1 elements to infinity
    for i in range(len(grid)-1, x-1, -1):
        for j in range(len(grid)-1, y-1, -1):
            # the below will step out of the grid, when you do i+1 TODO
            cache[i][j] = grid[i][j] + max(grid[i+1][j], grid[i][j+1])

    return cache[0][0]

def gold_coins():

    grid = [[3, 4, 3, 5],
            [3, 2, 2, 1],
            [2, 5, 7, 9],
            [1, 5, 3, 8]]

    cache = [[-1 for _ in range(len(grid)) for _ in range(len(grid))]]

    print("\nMax gold coins {}, memo:{}, ".format(
            _gold_coins(grid, 0, 0),
            _gold_coins_memo(grid, cache, 0, 0)))

if __name__ == "__main__":
    gold_coins()


