import unittest
import random


class TicTacToeTestSuite(unittest.TestCase):


    def init_board(self):
        return [[' ', ' ', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', ' '],]

    def read_user_input(self, user_input):
        return map(int, user_input.split(","))

    def move(self, board, cell, who):
        x, y = cell
        if board[x][y] == ' ':
            board[x][y] =  who
            return True
        return False

    def count_cells_for_player(self, board, who):
        counter = 0
        for row in board:
            for cell in row:
                if cell == who:
                    counter += 1
        return counter

    def count_cells(self, board):
        cnt_x = self.count_cells_for_player(board, 'x')
        cnt_o = self.count_cells_for_player(board, 'o')
        return (cnt_x, cnt_o)

    def next_to_move(self, board):
        cnt_x, cnt_o = self.count_cells(board)
        if cnt_x == cnt_o:
            next_to_move = 'x'
        elif cnt_x - cnt_o == 1:
            next_to_move = 'o'
        return next_to_move

    def get_value_in_cell(self, board, cell):
        x, y = cell
        return board[x][y]

    #def check_board_is_in_consistent_state(self, board):
    #    cnt_x = self.count_cells(board, 'x')
    #    cnt_o = self.count_cells(board, 'o')
    #    return (cnt_x - cnt_o) in (0, 1)

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
        cell = self.read_user_input(user_input)
        self.move(board, cell, 'x')
        (cnt_x, cnt_o) = self.count_cells(board)
        counter = cnt_x + cnt_o
        self.assertEqual(counter, 1)

    def test_requested_cell_is_occupied(self):
        """ Testing a cell requested by user to move is already taken """
        board = self.init_board()
        user_input = '1,2'
        cell = self.read_user_input(user_input)
        self.move(board, cell, 'x')
        self.assertTrue(self.get_value_in_cell(board, cell) != ' ')

    def test_counter_for_moves(self):
        """ test  """
        board = self.init_board()
        cell = (1, 2)
        self.move(board, cell, 'x')
        cell = (1, 0)
        self.move(board, cell, 'x')

        counter = self.count_cells_for_player(board, 'x')
        self.assertEqual(counter, 2)

    def test_x_is_first_player(self):
        board = self.init_board()
        next_to_move = self.next_to_move(board)
        self.assertEqual(next_to_move, 'x')

    def test_o_is_entitled_to_move_after_x(self):
        """ Test O person is entitled by program to move after X """
        board = self.init_board()

        cell = (1, 2)
        self.move(board, cell, 'x')
        self.assertEqual(self.next_to_move(board), 'o')

    def test_x_is_entitled_to_move_after_o(self):
        """ Test X person is entitled by program to move after O """
        board = self.init_board()
        cell = (1, 2)
        self.move(board, cell, 'x')
        cell = (1, 2)
        self.move(board, cell, 'o')
        self.assertEqual(self.next_to_move(board), 'x')
