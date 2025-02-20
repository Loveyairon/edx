"""
Tic Tac Toe Player
"""

import copy
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
    count_x = 0
    count_o = 0
    if board == initial_state():
        return X
    for row in board:
        count_x += row.count(X)
        count_o += row.count(O)

    if count_o < count_x:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                action_tup = (i, j)
                action.add(action_tup)
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if new_board[action[0]][action[1]] != EMPTY:
        raise Exception("No More actions")
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for mark in [X, O]:

        # Check for 3 moves in a row horizontally
        for row in range(0, 3):
            if all(board[row][col] == mark for col in range(0, 3)):
                return mark

        # Check for 3 moves in a row vertically
        for col in range(0, 3):
            if all(board[row][col] == mark for row in range(0, 3)):
                return mark

        # Check for 3 moves in a row diagonally
        diagonals = [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
        for diagonal in diagonals:
            if all(board[row][col] == mark for (row, col) in diagonal):
                return mark

    # Game is a tie or still in progress
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or not actions(board):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == O:
        return -1
    elif winner(board) == X:
        return 1
    else:
        return 0


# noinspection PyUnreachableCode
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        best_v = -math.inf
        for move in actions(board):
            max_v = min_value(result(board, move))
            if max_v > best_v:
                best_v = max_v
                best_move = move

    elif player(board) == O:
        best_v = math.inf
        for move in actions(board):
            min_v = max_value(result(board, move))
            if min_v < best_v:
                best_v = min_v
                best_move = move
    return best_move


def min_value(board):
    """
    Returns the minimum utility of the current board.
    """

    if terminal(board):
        return utility(board)

    v = math.inf
    for move in actions(board):
        v = min(v, max_value(result(board, move)))
    return v


def max_value(board):
    """
    Returns the maximum utility of the current board.
    """

    if terminal(board):
        return utility(board)

    v = -math.inf
    for move in actions(board):
        v = max(v, min_value(result(board, move)))
    return v