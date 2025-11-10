#!/usr/bin/env python3

import sys

args = sys.argv[1:]

if len(args) == 0:
    pass

elif len(args) > 1:
    raise AssertionError("More than one arguments is provided")

else:
    try:
        number = int(args[0])
        if number == 0:
            print("I'm Zero.")
        elif number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        raise AssertionError("argument is not an integer")
