from repr import Repr
from copy import deepcopy
from typing import Self


class State:
    def __init__(self, n_tiles: int):
        self.repr = Repr(n_tiles)
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0
        self.step = 0

    def is_game_over(self) -> bool:
        return self.repr.is_game_over()

    def neighbors(self) -> set:
        states = [self.move_up(), self.move_down(), self.move_left(), self.move_right()]
        states = set(filter(lambda item: item is not None, states))

        for s in states:
            s.parent = self

        return states

    def move_up(self) -> Self | None:
        state = deepcopy(self)
        try:
            state.repr.move_up()
        except:
            return None

        state.step = self.step + 1
        return state

    def move_down(self) -> Self | None:
        state = deepcopy(self)
        try:
            state.repr.move_down()
        except:
            return None

        state.step = self.step + 1
        return state

    def move_left(self) -> Self | None:
        state = deepcopy(self)
        try:
            state.repr.move_left()
        except:
            return None

        state.step = self.step + 1
        return state

    def move_right(self) -> Self | None:
        state = deepcopy(self)
        try:
            state.repr.move_right()
        except:
            return None

        state.step = self.step + 1
        return state

    def __str__(self):
        out = f"----- step {self.step}:\n"
        out += str(self.repr)
        out += "\n"
        out += f"g = {self.g}\n"
        out += f"h = {self.h}\n"
        out += f"f = {self.f}\n"
        out += "-----"

        return out

    def __eq__(self, o):
        if isinstance(o, State):
            return self.repr == o.repr
        else:
            return False

    def __ne__(self, o):
        return not self.__eq__(o)

    def __hash__(self):
        return hash(self.repr)
