import unittest
from main import chess
class TestChess(unittest.TestCase):
    def test_chess(self):
        self.assertEqual(chess(), "Chess")

if __name__ == '__main__':
    unittest.main()