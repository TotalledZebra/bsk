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

    def test_game_with_10_frames(self):

        game = BowlingGame()

        # Add 9 frames
        for i in range(9):
            game.add_frame(Frame(i, i))

        # Add the 10th frame
        frame = Frame(10, 10)
        game.add_frame(frame)

        # Assert that the 10th frame is the same
        self.assertEqual(frame, game.get_frame_at(9))

    def test_raises_error_when_adding_more_than_10_frames(self):

        game = BowlingGame()

        # Add the maximum 10 frames
        for i in range(10):
            game.add_frame(Frame(1, 1))

        # Attempt to add an extra frame
        self.assertRaises(BowlingError, game.add_frame, Frame(1, 1))