def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    trio = []
    trio.append(getCols(board))
    trio.append(board)
    trio.append(getDiagonals(board))

    for arrays in trio:
        for row in arrays:

            if all(elem == "X" for elem in row):
                return "X"
            
            elif all(elem == "O" for elem in row):
                return "O"


    return None
    
def getCols(board):
    """
    Gets all cols in a board and returns them in a 2D array
    """
    columns = []
    for r in range(len(board)):
        column = []

        for c in range(len(board)):
            column.append(board[c][r])

        columns.append(column)

    return columns


def getDiagonals(board):
    """
    Gets all diagonals in a board and returns them in a 2D array
    """
    diagonals = [[],[]]
    for i in range(len(board)):
        diagonals[0].append(board[i][i])
        diagonals[1].append(board[i][len(board) - 1 - i])
    
    return diagonals

array = [[None,"O","O"],["X", "X", "X"] , [None, None, None]]
print(winner(array))