#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_count = len(sys.argv)
    if args_count <= 1:
        print("{} arguments.".format(args_count - 1))
    elif args_count == 2:
        print("{} argument:".format(args_count - 1))
    else:
        print("{} arguments:".format(args_count - 1))
    for x in range(1, args_count):
        print("{}: {}".format(x, sys.argv[x]))
