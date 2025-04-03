import os
from msvcrt import getwch
from time import sleep

bits = 0
bits_click = 1
price_1 = 10

def the_game():
    os.system("cls")
    print("=" * 23)
    print("=== console clicker ===")
    print("=" * 23)
    print(f"\nclick - spacebar\n1 - upgrade 1: {price_1}\n")

    print(bits)
    click = getwch()
    if click == " ":
        bits += bits_click
    if click == "1" and bits > price_1:
        bits -= price_1
        price_1 *= 10
        bits_click += 1
    sleep(0.04)

while True:
    the_game