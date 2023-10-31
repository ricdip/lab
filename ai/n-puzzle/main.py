from state import State
from heuristics import MisplacedTiles
from algorithms import AStar

s = State(8)
h = MisplacedTiles(template=s)
a = AStar(heuristic=h, status=True)

print(s.repr)

path = a.exec(s)

print("\nSolution:\n")

for state in path:
    print(state, end="\n\n")
