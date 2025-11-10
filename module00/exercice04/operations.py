#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("Usage: python operations.py <number1> <number2>")
    print("Example: python operations.py 10 3")
    raise AssertionError("Wrong number of arguments")

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
except ValueError:
    raise AssertionError("only intergers")

print(f"Sum:        {a + b}")
print(f"Difference: {a - b}")
print(f"Product:    {a * b}")

try:
    print(f"Quotient:   {a / b}")
except ZeroDivisionError:
    print("Quotient:   ERROR (division by zero)")

try:
    print(f"Remainer:   {a % b}")
except ZeroDivisionError:
    print("Remainer:   ERROR (division byb zero)")
