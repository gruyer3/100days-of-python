from art import logo

should_run = True

print(logo)
print("Welcome to the Secret Auction")

while should_run == True:
    all_bids = {}

    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    others = input("Are there any other bidders? Type 'yes' or 'no':\n")

    all_bids[name] = bid

    while others == "yes":
        print("\n" * 100)
        name = input("What is your name?: ")
        bid = int(input("What's your bid?: $"))
        others = input("Are there any other bidders? Type 'yes' or 'no':\n")
        all_bids[name] = bid
        
        if others == "no":
            winner_name = max(all_bids, key=all_bids.get)
            highest_bid = max(all_bids.values())
            print(f"The winner is {winner_name} with bid amount of ${highest_bid}")
            should_run = False