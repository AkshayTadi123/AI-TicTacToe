"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
#count = 0


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
    countX = 0
    countO = 0

    for i in board:
        for j in i:
            if j==X:
                countX+=1
            elif j==O:
                countO+=1
    
    if countX>countO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    reqSet = set()
    for i in range(3):
        for j in range(3):
            if (board[i][j] == EMPTY):
                reqSet.add((i,j))
    return reqSet


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("impossible action")
    
    newBoard = copy.deepcopy(board)
    (i,j) = action
    newBoard[i][j] = player(board)        
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] == X):
            return X
    for j in range(3):
        if (board[0][j] == board[1][j] == board[2][j] == X):
            return X
    if (board[0][0] == board[1][1] == board[2][2] == X):
        return X
    if (board[0][2] == board[1][1] == board[2][0] == X):
        return X
    
    
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] == O):
            return O
    for j in range(3):
        if (board[0][j] == board[1][j] == board[2][j] == O):
            return O
    if (board[0][0] == board[1][1] == board[2][2] == O):
        return O
    if (board[0][2] == board[1][1] == board[2][0] == O):
        return O  
  

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) == X):
         return True
    if (winner(board) == O):
         return True
    
    for i in range(3):
        for j in range(3):
            if (board[i][j] == EMPTY):
                return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    val = winner(board)
    if (val == X):
        return 1
    elif (val == O):
        return -1
    else:
        return 0

def minValue(board):
    if terminal(board):
        return utility(board)
    
    v = float('inf')
    for action in actions(board):
        v = min(v, maxValue(result(board,action)))

    return v


def maxValue (board):
    if terminal(board):
        return utility(board)
    
    v = float('-inf')
    for action in actions(board):
        v = max(v, minValue(result(board,action)))

    return v



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    optAction = None
    maxVal = float('-inf')
    minVal =  float('inf')

    if (terminal(board)==True):
        return optAction
    
    if player(board)==X:
        for action in actions(board):
            w = minValue(result(board,action))
            if (w>maxVal):
                maxVal = w
                optAction = action
    else:
        for action in actions(board):
            w = maxValue(result(board,action))
            if (w<minVal):
                minVal = w
                optAction = action
    return optAction

