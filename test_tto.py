import unittest
import random


class TickTackToeTestSuite(unittest.TestCase):


    def init_board(self):
        return [[' ', ' ', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', ' '],]

    def test_first_cell_empty(self):
        """ Test first cell is empty """
        board = self.init_board()
        self.assertEqual(board[0][0], ' ')

    def test_random_cell_is_empty(self):
        """ test random cell is empty """
        board = self.init_board()
        rand_row = random.randint(0, 2)
        rand_col = random.randint(0, 2)
        self.assertEqual(board[rand_row][rand_col], ' ')

    def test_one_cell_occupied(self):
        """ Test that after first read, one cell is filled """
        board = self.init_board()
        user_input = '0,1'
        x, y = map(int, user_input.split(","))
        board[x][y] = 'x'
        counter = 0
        for row in board:
            for cell in row:
                if cell != ' ':
                    counter += 1
        self.assertEqual(counter, 1)

    def test_requested_cell_is_occupied(self):
        """ Testing a cell requested by user to move is already taken """
        board = self.init_board()
        board[1][2] = 'x'
        user_input = '1,2'
        x, y = map(int, user_input.split(","))
        self.assertTrue(board[x][y] != ' ')
