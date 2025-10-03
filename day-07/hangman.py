import random

word_list = ["pepperoni", "cheddar", "anchois"]

word_to_guess = random.choice(word_list)

user_choice = input("Guess a letter: ").lower()

for letter in word_to_guess:
    if letter == user_choice:
        print("Right")
    else:
        print("Wrong")