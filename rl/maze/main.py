from environment import Environment
from agent import Agent
from args import Args


def run(
    alpha: float, gamma: float, epsilon: float, episodes: int, shape: tuple
) -> None:
    change_arena = True
    env = Environment(shape=shape)

    # arena generation loop
    while change_arena:
        env.generate_arena()
        print(env)
        choice = input("Generate a new arena? [y/n] ")

        if choice == "n" or choice == "N":
            change_arena = False

    agent = Agent(env)
    # Agent training
    agent.train(alpha=alpha, gamma=gamma, epsilon=epsilon, episodes=episodes)

    print("Exec...")

    # Agent execution
    agent.exec()


def main() -> None:
    # parse cli args
    cli_args = Args().parse_args()
    # execution
    run(
        cli_args.alpha,
        cli_args.gamma,
        cli_args.epsilon,
        cli_args.episodes,
        cli_args.shape,
    )


if __name__ == "__main__":
    main()
