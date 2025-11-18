#!/usr/bin/env python3

import time
import sys

def ft_progress(lst):
    """
    Générateur qui affiche une barre de progression tout en itérant sur lst.
    """

    total = len(lst)
    start_time = time.time()

    for i, item in enumerate(lst):
        current_time = time.time()
        elapsed_time = current_time - start_time

        if i == 0:
            eta = 0
        else:
            avg_time_per_item = elapsed_time / i
            eta = avg_time_per_item * (total - i)
        percent = int((i / total) * 100)
        bar_length = 20
        filled_length = int(bar_length * i //total)
        bar = "=" * filled_length + ">" + " " * (bar_length - filled_length)
        print(f"\rETA: {eta:.2f}s [{percent:3d}%] [{bar}] {i}/{total} | elapsed time {elapsed_time:.2f}s", end="")
        yield item
    elapsed_total = time.time() - start_time
    bar = "=" * 20 + ">"
    print(f"\rETA: 0.00s [100%] [{bar}] {total}/{total} | elapsed time {elapsed_total:.2f}s")

# ------------------------------------------------------------------
if __name__ == "__main__":
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)
    
    # Deuxième test (optionnel, pour voir avec une plus grosse liste)
    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        time.sleep(0.005)
    print()
    print(ret)
    