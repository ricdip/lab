import argparse


class Args:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="An implementation of n-puzzle solved by AI search algorithms"
        )

    def parse_args(self) -> argparse.Namespace:
        self.parser.add_argument(
            "-n",
            "--n-tiles",
            help="set number of tiles. Default value: 8",
            type=int,
            default=8,
        )

        return self.parser.parse_args()
