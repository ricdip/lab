from moves import Move
from copy import deepcopy
from colorama import Back, Style
import random


class Environment:
    """
    Environment implementation of an arena that contains an Agent and an Exit and is filled with obstacles. The objective of the Agent is to reach the Exit
    """

    def __init__(self):
        """
        Environment constructor. Loads default arena

        Attributes:
            arena (Environment): the environment that the Agent will explore
            agent_pos (tuple): the (x, y) position of the Agent in the arena
            exit_pos (tuple): the (x, y) position of the Exit in the arena
            step (int): the total steps of the Agent in the arena
            collision (bool): set to True if a collision occurred
            done (bool): set to True if Agent reaches the exit
            last_action (Move): set to the last action performed by the Agent
            actions (list): all possible actions
            state_space (int): number of all possible states
            action_space (int): number of all possible actions
        """
        self.load_default()

    def __init(self) -> None:
        """
        Init function that initialized the environment
        """
        # the possible states are all possible agent positions in the arena grid
        self.arena = self.__generated_arena
        # agent starting position is always the same
        self.agent_pos = (9, 0)
        # exit position is always the same
        self.exit_pos = (0, 9)
        # total steps of the agent
        self.step = 0
        # set to True if a collision occurred: there is a collision if the agent choose to move to a tile where there is an obstacle or if the agent choose to move out of the arena bounds
        self.collision = False
        # set to True if the agent reaches the exit
        self.done = False
        # set to the last action performed by the agent
        self.last_action = None

        # all possible actions
        self.actions = [Move.UP, Move.DOWN, Move.LEFT, Move.RIGHT]

        # RL variables
        # state space = all possible states = row x col
        self.state_space = 10 * 10
        # action space = all possible actions = up, down, left, right = 4
        self.action_space = 4

    def generate_arena(self, obstacle_prob=0.2) -> None:
        """
        Function that generates a random arena. The Agent and the Exit are always at the same position but the obstacles are generated randomly

        Args:
            obstacle_prob (float): the probability [0, 1] of the generation of an obstacle
        """
        self.__generated_arena = [
            [
                random.choices([0, 3], [1 - obstacle_prob, obstacle_prob])[0]
                for i in range(0, 9)
            ]
            + [2],
            [
                random.choices([0, 3], [1 - obstacle_prob, obstacle_prob])[0]
                for i in range(0, 10)
            ],
            [
                random.choices([0, 3], [1 - obstacle_prob, obstacle_prob])[0]
                for i in range(0, 10)
            ],
            [
                random.choices([0, 3], [1 - obstacle_prob, obstacle_prob])[0]
                for i in range(0, 10)
            ],
            [
                random.choices([0, 3], [1 - obstacle_prob, obstacle_prob])[0]
                for i in range(0, 10)
            ],
            [
                random.choices([0, 3], [1 - obstacle_prob, obstacle_prob])[0]
                for i in range(0, 10)
            ],
            [
                random.choices([0, 3], [1 - obstacle_prob, obstacle_prob])[0]
                for i in range(0, 10)
            ],
            [
                random.choices([0, 3], [1 - obstacle_prob, obstacle_prob])[0]
                for i in range(0, 10)
            ],
            [
                random.choices([0, 3], [1 - obstacle_prob, obstacle_prob])[0]
                for i in range(0, 10)
            ],
            [1]
            + [
                random.choices([0, 3], [1 - obstacle_prob, obstacle_prob])[0]
                for i in range(0, 9)
            ],
        ]
        self.reset()

    def load_default(self) -> None:
        """
        Function that load the default arena
        """
        self.__generated_arena = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 3, 3, 0, 3, 0, 0, 3, 3],
            [0, 0, 3, 3, 0, 3, 0, 3, 0, 0],
            [0, 0, 0, 0, 0, 3, 0, 0, 3, 0],
            [3, 3, 3, 3, 0, 0, 0, 0, 3, 0],
            [0, 0, 0, 0, 0, 0, 3, 0, 3, 0],
            [0, 3, 3, 0, 0, 0, 3, 0, 3, 0],
            [0, 0, 0, 0, 0, 3, 3, 0, 0, 0],
            [0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        ]
        self.reset()

    def reset(self) -> None:
        """
        Function that resets the environment
        """
        self.__init()

    def set_agent(self, x: int, y: int) -> None:
        """
        Function that move the Agent to the new position

        Args:
            x (int): the x coordinate of the new position in the arena
            y (int): the y coordinate of the new position in the arena
        """
        if self.__is_collision(x, y):
            self.collision = True
            return
        else:
            self.collision = False

        self.arena[x][y] = 1

        prev_x, prev_y = self.agent_pos
        self.arena[prev_x][prev_y] = 0

        self.agent_pos = (x, y)

        if self.agent_pos == self.exit_pos:
            self.done = True

        self.step += 1

    # execute(current_state, action) = next_state, reward
    def move_agent(self, move: Move) -> tuple:
        """
        Function that executes an Agent move in the current state. It returns the next state and the reward of the next state

        Args:
            move (Move): the move of the Agent

        Returns:
            tuple: (next state, reward) pair
        """
        next_state = deepcopy(self)
        next_state.last_action = move
        x, y = next_state.agent_pos

        if move == Move.UP:
            next_state.set_agent(x - 1, y)
        elif move == Move.DOWN:
            next_state.set_agent(x + 1, y)
        elif move == Move.LEFT:
            next_state.set_agent(x, y - 1)
        elif move == Move.RIGHT:
            next_state.set_agent(x, y + 1)
        else:
            raise RuntimeError("Illegal move")

        return (next_state, next_state.reward())

    def reward(self):
        """
        Function that computes the reward of the current state

        Rewards setting:
            -100: wall collision
            -1: step
            +10000: agent arrives at exit
        """
        reward = -self.step

        if self.collision:
            reward -= 100

        if self.done:
            reward += 10000

        return reward

    def __is_collision(self, x: int, y: int) -> bool:
        """
        Function that checks if a collision with an obstacle of with the arena occurred

        Args:
            x (int): x coordinate of the position in the arena
            y (int): y coordinate of the position in the arena

        Returns:
            bool: True if (x, y) is occupied by an obstacle or is an out of bounds position of the arena
        """
        return x < 0 or x > 9 or y < 0 or y > 9 or self.arena[x][y] == 3

    def __get_colored_tile(self, x: int, y: int) -> str:
        """
        Function that returns the colored tile according to its content

        Tile contents:
            1: the Agent     -> blue
            2: the Exit      -> green
            3: the obstacles -> red
            0: empty         -> white
        """
        if self.arena[x][y] == 1:
            return f"{Back.BLUE}  "
        elif self.arena[x][y] == 2:
            return f"{Back.GREEN}  "
        elif self.arena[x][y] == 3:
            return f"{Back.RED}  "
        else:
            return f"{Back.WHITE}  "

    def __str__(self) -> str:
        arena = ""
        for i in range(0, 10):
            for j in range(0, 10):
                if j == 9:
                    arena += self.__get_colored_tile(i, j) + f"{Style.RESET_ALL}" + "\n"
                else:
                    arena += self.__get_colored_tile(i, j) + f"{Style.RESET_ALL}"
        return arena
