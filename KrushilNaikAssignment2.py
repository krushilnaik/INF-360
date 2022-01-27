# INF360 - Programming in Python
# Krushil Naik
# Assignment 2

import random

PLAY = True
print("-" * 10 + " Welcome, User! " + "-" * 10)
print()

while PLAY:
    age = int(input("Enter an age (type '0' to quit): "))
    print()

    if age == 0:
        break

    if age < 0 or age >= 100:
        print("You're lying, aren't you? Try again.")
        continue
    elif age >= 50:
        print("You're at least half a century old!")
    elif age >= 25:
        print("You're at least a quarter century old!")
    else:
        print("This game is rated 25+")
        break

    randomAge = random.randint(0, age - 1)

    MESSAGE = f"Wow, you're {age - randomAge} years older than someone who's {randomAge}!\n"

    print(MESSAGE)

    print("Now predicting your last 5 Christmas presents:")

    PRESENTS = [
        "Socks",
        "Gift card",
        "Coal",
        "Sweater",
        "Taco Bell"
    ]

    if age > 5:
        for i in range(5, 0, -1):
            print(f"{i}) {PRESENTS[i-1]}")

    print()
