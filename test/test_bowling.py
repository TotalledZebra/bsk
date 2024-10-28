import unittest

from bowling import BowlingGame
from bowling_error import BowlingError
from frame import Frame


class TestBowlingGame(unittest.TestCase):

    def test_create_game(self):

        frame = Frame(1, 5)

        game = BowlingGame()

        game.add_frame(frame)

        self.assertEqual(frame, game.get_frame_at(0))

    def test_raises_error_when_accessing_out_of_bounds(self):

        game = BowlingGame()

        self.assertRaises(BowlingError, game.get_frame_at, 0)