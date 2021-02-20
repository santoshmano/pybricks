def print_board(board):
    print("N-queens Board")
    [print(_) for _ in board]

def create_board(size):
    return [[0 for _ in range(size)] for _ in range(size)]

def is_safe(board, row, col):
    for r in range(len(board)):
        if board[r][col] == 1:
            return False

    for c in range(len(board)):
        if board[row][c] == 1:
            return False

    r = row+1
    c = col+1
    while r < len(board) and c < len(board):
        if board[r][c] == 1:
            return False
        r += 1
        c += 1

    r = row-1
    c = col-1
    while r >=0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1

    r = row-1
    c = col+1
    while r >=0 and c < len(board):
        if board[r][c] == 1:
            return False
        r -= 1
        c += 1

    r = row+1
    c = col-1
    while c >=0 and r < len(board):
        if board[r][c] == 1:
            return False
        c -= 1
        r += 1

    return True

def nqueens(board, row, col, queens):
    if queens == 0:
        print_board(board)
        return

    if col == len(board):
        col = 0
        row += 1
    for i in range(row, len(board)):
        for j in range(col, len(board)):
            if is_safe(board, i, j):
                board[i][j] = 1
                nqueens(board, row, col+1, queens-1)
                board[i][j] = 0

    return

if __name__ == "__main__":

    size = 5
    board = create_board(size)
    print_board(board)

    nqueens(board, 0, 0, size)
