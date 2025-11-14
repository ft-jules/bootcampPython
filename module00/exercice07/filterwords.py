#!/usr/bin/env python3

import sys
import string

try:
    if len(sys.argv) != 3:
        raise ValueError("Nombre d'arguments incorrect")

    S = sys.argv[1]
    N = int(sys.argv[2])
except ValueError:
    print("Error Args")
    sys.exit()

translator = str.maketrans('', '', string.punctuation)
cleaned_S = S.translate(translator)

word_list = cleaned_S.split()

result_list = [word for word in word_list if len(word) > N]

print(result_list)