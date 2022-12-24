#!/usr/bin.python3


def print_square(size):

    type_err = "size must be an integer"
    value_err = "size must be >= 0"

    if (not isinstance(size, int)):
        raise TypeError(type_err)

    if (size < 0):
        raise ValueError(value_err)

    if (isinstance(size, float) and size < 0):
        raise TypeError(type_err)

    i = 0
    while (i < size):

        j = 0
        while (j < size):
            print("#", end='')
            j += 1

        print()
        i += 1
