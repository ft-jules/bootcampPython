#!/usr/bin/env python3

import random


print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")

x = random.randint(1, 99)
attempts = 0

while True:
    guess = input("Choose a number between 1 and 99 >>> ")
    attempts +=1
    if guess == 'exit':
        print("Goodbye!")
        break
    try:
        nb = int(guess)
    except ValueError:
        print("That's not a number.")
        continue
    if not (1 <= nb <= 99):
        print("Your guess must be between 1 and 99.")
        continue
    if nb > x:
        print("Too high")
        continue
    elif nb < x:
        print("Too low")
        continue
    else:
        if x == 42:
            print("The answer to the ultimate question of life, "
              "the universe and everything is 42.")
            print("Congratulations!")
        else:
            print("Congratulations, you've got it!")
        if attempts == 1:
            print("You got it on your first try!")
        else:
            print(f"You won in {attempts} attempts!")

        break
