#!/usr/bin/env python3

import sys
import string

def text_analyzer(text=None):
    """
    This function counts the number of upper characters, lower characters, 
    punctuation and spaces in a givne text.
    """
    if text is None:
        try:
            text = input("What is the text to analyze?\n>> ")
        except EOFError:
            return
    if not isinstance(text, str):
        raise AssertionError("argument is not a string")

    upper_count = 0
    lower_count = 0
    punct_count = 0
    space_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isspace():
            space_count += 1
        elif char in string.punctuation:
            punct_count += 1
    total_chars = len(text)
    print(f"The text contains {total_chars} printable character(s):")
    print(f"{upper_count} upper letter(s)")
    print(f"{lower_count} lower letter(s)")
    print(f"{punct_count} punctuation mark(s)")
    print(f"{space_count} space(s)")

if __name__ == "__main__":
    """
    Partie exécutée SEULEMENT si on lance le script avec:
    $> python3 count.py "mon argument"
    """
    if len(sys.argv) > 2:
        raise AssertionError("too many arguments")
    arg = None
    if len(sys.argv) == 2:
        arg = sys.argv[1]

    text_analyzer(arg)