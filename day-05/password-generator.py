import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "q", "t", "u", "w", "v", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "[", "}", "]", ";", ":", "'", '"', "|", "<", ">", ",", ".", "?", "/"]

print("Welcome to Password Generator!")
nr_letters = int(input("How many letters would you like? "))
nr_numbers = int(input("How many numbers would you like? "))
nr_special = int(input("How many special characters would you like? "))

password = []
random_upper = random.randint(1, nr_letters + 1)

for number in range(1, nr_letters + 1 - random_upper):
    password += random.choice(letters)

for number in range(1, random_upper + 1):
    password += random.choice(letters).upper()

for number in range(1, nr_numbers + 1):
    password += random.choice(numbers)

for number in range(1, nr_special + 1):
    password += random.choice(special)

random.shuffle(password)

final_passwd = ""
for element in password:
    final_passwd += element

print(f"Your password is:\n{final_passwd}")