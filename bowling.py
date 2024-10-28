from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self.frames = []
        self.bonus_throw = 0
    
    def add_frame(self, frame: Frame) -> None:

        if len(self.frames) >= 10:
            raise BowlingError("a game can have at most 10 frames")

        self.frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:

        if i < 0 or i >= len(self.frames):
            raise BowlingError("tried to access frame out of bounds")

        return self.frames[i]

    def calculate_score(self) -> int:

        score = 0

        for i, frame in enumerate(self.frames):

            if frame.is_spare():

                if i == len(self.frames) - 1:
                    frame.set_bonus(self.bonus_throw)
                else:
                    frame.set_bonus(self.frames[i + 1].get_first_throw())

            if frame.is_strike():
                next_frame = self.frames[i + 1]
                bonus = next_frame.get_first_throw() + next_frame.get_second_throw()

                if next_frame.is_strike():
                    next_frame = self.frames[i + 2]
                    frame.set_bonus(bonus + next_frame.get_first_throw())
                else:
                    frame.set_bonus(bonus)

            score += frame.score()

        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        self.bonus_throw = bonus_throw

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
