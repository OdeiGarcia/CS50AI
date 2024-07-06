"""
Tic Tac Toe Player
"""

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
    
    count_X = sum(row.count('X') for row in board)
    count_O = sum(row.count('O') for row in board)
    
    # El jugador 'X' siempre comienza, así que si hay igual cantidad de 'X' y 'O', le toca a 'X'
    return 'O' if count_X > count_O else 'X'

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    act = set()
    for i, x in enumerate(board):
        for j, y in enumerate(x):
            if y == None:
                act.add((i,j))

    return act
    raise NotImplementedError


def result(board, action):


    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    fil, col = action
    if 0 <= fil <= 2 and 0 <= col <= 2 and board[fil][col] is None:
        board2 = [row[:] for row in board]  # Hacer una copia superficial del tablero
        board2[fil][col] = player(board)    # Colocar el movimiento del jugador en el tablero copiado
        return board2
    else:
        raise Exception("Movimiento inválido: posición ocupada o fuera de los límites del tablero")

    
    

    raise NotImplementedError


def winner(board):

    """
    Returns the winner of the game, if there is one.
    """
    size = len(board)
    for fila in board:
        if fila[0] != None and all(cell == fila[0] for cell in fila):
            return fila[0]
    for col in range(size):
        if board[0][col] != None and all(board[fila][col] == board[0][col] for fila in range(size)):
            return board[0][col]
        
    if board[0][0] != None and all(board[i][i] == board[0][0] for i in range(size)):
        return board[0][0]
    if board[0][2] != None and all(board[i][2-i] == board[0][2] for i in range(size)):
        return board[0][2]
    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) != None):
        return True
    else:
        for r in board:
            for j in r:
                if (j == None):
                    return False
        return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (terminal(board) == True):
        if (winner(board) == X):
            return 1
        elif (winner(board) == O):
            return -1
        else:
            return 0
    raise NotImplementedError

def min_value(board):
    if terminal(board):
        return None, utility(board)
    v = 99999
    move = None
    for action in actions(board):
        act, aux = max_value(result(board,action))
        if aux < v:
            move = action
            v = aux
            if v == -1:
                return move,v
    return move,v

def max_value(board):
    if terminal(board):
        return None,utility(board)
    v = -99999
    move = None
    for action in actions(board):
        act, aux = min_value(result(board,action))
        if aux > v:
            move = action
            v = aux
            if v == 1:
                return move,v

        

    return move,v

def minimax(board):
    if (player(board) == X):
        move, val =  max_value(board)
        return move
    if (player(board) == O):
        move, val = min_value(board)
        return move
        

    raise NotImplementedError
