def solve(n):
    #prepare a board
    board = [[0 for x in range(n)] for x in range(n)]
    #set initial positions
    place_queen(board, 0, 0)

def place_queen(board, row, column):
    """place a queen that satisfies all the conditions"""
    #base case
    if row > len(board)-1:
        print(board)
    #check every column of the current row if its safe to place a queen
    while column < len(board):
        if is_safe(board, row, column):
            #place a queen
            board[row][column] = 1
            #place the next queen with an updated board
            return place_queen(board, row+1, 0)
        else:
            column += 1
    #there is no column that satisfies the conditions. Backtrack
    for c in range(len(board)):
        if board[row-1][c] == 1:
            #remove this queen
            board[row-1][c] = 0
            #go back to the previous row and start from the last unchecked column
            return place_queen(board, row-1, c+1)

def is_safe(board, row, column):
    """ if no other queens threaten a queen at (row, queen) return True """
    queens = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 1:
                queen = (r,c)
                queens.append(queen)
    for queen in queens:
        qr, qc = queen
        #check if the pos is in the same column or row
        if row == qr or column == qc:
            return False
        #check diagonals
        if (row + column) == (qr+qc) or (column-row) == (qc-qr):
            return False
    return True

solve(3)