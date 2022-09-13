import random
from replit import clear
from Hangman_DB import logo, word_list, stages


chosen_word = random.choice(word_list)
lives = 6

print(logo)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for i in range(len(chosen_word)):
  display.append("_")

while "_" in display:
  
  guess = input("\nGuess a letter: ").lower() 
  clear()
  if guess in display:
    print(f"You've already guessed {guess}")
  
  for letter in range(len(chosen_word)):
    if chosen_word[letter] == guess:
      display[letter] = guess
  
  if not lives == 0:
    if guess not in display:
      print(f"You guessed {guess}, that's not in the word. You lose a life\n")
      lives-=1
  else:
    print(stages[lives])
    print("Game Over.....You lose")

  print(f"{' '.join(display)}")
  print(stages[lives])

print("\nCongrats!!!! You won")
