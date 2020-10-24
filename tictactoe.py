"""
Tic Tac Toe Player
"""
import copy
import random
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

    


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    Xs = 0
    Os = 0

    for row in board:
        for col in row:
            if col == "X":
                Xs+=1
            elif col == "O":
                Os += 1

    if (Xs == Os):
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions = set()

    for i in range (len(board)):
        for j in range (len(board[i])):
            
            if board[i][j] == None:
                actions.add((i,j))

    
    return actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    symbol = player(board)

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = symbol

    return new_board



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




def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) == None and NoneExists(board):
        return False

    return True 

def NoneExists(board):

    for row in board:
        for item in row:
            if item == None:
                return True

    return False
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1

    elif winner(board) == "O":
        return -1

    return 0
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):
        return None

    turn = player(board)

    if turn == "X":
        bestscore = -math.inf
        bestmove = None
        for action in actions(board):
            print(f"{getValue(result(board,action))} {action}")
            if getValue(result(board,action)) > bestscore:
                bestmove = action
                bestscore = getValue(result(board,action))

        
        return bestmove

    else:
        bestscore = math.inf
        bestmove = None
        for action in actions(board):
            print(f"{getValue(result(board,action))} {action}")
            if getValue(result(board, action)) < bestscore:
                bestmove = action
                bestscore = getValue(result(board,action))
        print(bestscore)
        return bestmove

def getValue(board):
    if winner(board) == "X":
        return 1

    if utility(board) == "O":
        return -1

    if NoneExists(board):
        return 0

    turn = player(board)

    if turn == X:
        bestvalue = -math.inf
        for action in actions(board):
            if getValue(result(board,action)) > bestvalue:
                bestvalue = getValue(result(board,action))

        
        return bestvalue

    else:
        bestvalue = math.inf
        for action in actions(board):
            if getValue(result(board,action)) < bestvalue:
                bestvalue = getValue(result(board,action))

        
        return bestvalue

    
