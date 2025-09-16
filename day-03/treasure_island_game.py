print("Welcome to the Treasure Island.\nYour mission is to find the treasure.")
direction = input("Which direction are you gonna go? Left or right? ").lower()

if direction == "left":
    boat = input("You found the river and see the boat coming your way.\nAre you going to swim down the river or wait for the boat? ").lower()
    if boat == "wait":
        door = input("You managed to get the boat and swim down the river.\nYou stopped near the lighthouse with three doors - yellow, red and blue. Which one are you going to open? ").lower()
        if door == "yellow":
            print("There's a treasure behind the doors. You win!")
        elif door == "blue":
            print("You got shot by a stranger. Game over.")
        elif door == "red":
            print("Doors exploded. Game over.")
        else:
            ("You were supposed to open the door. Game over.")
    elif boat == "swim":
        print("You drowned. Game over.")
    else:
        print("You got attacked by a tiger. Game over.")
else:
    print("You're lost in the jungle. Game over.")
    