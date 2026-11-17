
# Password Generator - Python Practice

import random

print("Welcome to the Password Generator!")

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!#$%&()*+"

num_letters = int(input("How many letters would you like? "))
num_numbers = int(input("How many numbers would you like? "))
num_symbols = int(input("How many symbols would you like? "))

# Generate the password
password = []

for i in range(num_letters):
    password.append(random.choice(letters))

for i in range(num_numbers):
    password.append(random.choice(numbers))

for i in range(num_symbols):
    password.append(random.choice(symbols))

# Shuffle the characters
random.shuffle(password)

# Join the characters into a string
final_password = "".join(password)

print(f"Your password is: {final_password}")
