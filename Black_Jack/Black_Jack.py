"""
Black Jack

This program allows you to play the classic black jack game.

"""

from Black_Jack_DB import logo
import random

# from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def get_new_card(new_card, sum_user, sum_computer):
    if new_card == 'y':
        user.append(random.choice(cards))
        computer.append(random.choice(cards))
        sum_user = sum(user)
        sum_computer = sum(computer)
        check_user(new_card, sum_user, sum_computer)
    elif new_card == 'n':
        check_computer(new_card, sum_user, sum_computer)


def check_user(new_card, sum_user, sum_computer):
    if sum_user <= 21:
        if sum_user > 10 and user[-1] == 11:
            user[-1] = 1
            print(f"Your cards: {user}, current score: {sum_user}")
            print(f"Computer's first card: {computer[0]}")
            yes_no()
        else:
            print(f"Your cards: {user}, current score: {sum_user}")
            print(f"Computer's first card: {computer[0]}")
            yes_no()

    elif sum_user > 21:
        if user[-1] == 11:
            user[-1] = 1
            sum_user = sum(user)
            check_user(new_card, sum_user, sum_computer)

        else:
            print(f"Your final hand: {user}, final score: {sum_user}")
            print(f"Computer's final hand: {computer}, final score: {sum_computer}")
            print("You went over. You Lose...")


def check_computer(new_card, sum_user, sum_computer):
    if sum_computer < 17:
        computer.append(random.choice(cards))
        sum_computer = sum(computer)
        get_new_card(new_card, sum_user, sum_computer)
    elif sum_computer >= 17:
        print(f"Your final hand: {user}, final score: {sum_user}")
        print(f"Computer's final hand: {computer}, final score: {sum_computer}")
        if sum_computer > 21:
            print("Congratulations....You Win")
        else:
            winner(sum_user, sum_computer)


def yes_no():
    new_card = input("Type 'y' to get another card, type 'n' to pass:")
    sum_user = sum(user)
    sum_computer = sum(computer)
    get_new_card(new_card, sum_user, sum_computer)


def black_jack():
    if sum_user == 21 and sum_computer == 21:
        print("BLACK JACK... for both user and computer")
        print(f"User hand : {user}, \n Computer hand : {computer}")
        print("You Lose")
    elif sum_user == 21:
        print(f"User hand : {user}, BLACK JACK...")
        print("You Win")
    elif sum_computer == 21:
        print(f"Computer hand : {computer}, BLACK JACK...")
        print("You Lose")
    else:
        yes_no()


def winner(sum_user, sum_computer):
    if abs(21 - sum_user) == abs(21 - sum_computer):
        print("It's a Draw")
    elif abs(21 - sum_user) < abs(21 - sum_computer):
        print("Congratulations....You Win")
    else:
        print("You Lose")


I = True
while I:
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    # clear()
    print(logo)
    computer = []
    user = []
    if start == 'y':
        for i in range(2):
            user.append(random.choice(cards))
            computer.append(random.choice(cards))

        sum_user = sum(user)
        sum_computer = sum(computer)

        print(f"Your cards: {user}, current score: {sum_user}")
        print(f"Computer's first card: {computer[0]}")
        black_jack()
    else:
        I = False
        print("Good Bye.... Have a nice day!!")
