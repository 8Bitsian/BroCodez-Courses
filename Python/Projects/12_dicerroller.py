# Project 12: Rock Paper Scissor - Create a game that has users fight the machine
# Use 17 Notes
# Use the random library to have users fight a computer w/rock paper and scissors

# The random module will pick a random number from 1-6
import random

# To enter Unicode characters use forward slash and the code
# These are what I will use to make the dice: ● ┌ ─ ┐ │ └ ┘
print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# Each die will be a tuple that will be made w/5 lines:
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│         │",
        "│  ●   ●  │",
        "│         │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice? "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# Prints dice vertically
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)

# Prints dice horizontally
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end=(""))
    print()

for die in dice:
    total += die
print(f"Total: {total}")