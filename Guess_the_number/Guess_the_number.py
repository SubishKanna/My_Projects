"""
GUESS THE NUMBER GAME

This program allows you to play the guessing the number game.

"""

from Guess_the_number_DB import logo
import random

# from replit import clear

EASY = 10
HARD = 5
NUMBER = random.randint(1, 100)
GAME = True


def set_difficulty():
    print("Welcome to the Guessing Game!!!")
    print("I'm thinking of a number between 1 and 100.")
    return input("Choose a difficulty. Type  'Easy' or 'Hard' : ").lower()


def easy():
    for i in range(EASY, 0, -1):
        print(f"You have {i} guesses remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess < NUMBER:
            print("Too low")
        elif guess > NUMBER:
            print("Too high")
        else:
            print("Congratulations.... You guess the correct number!!")
            break


def hard():
    for i in range(HARD, 0, -1):
        print(f"You have {i} guesses remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess < NUMBER:
            print("Too low")
        elif guess > NUMBER:
            print("Too high")
        else:
            print("Congratulations.... You guess the correct number!!")
            break


while GAME:
    yes_no = input("Do you want to play the Guessing Game?.. type 'Yes' to continue or Type 'No' to exit : ").lower()
    if yes_no == "yes":
        # clear()
        print(logo)
        difficulty = set_difficulty()
        if difficulty == "easy":
            easy()
        else:
            hard()
    else:
        print("Have a good day...BYE")
        GAME = False
