
# Number Guessing Game - Python Practice

import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)

# Choose difficulty
def choose_difficulty():
    level = input("Choose a difficulty (easy or hard): ").lower()

    if level == "easy":
        return 10
    elif level == "hard":
        return 5
    else:
        return 0

attempts = choose_difficulty()

if attempts == 0:
    print("Invalid difficulty!")

# Guess the number
while attempts > 0:
    print(f"You have {attempts} attempts remaining.")

    guess = int(input("Make a guess: "))

    if guess == number:
        print("You got it! You win!")
        break

    elif guess > number:
        print("Too high!")

    else:
        print("Too low!")

    attempts -= 1

    if attempts == 0:
        print(f"Game over! The number was {number}.")
