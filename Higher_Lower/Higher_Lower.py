"""
HIGHER LOWER

This program allows you to play the higher lower game.

"""

from Higher_Lower_DB import data, logo, vs
import random

# from replit import clear as cl
A_B = ["A", "B"]
store_data = []
follower_count = []
score = 0


def get_data(random_number):
    store_data.append(data[random_number])


def swap():
    store_data.pop(0)
    follower_count.clear()
    rand_number = random.randint(0, len(data) - 1)
    get_data(rand_number)
    p_data(store_data)


def p_data(store_data):
    for i in range(len(store_data)):
        name = store_data[i]['name']
        follower_count.append(store_data[i]['follower_count'])
        description = store_data[i]['description']
        country = store_data[i]['country']
        print(f"Compare {A_B[i]} : {name} a {description} from {country}")
        if i == 0:
            print(vs)


def compare():
    global score
    if follower_count[0] > follower_count[1] and user == 'A':
        score += 1
        print(f"You are right! Current score : {score}")
        swap()
    elif follower_count[0] > follower_count[1] and user == 'B':
        print(f"Sorry.. You lose. Your score is {score}")
        return 0
    elif follower_count[0] < follower_count[1] and user == 'A':
        print(f"Sorry.. You lose. Your score is {score}")
        return 0
    elif follower_count[0] < follower_count[1] and user == 'B':
        score += 1
        print(f"You are right! Current score : {score}")
        swap()


for _ in range(2):
    rand_number = random.randint(0, len(data) - 1)
    get_data(rand_number)
print(logo)
p_data(store_data)

cont = True
while cont:
    user = input("Who has more followers? Type 'A' or 'B' : ")
    # cl()
    print(logo)
    value = compare()
    if value == 0:
        cont = False
