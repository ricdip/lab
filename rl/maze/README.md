# Maze

A reinforcement learning maze implementation using Q-learning

## Description

The maze is composed by a grid filled with obstacles (red tiles). The Agent (blu tile) must reach the Exit (green tile).
The Agent can move up, down, left, right.

<kbd>
<img src="docs/maze.png" alt="maze" />
</kbd>

## Algorithm

The Q-learning algorithm allows the Agent to use the environment's rewards to learn the best action to take in a given state.
It uses a Q-table, it's cardinality is (state space, action space).

The values stored in it are the Q-values. The Q-table maps each pair (state, action) to a Q-value. The Q-value represents the quality of an action taken from a state, better Q-values mean better chances of greater rewards.

## Execution

```bash
user@host:~$ poetry shell
(rl-py3.11) user@host:~$ python main.py
```

## References

Some really helpful resources that I used:

- https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/
