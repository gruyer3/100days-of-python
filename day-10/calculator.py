from logo import logo
from functions import add, subtract, multiply, divide, calculations

def calculator():
    print(logo)
    n1 = float(input("What's the first number?: "))
    for key in calculations:
        print(key)
    running = True

    while running:
        operation = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))
        task = calculations[operation]
        answer = task(n1, n2)
        print(f"{n1} {operation} {n2} = {answer}")

        continuity = input(f"Type 'y' to continue calculating with {n2}, or type 'n' to start a new calculation.: ")

        if  continuity == 'y':
            num1 = answer
        else:
            running = False
            calculator()


calculator()