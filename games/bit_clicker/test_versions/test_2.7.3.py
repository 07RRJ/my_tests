from time import sleep
from suffixes import millify
import os

os.system('cls')

number = 1

while True:
    sleep(0.01)
    formatted = millify(number, precision=2)
    print(formatted, len(str(number)))
    number *= 1000