from state import State
from heuristics import MisplacedTiles
from algorithms import AStar
from args import Args


def run(n_tiles: int) -> None:
    initial_state = State(n_tiles=n_tiles)
    heuristic = MisplacedTiles(template=initial_state)
    algorithm = AStar(heuristic=heuristic, status=True)

    print(initial_state.repr)

    path = algorithm.exec(initial_state)

    print("\nSolution:\n")

    for state in path:
        print(state, end="\n\n")


def main() -> None:
    cli_args = Args().parse_args()
    run(cli_args.n_tiles)


if __name__ == "__main__":
    main()
