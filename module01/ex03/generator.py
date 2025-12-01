import sys
import random

def generator(text, sep=" ", option=None):
    if not isinstance(text, str) or option not in [None, "shuffle", "unique", "ordered"]:
        yield "ERROR"
        return
    
    words = text.split(sep)

    if option == "ordered":
        words.sort()
    elif option == "unique":
        seen = set()
        unique_words = []
        for word in words:
            if word not in seen:
                unique_words.append(word)
                seen.add(word)
        words = unique_words
    elif option == "shuffle":
        for i in range(len(words) - 1, 0 , -1):
            j = random.randint(0, i)
            words[i], words[j] = words[j], words[i]
    for word in words:
        yield word