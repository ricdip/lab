from heuristics import Heuristic
from state import State


def get_elem_from_list(l: list, state: State) -> State | None:
    for elem in l:
        if elem == state:
            return elem
    return None


def reconstruct_path(state: State) -> list:
    s = state
    path = []
    while s is not None:
        path.append(s)
        s = s.parent

    return list(reversed(path))


class Algorithm:
    def exec(self, initial_state: State) -> None:
        pass


class AStar(Algorithm):
    def __init__(self, heuristic: Heuristic):
        self.heuristic = heuristic

    # https://www.geeksforgeeks.org/a-search-algorithm/
    def exec(self, initial_state: State) -> list | None:
        open_list = []
        closed_list = []

        open_list.append(initial_state)

        while len(open_list) != 0:
            open_list.sort(key=lambda elem: elem.f)
            q = open_list.pop(0)

            neighbors = q.neighbors()

            for state in neighbors:
                if state.is_game_over():
                    return reconstruct_path(state)
                else:
                    state.g = q.g + 1
                    state.h = self.heuristic.H(state)
                    state.f = state.g + state.h

                if state in open_list:
                    node = get_elem_from_list(open_list, state)
                    if node.f < state.f:
                        continue

                if state in closed_list:
                    node = get_elem_from_list(closed_list, state)
                    if node.f < state.f:
                        continue

                open_list.append(state)

            closed_list.append(q)

        return None
