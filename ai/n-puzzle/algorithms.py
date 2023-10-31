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
    def __init__(self, heuristic: Heuristic):
        pass

    def exec(self, initial_state: State) -> None:
        pass


class AStar(Algorithm):
    def __init__(self, heuristic: Heuristic, status: bool = False):
        self.heuristic = heuristic
        self.status = status

    # https://www.geeksforgeeks.org/a-search-algorithm/
    def exec(self, initial_state: State) -> list | None:
        open_list = []
        closed_list = []

        initial_state.h = self.heuristic.H(initial_state)
        initial_state.g = 0
        initial_state.f = initial_state.g + initial_state.h

        open_list.append(initial_state)

        while len(open_list) != 0:
            open_list.sort(key=lambda elem: elem.f)
            q = open_list.pop(0)

            if self.status:
                print(
                    f"open list: {len(open_list)} - closed list: {len(closed_list)} - state.H: {q.h} - state.G: {q.g} - state.F: {q.f}",
                    end="\r",
                )

            if q.is_game_over():
                if self.status:
                    print("")
                return reconstruct_path(q)

            neighbors = q.neighbors()

            for state in neighbors:
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

        if self.status:
            print("")

        return None
