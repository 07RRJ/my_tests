import humanize
from millify import millify
from time import sleep

number = 1234

while True:
    sleep(1)
    number *= 10
    mumanize_formatted = humanize.intword(number)  # Converts to "1.2 million"
    millify_formatted = millify(number, precision=2)  # Converts to "1.23M"
    print(mumanize_formatted, millify_formatted, number)