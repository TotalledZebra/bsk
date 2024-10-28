from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self.frames = []
    
    def add_frame(self, frame: Frame) -> None:
        self.frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:

        if i < 0 or i >= len(self.frames):
            raise BowlingError("tried to access frame out of bounds")

        return self.frames[i]

    def calculate_score(self) -> int:
        pass

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
