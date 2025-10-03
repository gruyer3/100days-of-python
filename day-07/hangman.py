import random

word_list = ["pepperoni", "cheddar", "anchois"]

word_to_guess = random.choice(word_list)
placeholder = ""

for letter in word_to_guess:
    placeholder += "_"
print(placeholder)

user_choice = input("Guess a letter: ").lower()

display = ""
for letter in word_to_guess:
    if letter == user_choice:
        display += user_choice
    else:
        display += "_"

print(display)