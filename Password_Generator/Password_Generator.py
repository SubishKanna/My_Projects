"""
PASSWORD GENERATOR

This program allows you to generate password based on your input (no of letters, symbols, numbers)


"""

import random
from Password_Generator_DB import letters, numbers, symbols

print("Hello.....Welcome to the Password Generator!!")
n_letters = int(input("How many letters would you like in your password?\n"))
n_symbols = int(input("How many symbols would you like in  your password?\n"))
n_numbers = int(input("How many numbers would you like in  your password?\n"))

total_len = n_letters + n_symbols + n_numbers
random_letters = ''
random_numbers = ''
random_symbols = ''
your_password = ''

for i in range(total_len):
    if i < n_letters:
        random_letters += letters[random.randint(0, len(letters) - 1)]
    if i < n_numbers:
        random_numbers += numbers[random.randint(0, len(numbers) - 1)]
    if i < n_symbols:
        random_symbols += symbols[random.randint(0, len(symbols) - 1)]

your_password = random_letters + random_numbers + random_symbols
print("Here's your generated password\n", your_password)

shuffled_password = ''.join(random.sample(your_password, len(your_password)))
print("Here's your generated shuffled password\n", shuffled_password)
