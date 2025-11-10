#!/usr/bin/env python3

import sys

args_list = sys.argv[1:]

if not args_list:

    pass

else:

    full_string = "".join(args_list)

    reversed_string = full_string[::-1]

    swapped_case_string = reversed_string.swapcase()

    print(swapped_case_string)
