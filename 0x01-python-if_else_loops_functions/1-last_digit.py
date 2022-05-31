#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = int(repr(number)[-1])
out = "Last digit of "
if lastdigit > 5:
    print(f"{out}{number} and is greater than 5")
elif lastdigit == 0:
    print(f"{out}{number} and is 0")
elif lastdigit < 6 and lastdigit != 0:
    print(f"{out}{number} is less than 6 and not 0")
