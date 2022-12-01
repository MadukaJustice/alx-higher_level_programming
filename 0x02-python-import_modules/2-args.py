#!/usr/bin/python3


def print_arg_list():
    from sys import argv
    argc = len(argv)
    i = 1
    if argc == 1:
        print("{:d} arguments.".format(argc - 1))
    elif argc == 2:
        print("{:d} argument:".format(argc - 1))
    else:
        print("{:d} arguments:".format(argc - 1))
    while i < argc:
        print("{:d}: {:s}".format(i, argv[i]))
        i += 1


if __name__ == "__main__":
    print_arg_list()
