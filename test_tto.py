import unittest
import random


class TickTackToeTestSuite(unittest.TestCase):


    def init_board(self):
        return [[' ', ' ', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', ' '],]

    def read_user_input(self, user_input):
        return map(int, user_input.split(","))

    def move(self, board, x, y, who):
        board[x][y] =  who

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
        x, y = self.read_user_input(user_input)
        self.move(board, x, y, 'x')
        counter = 0
        for row in board:
            for cell in row:
                if cell != ' ':
                    counter += 1
        self.assertEqual(counter, 1)

    def test_requested_cell_is_occupied(self):
        """ Testing a cell requested by user to move is already taken """
        board = self.init_board()
        user_input = '1,2'
        x, y = self.read_user_input(user_input)
        self.move(board, x, y, 'x')
        self.assertTrue(board[x][y] != ' ')

    def test_board_consistent_state(self):
        """ Tests board is in consistent state """
        board = self.init_board()

        self.move(board, 1, 2, 'x')
        self.move(board, 1, 0, 'x')
        self.move(board, 1, 1, 'x')
        self.move(board, 2, 2, '0')

        cnt_x = cnt_o = 0
        for row in board:
            for cell in row:
                if cell == 'x':
                    cnt_x += 1
                if cell == 'o':
                    cnt_o += 1

        self.assertTrue((cnt_x - cnt_o) in (0, 1))