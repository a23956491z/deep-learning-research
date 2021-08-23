import argparse

parser = argparse.ArgumentParser()
parser.add_argument("arg1",
                    nargs=3,
                    type=int,
                    help="pls type 3 integers")
parser.add_argument("arg2",
                    nargs='?',
                    help="argument 2, type 1 value or none",
                    default=None)
parser.add_argument("arg3",
                    nargs='+',
                    help="argument 3, type at least 1 value")


args = parser.parse_args()
print(args)