from environment import Environment
from agent import Agent
import sys

change_arena = True
env = Environment()

# arena generation loop
while change_arena:
    env.generate_arena()
    print(env)
    choice = input("Generate a new arena? [y/n] ")

    if choice == "n" or choice == "N":
        change_arena = False

agent = Agent(env)
# Agent training
agent.train(alpha=0.3, gamma=0.9, epsilon=0.3, episodes=5000)

print("Solving...")

# Agent execution
agent.execute()
