import random

word_list = ["pepperoni", "cheddar", "anchois"]

word_to_guess = random.choice(word_list)
placeholder = ""

for letter in word_to_guess:
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while True:

    user_choice = input("Guess a letter: ").lower()

    display = ""
    for letter in word_to_guess:
        if letter == user_choice:
            display += user_choice
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You won!")