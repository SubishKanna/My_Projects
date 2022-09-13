#Password Generator Project
import random
from Password_Generator_DB import letters, numbers, symbols


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


total_len = nr_letters+nr_symbols+nr_numbers
r_letter = ''
r_number = ''
r_symbol = ''
password = ''

for i in range(total_len):
    if i<nr_letters:
        r_letter += letters[random.randint(0,len(letters)-1)]
    if i<nr_numbers:
        r_number += numbers[random.randint(0,len(numbers)-1)]
    if i<nr_symbols:
        r_symbol += symbols[random.randint(0,len(symbols)-1)]

password = r_letter+r_number+r_symbol
print("Here's your generated passsword\n",password)

pass_shuf =''.join(random.sample(password,len(password)))
print("Here's your generated shuffled passsword\n",pass_shuf)

