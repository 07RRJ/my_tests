import os

os.system("cls")

print("=" * 18)
print("===", "calculator", "===")
print("=" * 18)
print("""\nyou can use these in your equation:
\"+\" - add addition
\"-\" - subtract
\"*\" - multiply
\"**\" - potencies
\"/\" - divide
\"//\" - divide without decimals
""")


while True:
    number = input("your equation: ")
    os.system("cls")
    try:
        print(f"{number} = {eval(number)}\n")
    except:
        print("something went wrong")