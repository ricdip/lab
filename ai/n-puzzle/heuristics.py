import numpy as np
from state import State


class Heuristic:
    def H(self, state: State) -> int:
        pass


class MisplacedTiles(Heuristic):
    def __init__(self, initial_state: State):
        self.n_tiles = initial_state.repr.n_tiles
        self.shape = initial_state.repr.shape
        self.n = initial_state.repr.n
        self.goal = np.arange(1, self.n_tiles + 1)
        self.goal = np.append(self.goal, 0)
        self.goal = np.reshape(self.goal, newshape=self.shape)

    def H(self, state: State) -> int:
        misplaced = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if state.repr.grid[i, j] != self.goal[i, j]:
                    misplaced += 1
        return misplaced
