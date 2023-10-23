from environment import Environment
import numpy as np
import random
import time


class Agent:
    """
    Agent implementation that uses Q-learning. The algorithm allows the Agent to use the environment's rewards to learn the best action to take in a given state.

    Q-learning algorithm:

        - uses Q-table, the values stored in the Q-table are the Q-values, mapping (state, action) -> Q-value

        - a Q-value for a particular state-action combination is the quality of an action taken from a state, better Q-values = better chances of greater rewards

        - as the agent exposes itself to the environment and receives different rewards by executing different actions, the Q-values are updated in the following manner:

            Q(state, action) = (1 - alpha) * Q(state, action) + alpha * (reward + gamma * max_action(Q(next_state, all_actions)))

        where:
            - alpha: learning rate (0 < alpha <= 1), determines to what extent newly acquired information overrides old information. With 0 the agent learn nothing (exploitation, choosing actions based on already learned Q-values), with 1 the agent consider only the most recent information (exploration, choosing random action)

            - gamma: discount factor (0 <= gamma <= 1), determines how much importance we give to future reward. With a value close to 1 we consider the long-term effective rewards, with 0 we consider only immediate reward (greedy)

        - so, we are learning the correct action to take in the current state by looking at the reward for (current state, action), and the max rewards for the next state (considering all actions that we can take to arrive at the next state)

        - Q(state, action), so, the Q-value of a state-action pair is the sum of the instant reward and the discounted future reward (of the resulting state). We store the Q-values for each state and action in the Q-table

        - Q-table: matrix with row = every state (state space), column = every action (action space). It's initialized to 0, and the Q-values are updated during training

        - after enough random exploration of actions, the Q-values tend to converge serving the agent as an action-value function which it can exploit to pick the most optimal action for a given state

        - tradeoff between exploration and exploitation: we want to prevent the action from always taking the same route. So we introduce the parameter "epsilon"
            - epsilon: probability to choose a random action (exploration) instead of choosing the best learned Q-value action (exploitation)
    """

    def __init__(self, env: Environment):
        """
        Agent constructor

        Args:
            env (Environment): the environment that the agent will explore

        Attributes:
            env (Environment): the environment that the agent will explore
            q_table (np array): the Q-table with shape (state space, action space)
            trained (bool): set to True if the training is completed
        """
        self.env = env
        # Q-table: a row for every state, a column for every action, all Q-values are 0
        self.q_table = np.zeros(
            (self.env.state_space, self.env.action_space), dtype=int
        )
        self.trained = False

    def train(self, alpha=0.3, gamma=0.9, epsilon=0.3, episodes=5000) -> None:
        """
        The function that executes the training of the agent

        Args:
            alpha (float): learning rate hyperparameter
            gamma (float): discount factor hyperparameter
            epsilon (float): probability of choosing exploration instead of exploitation hyperparameter
            episodes (int): total number of episodes
        """
        # do not re-run training if already executed
        if self.trained:
            return

        state = self.env
        rows, cols = state.shape

        # for each episode, the agent goes from initial state to final state, and we update the Q-table
        for i in range(1, episodes + 1):
            # reset state
            state.reset()

            # explore environment from initial state to final state
            while not state.done:
                # the grid contains all state, we get the current state_index from the agent position
                agent_x, agent_y = state.agent_pos
                state_index = agent_x * rows + agent_y

                # random.uniform(0, 1) returns a random float number in the interval [0, 1]
                if random.uniform(0, 1) < epsilon:
                    # explore action space: choose a random action (actions are 0, 1, 2, 3)
                    action_index = random.choice(range(0, state.action_space))
                else:
                    # exploit learned values: choose the action that maximizes the Q-value for the current state
                    # Q(state, action), so with Q(state) we have all the array of actions from state. With argmax we get the action_index (0, 1, 2, 3) with max Q(state, action) value (Q-value)
                    action_index = np.argmax(self.q_table[state_index])

                # we get the action object from the action_index
                action = state.actions[action_index]
                # we compute the next state from the current state, so we get the next state and the reward
                next_state, reward = state.move_agent(action)
                # we get the new state_index from agent position
                next_agent_x, next_agent_y = next_state.agent_pos
                next_state_index = next_agent_x * rows + next_agent_y

                # we get the old Q(state, action) for old state from Q-table
                old_value = self.q_table[state_index, action_index]
                # we get the new max_action(Q(next_state, all actions)) for new state from Q-table: with np.max we get the max Q-value from all actions associated with next_state
                next_max = np.max(self.q_table[next_state_index])

                # we apply the Q-learning formula
                new_value = (1 - alpha) * old_value + alpha * (
                    reward + gamma * next_max
                )
                # we update the Q(state, action) in the Q-table
                self.q_table[state_index, action_index] = new_value

                # the agent is in the next_state
                state = next_state

            # we print the current episode
            print(f"Episode: {i}", end="\r")

        print("")
        print("training completed")

        self.trained = True

    def exec(self) -> None:
        """
        The function that executes the agent exploration of the environment. The explored states are printed to stdout
        """
        state = self.env
        rows, cols = state.shape
        # we reset the state and print it
        state.reset()
        self.print_state(state)

        # explore environment from initial state to final state
        while not state.done:
            # the grid contains all state, we get the current state_index from the agent position
            agent_x, agent_y = state.agent_pos
            state_index = agent_x * rows + agent_y

            # we exploit the Q-table to choose the best action to take in the current state
            action_index = np.argmax(self.q_table[state_index])
            # we get the action object from the action_index
            action = state.actions[action_index]

            # we compute the next state from the current state, so we get the next state and the reward
            state, reward = state.move_agent(action)

            # we print the new state
            self.print_state(state)
            # we sleep so that we can follow the steps of the agent during the exploration
            time.sleep(1)

    def print_state(self, state: Environment) -> None:
        """
        Function that prints a state to stdout

        Args:
            state (Environment): the state to print
        """
        print(state, end="")
        print(f"collision: {state.collision}")
        print(f"   action: {state.last_action}")
        print(f"     done: {state.done}")
        print(f"     step: {state.step}")
        print("")
        print("")
