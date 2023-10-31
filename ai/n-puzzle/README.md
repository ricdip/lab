# n-puzzle

An implementation of n-puzzle solved by AI search algorithms

## Implemented algorithms

- **A\***: informed search algorithm that uses an heuristic to traverse the state space graph. It aims to find a path to the goal state that has the smallest cost. It selects the path that minimizes `f(n) = g(n) + h(n)`, where `n` is the current node, `g(n)` is the cost of the path from the start node to `n`, and `h(n)` is the estimate of the cost of the cheapest path from `n` to the goal state (`h` is the heuristic function).

## Implemented heuristics

- **Misplaced tiles**: heuristic that returns the number of tiles that are different (misplaced) compared to the goal state

## Execution

```bash
# activate Python env
user@host:~$ poetry shell

# show help message
(ai-py3.11) user@host:~$ python main.py --help

# call with default args
(ai-py3.11) user@host:~$ python main.py

# call with custom number of tiles
(ai-py3.11) user@host:~$ python main.py --n-tiles 8
```
