from state import State
from heuristics import MisplacedTiles
from algorithms import AStar

s = State(8)
h = MisplacedTiles(initial_state=s)
a = AStar(heuristic=h)

print(s)

print("-----------")

path = a.exec(s)

for state in path:
    print(state, end="\n\n")
