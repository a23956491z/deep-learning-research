import argparse

parser = argparse.ArgumentParser()

# Error happens if no argument
# even if too much arguments
parser.add_argument("arg1")
parser.add_argument("arg2",
                    help="It's argument 2, input a integer")
# If we assign a type to argument, the input argument should be the type!
parser.add_argument("arg3",
                    help="It's argument 3, \"must\" input integer",
                    type=int)

args = parser.parse_args()
print(f"arg1 {args.arg1:^10}, type={type(args.arg1)}")
print(f"arg2 {args.arg2:^10}, type={type(args.arg2)}")
print(f"arg3 {args.arg3:^10}, type={type(args.arg3)}")