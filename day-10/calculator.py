def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
    }

n1 = float(input("Number 1: "))
operation = input("Operation: ")
n2 = float(input("Number 2: "))

def result():
    return calculations[operation](n1, n2)

print(result())

