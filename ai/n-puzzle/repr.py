import numpy as np
import math


class Repr:
    def __init__(self, n_tiles: int):
        self.n_tiles = n_tiles
        self.__compute_shape()
        self.__generate_instance()

    def move_up(self) -> None:
        x, y = self.__get_x_pos()
        if x - 1 < 0:
            raise RuntimeError("move up not possible")
        tmp = self.grid[x - 1, y]
        self.grid[x - 1, y] = self.grid[x, y]
        self.grid[x, y] = tmp

    def move_down(self) -> None:
        x, y = self.__get_x_pos()
        if x + 1 >= self.n:
            raise RuntimeError("move down not possible")
        tmp = self.grid[x + 1, y]
        self.grid[x + 1, y] = self.grid[x, y]
        self.grid[x, y] = tmp

    def move_left(self) -> None:
        x, y = self.__get_x_pos()
        if y - 1 < 0:
            raise RuntimeError("move left not possible")
        tmp = self.grid[x, y - 1]
        self.grid[x, y - 1] = self.grid[x, y]
        self.grid[x, y] = tmp

    def move_right(self) -> None:
        x, y = self.__get_x_pos()
        if y + 1 >= self.n:
            raise RuntimeError("move right not possible")
        tmp = self.grid[x, y + 1]
        self.grid[x, y + 1] = self.grid[x, y]
        self.grid[x, y] = tmp

    def is_game_over(self) -> bool:
        line = self.__compute_line_grid(self.grid)
        expect = 1
        for i in range(0, self.n_tiles):
            if line[i] != expect:
                return False
            expect += 1
        return True

    def __compute_shape(self) -> None:
        shape = math.sqrt(self.n_tiles + 1)
        if not shape.is_integer():
            raise RuntimeError("Instance must be compatible with a grid (n x n)")
        self.n = int(shape)
        self.shape = (self.n, self.n)

    def __generate_instance(self) -> None:
        self.grid = np.arange(0, self.n_tiles + 1)
        while True:
            np.random.shuffle(self.grid)
            self.grid = self.grid.reshape(self.shape)
            if self.__validate(self.grid):
                break

    def __validate(self, grid: np.ndarray) -> bool:
        is_even_inversion_count = self.__compute_inversions(grid) % 2 == 0
        if not self.n % 2 == 0:
            # width is odd
            return is_even_inversion_count
        else:
            # width is even
            is_even_row_blank_count = self.__compute_blank_row_count(grid) % 2 == 0
            return (is_even_row_blank_count and not is_even_inversion_count) or (
                not is_even_row_blank_count and is_even_inversion_count
            )
        return False

    def __compute_inversions(self, grid: np.ndarray) -> int:
        line = self.__compute_line_grid(grid)
        total_inv = 0
        for i in range(0, self.n_tiles):
            inv = 0
            for j in range(i + 1, self.n_tiles):
                if line[i] > line[j]:
                    inv += 1
            total_inv += inv
        return total_inv

    def __compute_blank_row_count(self, grid: np.ndarray) -> int:
        return self.n - np.argwhere(grid == 0)[0][0]

    def __compute_line_grid(self, grid: np.ndarray) -> np.ndarray:
        line = np.reshape(grid, newshape=self.n_tiles + 1)
        return np.delete(line, line == 0)

    def __get_x_pos(self) -> tuple:
        return tuple(np.argwhere(self.grid == 0)[0])

    def __str__(self):
        out = ""
        for i in range(0, self.n):
            for j in range(0, self.n):
                tile = "X" if self.grid[i, j] == 0 else str(self.grid[i, j])
                if j == self.n - 1:
                    out += tile + "\n"
                else:
                    out += tile + " "
        return out
