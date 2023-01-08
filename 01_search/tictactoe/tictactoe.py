"""
Tic Tac Toe Player
"""

import math
import random
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

# patterns for win (position in [0.,,8] for vec of board
PATTERNS_3 = [
    # row
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    # col
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    # diag
    [0, 4, 8],
    [2, 4, 6]
]

# patterns for win (position in [0.,,15] for vec of board
PATTERNS_4 = [
    # row
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15],
    # col
    [0, 4, 8, 12],
    [1, 5, 9, 13],
    [2, 6, 10, 14],
    [3, 7, 11, 15],
    # diag
    [0, 5, 10, 15],
    [3, 6, 9, 12]
]

# size of board
DIM = 3
PATTERNS = PATTERNS_3
DEPTH_LIMIT = 10  # 4 # 10


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY for i in range(DIM)] for j in range(DIM)]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    vec = [x for row in board for x in row]
    if vec.count(X) == vec.count(O):
        return X

    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    vec = [x for row in board for x in row]
    moves = [(p // DIM, p % DIM) for p in range(len(vec)) if vec[p] == EMPTY]
    return set(moves)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action is None:
        return deepcopy(board)

    i, j = action
    if board[i][j] != EMPTY:
        raise ValueError("Box is already filled!")

    new_board = deepcopy(board)
    new_board[i][j] = player(new_board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    vec = [x for row in board for x in row]
    for pat in PATTERNS:
        marks = set([vec[p] for p in pat])
        if marks == {X}:
            return X
        if marks == {O}:
            return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    vec = [x for row in board for x in row]
    count_empty = vec.count(EMPTY)
    return count_empty == 0


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_to_val = {X: 1, O: -1, None: 0}
    return winner_to_val[winner(board)]


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    ret = None
    if player(board) == O:
        ret = min_player(board)
    else:
        ret = max_player(board)

    print("v:{:>2}, try_count:{:-7}".format(ret['val'], ret['count']))
    return ret["move"]


def max_player(board, depth=0, alpha=-math.inf, beta=math.inf, count=0):
    """
    Returns best_move for max_player.
    {"move": best_move, "val": vql, "count" try_count}
    """
    if DEPTH_LIMIT < depth or terminal(board):
        return {"move": None, "val": utility(board), "count": count + 1}

    val = -math.inf
    best_move = None
    # shuffle actions
    action_list = list(actions(board))
    random.shuffle(action_list)

    for action in action_list:
        ret = min_player(result(board, action), depth + 1, alpha, beta, count)
        ret_val = ret["val"]
        count = ret["count"]
        if val < ret_val:
            val = ret_val
            best_move = action
            alpha = max(alpha, val)

        # A-B Pruning skips calls to min_player if lower result already found:
        if alpha > beta:
            break

    return {"move": best_move, "val": val, "count": count}


def min_player(board, depth=0, alpha=-math.inf, beta=math.inf, count=0):
    """
    Returns best_move for min_player.
    {"move": bes5_move, "val": vql, "count" try_count}
    """
    if DEPTH_LIMIT < depth or terminal(board):
        return {"move": None, "val": utility(board), "count": count + 1}

    val = math.inf
    best_move = None
    # shuffle actions
    action_list = list(actions(board))
    random.shuffle(action_list)

    for action in action_list:
        ret = max_player(result(board, action), depth + 1, alpha, beta, count)
        ret_val = ret["val"]
        count = ret["count"]
        if ret_val < val:
            val = ret_val
            best_move = action
            beta = min(val, beta)

        # A-B Pruning skips calls to max_player if higher result already found:
        if alpha > beta:
            break

    return {"move": best_move, "val": val, "count": count}
