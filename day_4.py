# Guessing Game

from random import randint

num = int(input("Guess the number b/w 1-100: "))

guess = randint(1, 100)

total_guess = 0

while num > 0:
    if num == guess:
        print("You guessed it")
        total_guess += 1
        break
    elif num > guess:
        print("Guess Lower")
        num = int(input("Guess the number b/w 1-100: "))
        total_guess += 1
    elif num < guess:
        print("Guess Higher")
        num = int(input("Guess the number b/w 1-100: "))
        total_guess += 1

print(f"Total guesses = {total_guess}")
