#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv)
    text = "{:d} argument{:s}{:s}\n".format(
        argc - 1, ("" if argc == 2 else "s"), ("." if argc == 1 else ":")
    )
    for i in range(1, argc):
        text += "{:d}: {:s}\n".format(i, sys.argv[i])
    print(text, end="")
    