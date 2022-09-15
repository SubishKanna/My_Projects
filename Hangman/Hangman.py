"""
HANGMAN PROJECT

"""

import random
# from replit import clear
from Hangman_DB import logo, word_list, stages

chosen_word = random.choice(word_list)
lives = 6

print(logo)
# print(f'Pssst, the solution is {chosen_word}.')
display = []

for i in range(len(chosen_word)):
    display.append("_")

while "_" in display:
    user_guess = input("\nGuess a letter: ").lower()
    # clear()
    if user_guess in display:
        print(f"You've already guessed {user_guess}")

    for letter in range(len(chosen_word)):
        if chosen_word[letter] == user_guess:
            display[letter] = user_guess

    if not lives == 0:
        if user_guess not in display:
            print(f"You guessed {user_guess}, that's not in the word. You lose a life\n")
            lives -= 1
    else:
        print(stages[lives])
        print("Game Over.....You lose")

    print(f"{' '.join(display)}")
    print(stages[lives])

print("\nCongrats!!!! You won")
