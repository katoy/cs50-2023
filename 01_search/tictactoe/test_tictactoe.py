import unittest
from copy import deepcopy
import tictactoe as ttt

'''
$ python3 -m unittest test_tictactoe.py

to see coverage,

# rm .coverage
# coverage run test_tictactoe.py
# coverage html
# open htmlcov/index.html
'''


class Test(unittest.TestCase):
    # test
    def test_initial_state(self):
        actual_result = ttt.initial_state()
        expected = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.assertEqual(actual_result, expected)

    # test test_player
    def test_player(self):
        test_cases = [
            [ttt.initial_state(), "X"],
            [
                [
                    [None, None, None],
                    [None, None, None],
                    [None, None, None]
                ], "X"
            ],
            [
                [
                    [None, None, None],
                    [None, "X", None],
                    [None, None, None]
                ], "O"
            ],
            [
                [
                    ['O',  None, None],
                    [None, "X", None],
                    [None, None, None]
                ], "X"
            ],
            [
                [
                    ['O',  None, 'X'],
                    [None, "X", None],
                    [None, None, None]
                ], "O"
            ],
            [
                [
                    ['O', 'X', 'O'],
                    ['X', "O", 'X'],
                    ['X', 'O', None]
                ], 'X'
            ],
        ]

        for topic in test_cases:
            actual_result = ttt.player(topic[0])
            expected = topic[1]
            self.assertEqual(actual_result, expected, topic)

    # test test_actions
    def test_actions(self):
        test_cases = [
            [
                [
                    [None, None, None],
                    [None, None, None],
                    [None, None, None]
                ], set([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])
            ],
            [
                [
                    [None, None, None],
                    [None, "X", None],
                    [None, None, None]
                ], set([(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)])
            ],
            [
                [
                    ['O',  None, None],
                    [None, "X", None],
                    [None, None, None]
                ], set([(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)])
            ],
            [
                [
                    ['O',  None, 'X'],
                    [None, "X", None],
                    [None, None, None]
                ], set([(0, 1), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)])
            ],
            [
                [
                    ['O', 'X', 'O'],
                    ['X', "O", 'X'],
                    ['X', 'O', None]
                ], set([(2, 2)])
            ],
            [
                [
                    ['O', 'X', 'O'],
                    ['X', "O", 'X'],
                    ['X', 'O', 'X']
                ], set()
            ]
        ]

        for topic in test_cases:
            actual_result = ttt.actions(topic[0])
            expected = topic[1]
            self.assertEqual(actual_result, expected, topic)

    # test test_result_x
    def test_result_x(self):
        test_cases = [
            (0, 0), (0, 1), (0, 2),
            (1, 0), (1, 1), (1, 2),
            (2, 0), (2, 1), (2, 2)
        ]
        for topic in test_cases:
            actual_result = ttt.result(ttt.initial_state(), topic)
            expected = ttt.initial_state()
            i, j = topic
            expected[i][j] = 'X'
            self.assertEqual(actual_result, expected, topic)

    # test test_result_o
    def test_result_o(self):
        test_cases = [
            (0, 0), (0, 1), (0, 2),
            (1, 0), (1, 1), (1, 2),
            (2, 0), (2, 1)
        ]
        for topic in test_cases:
            board = ttt.initial_state()
            board[2][2] = 'X'

            actual_result = ttt.result(board, topic)
            expected = deepcopy(board)
            i, j = topic
            expected[i][j] = 'O'

            self.assertEqual(actual_result, expected, topic)

    # test test_result_invalid_move
    def test_result_invalid_move(self):
        test_cases = [
            [
                [
                    [None, None, None],
                    [None, 'X', None],
                    [None, None, None]
                ], (1, 3)
            ],
            [
                [
                    [None, None, None],
                    [None, 'X', None],
                    [None, None, None]
                ], (3, 1)
            ],
            [
                [
                    [None, None, None],
                    [None, 'X', None],
                    [None, None, None]
                ], (-1, 1)
            ],
            [
                [
                    [None, None, None],
                    [None, 'X', None],
                    [None, None, None]
                ], (1, -1)
            ],
            [
                [
                    [None, None, None],
                    [None, 'X', None],
                    [None, None, None]
                ], (1, 1)
            ],
            [
                [
                    ['O', None, None],
                    [None, 'X', None],
                    [None, None, None]
                ], (0, 0)
            ],
            [
                [
                    ['O', None, None],
                    [None, 'X', None],
                    [None, None, None]
                ], (1, 1)
            ]
        ]

        for topic in test_cases:
            actual_result = ttt.actions(topic[0])
            expected = topic[1]
            with self.assertRaises(ValueError):
                ttt.result(topic[0], topic[1])

    # test test_result_move_none
    def test_result_move_none(self):
        test_cases = [
            [
                [
                    [None, None, None],
                    [None, 'X', None],
                    [None, None, None]
                ], None
            ],
            [
                [
                    ['O', None, None],
                    [None, 'X', None],
                    [None, None, None]
                ], None
            ]
        ]

        for topic in test_cases:
            actual_result = ttt.result(topic[0], topic[1])
            expected = topic[0]
            self.assertEqual(actual_result, expected, topic)

    # test test_winner
    def test_winner(self):
        test_cases = [
            [
                [
                    [None, None, None],
                    [None, None, None],
                    [None, None, None]
                ], None
            ],
            [
                [
                    ['X', 'X', 'X'],
                    [None, None, None],
                    [None, None, None]
                ], 'X'
            ],
            [
                [
                    [None, None, None],
                    ['X', 'X', 'X'],
                    [None, None, None]
                ], 'X'
            ],
            [
                [
                    [None, None, None],
                    [None, None, None],
                    ['X', 'X', 'X']
                ], 'X'
            ],
            [
                [
                    ['X', None, None],
                    ['X', None, None],
                    ['X', None, None]
                ], 'X'
            ],
            [
                [
                    [None, 'X', None],
                    [None, 'X', None],
                    [None, 'X', None]
                ], 'X'
            ],
            [
                [
                    [None, None, 'X'],
                    [None, None, 'X'],
                    [None, None, 'X']
                ], 'X'
            ],
            [
                [
                    [None, None, 'X'],
                    [None, 'X', None],
                    ['X', None, None]
                ], 'X'
            ],
            [
                [
                    ['X', None, None],
                    [None, 'X', None],
                    [None, None, 'X']
                ], 'X'
            ],
            [
                [
                    ['X', 'X', 'O'],
                    ['X', 'X', None],
                    ['O', None, 'O']
                ], None
            ],
        ]

        for topic in test_cases:
            actual_result = ttt.winner(topic[0])
            expected = topic[1]
            self.assertEqual(actual_result, expected, topic)

    # test test_terminal
    def test_terminal(self):
        test_cases = [
            [
                [
                    [None, None, None],
                    [None, None, None],
                    [None, None, None]
                ], False
            ],
            [
                [
                    ['X', 'X', 'O'],
                    ['O', 'X', 'X'],
                    ['X', 'O', 'O']
                ], True
            ],
            [
                [
                    ['X', 'X', 'X'],
                    ['O', None, None],
                    ['O', None, None]
                ], True
            ],
            [
                [
                    [None, 'O', None],
                    ['X', 'X', 'X'],
                    [None, 'O', None]
                ], True
            ],
            [
                [
                    [None, None, 'O'],
                    [None, None, 'O'],
                    ['X', 'X', 'X']
                ], True
            ],
            [
                [
                    ['X', 'O', 'O'],
                    ['X', None, None],
                    ['X', None, None]
                ], True
            ],
            [
                [
                    [None, 'X', None],
                    ['O', 'X', 'O'],
                    [None, 'X', None]
                ], True
            ],
            [
                [
                    ['O', None, 'X'],
                    [None, 'O', 'X'],
                    [None, None, 'X']
                ], True
            ],
            [
                [
                    ['O', None, 'X'],
                    [None, 'X', None],
                    ['X', None, 'O']
                ], True
            ],
            [
                [
                    ['X', None, 'O'],
                    [None, 'X', None],
                    ['O', None, 'X']
                ], True
            ]
        ]

        for topic in test_cases:
            actual_result = ttt.terminal(topic[0])
            expected = topic[1]
            self.assertEqual(actual_result, expected, topic)

    # test test_utility
    def test_utility(self):
        test_cases = [
            [
                [
                    [None, None, None],
                    [None, None, None],
                    [None, None, None]
                ], 0
            ],
            [
                [
                    ['X', 'X', 'X'],
                    [None, None, None],
                    [None, None, None]
                ], 1
            ],
            [
                [
                    ['O', 'O', 'O'],
                    [None, None, None],
                    [None, None, None]
                ], -1
            ],
        ]
        for topic in test_cases:
            actual_result = ttt.utility(topic[0])
            expected = topic[1]
            self.assertEqual(actual_result, expected, topic)


    # test test_minimax
    def test_minimax(self):
        test_cases = [
            # win
            [
                [
                    [None, "X", "O"],
                    ["O", "X", None],
                    ["X", None, "O"]
                ], (2, 1)
            ],
            [
                [
                    [None, None, "X"],
                    ["O", "O", "X"],
                    ["X", None, "O"]
                ], (0, 0)
            ],
            [
                [
                    [None, "X", "O"],
                    [None, None, "X"],
                    ["O", "O", "X"]
                ], (1, 1)
            ],
            [
                [
                    [None, "O", None],
                    ["O", None, "X"],
                    [None, "X", None]
                ], (2, 2)
            ],
            # not lose
            [
                [
                    ["O", "X", "O"],
                    ["X", None, None],
                    [None, None, None]
                ], (1, 1)
            ],
            [
                [
                    [None, "X", None],
                    ["X", "O", None],
                    [None, "O", None]
                ], (0, 0)
            ]
        ]

        for topic in test_cases:
            actual_result = ttt.minimax(topic[0])
            expected = topic[1]
            self.assertEqual(actual_result, expected, topic)


if __name__ == "__main__":
    unittest.main()
