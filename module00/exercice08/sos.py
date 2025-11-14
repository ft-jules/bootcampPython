#!/usr/bin/env python3

import sys

MORSE_CODE_DICT = {
    ' ': '/',
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}

def main():
    print("TEST")
    args = sys.argv[1:]
    if not args:
        return
    full_string = " ".join(args)
    for char in full_string:
        if not (char.isalnum() or char.isspace()):
            print("ERROR")
            return
    morse_list = []
    for char in full_string:
        upper_char = char.upper()
        morse_list.append(MORSE_CODE_DICT[upper_char])
    print(" ".join(morse_list))

if __name__ == "__main__":
    main()
