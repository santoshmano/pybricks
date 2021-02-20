def is_queen_safe(board, row, col):
    # check every row
    rowi = 0
    while rowi < len(board) and board[rowi] != None:
        if board[rowi] == col:
            return False
        rowi += 1

    # check every left and right diagonal
    lcol, rcol = 1, 1

    for i in range(row - 1, -1, -1):
        if (board[i] == col - lcol) or (board[i] == col + rcol):
            return False
        lcol += 1
        rcol += 1

    return True


def _find_all_arrangements(n, row, board, result):
    if row >= n:
        # completed all rows successfully
        result.append(list(board))
        return

    for col in range(n):
        if is_queen_safe(board, row, col):
            board[row] = col
            _find_all_arrangements(n, row + 1, board, result)
            board[row] = None


def find_all_arrangements(n):
    board = [None for _ in range(n)]
    result = []
    _find_all_arrangements(n, 0, board, result)
    return result


print(find_all_arrangements(4))