import argparse


class Args:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="A reinforcement learning maze implementation using Q-learning"
        )

    def parse_args(self) -> argparse.Namespace:
        self.parser.add_argument(
            "-a",
            "--alpha",
            help="set Alpha hyperparameter for Agent's Q-learning algorithm: [0, 1]. Default value: 0.3",
            type=Args.restricted_0_1_float_type,
            default=0.3,
        )

        self.parser.add_argument(
            "-g",
            "--gamma",
            help="set Gamma hyperparameter for Agent's Q-learning algorithm: [0, 1]. Default value: 0.9",
            type=Args.restricted_0_1_float_type,
            default=0.9,
        )

        self.parser.add_argument(
            "-e",
            "--epsilon",
            help="set Epsilon hyperparameter for Agent's Q-learning algorithm: [0, 1]. Default value: 0.3",
            type=Args.restricted_0_1_float_type,
            default=0.3,
        )

        self.parser.add_argument(
            "-eps",
            "--episodes",
            help="set number of episodes hyperparameter for Agent's Q-learning algorithm: [0, n]. Default value: 5000",
            type=Args.restricted_0_n_int_type,
            default=5000,
        )

        self.parser.add_argument(
            "-s",
            "--shape",
            help="set arena shape: rows,columns. Default value: 10,10",
            type=Args.arena_shape_type,
            default=(10, 10),
        )

        return self.parser.parse_args()

    @staticmethod
    def restricted_0_1_float_type(x):
        try:
            f = float(x)
        except:
            raise argparse.ArgumentTypeError(f"'{x}' is not a float")

        if f < 0.0 or f > 1.0:
            raise argparse.ArgumentTypeError(f"'{x}' is not in range [0, 1]")

        return f

    @staticmethod
    def restricted_0_n_int_type(x):
        try:
            i = int(x)
        except:
            raise argparse.ArgumentTypeError(f"'{x}' is not a int")

        if i < 0:
            raise argparse.ArgumentTypeError(f"'{x}' is not in range [0, n]")

        return i

    @staticmethod
    def arena_shape_type(x):
        try:
            shape = x.split(",")
            i, j = map(Args.restricted_0_n_int_type, shape)
        except:
            raise argparse.ArgumentTypeError(
                f"Coordinates are not int [0, n] in form x,y"
            )

        return (i, j)
