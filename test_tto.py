import unittest



class TickTackToeTestSuite(unittest.TestCase):


    def test_get_cell(self):
        """ Test first cell is empty """
        board = [[' ']]
        self.assertEqual(board[0][0], ' ')
