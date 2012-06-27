import unittest
import random


class TickTackToeTestSuite(unittest.TestCase):


    def test_first_cell_empty(self):
        """ Test first cell is empty """
        board = [[' ']]
        self.assertEqual(board[0][0], ' ')

    def test_random_cell_is_empty(self):
        """ test random cell is empty """
        board = [[' ', ' ', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', ' '],]
        rand_row = random.randint(0, 2)
        rand_col = random.randint(0, 2)
        self.assertEqual(board[rand_row][rand_col], ' ')
