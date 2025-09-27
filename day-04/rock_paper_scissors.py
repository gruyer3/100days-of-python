import random

player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer_choose = random.randint(0, 2)

choices = ["Rock", "Paper", "Scissors"]

if player_input >= 3:
    print("You've chosen wrong number. Try again!")
else:
    print(f"You've chosen {choices[player_input]}")
    print(f"Computer chose {choices[computer_choose]}")
    if computer_choose == 0 and player_input == 2:
        print("You lost!")
    elif player_input == 0 and computer_choose == 2:
        print("You won!")
    else:
        if player_input > computer_choose:
            print("You won!")
        elif player_input == computer_choose:
            print("It's a draw!")
        else:
            print("You lost!")