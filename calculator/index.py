import os

os.system("cls")

friends = ""                    # variables

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

while True:                 # the main loop
    action = input("\"1\" to add\n\"2\" to remove\n\"3\" to change\n\"4\" or \"q\" to quit\n\n")
    if action.isdigit():
        action = int(action)
    if action == 1:
        a = float(input("a: "))
        b = float(input("b: "))
        os.system("cls")
        print(f"{a} + {b} = {addition(a, b)}")
    
    if action == 2:
        a = float(input("a: "))
        b = float(input("b: "))
        os.system("cls")
        print(f"{a} - {b} = {subtraction(a, b)}")