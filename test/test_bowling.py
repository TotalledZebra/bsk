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

    def test_calculate_score(self):

        game = BowlingGame()

        # The total score should be 20
        for i in range(10):
            game.add_frame(Frame(1, 1))

        self.assertEqual(20, game.calculate_score())

    def test_calculate_score_with_spare(self):

        game = BowlingGame()

        game.add_frame(Frame(1, 9))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))

        # As this game contains a spare, the score should be 88
        self.assertEqual(88, game.calculate_score())