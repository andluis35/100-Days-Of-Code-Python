import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
random_password = []

for i in range(1, nr_letters + 1):
    random_character = random.choice(letters)
    random_password.append(random_character)

for j in range(1, nr_symbols + 1):
    random_character = random.choice(symbols)
    random_password.append(random_character)

for k in range(1, nr_numbers + 1):
    random_character = random.choice(numbers)
    random_password.append(random_character)

random.shuffle(random_password)

for char in random_password:
    password += char

print(f"Your randomized password is: {password}")
